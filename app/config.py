"""Configuration settings for RAG service - Version 100% gratuite."""

from pydantic_settings import BaseSettings
from functools import lru_cache
import logging

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Environment
    env: str = "dev"
    debug: bool = False

    # KILL SWITCH - Blocks ALL writes in production
    # CRITICAL: This is the master switch for production safety
    ai_prod_write: bool = False

    # Weaviate Vector Database
    weaviate_url: str = "http://weaviate:8080"

    # Redis Cache
    redis_url: str = "redis://redis:6379"

    # API Security
    rag_api_key: str = ""

    # Knowledge Corpus
    knowledge_path: str = "/knowledge"

    # Embeddings (sentence-transformers - GRATUIT)
    embedding_model: str = "all-MiniLM-L6-v2"
    embedding_dimension: int = 384  # all-MiniLM-L6-v2 outputs 384 dimensions

    # RAG Settings
    retrieval_top_k: int = 5
    retrieval_alpha: float = 0.7  # 70% vectoriel, 30% BM25
    min_score_threshold: float = 0.70  # P1: Increased from 0.3 to reduce hallucinations
    min_results_required: int = 3  # P1: Minimum results for confident answer

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


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
