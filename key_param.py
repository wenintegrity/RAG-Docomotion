"""Connection settings from environment variables.

Locally they come from .env (git-ignored). On Vercel there is no .env: set them under
Project -> Settings -> Environment Variables.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")  # no-op when the file doesn't exist (e.g. on Vercel)

MONGODB_URI = os.getenv("MONGODB_URI")
VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY")
VOYAGE_API_BASE = os.getenv("VOYAGE_API_BASE")  # Atlas-issued Voyage keys use https://ai.mongodb.com/v1
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")    # Google AI Studio key
LLM_API_KEY = os.getenv("LLM_API_KEY")          # OpenAI (unused: account has no credits)

REQUIRED = ["MONGODB_URI", "VOYAGE_API_KEY", "GEMINI_API_KEY"]


def missing_settings() -> list[str]:
    """Names of required settings that are not set."""
    return [name for name in REQUIRED if not os.getenv(name)]
