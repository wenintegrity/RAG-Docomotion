"""Web app for the Docomotion RAG demo (runs locally and on Vercel).

Serves public/index.html and a small, stateless JSON API. Each question is handled in
two calls so the page can show the retrieved chunks before the answer is ready:

  POST /api/retrieve  {question}             -> embed question + vector search -> chunks (with ids), scores, timing
  POST /api/answer    {question, chunk_ids}  -> reload those chunks from Atlas + Gemini -> answer, timing
  GET  /api/stats                            -> live numbers and settings shown on the page

The answer step reloads chunks by id instead of trusting text sent by the browser, so only
knowledge base content can reach the prompt, and no state is kept between requests
(serverless instances can differ between the two calls).

API keys stay on the server (environment variables), never in the browser.

Local:   python app.py   then open http://localhost:8000
Vercel:  deployed automatically from GitHub; set the environment variables listed in key_param.REQUIRED
"""

import time
from pathlib import Path

from bson.errors import InvalidId
from flask import Flask, jsonify, request, send_from_directory

import config
import key_param

PUBLIC_DIR = Path(__file__).parent / "public"
# Serve the front end (public/index.html, public/css, public/js) at the site root, like Vercel's CDN does
app = Flask(__name__, static_folder=str(PUBLIC_DIR), static_url_path="")

MISSING = key_param.missing_settings()
if not MISSING:
    # Only import the RAG modules when configured: they connect to the APIs at import time
    import rag
    import retriever


def _error(message: str, status: int):
    return jsonify(error=message), status


def _config_error():
    return _error(
        "The server is missing these settings: " + ", ".join(MISSING)
        + ". Locally, add them to .env. On Vercel, add them under Project > Settings > "
          "Environment Variables, then redeploy.", 500)


@app.get("/")
def index():
    # On Vercel, public/index.html is served by the CDN before reaching this route
    return send_from_directory(PUBLIC_DIR, "index.html")


@app.get("/api/stats")
def stats():
    if MISSING:
        return _config_error()
    try:
        collection = retriever.vector_store.collection
        chunks = collection.count_documents({})
        articles = len(collection.distinct("source"))
        # Knowledge base areas for the "Search in" filter, with how much content each has
        sections = [
            {"name": s["_id"] or "", "chunks": s["chunks"], "articles": len(s["articles"])}
            for s in collection.aggregate([
                {"$group": {"_id": "$section", "chunks": {"$sum": 1}, "articles": {"$addToSet": "$source"}}},
                {"$sort": {"chunks": -1}},
            ])
        ]
    except Exception as e:
        app.logger.exception("Stats query failed")
        return _error(f"Could not reach MongoDB Atlas ({type(e).__name__}). "
                      "Check that the server's IP is allowed in Atlas Network Access.", 502)
    return jsonify(
        articles=articles,
        chunks=chunks,
        sections=sections,
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        tagging_model=config.TAGGING_MODEL,
        embedding_model=config.EMBEDDING_MODEL,
        embedding_dimensions=config.EMBEDDING_DIMENSIONS,
        top_k=config.TOP_K,
        answer_model=config.ANSWER_MODEL,
        database=f"{config.DB_NAME}.{config.COLLECTION_NAME}",
        index=config.INDEX_NAME,
    )


def _read_question(body: dict):
    question = str(body.get("question", "")).strip()
    if not question:
        return None, _error("Please type a question.", 400)
    if len(question) > 1000:
        return None, _error("Please keep the question under 1000 characters.", 400)
    return question, None


@app.post("/api/retrieve")
def retrieve():
    if MISSING:
        return _config_error()
    body = request.get_json(silent=True) or {}
    question, err = _read_question(body)
    if err:
        return err
    # Optional "Search in" filter: None/"all" = whole knowledge base, "" = top-level articles
    section = body.get("section")
    if section == "all":
        section = None
    if section is not None and (not isinstance(section, str) or len(section) > 80):
        return _error("Invalid section.", 400)

    start = time.time()
    try:
        results = retriever.query_data_with_scores(question, section=section, k=config.TOP_K)
    except Exception as e:  # surface API errors (rate limits, network) in the page
        app.logger.exception("Retrieval failed")
        return _error(f"{type(e).__name__}: {str(e)[:300]}", 502)

    chunks = [
        {
            "id": str(doc.metadata.get("_id", "")),
            "score": round(score, 4),
            "headings": doc.metadata.get("headings", ""),
            "section": doc.metadata.get("section", ""),
            "source": doc.metadata.get("source", ""),
            "keywords": doc.metadata.get("keywords", []),
            "text": doc.page_content.split("\n\n", 1)[-1],  # without the breadcrumb line
        }
        for doc, score in results
    ]
    return jsonify(seconds=round(time.time() - start, 2), chunks=chunks)


@app.post("/api/answer")
def answer():
    if MISSING:
        return _config_error()
    body = request.get_json(silent=True) or {}
    question, err = _read_question(body)
    if err:
        return err
    chunk_ids = body.get("chunk_ids", [])
    if not isinstance(chunk_ids, list) or len(chunk_ids) > config.TOP_K:
        return _error("Invalid chunk list.", 400)

    try:
        docs = retriever.get_chunks_by_ids([str(i) for i in chunk_ids])
    except InvalidId:
        return _error("Invalid chunk id.", 400)
    except Exception as e:
        app.logger.exception("Loading chunks failed")
        return _error(f"{type(e).__name__}: {str(e)[:300]}", 502)

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
