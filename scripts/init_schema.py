#!/usr/bin/env python3
"""Initialize Weaviate schema for RAG service (100% gratuit - sans OpenAI)."""

import os
import sys
import weaviate
from weaviate.classes.config import Property, DataType, Configure

# Weaviate connection
WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://localhost:8080")


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
        # Check if collection exists
        if client.collections.exists("Prod_Chatbot"):
            print("Collection 'Prod_Chatbot' already exists.")
            response = input("Delete and recreate? (y/N): ")
            if response.lower() == "y":
                client.collections.delete("Prod_Chatbot")
                print("Deleted existing collection.")
            else:
                print("Keeping existing collection.")
                return

        # Create collection WITHOUT vectorizer (we use sentence-transformers)
        print("Creating collection 'Prod_Chatbot' (vectorizer: none)...")
        client.collections.create(
            name="Prod_Chatbot",
            description="Corpus métier AutoMecanik - 100% gratuit avec niveaux de vérité",
            vectorizer_config=Configure.Vectorizer.none(),
            properties=[
                # Core properties
                Property(name="content", data_type=DataType.TEXT),
                Property(name="title", data_type=DataType.TEXT),
                Property(name="source_type", data_type=DataType.TEXT),
                Property(name="source_path", data_type=DataType.TEXT),
                Property(name="category", data_type=DataType.TEXT),
                # Truth Level System (Semantic Brain L1-L4)
                Property(name="truth_level", data_type=DataType.TEXT),  # L1|L2|L3|L4
                Property(name="verification_status", data_type=DataType.TEXT),  # verified|unverified|disputed
                Property(name="confidence_score", data_type=DataType.NUMBER),  # 0.0-1.0
                Property(name="last_verified_date", data_type=DataType.TEXT),  # ISO date string
                Property(name="verified_by", data_type=DataType.TEXT),  # who verified
            ],
        )
        print("Collection 'Prod_Chatbot' created successfully!")

        # Create Dev_Full collection (optional)
        if not client.collections.exists("Dev_Full"):
            print("Creating collection 'Dev_Full' (vectorizer: none)...")
            client.collections.create(
                name="Dev_Full",
                description="Knowledge + code + audits (DEV only) avec niveaux de vérité",
                vectorizer_config=Configure.Vectorizer.none(),
                properties=[
                    # Core properties
                    Property(name="content", data_type=DataType.TEXT),
                    Property(name="title", data_type=DataType.TEXT),
                    Property(name="source_type", data_type=DataType.TEXT),
                    Property(name="source_path", data_type=DataType.TEXT),
                    Property(name="language", data_type=DataType.TEXT),
                    Property(name="category", data_type=DataType.TEXT),
                    # Truth Level System (Semantic Brain L1-L4)
                    Property(name="truth_level", data_type=DataType.TEXT),  # L1|L2|L3|L4
                    Property(name="verification_status", data_type=DataType.TEXT),  # verified|unverified|disputed
                    Property(name="confidence_score", data_type=DataType.NUMBER),  # 0.0-1.0
                    Property(name="last_verified_date", data_type=DataType.TEXT),  # ISO date string
                    Property(name="verified_by", data_type=DataType.TEXT),  # who verified
                ],
            )
            print("Collection 'Dev_Full' created successfully!")

    finally:
        client.close()


if __name__ == "__main__":
    init_schema()
