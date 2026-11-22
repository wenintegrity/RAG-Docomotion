"""Local chat UI for the Docomotion RAG application.

Serves static/index.html and a JSON endpoint that runs the RAG chain from rag.py.
API keys stay on the server side (read from .env), never in the browser.

Usage:  python app.py   then open http://localhost:8000
"""

import time
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

from rag import rag_chain

STATIC_DIR = Path(__file__).parent / "static"
app = Flask(__name__)


@app.get("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")


@app.post("/api/chat")
def chat():
    question = (request.get_json(silent=True) or {}).get("question", "").strip()
    if not question:
        return jsonify(error="Please type a question."), 400
    if len(question) > 1000:
        return jsonify(error="Please keep the question under 1000 characters."), 400

    start = time.time()
    try:
        answer = str(rag_chain.invoke(question))
    except Exception as e:  # surface API errors (rate limits, overload) in the chat instead of a blank failure
        app.logger.exception("RAG chain failed")
        return jsonify(error=f"{type(e).__name__}: {str(e)[:300]}"), 502
    return jsonify(answer=answer, seconds=round(time.time() - start, 1))


if __name__ == "__main__":
    # threaded: the page stays responsive while an answer (~20 s) is being generated
    app.run(host="127.0.0.1", port=8000, threaded=True)
