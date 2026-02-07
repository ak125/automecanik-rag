"""Chat endpoint - Returns context with Truth Levels.

ARCHITECTURE:
- v1 (POST /chat): Mode Context-Only - Pas de génération LLM
- v2 (POST /chat/v2): Mode LangGraph - Full pipeline avec guardrails + génération

SECURITY:
- Namespace is HARDCODED to knowledge:faq in production
- No namespace parameter exposed to API
- NamespaceGuard validates all requests
- LangGraph v2 adds classify node for off-topic detection
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import uuid
import logging

from app.services.rag_service import get_rag_service
from app.services.namespace_guard import get_namespace_guard
from app.services.langgraph_flow import run_chat_pipeline
from app.config import get_settings

logger = logging.getLogger(__name__)
router = APIRouter()

# HARDCODED namespace for production chatbot - NOT configurable via API
PROD_CHATBOT_NAMESPACE = "knowledge:faq"


class ChatRequest(BaseModel):
    """Request body for chat endpoint - Context-Only mode."""
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
    """Response body for chat endpoint - Context-Only mode."""
    context: str = Field(..., description="Formatted context from knowledge base")
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
    Get RAG context with Truth Levels (Context-Only Mode).

    Le chatbot répond uniquement à partir de la source de vérité.
    Pas de génération LLM - le frontend formate le contexte.

    1. Search relevant documents in Weaviate
    2. Analyze truth levels (L1-L4)
    3. Format context with truth indicators
    4. Return context + truth metadata

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

        # Context-Only: Return context directly, no LLM generation
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


# =============================================================================
# V2: LangGraph Pipeline with Guardrails + Generation
# =============================================================================

class ChatRequestV2(BaseModel):
    """Request body for chat v2 endpoint - LangGraph mode."""
    message: str = Field(..., min_length=1, max_length=2000, description="User message")
    session_id: Optional[str] = Field(None, description="Session ID for tracking")
    locale: str = Field("fr", description="User locale (fr/en)")


class ChatResponseV2(BaseModel):
    """Response body for chat v2 endpoint - LangGraph mode."""
    response: str = Field(..., description="Generated response or refusal message")
    citations: list[str] = Field(default_factory=list, description="Citations from sources")
    sources: list[str] = Field(default_factory=list, description="Source file paths")
    session_id: str = Field(..., description="Session ID")
    # Classification and guardrails
    query_type: Optional[str] = Field(None, description="Query type: on_topic, off_topic, ambiguous")
    passed_guardrails: bool = Field(False, description="Whether query passed guardrails")
    refusal_reason: Optional[str] = Field(None, description="Reason for refusal if any")
    # Truth metadata
    truth_metadata: dict = Field(default_factory=dict, description="Truth level metadata")
    # Error info
    error: Optional[str] = Field(None, description="Error message if any")


@router.post("/v2", response_model=ChatResponseV2)
async def chat_v2(request: ChatRequestV2):
    """
    Chat with LangGraph pipeline (Full Generation Mode).

    Flow: classify → retrieve → guardrails → generate/refuse

    1. Classify query (on-topic, off-topic, ambiguous)
    2. Retrieve relevant documents from Weaviate
    3. Apply guardrails (score >= 0.70, results >= 3)
    4. Generate response with Claude OR refuse with helpful message

    Guardrails:
    - Off-topic queries are refused immediately
    - Score < 0.70 triggers refusal
    - < 3 results triggers refusal for ambiguous queries

    Args:
        request: Chat request with message and locale

    Returns:
        ChatResponseV2 with response, citations, and metadata
    """
    try:
        session_id = request.session_id or str(uuid.uuid4())
        settings = get_settings()

        # Log request
        logger.info(f"Chat v2 request - session={session_id}, locale={request.locale}")

        # Check if LangGraph is enabled
        if not settings.langgraph_enabled:
            raise HTTPException(
                status_code=503,
                detail="LangGraph pipeline is disabled"
            )

        # Run the full LangGraph pipeline
        result = await run_chat_pipeline(
            query=request.message,
            session_id=session_id,
            user_locale=request.locale,
        )

        # Log result
        logger.info(
            f"Chat v2 result - session={session_id}, "
            f"type={result.get('query_type')}, "
            f"guardrails={result.get('passed_guardrails')}, "
            f"refusal={result.get('refusal_reason')}"
        )

        return ChatResponseV2(
            response=result.get("response", ""),
            citations=result.get("citations", []),
            sources=result.get("sources", []),
            session_id=session_id,
            query_type=result.get("query_type"),
            passed_guardrails=result.get("passed_guardrails", False),
            refusal_reason=result.get("refusal_reason"),
            truth_metadata=result.get("truth_metadata", {}),
            error=result.get("error"),
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Chat v2 error: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Error processing chat request"
        )
