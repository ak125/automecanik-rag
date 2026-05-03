"""Phase F.5 (ADR-031) — import_wiki_exports.py filter & idempotence tests.

Pure-Python tests : exercises the parser, schema validator, and filter
logic on the local fixtures under tests/fixtures/wiki_exports/. Live
Weaviate behaviour (insert + idempotency check) is exercised in CI
integration tests against the docker-compose Weaviate instance.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

# Module under test
from scripts.importers import import_wiki_exports as importer
from app.models.wiki_frontmatter import WikiExportFrontmatter

from pydantic import TypeAdapter, ValidationError


FIXTURES_DIR = Path(__file__).parent / "fixtures" / "wiki_exports"
_VALIDATOR = TypeAdapter(WikiExportFrontmatter)


# ---------------------------------------------------------------------------
# Frontmatter parsing + Pydantic schema validation
# ---------------------------------------------------------------------------


def test_valid_gamme_frontmatter_parses_and_validates():
    fm = importer.parse_frontmatter_yaml(FIXTURES_DIR / "gamme/valid-plaquette-de-frein.md")
    assert fm is not None
    obj = _VALIDATOR.validate_python(fm)
    assert obj.entity_type == "gamme"
    assert obj.slug == "plaquette-de-frein"
    assert obj.truth_level == "L1"
    assert obj.review_status == "approved"
    assert obj.exportable.rag is True


def test_valid_vehicle_frontmatter_parses_and_validates():
    fm = importer.parse_frontmatter_yaml(FIXTURES_DIR / "vehicle/valid-renault-clio-3.md")
    assert fm is not None
    obj = _VALIDATOR.validate_python(fm)
    assert obj.entity_type == "vehicle"
    assert obj.brand == "Renault"
    assert obj.year == 2008


def test_pydantic_rejects_unknown_entity_type():
    bad = {
        "schema_version": "1.0.0",
        "entity_type": "unknown_thing",
        "slug": "x",
        "title": "x",
        "truth_level": "L1",
        "review_status": "approved",
        "content_hash": "0" * 64,
        "source_refs": [{"id": "x"}],
    }
    with pytest.raises(ValidationError):
        _VALIDATOR.validate_python(bad)


def test_pydantic_rejects_truth_level_l5():
    bad = {
        "schema_version": "1.0.0",
        "entity_type": "gamme",
        "slug": "x",
        "title": "x",
        "truth_level": "L5",  # not in enum
        "review_status": "approved",
        "content_hash": "0" * 64,
        "source_refs": [{"id": "x"}],
    }
    with pytest.raises(ValidationError):
        _VALIDATOR.validate_python(bad)


def test_pydantic_rejects_short_content_hash():
    bad = {
        "schema_version": "1.0.0",
        "entity_type": "gamme",
        "slug": "x",
        "title": "x",
        "truth_level": "L1",
        "review_status": "approved",
        "content_hash": "tooshort",
        "source_refs": [{"id": "x"}],
    }
    with pytest.raises(ValidationError):
        _VALIDATOR.validate_python(bad)


def test_pydantic_rejects_extra_top_level_fields():
    """`extra="forbid"` surfaces schema drift early."""
    bad = {
        "schema_version": "1.0.0",
        "entity_type": "gamme",
        "slug": "x",
        "title": "x",
        "truth_level": "L1",
        "review_status": "approved",
        "content_hash": "0" * 64,
        "source_refs": [{"id": "x"}],
        "this_field_is_not_in_schema": "drift",
    }
    with pytest.raises(ValidationError):
        _VALIDATOR.validate_python(bad)


# ---------------------------------------------------------------------------
# Filter (5 conservative criteria)
# ---------------------------------------------------------------------------


def test_filter_passes_valid_gamme():
    fm = importer.parse_frontmatter_yaml(FIXTURES_DIR / "gamme/valid-plaquette-de-frein.md")
    assert importer.evaluate_filters(fm) is None


def test_filter_rejects_not_exportable_rag():
    fm = importer.parse_frontmatter_yaml(FIXTURES_DIR / "gamme/skip-not-exportable.md")
    assert importer.evaluate_filters(fm) == "not_exportable_rag"


def test_filter_rejects_no_source_refs():
    fm = importer.parse_frontmatter_yaml(FIXTURES_DIR / "gamme/skip-no-source-refs.md")
    assert importer.evaluate_filters(fm) == "no_source_refs"


def test_filter_rejects_truth_level_too_low():
    fm = importer.parse_frontmatter_yaml(FIXTURES_DIR / "gamme/skip-truth-level-too-low.md")
    assert importer.evaluate_filters(fm) == "truth_level_too_low"


def test_filter_rejects_auto_passed_review_status():
    """Phase F.5 conservative — auto_passed is intentionally excluded."""
    fm = importer.parse_frontmatter_yaml(FIXTURES_DIR / "gamme/skip-not-approved.md")
    assert importer.evaluate_filters(fm) == "not_approved"


def test_filter_rejects_missing_content_hash():
    """Constructed inline because Pydantic would reject a fixture with this shape."""
    meta = {
        "exportable": {"rag": True},
        "review_status": "approved",
        "truth_level": "L1",
        "source_refs": [{"id": "x"}],
        # content_hash absent
    }
    assert importer.evaluate_filters(meta) == "missing_content_hash"


# ---------------------------------------------------------------------------
# Skip reason taxonomy
# ---------------------------------------------------------------------------


def test_skip_reasons_dict_is_low_cardinality():
    """Skip reasons go into the dead-letter directory tree — keep them few."""
    assert len(importer.SKIP_REASONS) <= 8


def test_skip_reasons_match_filter_outputs():
    """Every reason returned by evaluate_filters must be a documented key."""
    reasons_returned = {
        "not_exportable_rag",
        "not_approved",
        "truth_level_too_low",
        "no_source_refs",
        "missing_content_hash",
    }
    assert reasons_returned.issubset(importer.SKIP_REASONS.keys())


# ---------------------------------------------------------------------------
# Constants & module-level config
# ---------------------------------------------------------------------------


def test_canonical_source_is_wiki():
    assert importer.CANONICAL_SOURCE_WIKI == "automecanik-wiki"


def test_source_layer_is_exports_rag():
    assert importer.SOURCE_LAYER_EXPORTS_RAG == "exports/rag"


def test_origin_batch_kind_is_wiki_import():
    assert importer.ORIGIN_BATCH_KIND_WIKI == "wiki_import"


def test_allowed_truth_levels_are_l1_l2_only():
    assert importer.ALLOWED_TRUTH_LEVELS == {"L1", "L2"}


def test_allowed_review_statuses_intentionally_conservative():
    """Phase F.5 documents this is approved-only ; auto_passed comes later via amendment."""
    assert importer.ALLOWED_REVIEW_STATUSES == {"approved"}


def test_quarantine_default_outside_repo():
    """Dead-letter must NOT live in the rag Git repo (avoids confusion with raw/quarantine)."""
    assert str(importer.QUARANTINE_DIR).startswith("/var/lib/automecanik-rag")


def test_target_collection_is_v2():
    assert importer.TARGET_COLLECTION == "KB_Knowledge_v2"


def test_exit_codes_distinct_and_meaningful():
    """Each exit code maps to one specific failure class."""
    codes = {
        importer.EXIT_OK: 0,
        importer.EXIT_USER_ERROR: 1,
        importer.EXIT_TARGET_MISSING: 2,
        importer.EXIT_LOCK_HELD: 3,
        importer.EXIT_WIKI_PATH_INVALID: 4,
        importer.EXIT_RUNTIME_ERROR: 5,
    }
    assert len(set(codes.values())) == 6  # all distinct
