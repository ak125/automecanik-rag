"""RAG Orchestrator Package - BUILD Plane Only.

This package handles all RAG ingestion operations and MUST ONLY run in BUILD plane
(dev/ci environments). Production environments are STRICTLY BLOCKED.

Components:
- kill_switch: Enforces BUILD plane policy
- pipeline: Main orchestration flow
- extractors: Data extraction from MinIO, Wiki, knowledge folder
- processors: Document chunking and embedding

CRITICAL: All write operations (index, create, update, delete) are blocked in PROD.
"""

from .kill_switch import (
    enforce_build_plane,
    BuildPlaneViolation,
    is_build_plane,
    get_current_environment,
    validate_environment_config,
)
from .pipeline import OrchestratorPipeline, run_full_ingestion

__all__ = [
    "enforce_build_plane",
    "BuildPlaneViolation",
    "is_build_plane",
    "get_current_environment",
    "validate_environment_config",
    "OrchestratorPipeline",
    "run_full_ingestion",
]

__version__ = "1.0.0"
