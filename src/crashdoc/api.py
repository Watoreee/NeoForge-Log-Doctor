"""FastAPI routes. Handlers only translate HTTP <-> service calls; no logic here (PLAN 6.0).

Run: uvicorn crashdoc.api:app --reload
POST /diagnose streams Server-Sent Events: facts, tool_call, tool_result, final, error (structured events only,
never raw model tokens). GET /health. The web page is served at /.
"""

from __future__ import annotations

import json
from collections.abc import Iterator
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

from crashdoc import service
from crashdoc.config import REPO_ROOT

WEB_DIR = REPO_ROOT / "web"
EXAMPLES_DIR = REPO_ROOT / "data" / "examples"
BODY_SLACK = 4096  # JSON overhead allowed on top of the 200 KB log


def sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


def friendly_error(exc: Exception) -> str:
    """A short message for the page. No stack trace, never a key or URL."""
    name = type(exc).__name__
    if name == "ProxyNotConfiguredError":
        return "The language model is not configured on the server."
    if name == "CacheMissError":
        return "Replay mode: this log was not recorded, and no model call was made."
    if name == "RateLimitError":
        return "The model service is rate-limited right now. Try again in a minute."
    return f"Diagnosis failed ({name})."


def create_app(pipeline: service.Pipeline | None = None) -> FastAPI:
    run = pipeline or service.default_pipeline
    app = FastAPI(title="NeoForge Log Doctor")

    @app.get("/health")
    def health() -> dict[str, object]:
        return service.health()

    @app.post("/diagnose")
    async def diagnose(request: Request):
        body = await request.body()
        if len(body) > service.MAX_LOG_BYTES + BODY_SLACK:
            return JSONResponse({"error": "log too large (limit 200 KB)"}, status_code=413)
        try:
            log = json.loads(body).get("log", "") if body else ""
            log = service.check_input(log if isinstance(log, str) else "")
        except service.Rejected as rej:
            return JSONResponse({"error": rej.message}, status_code=rej.status)
        except (ValueError, AttributeError):
            return JSONResponse({"error": 'send JSON like {"log": "..."}'}, status_code=400)

        def stream() -> Iterator[str]:
            try:
                for event in run(log):
                    yield sse(event["event"], event["data"])
            except Exception as exc:  # the stream has started: report as an event, never a stack trace
                yield sse("error", {"message": friendly_error(exc)})

        return StreamingResponse(
            stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"}
        )

    @app.get("/")
    def index_page():
        page = Path(WEB_DIR / "index.html")
        return FileResponse(page) if page.is_file() else JSONResponse({"error": "web/index.html is missing"}, 404)

    if WEB_DIR.is_dir():
        app.mount("/web", StaticFiles(directory=WEB_DIR), name="web")
    if EXAMPLES_DIR.is_dir():  # two redacted sample logs for the page's example buttons
        app.mount("/examples", StaticFiles(directory=EXAMPLES_DIR), name="examples")
    return app


app = create_app()
