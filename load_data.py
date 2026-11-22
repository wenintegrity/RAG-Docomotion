"""Load the Docomotion knowledge base (knowledge_base/*.md) into MongoDB Atlas.

Adapted from the MongoDB + LangChain RAG tutorial's PDF loader:
reads the Markdown articles exported by export_kb.py, drops near-empty ones,
tags each article with metadata using an LLM, splits it into chunks along its
headings, embeds the chunks with Voyage AI and stores them in Atlas, then makes
sure the Atlas Vector Search index exists.

Usage:  python load_data.py
"""

import hashlib
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import voyageai
import yaml
from langchain_core.documents import Document
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_voyageai import VoyageAIEmbeddings
from pydantic import BaseModel, Field
from pymongo import MongoClient

import key_param

KB_DIR = Path(__file__).parent / "knowledge_base"
DB_NAME = "docomotion_kb"
COLLECTION_NAME = "chunked_data"
INDEX_NAME = "vector_index"
TAGGING_MODEL = "gemini-3.5-flash-lite"  # ~1-2 s per article; tested fastest of the available Flash models
TAGGING_REQUESTS_PER_MINUTE = 12  # stays under the Gemini free-tier per-minute limit
TAGS_CACHE = Path(__file__).parent / "tags_cache.json"  # re-runs only re-tag articles whose text changed
EMBEDDING_MODEL = "voyage-3.5-lite"
EMBEDDING_DIMENSIONS = 1024  # voyage-3.5-lite default
# Voyage limits without a payment method on the Atlas/Voyage account: 3 requests and 10K tokens per minute.
# After adding a payment method, raise these (standard limits are far higher) and the load takes ~1 minute.
VOYAGE_REQUESTS_PER_MINUTE = 3
VOYAGE_TOKENS_PER_MINUTE = 10_000
CHUNK_SIZE = 1000            # tutorial used 500 for PDF paragraphs; KB how-to steps read better whole
CHUNK_OVERLAP = 150
MIN_CHUNK_CHARS = 50         # chunks with less text than this (besides headings) are dropped


def load_markdown_files() -> list[Document]:
    """Read each article; its YAML front matter (title, source, section, ...) becomes metadata."""
    docs = []
    for path in sorted(KB_DIR.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        _, front, body = text.split("---", 2)
        meta = yaml.safe_load(front)
        meta["last_modified"] = str(meta.get("last_modified", ""))
        meta["file"] = path.relative_to(KB_DIR).as_posix()
        docs.append(Document(page_content=body.strip(), metadata=meta))
    return docs


class ArticleMetadata(BaseModel):
    """Same schema as the tutorial's metadata tagger."""
    title: str = Field(description="Short title of the article")
    keywords: list[str] = Field(description="5-10 keywords a user might search for to find this article")
    hasCode: bool = Field(description="True if the article contains code, scripts, formulas or API payloads")


def tag_documents(docs: list[Document]) -> list[Document]:
    """LLM-generated metadata, as in the tutorial (whose tagger only works with OpenAI).
    Existing metadata wins, so the real page title from the front matter is kept."""
    llm = ChatGoogleGenerativeAI(
        model=TAGGING_MODEL,
        api_key=key_param.GEMINI_API_KEY,
        temperature=0,
        max_retries=6,
        rate_limiter=InMemoryRateLimiter(requests_per_second=TAGGING_REQUESTS_PER_MINUTE / 60),
    )
    tagger = llm.with_structured_output(ArticleMetadata)
    prompt = ("Extract metadata from this Docomotion knowledge base article "
              "(Docomotion is a document generation app for Salesforce).\n\n{article}")

    cache = json.loads(TAGS_CACHE.read_text(encoding="utf-8")) if TAGS_CACHE.exists() else {}
    lock = threading.Lock()

    def tag(doc: Document) -> Document:
        key = doc.metadata["file"] + ":" + hashlib.sha256(doc.page_content.encode()).hexdigest()[:16]
        extracted = cache.get(key)
        if extracted is None:
            extracted = tagger.invoke(prompt.format(article=doc.page_content)).model_dump()
            with lock:
                cache[key] = extracted
        return Document(page_content=doc.page_content, metadata={**extracted, **doc.metadata})

    cached_before = sum(
        1 for d in docs
        if d.metadata["file"] + ":" + hashlib.sha256(d.page_content.encode()).hexdigest()[:16] in cache
    )
    print(f"Tagging: {cached_before} articles from cache, {len(docs) - cached_before} to tag with {TAGGING_MODEL}")
    try:
        # The rate limiter paces the calls; a few workers keep the pipeline full while requests are in flight
        with ThreadPoolExecutor(max_workers=4) as pool:
            return list(pool.map(tag, docs))
    finally:
        # Save even if a call failed midway, so finished work is never redone
        TAGS_CACHE.write_text(json.dumps(cache, indent=1, ensure_ascii=False), encoding="utf-8")


def split_documents(docs: list[Document]) -> list[Document]:
    """Split on Markdown headings first, then by size. Each chunk is prefixed with its
    article title and heading path so it still makes sense when retrieved on its own."""
    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[("#", "h1"), ("##", "h2"), ("###", "h3")], strip_headers=False
    )
    size_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

    chunks = []
    for doc in docs:
        sections = header_splitter.split_text(doc.page_content)
        for section in size_splitter.split_documents(sections):
            text_only = "\n".join(l for l in section.page_content.splitlines() if not l.lstrip().startswith("#"))
            if len(text_only.strip()) < MIN_CHUNK_CHARS:
                continue  # heading-only fragment; its headings are repeated in the next chunk anyway
            headings = [section.metadata.get(h) for h in ("h2", "h3") if section.metadata.get(h)]
            breadcrumb = " > ".join([doc.metadata["title"], *headings])
            metadata = {**doc.metadata, "headings": breadcrumb}
            chunks.append(Document(page_content=f"{breadcrumb}\n\n{section.page_content}", metadata=metadata))
    return chunks


