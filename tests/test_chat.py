"""Tests for chat endpoint."""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock

from app.main import app
from app.services.rag_service import ChatResponse


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


@pytest.fixture
def api_key_header():
    """API key header for authenticated requests."""
    return {"X-API-Key": "test-api-key"}


class TestHealthEndpoint:
    """Tests for health endpoint."""

    def test_health_check(self, client):
        """Test health endpoint returns 200."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"


class TestChatEndpoint:
    """Tests for chat endpoint."""

    @patch("app.main.get_settings")
    @patch("app.api.chat.get_rag_service")
    def test_chat_success(self, mock_rag_service, mock_settings, client, api_key_header):
        """Test successful chat request."""
        # Mock settings
        mock_settings.return_value.rag_api_key = "test-api-key"

        # Mock RAG service response
        mock_service = AsyncMock()
        mock_service.chat.return_value = ChatResponse(
            answer="La livraison prend 24-48h.",
            sources=["faq/livraison.md"],
            session_id="test-session",
            confidence=0.85,
        )
        mock_rag_service.return_value = mock_service

        response = client.post(
            "/chat",
            json={"message": "Quels sont les délais de livraison?"},
            headers=api_key_header,
        )

        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert "sources" in data
        assert "session_id" in data

    def test_chat_without_api_key(self, client):
        """Test chat request without API key returns 401."""
        response = client.post(
            "/chat",
            json={"message": "Test message"},
        )
        assert response.status_code == 401

    def test_chat_empty_message(self, client, api_key_header):
        """Test chat with empty message returns 422."""
        response = client.post(
            "/chat",
            json={"message": ""},
            headers=api_key_header,
        )
        assert response.status_code == 422
