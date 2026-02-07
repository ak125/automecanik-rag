#!/usr/bin/env python3
"""Standalone RAG reindex script using FastEmbed (memory-efficient).

This script indexes RAG markdown files to Weaviate with TRUE STREAMING:
- Read one file at a time
- Chunk immediately
- Embed immediately
- Upsert immediately
- Free memory before next file

Usage:
    # Dry run (show what would be indexed)
    ENV=dev python scripts/reindex.py --dry-run

    # Full reindex
    ENV=dev python scripts/reindex.py

    # Reindex specific folder
    ENV=dev python scripts/reindex.py --path /opt/automecanik/rag/knowledge/gammes

    # Clear collection and reindex
    ENV=dev python scripts/reindex.py --clear

Environment Variables:
    ENV: Must be 'dev', 'development', 'ci', 'staging', or 'test' (kill switch)
    WEAVIATE_URL: Weaviate endpoint (default: http://localhost:8080)
    COLLECTION_NAME: Weaviate collection (default: Prod_Chatbot)
"""

import os
import sys
import argparse
import logging
import uuid
import gc
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Generator, Iterator

import yaml

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
# Inside container, knowledge is mounted at /knowledge
DEFAULT_KNOWLEDGE_PATH = "/knowledge"
DEFAULT_WEAVIATE_URL = "http://weaviate:8080"
DEFAULT_WEAVIATE_GRPC_PORT = 50051
DEFAULT_COLLECTION = "Prod_Chatbot"
CHUNK_SIZE = 2000  # characters
CHUNK_OVERLAP = 200
BATCH_SIZE = 10  # Very small batches to prevent OOM

# FastEmbed model (same 384 dimensions as all-MiniLM-L6-v2)
FASTEMBED_MODEL = "BAAI/bge-small-en-v1.5"

# Kill switch: only allow in BUILD plane
ALLOWED_ENVIRONMENTS = frozenset(["dev", "development", "ci", "staging", "test"])


def enforce_build_plane():
    """Enforce BUILD plane (dev/ci/staging only)."""
    env = os.environ.get("ENV", "").lower()
    if env not in ALLOWED_ENVIRONMENTS:
        logger.error(f"KILL SWITCH: ENV={env} not in allowed list {ALLOWED_ENVIRONMENTS}")
        logger.error("Set ENV=dev to run this script")
        sys.exit(1)
    logger.info(f"BUILD plane confirmed (ENV={env})")


def parse_frontmatter(content: str) -> Dict[str, Any]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}
    try:
        end_idx = content.find("---", 3)
        if end_idx == -1:
            return {}
        frontmatter = content[3:end_idx].strip()
        return yaml.safe_load(frontmatter) or {}
    except Exception:
        return {}


def iter_documents(knowledge_path: str) -> Generator[Dict, None, None]:
    """Iterate documents one at a time (streaming - no accumulation)."""
    path = Path(knowledge_path)

    if not path.exists():
        logger.error(f"Knowledge path not found: {knowledge_path}")
        return

    for md_file in path.rglob("*.md"):
        # Skip README and backup files
        if md_file.name == "README.md":
            continue
        if ".backup" in str(md_file):
            continue

        try:
            content = md_file.read_text(encoding="utf-8")
            relative_path = str(md_file.relative_to(path))
            metadata = parse_frontmatter(content)

            yield {
                "source_path": relative_path,
                "content": content,
                "title": metadata.get("title", md_file.stem),
                "truth_level": metadata.get("truth_level", "L2"),
                "entity_type": metadata.get("entity_type", "unknown"),
            }
        except Exception as e:
            logger.error(f"Failed to read {md_file}: {e}")


def chunk_document(doc: Dict) -> List[Dict]:
    """Chunk a single document into smaller pieces."""
    chunks = []
    content = doc["content"]
    start = 0
    chunk_index = 0

    while start < len(content):
        end = min(start + CHUNK_SIZE, len(content))

        # Try to break at newline
        if end < len(content):
            newline_pos = content.rfind("\n", start, end)
            if newline_pos > start + CHUNK_SIZE // 2:
                end = newline_pos + 1

        chunk_content = content[start:end]

        # Generate deterministic UUID
        chunk_uuid = str(uuid.uuid5(
            uuid.NAMESPACE_DNS,
            f"{doc['source_path']}:{chunk_index}"
        ))

        chunks.append({
            "uuid": chunk_uuid,
            "content": chunk_content,
            "title": doc["title"],
            "source_path": doc["source_path"],
            "source_type": "knowledge",
            "truth_level": doc["truth_level"],
            "namespace": f"knowledge:{doc['entity_type']}",
            "chunk_index": chunk_index,
        })

        start = end - CHUNK_OVERLAP
        chunk_index += 1

        if start >= len(content):
            break

    return chunks


