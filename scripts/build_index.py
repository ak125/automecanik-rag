#!/usr/bin/env python3
"""Build and index knowledge corpus into Weaviate (100% gratuit - embeddings locaux)."""

import os
import sys
from pathlib import Path
import frontmatter
import weaviate
from sentence_transformers import SentenceTransformer

# Configuration
WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://localhost:8080")
KNOWLEDGE_PATH = os.getenv("KNOWLEDGE_PATH", "/knowledge")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

# Directory name -> canonical source_type mapping
DIR_TO_SOURCE_TYPE = {
    "diagnostic": "diagnostic", "diagnostics": "diagnostic",
    "gamme": "gamme", "gammes": "gamme",
    "faq": "faq", "faqs": "faq",
    "guide": "guide", "guides": "guide",
    "vehicle": "vehicle", "vehicles": "vehicle",
    "policy": "policy", "policies": "policy",
}


def resolve_source_type(metadata: dict, rel_path: str) -> str:
    """Resolve source_type with priority: source_type > entity_type > directory inference."""
    st = metadata.get("source_type")
    if st:
        return st

    et = metadata.get("entity_type")
    if et and et != "unknown":
        return et

    parts = rel_path.split("/")
    if parts:
        first_dir = parts[0].lower()
        return DIR_TO_SOURCE_TYPE.get(first_dir, "general")

    return "general"


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

            # Extract metadata from frontmatter
            rel_path = str(md_file.relative_to(base))
            title = post.metadata.get("title", md_file.stem)
            source_type = resolve_source_type(post.metadata, rel_path)
            category = post.metadata.get("category", md_file.parent.name)

            # Truth Level System (Semantic Brain L1-L4)
            # L1: Faits vérifiés, L2: Règles métier, L3: Hypothèses, L4: Heuristiques
            truth_level = post.metadata.get("truth_level", "L3")  # Default: hypothèse
            verification_status = post.metadata.get("verification_status", "unverified")
            confidence_score = post.metadata.get("confidence_score", 0.5)
            last_verified_date = post.metadata.get("last_verified_date", "")
            verified_by = post.metadata.get("verified_by", "")

            documents.append({
                "content": post.content,
                "title": title,
                "source_type": source_type,
                "source_path": rel_path,
                "category": category,
                "namespace": f"knowledge:{source_type}",
                # Truth Level metadata
                "truth_level": truth_level,
                "verification_status": verification_status,
                "confidence_score": float(confidence_score) if confidence_score else 0.5,
                "last_verified_date": str(last_verified_date) if last_verified_date else "",
                "verified_by": verified_by,
            })

            # Show truth level in output
            level_emoji = {"L1": "✅", "L2": "📋", "L3": "❓", "L4": "💭"}.get(truth_level, "❓")
            print(f"  {level_emoji} [{truth_level}] {md_file.relative_to(base)}")

        except Exception as e:
            print(f"  ERROR loading {md_file}: {e}")

    return documents


def index_documents(documents: list[dict], embeddings_model: SentenceTransformer):
    """Index documents into Weaviate with local embeddings."""
    print(f"\nConnecting to Weaviate at {WEAVIATE_URL}...")

    # Parse host and port
    url_clean = WEAVIATE_URL.replace("http://", "").replace("https://", "")
    host = url_clean.split(":")[0]
    port = int(url_clean.split(":")[-1]) if ":" in url_clean else 8080

    client = weaviate.connect_to_local(host=host, port=port)

    try:
        collection = client.collections.get("Prod_Chatbot")

        # Note: Skip clearing - the collection is fresh or we'll replace by re-indexing
        # For incremental updates, consider using upsert or clearing via schema recreation

        # Generate embeddings for all documents
        print(f"Generating embeddings for {len(documents)} documents...")
        contents = [doc["content"] for doc in documents]
        embeddings = embeddings_model.encode(contents, show_progress_bar=True)

        # Batch insert with vectors
        print(f"Indexing {len(documents)} documents...")
        with collection.batch.dynamic() as batch:
            for i, doc in enumerate(documents):
                batch.add_object(
                    properties=doc,
                    vector=embeddings[i].tolist(),
                )

        print(f"\nSuccessfully indexed {len(documents)} documents!")

        # Verify
        count = collection.aggregate.over_all(total_count=True)
        print(f"Total documents in collection: {count.total_count}")

    finally:
        client.close()


def main():
    """Main function."""
    print("=" * 60)
    print("AutoMecanik RAG - Build Index (100% gratuit)")
    print("=" * 60)

    # Get knowledge path from args or env
    knowledge_path = sys.argv[1] if len(sys.argv) > 1 else KNOWLEDGE_PATH
    print(f"\nKnowledge path: {knowledge_path}")
    print(f"Embedding model: {EMBEDDING_MODEL}")

    # Load embedding model (100% gratuit - local)
    print(f"\nLoading embedding model: {EMBEDDING_MODEL}")
    embeddings_model = SentenceTransformer(EMBEDDING_MODEL)
    print("Model loaded!")

    # Load documents
    print(f"\nLoading documents from: {knowledge_path}")
    documents = load_markdown_files(knowledge_path)

    if not documents:
        print("No documents found to index.")
        sys.exit(1)

    # Show truth level summary
    truth_counts = {"L1": 0, "L2": 0, "L3": 0, "L4": 0}
    for doc in documents:
        level = doc.get("truth_level", "L3")
        if level in truth_counts:
            truth_counts[level] += 1

    print(f"\nFound {len(documents)} documents")
    print("\n📊 Truth Level Distribution:")
    print(f"  ✅ L1 (Faits vérifiés):  {truth_counts['L1']}")
    print(f"  📋 L2 (Règles métier):   {truth_counts['L2']}")
    print(f"  ❓ L3 (Hypothèses):      {truth_counts['L3']}")
    print(f"  💭 L4 (Heuristiques):    {truth_counts['L4']}")

    # Index documents
    index_documents(documents, embeddings_model)

    print("\nDone!")


if __name__ == "__main__":
    main()
