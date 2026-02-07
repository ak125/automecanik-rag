"""Kill Switch - BUILD Plane Enforcement.

CRITICAL SECURITY COMPONENT

This module enforces that the RAG Orchestrator can ONLY run in BUILD plane
environments (dev, ci, staging). Production environments are STRICTLY BLOCKED.

The kill switch uses HARDCODED environment lists - NOT environment variables -
to prevent any bypass attempts.

Usage:
    from orchestrator.kill_switch import enforce_build_plane

    # At the start of any write operation
    enforce_build_plane()  # Raises BuildPlaneViolation if in PROD

Rules:
    - ALLOWED: dev, ci, staging
    - BLOCKED: prod, production (and any unknown environment)
    - Default (empty ENV): BLOCKED for safety
"""

import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class BuildPlaneViolation(Exception):
    """Raised when attempting write operations outside BUILD plane."""

    def __init__(self, message: str, environment: str = "unknown"):
        self.environment = environment
        super().__init__(f"BUILD PLANE VIOLATION: {message} (env={environment})")


# HARDCODED - These values are NOT configurable via environment variables
# This is intentional to prevent bypass via .env manipulation
ALLOWED_ENVIRONMENTS = frozenset(["dev", "ci", "staging", "development", "test"])
BLOCKED_ENVIRONMENTS = frozenset(["prod", "production", "live"])


def get_current_environment() -> str:
    """Get the current environment from ENV variable.

    Returns:
        Environment string (lowercase), or "unknown" if not set.
    """
    return os.getenv("ENV", "").lower().strip() or "unknown"


def is_build_plane(env: Optional[str] = None) -> bool:
    """Check if current environment is in BUILD plane.

    Args:
        env: Optional environment to check. If None, uses ENV variable.

    Returns:
        True if in BUILD plane (dev/ci/staging), False otherwise.
    """
    if env is None:
        env = get_current_environment()
    else:
        env = env.lower().strip()

    return env in ALLOWED_ENVIRONMENTS


def is_runtime_plane(env: Optional[str] = None) -> bool:
    """Check if current environment is in RUNTIME plane (PROD).

    Args:
        env: Optional environment to check. If None, uses ENV variable.

    Returns:
        True if in RUNTIME plane (prod), False otherwise.
    """
    if env is None:
        env = get_current_environment()
    else:
        env = env.lower().strip()

    return env in BLOCKED_ENVIRONMENTS


def enforce_build_plane(operation: str = "write") -> None:
    """Enforce that we're in BUILD plane. Raises exception if not.

    This is the main guard function that should be called at the start
    of any write operation (index, create, update, delete).

    Args:
        operation: Description of the operation being attempted.

    Raises:
        BuildPlaneViolation: If not in BUILD plane.

    Example:
        >>> enforce_build_plane("index documents")  # OK in dev
        >>> enforce_build_plane("index documents")  # Raises in prod
    """
    env = get_current_environment()

    # BLOCKED environments - explicit production
    if env in BLOCKED_ENVIRONMENTS:
        logger.critical(
            f"KILL SWITCH ACTIVATED: Attempted '{operation}' in PROD environment. "
            f"Orchestrator MUST run in BUILD plane (dev/ci). Current: {env}"
        )
        raise BuildPlaneViolation(
            f"Orchestrator cannot perform '{operation}' in PRODUCTION. "
            f"Write operations are only allowed in BUILD plane (dev/ci/staging).",
            environment=env,
        )

    # UNKNOWN environments - fail closed for safety
    if env not in ALLOWED_ENVIRONMENTS:
        logger.critical(
            f"KILL SWITCH ACTIVATED: Unknown environment '{env}'. "
            f"Orchestrator requires explicit BUILD plane environment."
        )
        raise BuildPlaneViolation(
            f"Unknown environment '{env}'. "
            f"Set ENV to one of: {', '.join(sorted(ALLOWED_ENVIRONMENTS))}",
            environment=env,
        )

    # BUILD plane - allowed
    logger.info(f"BUILD plane confirmed (env={env}). Operation '{operation}' allowed.")


def validate_environment_config() -> dict:
    """Validate environment configuration and return status.

    Returns:
        Dict with validation results for diagnostics.
    """
    env = get_current_environment()

    return {
        "environment": env,
        "is_build_plane": is_build_plane(env),
        "is_runtime_plane": is_runtime_plane(env),
        "is_unknown": env not in ALLOWED_ENVIRONMENTS and env not in BLOCKED_ENVIRONMENTS,
        "allowed_environments": list(sorted(ALLOWED_ENVIRONMENTS)),
        "blocked_environments": list(sorted(BLOCKED_ENVIRONMENTS)),
        "write_operations_allowed": is_build_plane(env),
        "message": (
            "OK - BUILD plane, writes allowed"
            if is_build_plane(env)
            else "BLOCKED - Not in BUILD plane, writes denied"
        ),
    }


# Decorator for functions that require BUILD plane
def require_build_plane(func):
    """Decorator to enforce BUILD plane before executing a function.

    Usage:
        @require_build_plane
        def index_documents():
            # This will only run in BUILD plane
            pass
    """

    def wrapper(*args, **kwargs):
        enforce_build_plane(operation=func.__name__)
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


if __name__ == "__main__":
    # Quick validation when run directly
    import json

    print("=" * 60)
    print("KILL SWITCH VALIDATION")
    print("=" * 60)
    status = validate_environment_config()
    print(json.dumps(status, indent=2))
    print("=" * 60)

    try:
        enforce_build_plane("self-test")
        print("Result: BUILD plane confirmed - writes ALLOWED")
    except BuildPlaneViolation as e:
        print(f"Result: {e}")
