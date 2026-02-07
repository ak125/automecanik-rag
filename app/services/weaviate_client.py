"""Weaviate client for hybrid search with local embeddings."""

import logging
from typing import Optional
import weaviate
from weaviate.classes.query import HybridFusion

from app.config import get_settings
from app.services.embeddings import get_embeddings_service

logger = logging.getLogger(__name__)


class WeaviateClient:
    """Client for Weaviate vector database."""

    COLLECTION_NAME = "Prod_Chatbot"

    def __init__(self):
        """Initialize Weaviate client with local embeddings."""
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
        self.embeddings = get_embeddings_service()

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
            List of matching documents with scores (deduplicated by source_path)
        """
        if alpha is None:
            alpha = self.settings.retrieval_alpha

        try:
            collection = self.client.collections.get(self.COLLECTION_NAME)

            # Generate query embedding locally (100% gratuit)
            query_vector = self.embeddings.embed(query)

            # Fetch more results to account for potential duplicates
            # After dedupe, we trim to the original limit
            fetch_limit = limit * 2

            response = collection.query.hybrid(
                query=query,
                vector=query_vector,
                limit=fetch_limit,
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
                        # Core properties
                        "content": obj.properties.get("content", ""),
                        "title": obj.properties.get("title", ""),
                        "source_type": obj.properties.get("source_type", ""),
                        "source_path": obj.properties.get("source_path", ""),
                        "category": obj.properties.get("category", ""),
                        "score": score,
                        # Truth Level properties (Semantic Brain L1-L4)
                        "truth_level": obj.properties.get("truth_level", "L3"),
                        "verification_status": obj.properties.get("verification_status", "unverified"),
                        "confidence_score": obj.properties.get("confidence_score", 0.5),
                        "last_verified_date": obj.properties.get("last_verified_date", ""),
                        "verified_by": obj.properties.get("verified_by", ""),
                    })

            # DEDUPE: Keep only first occurrence per source_path (highest score)
            # Results are already sorted by score from Weaviate
            seen_sources: set[str] = set()
            deduped_results: list[dict] = []
            for r in results:
                source_path = r.get("source_path", "")
                if source_path and source_path not in seen_sources:
                    seen_sources.add(source_path)
                    deduped_results.append(r)

            # Log dedupe stats for debugging
            if len(results) != len(deduped_results):
                logger.info(
                    f"Dedupe: {len(results)} -> {len(deduped_results)} results "
                    f"({len(results) - len(deduped_results)} duplicates removed)"
                )

            # Trim to original limit after dedupe
            final_results = deduped_results[:limit]

            logger.info(f"Hybrid search for '{query[:50]}...' returned {len(final_results)} results")
            return final_results

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

    async def is_healthy(self) -> bool:
        """Check if Weaviate is healthy (for startup validation)."""
        try:
            return self.client.is_ready()
        except Exception as e:
            logger.error(f"Weaviate is_healthy check failed: {e}")
            return False

    async def get_schema(self) -> Optional[dict]:
        """Get schema for the collection (for dimension validation)."""
        try:
            collection = self.client.collections.get(self.COLLECTION_NAME)
            config = collection.config.get()
            return {
                "vectorDimension": self.settings.embedding_dimension,  # Assume config matches
                "class": self.COLLECTION_NAME,
            }
        except Exception as e:
            logger.error(f"Failed to get schema: {e}")
            return None

    async def count_documents(self) -> int:
        """Count documents in the collection (for corpus validation)."""
        try:
            collection = self.client.collections.get(self.COLLECTION_NAME)
            response = collection.aggregate.over_all(total_count=True)
            return response.total_count or 0
        except Exception as e:
            logger.error(f"Failed to count documents: {e}")
            return 0

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
