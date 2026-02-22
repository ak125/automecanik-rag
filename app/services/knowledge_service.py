"""Knowledge management service for RAG corpus CRUD operations."""

import json
import os
import re
import uuid
import logging
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional
from dataclasses import dataclass, field

import frontmatter

from app.config import get_settings

logger = logging.getLogger(__name__)

CORE_DOC_FAMILIES = {"catalog", "diagnostic", "knowledge"}
ALLOWED_DOC_FAMILIES = CORE_DOC_FAMILIES | {"media", "router_memory"}

DIR_TO_SOURCE_TYPE = {
    "catalog": "gamme",
    "gamme": "gamme",
    "gammes": "gamme",
    "diagnostic": "diagnostic",
    "diagnostics": "diagnostic",
    "faq": "faq",
    "faqs": "faq",
    "policy": "policy",
    "policies": "policy",
    "guide": "guide",
    "guides": "guide",
    "vehicle": "vehicle",
    "vehicles": "vehicle",
    "knowledge": "knowledge",
    "canonical": "canonical",
    "media": "media",
    "router_memory": "router_memory",
    "routermemory": "router_memory",
}

SOURCE_TYPE_TO_DOC_FAMILY = {
    "diagnostic": "diagnostic",
    "gamme": "catalog",
    "catalog": "catalog",
    "vehicle": "catalog",
    "json": "catalog",
    "csv": "catalog",
    "faq": "knowledge",
    "policy": "knowledge",
    "guide": "knowledge",
    "knowledge": "knowledge",
    "canonical": "knowledge",
    "general": "knowledge",
    "support": "knowledge",
    "media": "media",
    "image": "media",
    "video": "media",
    "audio": "media",
    "router_memory": "router_memory",
}

ALLOWED_DIRS_BY_FAMILY = {
    "catalog": {"catalog", "gamme", "gammes", "vehicle", "vehicles", "tabular", "structured"},
    "diagnostic": {"diagnostic", "diagnostics"},
    "knowledge": {"knowledge", "guide", "guides", "faq", "faqs", "policy", "policies", "canonical", "general"},
    "media": {"media", "video", "image", "audio"},
    "router_memory": {"router_memory", "routermemory"},
}


@dataclass
class KnowledgeDocument:
    """Represents a knowledge document."""
    id: str
    title: str
    content: str
    source_type: str
    category: str
    doc_family: str = "knowledge"
    truth_level: str = "L3"
    verification_status: str = "unverified"
    source_path: str = ""
    source_uri: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "source_type": self.source_type,
            "category": self.category,
            "doc_family": self.doc_family,
            "truth_level": self.truth_level,
            "verification_status": self.verification_status,
            "source_path": self.source_path,
            "source_uri": self.source_uri,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


@dataclass
class KnowledgeListResponse:
    """Response for listing knowledge documents."""
    documents: list[KnowledgeDocument] = field(default_factory=list)
    total: int = 0
    page: int = 1
    limit: int = 20
    categories: list[str] = field(default_factory=list)
    source_types: list[str] = field(default_factory=list)
    doc_families: list[str] = field(default_factory=list)


