"""Chat endpoint - Returns context with Truth Levels for Claude CLI (Semantic Brain).

SECURITY:
- Namespace is HARDCODED to knowledge:faq in production
- No namespace parameter exposed to API
- NamespaceGuard validates all requests
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import uuid
import logging

from app.services.rag_service import get_rag_service
from app.services.namespace_guard import get_namespace_guard
from app.config import get_settings

logger = logging.getLogger(__name__)
router = APIRouter()

# HARDCODED namespace for production chatbot - NOT configurable via API
PROD_CHATBOT_NAMESPACE = "knowledge:faq"


class ChatRequest(BaseModel):
    """Request body for chat endpoint."""
    message: str = Field(..., min_length=1, max_length=2000, description="User message")
    session_id: Optional[str] = Field(None, description="Session ID for tracking")
    limit: int = Field(5, ge=1, le=20, description="Number of sources to retrieve")


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


class ChatResponse(BaseModel):
    """Response body for chat endpoint with Semantic Brain metadata."""
    context: str = Field(..., description="Formatted context for Claude CLI")
    sources: list[str] = Field(default_factory=list, description="Source file paths")
    session_id: str = Field(..., description="Session ID")
    total_sources: int = Field(0, description="Number of relevant sources found")
    # Semantic Brain - Truth Level metadata
    truth_metadata: TruthMetadataResponse = Field(
        default_factory=TruthMetadataResponse,
        description="Truth level analysis (L1-L4)"
    )


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Get RAG context with Truth Levels for Claude CLI (Semantic Brain).

    1. Search relevant documents in Weaviate
    2. Analyze truth levels (L1-L4)
    3. Format context with truth indicators
    4. Return context + truth metadata for Claude CLI

    Truth Levels:
    - L1: Faits vérifiés (documentation officielle)
    - L2: Règles métier (procédures établies)
    - L3: Hypothèses (inférences raisonnées)
    - L4: Heuristiques (approximations empiriques)

    Args:
        request: Chat request with message

    Returns:
        ChatResponse with context, sources, and truth metadata
    """
    try:
        session_id = request.session_id or str(uuid.uuid4())
        settings = get_settings()

        # P0 SECURITY: Validate namespace access
        # In PROD, namespace is HARDCODED - no user input accepted
        namespace_guard = get_namespace_guard()
        namespace = namespace_guard.get_default_namespace()

        # Log namespace usage for security audit
        if settings.is_runtime_plane:
            logger.info(
                f"PROD chat request - namespace={namespace}, session={session_id}"
            )

        # Validate namespace access (will raise PermissionError if denied)
        namespace_guard.validate(namespace)

        rag_service = get_rag_service()
        result = await rag_service.search(
            query=request.message,
            limit=request.limit,
            namespace=namespace,  # Pass validated namespace
        )

        sources = [r.get("source_path", "") for r in result.results if r.get("source_path")]

        # Convert truth metadata to response format
        truth_metadata = TruthMetadataResponse(
            composition=TruthComposition(**result.truth_metadata.composition),
            dominant_level=result.truth_metadata.dominant_level,
            composite_confidence=result.truth_metadata.composite_confidence,
            mixing_warning=result.truth_metadata.mixing_warning,
            contradictions=result.truth_metadata.contradictions,
            reasoning_chain=result.truth_metadata.reasoning_chain,
        )

        return ChatResponse(
            context=result.context,
            sources=sources,
            session_id=session_id,
            total_sources=result.total,
            truth_metadata=truth_metadata,
        )

    except PermissionError as e:
        # P0 SECURITY: Namespace access denied
        logger.error(f"Namespace access denied: {e}")
        raise HTTPException(
            status_code=403,
            detail="Access denied to requested namespace"
        )
    except Exception as e:
        logger.error(f"Chat error: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Error retrieving context"
        )
