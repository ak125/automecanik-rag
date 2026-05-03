"""Phase F.5 (ADR-031) — Weaviate KB_Knowledge_v2 schema definition.

Creates the v2 collection with 14 strict properties (8 existing + 6 new) without
touching the v1 ``KB_Knowledge`` collection (versioning, not in-place mutation).

Backward-compat reads of v1 are preserved by ``_format_result``'s tolerance of
absent properties.

The 6 new properties :
    canonical_source : "automecanik-wiki" | "legacy-rag-knowledge"
    source_layer     : "exports/rag" | "knowledge"
    source_commit    : sha-1 of the canonical source repo (wiki for exports,
                       rag for traceable legacy ingest, null otherwise)
    lineage_id       : UUIDv7 of the import/migration batch — TRACE only,
                       NOT the idempotency key
    embedding_model  : e.g. "all-MiniLM-L6-v2" — re-indexation trigger if model changes
    origin_batch_kind: "legacy_migration" | "wiki_import" — discriminates
                       v1-migrated chunks from natively-v2 chunks

Idempotency key (filterable inverted indexes, NOT a relational composite index) :
    (canonical_source, source_path, content_hash, chunk_index)

Plus ``embedding_model`` is filterable too so a model change can re-index
selectively.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from weaviate import WeaviateClient

logger = logging.getLogger(__name__)

KB_KNOWLEDGE_V2 = "KB_Knowledge_v2"

# Order matches the runbook §"Schema Weaviate v2" for documentation alignment.
PROPERTY_NAMES_V2 = [
    "content",
    "title",
    "source_path",
    "source_type",
    "truth_level",
    "namespace",
    "chunk_index",
    "content_hash",
    # Phase F.5 additions
    "canonical_source",
    "source_layer",
    "source_commit",
    "lineage_id",
    "embedding_model",
    "origin_batch_kind",
]

FILTERABLE_PROPERTIES_V2 = {
    # Idempotency natural key (4 fields)
    "canonical_source",
    "source_path",
    "content_hash",
    "chunk_index",
    # Re-indexation discriminator
    "embedding_model",
    # Lifecycle / debugging
    "lineage_id",
    "origin_batch_kind",
    "source_layer",
    "truth_level",
    "namespace",
    "source_type",
}

# Allowed string-literal values (validated client-side before write).
ALLOWED_CANONICAL_SOURCES = {"automecanik-wiki", "legacy-rag-knowledge"}
ALLOWED_SOURCE_LAYERS = {"exports/rag", "knowledge"}
ALLOWED_ORIGIN_BATCH_KINDS = {"legacy_migration", "wiki_import"}


def build_v2_property_specs() -> list[dict]:
    """Return the 14-property spec as a list of dicts.

    Used both by the schema creator and by tests (so both share one source).
    Kept dict-based (not weaviate.classes.config.Property) so the test does
    not require a live weaviate import path.
    """
    text = "text"
    int_ = "int"
    return [
        {"name": "content", "data_type": text, "indexFilterable": False, "indexSearchable": True},
        {"name": "title", "data_type": text, "indexFilterable": False, "indexSearchable": True},
        {"name": "source_path", "data_type": text, "indexFilterable": True},
        {"name": "source_type", "data_type": text, "indexFilterable": True},
        {"name": "truth_level", "data_type": text, "indexFilterable": True},
        {"name": "namespace", "data_type": text, "indexFilterable": True},
        {"name": "chunk_index", "data_type": int_, "indexFilterable": True},
        {"name": "content_hash", "data_type": text, "indexFilterable": True},
        # Phase F.5 additions
        {"name": "canonical_source", "data_type": text, "indexFilterable": True},
        {"name": "source_layer", "data_type": text, "indexFilterable": True},
        {"name": "source_commit", "data_type": text, "indexFilterable": False},  # high cardinality
        {"name": "lineage_id", "data_type": text, "indexFilterable": True},  # batch rollback queries
        {"name": "embedding_model", "data_type": text, "indexFilterable": True},
        {"name": "origin_batch_kind", "data_type": text, "indexFilterable": True},
    ]


def create_kb_knowledge_v2(client: "WeaviateClient", *, recreate: bool = False) -> str:
    """Create the ``KB_Knowledge_v2`` collection if absent.

    Args:
        client: live weaviate.WeaviateClient
        recreate: if True, delete and recreate (USE WITH CAUTION — destructive
                  on the v2 collection only ; never touches v1).

    Returns:
        The collection name.

    Raises:
        Whatever weaviate raises on schema collisions / connectivity errors.
    """
    # Late import so this module is importable in test environments without
    # weaviate-client installed (the test files mock or skip).
    from weaviate.classes.config import Configure, DataType, Property  # type: ignore

    if client.collections.exists(KB_KNOWLEDGE_V2):
        if recreate:
            logger.warning(
                "F.5: deleting existing %s before recreate (destructive on v2 only)",
                KB_KNOWLEDGE_V2,
            )
            client.collections.delete(KB_KNOWLEDGE_V2)
        else:
            logger.info("F.5: %s already exists — no-op", KB_KNOWLEDGE_V2)
            return KB_KNOWLEDGE_V2

    type_map = {"text": DataType.TEXT, "int": DataType.INT}
    properties = []
    for spec in build_v2_property_specs():
        properties.append(
            Property(
                name=spec["name"],
                data_type=type_map[spec["data_type"]],
                index_filterable=spec.get("indexFilterable", False),
                index_searchable=spec.get("indexSearchable", False),
            )
        )

    client.collections.create(
        name=KB_KNOWLEDGE_V2,
        properties=properties,
        # We rely on the same vectorizer config as v1 (configured globally).
        # If a future Phase F.5+ wants per-collection vectorizer override,
        # plumb a kwarg here.
        vectorizer_config=Configure.Vectorizer.none(),
    )

    logger.info(
        "F.5: created collection %s with %d properties (%d filterable)",
        KB_KNOWLEDGE_V2,
        len(properties),
        sum(1 for p in build_v2_property_specs() if p.get("indexFilterable")),
    )
    return KB_KNOWLEDGE_V2


def is_natural_key_complete(props: dict) -> bool:
    """Return True if a chunk has the 4 fields needed for natural-key idempotence.

    Phase F.5 (ADR-031) — the idempotency check requires :
        canonical_source, source_path, content_hash, chunk_index
    A chunk missing any of these cannot be deduplicated reliably.
    """
    return all(
        props.get(k) is not None
        for k in ("canonical_source", "source_path", "content_hash", "chunk_index")
    )
