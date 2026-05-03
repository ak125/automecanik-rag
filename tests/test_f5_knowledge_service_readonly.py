"""Phase F.5 (ADR-031) — L5 service-layer guard tests.

Verifies that all write methods on `knowledge_service` raise
``RagReadOnlyError`` when the service is in readonly mode. These guards
fire regardless of how the call is invoked (HTTP route, cron, queue
worker, M2M endpoint, ad-hoc Python script), providing defense-in-depth
beyond the L4 HTTP wrapper.
"""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from app.exceptions import RagReadOnlyError
from app.services import knowledge_service as ks_module


@pytest.fixture(autouse=True)
def _reset_settings_cache(monkeypatch):
    """Ensure each test starts from a fresh Settings (lru_cache)."""
    from app.config import get_settings
    get_settings.cache_clear()
    # default = readonly mode
    monkeypatch.delenv("RAG_LEGACY_ADMIN_ENABLED", raising=False)
    monkeypatch.delenv("RAG_WRITE_MODE", raising=False)
    yield
    get_settings.cache_clear()


def _make_service():
    """Construct a minimal KnowledgeService instance for guard testing.

    We don't need Weaviate or any IO — the assert_writeable() guard fires
    before any IO. So we just need an instance with the methods bound.
    """
    return ks_module.KnowledgeService.__new__(ks_module.KnowledgeService)


def test_create_document_blocked_in_readonly():
    svc = _make_service()
    with pytest.raises(RagReadOnlyError) as exc:
        svc.create_document(
            title="t", content="c", source_type="general", category="cat"
        )
    assert exc.value.operation == "create_document"


def test_update_document_blocked_in_readonly():
    svc = _make_service()
    with pytest.raises(RagReadOnlyError) as exc:
        svc.update_document(doc_id="abc", title="new")
    assert exc.value.operation == "update_document"


def test_delete_document_blocked_in_readonly():
    """delete_document checks readonly AFTER reading the doc, but the guard
    runs before any state mutation. Use a stub get_document that returns None
    so the test still hits the assert_writeable() call path."""
    svc = _make_service()
    # The assert_writeable call is the very first line — it fires before
    # get_document is consulted.
    with pytest.raises(RagReadOnlyError) as exc:
        svc.delete_document(doc_id="abc")
    assert exc.value.operation == "delete_document"


def test_promote_document_blocked_in_readonly():
    svc = _make_service()
    with pytest.raises(RagReadOnlyError) as exc:
        svc.promote_document(doc_id="abc")
    assert exc.value.operation == "promote_document"


def test_revive_tombstone_blocked_in_readonly():
    svc = _make_service()
    with pytest.raises(RagReadOnlyError) as exc:
        svc.revive_tombstone(source_uri="http://example/foo.md")
    assert exc.value.operation == "revive_tombstone"


def test_legacy_mode_allows_writes_through_l5(monkeypatch, tmp_path):
    """When legacy mode is properly configured, L5 guard does NOT fire.
    (Other layers may still validate ; this only proves the guard yields.)"""
    from datetime import datetime, timedelta, timezone

    monkeypatch.setenv("RAG_WRITE_MODE", "legacy")
    monkeypatch.setenv("RAG_LEGACY_REASON", "INC-2026-099")
    monkeypatch.setenv(
        "RAG_LEGACY_EXPIRES_AT",
        (datetime.now(timezone.utc) + timedelta(days=3)).isoformat(),
    )
    monkeypatch.setenv("RAG_LEGACY_AUTHORIZED_BY", "@reviewer")

    from app.config import get_settings
    get_settings.cache_clear()

    # The guard should now no-op. We don't go further because constructing
    # a real KnowledgeService requires Weaviate/Redis. We verify only that
    # assert_writeable does not raise.
    from app.dependencies import assert_writeable
    assert_writeable("test_op")  # must not raise
