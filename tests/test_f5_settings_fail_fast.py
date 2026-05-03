"""Phase F.5 (ADR-031) — Pydantic v2 settings fail-fast tests.

Verifies the strict legacy-mode validator refuses invalid configurations
at boot time so the service cannot start in an unsafe state.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest
from pydantic import ValidationError

from app.config import Settings


def _future_iso(days: int) -> str:
    """Return an ISO-8601 datetime that many days from now (UTC)."""
    return (datetime.now(timezone.utc) + timedelta(days=days)).isoformat()


def test_default_settings_are_readonly(monkeypatch):
    """Without any env var, settings default to safe readonly mode."""
    for var in (
        "RAG_LEGACY_ADMIN_ENABLED",
        "RAG_WRITE_MODE",
        "RAG_LEGACY_REASON",
        "RAG_LEGACY_EXPIRES_AT",
        "RAG_LEGACY_AUTHORIZED_BY",
    ):
        monkeypatch.delenv(var, raising=False)

    s = Settings()
    assert s.rag_write_mode == "readonly"
    assert s.is_rag_readonly is True
    assert s.rag_legacy_admin_enabled is False
    assert s.rag_index_source == "wiki_exports_only"


def test_invalid_write_mode_refused(monkeypatch):
    monkeypatch.setenv("RAG_WRITE_MODE", "anything-not-in-literal")
    with pytest.raises(ValidationError):
        Settings()


def test_legacy_without_reason_refused(monkeypatch):
    monkeypatch.setenv("RAG_LEGACY_ADMIN_ENABLED", "true")
    with pytest.raises(ValidationError) as exc:
        Settings()
    assert "REASON" in str(exc.value)


def test_legacy_without_expires_at_refused(monkeypatch):
    monkeypatch.setenv("RAG_LEGACY_ADMIN_ENABLED", "true")
    monkeypatch.setenv("RAG_LEGACY_REASON", "INC-2026-099")
    with pytest.raises(ValidationError) as exc:
        Settings()
    assert "EXPIRES_AT" in str(exc.value)


def test_legacy_without_authorized_by_refused(monkeypatch):
    monkeypatch.setenv("RAG_LEGACY_ADMIN_ENABLED", "true")
    monkeypatch.setenv("RAG_LEGACY_REASON", "INC-2026-099")
    monkeypatch.setenv("RAG_LEGACY_EXPIRES_AT", _future_iso(7))
    with pytest.raises(ValidationError) as exc:
        Settings()
    assert "AUTHORIZED_BY" in str(exc.value)


def test_legacy_expires_at_in_past_refused(monkeypatch):
    monkeypatch.setenv("RAG_LEGACY_ADMIN_ENABLED", "true")
    monkeypatch.setenv("RAG_LEGACY_REASON", "INC-2026-099")
    monkeypatch.setenv("RAG_LEGACY_EXPIRES_AT", _future_iso(-1))
    monkeypatch.setenv("RAG_LEGACY_AUTHORIZED_BY", "@reviewer")
    with pytest.raises(ValidationError) as exc:
        Settings()
    assert "in the past" in str(exc.value)


def test_legacy_expires_at_too_far_refused(monkeypatch):
    """+15 days exceeds the 14-day anti-permanence window."""
    monkeypatch.setenv("RAG_LEGACY_ADMIN_ENABLED", "true")
    monkeypatch.setenv("RAG_LEGACY_REASON", "INC-2026-099")
    monkeypatch.setenv("RAG_LEGACY_EXPIRES_AT", _future_iso(15))
    monkeypatch.setenv("RAG_LEGACY_AUTHORIZED_BY", "@reviewer")
    with pytest.raises(ValidationError) as exc:
        Settings()
    assert "+14d" in str(exc.value)


def test_legacy_valid_accepted(monkeypatch):
    """All 4 vars present and within window → accepted."""
    monkeypatch.setenv("RAG_LEGACY_ADMIN_ENABLED", "true")
    monkeypatch.setenv("RAG_LEGACY_REASON", "INC-2026-099")
    monkeypatch.setenv("RAG_LEGACY_EXPIRES_AT", _future_iso(7))
    monkeypatch.setenv("RAG_LEGACY_AUTHORIZED_BY", "@reviewer")

    s = Settings()
    assert s.rag_legacy_admin_enabled is True
    assert s.rag_legacy_reason == "INC-2026-099"
    assert s.rag_legacy_authorized_by == "@reviewer"
    assert s.rag_legacy_expires_at is not None


def test_write_mode_legacy_also_requires_4_vars(monkeypatch):
    """RAG_WRITE_MODE=legacy alone (without _enabled) also triggers validator."""
    monkeypatch.setenv("RAG_WRITE_MODE", "legacy")
    with pytest.raises(ValidationError) as exc:
        Settings()
    assert "REASON" in str(exc.value)


def test_admin_sunset_http_date_format(monkeypatch):
    """Sunset date is exposed in RFC 7231 HTTP format."""
    monkeypatch.delenv("RAG_LEGACY_ADMIN_ENABLED", raising=False)
    monkeypatch.delenv("RAG_WRITE_MODE", raising=False)
    s = Settings()
    s.rag_admin_sunset_at = "2026-06-03"
    # Should look like "Wed, 03 Jun 2026 00:00:00 GMT"
    assert "GMT" in s.admin_sunset_http_date
    assert "Jun" in s.admin_sunset_http_date or "Jun 2026" in s.admin_sunset_http_date
