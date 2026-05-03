"""FastAPI dependency wrappers for Phase F.5 (ADR-031) runtime hardening.

Exposes :
  - block_if_readonly_admin   : returns a JSONResponse(410) when the route
                                must be deprecated and legacy mode is OFF
  - require_writeable_service : raises RagReadOnlyError when the underlying
                                service-layer call must be blocked

The HTTP layer (L4) and service layer (L5) use these together for
defense-in-depth — service guards still fire even if a future refactor
forgets to wire the HTTP wrapper.
"""

from __future__ import annotations

from typing import Awaitable, Callable, Optional

from fastapi import Request, Response
from fastapi.responses import JSONResponse

from app.config import get_settings
from app.exceptions import RagReadOnlyError
from app.observability import audit, metrics


_VAULT_ADR_LINK = (
    "<https://github.com/ak125/governance-vault/blob/main/"
    "ledger/decisions/adr/ADR-031-four-layer-content-architecture.md>; "
    'rel="successor-version"'
)

_DEFAULT_REPLACEMENT = "automecanik-raw → automecanik-wiki/exports/rag → rag indexer"


def _build_410_response(route: str, method: str, replacement: str) -> JSONResponse:
    """Return the canonical 410 Gone response with RFC 8594/9745 headers."""
    settings = get_settings()
    body = {
        "error": "deprecated",
        "replacement": replacement,
        "adr": "ADR-031",
        "phase": "F.5",
        "sunset_at": settings.rag_admin_sunset_at,
        "write_mode": settings.rag_write_mode,
    }
    headers = {
        "Sunset": settings.admin_sunset_http_date,
        "Deprecation": "true",
        "Link": _VAULT_ADR_LINK,
        "X-Phase": "F.5",
    }
    metrics.record_deprecated_route_hit(route=route, method=method)
    return JSONResponse(status_code=410, content=body, headers=headers)


def block_if_readonly_admin(
    *,
    replacement: str = _DEFAULT_REPLACEMENT,
) -> Callable[[Request], Awaitable[Optional[Response]]]:
    """FastAPI dependency factory.

    Usage in a route :

        @router.post("/foo", dependencies=[Depends(block_if_readonly_admin())])
        def foo(...): ...

    Behaviour :
      - if rag_legacy_admin_enabled=False → return 410 Gone (request short-circuited)
      - if rag_legacy_admin_enabled=True  → emit audit log + counter, allow
        through (route handler runs normally)
    """

    async def _dep(request: Request) -> Optional[Response]:
        settings = get_settings()
        route = request.url.path
        method = request.method

        if not settings.rag_legacy_admin_enabled:
            # Route closed — return 410 directly.
            # Raising HTTPException would lose our custom headers, so we
            # return the JSONResponse and FastAPI will use it.
            return _build_410_response(route, method, replacement)

        # Legacy mode active — passthrough but emit audit log + counter
        ua = request.headers.get("user-agent")
        ua_class = audit.classify_user_agent(ua)
        metrics.record_legacy_mode_call(route=route, method=method, user_agent_class=ua_class)
        audit.emit_legacy_admin_call(
            route=route,
            method=method,
            user_id=request.headers.get("x-user-id"),  # set by upstream auth, never raw token
            ip=request.client.host if request.client else None,
            user_agent=ua,
            reason=settings.rag_legacy_reason,
            expires_at=settings.rag_legacy_expires_at,
            authorized_by=settings.rag_legacy_authorized_by,
        )
        return None  # let the route handler run

    return _dep


def assert_writeable(operation: str, *, replacement: str = _DEFAULT_REPLACEMENT) -> None:
    """L5 service-layer guard.

    Call from within `knowledge_service.{create,update,delete,promote,quarantine,
    unquarantine,revive_tombstone,ingest_pdf,...}_document` — fires regardless
    of whether the call originated from HTTP, cron, queue worker, or ad-hoc
    Python script.

    Raises RagReadOnlyError if rag_write_mode == "readonly".
    """
    settings = get_settings()
    if settings.rag_write_mode == "readonly":
        raise RagReadOnlyError(operation=operation, replacement=replacement)
