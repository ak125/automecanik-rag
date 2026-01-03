"""Knowledge management service for RAG corpus CRUD operations."""

import os
import re
import uuid
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional
from dataclasses import dataclass, field

import frontmatter

from app.config import get_settings

logger = logging.getLogger(__name__)


@dataclass
class KnowledgeDocument:
    """Represents a knowledge document."""
    id: str
    title: str
    content: str
    source_type: str
    category: str
    truth_level: str = "L3"
    verification_status: str = "unverified"
    source_path: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "source_type": self.source_type,
            "category": self.category,
            "truth_level": self.truth_level,
            "verification_status": self.verification_status,
            "source_path": self.source_path,
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

    def _parse_document(self, file_path: Path) -> Optional[KnowledgeDocument]:
        """Parse a markdown file into a KnowledgeDocument."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                post = frontmatter.load(f)

            # Get relative path from knowledge root
            rel_path = str(file_path.relative_to(self.knowledge_path))

            # Extract metadata from frontmatter
            metadata = post.metadata

            # Get file stats for dates
            stat = file_path.stat()
            created_at = metadata.get("created_at") or datetime.fromtimestamp(stat.st_ctime).isoformat()
            updated_at = metadata.get("updated_at") or datetime.fromtimestamp(stat.st_mtime).isoformat()

            return KnowledgeDocument(
                id=self._generate_id(rel_path),
                title=metadata.get("title", file_path.stem.replace("-", " ").title()),
                content=post.content,
                source_type=metadata.get("source_type", self._infer_source_type(rel_path)),
                category=metadata.get("category", self._infer_category(rel_path)),
                truth_level=metadata.get("truth_level", "L3"),
                verification_status=metadata.get("verification_status", "unverified"),
                source_path=rel_path,
                created_at=created_at if isinstance(created_at, str) else str(created_at),
                updated_at=updated_at if isinstance(updated_at, str) else str(updated_at),
            )
        except Exception as e:
            logger.error(f"Error parsing document {file_path}: {e}")
            return None

    def _infer_source_type(self, rel_path: str) -> str:
        """Infer source type from path."""
        parts = rel_path.split("/")
        if len(parts) > 0:
            first_dir = parts[0].lower()
            if first_dir in ["diagnostic", "diagnostics"]:
                return "diagnostic"
            elif first_dir in ["faq", "faqs"]:
                return "faq"
            elif first_dir in ["policy", "policies"]:
                return "policy"
            elif first_dir in ["guide", "guides"]:
                return "guide"
            elif first_dir in ["vehicle", "vehicles"]:
                return "vehicle"
        return "general"

    def _infer_category(self, rel_path: str) -> str:
        """Infer category from path or filename."""
        parts = rel_path.split("/")
        if len(parts) > 1:
            # Use second part of path as category
            return parts[0]
        return "general"

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
                "truth_level": doc.truth_level,
                "verification_status": doc.verification_status,
                "created_at": doc.created_at or datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
            }

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
        source_type: Optional[str] = None,
        truth_level: Optional[str] = None,
        search: Optional[str] = None,
    ) -> KnowledgeListResponse:
        """List all knowledge documents with optional filters."""
        documents = []
        categories = set()
        source_types = set()

        # Walk through knowledge directory
        for root, dirs, files in os.walk(self.knowledge_path):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith(".")]

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

                    # Apply filters
                    if category and doc.category != category:
                        continue
                    if source_type and doc.source_type != source_type:
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
        )

    def get_document(self, doc_id: str) -> Optional[KnowledgeDocument]:
        """Get a single document by ID."""
        # Convert ID back to path
        source_path = doc_id.replace(".", "/") + ".md"
        file_path = self.knowledge_path / source_path

        if not file_path.exists():
            # Try searching for the document
            for root, dirs, files in os.walk(self.knowledge_path):
                dirs[:] = [d for d in dirs if not d.startswith(".")]
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
        truth_level: str = "L3",
    ) -> Optional[KnowledgeDocument]:
        """Create a new knowledge document."""
        # Generate filename from title
        filename = re.sub(r"[^\w\s-]", "", title.lower())
        filename = re.sub(r"[-\s]+", "-", filename).strip("-")
        filename = f"{filename}.md"

        # Determine directory based on source_type
        dir_map = {
            "diagnostic": "diagnostic",
            "faq": "faq",
            "policy": "policies",
            "guide": "guides",
            "vehicle": "vehicle",
        }
        directory = dir_map.get(source_type, source_type)

        source_path = f"{directory}/{filename}"

        # Check if file already exists
        file_path = self.knowledge_path / source_path
        if file_path.exists():
            # Add unique suffix
            base = filename[:-3]  # Remove .md
            source_path = f"{directory}/{base}-{uuid.uuid4().hex[:6]}.md"

        doc = KnowledgeDocument(
            id=self._generate_id(source_path),
            title=title,
            content=content,
            source_type=source_type,
            category=category,
            truth_level=truth_level,
            verification_status="unverified",
            source_path=source_path,
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
        truth_level: Optional[str] = None,
        verification_status: Optional[str] = None,
    ) -> Optional[KnowledgeDocument]:
        """Update an existing document."""
        doc = self.get_document(doc_id)
        if not doc:
            return None

        # Update fields if provided
        if title is not None:
            doc.title = title
        if content is not None:
            doc.content = content
        if source_type is not None:
            doc.source_type = source_type
        if category is not None:
            doc.category = category
        if truth_level is not None:
            doc.truth_level = truth_level
        if verification_status is not None:
            doc.verification_status = verification_status

        doc.updated_at = datetime.now().isoformat()

        if self._save_document(doc):
            return doc
        return None

    def delete_document(self, doc_id: str) -> bool:
        """Delete a document."""
        doc = self.get_document(doc_id)
        if not doc:
            return False

        file_path = self.knowledge_path / doc.source_path
        try:
            if file_path.exists():
                file_path.unlink()
                return True
        except Exception as e:
            logger.error(f"Error deleting document {doc_id}: {e}")

        return False

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
