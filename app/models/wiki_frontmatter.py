"""Phase F.5 (ADR-031) — Pydantic v2 models mirror of the wiki exports JSON Schema.

Source of truth : ``automecanik-wiki/_meta/schema/exports/rag.schema.json``.
This module is a **typed projection** for runtime validation in the Python
indexer ; if the JSON Schema changes, this file must be updated in lockstep
(ADR-039 — wiki frontmatter Zod canon for the JS-side mirror).

Strict policy :
  - Reject extra fields (model_config extra="forbid") — surfaces schema drift
  - Discriminated union on ``entity_type`` — each entity has its own data shape
  - All ``content_hash``, ``source_refs``, ``review_status`` fields are
    REQUIRED at parse time : the L3/L4 filters in import_wiki_exports.py
    further validate semantic constraints (review_status == "approved", etc.)
"""

from __future__ import annotations

from typing import Annotated, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator


class _Strict(BaseModel):
    """Common config : forbid extras to surface schema drift early."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)


class ExportableFlags(_Strict):
    """`exportable.<channel>: bool` map, restricted to known channels."""

    rag: bool = False
    seo: bool = False
    support: bool = False


class SourceRef(_Strict):
    """One entry in the `source_refs` array.

    Mirror of `automecanik-wiki/_meta/schema/source-catalog-entry.schema.json`
    minimally — only the fields the rag indexer needs.
    """

    id: str = Field(..., min_length=1, description="Catalogue id")
    url: Optional[str] = None
    accessed_at: Optional[str] = None  # ISO-8601 date


class TraceabilityBlock(_Strict):
    """Phase 5 traceability section."""

    lineage_id: Optional[str] = None
    parent_lineage_id: Optional[str] = None
    source_commit: Optional[str] = None  # commit of the WIKI repo
    raw_refs: List[str] = Field(default_factory=list)


class _CommonFrontmatter(_Strict):
    """Fields common to all entity types (any wiki export)."""

    schema_version: str = Field(..., description="Schema version, e.g. '1.0.0'")
    slug: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    truth_level: Literal["L0", "L1", "L2", "L3", "L4"] = Field(...)
    review_status: Literal["draft", "auto_passed", "approved", "rejected"] = Field(...)
    exportable: ExportableFlags = Field(default_factory=ExportableFlags)
    source_refs: List[SourceRef] = Field(default_factory=list)
    content_hash: str = Field(..., min_length=1, description="sha256 of body markdown")
    traceability: Optional[TraceabilityBlock] = None

    @field_validator("content_hash")
    @classmethod
    def _content_hash_looks_like_sha256(cls, v: str) -> str:
        if len(v) < 32:
            raise ValueError("content_hash too short — expected sha256 hex (≥32 chars)")
        return v


class GammeFrontmatter(_CommonFrontmatter):
    entity_type: Literal["gamme"]
    # gamme-specific fields can be added as needed for downstream filtering
    # ; we keep the minimum set the indexer reads.
    references: List[dict] = Field(default_factory=list)


class VehicleFrontmatter(_CommonFrontmatter):
    entity_type: Literal["vehicle"]
    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None


class ConstructeurFrontmatter(_CommonFrontmatter):
    entity_type: Literal["constructeur"]
    brand: Optional[str] = None


class SupportFrontmatter(_CommonFrontmatter):
    entity_type: Literal["support"]
    category: Optional[str] = None


class DiagnosticFrontmatter(_CommonFrontmatter):
    entity_type: Literal["diagnostic"]
    system: Optional[str] = None


# Discriminated union — Pydantic picks the right model based on `entity_type`.
WikiExportFrontmatter = Annotated[
    Union[
        GammeFrontmatter,
        VehicleFrontmatter,
        ConstructeurFrontmatter,
        SupportFrontmatter,
        DiagnosticFrontmatter,
    ],
    Field(discriminator="entity_type"),
]
