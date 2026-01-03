"""Local embeddings service using sentence-transformers (100% gratuit)."""

import logging
from typing import Optional
import numpy as np
from sentence_transformers import SentenceTransformer

from app.config import get_settings

logger = logging.getLogger(__name__)


class EmbeddingsService:
    """
    Local embeddings service using sentence-transformers.

    Uses all-MiniLM-L6-v2 by default (384 dimensions, fast, accurate).
    100% gratuit - runs locally without any API calls.
    """

    def __init__(self):
        """Initialize embeddings model."""
        settings = get_settings()
        self.model_name = settings.embedding_model
        self.dimension = settings.embedding_dimension

        logger.info(f"Loading embedding model: {self.model_name}")
        self.model = SentenceTransformer(self.model_name)
        logger.info(f"Embedding model loaded. Dimension: {self.dimension}")

    def embed(self, text: str) -> list[float]:
        """Generate embedding for a single text."""
        embedding = self.model.encode(text, convert_to_numpy=True)
        return embedding.tolist()

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings for multiple texts."""
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings.tolist()

    def get_dimension(self) -> int:
        """Return embedding dimension."""
        return self.dimension

    def health_check(self) -> dict:
        """Check embeddings service health."""
        try:
            test_embedding = self.embed("test")
            return {
                "status": "healthy",
                "model": self.model_name,
                "dimension": len(test_embedding),
            }
        except Exception as e:
            logger.error(f"Embeddings health check failed: {e}")
            return {"status": "unhealthy", "error": str(e)}


_embeddings_service: Optional[EmbeddingsService] = None


def get_embeddings_service() -> EmbeddingsService:
    """Get or create embeddings service instance."""
    global _embeddings_service
    if _embeddings_service is None:
        _embeddings_service = EmbeddingsService()
    return _embeddings_service