def store_chunks(chunks: list[Document], vector_store: MongoDBAtlasVectorSearch) -> None:
    """Embed and insert in batches that respect the Voyage per-minute request and token limits."""
    counter = voyageai.Client(api_key=key_param.VOYAGE_API_KEY, base_url=key_param.VOYAGE_API_BASE)
    # Free tier rejects single requests near the per-minute token limit (a 9K-token request failed,
    # 4.4K passed), so send smaller batches more often - same total throughput
    budget = int(VOYAGE_TOKENS_PER_MINUTE * 0.4)
    batches, batch, batch_tokens = [], [], 0
    for chunk in chunks:
        n = counter.count_tokens([chunk.page_content], model=EMBEDDING_MODEL)
        if batch and batch_tokens + n > budget:
            batches.append((batch, batch_tokens))
            batch, batch_tokens = [], 0
        batch.append(chunk)
        batch_tokens += n
    if batch:
        batches.append((batch, batch_tokens))

    total = sum(t for _, t in batches)
    print(f"Embedding {len(chunks)} chunks (~{total:,} tokens) in {len(batches)} batches")
    for i, (batch, tokens) in enumerate(batches, 1):
        start = time.time()
        for attempt in range(1, 6):
            try:
                vector_store.add_documents(batch)  # embedding happens before insert: a rejected batch stores nothing
                break
            except voyageai.error.RateLimitError:
                if attempt == 5:
                    raise
                print(f"  batch {i}: rate limited, waiting 60s (attempt {attempt}/5)")
                time.sleep(60)
        print(f"  batch {i}/{len(batches)}: {len(batch)} chunks, {tokens:,} tokens")
        if i < len(batches):
            # Wait long enough that neither the per-minute request nor token limit is exceeded
            pause = max(60 / VOYAGE_REQUESTS_PER_MINUTE, 60 * tokens / VOYAGE_TOKENS_PER_MINUTE)
            time.sleep(max(0.0, pause - (time.time() - start)) + 1)


def main():
    client = MongoClient(key_param.MONGODB_URI)
    collection = client[DB_NAME][COLLECTION_NAME]

    docs = load_markdown_files()
    cleaned_docs = [d for d in docs if len(d.page_content.split()) > 20]
    print(f"Loaded {len(docs)} articles, {len(cleaned_docs)} with enough text")

    t = time.time()
    tagged_docs = tag_documents(cleaned_docs)
    print(f"Tagged metadata with LLM in {time.time() - t:.0f}s")

    split_docs = split_documents(tagged_docs)
    print(f"Split into {len(split_docs)} chunks")

    embeddings = VoyageAIEmbeddings(
        voyage_api_key=key_param.VOYAGE_API_KEY,
        model=EMBEDDING_MODEL,
        base_url=key_param.VOYAGE_API_BASE,
    )

    # Re-running replaces the previous load instead of duplicating it
    deleted = collection.delete_many({}).deleted_count
    if deleted:
        print(f"Removed {deleted} chunks from the previous load")

    t = time.time()
    vector_store = MongoDBAtlasVectorSearch(collection=collection, embedding=embeddings, index_name=INDEX_NAME)
    store_chunks(split_docs, vector_store)
    print(f"Embedded and stored {collection.count_documents({})} chunks in "
          f"{DB_NAME}.{COLLECTION_NAME} in {time.time() - t:.0f}s")

    existing = {ix["name"] for ix in collection.list_search_indexes()}
    if INDEX_NAME in existing:
        print(f"Vector search index '{INDEX_NAME}' already exists")
    else:
        print(f"Creating vector search index '{INDEX_NAME}' (waits until it is ready)...")
        vector_store.create_vector_search_index(
            dimensions=EMBEDDING_DIMENSIONS,
            filters=["section", "hasCode"],
            wait_until_complete=300,
        )
        print("Index ready")

    client.close()


if __name__ == "__main__":
    main()
