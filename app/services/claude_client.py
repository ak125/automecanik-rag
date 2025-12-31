"""Claude API client for LLM generation."""

import logging
from typing import Optional
from anthropic import Anthropic

from app.config import get_settings
from app.prompts.templates import SYSTEM_PROMPT, NO_CONTEXT_RESPONSE

logger = logging.getLogger(__name__)


class ClaudeClient:
    """Client for Anthropic Claude API."""

    def __init__(self):
        """Initialize Claude client."""
        settings = get_settings()
        self.client = Anthropic(api_key=settings.anthropic_api_key)
        self.model = settings.rag_model
        self.max_tokens = settings.max_tokens
        self.temperature = settings.temperature

    async def generate(
        self,
        user_message: str,
        context: str,
        system_prompt: Optional[str] = None,
    ) -> str:
        """
        Generate response using Claude.

        Args:
            user_message: User's question
            context: Retrieved context from RAG
            system_prompt: Optional custom system prompt

        Returns:
            Generated response text
        """
        if not context or context.strip() == "":
            logger.warning("No context provided for generation")
            return NO_CONTEXT_RESPONSE

        # Format system prompt with context
        prompt = (system_prompt or SYSTEM_PROMPT).format(context=context)

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=prompt,
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )

            answer = response.content[0].text
            logger.info(f"Generated response for '{user_message[:50]}...'")
            return answer

        except Exception as e:
            logger.error(f"Claude generation error: {e}")
            raise

    async def health_check(self) -> dict:
        """Check Claude API health."""
        try:
            # Simple test call
            response = self.client.messages.create(
                model=self.model,
                max_tokens=10,
                messages=[{"role": "user", "content": "test"}]
            )
            return {
                "status": "healthy",
                "model": self.model,
            }
        except Exception as e:
            logger.error(f"Claude health check failed: {e}")
            return {
                "status": "unhealthy",
                "error": str(e),
            }


# Singleton instance
_claude_client: Optional[ClaudeClient] = None


def get_claude_client() -> ClaudeClient:
    """Get or create Claude client instance."""
    global _claude_client
    if _claude_client is None:
        _claude_client = ClaudeClient()
    return _claude_client
