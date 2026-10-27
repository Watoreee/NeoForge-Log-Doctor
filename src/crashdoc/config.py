"""Configuration: fixed constants plus settings read from environment variables only (PLAN 2).

A local, git-ignored `.env` is copied into the environment by python-dotenv for convenience;
real environment variables always win. Nothing here ever prints the key or base URL.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]

# --- Models (docs/proxy-notes.md) ---
CHAT_MODEL = "gemma-4-E4B-it"  # fixed by the assignment; never change
EMBED_MODEL = "bge-m3"  # served by the proxy, 1024-dim
EMBED_DIM = 1024
EMBED_BATCH_SIZE = 32  # 64 tested OK; 32 keeps each call ~30 s

# Chunking tokenizer: bge-m3's own tokenizer files only (no weights), pinned for reproducibility.
TOKENIZER_REPO = "BAAI/bge-m3"
TOKENIZER_REVISION = "5617a9f61b028005a4858fdac845db406aefb181"

# --- Budgets (docs/decisions.md) ---
MAX_INPUT_BYTES = 10 * 1024 * 1024  # larger pasted logs get HTTP 413
LOG_TOKEN_BUDGET = 6_000  # max Gemma tokens of log text sent to the LLM
GEMMA_UNDERCOUNT_FACTOR = 1.25  # cl100k undercounts Gemma by ~21%; 1.25 adds margin

# --- Proxy calls ---
REQUEST_TIMEOUT_S = 180
MAX_RETRIES = 6  # retries on 429 / transient errors before giving up
BACKOFF_BASE_S = 2.0  # exponential backoff when no retry-after header is sent
BACKOFF_MAX_S = 60.0


@dataclass(frozen=True)
class Settings:
    """Everything that varies between machines or runs."""

    api_key: str | None
    base_url: str | None
    cache_dir: Path
    replay: bool  # CRASHDOC_REPLAY=1: serve only from cache, never call the proxy (PLAN 6.9)

    @property
    def proxy_configured(self) -> bool:
        return bool(self.api_key and self.base_url)


def _env_flag(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes"}


def load_settings() -> Settings:
    """Read settings from the environment (after loading .env, if present)."""
    load_dotenv(REPO_ROOT / ".env", override=False)
    cache_dir = os.environ.get("CRASHDOC_CACHE_DIR", "").strip()
    return Settings(
        api_key=os.environ.get("OPENAI_API_KEY", "").strip() or None,
        base_url=os.environ.get("OPENAI_BASE_URL", "").strip() or None,
        cache_dir=Path(cache_dir) if cache_dir else REPO_ROOT / "eval" / "cache",
        replay=_env_flag("CRASHDOC_REPLAY"),
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Process-wide settings, read once."""
    return load_settings()


def use_os_trust_store() -> None:
    """Verify TLS against the OS certificate store (certifi fails on some networks; see decisions.md)."""
    try:
        import truststore

        truststore.inject_into_ssl()
    except ImportError:
        pass
