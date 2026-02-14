#!/usr/bin/env python3
"""Extract embedded images from PDF files and build a JSON manifest.

Usage:
  python scripts/extract_pdf_images.py --input /app/pdfs --output /app/pdf-images
  python scripts/extract_pdf_images.py --input /app/pdfs --output /app/pdf-images --min-bytes 4096
"""

import argparse
import json
import logging
import re
from pathlib import Path
from typing import Any

from pypdf import PdfReader


logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "document"


def detect_ext(name: str) -> str:
    suffix = Path(name).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".bmp"}:
        return suffix
    return ".bin"


def extract_from_pdf(pdf_path: Path, output_dir: Path, min_bytes: int) -> dict[str, Any]:
    reader = PdfReader(str(pdf_path))
    slug = slugify(pdf_path.stem)
    doc_dir = output_dir / slug
    doc_dir.mkdir(parents=True, exist_ok=True)

    extracted = []
    skipped_small = 0
    image_counter = 0

    for page_index, page in enumerate(reader.pages, start=1):
        for page_img_index, img in enumerate(page.images, start=1):
            name = getattr(img, "name", f"img-{page_img_index}")
            data = getattr(img, "data", b"") or b""
            if len(data) < min_bytes:
                skipped_small += 1
                continue

            ext = detect_ext(name)
            filename = f"{slug}_p{page_index:03d}_{page_img_index:03d}{ext}"
            out_path = doc_dir / filename
            out_path.write_bytes(data)

            item: dict[str, Any] = {
                "source_pdf": str(pdf_path),
                "page": page_index,
                "index_on_page": page_img_index,
                "filename": filename,
                "path": str(out_path),
                "bytes": len(data),
            }

            pil_image = getattr(img, "image", None)
            if pil_image is not None:
                item["width"] = getattr(pil_image, "width", None)
                item["height"] = getattr(pil_image, "height", None)

            extracted.append(item)
            image_counter += 1

    manifest = {
        "source_pdf": str(pdf_path),
        "output_dir": str(doc_dir),
        "images_extracted": image_counter,
        "images_skipped_small": skipped_small,
        "images": extracted,
    }
    (doc_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract embedded images from PDF files")
    parser.add_argument("--input", required=True, help="Input PDF file or directory")
    parser.add_argument("--output", required=True, help="Output directory for extracted images")
    parser.add_argument("--min-bytes", type=int, default=2048, help="Skip tiny images below this size")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logs")
    args = parser.parse_args()

    setup_logging(args.verbose)

    input_path = Path(args.input).resolve()
    output_dir = Path(args.output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files: list[Path]
    if input_path.is_file() and input_path.suffix.lower() == ".pdf":
        pdf_files = [input_path]
    elif input_path.is_dir():
        pdf_files = sorted(input_path.rglob("*.pdf"))
    else:
        logger.error(f"Input not found or not PDF/directory: {input_path}")
        return 1

    if not pdf_files:
        logger.warning(f"No PDF files found in: {input_path}")
        return 0

    total_images = 0
    for pdf_file in pdf_files:
        try:
            manifest = extract_from_pdf(pdf_file, output_dir, args.min_bytes)
            total_images += manifest["images_extracted"]
            logger.info(
                f"{pdf_file.name}: extracted={manifest['images_extracted']} "
                f"skipped_small={manifest['images_skipped_small']}"
            )
        except Exception as exc:  # noqa: BLE001
            logger.error(f"Failed for {pdf_file}: {exc}")

    logger.info(f"Done. PDFs={len(pdf_files)}, total_images={total_images}, output={output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