class KnowledgeService:
    """Service for managing knowledge corpus files."""

    def __init__(self):
        self.settings = get_settings()
        self.knowledge_path = Path(self.settings.knowledge_path)

    def _generate_id(self, source_path: str) -> str:
        """Generate a unique ID from source path."""
        # Use path as base for ID (remove extension, replace / with .)
        clean_path = source_path.replace("/", ".").replace("\\", ".")
        if clean_path.endswith(".md"):
            clean_path = clean_path[:-3]
        return clean_path

    def _is_ignored_dir(self, dirname: str) -> bool:
        """Directories excluded from document listing/search."""
        if dirname.startswith("."):
            return True
        return dirname in {"_trash", "_raw", "__pycache__"}

    def _parse_document(self, file_path: Path) -> Optional[KnowledgeDocument]:
        """Parse a markdown file into a KnowledgeDocument."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                post = frontmatter.load(f)

            # Get relative path from knowledge root
            rel_path = str(file_path.relative_to(self.knowledge_path))

            # Extract metadata from frontmatter
            metadata = post.metadata
            source_type = metadata.get("source_type", self._infer_source_type(rel_path))
            category = metadata.get("category", self._infer_category(rel_path))
            explicit_doc_family = metadata.get("doc_family", "")
            try:
                doc_family = self._resolve_doc_family(
                    source_type=source_type,
                    explicit_doc_family=explicit_doc_family,
                    rel_path=rel_path,
                )
            except ValueError:
                # Never block read path: fallback to inferred family.
                doc_family = self._resolve_doc_family(
                    source_type=source_type,
                    explicit_doc_family="",
                    rel_path=rel_path,
                )

            # Get file stats for dates
            stat = file_path.stat()
            created_at = metadata.get("created_at") or datetime.fromtimestamp(stat.st_ctime).isoformat()
            updated_at = metadata.get("updated_at") or datetime.fromtimestamp(stat.st_mtime).isoformat()

            return KnowledgeDocument(
                id=self._generate_id(rel_path),
                title=metadata.get("title", file_path.stem.replace("-", " ").title()),
                content=post.content,
                source_type=source_type,
                category=category,
                doc_family=doc_family,
                truth_level=metadata.get("truth_level", "L3"),
                verification_status=metadata.get("verification_status", "unverified"),
                source_path=rel_path,
                source_uri=metadata.get("source_uri", ""),
                created_at=created_at if isinstance(created_at, str) else str(created_at),
                updated_at=updated_at if isinstance(updated_at, str) else str(updated_at),
            )
        except Exception as e:
            logger.error(f"Error parsing document {file_path}: {e}")
            return None

    def _infer_source_type(self, rel_path: str) -> str:
        """Infer source type from path."""
        parts = rel_path.split("/")
        if parts:
            first_dir = parts[0].lower()
            inferred = DIR_TO_SOURCE_TYPE.get(first_dir)
            if inferred:
                return inferred
        return "general"

    def _infer_category(self, rel_path: str) -> str:
        """Infer category from path or filename."""
        parts = [p for p in rel_path.split("/") if p]
        if not parts:
            return "general"
        if len(parts) > 1 and parts[0].lower() in {"catalog", "diagnostic", "knowledge"}:
            return parts[1]
        return parts[0]

    def _normalize_doc_family(self, doc_family: Optional[str]) -> str:
        """Normalize doc_family aliases and enforce allowed values."""
        fam = (doc_family or "").strip().lower().replace("-", "_")
        if fam == "routermemory":
            fam = "router_memory"
        if fam and fam not in ALLOWED_DOC_FAMILIES:
            raise ValueError(
                f"Invalid doc_family='{fam}'. Allowed: {sorted(ALLOWED_DOC_FAMILIES)}"
            )
        return fam

    def _infer_doc_family_from_path(self, rel_path: str) -> str:
        parts = [p for p in rel_path.split("/") if p]
        if not parts:
            return "knowledge"
        first = parts[0].lower()
        if first in {"catalog", "gamme", "gammes", "vehicle", "vehicles", "tabular", "structured"}:
            return "catalog"
        if first in {"diagnostic", "diagnostics"}:
            return "diagnostic"
        if first in {"media"}:
            return "media"
        if first in {"router_memory", "routermemory"}:
            return "router_memory"
        return "knowledge"

    def _resolve_doc_family(
        self,
        source_type: str,
        explicit_doc_family: Optional[str] = None,
        rel_path: str = "",
    ) -> str:
        source_type_norm = (source_type or "general").strip().lower()
        explicit = self._normalize_doc_family(explicit_doc_family)
        inferred = SOURCE_TYPE_TO_DOC_FAMILY.get(source_type_norm)
        if not inferred and rel_path:
            inferred = self._infer_doc_family_from_path(rel_path)
        resolved = explicit or inferred or "knowledge"

        expected = SOURCE_TYPE_TO_DOC_FAMILY.get(source_type_norm)
        if expected and resolved != expected:
            raise ValueError(
                f"source_type='{source_type_norm}' must belong to doc_family='{expected}', got '{resolved}'"
            )
        return resolved

    def _directory_for_source_type(self, source_type: str) -> str:
        st = (source_type or "").strip().lower()
        dir_map = {
            "diagnostic": "diagnostic",
            "faq": "faq",
            "policy": "policies",
            "guide": "guides",
            "vehicle": "vehicle",
            "gamme": "gammes",
            "catalog": "catalog",
            "knowledge": "knowledge",
            "canonical": "canonical",
            "media": "media",
            "image": "media",
            "video": "media",
            "audio": "media",
            "router_memory": "router_memory",
            "json": "structured",
            "csv": "tabular",
        }
        return dir_map.get(st, st or "knowledge")

    def _validate_directory_for_family(self, directory: str, doc_family: str) -> None:
        allowed = ALLOWED_DIRS_BY_FAMILY.get(doc_family, set())
        if directory.lower() not in allowed:
            raise ValueError(
                f"Write path blocked: directory='{directory}' incompatible with doc_family='{doc_family}'"
            )

    def _strip_frontmatter_block(self, content: str) -> str:
        """Remove a leading YAML frontmatter block if present."""
        text = content.lstrip("\ufeff")
        if not text.startswith("---"):
            return content

        end_idx = text.find("\n---", 3)
        if end_idx == -1:
            return content

        return text[end_idx + 4:].lstrip("\n")

    def _clean_raw_content(self, content: str) -> str:
        """
        Clean noisy raw text while preserving useful technical information.

        Rules:
        - remove frontmatter duplicated from copy/paste
        - normalize whitespace
        - drop obvious navigation/cookie/footer noise lines
        - collapse repeated duplicate lines
        """
        text = self._strip_frontmatter_block(content)
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        # Remove excessive spacing but keep paragraph boundaries.
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)

        noisy_line_patterns = [
            r"^cookie(s)?\b",
            r"^politique de confidentialit[eé]\b",
            r"^conditions (g[eé]n[eé]rales|d'utilisation)\b",
            r"^mentions l[eé]gales\b",
            r"^accepter (tous )?les cookies\b",
            r"^refuser (tous )?les cookies\b",
            r"^menu\b",
            r"^navigation\b",
            r"^retour (en haut|accueil)\b",
            r"^suivez-nous\b",
            r"^inscrivez-vous [aà] la newsletter\b",
            r"^tous droits r[eé]serv[eé]s\b",
        ]

        cleaned_lines: list[str] = []
        seen_normalized: set[str] = set()

        for raw_line in text.split("\n"):
            line = raw_line.strip()
            if not line:
                cleaned_lines.append("")
                continue

            lower = line.lower()
            if any(re.match(pattern, lower) for pattern in noisy_line_patterns):
                continue

            normalized = re.sub(r"\W+", "", lower)
            if normalized and normalized in seen_normalized:
                continue
            if normalized:
                seen_normalized.add(normalized)

            cleaned_lines.append(line)

        cleaned = "\n".join(cleaned_lines).strip()
        cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
        return cleaned

    def _infer_source_type_from_content(self, content: str) -> str:
        """Infer source type from lexical signals in the content."""
        text = content.lower()
        signals = {
            "diagnostic": [
                "sympt",
                "bruit",
                "vibration",
                "panne",
                "diagnostic",
                "contr[ôo]le",
                "cause probable",
            ],
            "faq": [
                "faq",
                "question",
                "r[eé]ponse",
                "combien",
                "pourquoi",
                "comment",
            ],
            "policy": [
                "livraison",
                "retour",
                "remboursement",
                "garantie",
                "paiement",
                "conditions",
            ],
            "guide": [
                "guide",
                "[eé]tape",
                "proc[eé]dure",
                "tutoriel",
                "installation",
                "montage",
            ],
            "vehicle": [
                "mod[eè]le",
                "motorisation",
                "immatriculation",
                "vin",
                "v[eé]hicule",
            ],
            "gamme": [
                "gamme",
                "r[eé]f[eé]rence",
                "caract[eé]ristique",
                "compatibilit[eé]",
                "sp[eé]cification",
            ],
        }

        scores: dict[str, int] = {k: 0 for k in signals}
        for source_type, patterns in signals.items():
            for pattern in patterns:
                if re.search(pattern, text):
                    scores[source_type] += 1

        best_type = max(scores, key=scores.get)
        return best_type if scores[best_type] > 0 else "general"

    def _infer_category_from_content(self, source_type: str, content: str) -> str:
        """Infer a coarse category from source type and content keywords."""
        text = content.lower()
        category_signals = {
            "freinage": [
                r"frein", r"plaquette", r"disque", r"[eé]trier",
                r"\bbrake(s)?\b", r"\bdisc(s)?\b", r"\brotor(s)?\b", r"\bpad(s)?\b", r"\bcaliper(s)?\b",
            ],
            "moteur": [r"moteur", r"injection", r"allumage", r"bougie"],
            "refroidissement": [r"refroidissement", r"radiateur", r"thermostat"],
            "suspension": [r"suspension", r"amortisseur", r"triangle"],
            "direction": [r"direction", r"cr[eé]maill[eè]re", r"rotule"],
            "embrayage": [r"embrayage", r"but[eé]e", r"volant moteur"],
            "transmission": [r"transmission", r"cardan", r"bo[iî]te"],
            "electrique": [r"alternateur", r"g[eé]n[eé]rateur", r"d[eé]marreur", r"stator", r"r[eé]gulateur", r"batterie"],
            "livraison": [r"livraison", r"d[eé]lai", r"exp[eé]dition"],
            "retours": [r"retour", r"remboursement", r"r[eé]tractation"],
            "paiement": [r"paiement", r"carte", r"virement", r"facture"],
        }

        best_category = "general"
        best_score = 0
        for category, patterns in category_signals.items():
            score = sum(1 for pattern in patterns if re.search(pattern, text))
            if score > best_score:
                best_score = score
                best_category = category

        if best_score > 0:
            return best_category
        return source_type if source_type != "general" else "general"

    def _find_existing_by_source_uri(self, source_uri: str) -> Optional[KnowledgeDocument]:
        """Return the first document with matching source_uri, if any."""
        needle = (source_uri or "").strip()
        if not needle:
            return None

        for root, dirs, files in os.walk(self.knowledge_path):
            dirs[:] = [d for d in dirs if not self._is_ignored_dir(d)]
            for file in files:
                if not file.endswith(".md") or file.startswith("."):
                    continue
                doc = self._parse_document(Path(root) / file)
                if doc and (doc.source_uri or "").strip() == needle:
                    return doc
        return None

    def _save_document(self, doc: KnowledgeDocument) -> bool:
        """Save a document to disk."""
        try:
            file_path = self.knowledge_path / doc.source_path

            # Ensure parent directory exists
            file_path.parent.mkdir(parents=True, exist_ok=True)

            # Create frontmatter post
            post = frontmatter.Post(doc.content)
            post.metadata = {
                "title": doc.title,
                "source_type": doc.source_type,
                "category": doc.category,
                "doc_family": doc.doc_family,
                "truth_level": doc.truth_level,
                "verification_status": doc.verification_status,
                "created_at": doc.created_at or datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
            }
            if doc.source_uri:
                post.metadata["source_uri"] = doc.source_uri

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(frontmatter.dumps(post))

            return True
        except Exception as e:
            logger.error(f"Error saving document {doc.source_path}: {e}")
            return False

    def list_documents(
        self,
        page: int = 1,
        limit: int = 20,
        category: Optional[str] = None,
        doc_family: Optional[str] = None,
        source_type: Optional[str] = None,
        truth_level: Optional[str] = None,
        search: Optional[str] = None,
        exclude_source_types: Optional[list[str]] = None,
        deduplicate: bool = False,
    ) -> KnowledgeListResponse:
        """List all knowledge documents with optional filters."""
        documents = []
        categories = set()
        source_types = set()
        doc_families = set()
        excluded_types = {s.strip().lower() for s in (exclude_source_types or []) if s.strip()}

        # Walk through knowledge directory
        for root, dirs, files in os.walk(self.knowledge_path):
            dirs[:] = [d for d in dirs if not self._is_ignored_dir(d)]

            for file in files:
                if not file.endswith(".md"):
                    continue
                if file.startswith("."):
                    continue

                file_path = Path(root) / file
                doc = self._parse_document(file_path)

                if doc:
                    categories.add(doc.category)
                    source_types.add(doc.source_type)
                    doc_families.add(doc.doc_family)

                    # Apply filters
                    if category and doc.category != category:
                        continue
                    if doc_family and doc.doc_family != doc_family:
                        continue
                    if source_type and doc.source_type != source_type:
                        continue
                    if excluded_types and doc.source_type.lower() in excluded_types:
                        continue
                    if truth_level and doc.truth_level != truth_level:
                        continue
                    if search:
                        search_lower = search.lower()
                        if (search_lower not in doc.title.lower() and
                            search_lower not in doc.content.lower()):
                            continue

                    documents.append(doc)

        # Sort by updated_at descending
        documents.sort(key=lambda d: d.updated_at or "", reverse=True)

        # Optional view-level deduplication for admin readability.
        if deduplicate:
            seen_keys: set[str] = set()
            deduped: list[KnowledgeDocument] = []
            for doc in documents:
                src_key = (doc.source_uri or "").strip().lower()
                if src_key:
                    key = f"src::{src_key}::{doc.source_type.lower()}"
                else:
                    title_norm = re.sub(r"\s+", " ", (doc.title or "").strip().lower())
                    key = f"title::{title_norm}::{doc.source_type.lower()}::{doc.category.lower()}"
                if key in seen_keys:
                    continue
                seen_keys.add(key)
                deduped.append(doc)
            documents = deduped

        # Pagination
        total = len(documents)
        start = (page - 1) * limit
        end = start + limit
        paginated_docs = documents[start:end]

        return KnowledgeListResponse(
            documents=paginated_docs,
            total=total,
            page=page,
            limit=limit,
            categories=sorted(list(categories)),
            source_types=sorted(list(source_types)),
            doc_families=sorted(list(doc_families)),
        )

    def get_document(self, doc_id: str) -> Optional[KnowledgeDocument]:
        """Get a single document by ID."""
        # Convert ID back to path
        source_path = doc_id.replace(".", "/") + ".md"
        file_path = (self.knowledge_path / source_path).resolve()

        # Prevent path traversal attacks
        if not str(file_path).startswith(str(self.knowledge_path.resolve())):
            logger.warning(f"Path traversal attempt blocked: doc_id={doc_id}")
            return None

        if not file_path.exists():
            # Try searching for the document
            for root, dirs, files in os.walk(self.knowledge_path):
                dirs[:] = [d for d in dirs if not self._is_ignored_dir(d)]
                for file in files:
                    if file.endswith(".md"):
                        fp = Path(root) / file
                        doc = self._parse_document(fp)
                        if doc and doc.id == doc_id:
                            return doc
            return None

        return self._parse_document(file_path)

    def create_document(
        self,
        title: str,
        content: str,
        source_type: str,
        category: str,
        doc_family: str = "",
        truth_level: str = "L3",
        source_uri: str = "",
    ) -> Optional[KnowledgeDocument]:
        """Create a new knowledge document."""
        cleaned_content = self._clean_raw_content(content)
        resolved_source_type = source_type
        resolved_category = category

        # Auto-classify if user sends generic/auto placeholders.
        if resolved_source_type in ["", "general", "auto"]:
            resolved_source_type = self._infer_source_type_from_content(cleaned_content)
        if resolved_category in ["", "general", "auto"]:
            resolved_category = self._infer_category_from_content(resolved_source_type, cleaned_content)

        resolved_doc_family = self._resolve_doc_family(
            source_type=resolved_source_type,
            explicit_doc_family=doc_family,
        )

        # Tombstone check: skip documents that were explicitly deleted.
        if source_uri and self.is_tombstoned(source_uri):
            logger.info(f"Skipping tombstoned source_uri={source_uri}")
            return None

        # Idempotent create for ingestion pipelines: same source_uri => update existing doc.
        existing_doc = self._find_existing_by_source_uri(source_uri)
        if existing_doc:
            existing_doc.title = re.sub(r"\s+", " ", title).strip()
            existing_doc.content = cleaned_content
            existing_doc.source_type = resolved_source_type
            existing_doc.category = resolved_category
            existing_doc.doc_family = resolved_doc_family
            existing_doc.truth_level = truth_level
            existing_doc.updated_at = datetime.now().isoformat()
            self._validate_directory_for_family(
                directory=Path(existing_doc.source_path).parts[0] if Path(existing_doc.source_path).parts else "",
                doc_family=resolved_doc_family,
            )
            if self._save_document(existing_doc):
                return existing_doc
            return None

        clean_title = re.sub(r"\s+", " ", title).strip()

        # Generate filename from title
        filename = re.sub(r"[^\w\s-]", "", clean_title.lower())
        filename = re.sub(r"[-\s]+", "-", filename).strip("-")
        filename = f"{filename}.md"

        # Strict write-path: source_type + doc_family must map to a valid directory.
        directory = self._directory_for_source_type(resolved_source_type)
        self._validate_directory_for_family(directory, resolved_doc_family)

        source_path = f"{directory}/{filename}"

        # Check if file already exists
        file_path = self.knowledge_path / source_path
        if file_path.exists():
            # Add unique suffix
            base = filename[:-3]  # Remove .md
            source_path = f"{directory}/{base}-{uuid.uuid4().hex[:6]}.md"

        doc = KnowledgeDocument(
            id=self._generate_id(source_path),
            title=clean_title,
            content=cleaned_content,
            source_type=resolved_source_type,
            category=resolved_category,
            doc_family=resolved_doc_family,
            truth_level=truth_level,
            verification_status="unverified",
            source_path=source_path,
            source_uri=source_uri,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
        )

        if self._save_document(doc):
            return doc
        return None

    def update_document(
        self,
        doc_id: str,
        title: Optional[str] = None,
        content: Optional[str] = None,
        source_type: Optional[str] = None,
        category: Optional[str] = None,
        doc_family: Optional[str] = None,
        truth_level: Optional[str] = None,
        verification_status: Optional[str] = None,
    ) -> Optional[KnowledgeDocument]:
        """Update an existing document."""
        doc = self.get_document(doc_id)
        if not doc:
            return None

        # Update fields if provided
        if title is not None:
            doc.title = re.sub(r"\s+", " ", title).strip()
        if content is not None:
            doc.content = self._clean_raw_content(content)
        if source_type is not None:
            doc.source_type = source_type
        if category is not None:
            doc.category = category

        # Re-run auto classification when generic placeholders are used.
        if doc.source_type in ["", "general", "auto"]:
            doc.source_type = self._infer_source_type_from_content(doc.content)
        if doc.category in ["", "general", "auto"]:
            doc.category = self._infer_category_from_content(doc.source_type, doc.content)
        doc.doc_family = self._resolve_doc_family(
            source_type=doc.source_type,
            explicit_doc_family=doc_family or doc.doc_family,
            rel_path=doc.source_path,
        )
        self._validate_directory_for_family(
            directory=Path(doc.source_path).parts[0] if Path(doc.source_path).parts else "",
            doc_family=doc.doc_family,
        )
        if truth_level is not None:
            doc.truth_level = truth_level
        if verification_status is not None:
            doc.verification_status = verification_status

        doc.updated_at = datetime.now().isoformat()

        if self._save_document(doc):
            return doc
        return None

    def delete_document(self, doc_id: str, leave_tombstone: bool = True) -> bool:
        """Delete a document and optionally leave a tombstone to prevent re-ingestion.

        Args:
            doc_id: Document identifier.
            leave_tombstone: If True, write a tombstone record so the same
                source_uri is not re-ingested on the next pipeline run.

        Returns:
            True if the document was deleted successfully.
        """
        doc = self.get_document(doc_id)
        if not doc:
            return False

        file_path = self.knowledge_path / doc.source_path
        try:
            if file_path.exists():
                if leave_tombstone and doc.source_uri:
                    self._write_tombstone(doc)
                file_path.unlink()

                # Best-effort Weaviate cleanup
                self._delete_weaviate_chunks(doc)
                return True
        except Exception as e:
            logger.error(f"Error deleting document {doc_id}: {e}")

        return False

    # ── Tombstone support ──────────────────────────────────

    def _tombstone_dir(self) -> Path:
        return self.knowledge_path / "_trash" / "tombstones"

    def _tombstone_path(self, source_uri: str) -> Path:
        import hashlib
        digest = hashlib.sha256(source_uri.encode()).hexdigest()[:16]
        return self._tombstone_dir() / f"{digest}.json"

    def _write_tombstone(self, doc: "KnowledgeDocument") -> None:
        """Write a tombstone record for a deleted document."""
        tombstone_dir = self._tombstone_dir()
        tombstone_dir.mkdir(parents=True, exist_ok=True)
        record = {
            "source_uri": doc.source_uri,
            "source_path": doc.source_path,
            "title": doc.title,
            "deleted_at": datetime.now(timezone.utc).isoformat(),
            "reason": "deleted_by_user",
        }
        path = self._tombstone_path(doc.source_uri)
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        logger.info(f"Tombstone written for source_uri={doc.source_uri}")

    def is_tombstoned(self, source_uri: str) -> bool:
        """Check whether a source_uri has a tombstone (was previously deleted)."""
        if not source_uri:
            return False
        return self._tombstone_path(source_uri).exists()

    def revive_tombstone(self, source_uri: str) -> bool:
        """Remove a tombstone so the document can be re-ingested."""
        path = self._tombstone_path(source_uri)
        if path.exists():
            path.unlink()
            logger.info(f"Tombstone revived for source_uri={source_uri}")
            return True
        return False

    def list_tombstones(self) -> list[dict]:
        """List all tombstone records."""
        tombstone_dir = self._tombstone_dir()
        if not tombstone_dir.exists():
            return []
        records = []
        for f in sorted(tombstone_dir.glob("*.json")):
            try:
                records.append(json.loads(f.read_text(encoding="utf-8")))
            except Exception:
                pass
        return records

    def _delete_weaviate_chunks(self, doc: "KnowledgeDocument") -> None:
        """Best-effort deletion of Weaviate chunks belonging to this document."""
        try:
            from app.services.weaviate_client import get_weaviate_client
            from weaviate.classes.query import Filter

            weaviate_client = get_weaviate_client()
            target = weaviate_client.resolve_collection(
                namespace=f"knowledge:{doc.source_type}",
            )
            collection = weaviate_client.client.collections.get(target)
            # Delete all chunks whose parent_id matches this doc
            collection.data.delete_many(
                where=Filter.by_property("parent_id").equal(doc.id),
            )
            logger.info(f"Weaviate chunks deleted for parent_id={doc.id} in {target}")
        except ImportError:
            logger.debug("Weaviate client not available, skipping vector cleanup")
        except Exception as exc:
            logger.warning(f"Weaviate chunk cleanup failed: {exc}")

    def promote_document(self, doc_id: str) -> Optional[KnowledgeDocument]:
        """Promote a document to the next truth level."""
        doc = self.get_document(doc_id)
        if not doc:
            return None

        # Promotion order: L4 -> L3 -> L2 -> L1
        promotion_map = {
            "L4": "L3",
            "L3": "L2",
            "L2": "L1",
            "L1": "L1",  # Already at max
        }

        new_level = promotion_map.get(doc.truth_level, doc.truth_level)

        if new_level != doc.truth_level:
            doc.truth_level = new_level
            doc.verification_status = "verified" if new_level in ["L1", "L2"] else "unverified"
            doc.updated_at = datetime.now().isoformat()

            if self._save_document(doc):
                return doc

        return doc


# Singleton instance
_knowledge_service: Optional[KnowledgeService] = None


def get_knowledge_service() -> KnowledgeService:
    """Get the knowledge service singleton."""
    global _knowledge_service
    if _knowledge_service is None:
        _knowledge_service = KnowledgeService()
    return _knowledge_service
