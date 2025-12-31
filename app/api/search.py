"""Search endpoint for semantic search."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import logging

from app.services.rag_service import get_rag_service

logger = logging.getLogger(__name__)
router = APIRouter()


class SearchRequest(BaseModel):
    """Request body for search endpoint."""
    query: str = Field(..., min_length=1, max_length=500, description="Search query")
    limit: int = Field(10, ge=1, le=50, description="Maximum number of results")
    filters: Optional[dict] = Field(None, description="Optional filters")


class SearchResult(BaseModel):
    """Single search result."""
    title: str
    content: str
    source_path: str
    source_type: str
    category: str
    score: float


class SearchResponse(BaseModel):
    """Response body for search endpoint."""
    results: list[SearchResult] = Field(default_factory=list)
    query: str
    total: int


@router.post("", response_model=SearchResponse)
async def search(request: SearchRequest):
    """
    Perform semantic search without generation.

    Uses hybrid search (BM25 + vector) in Weaviate.

    Args:
        request: Search request with query and optional filters

    Returns:
        SearchResponse with matching documents
    """
    try:
        rag_service = get_rag_service()
        result = await rag_service.search(
            query=request.query,
            limit=request.limit,
            filters=request.filters,
        )

        return SearchResponse(
            results=[
                SearchResult(
                    title=r.get("title", ""),
                    content=r.get("content", "")[:500] + "..." if len(r.get("content", "")) > 500 else r.get("content", ""),
                    source_path=r.get("source_path", ""),
                    source_type=r.get("source_type", ""),
                    category=r.get("category", ""),
                    score=r.get("score", 0),
                )
                for r in result.results
            ],
            query=result.query,
            total=result.total,
        )

    except Exception as e:
        logger.error(f"Search error: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Error processing search query"
        )
