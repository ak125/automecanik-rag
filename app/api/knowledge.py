"""Knowledge CRUD API endpoints for RAG Admin.

SECURITY:
- Build Plane (DEV/CI): Full CRUD access
- Runtime Plane (PROD): Read-only access (GET only)
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Optional
import logging
import subprocess

from app.services.knowledge_service import get_knowledge_service, KnowledgeDocument
from app.config import get_settings

logger = logging.getLogger(__name__)
router = APIRouter()


def require_build_plane():
    """
    Guard function to block write operations in Runtime Plane (PROD).

    Raises:
        HTTPException 403 if in production environment
    """
    settings = get_settings()
    if not settings.can_write():
        logger.warning(
            f"Write operation blocked in {settings.env} environment. "
            f"Runtime Plane is read-only."
        )
        raise HTTPException(
            status_code=403,
            detail=(
                f"Write operations are disabled in {settings.env} environment. "
                f"Knowledge corpus can only be modified in Build Plane (dev/ci). "
                f"Use GitHub Actions or CI/CD pipeline to update the corpus."
            )
        )


# Request/Response models
class DocumentCreate(BaseModel):
    """Request body for creating a document."""
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    source_type: str = Field(..., pattern="^(diagnostic|faq|policy|guide|vehicle|general)$")
    category: str = Field(..., min_length=1, max_length=100)
    truth_level: str = Field("L3", pattern="^(L1|L2|L3|L4)$")


class DocumentUpdate(BaseModel):
    """Request body for updating a document."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=1)
    source_type: Optional[str] = Field(None, pattern="^(diagnostic|faq|policy|guide|vehicle|general)$")
    category: Optional[str] = Field(None, min_length=1, max_length=100)
    truth_level: Optional[str] = Field(None, pattern="^(L1|L2|L3|L4)$")
    verification_status: Optional[str] = Field(None, pattern="^(verified|unverified|disputed)$")


class DocumentResponse(BaseModel):
    """Single document response."""
    id: str
    title: str
    content: str
    source_type: str
    category: str
    truth_level: str
    verification_status: str
    source_path: str
    created_at: Optional[str]
    updated_at: Optional[str]


class DocumentListResponse(BaseModel):
    """List of documents response."""
    documents: list[DocumentResponse]
    total: int
    page: int
    limit: int
    categories: list[str]
    source_types: list[str]


class ReindexResponse(BaseModel):
    """Reindex operation response."""
    success: bool
    message: str
    indexed_count: Optional[int] = None


class StatsResponse(BaseModel):
    """Knowledge corpus statistics."""
    total_documents: int
    by_source_type: dict[str, int]
    by_truth_level: dict[str, int]
    by_category: dict[str, int]


def doc_to_response(doc: KnowledgeDocument) -> DocumentResponse:
    """Convert KnowledgeDocument to response model."""
    return DocumentResponse(
        id=doc.id,
        title=doc.title,
        content=doc.content,
        source_type=doc.source_type,
        category=doc.category,
        truth_level=doc.truth_level,
        verification_status=doc.verification_status,
        source_path=doc.source_path,
        created_at=doc.created_at,
        updated_at=doc.updated_at,
    )


@router.get("", response_model=DocumentListResponse)
async def list_documents(
    page: int = 1,
    limit: int = 20,
    category: Optional[str] = None,
    source_type: Optional[str] = None,
    truth_level: Optional[str] = None,
    search: Optional[str] = None,
):
    """
    List all knowledge documents with optional filters.

    Query parameters:
    - page: Page number (default: 1)
    - limit: Items per page (default: 20, max: 100)
    - category: Filter by category
    - source_type: Filter by source type (diagnostic, faq, policy, guide, vehicle)
    - truth_level: Filter by truth level (L1, L2, L3, L4)
    - search: Search in title and content
    """
    if limit > 100:
        limit = 100

    service = get_knowledge_service()
    result = service.list_documents(
        page=page,
        limit=limit,
        category=category,
        source_type=source_type,
        truth_level=truth_level,
        search=search,
    )

    return DocumentListResponse(
        documents=[doc_to_response(doc) for doc in result.documents],
        total=result.total,
        page=result.page,
        limit=result.limit,
        categories=result.categories,
        source_types=result.source_types,
    )


