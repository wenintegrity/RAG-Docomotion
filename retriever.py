"""Retriever over the Docomotion knowledge base stored in MongoDB Atlas.

Embeds the question with Voyage AI (same model used at load time) and runs an
Atlas Vector Search for the most similar chunks, optionally pre-filtered by
knowledge base section or by whether the article contains code.

Usage:  python retriever.py "your question"
"""

import sys
import time

import voyageai
from langchain_core.documents import Document
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_voyageai import VoyageAIEmbeddings

import key_param

DB_NAME = "docomotion_kb"
COLLECTION_NAME = "chunked_data"
INDEX_NAME = "vector_index"
EMBEDDING_MODEL = "voyage-3.5-lite"  # must match the model used in load_data.py
TOP_K = 5

vector_store = MongoDBAtlasVectorSearch.from_connection_string(
    connection_string=key_param.MONGODB_URI,
    namespace=f"{DB_NAME}.{COLLECTION_NAME}",
    embedding=VoyageAIEmbeddings(
        model=EMBEDDING_MODEL,
        voyage_api_key=key_param.VOYAGE_API_KEY,
        base_url=key_param.VOYAGE_API_BASE,  # Atlas-issued Voyage keys use ai.mongodb.com
    ),
    index_name=INDEX_NAME,
)


def query_data(query: str, section: str | None = None, has_code: bool | None = None,
               k: int = TOP_K) -> list[Document]:
    """Return the k chunks most similar to the query.

    section:  limit to one KB area, e.g. "docomotion-for-administrators", "docomotion-for-designers",
              "docomotion-for-generators", "advanced-features", "connect", "release-notes"
    has_code: True = only articles with code/scripts, False = only articles without
    """
    pre_filter = {}
    if section is not None:
        pre_filter["section"] = {"$eq": section}
    if has_code is not None:
        pre_filter["hasCode"] = {"$eq": has_code}

    search_kwargs = {"k": k}
    if pre_filter:
        search_kwargs["pre_filter"] = pre_filter

    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs=search_kwargs)

    # Each query is embedded by Voyage; without a payment method the account allows only 3 requests/minute
    for attempt in range(1, 4):
        try:
            return retriever.invoke(query)
        except voyageai.error.RateLimitError:
            if attempt == 3:
                raise
            print("(Voyage rate limit reached - waiting 20s and retrying)")
            time.sleep(20)


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
