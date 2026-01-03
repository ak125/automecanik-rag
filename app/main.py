"""AutoMecanik RAG Service - FastAPI Application.

P0 SECURITY FEATURES:
- CORS hardened (no wildcard in PROD)
- Rate limiting (60 req/min default)
- Prompt injection detection
- PII detection (GDPR)
- Request size limits
- Kill switch validation at startup
"""

from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import sys
import time

from app.config import get_settings
from app.api.chat import router as chat_router
from app.api.search import router as search_router
from app.api.health import router as health_router
from app.api.knowledge import router as knowledge_router
from app.middleware.rate_limiter import (
    RateLimitMiddleware,
    RateLimitConfig,
    RateLimitExceeded,
    rate_limit_exceeded_handler,
)
from app.services.security_validator import get_security_validator, SecurityRisk
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Get settings
settings = get_settings()

# Create FastAPI app
app = FastAPI(
    title="AutoMecanik RAG Service",
    description="Service RAG pour le support client AutoMecanik",
    version="1.0.0",
    docs_url="/docs" if settings.debug else None,
    redoc_url="/redoc" if settings.debug else None,
)


# ============================================
# P0 SECURITY: CORS Configuration
# ============================================
def get_cors_origins() -> list[str]:
    """Get CORS origins based on environment."""
    if settings.env == "prod":
        # PROD: Use specific origins from config
        if settings.cors_origins == "*":
            logger.warning(
                "SECURITY WARNING: CORS_ORIGINS='*' in PROD. "
                "This should be set to specific domains."
            )
            return ["https://automecanik.com", "https://www.automecanik.com"]
        return [origin.strip() for origin in settings.cors_origins.split(",")]
    else:
        # DEV: Allow all origins for testing
        return ["*"]


cors_origins = get_cors_origins()
# P1 FIX: Don't use credentials with wildcard origins
allow_credentials = "*" not in cors_origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=allow_credentials,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["X-API-Key", "Content-Type", "Authorization"],
)


# ============================================
# P0 SECURITY: Rate Limiting Middleware
# ============================================
rate_limit_config = RateLimitConfig(
    requests_per_minute=settings.rate_limit_rpm,
    requests_per_hour=settings.rate_limit_rpm * 60,
)
app.add_middleware(RateLimitMiddleware, config=rate_limit_config)

# Register rate limit exception handler
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)


# ============================================
# P0 SECURITY: Security Validation Middleware
# ============================================
class SecurityValidationMiddleware:
    """
    ASGI Middleware for security validation (prompt injection + PII).

    Must be middleware (not dependency) because:
    1. We need to read the body before it's consumed
    2. Validate for injection/PII threats
    3. Replay the body so the endpoint can parse it
    """

    PROTECTED_PATHS = ["/chat", "/search"]

    def __init__(self, app):
        self.app = app
        self.validator = get_security_validator()

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        # Only validate POST/PUT to protected paths
        path = scope.get("path", "")
        method = scope.get("method", "")

        if method not in ["POST", "PUT"] or path not in self.PROTECTED_PATHS:
            await self.app(scope, receive, send)
            return

        # Read complete body
        body = b""
        more_body = True
        while more_body:
            message = await receive()
            body += message.get("body", b"")
            more_body = message.get("more_body", False)

        # Validate if we have a body
        if body:
            try:
                body_json = json.loads(body)
                message_text = body_json.get("message") or body_json.get("query") or ""

                if message_text:
                    result = self.validator.validate(message_text)

                    if not result.is_safe:
                        # Return error response
                        if result.risk == SecurityRisk.PROMPT_INJECTION:
                            logger.warning(
                                f"SECURITY: Blocked prompt injection on {path}"
                            )
                            response = JSONResponse(
                                status_code=400,
                                content={
                                    "detail": "Request blocked: potential security threat detected"
                                }
                            )
                        else:
                            logger.warning(
                                f"SECURITY: Blocked PII ({result.risk.value}) on {path}"
                            )
                            response = JSONResponse(
                                status_code=400,
                                content={
                                    "error": "PII_DETECTED",
                                    "detail": "Personal information detected. Please use support API.",
                                    "redirect_to": result.redirect_to or "support_api",
                                }
                            )
                        await response(scope, receive, send)
                        return
            except json.JSONDecodeError:
                pass  # Not JSON, skip validation

        # Create a new receive that replays the body we already read
        body_sent = False

        async def replay_receive():
            nonlocal body_sent
            if not body_sent:
                body_sent = True
                return {"type": "http.request", "body": body, "more_body": False}
            return {"type": "http.disconnect"}

        await self.app(scope, replay_receive, send)


