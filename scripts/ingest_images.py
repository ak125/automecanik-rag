#!/usr/bin/env python3
"""Ingest local image files into knowledge corpus with OCR + caption docs.

Supports optional vision model (Claude Haiku) for semantic captions.
Fallback to deterministic captions if no ANTHROPIC_API_KEY or --no-vision.

Usage:
  ENV=dev python scripts/ingest_images.py --input /path/to/images
  ENV=dev python scripts/ingest_images.py --input /path/to/images --no-vision
  ENV=dev python scripts/ingest_images.py --input /path/to/images --truth-level L2
  ENV=dev python scripts/ingest_images.py --input /path/to/images --dry-run
"""

import argparse
import base64
import hashlib
import json
import logging
import os
import shutil
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

# Add repo root for imports when executed from scripts/
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import get_settings  # noqa: E402
from app.services.knowledge_service import get_knowledge_service  # noqa: E402


logger = logging.getLogger(__name__)
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s - %(levelname)s - %(message)s")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def archive_raw_image(image_path: Path, rel_name: Path, knowledge_root: Path) -> tuple[Path, str]:
    """Store immutable raw image under knowledge/_raw/images/<sha256>.<ext>."""
    digest = sha256_file(image_path)
    raw_dir = knowledge_root / "_raw" / "images"
    raw_dir.mkdir(parents=True, exist_ok=True)

    ext = image_path.suffix.lower() or ".bin"
    raw_image = raw_dir / f"{digest}{ext}"
    if not raw_image.exists():
        shutil.copy2(image_path, raw_image)

    sidecar = raw_dir / f"{digest}.json"
    if not sidecar.exists():
        metadata = {
            "sha256": digest,
            "original_name": rel_name.as_posix(),
            "ingested_at": datetime.now(timezone.utc).isoformat(),
            "size_bytes": image_path.stat().st_size,
            "mime_hint": f"image/{ext.lstrip('.')}",
        }
        sidecar.write_text(json.dumps(metadata, ensure_ascii=True, indent=2), encoding="utf-8")

    return raw_image, digest


def ocr_tools_available() -> bool:
    return shutil.which("tesseract") is not None


def _as_int(value: str, default: int = 0) -> int:
    try:
        return int(float(value))
    except Exception:
        return default


def extract_ocr_blocks(image_path: Path) -> list[dict]:
    """
    Extract OCR text grouped by block, with optional bounding boxes.
    Returns list like:
      { "text": "...", "bbox": [x1,y1,x2,y2] }
    """
    if not ocr_tools_available():
        return []

    try:
        proc = subprocess.run(
            ["tesseract", str(image_path), "stdout", "-l", "fra+eng", "tsv"],
            check=False,
            capture_output=True,
            text=True,
            timeout=90,
        )
    except Exception:
        return []

    if proc.returncode != 0 or not proc.stdout.strip():
        return []

    lines = proc.stdout.splitlines()
    if not lines:
        return []

    grouped: dict[int, list[tuple[int, int, int, int, int, str]]] = defaultdict(list)
    for row in lines[1:]:
        cols = row.split("\t")
        if len(cols) < 12:
            continue
        level = _as_int(cols[0], 0)
        if level != 5:  # words
            continue
        block_num = _as_int(cols[2], 0)
        line_num = _as_int(cols[4], 0)
        word_num = _as_int(cols[5], 0)
        left = _as_int(cols[6], 0)
        top = _as_int(cols[7], 0)
        width = _as_int(cols[8], 0)
        height = _as_int(cols[9], 0)
        conf = _as_int(cols[10], -1)
        text = (cols[11] or "").strip()
        if not text or conf < 0:
            continue
        grouped[block_num].append((line_num, word_num, left, top, width, height, text))

    blocks: list[dict] = []
    for block_num in sorted(grouped.keys()):
        words = sorted(grouped[block_num], key=lambda x: (x[0], x[1]))
        if not words:
            continue
        text = " ".join(w[6] for w in words).strip()
        if not text:
            continue
        x1 = min(w[2] for w in words)
        y1 = min(w[3] for w in words)
        x2 = max(w[2] + w[4] for w in words)
        y2 = max(w[3] + w[5] for w in words)
        blocks.append({"text": text, "bbox": [x1, y1, x2, y2]})

    return blocks


def build_caption(image_path: Path, ocr_blocks: list[dict]) -> str:
    """Simple deterministic caption fallback when no vision model is configured."""
    name = image_path.stem.replace("-", " ").replace("_", " ").strip() or "image"
    try:
        with Image.open(image_path) as img:
            w, h = img.size
    except Exception:
        w, h = 0, 0

    first_ocr = ""
    if ocr_blocks:
        first_ocr = (ocr_blocks[0].get("text", "") or "")[:180].strip()

    parts = [f"Image technique: {name}"]
    if w > 0 and h > 0:
        parts.append(f"Resolution: {w}x{h}")
    if first_ocr:
        parts.append(f"Texte detecte: {first_ocr}")
    return ". ".join(parts).strip() + "."


