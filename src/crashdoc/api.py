"""FastAPI routes. Handlers only translate HTTP <-> service calls; no logic here (PLAN 6.0).

Run: uvicorn crashdoc.api:app --reload
"""

from __future__ import annotations

from fastapi import FastAPI

from crashdoc import service

app = FastAPI(title="NeoForge Log Doctor")


@app.get("/health")
def health() -> dict[str, object]:
    return service.health()
