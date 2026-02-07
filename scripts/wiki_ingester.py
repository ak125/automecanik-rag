#!/usr/bin/env python3
"""
Wiki Ingester - Ingest exported wiki content into Weaviate.

Reads the manifest.json from wiki_exporter.py and:
1. Chunks documents into smaller pieces
2. Generates embeddings using sentence-transformers
3. Upserts into Weaviate

Usage:
    python wiki_ingester.py [--manifest PATH] [--dry-run]
"""

import argparse
import hashlib
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import weaviate
import yaml
from sentence_transformers import SentenceTransformer
from weaviate.classes.config import Configure, Property, DataType

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("wiki_ingester")


def load_config() -> dict:
    """Load configuration from rag_config.yml."""
    config_path = Path(__file__).parent.parent / "rag_config.yml"
    if config_path.exists():
        with open(config_path) as f:
            return yaml.safe_load(f)
    return {}


class WikiIngester:
    """Ingest wiki content into Weaviate."""

    def __init__(
        self,
        weaviate_url: str = "http://localhost:8080",
        collection_name: str = "Prod_Chatbot",
        embedding_model: str = "all-MiniLM-L6-v2",
        chunk_size: int = 500,
        chunk_overlap: int = 50,
        dry_run: bool = False
    ):
        self.weaviate_url = weaviate_url
        self.collection_name = collection_name
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.dry_run = dry_run

        # Initialize embedding model
        logger.info(f"Loading embedding model: {embedding_model}")
        self.embedder = SentenceTransformer(embedding_model)

        # Initialize Weaviate client
        if not dry_run:
            logger.info(f"Connecting to Weaviate: {weaviate_url}")
            self.client = weaviate.connect_to_local(
                host=weaviate_url.replace("http://", "").replace("https://", "").split(":")[0],
                port=int(weaviate_url.split(":")[-1]) if ":" in weaviate_url else 8080
            )
        else:
            self.client = None

    def ingest_from_manifest(self, manifest_path: str) -> dict:
        """
        Ingest documents from an export manifest.

        Args:
            manifest_path: Path to manifest.json from wiki_exporter.py

        Returns:
            dict with ingestion statistics
        """
        logger.info(f"Reading manifest: {manifest_path}")

        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        documents = manifest.get("documents", [])
        logger.info(f"Found {len(documents)} documents in manifest")

        stats = {
            "documents_processed": 0,
            "chunks_created": 0,
            "chunks_inserted": 0,
            "errors": 0,
            "started_at": datetime.now().isoformat()
        }

        all_chunks = []

        for doc in documents:
            try:
                chunks = self._process_document(doc)
                all_chunks.extend(chunks)
                stats["documents_processed"] += 1
                stats["chunks_created"] += len(chunks)
            except Exception as e:
                logger.error(f"Error processing document {doc.get('path')}: {e}")
                stats["errors"] += 1

        logger.info(f"Created {stats['chunks_created']} chunks from {stats['documents_processed']} documents")

        # Generate embeddings in batches
        if all_chunks:
            logger.info("Generating embeddings...")
            texts = [c["content"] for c in all_chunks]
            embeddings = self.embedder.encode(texts, show_progress_bar=True)

            for i, chunk in enumerate(all_chunks):
                chunk["embedding"] = embeddings[i].tolist()

        # Insert into Weaviate
        if not self.dry_run and all_chunks:
            logger.info(f"Inserting {len(all_chunks)} chunks into Weaviate...")
            stats["chunks_inserted"] = self._insert_chunks(all_chunks)
        elif self.dry_run:
            logger.info(f"[DRY RUN] Would insert {len(all_chunks)} chunks")
            stats["chunks_inserted"] = 0

        stats["completed_at"] = datetime.now().isoformat()
        return stats

    def _process_document(self, doc: dict) -> list:
        """Process a document into chunks."""
        content = doc.get("content", "")
        if not content.strip():
            return []

        # Split into chunks
        chunks = self._chunk_text(content)

        # Build chunk objects
        result = []
        for i, chunk_text in enumerate(chunks):
            # Generate deterministic chunk ID
            chunk_id = self._generate_chunk_id(doc.get("source_path", ""), i, chunk_text)

            chunk = {
                "chunk_id": chunk_id,
                "content": chunk_text,
                "title": doc.get("title", ""),
                "source_path": doc.get("source_path", ""),
                "source_type": doc.get("doc_type", "general"),
                "category": doc.get("doc_type", "general"),
                "truth_level": doc.get("truth_level", "L3"),
                "verification_status": "unverified",
                "confidence_score": 0.5,
                "chunk_index": i,
                "total_chunks": len(chunks),
                "tags": doc.get("tags", []),
                "updated_at": doc.get("updated_at") or datetime.now().isoformat()
            }
            result.append(chunk)

        return result

    def _chunk_text(self, text: str) -> list:
        """
        Split text into chunks.

        Simple chunking by approximate token count (words * 1.3).
        For production, consider using tiktoken or a smarter chunker.
        """
        words = text.split()
        approx_tokens = len(words) * 1.3

        if approx_tokens <= self.chunk_size:
            return [text.strip()]

        chunks = []
        current_chunk = []
        current_count = 0

        for word in words:
            current_chunk.append(word)
            current_count += 1.3

            if current_count >= self.chunk_size:
                chunks.append(" ".join(current_chunk))
                # Overlap: keep last N words
                overlap_words = max(1, int(self.chunk_overlap / 1.3))
                current_chunk = current_chunk[-overlap_words:]
                current_count = len(current_chunk) * 1.3

        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks

    def _generate_chunk_id(self, source_path: str, chunk_index: int, content: str) -> str:
        """Generate deterministic chunk ID for upsert."""
        # Hash based on source + index + content hash
        content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        unique = f"{source_path}:{chunk_index}:{content_hash}"
        return hashlib.sha256(unique.encode()).hexdigest()

    def _insert_chunks(self, chunks: list) -> int:
        """Insert chunks into Weaviate using upsert logic."""
        if not self.client:
            return 0

        inserted = 0

        try:
            collection = self.client.collections.get(self.collection_name)

            # Insert in batches
            batch_size = 100
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i + batch_size]

                with collection.batch.dynamic() as batch_obj:
                    for chunk in batch:
                        try:
                            batch_obj.add_object(
                                properties={
                                    "content": chunk["content"],
                                    "title": chunk["title"],
                                    "source_path": chunk["source_path"],
                                    "source_type": chunk["source_type"],
                                    "category": chunk["category"],
                                    "truth_level": chunk["truth_level"],
                                    "verification_status": chunk["verification_status"],
                                    "confidence_score": chunk["confidence_score"],
                                },
                                vector=chunk["embedding"],
                                uuid=chunk["chunk_id"]
                            )
                            inserted += 1
                        except Exception as e:
                            logger.warning(f"Failed to insert chunk {chunk['chunk_id']}: {e}")

                logger.info(f"Inserted batch {i // batch_size + 1}/{(len(chunks) + batch_size - 1) // batch_size}")

        except Exception as e:
            logger.error(f"Error inserting chunks: {e}")

        return inserted

    def cleanup_old_documents(self, source_path_prefix: str) -> int:
        """Delete old documents that match a source path prefix."""
        if self.dry_run or not self.client:
            logger.info(f"[DRY RUN] Would delete documents with source_path starting with: {source_path_prefix}")
            return 0

        try:
            collection = self.client.collections.get(self.collection_name)

            # Query for matching documents
            result = collection.query.fetch_objects(
                filters=weaviate.classes.query.Filter.by_property("source_path").like(f"{source_path_prefix}*"),
                limit=10000
            )

            deleted = 0
            for obj in result.objects:
                collection.data.delete_by_id(obj.uuid)
                deleted += 1

            logger.info(f"Deleted {deleted} old documents with prefix: {source_path_prefix}")
            return deleted

        except Exception as e:
            logger.error(f"Error cleaning up old documents: {e}")
            return 0

    def close(self):
        """Close Weaviate connection."""
        if self.client:
            self.client.close()


