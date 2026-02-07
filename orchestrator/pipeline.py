"""RAG Orchestrator Pipeline - Main Ingestion Flow.

This module orchestrates the full RAG ingestion pipeline:
1. validate_env() - KILL SWITCH enforcement
2. extract_sources() - Extract from MinIO, Wiki, knowledge folder
3. convert_to_markdown() - Convert PDF/DOCX to markdown
4. chunk_documents() - Split into ~500 token chunks
5. generate_embeddings() - all-MiniLM-L6-v2
6. upsert_weaviate() - Batch insert to Weaviate
7. version_index() - Tag with @latest/@rollback

CRITICAL: This pipeline ONLY runs in BUILD plane (dev/ci).
"""

import logging
import asyncio
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from pathlib import Path
import hashlib
import json
import uuid
import gc

from .kill_switch import enforce_build_plane, require_build_plane

logger = logging.getLogger(__name__)


@dataclass
class PipelineConfig:
    """Configuration for the orchestrator pipeline."""

    # Sources
    minio_enabled: bool = True
    wiki_enabled: bool = True
    knowledge_enabled: bool = True
    knowledge_path: str = "/knowledge"

    # MinIO config
    minio_endpoint: str = "minio:9000"
    minio_buckets: List[str] = field(default_factory=lambda: ["docs", "exports"])
    minio_access_key: str = ""
    minio_secret_key: str = ""

    # Wiki config
    wiki_mode: str = "git"  # git | graphql
    wiki_repo_path: str = ""
    wiki_graphql_url: str = ""

    # Processing
    chunk_size: int = 500
    chunk_overlap: int = 50
    batch_size: int = 100

    # Versioning
    create_version: bool = True
    promote_latest: bool = True
    keep_versions: int = 5

    # Weaviate
    weaviate_url: str = "http://weaviate:8080"
    collection_name: str = "Prod_Chatbot"

    @classmethod
    def from_yaml(cls, config: dict) -> "PipelineConfig":
        """Create config from YAML dict (rag_config.yml orchestrator section)."""
        orch = config.get("orchestrator", {})
        sources = orch.get("sources", {})
        processing = orch.get("processing", {})
        versioning = orch.get("versioning", {})

        return cls(
            # Sources
            minio_enabled=sources.get("minio", {}).get("enabled", True),
            wiki_enabled=sources.get("wiki", {}).get("enabled", True),
            knowledge_enabled=sources.get("knowledge", {}).get("enabled", True),
            knowledge_path=sources.get("knowledge", {}).get("path", "/knowledge"),
            # MinIO
            minio_endpoint=sources.get("minio", {}).get("endpoint", "minio:9000"),
            minio_buckets=sources.get("minio", {}).get("buckets", ["docs", "exports"]),
            # Wiki
            wiki_mode=sources.get("wiki", {}).get("mode", "git"),
            wiki_repo_path=sources.get("wiki", {}).get("repo_path", ""),
            wiki_graphql_url=sources.get("wiki", {}).get("graphql_url", ""),
            # Processing
            chunk_size=processing.get("chunk_size", 500),
            chunk_overlap=processing.get("chunk_overlap", 50),
            batch_size=processing.get("batch_size", 100),
            # Versioning
            create_version=versioning.get("create_version", True),
            promote_latest=versioning.get("promote_latest", True),
            keep_versions=versioning.get("keep_versions", 5),
            # Weaviate from main config
            weaviate_url=config.get("vector_store", {}).get("url", "http://weaviate:8080"),
            collection_name=config.get("vector_store", {}).get("class_name", "Prod_Chatbot"),
        )


@dataclass
class Document:
    """A document to be indexed."""

    source_path: str
    content: str
    title: str = ""
    source_type: str = "knowledge"  # knowledge | wiki | minio
    truth_level: str = "L3"
    namespace: str = "knowledge:faq"
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def source_id(self) -> str:
        """Generate deterministic source ID from path and content hash."""
        content_hash = hashlib.sha256(self.content.encode()).hexdigest()[:16]
        return hashlib.sha256(f"{self.source_path}:{content_hash}".encode()).hexdigest()


@dataclass
class Chunk:
    """A chunk of a document."""

    document: Document
    content: str
    chunk_index: int
    start_char: int
    end_char: int

    @property
    def chunk_id(self) -> str:
        """Generate deterministic chunk ID."""
        chunk_hash = hashlib.sha256(self.content.encode()).hexdigest()[:16]
        return hashlib.sha256(
            f"{self.document.source_id}:{self.chunk_index}:{chunk_hash}".encode()
        ).hexdigest()


