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
import re
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from pathlib import Path
import hashlib
import json
import uuid
import gc

from .kill_switch import enforce_build_plane, require_build_plane

logger = logging.getLogger(__name__)

# Directory name -> canonical source_type mapping
DIR_TO_SOURCE_TYPE = {
    "diagnostic": "diagnostic", "diagnostics": "diagnostic",
    "gamme": "gamme", "gammes": "gamme",
    "faq": "faq", "faqs": "faq",
    "guide": "guide", "guides": "guide",
    "vehicle": "vehicle", "vehicles": "vehicle",
    "policy": "policy", "policies": "policy",
}


def resolve_namespace(metadata: Dict[str, Any], rel_path: str) -> str:
    """Resolve namespace from metadata and path. Returns knowledge:{source_type}."""
    # Priority: source_type > entity_type > directory inference
    st = metadata.get("source_type")
    if st:
        return f"knowledge:{st}"

    et = metadata.get("entity_type")
    if et and et != "unknown":
        return f"knowledge:{et}"

    parts = rel_path.split("/")
    if parts:
        first_dir = parts[0].lower()
        source_type = DIR_TO_SOURCE_TYPE.get(first_dir, "faq")
        return f"knowledge:{source_type}"

    return "knowledge:faq"


# ──────────────────────────────────────────────────
# Heuristic enrichment (intent / domain / entities)
# ──────────────────────────────────────────────────

_DOMAIN_KEYWORDS: Dict[str, List[str]] = {
    "freinage": ["frein", "plaquette", "disque de frein", "etrier", "abs", "brake", "plaquettes"],
    "moteur": ["moteur", "piston", "culasse", "soupape", "turbo", "injection", "bougie", "engine"],
    "transmission": ["embrayage", "boite de vitesse", "transmission", "cardan", "clutch", "gearbox"],
    "suspension": ["amortisseur", "ressort", "rotule", "bras de suspension", "silent-bloc", "suspension"],
    "eclairage": ["phare", "ampoule", "feux", "clignotant", "eclairage", "led", "xenon"],
    "filtration": ["filtre", "filtre a huile", "filtre a air", "filtre habitacle", "filtration"],
    "refroidissement": ["radiateur", "pompe a eau", "thermostat", "liquide de refroidissement", "cooling"],
    "echappement": ["echappement", "catalyseur", "pot", "silencieux", "fap", "dpf", "egr", "exhaust"],
    "direction": ["direction", "cremaillere", "rotule de direction", "pompe direction", "steering"],
    "electricite": ["batterie", "alternateur", "demarreur", "capteur", "sonde", "electrical"],
    "carrosserie": ["pare-chocs", "aile", "capot", "retroviseur", "calandre", "body"],
    "distribution": ["courroie", "chaine de distribution", "kit distribution", "galet", "timing"],
}

_INTENT_PATTERNS: Dict[str, List[str]] = {
    "diagnostic": ["symptome", "panne", "defaut", "probleme", "code erreur", "dtc", "obd", "voyant"],
    "guide": ["comment", "tuto", "etape", "procedure", "methode", "remplacement", "demontage", "how to"],
    "comparaison": ["versus", "vs", "difference", "comparaison", "comparatif", "meilleur"],
    "compatibilite": ["compatible", "compatibilite", "fitment", "s'adapte", "convient", "oem"],
    "tarification": ["prix", "tarif", "cout", "devis", "promo", "reduction", "price"],
    "specification": ["reference", "dimension", "specification", "technique", "fiche", "spec"],
}

_BRAND_NAMES = (
    r"Bosch|TRW|Brembo|Valeo|SKF|SNR|Sachs|LuK|Monroe|KYB|Mann|Hella|Osram|NGK|Denso|ATE|Ferodo|Textar"
    r"|Continental|Delphi|Mahle|Elring|Corteco|FAG|INA|Gates|Contitech|Dayco|Lemforder"
    r"|Renault|Peugeot|Citroen|Volkswagen|BMW|Mercedes|Audi|Opel|Ford|Toyota|Hyundai|Kia|Nissan|Fiat|Dacia"
    r"|Volvo|Seat|Skoda|Mazda|Honda|Suzuki|Mitsubishi|Alfa Romeo|Land Rover|Mini|Porsche"
)

