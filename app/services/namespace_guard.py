"""
Namespace Guard - Security layer for RAG namespaces.

SECURITY CRITICAL:
- Namespaces are HARDCODED, not configurable via API or environment
- PROD chatbot can NEVER access dev:* or internal:* namespaces
- This prevents data leakage from development to production

Truth Levels:
- knowledge:* = L1-L4 verified content for chatbot
- internal:* = Code, audits, configs (DEV only)
"""

from typing import Optional
import logging

logger = logging.getLogger(__name__)


class NamespaceGuard:
    """
    Namespace security guard - HARDCODED namespaces.

    CRITICAL: These values are intentionally NOT configurable via .env
    to prevent accidental or malicious namespace exposure in production.
    """

    # Knowledge namespaces - accessible to chatbot
    KNOWLEDGE_NAMESPACES = [
        "knowledge:vehicle",
        "knowledge:diagnostic",
        "knowledge:faq",
        "knowledge:seo",
        "knowledge:guide",
        "knowledge:policy",
    ]

    # Internal namespaces - DEV/CI only, NEVER in production
    INTERNAL_NAMESPACES = [
        "internal:code",
        "internal:audits",
        "internal:configs",
        "internal:runbooks",
    ]

    # Actor permissions - HARDCODED
    ALLOWED_NAMESPACES = {
        # Production chatbot - ONLY knowledge namespaces
        "chatbot_prod": [
            "knowledge:vehicle",
            "knowledge:diagnostic",
            "knowledge:faq",
            "knowledge:guide",
            "knowledge:policy",
        ],
        # Production support - extended knowledge access
        "support_prod": KNOWLEDGE_NAMESPACES,
        # Dev agents - full access
        "agents_dev": KNOWLEDGE_NAMESPACES + INTERNAL_NAMESPACES,
        # CI/CD pipeline - full access for indexation
        "pipeline_ci": KNOWLEDGE_NAMESPACES + INTERNAL_NAMESPACES,
    }

    # Default namespace for production chatbot - HARDCODED
    PROD_CHATBOT_NAMESPACE = "knowledge:faq"

    def __init__(self, env: str = "dev"):
        """Initialize guard with environment."""
        self.env = env
        self._validate_env()

    def _validate_env(self):
        """Validate environment is recognized."""
        valid_envs = ["dev", "ci", "staging", "prod"]
        if self.env not in valid_envs:
            logger.warning(
                f"Unknown environment '{self.env}', defaulting to 'prod' (safest)"
            )
            self.env = "prod"

    def get_actor_for_env(self) -> str:
        """Get the actor based on current environment."""
        if self.env == "prod":
            return "chatbot_prod"
        elif self.env == "ci":
            return "pipeline_ci"
        else:
            return "agents_dev"

    def validate(self, namespace: str, actor: Optional[str] = None) -> bool:
        """
        Validate namespace access for an actor.

        Args:
            namespace: The namespace to access
            actor: The actor requesting access (defaults to env-based actor)

        Returns:
            True if access is allowed

        Raises:
            PermissionError if access is denied
        """
        if actor is None:
            actor = self.get_actor_for_env()

        allowed = self.ALLOWED_NAMESPACES.get(actor, [])

        # Check exact match
        if namespace in allowed:
            return True

        # Check wildcard match for internal namespaces
        if namespace.startswith("internal:") and actor in ["agents_dev", "pipeline_ci"]:
            if self.env in ["dev", "ci"]:
                return True

        # CRITICAL: PROD can NEVER access dev:* or internal:*
        if self.env == "prod":
            if namespace.startswith("dev:") or namespace.startswith("internal:"):
                logger.error(
                    f"SECURITY VIOLATION: PROD actor '{actor}' attempted "
                    f"to access forbidden namespace '{namespace}'"
                )
                raise PermissionError(
                    f"Namespace '{namespace}' is forbidden in production. "
                    f"Only knowledge:* namespaces are allowed."
                )

        # Default: deny and log
        logger.warning(
            f"Namespace access denied: actor='{actor}', namespace='{namespace}', env='{self.env}'"
        )
        raise PermissionError(
            f"Namespace '{namespace}' is not allowed for actor '{actor}'"
        )

    def get_default_namespace(self) -> str:
        """
        Get the default namespace for the current environment.

        PROD always returns knowledge:faq (safe default).
        DEV can access broader namespaces.
        """
        if self.env == "prod":
            return self.PROD_CHATBOT_NAMESPACE
        return "knowledge:faq"

    def get_allowed_namespaces(self, actor: Optional[str] = None) -> list[str]:
        """Get list of allowed namespaces for an actor."""
        if actor is None:
            actor = self.get_actor_for_env()
        return self.ALLOWED_NAMESPACES.get(actor, [])


# Singleton instance
_namespace_guard: Optional[NamespaceGuard] = None


def get_namespace_guard(env: Optional[str] = None) -> NamespaceGuard:
    """Get or create NamespaceGuard instance."""
    global _namespace_guard
    if _namespace_guard is None:
        from app.config import get_settings
        settings = get_settings()
        _namespace_guard = NamespaceGuard(env=env or settings.env)
    return _namespace_guard
