"""Local chat UI for the Docomotion RAG application.

Serves static/index.html and a small JSON API that runs the RAG steps from
rag.py / retriever.py. Each question is handled in two calls so the page can
show the retrieved chunks before the answer is ready:

  POST /api/retrieve  {question}  -> embed question + vector search -> chunks, scores, timing
  POST /api/answer    {trace_id}  -> build prompt from those chunks + Gemini -> answer, timing
  GET  /api/stats                 -> live numbers and settings shown on the page

API keys stay on the server side (read from .env), never in the browser.

Usage:  python app.py   then open http://localhost:8000
"""

import threading
import time
import uuid
from collections import OrderedDict
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

import load_data
import rag
import retriever

STATIC_DIR = Path(__file__).parent / "static"
app = Flask(__name__)

# Retrieved chunks waiting for their answer step, keyed by trace id (kept small; local demo server)
_traces: OrderedDict[str, tuple[str, list]] = OrderedDict()
_traces_lock = threading.Lock()
MAX_TRACES = 100


def _error(message: str, status: int):
    return jsonify(error=message), status


@app.get("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")


@app.get("/api/stats")
def stats():
    collection = retriever.vector_store.collection
    try:
        chunks = collection.count_documents({})
        articles = len(collection.distinct("source"))
    except Exception as e:
        app.logger.exception("Stats query failed")
        return _error(f"Could not reach MongoDB Atlas: {type(e).__name__}", 502)
    return jsonify(
        articles=articles,
        chunks=chunks,
        chunk_size=load_data.CHUNK_SIZE,
        chunk_overlap=load_data.CHUNK_OVERLAP,
        tagging_model=load_data.TAGGING_MODEL,
        embedding_model=retriever.EMBEDDING_MODEL,
        embedding_dimensions=load_data.EMBEDDING_DIMENSIONS,
        top_k=rag.TOP_K,
        answer_model=rag.ANSWER_MODEL,
        database=f"{retriever.DB_NAME}.{retriever.COLLECTION_NAME}",
        index=retriever.INDEX_NAME,
    )


@app.post("/api/retrieve")
def retrieve():
    question = (request.get_json(silent=True) or {}).get("question", "").strip()
    if not question:
        return _error("Please type a question.", 400)
    if len(question) > 1000:
        return _error("Please keep the question under 1000 characters.", 400)

    start = time.time()
    try:
        results = retriever.query_data_with_scores(question, k=rag.TOP_K)
    except Exception as e:  # surface API errors (rate limits, network) in the page
        app.logger.exception("Retrieval failed")
        return _error(f"{type(e).__name__}: {str(e)[:300]}", 502)
    seconds = round(time.time() - start, 2)

    docs = [doc for doc, _ in results]
    trace_id = uuid.uuid4().hex
    with _traces_lock:
        _traces[trace_id] = (question, docs)
        while len(_traces) > MAX_TRACES:
            _traces.popitem(last=False)

    chunks = [
        {
            "score": round(score, 4),
            "headings": doc.metadata.get("headings", ""),
            "title": doc.metadata.get("title", ""),
            "section": doc.metadata.get("section", ""),
            "source": doc.metadata.get("source", ""),
            "keywords": doc.metadata.get("keywords", []),
            "text": doc.page_content.split("\n\n", 1)[-1],  # without the breadcrumb line
        }
        for doc, score in results
    ]
    return jsonify(trace_id=trace_id, seconds=seconds, chunks=chunks)


@app.post("/api/answer")
def answer():
    trace_id = (request.get_json(silent=True) or {}).get("trace_id", "")
    with _traces_lock:
        trace = _traces.pop(trace_id, None)
    if trace is None:
        return _error("This question expired, please ask it again.", 404)
    question, docs = trace

    prompt = rag.build_prompt(question, docs)
    start = time.time()
    try:
        text = rag.generate_answer(question, docs)
    except Exception as e:  # e.g. Gemini overloaded or rate limited
        app.logger.exception("Answer generation failed")
        return _error(f"{type(e).__name__}: {str(e)[:300]}", 502)
    return jsonify(
        answer=text,
        seconds=round(time.time() - start, 1),
        prompt_chars=len(prompt),
        prompt_tokens_estimate=len(prompt) // 4,
    )


if __name__ == "__main__":
    # threaded: the page stays responsive while an answer (~10-20 s) is being generated
    app.run(host="127.0.0.1", port=8000, threaded=True)
