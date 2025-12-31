"""AutoMecanik RAG Service - FastAPI Application."""

from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

from app.config import get_settings, Settings
from app.api.chat import router as chat_router
from app.api.search import router as search_router
from app.api.health import router as health_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="AutoMecanik RAG Service",
    description="Service RAG pour le support client AutoMecanik",
    version="1.0.0",
    docs_url="/docs" if get_settings().debug else None,
    redoc_url="/redoc" if get_settings().debug else None,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API Key validation
async def verify_api_key(request: Request):
    """Verify API key from request headers."""
    settings = get_settings()
    api_key = request.headers.get("X-API-Key")

    if not api_key or api_key != settings.rag_api_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )
    return True


# Include routers
app.include_router(health_router, tags=["Health"])
app.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"],
    dependencies=[Depends(verify_api_key)]
)
app.include_router(
    search_router,
    prefix="/search",
    tags=["Search"],
    dependencies=[Depends(verify_api_key)]
)


@app.on_event("startup")
async def startup_event():
    """Initialize services on startup."""
    settings = get_settings()
    logger.info(f"Starting RAG service in {settings.env} mode")
    logger.info(f"Weaviate URL: {settings.weaviate_url}")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    logger.info("Shutting down RAG service")


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler."""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=get_settings().debug
    )
