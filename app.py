"""Deployment entrypoint (Vercel looks for `app` in ./app.py).

The package lives in src/ and is not installed on the platform, so put src/ on the path and re-export the FastAPI app.
Locally, `uvicorn crashdoc.api:app` is still the way to run it (README).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from crashdoc.api import app  # noqa: E402

__all__ = ["app"]
