"""Retriever over the Docomotion knowledge base stored in MongoDB Atlas.

Embeds the question with Voyage AI (same model used at load time) and runs an
Atlas Vector Search for the most similar chunks, optionally pre-filtered by
knowledge base section or by whether the article contains code.

Usage:  python retriever.py "your question"
"""

import sys
import time

import voyageai
from bson import ObjectId
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_mongodb import MongoDBAtlasVectorSearch

import key_param
from config import COLLECTION_NAME, DB_NAME, EMBEDDING_MODEL, INDEX_NAME, TOP_K


class VoyageEmbeddings(Embeddings):
    """Minimal Voyage AI embeddings for querying.

    langchain_voyageai.VoyageAIEmbeddings tokenizes every text before sending it, which downloads
    a tokenizer from Hugging Face at runtime - that fails on read-only serverless filesystems
    (Vercel). The plain voyageai client call needs no tokenizer.
    """

    def __init__(self, model: str, api_key: str, base_url: str | None = None):
        self.model = model
        self.client = voyageai.Client(api_key=api_key, base_url=base_url)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self.client.embed(texts, model=self.model, input_type="document").embeddings

    def embed_query(self, text: str) -> list[float]:
        return self.client.embed([text], model=self.model, input_type="query").embeddings[0]


vector_store = MongoDBAtlasVectorSearch.from_connection_string(
    connection_string=key_param.MONGODB_URI,
    namespace=f"{DB_NAME}.{COLLECTION_NAME}",
    embedding=VoyageEmbeddings(
        model=EMBEDDING_MODEL,  # must match the model used in load_data.py
        api_key=key_param.VOYAGE_API_KEY,
        base_url=key_param.VOYAGE_API_BASE,  # Atlas-issued Voyage keys use ai.mongodb.com
    ),
    index_name=INDEX_NAME,
)


def get_chunks_by_ids(ids: list[str]) -> list[Document]:
    """Load stored chunks by their _id, in the given order (used by the web app's answer step)."""
    object_ids = [ObjectId(i) for i in ids]
    found = {str(d["_id"]): d for d in vector_store.collection.find({"_id": {"$in": object_ids}},
                                                                     {"embedding": 0})}
    docs = []
    for i in ids:
        d = found.get(i)
        if d:
            metadata = {k: v for k, v in d.items() if k not in ("_id", "text")}
            docs.append(Document(page_content=d["text"], metadata=metadata))
    return docs


def _build_pre_filter(section: str | None, has_code: bool | None) -> dict:
    pre_filter = {}
    if section is not None:
        pre_filter["section"] = {"$eq": section}
    if has_code is not None:
        pre_filter["hasCode"] = {"$eq": has_code}
    return pre_filter


def _with_rate_limit_retry(fn):
    # Each query is embedded by Voyage; without a payment method the account allows only 3 requests/minute
    for attempt in range(1, 4):
        try:
            return fn()
        except voyageai.error.RateLimitError:
            if attempt == 3:
                raise
            print("(Voyage rate limit reached - waiting 20s and retrying)")
            time.sleep(20)


def query_data(query: str, section: str | None = None, has_code: bool | None = None,
               k: int = TOP_K) -> list[Document]:
    """Return the k chunks most similar to the query.

    section:  limit to one KB area, e.g. "docomotion-for-administrators", "docomotion-for-designers",
              "docomotion-for-generators", "advanced-features", "connect", "release-notes"
    has_code: True = only articles with code/scripts, False = only articles without
    """
    search_kwargs = {"k": k}
    pre_filter = _build_pre_filter(section, has_code)
    if pre_filter:
        search_kwargs["pre_filter"] = pre_filter

    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs=search_kwargs)
    return _with_rate_limit_retry(lambda: retriever.invoke(query))


def query_data_with_scores(query: str, section: str | None = None, has_code: bool | None = None,
                           k: int = TOP_K) -> list[tuple[Document, float]]:
    """Same search as query_data, also returning each chunk's similarity score (0-1, higher = closer)."""
    pre_filter = _build_pre_filter(section, has_code) or None
    return _with_rate_limit_retry(
        lambda: vector_store.similarity_search_with_score(query, k=k, pre_filter=pre_filter)
    )


def print_results(query: str, results: list[Document]) -> None:
    print(f"\nQuery: {query}\n")
    for i, doc in enumerate(results, 1):
        text = doc.page_content.split("\n\n", 1)[-1]  # drop the breadcrumb line, shown separately
        snippet = " ".join(text.split())[:200]
        print(f"{i}. {doc.metadata['headings']}")
        print(f"   {doc.metadata['source']}")
        print(f"   {snippet}...\n")


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "How do I add a Generate button to a Salesforce record page?"
    print_results(question, query_data(question))
