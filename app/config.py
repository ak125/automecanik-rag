"""Configuration settings for RAG service."""

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Environment
    env: str = "dev"
    debug: bool = False

    # Weaviate Vector Database
    weaviate_url: str = "http://weaviate:8080"
    weaviate_api_key: str = ""

    # Redis Cache
    redis_url: str = "redis://redis:6379"

    # Anthropic Claude
    anthropic_api_key: str
    rag_model: str = "claude-3-5-sonnet-20241022"
    max_tokens: int = 1024
    temperature: float = 0.3

    # OpenAI Embeddings
    openai_api_key: str

    # API Security
    rag_api_key: str

    # RAG Settings
    retrieval_top_k: int = 5
    retrieval_alpha: float = 0.7  # 70% vectoriel, 30% BM25
    min_score_threshold: float = 0.5

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
