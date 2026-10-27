"""Application logic behind the API routes (PLAN 6.0: api.py -> service.py -> llm/retrieval/agent)."""

from __future__ import annotations

from crashdoc.config import CHAT_MODEL, EMBED_MODEL, get_settings


def health() -> dict[str, object]:
    """Liveness plus the config facts worth seeing at a glance. Never includes the key or base URL."""
    settings = get_settings()
    return {
        "status": "ok",
        "chat_model": CHAT_MODEL,
        "embed_model": EMBED_MODEL,
        "proxy_configured": settings.proxy_configured,
        "replay": settings.replay,
    }
