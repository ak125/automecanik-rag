"""Search endpoint with Truth Levels (Semantic Brain)."""

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
    """Single search result with truth level."""
    title: str
    content: str
    source_path: str
    source_type: str
    category: str
    score: float
    # Truth Level properties (Semantic Brain L1-L4)
    truth_level: str = Field("L3", description="Truth level: L1|L2|L3|L4")
    verification_status: str = Field("unverified", description="verified|unverified|disputed")
    confidence_score: float = Field(0.5, description="Source confidence 0-1")


class TruthComposition(BaseModel):
    """Truth level composition of sources."""
    L1: int = Field(0, description="Faits vérifiés count")
    L2: int = Field(0, description="Règles métier count")
    L3: int = Field(0, description="Hypothèses count")
    L4: int = Field(0, description="Heuristiques count")


class TruthMetadataResponse(BaseModel):
    """Truth level metadata in response."""
    composition: TruthComposition = Field(default_factory=TruthComposition)
    dominant_level: str = Field("L3", description="Most frequent truth level")
    composite_confidence: float = Field(0.5, description="Weighted confidence score 0-1")
    mixing_warning: Optional[str] = Field(None, description="Warning if mixing rules violated")
    contradictions: list[str] = Field(default_factory=list, description="Detected contradictions")
    reasoning_chain: list[str] = Field(default_factory=list, description="Explainable reasoning")


class SearchResponse(BaseModel):
    """Response body for search endpoint with Semantic Brain metadata."""
    results: list[SearchResult] = Field(default_factory=list)
    query: str
    total: int
    context: str = Field("", description="Formatted context for Claude CLI")
    # Semantic Brain - Truth Level metadata
    truth_metadata: TruthMetadataResponse = Field(
        default_factory=TruthMetadataResponse,
        description="Truth level analysis (L1-L4)"
    )


@router.post("", response_model=SearchResponse)
async def search(request: SearchRequest):
    """
    Perform semantic search with Truth Levels (Semantic Brain).

    Uses hybrid search (BM25 + vector) in Weaviate with truth level analysis.

    Truth Levels:
    - L1: Faits vérifiés (documentation officielle)
    - L2: Règles métier (procédures établies)
    - L3: Hypothèses (inférences raisonnées)
    - L4: Heuristiques (approximations empiriques)

    Args:
        request: Search request with query and optional filters

    Returns:
        SearchResponse with matching documents and truth metadata
    """
    try:
        rag_service = get_rag_service()
        result = await rag_service.search(
            query=request.query,
            limit=request.limit,
            filters=request.filters,
        )

        # Convert truth metadata to response format
        truth_metadata = TruthMetadataResponse(
            composition=TruthComposition(**result.truth_metadata.composition),
            dominant_level=result.truth_metadata.dominant_level,
            composite_confidence=result.truth_metadata.composite_confidence,
            mixing_warning=result.truth_metadata.mixing_warning,
            contradictions=result.truth_metadata.contradictions,
            reasoning_chain=result.truth_metadata.reasoning_chain,
        )

        return SearchResponse(
            results=[
                SearchResult(
                    title=r.get("title", ""),
                    content=(
                        r.get("content", "")[:500] + "..."
                        if len(r.get("content", "")) > 500
                        else r.get("content", "")
                    ),
                    source_path=r.get("source_path", ""),
                    source_type=r.get("source_type", ""),
                    category=r.get("category", ""),
                    score=r.get("score", 0),
                    # Truth Level properties
                    truth_level=r.get("truth_level", "L3"),
                    verification_status=r.get("verification_status", "unverified"),
                    confidence_score=r.get("confidence_score", 0.5),
                )
                for r in result.results
            ],
            query=result.query,
            total=result.total,
            context=result.context,
            truth_metadata=truth_metadata,
        )

    except Exception as e:
        logger.error(f"Search error: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Error processing search query"
        )
