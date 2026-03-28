#!/usr/bin/env python3
"""Initialize Weaviate schema for RAG service (100% gratuit - sans OpenAI)."""

import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import weaviate
from weaviate.classes.config import Property, DataType, Configure
from app.config import get_settings

# Weaviate connection
_settings = get_settings()
WEAVIATE_URL = _settings.weaviate_url
TARGET_COLLECTIONS = [
    "KB_Catalog",
    "KB_Diagnostic",
    "KB_Knowledge",
    "KB_Media",
    "KB_RouterMemory",
]


def build_gold_properties() -> list[Property]:
    """Canonical chunk schema used across all collections."""
    return [
        # Required
        Property(name="chunk_id", data_type=DataType.TEXT),
        Property(name="parent_id", data_type=DataType.TEXT),
        Property(name="source_path", data_type=DataType.TEXT),
        Property(name="source_uri", data_type=DataType.TEXT),
        Property(name="source_ref", data_type=DataType.TEXT),
        Property(name="title", data_type=DataType.TEXT),
        Property(name="content", data_type=DataType.TEXT),
        Property(name="anchors", data_type=DataType.TEXT_ARRAY),
        Property(name="intent", data_type=DataType.TEXT),
        Property(name="domain", data_type=DataType.TEXT),
        Property(name="entities", data_type=DataType.TEXT_ARRAY),
        Property(name="truth_level", data_type=DataType.TEXT),
        Property(name="verification_status", data_type=DataType.TEXT),
        Property(name="doc_weight", data_type=DataType.NUMBER),
        Property(name="evidence_grade", data_type=DataType.TEXT),
        Property(name="is_canonical", data_type=DataType.BOOL),
        Property(name="canonical_weight", data_type=DataType.NUMBER),
        # Useful
        Property(name="chunk_index", data_type=DataType.INT),
        Property(name="created_at", data_type=DataType.TEXT),
        Property(name="updated_at", data_type=DataType.TEXT),
        Property(name="content_hash", data_type=DataType.TEXT),
        # Backward-compatible fields still used in some filters
        Property(name="source_type", data_type=DataType.TEXT),
        Property(name="doc_family", data_type=DataType.TEXT),
        Property(name="namespace", data_type=DataType.TEXT),
        Property(name="category", data_type=DataType.TEXT),
        Property(name="language", data_type=DataType.TEXT),
        Property(name="confidence_score", data_type=DataType.NUMBER),
        Property(name="last_verified_date", data_type=DataType.TEXT),
        Property(name="verified_by", data_type=DataType.TEXT),
        # Role classification (Phase 1)
        Property(name="section_key", data_type=DataType.TEXT),
        Property(name="primary_role", data_type=DataType.TEXT),
        Property(name="allowed_roles", data_type=DataType.TEXT_ARRAY),
        Property(name="purity_score", data_type=DataType.INT),
        Property(name="contamination_flags", data_type=DataType.TEXT_ARRAY),
        # Chunk kind classification (Phase 2)
        Property(name="chunk_kind", data_type=DataType.TEXT),
        # Page contract + media hints (Phase 3)
        Property(name="page_contract_id", data_type=DataType.TEXT),
        Property(name="media_slots_hint", data_type=DataType.TEXT),
    ]


ROLE_PROPERTIES = [
    Property(name="section_key", data_type=DataType.TEXT),
    Property(name="primary_role", data_type=DataType.TEXT),
    Property(name="allowed_roles", data_type=DataType.TEXT_ARRAY),
    Property(name="purity_score", data_type=DataType.INT),
    Property(name="contamination_flags", data_type=DataType.TEXT_ARRAY),
    Property(name="chunk_kind", data_type=DataType.TEXT),
]


CONTRACT_PROPERTIES = [
    Property(name="page_contract_id", data_type=DataType.TEXT),
    Property(name="media_slots_hint", data_type=DataType.TEXT),
]


def migrate_add_contract_properties(client):
    """Add Phase 3 contract properties to existing collections (non-destructive)."""
    all_collections = TARGET_COLLECTIONS + ["Dev_Full"]
    for collection_name in all_collections:
        if not client.collections.exists(collection_name):
            continue
        collection = client.collections.get(collection_name)
        config = collection.config.get()
        existing_names = {p.name for p in config.properties}
        added = 0
        for prop in CONTRACT_PROPERTIES:
            if prop.name not in existing_names:
                collection.config.add_property(prop)
                added += 1
        if added:
            print(f"  Added {added} contract properties to '{collection_name}'")
        else:
            print(f"  '{collection_name}' already has all contract properties")


def migrate_add_role_properties(client):
    """Add Phase 1 role properties to existing collections (non-destructive)."""
    all_collections = TARGET_COLLECTIONS + ["Dev_Full"]
    for collection_name in all_collections:
        if not client.collections.exists(collection_name):
            continue
        collection = client.collections.get(collection_name)
        config = collection.config.get()
        existing_names = {p.name for p in config.properties}
        added = 0
        for prop in ROLE_PROPERTIES:
            if prop.name not in existing_names:
                collection.config.add_property(prop)
                added += 1
        if added:
            print(f"  Added {added} role properties to '{collection_name}'")
        else:
            print(f"  '{collection_name}' already has all role properties")


def init_schema():
    """Initialize Weaviate schema with local embeddings (no vectorizer)."""
    print(f"Connecting to Weaviate at {WEAVIATE_URL}...")

    # Parse host and port
    url_clean = WEAVIATE_URL.replace("http://", "").replace("https://", "")
    host = url_clean.split(":")[0]
    port = int(url_clean.split(":")[-1]) if ":" in url_clean else 8080

    # Connect to Weaviate (no API keys needed)
    client = weaviate.connect_to_local(host=host, port=port)

    try:
        properties = build_gold_properties()

        for collection_name in TARGET_COLLECTIONS:
            if client.collections.exists(collection_name):
                print(f"Collection '{collection_name}' already exists.")
                continue

            print(f"Creating collection '{collection_name}' (vectorizer: none)...")
            client.collections.create(
                name=collection_name,
                description=f"{collection_name} - corpus AutoMecanik segmente",
                vectorizer_config=Configure.Vectorizer.none(),
                properties=properties,
            )
            print(f"Collection '{collection_name}' created successfully!")

        # Keep legacy dev collection for tooling compatibility.
        if not client.collections.exists("Dev_Full"):
            print("Creating collection 'Dev_Full' (vectorizer: none)...")
            client.collections.create(
                name="Dev_Full",
                description="Knowledge + code + audits (DEV only) avec niveaux de verite",
                vectorizer_config=Configure.Vectorizer.none(),
                properties=properties,
            )
            print("Collection 'Dev_Full' created successfully!")

        # Migrate existing collections: add Phase 1 role properties
        print("\nMigrating existing collections (add role properties)...")
        migrate_add_role_properties(client)

        # Migrate existing collections: add Phase 3 contract properties
        print("\nMigrating existing collections (add contract properties)...")
        migrate_add_contract_properties(client)

    finally:
        client.close()


if __name__ == "__main__":
    init_schema()
