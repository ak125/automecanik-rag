"""Prometheus metrics for Phase F.5 (ADR-031) runtime hardening.

Exposes :
- rag_admin_deprecated_route_hits_total : counter, calls to 410-Gone routes
- rag_admin_legacy_mode_calls_total     : counter, calls passing through
                                          when legacy mode is enabled
- rag_legacy_mode_enabled               : gauge, 1 when legacy mode active
- rag_legacy_mode_expires_in_seconds    : gauge, seconds remaining

Lazy-imported : if `prometheus_client` is not installed, metrics are no-ops
so the service still boots in minimal environments.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Optional

logger = logging.getLogger(__name__)

try:
    from prometheus_client import Counter, Gauge

    RAG_ADMIN_DEPRECATED_ROUTE_HITS = Counter(
        "rag_admin_deprecated_route_hits_total",
        "Calls to deprecated admin routes that returned 410 Gone (Phase F.5).",
        labelnames=("route", "method"),
    )

    RAG_ADMIN_LEGACY_MODE_CALLS = Counter(
        "rag_admin_legacy_mode_calls_total",
        "Calls to admin routes passed through because legacy mode is enabled (Phase F.5).",
        labelnames=("route", "method", "user_agent_class"),
    )

    RAG_LEGACY_MODE_ENABLED = Gauge(
        "rag_legacy_mode_enabled",
        "1 when Phase F.5 legacy mode is currently active, else 0.",
        labelnames=("reason_class",),
    )

    RAG_LEGACY_MODE_EXPIRES_IN_SECONDS = Gauge(
        "rag_legacy_mode_expires_in_seconds",
        "Seconds remaining until RAG_LEGACY_EXPIRES_AT (Phase F.5). "
        "Negative means already expired (service should fail boot).",
    )

    _PROMETHEUS_AVAILABLE = True
except ImportError:  # pragma: no cover
    logger.warning("prometheus_client not installed — F.5 metrics will be no-ops")
    RAG_ADMIN_DEPRECATED_ROUTE_HITS = None  # type: ignore[assignment]
    RAG_ADMIN_LEGACY_MODE_CALLS = None  # type: ignore[assignment]
    RAG_LEGACY_MODE_ENABLED = None  # type: ignore[assignment]
    RAG_LEGACY_MODE_EXPIRES_IN_SECONDS = None  # type: ignore[assignment]
    _PROMETHEUS_AVAILABLE = False


def record_deprecated_route_hit(route: str, method: str) -> None:
    """Increment the 410-Gone hits counter for a given route+method."""
    if RAG_ADMIN_DEPRECATED_ROUTE_HITS is not None:
        try:
            RAG_ADMIN_DEPRECATED_ROUTE_HITS.labels(route=route, method=method).inc()
        except Exception as exc:  # pragma: no cover
            logger.debug("Prometheus counter inc failed: %s", exc)


def record_legacy_mode_call(route: str, method: str, user_agent_class: str) -> None:
    """Increment the legacy-mode passthrough counter."""
    if RAG_ADMIN_LEGACY_MODE_CALLS is not None:
        try:
            RAG_ADMIN_LEGACY_MODE_CALLS.labels(
                route=route, method=method, user_agent_class=user_agent_class
            ).inc()
        except Exception as exc:  # pragma: no cover
            logger.debug("Prometheus counter inc failed: %s", exc)


def update_legacy_mode_gauges(
    is_active: bool,
    expires_at: Optional[datetime],
    reason_class: str = "none",
) -> None:
    """Refresh the legacy-mode gauges (call at boot + on each request boundary).

    `reason_class` should be derived from RAG_LEGACY_REASON (e.g. "INC", "P0",
    "P1") to bucket dashboards without leaking the full reason string.
    """
    if RAG_LEGACY_MODE_ENABLED is not None:
        try:
            RAG_LEGACY_MODE_ENABLED.labels(reason_class=reason_class).set(
                1 if is_active else 0
            )
        except Exception as exc:  # pragma: no cover
            logger.debug("Prometheus gauge set failed: %s", exc)

    if RAG_LEGACY_MODE_EXPIRES_IN_SECONDS is not None and expires_at is not None:
        try:
            now = datetime.now(timezone.utc)
            if expires_at.tzinfo is None:
                expires_at = expires_at.replace(tzinfo=timezone.utc)
            remaining = (expires_at - now).total_seconds()
            RAG_LEGACY_MODE_EXPIRES_IN_SECONDS.set(remaining)
        except Exception as exc:  # pragma: no cover
            logger.debug("Prometheus gauge set failed: %s", exc)


def classify_reason(reason: Optional[str]) -> str:
    """Return a low-cardinality bucket for `RAG_LEGACY_REASON`."""
    if not reason:
        return "none"
    reason_upper = reason.upper()
    for prefix in ("INC-", "P0-", "P1-", "P2-"):
        if prefix in reason_upper:
            return prefix.rstrip("-")
    return "other"