_ENTITY_RE = re.compile(
    r"\b("
    r"[A-Z]{1,4}[0-9]{3,}[A-Z0-9]*"  # OEM refs: GDB1726, P68052, ATE24.0124
    r"|[A-Z]{2,5}-[A-Z0-9]{2,}"  # Hyphenated refs: TRW-GDB1726
    r"|(?:" + _BRAND_NAMES + r")"
    r")\b",
)


def classify_domain(content: str) -> str:
    """Classify chunk content into an automotive domain."""
    text = content.lower()
    best_domain = "general"
    best_score = 0
    for domain, keywords in _DOMAIN_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in text)
        if score > best_score:
            best_score = score
            best_domain = domain
    return best_domain if best_score >= 1 else "general"


def classify_intent(content: str) -> str:
    """Classify chunk content intent (diagnostic, guide, comparaison, etc.)."""
    text = content.lower()
    best_intent = ""
    best_score = 0
    for intent, keywords in _INTENT_PATTERNS.items():
        score = sum(1 for kw in keywords if kw in text)
        if score > best_score:
            best_score = score
            best_intent = intent
    return best_intent if best_score >= 1 else ""


def extract_entities(content: str) -> List[str]:
    """Extract brand names and OEM references from chunk content."""
    matches = _ENTITY_RE.findall(content)
    seen: set[str] = set()
    entities: List[str] = []
    for m in matches:
        normalized = m.strip()
        key = normalized.lower()
        if key not in seen and len(normalized) >= 2:
            seen.add(key)
            entities.append(normalized)
    return entities[:30]  # Cap at 30 entities per chunk


def compute_doc_weight(truth_level: str, is_canonical: bool) -> float:
    """Compute document weight from truth level and canonical status."""
    base = {"L1": 1.0, "L2": 0.85, "L3": 0.7, "L4": 0.5}.get(truth_level, 0.7)
    if is_canonical:
        base = min(1.0, base + 0.15)
    return base


def compute_evidence_grade(
    content: str,
    truth_level: str,
    domain: str,
    entities: List[str],
    heading: Optional[str],
) -> str:
    """Compute evidence grade (A/B/C/D) based on chunk quality signals.

    Grades:
      A - High quality: canonical truth, rich entities, clear heading
      B - Good quality: verified truth or good domain/entity coverage
      C - Acceptable: basic content with some structure
      D - Low quality: thin content, no entities, heuristic truth
    """
    score = 0.0

    # Truth level contribution (0-30)
    truth_scores = {"L1": 30, "L2": 22, "L3": 14, "L4": 5}
    score += truth_scores.get(truth_level, 10)

    # Entity richness (0-25)
    entity_count = len(entities)
    if entity_count >= 5:
        score += 25
    elif entity_count >= 3:
        score += 18
    elif entity_count >= 1:
        score += 10

    # Content length / depth (0-20)
    word_count = len(content.split())
    if word_count >= 200:
        score += 20
    elif word_count >= 100:
        score += 14
    elif word_count >= 40:
        score += 8

    # Has heading structure (0-15)
    if heading:
        score += 15
    elif "##" in content or "**" in content:
        score += 8

    # Domain specificity (0-10)
    if domain and domain != "general":
        score += 10

    if score >= 75:
        return "A"
    if score >= 55:
        return "B"
    if score >= 35:
        return "C"
    return "D"


def infer_doc_family(source_type: str, namespace: str) -> str:
    """Map source_type + namespace to doc_family."""
    ns = namespace.lower() if namespace else ""
    if "diagnostic" in ns or source_type == "diagnostic":
        return "diagnostic"
    if "gamme" in ns or "catalog" in ns or source_type == "gamme":
        return "catalog"
    if "media" in ns or source_type == "media":
        return "media"
    if "router" in ns:
        return "router_memory"
    return "knowledge"


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
    collection_name: str = "KB_Knowledge"

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
            collection_name=config.get("vector_store", {}).get("class_name", "KB_Knowledge"),
        )


