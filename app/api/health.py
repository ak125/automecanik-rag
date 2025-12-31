"""Health check endpoint."""

from fastapi import APIRouter
from app.services.weaviate_client import get_weaviate_client
from app.services.claude_client import get_claude_client

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Health check endpoint.

    Returns status of all services.
    """
    weaviate = get_weaviate_client()
    weaviate_status = await weaviate.health_check()

    return {
        "status": "healthy",
        "services": {
            "weaviate": weaviate_status,
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
