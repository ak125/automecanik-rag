"""Health check endpoint (100% gratuit - sans Claude API)."""

from fastapi import APIRouter
from fastapi.responses import JSONResponse
import logging

from app.services.weaviate_client import get_weaviate_client
from app.services.embeddings import get_embeddings_service

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Health check endpoint.

    Returns status of all services (Weaviate + Embeddings locaux).
    Returns 503 if any critical service is unhealthy.
    """
    try:
        weaviate = get_weaviate_client()
        weaviate_status = await weaviate.health_check()
    except Exception as e:
        logger.error(f"Health check - Weaviate error: {e}")
        weaviate_status = {"status": "unhealthy", "error": str(e)}

    try:
        embeddings = get_embeddings_service()
        embeddings_status = embeddings.health_check()
    except Exception as e:
        logger.error(f"Health check - Embeddings error: {e}")
        embeddings_status = {"status": "unhealthy", "error": str(e)}

    all_healthy = (
        weaviate_status.get("status") == "healthy"
        and embeddings_status.get("status") == "healthy"
    )
    overall_status = "healthy" if all_healthy else "degraded"
    status_code = 200 if all_healthy else 503

    return JSONResponse(
        status_code=status_code,
        content={
            "status": overall_status,
            "version": "1.0.0-gratuit",
            "services": {
                "weaviate": weaviate_status,
                "embeddings": embeddings_status,
                "api": {"status": "healthy"},
            }
        }
    )


@router.get("/ready")
async def readiness_check():
    """
    Readiness check for Kubernetes.

    Returns 200 only if all dependencies are ready.
    Returns 503 if not ready so load balancers route correctly.
    """
    try:
        weaviate = get_weaviate_client()
        weaviate_status = await weaviate.health_check()
    except Exception as e:
        logger.error(f"Readiness check - Weaviate error: {e}")
        return JSONResponse(
            status_code=503,
            content={"ready": False, "reason": f"Weaviate error: {e}"}
        )

    if weaviate_status.get("status") != "healthy":
        return JSONResponse(
            status_code=503,
            content={"ready": False, "reason": "Weaviate not ready"}
        )

    return {"ready": True}
