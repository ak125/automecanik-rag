"""Weaviate client for hybrid search with local embeddings."""

import logging
from typing import Optional
import weaviate
from weaviate.classes.query import HybridFusion, Filter

from app.config import get_settings
from app.services.embeddings import get_embeddings_service

logger = logging.getLogger(__name__)


class WeaviateClient:
    """Client for Weaviate vector database."""

    COLLECTION_NAME = "Prod_Chatbot"

    def __init__(self):
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
        self.collection_by_family = {
            "catalog": self.settings.weaviate_collection_catalog,
            "diagnostic": self.settings.weaviate_collection_diagnostic,
            "knowledge": self.settings.weaviate_collection_knowledge,
            "media": self.settings.weaviate_collection_media,
            "router_memory": self.settings.weaviate_collection_router_memory,
        }

    def resolve_collection(self, namespace: Optional[str] = None, routing: Optional[dict] = None) -> str:
        if routing and isinstance(routing, dict):
            family = routing.get("intentFamily")
            if isinstance(family, str) and family in self.collection_by_family:
                return self.collection_by_family[family]

        if namespace:
            ns = namespace.lower()
            if "diagnostic" in ns:
                return self.settings.weaviate_collection_diagnostic
            if "gamme" in ns or "catalog" in ns:
                return self.settings.weaviate_collection_catalog
            if "media" in ns:
                return self.settings.weaviate_collection_media
            if "router" in ns:
                return self.settings.weaviate_collection_router_memory

        return self.settings.weaviate_collection_knowledge

    def _format_result(self, obj, score: float, target_collection: str) -> dict:
        props = obj.properties
        return {
            "content": props.get("content") or "",
            "title": props.get("title") or "",
            "source_type": props.get("source_type") or "",
            "doc_family": props.get("doc_family") or "knowledge",
            "source_path": props.get("source_path") or "",
            "source_uri": props.get("source_uri") or "",
            "source_ref": props.get("source_ref") or "",
            "category": props.get("category") or "",
            "score": score,
            "truth_level": props.get("truth_level") or "L3",
            "verification_status": props.get("verification_status") or "unverified",
            "confidence_score": props.get("confidence_score") if props.get("confidence_score") is not None else 0.5,
            "evidence_grade": props.get("evidence_grade") or "",
            "last_verified_date": props.get("last_verified_date") or "",
            "verified_by": props.get("verified_by") or "",
            "chunk_id": props.get("chunk_id") or "",
            "parent_id": props.get("parent_id") or "",
            "intent": props.get("intent") or "",
            "domain": props.get("domain") or "general",
            "entities": props.get("entities", []) or [],
            "anchors": props.get("anchors", []) or [],
            "doc_weight": props.get("doc_weight") if props.get("doc_weight") is not None else 0.7,
            "is_canonical": bool(props.get("is_canonical", False)),
            "canonical_weight": props.get("canonical_weight") if props.get("canonical_weight") is not None else 0.0,
            "created_at": props.get("created_at") or "",
            "updated_at": props.get("updated_at") or "",
            "content_hash": props.get("content_hash") or "",
            "collection": target_collection,
        }

    async def hybrid_search(
        self,
        query: str,
        limit: int = 5,
        alpha: Optional[float] = None,
        collection_name: Optional[str] = None,
        domain: Optional[str] = None,
        exclude_disputed: bool = False,
        min_score: Optional[float] = None,
    ) -> list[dict]:
        if alpha is None:
            alpha = self.settings.retrieval_alpha
        if min_score is None:
            min_score = self.settings.min_score_threshold

        try:
            target_collection = collection_name or self.settings.weaviate_collection_knowledge
            collection = self.client.collections.get(target_collection)
            query_vector = self.embeddings.embed(query)

            canonical_limit = max(1, limit // 2)
            domain_filter = None
            if domain and domain != "general":
                domain_filter = Filter.by_property("domain").equal(domain)

            canonical_filters = Filter.by_property("is_canonical").equal(True)
            if domain_filter is not None:
                canonical_filters = canonical_filters & domain_filter

            general_filters = domain_filter
            merged_results: list[dict] = []

            # Canonical pass is optional: some legacy collections may not yet have is_canonical.
            try:
                canonical_response = collection.query.hybrid(
                    query=query,
                    vector=query_vector,
                    limit=canonical_limit,
                    alpha=alpha,
                    fusion_type=HybridFusion.RELATIVE_SCORE,
                    filters=canonical_filters,
                    return_metadata=["score"],
                )
                for obj in canonical_response.objects:
                    score = obj.metadata.score if obj.metadata else 0.0
                    if score >= min_score:
                        merged_results.append(self._format_result(obj, score, target_collection))
            except Exception as exc:  # noqa: BLE001
                logger.warning(
                    "Canonical query skipped in %s (likely missing is_canonical): %s",
                    target_collection,
                    exc,
                )

            general_fetch_limit = limit * 3
            general_response = collection.query.hybrid(
                query=query,
                vector=query_vector,
                limit=general_fetch_limit,
                alpha=alpha,
                fusion_type=HybridFusion.RELATIVE_SCORE,
                filters=general_filters,
                return_metadata=["score"],
            )

            for obj in general_response.objects:
                score = obj.metadata.score if obj.metadata else 0.0
                if score >= min_score:
                    merged_results.append(self._format_result(obj, score, target_collection))

            if exclude_disputed:
                merged_results = [
                    r for r in merged_results
                    if str(r.get("verification_status", "unverified")).lower() != "disputed"
                ]

            seen_keys: set[str] = set()
            deduped_results: list[dict] = []
            for r in merged_results:
                dedupe_key = r.get("chunk_id") or r.get("source_path")
                if dedupe_key and dedupe_key not in seen_keys:
                    seen_keys.add(dedupe_key)
                    deduped_results.append(r)

            final_results = deduped_results[:limit]
            canonical_count = sum(1 for r in final_results if r.get("is_canonical"))
            logger.info(
                f"Hybrid search '{query[:40]}...' in {target_collection}: "
                f"{len(final_results)} results ({canonical_count} canonical first, domain={domain or 'any'}, strict={exclude_disputed})"
            )
            return final_results

        except Exception as e:
            logger.error(f"Weaviate search error: {e}")
            return []

    async def health_check(self) -> dict:
        try:
            is_ready = self.client.is_ready()
            return {"status": "healthy" if is_ready else "unhealthy", "ready": is_ready}
        except Exception as e:
            logger.error(f"Weaviate health check failed: {e}")
            return {"status": "unhealthy", "error": str(e)}

    async def is_healthy(self) -> bool:
        try:
            return self.client.is_ready()
        except Exception as e:
            logger.error(f"Weaviate is_healthy check failed: {e}")
            return False

    async def get_schema(self, collection_name: Optional[str] = None) -> Optional[dict]:
        try:
            target_collection = collection_name or self.settings.weaviate_collection_knowledge
            _ = self.client.collections.get(target_collection).config.get()
            return {"vectorDimension": self.settings.embedding_dimension, "class": target_collection}
        except Exception as e:
            logger.error(f"Failed to get schema: {e}")
            return None

    async def count_documents(self, collection_name: Optional[str] = None) -> int:
        try:
            target_collection = collection_name or self.settings.weaviate_collection_knowledge
            collection = self.client.collections.get(target_collection)
            response = collection.aggregate.over_all(total_count=True)
            return response.total_count or 0
        except Exception as e:
            logger.error(f"Failed to count documents: {e}")
            return 0

    def close(self):
        if self.client:
            self.client.close()


_weaviate_client: Optional[WeaviateClient] = None


def get_weaviate_client() -> WeaviateClient:
    global _weaviate_client
    if _weaviate_client is None:
        _weaviate_client = WeaviateClient()
    return _weaviate_client
