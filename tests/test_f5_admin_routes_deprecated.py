"""Phase F.5 (ADR-031) — HTTP 410 Gone wrapper tests.

Verifies the L4 deprecation wrapper :
  - returns 410 Gone with RFC 8594/9745 headers in default readonly mode
  - includes a structured JSON body with `write_mode`, `replacement`, `adr`
  - lets requests pass through when legacy mode is properly configured
    (with `Sunset`/`Deprecation` headers still applied for transparency)
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.config import get_settings
from app.dependencies import block_if_readonly_admin


@pytest.fixture
def readonly_app(monkeypatch):
    """Build a tiny FastAPI app with one protected route, no env vars set."""
    for var in (
        "RAG_LEGACY_ADMIN_ENABLED",
        "RAG_WRITE_MODE",
        "RAG_LEGACY_REASON",
        "RAG_LEGACY_EXPIRES_AT",
        "RAG_LEGACY_AUTHORIZED_BY",
    ):
        monkeypatch.delenv(var, raising=False)
    get_settings.cache_clear()

    app = FastAPI()
    from fastapi import Depends

    @app.post(
        "/test/write",
        dependencies=[Depends(block_if_readonly_admin())],
    )
    async def write_op():
        return {"ok": True}

    return TestClient(app)


@pytest.fixture
def legacy_app(monkeypatch):
    """Build a tiny FastAPI app with legacy mode properly configured."""
    monkeypatch.setenv("RAG_LEGACY_ADMIN_ENABLED", "true")
    monkeypatch.setenv("RAG_LEGACY_REASON", "INC-2026-099")
    monkeypatch.setenv(
        "RAG_LEGACY_EXPIRES_AT",
        (datetime.now(timezone.utc) + timedelta(days=3)).isoformat(),
    )
    monkeypatch.setenv("RAG_LEGACY_AUTHORIZED_BY", "@reviewer")
    get_settings.cache_clear()

    app = FastAPI()
    from fastapi import Depends

    @app.post(
        "/test/write",
        dependencies=[Depends(block_if_readonly_admin())],
    )
    async def write_op():
        return {"ok": True}

    return TestClient(app)


def test_410_gone_in_readonly_mode(readonly_app):
    response = readonly_app.post("/test/write", json={})
    assert response.status_code == 410


def test_sunset_header_present(readonly_app):
    response = readonly_app.post("/test/write", json={})
    assert "Sunset" in response.headers
    assert "GMT" in response.headers["Sunset"]


def test_deprecation_header_true(readonly_app):
    response = readonly_app.post("/test/write", json={})
    assert response.headers.get("Deprecation") == "true"


def test_link_header_points_to_adr_031(readonly_app):
    response = readonly_app.post("/test/write", json={})
    link = response.headers.get("Link", "")
    assert "ADR-031" in link
    assert 'rel="successor-version"' in link


def test_response_body_structured(readonly_app):
    response = readonly_app.post("/test/write", json={})
    body = response.json()
    assert body["error"] == "deprecated"
    assert body["adr"] == "ADR-031"
    assert body["phase"] == "F.5"
    assert body["write_mode"] == "readonly"
    assert "replacement" in body
    assert "sunset_at" in body


def test_legacy_mode_passes_through(legacy_app):
    """In properly-configured legacy mode the request reaches the handler."""
    response = legacy_app.post("/test/write", json={})
    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_replacement_string_overridable(monkeypatch):
    """A custom `replacement` is reflected in the body."""
    for var in (
        "RAG_LEGACY_ADMIN_ENABLED",
        "RAG_WRITE_MODE",
        "RAG_LEGACY_REASON",
        "RAG_LEGACY_EXPIRES_AT",
        "RAG_LEGACY_AUTHORIZED_BY",
    ):
        monkeypatch.delenv(var, raising=False)
    get_settings.cache_clear()

    app = FastAPI()
    from fastapi import Depends

    custom = "automecanik-raw/sources → wiki/proposals → wiki/exports/rag"

    @app.post(
        "/test/pdf",
        dependencies=[Depends(block_if_readonly_admin(replacement=custom))],
    )
    async def pdf_op():
        return {"ok": True}

    client = TestClient(app)
    response = client.post("/test/pdf", json={})
    assert response.json()["replacement"] == custom
