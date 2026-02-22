#!/usr/bin/env python3
"""Ingest local PDF files into knowledge corpus with chunking + Weaviate indexing.

Full pipeline: extract → chunk (H2/H3-aware) → embed → index to Weaviate.

Usage:
  ENV=dev python scripts/ingest_pdfs.py --input /path/to/pdfs
  ENV=dev python scripts/ingest_pdfs.py --input /path/to/pdfs --truth-level L2
  ENV=dev python scripts/ingest_pdfs.py --input /path/to/pdfs --dry-run
  ENV=dev python scripts/ingest_pdfs.py --input /path/to/pdfs --no-index
"""

import argparse
import hashlib
import json
import logging
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader

# Add repo root for imports when executed from scripts/
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import get_settings  # noqa: E402
from app.services.knowledge_service import get_knowledge_service  # noqa: E402


logger = logging.getLogger(__name__)

# Regex to find page markers inserted during extraction
_PAGE_MARKER_RE = re.compile(r"\[\[PDF_PAGE:(\d+)\]\]")


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s - %(levelname)s - %(message)s")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def ocr_tools_available() -> bool:
    return shutil.which("pdftoppm") is not None and shutil.which("tesseract") is not None


def ocr_page(pdf_path: Path, page_number: int) -> str:
    """
    OCR a single PDF page using pdftoppm + tesseract.
    page_number is 1-based.
    """
    with tempfile.TemporaryDirectory(prefix="ingest-ocr-") as tmp_dir:
        tmp = Path(tmp_dir)
        out_prefix = tmp / "page"
        img_path = tmp / "page.png"
        try:
            subprocess.run(
                [
                    "pdftoppm",
                    "-f", str(page_number),
                    "-l", str(page_number),
                    "-singlefile",
                    "-r", "300",
                    "-png",
                    str(pdf_path),
                    str(out_prefix),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=45,
            )
            if not img_path.exists():
                return ""
            proc = subprocess.run(
                ["tesseract", str(img_path), "stdout", "-l", "fra+eng"],
                check=False,
                capture_output=True,
                text=True,
                timeout=60,
            )
            if proc.returncode != 0:
                return ""
            return (proc.stdout or "").strip()
        except Exception:
            return ""


def extract_pdf_text(pdf_path: Path, enable_ocr: bool = True) -> tuple[str, dict]:
    """Extract plain text from a PDF file with page anchors for downstream chunk source_uri."""
    reader = PdfReader(str(pdf_path))
    pages = []
    stats = {"pages_total": len(reader.pages), "pages_text": 0, "pages_ocr": 0}
    can_ocr = enable_ocr and ocr_tools_available()
    for index, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        if not text and can_ocr:
            text = ocr_page(pdf_path, index)
            if text:
                stats["pages_ocr"] += 1
        if not text:
            continue
        stats["pages_text"] += 1
        pages.append(f"[[PDF_PAGE:{index}]]\n{text}")
    return "\n\n".join(pages).strip(), stats


def archive_raw_pdf(pdf_path: Path, rel_name: Path, knowledge_root: Path) -> tuple[Path, str]:
    """
    Store immutable raw PDF copy under knowledge root.
    Path format: _raw/pdf/<sha256>.pdf
    """
    digest = sha256_file(pdf_path)
    raw_dir = knowledge_root / "_raw" / "pdf"
    raw_dir.mkdir(parents=True, exist_ok=True)

    raw_pdf = raw_dir / f"{digest}.pdf"
    if not raw_pdf.exists():
        shutil.copy2(pdf_path, raw_pdf)

    sidecar = raw_dir / f"{digest}.json"
    if not sidecar.exists():
        metadata = {
            "sha256": digest,
            "original_name": rel_name.as_posix(),
            "ingested_at": datetime.now(timezone.utc).isoformat(),
            "size_bytes": pdf_path.stat().st_size,
        }
        sidecar.write_text(json.dumps(metadata, ensure_ascii=True, indent=2), encoding="utf-8")

    return raw_pdf, digest


def _detect_page_for_chunk(chunk_content: str) -> int | None:
    """Find the last [[PDF_PAGE:N]] marker within a chunk to identify its page."""
    matches = list(_PAGE_MARKER_RE.finditer(chunk_content))
    if matches:
        return int(matches[-1].group(1))
    return None


def _make_chunk_id(source_uri: str, chunk_index: int, content: str) -> str:
    """Deterministic UUID v5 chunk ID for idempotent upserts."""
    content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
    name = f"{source_uri}:{chunk_index}:{content_hash}"
    return str(uuid.uuid5(uuid.NAMESPACE_URL, name))


def chunk_and_index(
    content: str,
    title: str,
    source_uri: str,
    truth_level: str,
    source_type: str,
    category: str,
    raw_sha: str,
    chunk_size: int = 500,
    chunk_overlap: int = 50,
    dry_run: bool = False,
) -> dict:
    """Chunk PDF content, embed, and index to Weaviate.

    Returns:
        dict with keys: chunks_total, chunks_indexed, collection
    """
    from orchestrator.processors.chunker import TokenAwareChunker
    from app.services.embeddings import get_embeddings_service
    from app.services.weaviate_client import get_weaviate_client

    chunker = TokenAwareChunker(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        min_chunk_size=50,
        respect_headings=True,
    )
    raw_chunks = chunker.chunk(content)

    if not raw_chunks:
        logger.warning(f"No chunks produced for {source_uri}")
        return {"chunks_total": 0, "chunks_indexed": 0, "collection": ""}

    if dry_run:
        for i, c in enumerate(raw_chunks):
            heading = c.get("heading") or "(none)"
            page = _detect_page_for_chunk(c["content"])
            logger.info(
                f"  [DRY-RUN] chunk {i}: {c['token_estimate']} tokens, "
                f"heading={heading}, page={page}"
            )
        return {"chunks_total": len(raw_chunks), "chunks_indexed": 0, "collection": ""}

    # Embed all chunks
    embeddings_service = get_embeddings_service()
    texts = [c["content"] for c in raw_chunks]
    vectors = embeddings_service.embed_batch(texts, batch_size=32)

    # Determine target collection
    weaviate_client = get_weaviate_client()
    target_collection = weaviate_client.resolve_collection(
        namespace=f"knowledge:{source_type}"
    )

    # Build chunk objects for Weaviate
    from orchestrator.pipeline import (
        classify_domain, classify_intent, extract_entities,
        compute_doc_weight, compute_evidence_grade, infer_doc_family,
    )

    now_iso = datetime.now(timezone.utc).isoformat()
    is_canonical = truth_level in ("L1", "L2")
    doc_family_val = infer_doc_family(source_type, f"knowledge:{source_type}")

    objects_to_index = []
    for i, raw_chunk in enumerate(raw_chunks):
        page = _detect_page_for_chunk(raw_chunk["content"])
        chunk_source_uri = f"{source_uri}#page={page}" if page else source_uri
        chunk_id = _make_chunk_id(source_uri, i, raw_chunk["content"])
        content_hash = hashlib.sha256(raw_chunk["content"].encode()).hexdigest()[:32]

        chunk_content = raw_chunk["content"]
        domain = classify_domain(chunk_content)
        intent = classify_intent(chunk_content)
        entities = extract_entities(chunk_content)
        doc_weight = compute_doc_weight(truth_level, is_canonical)
        heading = raw_chunk.get("heading")
        evidence_grade = compute_evidence_grade(
            content=chunk_content, truth_level=truth_level,
            domain=domain, entities=entities, heading=heading,
        )

        anchors = [f"page:{page}"] if page else []
        if heading:
            anchors.append(f"heading:{heading}")

        props = {
            "chunk_id": chunk_id,
            "parent_id": raw_sha,
            "source_path": source_uri,
            "source_uri": chunk_source_uri,
            "source_ref": f"sha256:{raw_sha}",
            "title": title,
            "content": chunk_content,
            "anchors": anchors,
            "intent": intent,
            "domain": domain,
            "entities": entities,
            "truth_level": truth_level,
            "verification_status": "unverified",
            "doc_weight": doc_weight,
            "evidence_grade": evidence_grade,
            "is_canonical": is_canonical,
            "canonical_weight": doc_weight if is_canonical else 0.0,
            "chunk_index": i,
            "created_at": now_iso,
            "updated_at": now_iso,
            "content_hash": content_hash,
            "source_type": source_type,
            "doc_family": doc_family_val,
            "namespace": f"knowledge:{source_type}",
            "category": category,
            "language": "fr",
            "confidence_score": {"A": 0.92, "B": 0.75, "C": 0.55, "D": 0.35}.get(evidence_grade, 0.5),
            "last_verified_date": "",
            "verified_by": "",
        }
        objects_to_index.append((props, vectors[i]))

    # Batch upsert to Weaviate
    collection = weaviate_client.client.collections.get(target_collection)
    indexed = 0
    with collection.batch.dynamic() as batch:
        for props, vector in objects_to_index:
            batch.add_object(properties=props, vector=vector)
            indexed += 1

    logger.info(
        f"Indexed {indexed}/{len(raw_chunks)} chunks to {target_collection} "
        f"for {source_uri}"
    )
    return {"chunks_total": len(raw_chunks), "chunks_indexed": indexed, "collection": target_collection}


def run(args: argparse.Namespace) -> int:
    settings = get_settings()
    if not settings.can_write() and not args.dry_run:
        logger.error("Write operations are blocked in this environment (set ENV=dev/ci/staging).")
        return 1

    input_dir = Path(args.input).resolve()
    if not input_dir.exists() or not input_dir.is_dir():
        logger.error(f"Input directory not found: {input_dir}")
        return 1

    pdf_files = sorted(input_dir.rglob("*.pdf"))
    if not pdf_files:
        logger.warning(f"No PDF files found under: {input_dir}")
        return 0

    service = get_knowledge_service()
    created = 0
    failed = 0
    total_chunks = 0
    total_indexed = 0
    index_enabled = not args.no_index

    logger.info(f"Found {len(pdf_files)} PDF file(s) (index={index_enabled})")
    for pdf_path in pdf_files:
        rel_name = pdf_path.relative_to(input_dir)
        title = pdf_path.stem.replace("-", " ").replace("_", " ").strip() or "untitled"

        try:
            raw_pdf, raw_sha = archive_raw_pdf(pdf_path, rel_name, Path(service.knowledge_path))
            content, stats = extract_pdf_text(pdf_path, enable_ocr=True)
            if not content:
                logger.warning(f"Skip empty text extraction: {rel_name}")
                continue

            source_uri = f"pdf://{rel_name.as_posix()}"

            # Infer source_type and category from content
            src = service._infer_source_type_from_content(content)  # noqa: SLF001
            cat = service._infer_category_from_content(src, content)  # noqa: SLF001

            if args.dry_run:
                logger.info(
                    f"[DRY-RUN] FILE_WOULD_CREATE pdf_name={rel_name} "
                    f"source_type={src} category={cat} "
                    f"pages={stats['pages_text']}+{stats['pages_ocr']}ocr"
                )
                if index_enabled:
                    chunk_and_index(
                        content=content, title=title, source_uri=source_uri,
                        truth_level=args.truth_level, source_type=src, category=cat,
                        raw_sha=raw_sha, dry_run=True,
                    )
                continue

            # Step 1: Save to knowledge/ (markdown file)
            doc = service.create_document(
                title=title,
                content=content,
                source_type="auto",
                category="auto",
                truth_level=args.truth_level,
                source_uri=source_uri,
            )
            if not doc:
                failed += 1
                logger.error(f"Failed to create document for {rel_name}")
                continue

            created += 1
            logger.info(
                f"FILE_CREATED path={doc.source_path} "
                f"source=pdf pdf_name={rel_name} "
                f"source_type={doc.source_type} truth_level={args.truth_level}"
            )

            # Step 2: Chunk + embed + index to Weaviate
            if index_enabled:
                result = chunk_and_index(
                    content=content,
                    title=title,
                    source_uri=source_uri,
                    truth_level=args.truth_level,
                    source_type=doc.source_type,
                    category=doc.category,
                    raw_sha=raw_sha,
                )
                total_chunks += result["chunks_total"]
                total_indexed += result["chunks_indexed"]

            logger.info(
                f"Ingested {rel_name} -> {doc.source_path} "
                f"(source_type={doc.source_type}, category={doc.category}, "
                f"raw_sha256={raw_sha}, pages_text={stats['pages_text']}, pages_ocr={stats['pages_ocr']})"
            )
        except Exception as exc:  # noqa: BLE001
            failed += 1
            logger.error(f"Failed to ingest {rel_name}: {exc}")

    summary = f"Done. docs={created}, failed={failed}, total={len(pdf_files)}"
    if index_enabled:
        summary += f", chunks={total_chunks}, indexed={total_indexed}"
    logger.info(summary)
    return 0 if failed == 0 else 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest PDF files into RAG knowledge corpus")
    parser.add_argument("--input", required=True, help="Directory containing PDF files")
    parser.add_argument(
        "--truth-level",
        default="L3",
        choices=["L1", "L2", "L3", "L4"],
        help="Truth level metadata for created docs",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview classification and chunking only")
    parser.add_argument("--no-index", action="store_true", help="Save to knowledge/ only, skip Weaviate indexing")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logs")
    args = parser.parse_args()

    setup_logging(args.verbose)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
