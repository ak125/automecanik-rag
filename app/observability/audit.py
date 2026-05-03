"""Audit log emitter for Phase F.5 (ADR-031) legacy admin calls.

JSON-line format, append-only, RGPD-compliant:
  - IP hashed (sha256 + per-instance salt)
  - NEVER auth tokens, session IDs, X-Internal-Key, raw query strings
  - User-agent classified into {"browser","cli","cron","m2m"} bucket

File path defaults to /var/log/automecanik-rag/audit-legacy-admin.jsonl
(override via env RAG_AUDIT_LOG_PATH). Permissions enforced by deployment
(rag:rag 0640, group rag-readers for ops). Rotation by logrotate (90d).
"""

from __future__ import annotations

import hashlib
import json
import logging
import logging.handlers
import os
import secrets
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# Per-instance salt for IP hashing (rotates on service restart — defense
# against reverse rainbow attacks on a leaked log file). 32 bytes of urandom.
_INSTANCE_SALT = secrets.token_hex(32)

_AUDIT_LOG_PATH = os.getenv(
    "RAG_AUDIT_LOG_PATH", "/var/log/automecanik-rag/audit-legacy-admin.jsonl"
)

# Lazy file logger init — instantiated on first call to avoid boot failures
# when the directory doesn't exist yet (CI / test environments).
_audit_logger: Optional[logging.Logger] = None


def _get_audit_logger() -> logging.Logger:
    """Return (and lazy-init) a dedicated logger for audit lines.

    Uses WatchedFileHandler so logrotate's rename+create cycle is handled
    transparently without requiring a SIGHUP.
    """
    global _audit_logger
    if _audit_logger is not None:
        return _audit_logger

    audit = logging.getLogger("automecanik_rag.audit")
    audit.setLevel(logging.INFO)
    audit.propagate = False  # don't double-log to root

    try:
        log_path = Path(_AUDIT_LOG_PATH)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handler = logging.handlers.WatchedFileHandler(str(log_path), encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(message)s"))
        audit.addHandler(handler)
    except (OSError, PermissionError) as exc:
        # Fallback to stderr so audit isn't silently dropped in dev/test
        logger.warning(
            "F.5 audit: cannot open %s (%s) — falling back to stderr",
            _AUDIT_LOG_PATH,
            exc,
        )
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("[F.5 AUDIT] %(message)s"))
        audit.addHandler(handler)

    _audit_logger = audit
    return audit


def hash_ip(ip: Optional[str]) -> Optional[str]:
    """Return sha256(ip + salt) hex — RGPD-compliant pseudonym."""
    if not ip:
        return None
    return hashlib.sha256((ip + _INSTANCE_SALT).encode("utf-8")).hexdigest()[:32]


def classify_user_agent(ua: Optional[str]) -> str:
    """Bucket user-agent into low-cardinality classes for the audit log."""
    if not ua:
        return "unknown"
    ua_lower = ua.lower()
    if "curl" in ua_lower or "wget" in ua_lower or "httpie" in ua_lower:
        return "cli"
    if "python" in ua_lower or "go-http" in ua_lower or "node" in ua_lower:
        return "m2m"
    if "cron" in ua_lower:
        return "cron"
    if "mozilla" in ua_lower or "chrome" in ua_lower or "safari" in ua_lower or "firefox" in ua_lower:
        return "browser"
    return "other"


def emit_legacy_admin_call(
    *,
    route: str,
    method: str,
    user_id: Optional[str],
    ip: Optional[str],
    user_agent: Optional[str],
    reason: Optional[str],
    expires_at: Optional[datetime],
    authorized_by: Optional[str],
) -> None:
    """Append one structured JSON line to the audit log.

    Strict no-secret policy:
      - NEVER pass `Authorization` header values
      - NEVER pass `X-Internal-Key` or any secret token
      - NEVER pass query strings (may carry PII / tokens)
      - IPs are sha256-hashed before write (RGPD)
    """
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "request_id": str(uuid.uuid4()),
        "route": route,
        "method": method,
        "actor": {
            "user_id": user_id,
            "ip_hash": hash_ip(ip),
            "user_agent_class": classify_user_agent(user_agent),
        },
        "reason": reason,
        "expires_at": expires_at.isoformat() if expires_at else None,
        "authorized_by": authorized_by,
    }
    try:
        _get_audit_logger().info(json.dumps(record, separators=(",", ":")))
    except Exception as exc:  # pragma: no cover — never break the request
        logger.error("F.5 audit emit failed: %s", exc)
