#!/usr/bin/env python3
"""RAG Orchestrator CLI - Run ingestion pipeline.

Usage:
    python run_orchestrator.py              # Full ingestion
    python run_orchestrator.py --check      # Validate environment only
    python run_orchestrator.py --dry-run    # Preview without writing
    python run_orchestrator.py --source knowledge  # Only process knowledge folder

CRITICAL: This script ONLY runs in BUILD plane (dev/ci).
Production environments are BLOCKED by kill switch.
"""

import argparse
import asyncio
import logging
import sys
import json
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from orchestrator import (
    enforce_build_plane,
    BuildPlaneViolation,
    validate_environment_config,
)
from orchestrator.pipeline import OrchestratorPipeline, PipelineConfig


def setup_logging(verbose: bool = False):
    """Configure logging for the CLI."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )


def load_config(config_path: str = None) -> dict:
    """Load configuration from YAML file."""
    import yaml

    if config_path is None:
        config_path = Path(__file__).parent.parent / "rag_config.yml"
    else:
        config_path = Path(config_path)

    if not config_path.exists():
        logging.warning(f"Config file not found: {config_path}")
        return {}

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def check_environment():
    """Validate environment and print status."""
    print("=" * 60)
    print("ENVIRONMENT CHECK")
    print("=" * 60)

    status = validate_environment_config()

    print(f"Environment: {status['environment']}")
    print(f"Build Plane: {'YES' if status['is_build_plane'] else 'NO'}")
    print(f"Runtime Plane: {'YES' if status['is_runtime_plane'] else 'NO'}")
    print(f"Write Operations: {'ALLOWED' if status['write_operations_allowed'] else 'BLOCKED'}")
    print(f"Status: {status['message']}")
    print()
    print(f"Allowed environments: {', '.join(status['allowed_environments'])}")
    print(f"Blocked environments: {', '.join(status['blocked_environments'])}")
    print("=" * 60)

    return status['write_operations_allowed']


async def run_ingestion(args):
    """Run the full ingestion pipeline."""
    logger = logging.getLogger(__name__)

    # Step 1: Validate environment (kill switch)
    try:
        enforce_build_plane("run_orchestrator")
    except BuildPlaneViolation as e:
        logger.critical(str(e))
        print(f"\nERROR: {e}")
        print("\nThis script can only run in BUILD plane (dev/ci/staging).")
        print("Set ENV=dev to enable writes.")
        return 1

    # Step 2: Load configuration
    config_dict = load_config(args.config)

    # Step 3: Build pipeline config
    pipeline_config = PipelineConfig.from_yaml(config_dict)

    # Override from CLI args
    if args.source:
        if args.source == "knowledge":
            pipeline_config.minio_enabled = False
            pipeline_config.wiki_enabled = False
        elif args.source == "wiki":
            pipeline_config.minio_enabled = False
            pipeline_config.knowledge_enabled = False
        elif args.source == "minio":
            pipeline_config.wiki_enabled = False
            pipeline_config.knowledge_enabled = False

    if args.knowledge_path:
        pipeline_config.knowledge_path = args.knowledge_path

    # Step 4: Dry run check
    if args.dry_run:
        logger.info("DRY RUN - No writes will be performed")
        print("\n=== DRY RUN CONFIG ===")
        print(f"Knowledge: {pipeline_config.knowledge_enabled} ({pipeline_config.knowledge_path})")
        print(f"Wiki: {pipeline_config.wiki_enabled} (mode={pipeline_config.wiki_mode})")
        print(f"MinIO: {pipeline_config.minio_enabled} (buckets={pipeline_config.minio_buckets})")
        print(f"Chunk size: {pipeline_config.chunk_size} tokens")
        print(f"Chunk overlap: {pipeline_config.chunk_overlap} tokens")
        print(f"Batch size: {pipeline_config.batch_size}")
        print(f"Versioning: {pipeline_config.create_version}")
        print("======================\n")
        return 0

    # Step 5: Run pipeline
    logger.info("Starting RAG Orchestrator Pipeline...")
    pipeline = OrchestratorPipeline(pipeline_config)
    result = await pipeline.run()

    # Step 6: Print results
    print("\n" + "=" * 60)
    print("PIPELINE RESULT")
    print("=" * 60)
    print(f"Success: {result.success}")
    print(f"Documents processed: {result.documents_processed}")
    print(f"Chunks created: {result.chunks_created}")
    print(f"Chunks indexed: {result.chunks_indexed}")
    print(f"Duration: {result.duration_seconds:.2f}s")

    if result.version_tag:
        print(f"Version: {result.version_tag}")

    if result.errors:
        print(f"Errors: {len(result.errors)}")
        for error in result.errors:
            print(f"  - {error}")

    print("=" * 60)

    # Output JSON result if requested
    if args.json:
        print("\n=== JSON RESULT ===")
        print(json.dumps({
            "success": result.success,
            "documents_processed": result.documents_processed,
            "chunks_created": result.chunks_created,
            "chunks_indexed": result.chunks_indexed,
            "duration_seconds": result.duration_seconds,
            "version_tag": result.version_tag,
            "errors": result.errors,
            "timestamp": result.timestamp,
        }, indent=2))

    return 0 if result.success else 1


def main():
    parser = argparse.ArgumentParser(
        description="RAG Orchestrator CLI - Run ingestion pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          Run full ingestion
  %(prog)s --check                  Validate environment only
  %(prog)s --dry-run                Preview without writing
  %(prog)s --source knowledge       Only process /knowledge folder
  %(prog)s --source wiki            Only process Wiki.js
  %(prog)s --source minio           Only process MinIO buckets
  %(prog)s -v                       Verbose logging

IMPORTANT: This script ONLY runs in BUILD plane (dev/ci).
Set ENV=dev before running.
        """,
    )

    parser.add_argument(
        "--check",
        action="store_true",
        help="Only validate environment, don't run pipeline",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview pipeline config without running",
    )
    parser.add_argument(
        "--source",
        choices=["knowledge", "wiki", "minio"],
        help="Only process a specific source",
    )
    parser.add_argument(
        "--knowledge-path",
        type=str,
        help="Override knowledge folder path",
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to rag_config.yml",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output result as JSON",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    args = parser.parse_args()

    # Setup logging
    setup_logging(args.verbose)

    # Check-only mode
    if args.check:
        success = check_environment()
        return 0 if success else 1

    # Run ingestion
    try:
        return asyncio.run(run_ingestion(args))
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        return 130
    except Exception as e:
        logging.error(f"Pipeline failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