def count_files(knowledge_path: str) -> int:
    """Count markdown files without loading them."""
    path = Path(knowledge_path)
    if not path.exists():
        return 0
    return sum(1 for f in path.rglob("*.md") if f.name != "README.md")


def get_weaviate_client(weaviate_url: str):
    """Create Weaviate client with explicit HTTP and gRPC settings.

    Uses connect_to_custom() instead of connect_to_local() to avoid
    memory issues with gRPC initialization.
    """
    import weaviate

    # Parse URL: http://weaviate:8080 -> host=weaviate, port=8080
    url_clean = weaviate_url.replace("http://", "").replace("https://", "")
    parts = url_clean.split(":")
    host = parts[0]
    port = int(parts[1]) if len(parts) > 1 else 8080

    return weaviate.connect_to_custom(
        http_host=host,
        http_port=port,
        http_secure=False,
        grpc_host=host,
        grpc_port=DEFAULT_WEAVIATE_GRPC_PORT,
        grpc_secure=False,
    )


def clear_collection(weaviate_url: str, collection_name: str):
    """Clear all objects from collection."""
    logger.info(f"Clearing collection {collection_name}...")

    client = get_weaviate_client(weaviate_url)

    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)
        logger.info(f"Deleted collection {collection_name}")

    # Recreate collection
    from weaviate.classes.config import Configure, Property, DataType

    client.collections.create(
        name=collection_name,
        properties=[
            Property(name="content", data_type=DataType.TEXT),
            Property(name="title", data_type=DataType.TEXT),
            Property(name="source_path", data_type=DataType.TEXT),
            Property(name="source_type", data_type=DataType.TEXT),
            Property(name="truth_level", data_type=DataType.TEXT),
            Property(name="namespace", data_type=DataType.TEXT),
            Property(name="chunk_index", data_type=DataType.INT),
        ],
        vectorizer_config=Configure.Vectorizer.none(),
    )

    logger.info(f"Recreated collection {collection_name}")
    client.close()


def index_streaming_true(
    knowledge_path: str,
    weaviate_url: str,
    collection_name: str
) -> tuple:
    """
    TRUE STREAMING: Process one file at a time.

    1. Read one file
    2. Chunk it
    3. Embed chunks
    4. Upsert to Weaviate
    5. Free memory
    6. Next file

    Returns: (doc_count, chunk_count, indexed_count)
    """
    from fastembed import TextEmbedding

    logger.info(f"Loading FastEmbed model: {FASTEMBED_MODEL}")
    model = TextEmbedding(model_name=FASTEMBED_MODEL)
    logger.info("FastEmbed model loaded (Rust backend, ~80% less RAM than PyTorch)")

    logger.info("Connecting to Weaviate...")
    client = get_weaviate_client(weaviate_url)

    collection = client.collections.get(collection_name)

    doc_count = 0
    chunk_count = 0
    indexed_count = 0

    # TRUE STREAMING: one file at a time
    for doc in iter_documents(knowledge_path):
        doc_count += 1

        # Chunk this document
        chunks = chunk_document(doc)
        chunk_count += len(chunks)

        if not chunks:
            continue

        # Embed + Upsert in small batches
        for i in range(0, len(chunks), BATCH_SIZE):
            batch_chunks = chunks[i:i + BATCH_SIZE]
            texts = [c["content"] for c in batch_chunks]

            # Generate embeddings for this batch
            embeddings = list(model.embed(texts, batch_size=BATCH_SIZE))

            # Upsert immediately
            with collection.batch.dynamic() as batch_obj:
                for chunk, embedding in zip(batch_chunks, embeddings):
                    batch_obj.add_object(
                        properties={k: v for k, v in chunk.items() if k != "uuid"},
                        vector=embedding.tolist(),
                        uuid=chunk["uuid"],
                    )
                    indexed_count += 1

            # Free memory
            del embeddings

        # Free document memory
        del doc, chunks
        gc.collect()

        # Progress every 50 docs
        if doc_count % 50 == 0:
            logger.info(f"  Progress: {doc_count} docs, {chunk_count} chunks, {indexed_count} indexed")

    client.close()
    return doc_count, chunk_count, indexed_count


