"""Tests for Verified RAG fields exposed by API endpoints."""

from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.rag_service import SearchResponse, TruthMetadata


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def api_key_header():
    return {"X-RAG-API-Key": "test-api-key"}


def _mock_result_partial() -> SearchResponse:
    return SearchResponse(
        results=[
            {
                "title": "ECE R90 definition",
                "content": "ECE R90 est une norme de securite pour les plaquettes et disques.",
                "source_path": "knowledge/normes/ece-r90.md",
                "source_uri": "file://knowledge/normes/ece-r90.md",
                "source_ref": "#p12-13",
                "source_type": "md",
                "doc_family": "knowledge",
                "category": "normes",
                "score": 0.79,
                "truth_level": "L2",
                "verification_status": "verified",
                "collection": "KB_Knowledge",
                "chunk_id": "chunk-ece-r90-12-13",
                "is_canonical": True,
            }
        ],
        query="definition ece r90",
        total=1,
        context="partial context",
        truth_metadata=TruthMetadata(
            composition={"L1": 0, "L2": 1, "L3": 0, "L4": 0},
            dominant_level="L2",
            composite_confidence=0.66,
            reasoning_chain=[
                "mode=partial fallback=True reason=low_scores_or_low_evidence",
                "evidence_diversified=1/3",
                "Auto-improvement: proposer un chunk canonical (intent=define, domain=freinage, canonical_hits=1)",
            ],
        ),
        needs_clarification=True,
        clarify_questions=[
            "Voulez-vous une definition courte ou detaillee ?",
            "Vous parlez de quel composant exactement ?",
            "Cette question ne doit pas sortir (cap a 2).",
        ],
        response_mode="partial",
        sources_citation="## Sources\n1. [L2] ECE R90 definition (ece-r90.md) - Vérification: verified | Score: 0.79",
    )


@patch("app.main.settings.rag_api_key", "test-api-key")
@patch("app.api.search.get_rag_service")
def test_search_returns_verified_rag_fields(mock_get_rag_service, client, api_key_header):
    mock_service = AsyncMock()
    mock_service.search.return_value = _mock_result_partial()
    mock_get_rag_service.return_value = mock_service

    response = client.post(
        "/search",
        json={"query": "definition ece r90", "limit": 5},
        headers=api_key_header,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["response_mode"] == "partial"
    assert data["needs_clarification"] is True
    assert len(data["clarify_questions"]) == 2
    assert data["sources_citation"].startswith("## Sources")
    assert data["truth_metadata"]["composite_confidence"] == 0.66


@patch("app.main.settings.rag_api_key", "test-api-key")
@patch("app.api.chat.get_rag_service")
def test_chat_v1_returns_verified_rag_fields(mock_get_rag_service, client, api_key_header):
    mock_service = AsyncMock()
    mock_service.search.return_value = _mock_result_partial()
    mock_get_rag_service.return_value = mock_service

    response = client.post(
        "/chat",
        json={"message": "definition ece r90", "limit": 5},
        headers=api_key_header,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["response_mode"] == "partial"
    assert data["needs_clarification"] is True
    assert len(data["clarify_questions"]) == 2
    assert data["sources_citation"].startswith("## Sources")
