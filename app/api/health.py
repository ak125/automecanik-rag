"""Health check endpoint (100% gratuit - sans Claude API)."""

from fastapi import APIRouter
from app.services.weaviate_client import get_weaviate_client
from app.services.embeddings import get_embeddings_service

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Health check endpoint.

    Returns status of all services (Weaviate + Embeddings locaux).
    """
    weaviate = get_weaviate_client()
    weaviate_status = await weaviate.health_check()

    embeddings = get_embeddings_service()
    embeddings_status = embeddings.health_check()

    return {
        "status": "healthy",
        "version": "1.0.0-gratuit",
        "services": {
            "weaviate": weaviate_status,
            "embeddings": embeddings_status,
            "api": {"status": "healthy"},
        }
    }


@router.get("/ready")
async def readiness_check():
    """
    Readiness check for Kubernetes.

    Returns 200 only if all dependencies are ready.
    """
    weaviate = get_weaviate_client()
    weaviate_status = await weaviate.health_check()

    if weaviate_status.get("status") != "healthy":
        return {"ready": False, "reason": "Weaviate not ready"}

    return {"ready": True}