def caption_with_vision(image_path: Path, ocr_blocks: list[dict]) -> str | None:
    """Generate semantic caption using Claude Haiku vision (optional).

    Returns None if ANTHROPIC_API_KEY is not set or httpx is not installed.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None

    try:
        import httpx
    except ImportError:
        logger.debug("httpx not installed, skipping vision caption")
        return None

    try:
        with open(image_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode()

        ext = image_path.suffix.lower().lstrip(".")
        media_type = {
            "jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
            "webp": "image/webp", "gif": "image/gif", "bmp": "image/bmp",
            "tif": "image/tiff", "tiff": "image/tiff",
        }.get(ext, "image/png")

        ocr_context = ""
        if ocr_blocks:
            ocr_context = f"\nOCR detecte : {' | '.join(b['text'][:100] for b in ocr_blocks[:5])}"

        resp = httpx.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": 300,
                "messages": [{
                    "role": "user",
                    "content": [
                        {"type": "image", "source": {"type": "base64", "media_type": media_type, "data": img_b64}},
                        {"type": "text", "text": (
                            "Decris cette image technique automobile en francais, en 2-3 phrases. "
                            "Identifie : type de piece, marque visible, annotations, diagramme/schema. "
                            f"Contexte : AutoMecanik (pieces auto).{ocr_context}"
                        )},
                    ],
                }],
            },
            timeout=30,
        )
        if resp.status_code == 200:
            data = resp.json()
            return data["content"][0]["text"].strip()
        logger.warning(f"Vision API returned status {resp.status_code}")
    except Exception as exc:  # noqa: BLE001
        logger.warning(f"Vision caption failed: {exc}")

    return None


def render_ocr_markdown(ocr_blocks: list[dict]) -> str:
    lines = ["## OCR Blocks"]
    if not ocr_blocks:
        lines.append("- Aucun texte detecte.")
        return "\n".join(lines)

    for i, block in enumerate(ocr_blocks, start=1):
        bbox = block.get("bbox") or []
        if len(bbox) == 4:
            bbox_tag = f"[[BBOX:{bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]}]]"
        else:
            bbox_tag = ""
        lines.append(f"### Bloc {i} {bbox_tag}".rstrip())
        lines.append((block.get("text", "") or "").strip())
        lines.append("")
    return "\n".join(lines).strip()


def iter_image_files(input_dir: Path) -> list[Path]:
    files = []
    for p in sorted(input_dir.rglob("*")):
        if p.is_file() and p.suffix.lower() in IMAGE_EXTS:
            files.append(p)
    return files


def run(args: argparse.Namespace) -> int:
    settings = get_settings()
    if not settings.can_write() and not args.dry_run:
        logger.error("Write operations are blocked in this environment (set ENV=dev/ci/staging).")
        return 1

    input_dir = Path(args.input).resolve()
    if not input_dir.exists() or not input_dir.is_dir():
        logger.error(f"Input directory not found: {input_dir}")
        return 1

    image_files = iter_image_files(input_dir)
    if not image_files:
        logger.warning(f"No image files found under: {input_dir}")
        return 0

    service = get_knowledge_service()
    created = 0
    failed = 0
    logger.info(f"Found {len(image_files)} image file(s)")

    for image_path in image_files:
        rel_name = image_path.relative_to(input_dir)
        base_title = image_path.stem.replace("-", " ").replace("_", " ").strip() or "untitled image"

        try:
            ocr_blocks = extract_ocr_blocks(image_path)
            vision_caption = None
            if not args.no_vision:
                vision_caption = caption_with_vision(image_path, ocr_blocks)
            caption = vision_caption or build_caption(image_path, ocr_blocks)
            caption_source = "vision" if vision_caption else "deterministic"
            ocr_md = render_ocr_markdown(ocr_blocks)
            source_uri = f"image://{rel_name.as_posix()}"
            raw_sha = sha256_file(image_path)

            if args.dry_run:
                logger.info(
                    f"[DRY-RUN] {rel_name} -> caption({caption_source})+ocr docs | "
                    f"ocr_blocks={len(ocr_blocks)} | raw_sha256={raw_sha}"
                )
                continue

            raw_image, _ = archive_raw_image(image_path, rel_name, Path(service.knowledge_path))

            caption_doc = service.create_document(
                title=f"{base_title} image caption",
                content=f"## Caption\n\n{caption}\n",
                source_type="media",
                category="media",
                truth_level=args.truth_level,
                source_uri=source_uri,
            )
            if not caption_doc:
                failed += 1
                logger.error(f"Failed to create caption doc for {rel_name}")
                continue
            created += 1

            ocr_doc = service.create_document(
                title=f"{base_title} image ocr",
                content=ocr_md,
                source_type="media",
                category="media",
                truth_level=args.truth_level,
                source_uri=source_uri,
            )
            if ocr_doc:
                created += 1
            else:
                logger.warning(f"OCR doc skipped for {rel_name}")

            logger.info(
                f"Ingested {rel_name} -> caption({caption_source})={caption_doc.source_path} "
                f"ocr_blocks={len(ocr_blocks)} raw_sha256={raw_sha}"
            )
        except Exception as exc:  # noqa: BLE001
            failed += 1
            logger.error(f"Failed to ingest {rel_name}: {exc}")

    logger.info(f"Done. created={created}, failed={failed}, total_images={len(image_files)}")
    return 0 if failed == 0 else 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest image files into RAG knowledge corpus")
    parser.add_argument("--input", required=True, help="Directory containing image files")
    parser.add_argument(
        "--truth-level",
        default="L3",
        choices=["L1", "L2", "L3", "L4"],
        help="Truth level metadata for created docs",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview ingestion only")
    parser.add_argument("--no-vision", action="store_true", help="Skip vision model, use deterministic captions only")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logs")
    args = parser.parse_args()

    setup_logging(args.verbose)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
