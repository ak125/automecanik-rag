"""RAG Admin Interface - NO LOGIN (auth via monorepo staff level 5)."""

from fastapi import APIRouter, Request, HTTPException, Form, Query, UploadFile, File, Header, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
import csv
import json
import io
import gc
import uuid
from fastapi.templating import Jinja2Templates
from pathlib import Path
from typing import Optional, List
import logging
import yaml
from pydantic import BaseModel

from app.config import get_settings
from app.services.knowledge_service import get_knowledge_service
from app.services.embeddings import get_embeddings_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/admin", tags=["Admin"])
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


# ============================================
# API Models for BullMQ Worker Integration
# ============================================
class IndexBatchRequest(BaseModel):
    """Request body for index-batch endpoint."""
    files: List[str]  # Relative paths to index
    clear: bool = False  # Clear collection before indexing (only first batch)


class IndexBatchResponse(BaseModel):
    """Response from index-batch endpoint."""
    indexed: int
    errors: List[str]
    duration_ms: int


class ListFilesResponse(BaseModel):
    """Response from list-files endpoint."""
    files: List[str]
    count: int


# ============================================
# API Key Verification for Worker Endpoints
# ============================================
async def verify_api_key(x_rag_api_key: str = Header(None, alias="X-RAG-API-Key")):
    """Verify API key from X-RAG-API-Key header."""
    settings = get_settings()

    # If no API key configured, allow (dev mode)
    if not settings.rag_api_key:
        logger.warning("RAG_API_KEY not configured - allowing unauthenticated access")
        return True

    if x_rag_api_key != settings.rag_api_key:
        raise HTTPException(status_code=401, detail="Invalid or missing X-RAG-API-Key")

    return True


# ============================================
# Constants for TRUE Streaming Indexation
# ============================================
CHUNK_SIZE = 2000
CHUNK_OVERLAP = 200
BATCH_SIZE = 10
FASTEMBED_MODEL = "BAAI/bge-small-en-v1.5"


def get_context(request: Request) -> dict:
    """Base context for templates."""
    settings = get_settings()
    return {"request": request, "env": settings.env, "debug": settings.debug}