def main():
    parser = argparse.ArgumentParser(description="Ingest wiki content into Weaviate")
    parser.add_argument(
        "--manifest",
        default="/opt/automecanik/rag/wiki_export/manifest.json",
        help="Path to manifest.json from wiki_exporter.py"
    )
    parser.add_argument(
        "--weaviate-url",
        help="Weaviate URL (default from config)"
    )
    parser.add_argument(
        "--collection",
        help="Weaviate collection name (default from config)"
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=500,
        help="Chunk size in approximate tokens"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Process without inserting into Weaviate"
    )
    parser.add_argument(
        "--cleanup",
        action="store_true",
        help="Delete existing wiki documents before inserting"
    )

    args = parser.parse_args()

    # Load config
    config = load_config()
    vs_config = config.get("vector_store", {})
    emb_config = config.get("embeddings", {})

    # Build ingester
    ingester = WikiIngester(
        weaviate_url=args.weaviate_url or vs_config.get("url", "http://localhost:8080"),
        collection_name=args.collection or vs_config.get("class_name", "Prod_Chatbot"),
        embedding_model=emb_config.get("model", "all-MiniLM-L6-v2"),
        chunk_size=args.chunk_size,
        dry_run=args.dry_run
    )

    try:
        # Cleanup if requested
        if args.cleanup:
            ingester.cleanup_old_documents("wiki/")

        # Ingest
        stats = ingester.ingest_from_manifest(args.manifest)

        print(f"\nIngestion complete:")
        print(f"  Documents processed: {stats['documents_processed']}")
        print(f"  Chunks created: {stats['chunks_created']}")
        print(f"  Chunks inserted: {stats['chunks_inserted']}")
        print(f"  Errors: {stats['errors']}")

        if args.dry_run:
            print("\n[DRY RUN] No data was written to Weaviate")

    finally:
        ingester.close()


if __name__ == "__main__":
    main()
