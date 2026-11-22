"""Connection settings, read from .env so no secrets live in code (.env is git-ignored)."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

MONGODB_URI = os.environ["MONGODB_URI"]
VOYAGE_API_KEY = os.environ["VOYAGE_API_KEY"]
VOYAGE_API_BASE = os.getenv("VOYAGE_API_BASE")  # Atlas-issued keys use https://ai.mongodb.com/v1
LLM_API_KEY = os.getenv("LLM_API_KEY")        # OpenAI (currently unused: account has no credits)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Google AI Studio key
