"""HTTP routes. Day 1: /health."""

from __future__ import annotations

from fastapi.testclient import TestClient

from crashdoc.api import app


def test_health_reports_ok_without_leaking_secrets(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-secret-value")
    monkeypatch.setenv("OPENAI_BASE_URL", "http://fake-secret-host.test/v1")
    from crashdoc.config import get_settings

    get_settings.cache_clear()
    try:
        response = TestClient(app).get("/health")
    finally:
        get_settings.cache_clear()
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok" and body["chat_model"] == "gemma-4-E4B-it"
    assert body["proxy_configured"] is True
    assert "secret" not in response.text
