"""Chat endpoint for RAG conversations."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import uuid
import logging

from app.services.rag_service import get_rag_service

logger = logging.getLogger(__name__)
router = APIRouter()


class ChatRequest(BaseModel):
    """Request body for chat endpoint."""
    message: str = Field(..., min_length=1, max_length=2000, description="User message")
    session_id: Optional[str] = Field(None, description="Session ID for conversation continuity")
    context: Optional[dict] = Field(None, description="Additional context (vehicle, category, etc.)")


class ChatResponse(BaseModel):
    """Response body for chat endpoint."""
    answer: str = Field(..., description="Generated answer")
    sources: list[str] = Field(default_factory=list, description="Source file paths")
    session_id: str = Field(..., description="Session ID")
    confidence: float = Field(..., ge=0, le=1, description="Confidence score")


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Process a chat message through the RAG pipeline.

    1. Search relevant documents in Weaviate
    2. Format context from results
    3. Generate response with Claude
    4. Return answer with sources

    Args:
        request: Chat request with message and optional context

    Returns:
        ChatResponse with answer, sources, and confidence
    """
    try:
        # Generate session ID if not provided
        session_id = request.session_id or str(uuid.uuid4())

        # Get RAG service and process
        rag_service = get_rag_service()
        result = await rag_service.chat(
            message=request.message,
            session_id=session_id,
            context=request.context,
        )

        return ChatResponse(
            answer=result.answer,
            sources=result.sources,
            session_id=result.session_id,
            confidence=result.confidence,
        )

    except Exception as e:
        logger.error(f"Chat error: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Error processing chat message"
        )
