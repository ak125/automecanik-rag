#!/usr/bin/env python3
"""Build video storyboard assets (CSV + JSON) from PDF image manifests.

Input: folders containing `manifest.json` produced by `extract_pdf_images.py`.
Output:
  - storyboard.csv
  - storyboard.json

Usage:
  python scripts/build_video_storyboard.py --input /opt/automecanik/rag/pdf-images --output /opt/automecanik/rag/pdf-images/storyboard
"""

import argparse
import csv
import json
import logging
import re
from pathlib import Path
from typing import Any


logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def list_manifests(input_dir: Path) -> list[Path]:
    return sorted(input_dir.rglob("manifest.json"))


def slug_to_title(slug: str) -> str:
    words = [w for w in slug.replace("_", "-").split("-") if w]
    return " ".join(w.capitalize() for w in words)


def guess_segment(doc_slug: str, page: int) -> str:
    s = doc_slug.lower()
    if "brake" in s or "frein" in s:
        if page <= 3:
            return "intro"
        if page <= 8:
            return "diagnostic"
        return "repair"
    if "manual" in s or "operation" in s:
        if page <= 5:
            return "overview"
        if page <= 20:
            return "procedure"
        return "reference"
    return "main"


def score_visual(image: dict[str, Any], min_bytes: int) -> tuple[int, list[str]]:
    bytes_size = int(image.get("bytes") or 0)
    width = int(image.get("width") or 0)
    height = int(image.get("height") or 0)
    ext = Path(str(image.get("filename", ""))).suffix.lower()

    reasons = []
    score = 50

    if bytes_size >= 150_000:
        score += 20
        reasons.append("high_resolution")
    elif bytes_size < min_bytes:
        score -= 40
        reasons.append("too_small")

    if width and height:
        ratio = width / max(height, 1)
        if 0.8 <= ratio <= 1.9:
            score += 10
            reasons.append("good_frame_ratio")
        if width >= 1000:
            score += 10
            reasons.append("wide_enough")
    else:
        reasons.append("no_dimensions")

    if ext == ".bin":
        score -= 20
        reasons.append("unknown_binary_format")

    score = max(0, min(100, score))
    return score, reasons


def build_rows(input_dir: Path, min_bytes: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    manifests = list_manifests(input_dir)
    shot_id = 1

    for manifest_path in manifests:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            logger.warning(f"Skip invalid manifest {manifest_path}: {exc}")
            continue

        images = manifest.get("images", [])
        source_pdf = str(manifest.get("source_pdf", ""))
        doc_slug = manifest_path.parent.name
        doc_title = slug_to_title(doc_slug)

        images_sorted = sorted(images, key=lambda i: (int(i.get("page", 0)), int(i.get("index_on_page", 0))))

        for img in images_sorted:
            score, reasons = score_visual(img, min_bytes=min_bytes)
            page = int(img.get("page") or 0)
            duration = 6 if score >= 80 else 5 if score >= 60 else 4
            segment = guess_segment(doc_slug, page)
            rel_path = Path(img.get("path", ""))
            if rel_path.is_absolute():
                try:
                    rel_path = rel_path.relative_to(input_dir)
                except Exception:
                    rel_path = Path(img.get("filename", ""))

            rows.append(
                {
                    "shot_id": shot_id,
                    "doc_slug": doc_slug,
                    "doc_title": doc_title,
                    "source_pdf": source_pdf,
                    "page": page,
                    "index_on_page": int(img.get("index_on_page") or 0),
                    "image_file": str(rel_path),
                    "filename": str(img.get("filename", "")),
                    "bytes": int(img.get("bytes") or 0),
                    "width": int(img.get("width") or 0),
                    "height": int(img.get("height") or 0),
                    "format": Path(str(img.get("filename", ""))).suffix.lower().lstrip("."),
                    "segment": segment,
                    "recommended_duration_sec": duration,
                    "visual_score": score,
                    "priority": "high" if score >= 75 else "medium" if score >= 50 else "low",
                    "notes": ";".join(reasons),
                }
            )
            shot_id += 1

    return rows


def write_csv(rows: list[dict[str, Any]], output_csv: Path) -> None:
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        output_csv.write_text("", encoding="utf-8")
        return

    fieldnames = list(rows[0].keys())
    with output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_json(rows: list[dict[str, Any]], output_json: Path) -> None:
    output_json.parent.mkdir(parents=True, exist_ok=True)

    grouped: dict[str, Any] = {}
    for row in rows:
        slug = row["doc_slug"]
        grouped.setdefault(slug, {"doc_title": row["doc_title"], "source_pdf": row["source_pdf"], "shots": []})
        grouped[slug]["shots"].append(row)

    payload = {
        "total_shots": len(rows),
        "documents": grouped,
    }
    output_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build video storyboard CSV+JSON from PDF image manifests")
    parser.add_argument("--input", required=True, help="Directory containing manifest.json files")
    parser.add_argument("--output", required=True, help="Output directory for storyboard files")
    parser.add_argument("--min-bytes", type=int, default=2048, help="Threshold used for visual score penalties")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    setup_logging(args.verbose)

    input_dir = Path(args.input).resolve()
    output_dir = Path(args.output).resolve()

    if not input_dir.exists():
        logger.error(f"Input folder not found: {input_dir}")
        return 1

    rows = build_rows(input_dir, min_bytes=args.min_bytes)
    if not rows:
        logger.warning("No storyboard rows generated (no manifests/images found)")
        return 0

    output_csv = output_dir / "storyboard.csv"
    output_json = output_dir / "storyboard.json"
    write_csv(rows, output_csv)
    write_json(rows, output_json)

    logger.info(f"Generated {len(rows)} shots")
    logger.info(f"CSV: {output_csv}")
    logger.info(f"JSON: {output_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
