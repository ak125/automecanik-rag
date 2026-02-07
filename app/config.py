"""Configuration settings for RAG service - Version 100% gratuite.

QUARANTINE MODE (v1.0.0):
- Config YAML unique source de verite
- Fail-fast validation au demarrage
- Mode quarantine = RAG desactive jusqu'a validation
"""

from pydantic_settings import BaseSettings
from functools import lru_cache
from pathlib import Path
from typing import Optional, List
import logging
import yaml

logger = logging.getLogger(__name__)


def load_yaml_config() -> dict:
    """
    Load configuration from rag_config.yml.

    Priority: ENV vars > YAML config > defaults
    """
    config_path = Path(__file__).parent.parent / "rag_config.yml"
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
                logger.info(f"Loaded config from {config_path}")
                return config or {}
        except Exception as e:
            logger.error(f"Failed to load YAML config: {e}")
            return {}
    else:
        logger.warning(f"Config file not found: {config_path}")
        return {}


# Load YAML config once at module level
_yaml_config = load_yaml_config()


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Environment
    env: str = "dev"
    debug: bool = False

    # QUARANTINE MODE - New in v1.0.0
    mode: str = _yaml_config.get("mode", "quarantine")  # quarantine | active
    quarantine_enabled: bool = _yaml_config.get("quarantine", {}).get("enabled", True)
    quarantine_fail_fast: bool = _yaml_config.get("quarantine", {}).get("fail_fast", True)
    quarantine_on_failure: str = _yaml_config.get("quarantine", {}).get("on_failure", "exit")

    # KILL SWITCH - Blocks ALL writes in production
    # CRITICAL: This is the master switch for production safety
    ai_prod_write: bool = False

    # Weaviate Vector Database
    weaviate_url: str = "http://weaviate:8080"

    # Redis Cache
    redis_url: str = "redis://redis:6379"

    # API Security
    rag_api_key: str = ""

    # Claude LLM Configuration (V2 spec)
    anthropic_api_key: str = ""  # ANTHROPIC_API_KEY
    rag_model: str = "claude-3-5-sonnet-20241022"
    max_tokens: int = 1024
    temperature: float = 0.3

    # Knowledge Corpus
    knowledge_path: str = "/knowledge"

    # Embeddings (sentence-transformers - GRATUIT)
    embedding_model: str = "all-MiniLM-L6-v2"
    embedding_dimension: int = 384  # all-MiniLM-L6-v2 outputs 384 dimensions

    # RAG Settings (from rag_config.yml)
    retrieval_top_k: int = _yaml_config.get("retrieval", {}).get("top_k", 8)
    retrieval_alpha: float = _yaml_config.get("retrieval", {}).get("alpha", 0.7)
    min_score_threshold: float = _yaml_config.get("retrieval", {}).get("min_score_threshold", 0.70)
    min_results_required: int = _yaml_config.get("retrieval", {}).get("min_results_required", 3)

    # P0 SECURITY: CORS Configuration
    cors_origins: str = "*"  # Comma-separated list for PROD

    # P0 SECURITY: Rate Limiting
    rate_limit_rpm: int = 60  # Requests per minute

    # P0 SECURITY: Request Limits
    request_timeout: int = 30  # Seconds
    max_request_size: int = 1048576  # 1MB

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    # ========== Build Plane vs Runtime Plane ==========
    # Build Plane: DEV/CI - Can write (index, create, update, delete)
    # Runtime Plane: PROD - Read-only (search, chat)

    @property
    def is_build_plane(self) -> bool:
        """True if in Build Plane (DEV or CI) - writes allowed."""
        return self.env in ["dev", "ci", "staging"]

    @property
    def is_runtime_plane(self) -> bool:
        """True if in Runtime Plane (PROD) - read-only."""
        return self.env == "prod"

    def can_write(self) -> bool:
        """
        Check if write operations are allowed.

        CRITICAL SECURITY:
        - PROD: Always returns False (kill switch)
        - DEV/CI: Returns True only if ai_prod_write is True

        Returns:
            True if writes are allowed, False otherwise
        """
        # PROD is ALWAYS read-only
        if self.is_runtime_plane:
            if self.ai_prod_write:
                logger.warning(
                    "AI_PROD_WRITE=true in PROD - this should NEVER happen! "
                    "Writes are still blocked for safety."
                )
            return False

        # DEV/CI can write if explicitly enabled
        return self.is_build_plane

    def require_write_permission(self) -> None:
        """
        Raise error if writes are not allowed.

        Use this as a guard at the start of write operations.

        Raises:
            PermissionError if writes are blocked
        """
        if not self.can_write():
            raise PermissionError(
                f"Write operations are blocked in {self.env} environment. "
                f"Build Plane (dev/ci) required for writes. "
                f"Current: {'Runtime Plane' if self.is_runtime_plane else 'Build Plane'}"
            )

    # ========== QUARANTINE MODE ==========

    @property
    def is_quarantine_mode(self) -> bool:
        """True if RAG is in quarantine mode (validation required)."""
        return self.mode == "quarantine" and self.quarantine_enabled

    # ========== LANGGRAPH ==========

    @property
    def langgraph_enabled(self) -> bool:
        """True if LangGraph pipeline is enabled."""
        return _yaml_config.get("langgraph", {}).get("enabled", True)

    @property
    def gating_config(self) -> dict:
        """Get gating configuration from YAML."""
        return _yaml_config.get("gating", {
            "refuse_if_score_below": 0.70,
            "refuse_if_results_below": 3,
            "require_citations": True,
        })

    @property
    def refuse_message(self) -> str:
        """Get refusal message for insufficient results."""
        gating = self.gating_config
        return gating.get(
            "refuse_message_fr",
            "Je n'ai pas assez d'informations fiables pour repondre."
        )

    def validate_config(self) -> List[str]:
        """
        Validate configuration at startup.

        Returns:
            List of validation error messages (empty if valid)
        """
        errors = []

        # Check embedding dimension is expected value
        if self.embedding_dimension != 384:
            errors.append(
                f"Embedding dimension mismatch: {self.embedding_dimension} != 384 "
                f"(all-MiniLM-L6-v2 requires 384)"
            )

        # Check score threshold is reasonable
        if self.min_score_threshold < 0.5:
            errors.append(
                f"min_score_threshold too low: {self.min_score_threshold} < 0.5 "
                f"(risk of hallucinations)"
            )

        # Check API key exists (warning only)
        if not self.rag_api_key:
            logger.warning("RAG_API_KEY not set - endpoints will be unprotected")

        return errors

    def log_startup_config(self) -> None:
        """Log configuration at startup for debugging."""
        logger.info("=" * 50)
        logger.info("RAG SERVICE CONFIGURATION")
        logger.info("=" * 50)
        logger.info(f"Mode: {self.mode}")
        logger.info(f"Environment: {self.env}")
        logger.info(f"Quarantine Enabled: {self.quarantine_enabled}")
        logger.info(f"Quarantine Fail-Fast: {self.quarantine_fail_fast}")
        logger.info(f"LangGraph Enabled: {self.langgraph_enabled}")
        logger.info(f"Weaviate URL: {self.weaviate_url}")
        logger.info(f"Embedding Model: {self.embedding_model}")
        logger.info(f"Embedding Dimension: {self.embedding_dimension}")
        logger.info(f"Min Score Threshold: {self.min_score_threshold}")
        logger.info(f"Min Results Required: {self.min_results_required}")
        logger.info(f"Kill Switch (ai_prod_write): {self.ai_prod_write}")
        logger.info("=" * 50)


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