def dry_run(knowledge_path: str) -> tuple:
    """Dry run: count files and estimate chunks without loading all in memory."""
    doc_count = 0
    chunk_count = 0
    sample_docs = []

    for doc in iter_documents(knowledge_path):
        doc_count += 1
        chunks = chunk_document(doc)
        chunk_count += len(chunks)

        if doc_count <= 10:
            sample_docs.append(doc["source_path"])

        # Free memory immediately
        del doc, chunks
        gc.collect()

        # Stop early for large corpora
        if doc_count % 100 == 0:
            logger.info(f"  Scanning... {doc_count} docs found")

    return doc_count, chunk_count, sample_docs


def main():
    parser = argparse.ArgumentParser(description="Reindex RAG documents to Weaviate (FastEmbed)")
    parser.add_argument(
        "--path",
        default=DEFAULT_KNOWLEDGE_PATH,
        help=f"Path to knowledge folder (default: {DEFAULT_KNOWLEDGE_PATH})"
    )
    parser.add_argument(
        "--weaviate-url",
        default=os.environ.get("WEAVIATE_URL", DEFAULT_WEAVIATE_URL),
        help=f"Weaviate URL (default: {DEFAULT_WEAVIATE_URL})"
    )
    parser.add_argument(
        "--collection",
        default=os.environ.get("COLLECTION_NAME", DEFAULT_COLLECTION),
        help=f"Weaviate collection name (default: {DEFAULT_COLLECTION})"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be indexed without actually indexing"
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear collection before indexing"
    )

    args = parser.parse_args()

    # Enforce BUILD plane
    enforce_build_plane()

    start_time = datetime.utcnow()

    logger.info("=" * 60)
    logger.info("RAG REINDEX SCRIPT (FastEmbed + TRUE Streaming)")
    logger.info("=" * 60)
    logger.info(f"Knowledge path: {args.path}")
    logger.info(f"Weaviate URL: {args.weaviate_url}")
    logger.info(f"Collection: {args.collection}")
    logger.info(f"Model: {FASTEMBED_MODEL} (Rust backend)")
    logger.info(f"Batch size: {BATCH_SIZE}")
    logger.info(f"Dry run: {args.dry_run}")
    logger.info(f"Clear: {args.clear}")
    logger.info("=" * 60)

    if args.dry_run:
        logger.info("Running dry-run (streaming scan)...")
        doc_count, chunk_count, sample_docs = dry_run(args.path)

        logger.info("\n[DRY RUN] Would index:")
        for doc_path in sample_docs:
            logger.info(f"  - {doc_path}")
        if doc_count > 10:
            logger.info(f"  ... and {doc_count - 10} more")

        logger.info(f"\nTotal: {doc_count} documents, {chunk_count} chunks")
        logger.info("=" * 60)
        return

    # Clear collection if requested
    if args.clear:
        clear_collection(args.weaviate_url, args.collection)

    # TRUE STREAMING indexing
    logger.info("Starting TRUE STREAMING indexing...")
    logger.info("(Processing one file at a time to minimize memory)")

    doc_count, chunk_count, indexed_count = index_streaming_true(
        args.path,
        args.weaviate_url,
        args.collection
    )

    duration = (datetime.utcnow() - start_time).total_seconds()

    logger.info("=" * 60)
    logger.info("REINDEX COMPLETE")
    logger.info("=" * 60)
    logger.info(f"Documents: {doc_count}")
    logger.info(f"Chunks: {chunk_count}")
    logger.info(f"Indexed: {indexed_count}")
    logger.info(f"Duration: {duration:.2f}s")
    logger.info(f"Backend: FastEmbed (Rust)")
    logger.info(f"Mode: TRUE Streaming (1 file at a time)")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