@router.get("/stats", response_model=StatsResponse)
async def get_stats():
    """Get statistics about the knowledge corpus."""
    service = get_knowledge_service()
    result = service.list_documents(page=1, limit=1000)  # Get all for stats

    by_source_type: dict[str, int] = {}
    by_truth_level: dict[str, int] = {}
    by_category: dict[str, int] = {}

    # Count from all documents (need to get full list)
    all_docs = service.list_documents(page=1, limit=10000)

    for doc in all_docs.documents:
        by_source_type[doc.source_type] = by_source_type.get(doc.source_type, 0) + 1
        by_truth_level[doc.truth_level] = by_truth_level.get(doc.truth_level, 0) + 1
        by_category[doc.category] = by_category.get(doc.category, 0) + 1

    return StatsResponse(
        total_documents=all_docs.total,
        by_source_type=by_source_type,
        by_truth_level=by_truth_level,
        by_category=by_category,
    )


@router.get("/{doc_id}", response_model=DocumentResponse)
async def get_document(doc_id: str):
    """Get a single document by ID."""
    service = get_knowledge_service()
    doc = service.get_document(doc_id)

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    return doc_to_response(doc)


@router.post("", response_model=DocumentResponse, status_code=201)
async def create_document(body: DocumentCreate):
    """Create a new knowledge document. BUILD PLANE ONLY."""
    require_build_plane()
    service = get_knowledge_service()
    doc = service.create_document(
        title=body.title,
        content=body.content,
        source_type=body.source_type,
        category=body.category,
        truth_level=body.truth_level,
    )

    if not doc:
        raise HTTPException(status_code=500, detail="Failed to create document")

    logger.info(f"Created document: {doc.id}")
    return doc_to_response(doc)


@router.put("/{doc_id}", response_model=DocumentResponse)
async def update_document(doc_id: str, body: DocumentUpdate):
    """Update an existing document. BUILD PLANE ONLY."""
    require_build_plane()
    service = get_knowledge_service()
    doc = service.update_document(
        doc_id=doc_id,
        title=body.title,
        content=body.content,
        source_type=body.source_type,
        category=body.category,
        truth_level=body.truth_level,
        verification_status=body.verification_status,
    )

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    logger.info(f"Updated document: {doc_id}")
    return doc_to_response(doc)


@router.delete("/{doc_id}")
async def delete_document(doc_id: str):
    """Delete a document. BUILD PLANE ONLY."""
    require_build_plane()
    service = get_knowledge_service()
    success = service.delete_document(doc_id)

    if not success:
        raise HTTPException(status_code=404, detail="Document not found or could not be deleted")

    logger.info(f"Deleted document: {doc_id}")
    return {"success": True, "message": f"Document {doc_id} deleted"}


@router.post("/{doc_id}/promote", response_model=DocumentResponse)
async def promote_document(doc_id: str):
    """
    Promote a document to the next truth level. BUILD PLANE ONLY.

    Promotion order: L4 -> L3 -> L2 -> L1
    Documents at L1 or L2 are automatically marked as verified.
    """
    require_build_plane()
    service = get_knowledge_service()
    doc = service.promote_document(doc_id)

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    logger.info(f"Promoted document {doc_id} to {doc.truth_level}")
    return doc_to_response(doc)


def run_reindex():
    """Run the reindex script in background."""
    try:
        settings = get_settings()
        # Run the build_index.py script
        result = subprocess.run(
            ["python", "scripts/build_index.py"],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout
        )
        logger.info(f"Reindex completed: {result.stdout}")
        if result.returncode != 0:
            logger.error(f"Reindex error: {result.stderr}")
    except Exception as e:
        logger.error(f"Reindex failed: {e}")


@router.post("/reindex", response_model=ReindexResponse)
async def reindex_documents(background_tasks: BackgroundTasks):
    """
    Trigger a reindex of all documents into Weaviate. BUILD PLANE ONLY.

    This operation runs in the background and indexes all markdown files
    from the knowledge corpus into the Weaviate vector database.
    """
    require_build_plane()
    # Add reindex task to background
    background_tasks.add_task(run_reindex)

    return ReindexResponse(
        success=True,
        message="Reindex started in background. Check logs for progress.",
    )