# ============================================
# Dashboard
# ============================================
@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Admin dashboard with stats."""
    service = get_knowledge_service()
    result = service.list_documents(page=1, limit=10000)

    by_truth_level = {"L1": 0, "L2": 0, "L3": 0, "L4": 0}
    by_source_type = {}

    for doc in result.documents:
        by_truth_level[doc.truth_level] = by_truth_level.get(doc.truth_level, 0) + 1
        by_source_type[doc.source_type] = by_source_type.get(doc.source_type, 0) + 1

    context = get_context(request)
    context.update({
        "total": result.total,
        "by_truth_level": by_truth_level,
        "by_source_type": by_source_type,
        "recent_documents": result.documents[:5],
    })
    return templates.TemplateResponse("pages/dashboard.html", context)


# ============================================
# Documents
# ============================================
@router.get("/documents", response_class=HTMLResponse)
async def documents_list(
    request: Request,
    page: int = Query(1, ge=1),
    search: Optional[str] = None,
    truth_level: Optional[str] = None,
    source_type: Optional[str] = None,
):
    """List documents with filters."""
    service = get_knowledge_service()
    result = service.list_documents(
        page=page, limit=20, search=search,
        truth_level=truth_level, source_type=source_type
    )

    context = get_context(request)
    context.update({
        "documents": result.documents,
        "total": result.total,
        "page": page,
        "pages": (result.total + 19) // 20,
        "source_types": result.source_types,
        "filters": {
            "search": search or "",
            "truth_level": truth_level or "",
            "source_type": source_type or ""
        }
    })

    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("partials/_documents_table.html", context)
    return templates.TemplateResponse("pages/documents/list.html", context)


@router.get("/documents/new", response_class=HTMLResponse)
async def document_create_form(request: Request):
    """Create document form."""
    context = get_context(request)
    context["source_types"] = ["diagnostic", "faq", "policy", "guide", "vehicle", "general"]
    return templates.TemplateResponse("pages/documents/create.html", context)


@router.post("/documents/new")
async def document_create_submit(
    title: str = Form(...),
    content: str = Form(...),
    source_type: str = Form(...),
    category: str = Form(...),
    truth_level: str = Form("L3"),
):
    """Create document."""
    service = get_knowledge_service()
    doc = service.create_document(
        title=title, content=content, source_type=source_type,
        category=category, truth_level=truth_level
    )
    if not doc:
        raise HTTPException(status_code=500, detail="Failed to create document")
    return RedirectResponse(url=f"/admin/documents/{doc.id}", status_code=303)


@router.get("/documents/{doc_id}", response_class=HTMLResponse)
async def document_detail(request: Request, doc_id: str):
    """View document."""
    service = get_knowledge_service()
    doc = service.get_document(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    context = get_context(request)
    context["document"] = doc
    return templates.TemplateResponse("pages/documents/detail.html", context)


@router.get("/documents/{doc_id}/edit", response_class=HTMLResponse)
async def document_edit_form(request: Request, doc_id: str):
    """Edit document form."""
    service = get_knowledge_service()
    doc = service.get_document(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    context = get_context(request)
    context["document"] = doc
    context["source_types"] = ["diagnostic", "faq", "policy", "guide", "vehicle", "general"]
    return templates.TemplateResponse("pages/documents/edit.html", context)


@router.post("/documents/{doc_id}/edit")
async def document_edit_submit(
    doc_id: str,
    title: str = Form(...),
    content: str = Form(...),
    source_type: str = Form(...),
    category: str = Form(...),
    truth_level: str = Form(...),
):
    """Update document."""
    service = get_knowledge_service()
    doc = service.update_document(
        doc_id=doc_id, title=title, content=content,
        source_type=source_type, category=category, truth_level=truth_level
    )
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return RedirectResponse(url=f"/admin/documents/{doc_id}", status_code=303)


@router.post("/documents/{doc_id}/delete")
async def document_delete(request: Request, doc_id: str):
    """Delete document."""
    service = get_knowledge_service()
    success = service.delete_document(doc_id)
    if not success:
        raise HTTPException(status_code=404, detail="Document not found")

    if request.headers.get("HX-Request"):
        response = HTMLResponse(content="")
        response.headers["HX-Redirect"] = "/admin/documents"
        return response
    return RedirectResponse(url="/admin/documents", status_code=303)


@router.post("/documents/{doc_id}/promote")
async def document_promote(request: Request, doc_id: str):
    """Promote document truth level (L4->L3->L2->L1)."""
    service = get_knowledge_service()
    doc = service.promote_document(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    if request.headers.get("HX-Request"):
        context = get_context(request)
        context["level"] = doc.truth_level
        return templates.TemplateResponse("components/_truth_badge.html", context)
    return RedirectResponse(url=f"/admin/documents/{doc_id}", status_code=303)


# ============================================
# Chat & Search Testing
# ============================================
@router.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    """Chat testing page."""
    return templates.TemplateResponse("pages/chat.html", get_context(request))


@router.get("/search", response_class=HTMLResponse)
async def search_page(request: Request):
    """Search testing page."""
    return templates.TemplateResponse("pages/search.html", get_context(request))


# ============================================
# Settings
# ============================================
@router.get("/settings", response_class=HTMLResponse)
async def settings_page(request: Request):
    """Settings page."""
    settings = get_settings()
    context = get_context(request)
    context.update({
        "weaviate_url": settings.weaviate_url,
        "redis_url": settings.redis_url,
        "can_write": settings.can_write(),
        "rate_limit": settings.rate_limit_rpm,
    })
    return templates.TemplateResponse("pages/settings.html", context)


@router.post("/settings/reindex")
async def trigger_reindex(request: Request):
    """Trigger corpus reindex."""
    settings = get_settings()
    if not settings.can_write():
        raise HTTPException(status_code=403, detail="Reindex not allowed in this environment")

    import subprocess
    try:
        subprocess.Popen(["python", "scripts/build_index.py"], cwd="/opt/automecanik/rag")
        msg, ok = "Reindex started in background", True
    except Exception as e:
        msg, ok = f"Failed: {e}", False

    if request.headers.get("HX-Request"):
        css = "bg-green-100 text-green-800" if ok else "bg-red-100 text-red-800"
        return HTMLResponse(f'<div class="p-4 rounded-lg {css}">{msg}</div>')
    return RedirectResponse(url="/admin/settings", status_code=303)


# ============================================
# BullMQ Worker API Endpoints
# ============================================

def _parse_frontmatter(content: str) -> dict:
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


def _chunk_content(content: str, source_path: str, metadata: dict) -> List[dict]:
    """Chunk content into smaller pieces with deterministic UUIDs."""
    chunks = []
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
            f"{source_path}:{chunk_index}"
        ))

        chunks.append({
            "uuid": chunk_uuid,
            "content": chunk_content,
            "title": metadata.get("title", Path(source_path).stem),
            "source_path": source_path,
            "source_type": "knowledge",
            "truth_level": metadata.get("truth_level", "L2"),
            "namespace": f"knowledge:{metadata.get('entity_type', 'unknown')}",
            "chunk_index": chunk_index,
        })

        start = end - CHUNK_OVERLAP
        chunk_index += 1

        if start >= len(content):
            break

    return chunks


def _clear_collection(collection_name: str):
    """Clear and recreate Weaviate collection."""
    import weaviate
    from weaviate.classes.config import Configure, Property, DataType

    settings = get_settings()
    host = settings.weaviate_url.replace("http://", "").split(":")[0]
    port = int(settings.weaviate_url.split(":")[-1])

    client = weaviate.connect_to_local(host=host, port=port)

    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)
        logger.info(f"Deleted collection {collection_name}")

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


@router.get("/list-files", response_model=ListFilesResponse)
async def list_files(_: bool = Depends(verify_api_key)):
    """
    List all markdown files available for indexation.

    Used by BullMQ worker to discover files and create batch jobs.
    """
    settings = get_settings()
    knowledge_path = Path(settings.knowledge_path)
    files = []

    if not knowledge_path.exists():
        logger.warning(f"Knowledge path not found: {knowledge_path}")
        return ListFilesResponse(files=[], count=0)

    for md_file in knowledge_path.rglob("*.md"):
        # Skip README and backup files
        if md_file.name == "README.md":
            continue
        if ".backup" in str(md_file):
            continue

        relative_path = str(md_file.relative_to(knowledge_path))
        files.append(relative_path)

    files.sort()  # Consistent ordering
    logger.info(f"Found {len(files)} markdown files for indexation")

    return ListFilesResponse(files=files, count=len(files))


@router.post("/index-batch", response_model=IndexBatchResponse)
async def index_batch(
    request: IndexBatchRequest,
    _: bool = Depends(verify_api_key)
):
    """
    Index a batch of files using TRUE STREAMING.

    Called by BullMQ worker with batches of ~50 files.
    Each file is processed one at a time:
    1. Read file
    2. Chunk content
    3. Embed with FastEmbed (Rust backend)
    4. Upsert to Weaviate
    5. Free memory
    """
    import time
    start_time = time.time()

    settings = get_settings()

    # Verify write permission (BUILD plane only)
    if not settings.can_write():
        raise HTTPException(
            status_code=403,
            detail=f"Write operations blocked in {settings.env} environment"
        )

    knowledge_path = Path(settings.knowledge_path)
    collection_name = "Prod_Chatbot"
    indexed = 0
    errors = []

    # Clear collection if requested (only for first batch)
    if request.clear:
        try:
            _clear_collection(collection_name)
            logger.info("Collection cleared before indexing")
        except Exception as e:
            error_msg = f"Failed to clear collection: {str(e)}"
            logger.error(error_msg)
            errors.append(error_msg)

    # Use existing embeddings service (singleton - no new model loading)
    try:
        embeddings_service = get_embeddings_service()
        logger.info("Using existing embeddings service (singleton)")
    except Exception as e:
        error_msg = f"Failed to get embeddings service: {str(e)}"
        logger.error(error_msg)
        return IndexBatchResponse(
            indexed=0,
            errors=[error_msg],
            duration_ms=int((time.time() - start_time) * 1000)
        )

    # Connect to Weaviate
    try:
        import weaviate
        host = settings.weaviate_url.replace("http://", "").split(":")[0]
        port = int(settings.weaviate_url.split(":")[-1])
        client = weaviate.connect_to_local(host=host, port=port)
        collection = client.collections.get(collection_name)
        logger.info(f"Connected to Weaviate: {collection_name}")
    except Exception as e:
        error_msg = f"Failed to connect to Weaviate: {str(e)}"
        logger.error(error_msg)
        return IndexBatchResponse(
            indexed=0,
            errors=[error_msg],
            duration_ms=int((time.time() - start_time) * 1000)
        )

    # TRUE STREAMING: Process one file at a time
    for file_path in request.files:
        full_path = knowledge_path / file_path

        try:
            if not full_path.exists():
                errors.append(f"{file_path}: File not found")
                continue

            # 1. Read file
            content = full_path.read_text(encoding="utf-8")
            metadata = _parse_frontmatter(content)

            # 2. Chunk content
            chunks = _chunk_content(content, file_path, metadata)

            if not chunks:
                continue

            # 3. Embed + Upsert in small batches
            for i in range(0, len(chunks), BATCH_SIZE):
                batch_chunks = chunks[i:i + BATCH_SIZE]
                texts = [c["content"] for c in batch_chunks]

                # Generate embeddings using singleton service
                embeddings = embeddings_service.embed_batch(texts, batch_size=BATCH_SIZE)

                # Upsert to Weaviate
                with collection.batch.dynamic() as batch_obj:
                    for chunk, embedding in zip(batch_chunks, embeddings):
                        batch_obj.add_object(
                            properties={k: v for k, v in chunk.items() if k != "uuid"},
                            vector=embedding,  # Already a list from embed_batch
                            uuid=chunk["uuid"],
                        )
                        indexed += 1

                # Free embeddings memory
                del embeddings

            # 4. Free file memory
            del content, chunks
            gc.collect()

            logger.debug(f"Indexed: {file_path}")

        except Exception as e:
            error_msg = f"{file_path}: {str(e)}"
            logger.error(error_msg)
            errors.append(error_msg)

    # Cleanup
    try:
        client.close()
    except Exception:
        pass

    duration_ms = int((time.time() - start_time) * 1000)
    logger.info(f"Batch complete: {indexed} chunks indexed, {len(errors)} errors, {duration_ms}ms")

    return IndexBatchResponse(
        indexed=indexed,
        errors=errors,
        duration_ms=duration_ms
    )
