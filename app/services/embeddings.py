"""Memory-efficient embeddings service using FastEmbed (Rust backend).

FastEmbed advantages:
- Rust backend: 50-80% faster than PyTorch
- 80% less memory: ~200-500MB vs 2-4GB for sentence-transformers
- Cold start: ~2s vs ~10s
- Compatible with HuggingFace models

Model: BAAI/bge-small-en-v1.5 (384 dimensions, compatible with all-MiniLM-L6-v2)
"""

import logging
from typing import Optional, List
from fastembed import TextEmbedding

from app.config import get_settings

logger = logging.getLogger(__name__)

# Model mapping: legacy sentence-transformers name -> FastEmbed equivalent
MODEL_MAPPING = {
    "all-MiniLM-L6-v2": "BAAI/bge-small-en-v1.5",  # Same 384 dims
    "all-mpnet-base-v2": "BAAI/bge-base-en-v1.5",  # 768 dims
}


class EmbeddingsService:
    """
    Memory-efficient embeddings service using FastEmbed.

    Uses BAAI/bge-small-en-v1.5 by default (384 dimensions).
    100% gratuit - runs locally without any API calls.
    """

    _instance: Optional["EmbeddingsService"] = None
    _model: Optional[TextEmbedding] = None

    def __new__(cls) -> "EmbeddingsService":
        """Singleton pattern for memory efficiency."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize FastEmbed model (lazy loading)."""
        if self._model is not None:
            return  # Already initialized

        settings = get_settings()
        config_model = settings.embedding_model
        self.dimension = settings.embedding_dimension

        # Map legacy model names to FastEmbed equivalents
        fastembed_model = MODEL_MAPPING.get(config_model, "BAAI/bge-small-en-v1.5")

        logger.info(f"Loading FastEmbed model: {fastembed_model}")
        logger.info(f"  (mapped from config: {config_model})")

        try:
            self._model = TextEmbedding(model_name=fastembed_model)
            logger.info(f"FastEmbed model loaded. Expected dimension: {self.dimension}")
        except Exception as e:
            logger.error(f"Failed to load FastEmbed model: {e}")
            raise

    def embed(self, text: str) -> List[float]:
        """Generate embedding for a single text."""
        if not text or not text.strip():
            # Return zero vector for empty text
            return [0.0] * self.dimension

        embeddings = list(self._model.embed([text]))
        return embeddings[0].tolist()

    def embed_batch(self, texts: List[str], batch_size: int = 32) -> List[List[float]]:
        """
        Generate embeddings for multiple texts efficiently.

        Args:
            texts: List of texts to embed
            batch_size: Batch size for processing (default: 32)

        Returns:
            List of embedding vectors
        """
        if not texts:
            return []

        # Filter empty texts but keep track of indices
        valid_indices = []
        valid_texts = []
        for i, text in enumerate(texts):
            if text and text.strip():
                valid_indices.append(i)
                valid_texts.append(text)

        if not valid_texts:
            return [[0.0] * self.dimension] * len(texts)

        # Generate embeddings for valid texts
        embeddings_iter = self._model.embed(valid_texts, batch_size=batch_size)
        valid_embeddings = [e.tolist() for e in embeddings_iter]

        # Rebuild full result list with zero vectors for empty texts
        result = [[0.0] * self.dimension] * len(texts)
        for idx, emb in zip(valid_indices, valid_embeddings):
            result[idx] = emb

        return result

    def get_dimension(self) -> int:
        """Return embedding dimension."""
        return self.dimension

    def health_check(self) -> dict:
        """Check embeddings service health."""
        try:
            test_embedding = self.embed("test")
            return {
                "status": "healthy",
                "backend": "fastembed",
                "model": MODEL_MAPPING.get(
                    get_settings().embedding_model,
                    "BAAI/bge-small-en-v1.5"
                ),
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