@dataclass
class Document:
    """A document to be indexed."""

    source_path: str
    content: str
    title: str = ""
    source_type: str = "knowledge"  # knowledge | wiki | minio
    truth_level: str = "L3"
    namespace: str = ""  # Computed from source_path via resolve_namespace()
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
    heading: Optional[str] = None
    heading_level: Optional[int] = None

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

                namespace = resolve_namespace(metadata, str(relative_path))

                docs.append(
                    Document(
                        source_path=str(relative_path),
                        content=content,
                        title=title,
                        source_type="knowledge",
                        truth_level=truth_level,
                        namespace=namespace,
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

    async def _upsert_weaviate(self, embeddings: List[tuple]) -> int:
        """Upsert chunks with embeddings to Weaviate (legacy method).

        Uses full 29-property gold schema and collection routing.
        """
        if not embeddings:
            return 0

        try:
            from app.services.weaviate_client import get_weaviate_client

            weaviate_client = get_weaviate_client()

            indexed = 0
            batch_size = self.config.batch_size

            for i in range(0, len(embeddings), batch_size):
                batch = embeddings[i : i + batch_size]

                # Group by target collection
                collection_groups: Dict[str, List[tuple]] = {}
                for chunk, embedding in batch:
                    props = self._build_chunk_properties(chunk)
                    target = weaviate_client.resolve_collection(
                        namespace=chunk.document.namespace,
                    )
                    vec = embedding.tolist() if hasattr(embedding, "tolist") else list(embedding)
                    if target not in collection_groups:
                        collection_groups[target] = []
                    collection_groups[target].append((props, vec))

                for target_collection, items in collection_groups.items():
                    collection = weaviate_client.client.collections.get(target_collection)
                    with collection.batch.dynamic() as batch_obj:
                        for props, vec in items:
                            chunk_uuid = str(uuid.uuid5(
                                uuid.NAMESPACE_URL,
                                f"{props['source_path']}:{props['chunk_index']}:{props['content_hash']}",
                            ))
                            batch_obj.add_object(
                                properties=props,
                                vector=vec,
                                uuid=chunk_uuid,
                            )
                            indexed += 1

            return indexed

        except Exception as e:
            logger.error(f"Weaviate upsert failed: {e}")
            return 0

    def _build_chunk_properties(self, chunk: Chunk) -> Dict[str, Any]:
        """Build all 29 gold schema properties for a chunk."""
        now_iso = datetime.now(timezone.utc).isoformat()
        content_hash = hashlib.sha256(chunk.content.encode()).hexdigest()[:32]

        # Deterministic chunk ID (UUID v5)
        chunk_id = str(uuid.uuid5(
            uuid.NAMESPACE_URL,
            f"{chunk.document.source_path}:{chunk.chunk_index}:{content_hash}",
        ))

        # Heuristic enrichment
        domain = classify_domain(chunk.content)
        intent = classify_intent(chunk.content)
        entities = extract_entities(chunk.content)
        doc_family = infer_doc_family(chunk.document.source_type, chunk.document.namespace)
        is_canonical = chunk.document.truth_level in ("L1", "L2")
        doc_weight = compute_doc_weight(chunk.document.truth_level, is_canonical)
        evidence_grade = compute_evidence_grade(
            content=chunk.content,
            truth_level=chunk.document.truth_level,
            domain=domain,
            entities=entities,
            heading=chunk.heading,
        )

        # Source URI with heading anchor if available
        source_uri = chunk.document.source_path
        if chunk.heading:
            slug = re.sub(r"[^a-z0-9\s-]", "", chunk.heading.lower())
            slug = re.sub(r"[\s-]+", "-", slug).strip("-")
            source_uri = f"{source_uri}#section={slug}"

        # Anchors from heading
        anchors: List[str] = []
        if chunk.heading:
            anchors.append(f"heading:{chunk.heading}")
        if chunk.heading_level:
            anchors.append(f"h{chunk.heading_level}")

        # Infer category from metadata
        category = chunk.document.metadata.get("category", "")
        if not category:
            category = doc_family

        # Role classification (Phase 1)
        from .processors.role_classifier import classify_chunk as _classify_chunk
        role_fields = _classify_chunk(
            heading=chunk.heading,
            chunk_type="text",
            content=chunk.content,
            source_type=chunk.document.source_type,
        )

        return {
            "chunk_id": chunk_id,
            "parent_id": chunk.document.source_id,
            "source_path": chunk.document.source_path,
            "source_uri": source_uri,
            "source_ref": f"sha256:{content_hash}",
            "title": chunk.document.title,
            "content": chunk.content,
            "anchors": anchors,
            "intent": intent,
            "domain": domain,
            "entities": entities,
            "truth_level": chunk.document.truth_level,
            "verification_status": chunk.document.metadata.get("verification_status", "unverified"),
            "doc_weight": doc_weight,
            "evidence_grade": evidence_grade,
            "is_canonical": is_canonical,
            "canonical_weight": doc_weight if is_canonical else 0.0,
            "chunk_index": chunk.chunk_index,
            "created_at": now_iso,
            "updated_at": now_iso,
            "content_hash": content_hash,
            "source_type": chunk.document.source_type,
            "doc_family": doc_family,
            "namespace": chunk.document.namespace,
            "category": category,
            "language": "fr",
            "confidence_score": {"A": 0.92, "B": 0.75, "C": 0.55, "D": 0.35}.get(evidence_grade, 0.5),
            "last_verified_date": "",
            "verified_by": "",
            **role_fields,
        }

    async def _embed_and_upsert_streaming(self) -> int:
        """Generate embeddings and upsert to Weaviate in streaming batches.

        This method processes chunks in small batches to prevent OOM errors.
        It combines embedding generation and Weaviate upsert in a single pass.
        All 29 gold schema properties are populated with heuristic enrichment.

        Returns:
            Number of chunks successfully indexed.
        """
        if not self.chunks:
            return 0

        try:
            from app.services.embeddings import get_embeddings_service
            from app.services.weaviate_client import get_weaviate_client

            logger.info("Loading embedding service (FastEmbed)...")
            embeddings_service = get_embeddings_service()

            logger.info("Connecting to Weaviate...")
            weaviate_client = get_weaviate_client()

            indexed = 0
            batch_size = 20  # Small batches to prevent OOM
            total_batches = (len(self.chunks) + batch_size - 1) // batch_size

            # Group chunks by target collection for correct routing
            for i in range(0, len(self.chunks), batch_size):
                batch_num = i // batch_size + 1
                batch_chunks = self.chunks[i:i + batch_size]
                texts = [c.content for c in batch_chunks]

                # Generate embeddings for this batch only
                vectors = embeddings_service.embed_batch(texts, batch_size=8)

                # Group by target collection within this batch
                collection_groups: Dict[str, List[tuple]] = {}
                for chunk, vector in zip(batch_chunks, vectors):
                    props = self._build_chunk_properties(chunk)
                    target = weaviate_client.resolve_collection(
                        namespace=chunk.document.namespace,
                    )
                    if target not in collection_groups:
                        collection_groups[target] = []
                    collection_groups[target].append((props, vector))

                # Upsert each collection group
                for target_collection, items in collection_groups.items():
                    collection = weaviate_client.client.collections.get(target_collection)
                    with collection.batch.dynamic() as batch_obj:
                        for props, vector in items:
                            chunk_uuid = str(uuid.uuid5(
                                uuid.NAMESPACE_URL,
                                f"{props['source_path']}:{props['chunk_index']}:{props['content_hash']}",
                            ))
                            batch_obj.add_object(
                                properties=props,
                                vector=vector,
                                uuid=chunk_uuid,
                            )
                            indexed += 1

                # Free memory after each batch
                del vectors
                gc.collect()

                logger.info(f"  Batch {batch_num}/{total_batches}: {indexed}/{len(self.chunks)} indexed")

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