@dataclass
class PipelineResult:
    """Result of a pipeline run."""

    success: bool
    documents_processed: int = 0
    chunks_created: int = 0
    chunks_indexed: int = 0
    errors: List[str] = field(default_factory=list)
    version_tag: Optional[str] = None
    duration_seconds: float = 0.0
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())


class OrchestratorPipeline:
    """Main orchestrator pipeline for RAG ingestion.

    Usage:
        config = PipelineConfig()
        pipeline = OrchestratorPipeline(config)
        result = await pipeline.run()
    """

    def __init__(self, config: PipelineConfig):
        self.config = config
        self.documents: List[Document] = []
        self.chunks: List[Chunk] = []

    @require_build_plane
    async def run(self) -> PipelineResult:
        """Run the full ingestion pipeline.

        Returns:
            PipelineResult with statistics and status.
        """
        start_time = datetime.utcnow()
        errors: List[str] = []

        logger.info("=" * 60)
        logger.info("ORCHESTRATOR PIPELINE STARTING")
        logger.info("=" * 60)

        try:
            # Step 1: Extract from sources
            logger.info("Step 1/6: Extracting from sources...")
            await self._extract_sources()
            logger.info(f"  -> Extracted {len(self.documents)} documents")

            # Step 2: Convert to markdown (if needed)
            logger.info("Step 2/6: Converting to markdown...")
            await self._convert_to_markdown()

            # Step 3: Chunk documents
            logger.info("Step 3/6: Chunking documents...")
            await self._chunk_documents()
            logger.info(f"  -> Created {len(self.chunks)} chunks")

            # Step 4-5: Generate embeddings and upsert in streaming batches (prevents OOM)
            logger.info("Step 4-5/6: Embedding and upserting (streaming)...")
            indexed_count = await self._embed_and_upsert_streaming()
            logger.info(f"  -> Indexed {indexed_count} chunks")

            # Step 6: Version index
            version_tag = None
            if self.config.create_version:
                logger.info("Step 6/6: Creating version tag...")
                version_tag = await self._version_index()
                logger.info(f"  -> Version: {version_tag}")

            duration = (datetime.utcnow() - start_time).total_seconds()

            logger.info("=" * 60)
            logger.info("PIPELINE COMPLETE")
            logger.info(f"  Documents: {len(self.documents)}")
            logger.info(f"  Chunks: {len(self.chunks)}")
            logger.info(f"  Indexed: {indexed_count}")
            logger.info(f"  Duration: {duration:.2f}s")
            logger.info("=" * 60)

            return PipelineResult(
                success=True,
                documents_processed=len(self.documents),
                chunks_created=len(self.chunks),
                chunks_indexed=indexed_count,
                errors=errors,
                version_tag=version_tag,
                duration_seconds=duration,
            )

        except Exception as e:
            logger.error(f"Pipeline failed: {e}", exc_info=True)
            errors.append(str(e))
            duration = (datetime.utcnow() - start_time).total_seconds()

            return PipelineResult(
                success=False,
                documents_processed=len(self.documents),
                chunks_created=len(self.chunks),
                chunks_indexed=0,
                errors=errors,
                duration_seconds=duration,
            )

    async def _extract_sources(self) -> None:
        """Extract documents from all enabled sources."""
        self.documents = []

        # Extract from knowledge folder
        if self.config.knowledge_enabled:
            knowledge_docs = await self._extract_knowledge()
            self.documents.extend(knowledge_docs)

        # Extract from Wiki (if enabled)
        if self.config.wiki_enabled:
            wiki_docs = await self._extract_wiki()
            self.documents.extend(wiki_docs)

        # Extract from MinIO (if enabled)
        if self.config.minio_enabled:
            minio_docs = await self._extract_minio()
            self.documents.extend(minio_docs)

    async def _extract_knowledge(self) -> List[Document]:
        """Extract documents from /knowledge folder."""
        docs = []
        knowledge_path = Path(self.config.knowledge_path)

        if not knowledge_path.exists():
            logger.warning(f"Knowledge path not found: {knowledge_path}")
            return docs

        for md_file in knowledge_path.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
                relative_path = md_file.relative_to(knowledge_path)

                # Parse frontmatter for metadata
                metadata = self._parse_frontmatter(content)
                title = metadata.get("title", md_file.stem)
                truth_level = metadata.get("truth_level", "L3")

                docs.append(
                    Document(
                        source_path=str(relative_path),
                        content=content,
                        title=title,
                        source_type="knowledge",
                        truth_level=truth_level,
                        metadata=metadata,
                    )
                )
            except Exception as e:
                logger.error(f"Failed to read {md_file}: {e}")

        return docs

    async def _extract_wiki(self) -> List[Document]:
        """Extract documents from Wiki.js."""
        # Delegate to wiki_extractor
        try:
            from .extractors.wiki_extractor import extract_wiki_documents

            return await extract_wiki_documents(self.config)
        except ImportError:
            logger.warning("Wiki extractor not available")
            return []

    async def _extract_minio(self) -> List[Document]:
        """Extract documents from MinIO."""
        # Delegate to minio_extractor
        try:
            from .extractors.minio_extractor import extract_minio_documents

            return await extract_minio_documents(self.config)
        except ImportError:
            logger.warning("MinIO extractor not available")
            return []

    def _parse_frontmatter(self, content: str) -> Dict[str, Any]:
        """Parse YAML frontmatter from markdown content."""
        import yaml

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

    async def _convert_to_markdown(self) -> None:
        """Convert non-markdown documents to markdown."""
        # For now, only MD files are supported
        # Future: Add PDF/DOCX conversion
        pass

    async def _chunk_documents(self) -> None:
        """Chunk documents into smaller pieces."""
        self.chunks = []

        try:
            from .processors.chunker import chunk_document

            for doc in self.documents:
                doc_chunks = chunk_document(
                    doc,
                    chunk_size=self.config.chunk_size,
                    chunk_overlap=self.config.chunk_overlap,
                )
                self.chunks.extend(doc_chunks)
        except ImportError:
            # Fallback: simple chunking
            for doc in self.documents:
                self.chunks.extend(self._simple_chunk(doc))

    def _simple_chunk(self, doc: Document) -> List[Chunk]:
        """Simple character-based chunking (fallback)."""
        chunks = []
        content = doc.content
        chunk_size = self.config.chunk_size * 4  # Approximate chars per token
        overlap = self.config.chunk_overlap * 4

        start = 0
        chunk_index = 0

        while start < len(content):
            end = start + chunk_size
            chunk_content = content[start:end]

            chunks.append(
                Chunk(
                    document=doc,
                    content=chunk_content,
                    chunk_index=chunk_index,
                    start_char=start,
                    end_char=min(end, len(content)),
                )
            )

            start = end - overlap
            chunk_index += 1

            if start >= len(content):
                break

        return chunks

    async def _generate_embeddings(self) -> List[tuple]:
        """Generate embeddings for all chunks (legacy method for compatibility)."""
        try:
            from sentence_transformers import SentenceTransformer

            model = SentenceTransformer("all-MiniLM-L6-v2")

            # Batch processing with smaller batches to prevent OOM
            texts = [chunk.content for chunk in self.chunks]
            embeddings = model.encode(texts, batch_size=16, show_progress_bar=True)

            return list(zip(self.chunks, embeddings))
        except ImportError:
            logger.error("sentence-transformers not installed")
            return []

    async def _upsert_weaviate(self, embeddings: List[tuple]) -> int:
        """Upsert chunks with embeddings to Weaviate."""
        if not embeddings:
            return 0

        try:
            import weaviate

            client = weaviate.connect_to_local(
                host=self.config.weaviate_url.replace("http://", "").split(":")[0],
                port=int(self.config.weaviate_url.split(":")[-1]),
            )

            collection = client.collections.get(self.config.collection_name)

            # Batch upsert
            indexed = 0
            batch_size = self.config.batch_size

            for i in range(0, len(embeddings), batch_size):
                batch = embeddings[i : i + batch_size]

                with collection.batch.dynamic() as batch_obj:
                    for chunk, embedding in batch:
                        properties = {
                            "content": chunk.content,
                            "title": chunk.document.title,
                            "source_path": chunk.document.source_path,
                            "source_type": chunk.document.source_type,
                            "truth_level": chunk.document.truth_level,
                            "namespace": chunk.document.namespace,
                            "chunk_index": chunk.chunk_index,
                        }

                        # Use UUID v5 for deterministic, valid UUIDs
                        chunk_uuid = str(uuid.uuid5(
                            uuid.NAMESPACE_DNS,
                            f"{chunk.document.source_path}:{chunk.chunk_index}"
                        ))

                        batch_obj.add_object(
                            properties=properties,
                            vector=embedding.tolist(),
                            uuid=chunk_uuid,
                        )
                        indexed += 1

            client.close()
            return indexed

        except Exception as e:
            logger.error(f"Weaviate upsert failed: {e}")
            return 0

    async def _embed_and_upsert_streaming(self) -> int:
        """Generate embeddings and upsert to Weaviate in streaming batches.

        This method processes chunks in small batches to prevent OOM errors.
        It combines embedding generation and Weaviate upsert in a single pass.

        Returns:
            Number of chunks successfully indexed.
        """
        if not self.chunks:
            return 0

        try:
            from sentence_transformers import SentenceTransformer
            import weaviate

            logger.info("Loading embedding model...")
            model = SentenceTransformer("all-MiniLM-L6-v2")

            logger.info("Connecting to Weaviate...")
            client = weaviate.connect_to_local(
                host=self.config.weaviate_url.replace("http://", "").split(":")[0],
                port=int(self.config.weaviate_url.split(":")[-1]),
            )

            collection = client.collections.get(self.config.collection_name)

            indexed = 0
            batch_size = 20  # Small batches to prevent OOM
            total_batches = (len(self.chunks) + batch_size - 1) // batch_size

            for i in range(0, len(self.chunks), batch_size):
                batch_num = i // batch_size + 1
                batch_chunks = self.chunks[i:i + batch_size]
                texts = [c.content for c in batch_chunks]

                # Generate embeddings for this batch only
                embeddings = model.encode(texts, batch_size=8, show_progress_bar=False)

                # Upsert immediately
                with collection.batch.dynamic() as batch_obj:
                    for chunk, embedding in zip(batch_chunks, embeddings):
                        properties = {
                            "content": chunk.content,
                            "title": chunk.document.title,
                            "source_path": chunk.document.source_path,
                            "source_type": chunk.document.source_type,
                            "truth_level": chunk.document.truth_level,
                            "namespace": chunk.document.namespace,
                            "chunk_index": chunk.chunk_index,
                        }

                        # Use UUID v5 for deterministic, valid UUIDs
                        chunk_uuid = str(uuid.uuid5(
                            uuid.NAMESPACE_DNS,
                            f"{chunk.document.source_path}:{chunk.chunk_index}"
                        ))

                        batch_obj.add_object(
                            properties=properties,
                            vector=embedding.tolist(),
                            uuid=chunk_uuid,
                        )
                        indexed += 1

                # Free memory after each batch
                del embeddings
                gc.collect()

                logger.info(f"  Batch {batch_num}/{total_batches}: {indexed}/{len(self.chunks)} indexed")

            client.close()
            return indexed

        except ImportError as e:
            logger.error(f"Missing dependency: {e}")
            return 0
        except Exception as e:
            logger.error(f"Streaming embed/upsert failed: {e}")
            return 0

    async def _version_index(self) -> str:
        """Create a version tag for the index."""
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        version_tag = f"v{timestamp}"

        # Store version metadata (could be in Weaviate, MinIO, or local file)
        version_info = {
            "tag": version_tag,
            "timestamp": datetime.utcnow().isoformat(),
            "documents": len(self.documents),
            "chunks": len(self.chunks),
            "is_latest": self.config.promote_latest,
        }

        logger.info(f"Version created: {json.dumps(version_info)}")
        return version_tag


async def run_full_ingestion(config: Optional[PipelineConfig] = None) -> PipelineResult:
    """Convenience function to run full ingestion pipeline.

    Args:
        config: Pipeline configuration. If None, uses defaults.

    Returns:
        PipelineResult with statistics and status.
    """
    if config is None:
        config = PipelineConfig()

    pipeline = OrchestratorPipeline(config)
    return await pipeline.run()


if __name__ == "__main__":
    # Quick test when run directly
    logging.basicConfig(level=logging.INFO)

    async def main():
        config = PipelineConfig(
            knowledge_path="/opt/automecanik/rag/knowledge",
            minio_enabled=False,
            wiki_enabled=False,
        )
        result = await run_full_ingestion(config)
        print(f"Result: {result}")

    asyncio.run(main())
