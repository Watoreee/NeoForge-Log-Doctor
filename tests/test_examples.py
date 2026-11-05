"""The page's example logs must stay redacted and be served by the app."""

from fastapi.testclient import TestClient

from crashdoc.api import EXAMPLES_DIR, create_app
from crashdoc.redact import redact_text
from crashdoc.service import MAX_LOG_BYTES

NAMES = ("success_missing_dependency.log", "failure_version_mismatch.log")


def test_examples_are_already_redacted_and_within_the_size_limit():
    for name in NAMES:
        raw = (EXAMPLES_DIR / name).read_bytes()
        text = raw.decode("utf-8")
        assert redact_text(text).text == text, f"{name} still contains something the redactor would replace"
        assert len(raw) <= MAX_LOG_BYTES


def test_examples_are_served_and_the_page_has_the_two_buttons():
    client = TestClient(create_app(lambda log: iter(())))
    for name in NAMES:
        assert client.get(f"/examples/{name}").status_code == 200
    page = client.get("/").text
    assert "Success example" in page and "Known failure" in page
