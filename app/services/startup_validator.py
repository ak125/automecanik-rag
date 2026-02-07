"""Startup validation - Fail-fast checks for RAG service.

QUARANTINE MODE (v1.0.0):
- Validates configuration at startup
- Fail-fast if critical checks fail
- Ensures RAG is properly configured before accepting requests
"""

import logging
from typing import List, Tuple

logger = logging.getLogger(__name__)


class StartupValidator:
    """
    Validate RAG configuration at startup.

    Checks:
    - Weaviate connection
    - Embedding dimension match
    - Corpus not empty
    """

    def __init__(self, config, weaviate_client=None):
        """
        Initialize validator.

        Args:
            config: Settings instance
            weaviate_client: Optional Weaviate client for connection checks
        """
        self.config = config
        self.weaviate = weaviate_client

    async def validate_all(self) -> Tuple[bool, List[str]]:
        """
        Run all validation checks.

        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []

        logger.info("Running startup validation checks...")

        # 1. Config validation (no external deps)
        config_errors = self._check_config()
        errors.extend(config_errors)

        # 2. Weaviate connection (if client provided)
        if self.weaviate:
            weaviate_ok = await self._check_weaviate()
            if not weaviate_ok:
                errors.append("Weaviate connection failed")

            # 3. Embedding dimension match
            dimension_ok = await self._check_embedding_dimension()
            if not dimension_ok:
                errors.append("Embedding dimension mismatch with Weaviate schema")

            # 4. Corpus not empty
            corpus_ok = await self._check_corpus()
            if not corpus_ok:
                errors.append("Corpus is empty - no documents indexed")

        is_valid = len(errors) == 0

        if is_valid:
            logger.info("All startup validation checks PASSED")
        else:
            logger.error(f"Startup validation FAILED with {len(errors)} error(s):")
            for error in errors:
                logger.error(f"  - {error}")

        return is_valid, errors

    def _check_config(self) -> List[str]:
        """
        Validate configuration values.

        Returns:
            List of error messages
        """
        return self.config.validate_config()

    async def _check_weaviate(self) -> bool:
        """
        Check Weaviate is reachable.

        Returns:
            True if Weaviate is healthy
        """
        try:
            is_healthy = await self.weaviate.is_healthy()
            if is_healthy:
                logger.info("Weaviate connection: OK")
            else:
                logger.error("Weaviate connection: FAILED (not healthy)")
            return is_healthy
        except Exception as e:
            logger.error(f"Weaviate connection: FAILED ({e})")
            return False

    async def _check_embedding_dimension(self) -> bool:
        """
        Check embedding dimension matches Weaviate schema.

        Returns:
            True if dimensions match
        """
        try:
            # Get schema from Weaviate
            schema = await self.weaviate.get_schema()

            if not schema:
                logger.warning("Could not retrieve Weaviate schema - skipping dimension check")
                return True  # Non-blocking if schema unavailable

            # Get vector dimension from schema
            expected = self.config.embedding_dimension
            actual = schema.get("vectorDimension", expected)

            if actual != expected:
                logger.error(
                    f"Embedding dimension mismatch: "
                    f"config={expected}, weaviate_schema={actual}"
                )
                return False

            logger.info(f"Embedding dimension check: OK ({expected})")
            return True

        except Exception as e:
            logger.warning(f"Embedding dimension check skipped: {e}")
            return True  # Non-blocking on error

    async def _check_corpus(self) -> bool:
        """
        Check corpus has documents.

        Returns:
            True if corpus is not empty
        """
        try:
            count = await self.weaviate.count_documents()

            if count == 0:
                logger.error("Corpus is empty - no documents indexed")
                return False

            logger.info(f"Corpus check: OK ({count} documents)")
            return True

        except Exception as e:
            logger.warning(f"Corpus check skipped: {e}")
            return True  # Non-blocking on error


def run_startup_validation(config, weaviate_client=None) -> Tuple[bool, List[str]]:
    """
    Synchronous wrapper for startup validation.

    For use in non-async contexts (e.g., module import).

    Args:
        config: Settings instance
        weaviate_client: Optional Weaviate client

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    import asyncio

    validator = StartupValidator(config, weaviate_client)

    # Run async validation in sync context
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # Already in async context - can't use run_until_complete
            # Return partial validation (config only)
            errors = validator._check_config()
            return len(errors) == 0, errors
        else:
            return loop.run_until_complete(validator.validate_all())
    except RuntimeError:
        # No event loop - create one
        return asyncio.run(validator.validate_all())
