"""Tests for raw-content cleaning and auto-classification in KnowledgeService."""

from app.services.knowledge_service import KnowledgeService


def test_clean_raw_content_removes_noise_and_duplicates():
    service = KnowledgeService()
    raw = """
---
title: Ignore me
---
Cookie
Accepter tous les cookies
Bruit au freinage sur Clio 4.
Bruit au freinage sur Clio 4.

  Vibration dans la pedale.   
"""
    cleaned = service._clean_raw_content(raw)

    assert "Cookie" not in cleaned
    assert "Accepter tous les cookies" not in cleaned
    assert cleaned.count("Bruit au freinage sur Clio 4.") == 1
    assert "Vibration dans la pedale." in cleaned


def test_auto_classification_from_raw_content():
    service = KnowledgeService()
    raw = "Symptomes: bruit de freinage, vibration, controle des plaquettes et disques."
    cleaned = service._clean_raw_content(raw)

    source_type = service._infer_source_type_from_content(cleaned)
    category = service._infer_category_from_content(source_type, cleaned)

    assert source_type == "diagnostic"
    assert category == "freinage"
