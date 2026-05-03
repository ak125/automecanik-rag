"""Phase F.5 (ADR-031) — KB_Knowledge_v2 schema specification tests.

Pure-Python tests on the static schema spec. Live Weaviate behaviour is
exercised in CI integration tests (separate suite that requires a running
Weaviate instance).
"""

from __future__ import annotations

import pytest

from app.services.weaviate_v2_schema import (
    ALLOWED_CANONICAL_SOURCES,
    ALLOWED_ORIGIN_BATCH_KINDS,
    ALLOWED_SOURCE_LAYERS,
    FILTERABLE_PROPERTIES_V2,
    KB_KNOWLEDGE_V2,
    PROPERTY_NAMES_V2,
    build_v2_property_specs,
    is_natural_key_complete,
)


def test_collection_name_is_v2():
    assert KB_KNOWLEDGE_V2 == "KB_Knowledge_v2"


def test_property_count_is_14():
    """Phase F.5 plan canonical : 8 existing + 6 new = 14 properties."""
    specs = build_v2_property_specs()
    assert len(specs) == 14
    assert len(PROPERTY_NAMES_V2) == 14


def test_six_new_f5_properties_present():
    spec_names = {s["name"] for s in build_v2_property_specs()}
    new_six = {
        "canonical_source",
        "source_layer",
        "source_commit",
        "lineage_id",
        "embedding_model",
        "origin_batch_kind",
    }
    assert new_six.issubset(spec_names)


def test_eight_existing_properties_preserved():
    spec_names = {s["name"] for s in build_v2_property_specs()}
    existing = {
        "content",
        "title",
        "source_path",
        "source_type",
        "truth_level",
        "namespace",
        "chunk_index",
        "content_hash",
    }
    assert existing.issubset(spec_names)


def test_natural_key_fields_are_filterable():
    """Idempotency natural key (canonical_source, source_path, content_hash,
    chunk_index) MUST all be filterable for the `WHERE And` query to be
    usable."""
    natural_key = {"canonical_source", "source_path", "content_hash", "chunk_index"}
    filterable = {
        s["name"] for s in build_v2_property_specs() if s.get("indexFilterable")
    }
    missing = natural_key - filterable
    assert not missing, f"non-filterable natural key fields: {missing}"


def test_embedding_model_is_filterable_for_reindex_discriminator():
    """A model change should let us SELECT chunks for selective re-indexation."""
    filterable = {
        s["name"] for s in build_v2_property_specs() if s.get("indexFilterable")
    }
    assert "embedding_model" in filterable


def test_lineage_id_filterable_for_batch_rollback():
    """Rolling back an entire batch is `DELETE WHERE lineage_id = X` — fast iff filterable."""
    filterable = {
        s["name"] for s in build_v2_property_specs() if s.get("indexFilterable")
    }
    assert "lineage_id" in filterable


def test_content_searchable_only():
    """Full-text content does NOT need indexFilterable — it has indexSearchable.
    Filterable on a TEXT column with high cardinality wastes inverted-index space."""
    specs = {s["name"]: s for s in build_v2_property_specs()}
    assert specs["content"]["indexFilterable"] is False
    assert specs["content"]["indexSearchable"] is True


def test_filterable_set_consistent_with_specs():
    """The exported FILTERABLE_PROPERTIES_V2 set should match the specs."""
    spec_filterable = {
        s["name"] for s in build_v2_property_specs() if s.get("indexFilterable")
    }
    # FILTERABLE_PROPERTIES_V2 may be a strict superset (ops who want extra
    # filter columns) — but every spec-filterable must be in the set.
    assert spec_filterable.issubset(FILTERABLE_PROPERTIES_V2)


def test_canonical_source_allowed_values():
    assert ALLOWED_CANONICAL_SOURCES == {"automecanik-wiki", "legacy-rag-knowledge"}


def test_source_layer_allowed_values():
    assert ALLOWED_SOURCE_LAYERS == {"exports/rag", "knowledge"}


def test_origin_batch_kind_allowed_values():
    assert ALLOWED_ORIGIN_BATCH_KINDS == {"legacy_migration", "wiki_import"}


def test_is_natural_key_complete_true_when_all_fields_present():
    props = {
        "canonical_source": "automecanik-wiki",
        "source_path": "gammes/plaquette-de-frein.md",
        "content_hash": "abc123",
        "chunk_index": 0,
    }
    assert is_natural_key_complete(props) is True


@pytest.mark.parametrize("missing", [
    "canonical_source",
    "source_path",
    "content_hash",
    "chunk_index",
])
def test_is_natural_key_complete_false_when_any_field_missing(missing):
    base = {
        "canonical_source": "automecanik-wiki",
        "source_path": "gammes/plaquette-de-frein.md",
        "content_hash": "abc123",
        "chunk_index": 0,
    }
    base[missing] = None
    assert is_natural_key_complete(base) is False
