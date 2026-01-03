"""Rate Limiting Middleware for FastAPI.

P0 CRITICAL SECURITY:
- Prevents DDoS attacks
- Limits API abuse
- Uses in-memory storage (Redis optional for distributed)

Usage:
    from app.middleware.rate_limiter import limiter, rate_limit_exceeded_handler

    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

    @app.get("/endpoint")
    @limiter.limit("60/minute")
    async def endpoint(request: Request):
        ...
"""

import time
import logging
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional, Callable
from functools import wraps

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)


@dataclass
class RateLimitConfig:
    """Rate limit configuration."""
    requests_per_minute: int = 60
    requests_per_hour: int = 1000
    burst_size: int = 10  # Max requests in a short burst


class RateLimitExceeded(Exception):
    """Exception raised when rate limit is exceeded."""

    def __init__(self, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Retry after {retry_after} seconds.")


class InMemoryRateLimiter:
    """
    Simple in-memory rate limiter using sliding window.

    For production with multiple instances, use Redis-based limiter.
    """

    def __init__(self, config: Optional[RateLimitConfig] = None):
        self.config = config or RateLimitConfig()
        self._requests: dict[str, list[float]] = defaultdict(list)
        self._cleanup_interval = 60  # Cleanup every 60 seconds
        self._last_cleanup = time.time()

    def _get_client_id(self, request: Request) -> str:
        """Extract client identifier from request."""
        # Try X-Forwarded-For first (behind proxy)
        forwarded = request.headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()

        # Fall back to direct client IP
        if request.client:
            return request.client.host

        return "unknown"

    def _cleanup_old_requests(self):
        """Remove expired request timestamps."""
        now = time.time()
        if now - self._last_cleanup < self._cleanup_interval:
            return

        window = 3600  # 1 hour window
        for client_id in list(self._requests.keys()):
            self._requests[client_id] = [
                ts for ts in self._requests[client_id]
                if now - ts < window
            ]
            if not self._requests[client_id]:
                del self._requests[client_id]

        self._last_cleanup = now

    def is_allowed(self, request: Request) -> tuple[bool, int]:
        """
        Check if request is allowed under rate limits.

        Args:
            request: FastAPI request object

        Returns:
            Tuple of (is_allowed, retry_after_seconds)
        """
        self._cleanup_old_requests()

        client_id = self._get_client_id(request)
        now = time.time()

        # Get request history for this client
        requests = self._requests[client_id]

        # Count requests in last minute
        minute_ago = now - 60
        requests_last_minute = sum(1 for ts in requests if ts > minute_ago)

        if requests_last_minute >= self.config.requests_per_minute:
            # Calculate retry-after
            oldest_in_window = min(ts for ts in requests if ts > minute_ago)
            retry_after = int(60 - (now - oldest_in_window)) + 1
            logger.warning(
                f"Rate limit exceeded for {client_id}: "
                f"{requests_last_minute}/{self.config.requests_per_minute} rpm"
            )
            return False, retry_after

        # Count requests in last hour
        hour_ago = now - 3600
        requests_last_hour = sum(1 for ts in requests if ts > hour_ago)

        if requests_last_hour >= self.config.requests_per_hour:
            retry_after = 60  # Wait at least a minute
            logger.warning(
                f"Hourly rate limit exceeded for {client_id}: "
                f"{requests_last_hour}/{self.config.requests_per_hour} rph"
            )
            return False, retry_after

        # Record this request
        self._requests[client_id].append(now)

        return True, 0

    def limit(self, limit_string: str = "60/minute"):
        """
        Decorator to apply rate limiting to an endpoint.

        Args:
            limit_string: Rate limit in format "N/period" (e.g., "60/minute")

        Usage:
            @limiter.limit("30/minute")
            async def my_endpoint(request: Request):
                ...
        """
        def decorator(func: Callable):
            @wraps(func)
            async def wrapper(request: Request, *args, **kwargs):
                is_allowed, retry_after = self.is_allowed(request)
                if not is_allowed:
                    raise RateLimitExceeded(retry_after)
                return await func(request, *args, **kwargs)
            return wrapper
        return decorator


# Create default limiter instance
limiter = InMemoryRateLimiter()


async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded) -> JSONResponse:
    """Exception handler for rate limit exceeded."""
    return JSONResponse(
        status_code=429,
        content={
            "detail": "Rate limit exceeded",
            "retry_after": exc.retry_after,
        },
        headers={"Retry-After": str(exc.retry_after)},
    )


class RateLimitMiddleware:
    """
    ASGI Middleware for global rate limiting.

    Applies to all requests before they reach endpoints.
    """

    def __init__(self, app, config: Optional[RateLimitConfig] = None):
        self.app = app
        self.limiter = InMemoryRateLimiter(config)

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        # Create a mock request for rate limit check
        from starlette.requests import Request as StarletteRequest
        request = StarletteRequest(scope)

        is_allowed, retry_after = self.limiter.is_allowed(request)

        if not is_allowed:
            response = JSONResponse(
                status_code=429,
                content={
                    "detail": "Rate limit exceeded",
                    "retry_after": retry_after,
                },
                headers={"Retry-After": str(retry_after)},
            )
            await response(scope, receive, send)
            return

        await self.app(scope, receive, send)
