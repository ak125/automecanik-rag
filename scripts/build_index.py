#!/usr/bin/env python3
"""Build and index knowledge corpus into Weaviate."""

import os
import sys
from pathlib import Path
import frontmatter
import weaviate
from weaviate.classes.data import DataObject

# Configuration
WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://localhost:8080")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
KNOWLEDGE_PATH = os.getenv("KNOWLEDGE_PATH", "../knowledge")


def load_markdown_files(base_path: str) -> list[dict]:
    """Load all markdown files from knowledge directory."""
    documents = []
    base = Path(base_path)

    if not base.exists():
        print(f"ERROR: Knowledge path '{base_path}' does not exist")
        return []

    for md_file in base.rglob("*.md"):
        if md_file.name == "README.md":
            continue

        try:
            post = frontmatter.load(md_file)

            # Extract metadata
            doc_id = post.metadata.get("id", md_file.stem)
            category = post.metadata.get("category", md_file.parent.name)
            source_type = "faq" if "faq" in str(md_file) else "policy" if "policies" in str(md_file) else "guide"

            documents.append({
                "content": post.content,
                "title": doc_id,
                "source_type": source_type,
                "source_path": str(md_file.relative_to(base)),
                "category": category,
            })

            print(f"  Loaded: {md_file.relative_to(base)}")

        except Exception as e:
            print(f"  ERROR loading {md_file}: {e}")

    return documents


def index_documents(documents: list[dict]):
    """Index documents into Weaviate."""
    print(f"\nConnecting to Weaviate at {WEAVIATE_URL}...")

    client = weaviate.connect_to_local(
        host=WEAVIATE_URL.replace("http://", "").replace("https://", "").split(":")[0],
        port=int(WEAVIATE_URL.split(":")[-1]) if ":" in WEAVIATE_URL.split("/")[-1] else 8080,
        headers={"X-OpenAI-Api-Key": OPENAI_API_KEY} if OPENAI_API_KEY else None,
    )

    try:
        collection = client.collections.get("Prod_Chatbot")

        # Clear existing data (optional - comment out for incremental updates)
        print("Clearing existing documents...")
        collection.data.delete_many(where=None)

        # Batch insert
        print(f"Indexing {len(documents)} documents...")

        with collection.batch.dynamic() as batch:
            for doc in documents:
                batch.add_object(properties=doc)

        print(f"\nSuccessfully indexed {len(documents)} documents!")

        # Verify
        count = collection.aggregate.over_all(total_count=True)
        print(f"Total documents in collection: {count.total_count}")

    finally:
        client.close()


def main():
    """Main function."""
    print("=" * 60)
    print("AutoMecanik RAG - Build Index")
    print("=" * 60)

    # Check requirements
    if not OPENAI_API_KEY:
        print("ERROR: OPENAI_API_KEY environment variable is required")
        sys.exit(1)

    # Get knowledge path from args or env
    knowledge_path = sys.argv[1] if len(sys.argv) > 1 else KNOWLEDGE_PATH
    print(f"\nLoading documents from: {knowledge_path}")

    # Load documents
    documents = load_markdown_files(knowledge_path)

    if not documents:
        print("No documents found to index.")
        sys.exit(1)

    print(f"\nFound {len(documents)} documents")

    # Index documents
    index_documents(documents)

    print("\nDone!")


if __name__ == "__main__":
    main()
