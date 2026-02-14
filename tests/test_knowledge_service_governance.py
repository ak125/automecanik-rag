"""Tests for strict doc_family governance in KnowledgeService."""

from pathlib import Path

import frontmatter
import pytest

from app.services.knowledge_service import KnowledgeService


def _service_for_tmp(tmp_path: Path) -> KnowledgeService:
    service = KnowledgeService()
    service.knowledge_path = tmp_path
    return service


def test_infer_category_uses_family_subdirectory():
    service = KnowledgeService()
    assert service._infer_category("diagnostic/freinage/vibration-au-freinage.md") == "freinage"  # noqa: SLF001
    assert service._infer_category("knowledge/glossary/freinage__ece-r90.md") == "glossary"  # noqa: SLF001


def test_resolve_doc_family_from_source_type():
    service = KnowledgeService()
    assert service._resolve_doc_family("diagnostic") == "diagnostic"  # noqa: SLF001
    assert service._resolve_doc_family("gamme") == "catalog"  # noqa: SLF001
    assert service._resolve_doc_family("faq") == "knowledge"  # noqa: SLF001
    assert service._resolve_doc_family("video") == "media"  # noqa: SLF001


def test_create_document_blocks_mismatched_doc_family(tmp_path: Path):
    service = _service_for_tmp(tmp_path)
    with pytest.raises(ValueError):
        service.create_document(
            title="Brake vibration",
            content="Symptomes: vibration au freinage",
            source_type="diagnostic",
            category="freinage",
            doc_family="catalog",
            truth_level="L2",
        )


def test_create_document_persists_doc_family(tmp_path: Path):
    service = _service_for_tmp(tmp_path)
    doc = service.create_document(
        title="Bruit au freinage",
        content="Symptomes: bruit et vibration",
        source_type="diagnostic",
        category="freinage",
        doc_family="diagnostic",
        truth_level="L2",
    )
    assert doc is not None
    assert doc.doc_family == "diagnostic"

    saved = frontmatter.load(tmp_path / doc.source_path)
    assert saved.metadata["doc_family"] == "diagnostic"
