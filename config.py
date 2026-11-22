"""Settings shared by the loader (load_data.py) and the web app (retriever.py, rag.py, app.py).

Kept in its own module so the web app doesn't import the loader and its extra dependencies.
"""

# MongoDB Atlas
DB_NAME = "docomotion_kb"
COLLECTION_NAME = "chunked_data"
INDEX_NAME = "vector_index"

# Embeddings - the question must be embedded with the same model as the chunks
EMBEDDING_MODEL = "voyage-3.5-lite"
EMBEDDING_DIMENSIONS = 1024  # voyage-3.5-lite default

# Chunking (load time)
CHUNK_SIZE = 1000   # tutorial used 500 for PDF paragraphs; KB how-to steps read better whole
CHUNK_OVERLAP = 150

# LLMs
TAGGING_MODEL = "gemini-3.5-flash-lite"  # metadata tagging at load time; ~1-2 s per article
ANSWER_MODEL = "gemini-3.5-flash"        # ~20 s per answer; "gemini-3.5-flash-lite" is ~8 s with shorter answers

# Retrieval
TOP_K = 5  # chunks given to the model (lab used 3; our chunks are short sections)
