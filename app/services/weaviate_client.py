"""Weaviate client for hybrid search."""

import logging
from typing import Optional
import weaviate
from weaviate.classes.query import HybridFusion

from app.config import get_settings

logger = logging.getLogger(__name__)


class WeaviateClient:
    """Client for Weaviate vector database."""

    COLLECTION_NAME = "Prod_Chatbot"

    def __init__(self):
        """Initialize Weaviate client."""
        settings = get_settings()
        self.client = weaviate.connect_to_custom(
            http_host=settings.weaviate_url.replace("http://", "").replace("https://", "").split(":")[0],
            http_port=int(settings.weaviate_url.split(":")[-1]) if ":" in settings.weaviate_url.split("/")[-1] else 8080,
            http_secure=settings.weaviate_url.startswith("https"),
            grpc_host=settings.weaviate_url.replace("http://", "").replace("https://", "").split(":")[0],
            grpc_port=50051,
            grpc_secure=False,
        )
        self.settings = settings

    async def hybrid_search(
        self,
        query: str,
        limit: int = 5,
        alpha: Optional[float] = None,
    ) -> list[dict]:
        """
        Perform hybrid search (BM25 + vector).

        Args:
            query: Search query
            limit: Number of results to return
            alpha: Balance between BM25 (0) and vector (1). Default from settings.

        Returns:
            List of matching documents with scores
        """
        if alpha is None:
            alpha = self.settings.retrieval_alpha

        try:
            collection = self.client.collections.get(self.COLLECTION_NAME)

            response = collection.query.hybrid(
                query=query,
                limit=limit,
                alpha=alpha,
                fusion_type=HybridFusion.RELATIVE_SCORE,
                return_metadata=["score"],
            )

            results = []
            for obj in response.objects:
                score = obj.metadata.score if obj.metadata else 0.0

                # Filter by minimum score threshold
                if score >= self.settings.min_score_threshold:
                    results.append({
                        "content": obj.properties.get("content", ""),
                        "title": obj.properties.get("title", ""),
                        "source_type": obj.properties.get("source_type", ""),
                        "source_path": obj.properties.get("source_path", ""),
                        "category": obj.properties.get("category", ""),
                        "score": score,
                    })

            logger.info(f"Hybrid search for '{query[:50]}...' returned {len(results)} results")
            return results

        except Exception as e:
            logger.error(f"Weaviate search error: {e}")
            return []

    async def health_check(self) -> dict:
        """Check Weaviate connection health."""
        try:
            is_ready = self.client.is_ready()
            return {
                "status": "healthy" if is_ready else "unhealthy",
                "ready": is_ready,
            }
        except Exception as e:
            logger.error(f"Weaviate health check failed: {e}")
            return {
                "status": "unhealthy",
                "error": str(e),
            }

    def close(self):
        """Close Weaviate connection."""
        if self.client:
            self.client.close()


# Singleton instance
_weaviate_client: Optional[WeaviateClient] = None


def get_weaviate_client() -> WeaviateClient:
    """Get or create Weaviate client instance."""
    global _weaviate_client
    if _weaviate_client is None:
        _weaviate_client = WeaviateClient()
    return _weaviate_client
