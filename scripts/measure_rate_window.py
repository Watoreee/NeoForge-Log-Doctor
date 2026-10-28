"""Measure the proxy's rate-limit window with exactly 3 tiny embedding calls (requests, no tokens).

Each response's x-ratelimit-api_key-remaining-requests counts the requests still inside the window.
Read at t=0, t=+70 s and ~10 min later: if every read shows limit-1, the earlier calls had already
left the window, so the window is shorter than the gap. Results: docs/proxy-notes.md.

Usage: python scripts/measure_rate_window.py
"""

from __future__ import annotations

import json
import time
from datetime import UTC, datetime

import openai

from crashdoc.config import EMBED_MODEL, get_settings, use_os_trust_store


def read_headers(client: openai.OpenAI, label: str) -> dict:
    resp = client.embeddings.with_raw_response.create(model=EMBED_MODEL, input=["ping"])
    headers = {k: v for k, v in resp.headers.items() if "ratelimit" in k.lower() or "reset" in k.lower()}
    return {"label": label, "utc": datetime.now(UTC).isoformat(timespec="seconds"), "headers": headers}


def main() -> None:
    use_os_trust_store()
    settings = get_settings()
    client = openai.OpenAI(api_key=settings.api_key, base_url=settings.base_url, max_retries=0)
    t0 = time.monotonic()
    for label, at in (("t+0s", 0), ("t+70s", 70), ("t+670s", 670)):
        time.sleep(max(0.0, at - (time.monotonic() - t0)))
        print(json.dumps(read_headers(client, label)), flush=True)


if __name__ == "__main__":
    main()
