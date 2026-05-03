"""Configuration settings for RAG service - Version 100% gratuite.

QUARANTINE MODE (v1.0.0):
- Config YAML unique source de verite
- Fail-fast validation au demarrage
- Mode quarantine = RAG desactive jusqu'a validation
"""

from pydantic_settings import BaseSettings
from pydantic import model_validator
from functools import lru_cache
from pathlib import Path
from typing import Optional, List, Literal
from datetime import datetime, timedelta, timezone
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

    # ========== Phase F.5 — ADR-031 Runtime Hardening ==========
    # Le RAG devient consumer/indexer readonly. Source canonique = automecanik-wiki/exports/rag/
    # Voir governance-vault ledger/knowledge/adr-031-migration-runbook §Phase F.5

    # Mode d'écriture documentaire (orthogonal à can_write() qui gère indexation derivative)
    # readonly = défaut, bloque CRUD admin documentaire (create/update/delete/promote_document)
    # legacy   = mode exception pour incident/migration (encadrement strict ci-dessous)
    rag_write_mode: Literal["readonly", "legacy"] = "readonly"

    # Source d'ingestion canonique
    rag_index_source: Literal["wiki_exports_only", "legacy_filesystem"] = "wiki_exports_only"

    # Routes admin HTTP (UI + API knowledge) déprecées RFC 8594/9745
    # Si False (défaut) → 410 Gone + Sunset header
    # Si True → laisse passer downstream + audit log (rollback temporaire encadré)
    rag_legacy_admin_enabled: bool = False

    # Date de Sunset des routes admin (J0 + 30j)
    # Format ISO YYYY-MM-DD. Header HTTP `Sunset:` calculé depuis cette date
    rag_admin_sunset_at: str = "2026-06-03"

    # Encadrement strict du mode legacy (cf. model_validator ci-dessous)
    # Obligatoires si rag_legacy_admin_enabled=True ou rag_write_mode="legacy"
    rag_legacy_reason: Optional[str] = None  # cite INC-YYYY-NNN ou P0-XXX/P1-XXX
    rag_legacy_expires_at: Optional[datetime] = None  # max +14j depuis maintenant
    rag_legacy_authorized_by: Optional[str] = None  # GitHub handle de l'autorisateur (G3)

    # Weaviate Vector Database
    weaviate_url: str = "http://weaviate:8080"
    weaviate_grpc_port: int = 50051
    weaviate_collection_catalog: str = _yaml_config.get("vector_store", {}).get("catalog_class_name", "KB_Catalog")
    weaviate_collection_diagnostic: str = _yaml_config.get("vector_store", {}).get("diagnostic_class_name", "KB_Diagnostic")
    weaviate_collection_knowledge: str = _yaml_config.get("vector_store", {}).get("knowledge_class_name", "KB_Knowledge")
    weaviate_collection_media: str = _yaml_config.get("vector_store", {}).get("media_class_name", "KB_Media")
    weaviate_collection_router_memory: str = _yaml_config.get("vector_store", {}).get("router_memory_class_name", "KB_RouterMemory")

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
    fastembed_model: str = "BAAI/bge-small-en-v1.5"  # Used by PDF ingestion (router.py, reindex.py)

    # Reindex chunking params
    reindex_target_max_tokens: int = 900  # Max tokens per chunk in reindex.py

    # Temp file paths (centralized)
    tmp_base_dir: str = "/tmp"

    # RAG Settings (from rag_config.yml)
    retrieval_top_k: int = _yaml_config.get("retrieval", {}).get("top_k", 8)
    retrieval_alpha: float = _yaml_config.get("retrieval", {}).get("alpha", 0.7)
    min_score_threshold: float = _yaml_config.get("retrieval", {}).get("min_score_threshold", 0.70)
    min_results_required: int = _yaml_config.get("retrieval", {}).get("min_results_required", 3)

    # Phase 1: Role-based filtering (observe-only when false)
    role_filtering_enabled: bool = False

    # Phase 2: Chunk kind quotas for retrieval diversification (observe-only when false)
    chunk_kind_quotas_enabled: bool = False

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
        - DEV/CI/STAGING: Returns True (Build Plane)
        - Unknown environments: Returns False (fail-closed)

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

    # ========== TEMP FILE PATHS ==========

    @property
    def pdf_ingest_jobs_store(self) -> str:
        return f"{self.tmp_base_dir}/rag_pdf_ingest_jobs.json"

    @property
    def pdf_ingest_log_dir(self) -> str:
        return f"{self.tmp_base_dir}/rag_pdf_ingest_logs"

    @property
    def knowledge_import_dir(self) -> str:
        return f"{self.tmp_base_dir}/knowledge-import"

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

        # Production-specific validations
        if self.env == "prod":
            if not self.rag_api_key:
                errors.append(
                    "RAG_API_KEY not set in production - API will be unprotected"
                )
            if self.cors_origins == "*":
                errors.append(
                    "CORS_ORIGINS='*' in production - must be set to specific domains"
                )
            if not self.anthropic_api_key:
                errors.append(
                    "ANTHROPIC_API_KEY not set in production - LLM generation will fail"
                )
        else:
            # Dev/CI: warnings only
            if not self.rag_api_key:
                logger.warning("RAG_API_KEY not set - endpoints will be unprotected")

        # Warn about quarantine/mode contradiction
        if self.mode == "active" and self.quarantine_enabled:
            logger.warning(
                "mode='active' but quarantine.enabled=true in config - "
                "quarantine is effectively disabled (requires mode='quarantine')"
            )

        return errors

    # ========== Phase F.5 — Validators & helpers ==========

    @model_validator(mode="after")
    def _legacy_must_be_justified(self) -> "Settings":
        """Anti-permanence : mode legacy exige 4 vars cohérentes au boot.

        Refuse le démarrage si :
        - legacy activé sans REASON (citation INC-/P0-/P1- attendue)
        - legacy activé sans EXPIRES_AT
        - legacy activé sans AUTHORIZED_BY (GitHub handle G3)
        - EXPIRES_AT dans le passé (mode legacy expiré → revenir readonly)
        - EXPIRES_AT > +14j (incidents doivent fermer plus vite)
        """
        legacy_active = (
            self.rag_legacy_admin_enabled or self.rag_write_mode == "legacy"
        )
        if not legacy_active:
            return self

        if not self.rag_legacy_reason:
            raise ValueError(
                "F.5: legacy mode requires RAG_LEGACY_REASON (cite INC-YYYY-NNN or P0/P1 ticket id)"
            )
        if not self.rag_legacy_expires_at:
            raise ValueError("F.5: legacy mode requires RAG_LEGACY_EXPIRES_AT (max +14d)")
        if not self.rag_legacy_authorized_by:
            raise ValueError(
                "F.5: legacy mode requires RAG_LEGACY_AUTHORIZED_BY (GitHub handle, G3)"
            )

        now = datetime.now(timezone.utc)
        expires_at = self.rag_legacy_expires_at
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)

        if expires_at <= now:
            raise ValueError(
                f"F.5: RAG_LEGACY_EXPIRES_AT={expires_at.isoformat()} is in the past — "
                "refresh ticket or revert RAG_WRITE_MODE=readonly"
            )
        if (expires_at - now) > timedelta(days=14):
            raise ValueError(
                f"F.5: RAG_LEGACY_EXPIRES_AT={expires_at.isoformat()} exceeds +14d window — "
                "incidents must close faster ; reduce window or split mitigation"
            )
        return self

    @property
    def is_rag_readonly(self) -> bool:
        """True si le service est en mode readonly Phase F.5 (bloque CRUD admin documentaire)."""
        return self.rag_write_mode == "readonly"

    @property
    def admin_sunset_http_date(self) -> str:
        """Sunset date au format HTTP RFC 7231 (ex: 'Wed, 03 Jun 2026 00:00:00 GMT')."""
        try:
            d = datetime.fromisoformat(self.rag_admin_sunset_at)
        except ValueError:
            d = datetime(2026, 6, 3)
        return d.strftime("%a, %d %b %Y 00:00:00 GMT")

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
        logger.info(f"Weaviate gRPC Port: {self.weaviate_grpc_port}")
        logger.info(
            "Collections: "
            f"catalog={self.weaviate_collection_catalog}, "
            f"diagnostic={self.weaviate_collection_diagnostic}, "
            f"knowledge={self.weaviate_collection_knowledge}, "
            f"media={self.weaviate_collection_media}, "
            f"router_memory={self.weaviate_collection_router_memory}"
        )
        logger.info(f"Embedding Model: {self.embedding_model}")
        logger.info(f"Embedding Dimension: {self.embedding_dimension}")
        logger.info(f"FastEmbed Model: {self.fastembed_model}")
        logger.info(f"Reindex Max Tokens: {self.reindex_target_max_tokens}")
        logger.info(f"Min Score Threshold: {self.min_score_threshold}")
        logger.info(f"Min Results Required: {self.min_results_required}")
        logger.info(f"Kill Switch (ai_prod_write): {self.ai_prod_write}")
        logger.info(f"Tmp Base Dir: {self.tmp_base_dir}")
        # Phase F.5
        logger.info(f"[F.5] rag_write_mode: {self.rag_write_mode}")
        logger.info(f"[F.5] rag_index_source: {self.rag_index_source}")
        logger.info(f"[F.5] rag_legacy_admin_enabled: {self.rag_legacy_admin_enabled}")
        logger.info(f"[F.5] rag_admin_sunset_at: {self.rag_admin_sunset_at}")
        if self.rag_legacy_admin_enabled or self.rag_write_mode == "legacy":
            logger.warning(
                "[F.5] LEGACY MODE ACTIVE — reason=%r expires_at=%s authorized_by=%r "
                "(see governance-vault ADR-031 runbook §Phase F.5)",
                self.rag_legacy_reason,
                self.rag_legacy_expires_at.isoformat() if self.rag_legacy_expires_at else None,
                self.rag_legacy_authorized_by,
            )
        logger.info("=" * 50)


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
