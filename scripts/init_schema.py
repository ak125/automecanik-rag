#!/usr/bin/env python3
"""Initialize Weaviate schema for RAG service."""

import os
import sys
import weaviate
from weaviate.classes.config import Property, DataType, Configure

# Weaviate connection
WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://localhost:8080")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Schema definition
SCHEMA = {
    "class": "Prod_Chatbot",
    "description": "FAQ et politiques support client AutoMecanik",
    "properties": [
        Property(name="content", data_type=DataType.TEXT, description="Document content"),
        Property(name="title", data_type=DataType.TEXT, description="Document title/ID"),
        Property(name="source_type", data_type=DataType.TEXT, description="Type: faq, policy, guide"),
        Property(name="source_path", data_type=DataType.TEXT, description="File path"),
        Property(name="category", data_type=DataType.TEXT, description="Category"),
    ],
}


def init_schema():
    """Initialize Weaviate schema."""
    print(f"Connecting to Weaviate at {WEAVIATE_URL}...")

    # Connect to Weaviate
    client = weaviate.connect_to_local(
        host=WEAVIATE_URL.replace("http://", "").replace("https://", "").split(":")[0],
        port=int(WEAVIATE_URL.split(":")[-1]) if ":" in WEAVIATE_URL.split("/")[-1] else 8080,
        headers={"X-OpenAI-Api-Key": OPENAI_API_KEY} if OPENAI_API_KEY else None,
    )

    try:
        # Check if collection exists
        if client.collections.exists("Prod_Chatbot"):
            print("Collection 'Prod_Chatbot' already exists.")
            response = input("Do you want to delete and recreate it? (y/N): ")
            if response.lower() == "y":
                client.collections.delete("Prod_Chatbot")
                print("Deleted existing collection.")
            else:
                print("Keeping existing collection.")
                return

        # Create collection with OpenAI vectorizer
        print("Creating collection 'Prod_Chatbot'...")
        client.collections.create(
            name="Prod_Chatbot",
            description="FAQ et politiques support client AutoMecanik",
            vectorizer_config=Configure.Vectorizer.text2vec_openai(
                model="text-embedding-3-small",
            ),
            properties=[
                Property(name="content", data_type=DataType.TEXT),
                Property(name="title", data_type=DataType.TEXT),
                Property(name="source_type", data_type=DataType.TEXT),
                Property(name="source_path", data_type=DataType.TEXT),
                Property(name="category", data_type=DataType.TEXT),
            ],
        )

        print("Collection 'Prod_Chatbot' created successfully!")

    finally:
        client.close()


if __name__ == "__main__":
    if not OPENAI_API_KEY:
        print("ERROR: OPENAI_API_KEY environment variable is required")
        sys.exit(1)

    init_schema()
