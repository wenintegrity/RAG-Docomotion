"""Answer generator for the Docomotion RAG application.

Retrieves the most relevant knowledge base chunks from MongoDB Atlas (see
retriever.py) and has Gemini answer the question using only those chunks.

Usage:  python rag.py "your question"
        python rag.py                    (runs the two lab test questions)
"""

import sys

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

import key_param
from retriever import query_data as retrieve_chunks  # same Voyage model + Atlas index used at load time

ANSWER_MODEL = "gemini-3.5-flash"  # ~20 s per answer; "gemini-3.5-flash-lite" is ~8 s with shorter answers
TOP_K = 5                          # chunks given to the model (lab used 3; our chunks are short sections)

template = """
Use the following pieces of context from the Docomotion knowledge base to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Do not answer the question if there is no given context.
Do not answer the question if it is not related to the context.
Do not give recommendations to anything other than Docomotion.
At the end of your answer, list the source URLs of the context you used.
Context:
{context}
Question: {question}
"""


def format_docs(docs: list[Document]) -> str:
    """Join the chunks, labelling each with its source page so the answer can cite it."""
    return "\n\n".join(f"[Source: {d.metadata['source']}]\n{d.page_content}" for d in docs)


custom_rag_prompt = PromptTemplate.from_template(template)

retrieve = {
    "context": RunnableLambda(lambda q: retrieve_chunks(q, k=TOP_K)) | format_docs,
    "question": RunnablePassthrough(),
}

llm = ChatGoogleGenerativeAI(
    model=ANSWER_MODEL,
    api_key=key_param.GEMINI_API_KEY,
    temperature=0,
    thinking_level="low",  # default (high) reasoning took ~2 minutes per answer with no better result
    max_retries=3,
)

response_parser = StrOutputParser()

rag_chain = retrieve | custom_rag_prompt | llm | response_parser


def query_data(query: str) -> str:
    answer = rag_chain.invoke(query)
    print(answer)
    return answer


if __name__ == "__main__":
    if len(sys.argv) > 1:
        query_data(" ".join(sys.argv[1:]))
    else:
        # Test with a relevant query
        question = "Which permission sets does Docomotion support, and what can a Designer do?"
        print(f"Running query: {question}")
        query_data(question)

        print("=========================================================")

        # Test with an irrelevant query
        question = "Why is the sky blue?"
        print(f"Running query: {question}")
        query_data(question)