# Add Security Validation Middleware
app.add_middleware(SecurityValidationMiddleware)


# ============================================
# P2: Request Size Limit Middleware
# ============================================
@app.middleware("http")
async def limit_request_size(request: Request, call_next):
    """Limit request body size to prevent OOM attacks."""
    content_length = request.headers.get("content-length")
    if content_length:
        if int(content_length) > settings.max_request_size:
            return JSONResponse(
                status_code=413,
                content={"detail": "Request body too large"}
            )
    return await call_next(request)


# ============================================
# P2: Request Audit Logging Middleware
# ============================================
@app.middleware("http")
async def audit_log_middleware(request: Request, call_next):
    """Log all requests for audit trail."""
    start_time = time.time()

    # Get client info
    client_ip = request.headers.get("X-Forwarded-For", request.client.host if request.client else "unknown")

    # Process request
    response = await call_next(request)

    # Calculate duration
    duration = time.time() - start_time

    # Log request (skip health checks to reduce noise)
    if request.url.path != "/health":
        logger.info(
            f"AUDIT: {request.method} {request.url.path} | "
            f"client={client_ip} | status={response.status_code} | "
            f"duration={duration:.3f}s"
        )

    return response


# ============================================
# P1: Request Timeout Header
# ============================================
@app.middleware("http")
async def add_timeout_header(request: Request, call_next):
    """Add timeout info to response headers."""
    response = await call_next(request)
    response.headers["X-Request-Timeout"] = str(settings.request_timeout)
    return response


# ============================================
# API Key + Security Validation
# ============================================
async def verify_api_key(request: Request):
    """Verify API key from request headers."""
    api_key = request.headers.get("X-API-Key")

    if not api_key or api_key != settings.rag_api_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )
    return True


# ============================================
# Include Routers
# ============================================
app.include_router(health_router, tags=["Health"])
app.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"],
    dependencies=[Depends(verify_api_key)]  # Security validation via middleware
)
app.include_router(
    search_router,
    prefix="/search",
    tags=["Search"],
    dependencies=[Depends(verify_api_key)]  # Security validation via middleware
)
app.include_router(
    knowledge_router,
    prefix="/api/knowledge",
    tags=["Knowledge Admin"],
    dependencies=[Depends(verify_api_key)]
)


# ============================================
# Startup / Shutdown Events
# ============================================
@app.on_event("startup")
async def startup_event():
    """Initialize services and validate configuration on startup."""
    logger.info(f"Starting RAG service in {settings.env} mode")
    logger.info(f"Weaviate URL: {settings.weaviate_url}")

    # P1 SECURITY: Validate Kill Switch in PROD
    if settings.env == "prod":
        if settings.ai_prod_write:
            logger.critical(
                "SECURITY CRITICAL: AI_PROD_WRITE=true in PROD environment! "
                "This violates kill switch policy. Writes are still blocked."
            )

        # Verify CORS is not wildcard
        if settings.cors_origins == "*":
            logger.warning(
                "SECURITY WARNING: CORS_ORIGINS='*' in PROD. "
                "Update .env.prod with specific domains."
            )

        # Log security status
        logger.info("PROD Security Status:")
        logger.info(f"  - CORS Origins: {cors_origins}")
        logger.info(f"  - Rate Limit: {settings.rate_limit_rpm} req/min")
        logger.info(f"  - Max Request Size: {settings.max_request_size} bytes")
        logger.info(f"  - Kill Switch Active: {not settings.can_write()}")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    logger.info("Shutting down RAG service")


# ============================================
# Exception Handlers
# ============================================
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
        reload=settings.debug,
        timeout_keep_alive=settings.request_timeout,
    )
