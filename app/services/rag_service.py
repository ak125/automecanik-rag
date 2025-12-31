"""RAG Service - Orchestrates search and generation."""

import logging
from typing import Optional
from dataclasses import dataclass

from app.services.weaviate_client import get_weaviate_client
from app.services.claude_client import get_claude_client
from app.config import get_settings

logger = logging.getLogger(__name__)


@dataclass
class ChatResponse:
    """Response from chat endpoint."""
    answer: str
    sources: list[str]
    session_id: str
    confidence: float


@dataclass
class SearchResponse:
    """Response from search endpoint."""
    results: list[dict]
    query: str
    total: int


class RAGService:
    """
    RAG Service - Simple pipeline: Search → Format → Generate.

    This is the MVP version without LangGraph.
    """

    MIN_RESULTS_FOR_ANSWER = 1
    MIN_CONFIDENCE_THRESHOLD = 0.5

    def __init__(self):
        """Initialize RAG service."""
        self.weaviate = get_weaviate_client()
        self.claude = get_claude_client()
        self.settings = get_settings()

    async def chat(
        self,
        message: str,
        session_id: str,
        context: Optional[dict] = None,
    ) -> ChatResponse:
        """
        Process chat message through RAG pipeline.

        Args:
            message: User message
            session_id: Session identifier
            context: Optional additional context

        Returns:
            ChatResponse with answer and sources
        """
        logger.info(f"Processing chat message: {message[:100]}...")

        # Step 1: Search in Weaviate
        results = await self.weaviate.hybrid_search(
            query=message,
            limit=self.settings.retrieval_top_k,
            alpha=self.settings.retrieval_alpha,
        )

        # Step 2: Calculate confidence based on results
        if not results:
            confidence = 0.0
        else:
            avg_score = sum(r["score"] for r in results) / len(results)
            confidence = min(avg_score, 1.0)

        # Step 3: Format context from results
        context_text = self._format_context(results)

        # Step 4: Generate response with Claude
        answer = await self.claude.generate(
            user_message=message,
            context=context_text,
        )

        # Step 5: Extract sources
        sources = [r["source_path"] for r in results if r.get("source_path")]

        return ChatResponse(
            answer=answer,
            sources=sources,
            session_id=session_id,
            confidence=confidence,
        )

    async def search(
        self,
        query: str,
        limit: int = 10,
        filters: Optional[dict] = None,
    ) -> SearchResponse:
        """
        Perform semantic search without generation.

        Args:
            query: Search query
            limit: Max results
            filters: Optional filters

        Returns:
            SearchResponse with results
        """
        logger.info(f"Processing search query: {query[:100]}...")

        results = await self.weaviate.hybrid_search(
            query=query,
            limit=limit,
        )

        return SearchResponse(
            results=results,
            query=query,
            total=len(results),
        )

    def _format_context(self, results: list[dict]) -> str:
        """
        Format search results into context string for LLM.

        Args:
            results: List of search results

        Returns:
            Formatted context string
        """
        if not results:
            return ""

        context_parts = []
        for i, result in enumerate(results, 1):
            title = result.get("title", "Sans titre")
            content = result.get("content", "")
            source = result.get("source_path", "")
            score = result.get("score", 0)

            context_parts.append(
                f"[Source {i}] {title}\n"
                f"Pertinence: {score:.2f}\n"
                f"Fichier: {source}\n"
                f"Contenu:\n{content}\n"
            )

        return "\n---\n".join(context_parts)


# Singleton instance
_rag_service: Optional[RAGService] = None


def get_rag_service() -> RAGService:
    """Get or create RAG service instance."""
    global _rag_service
    if _rag_service is None:
        _rag_service = RAGService()
    return _rag_service
