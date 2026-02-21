#!/usr/bin/env python3
"""Normalize extracted PDF images:
- rename .bin files to detected real extension when possible
- fallback conversion to PNG via Pillow for unknown binaries
- update manifest.json filenames/paths accordingly
"""

import argparse
import json
import logging
from io import BytesIO
from pathlib import Path


logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def detect_extension(data: bytes) -> str | None:
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if data.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if data.startswith(b"GIF87a") or data.startswith(b"GIF89a"):
        return ".gif"
    if data.startswith(b"BM"):
        return ".bmp"
    if data.startswith(b"II*\x00") or data.startswith(b"MM\x00*"):
        return ".tiff"
    if len(data) > 12 and data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return ".webp"
    return None


def convert_with_pillow(src: Path, dst: Path) -> bool:
    try:
        from PIL import Image  # type: ignore
    except Exception:
        return False

    try:
        data = src.read_bytes()
        with Image.open(BytesIO(data)) as img:
            img.save(dst, format="PNG")
        return True
    except Exception:
        return False


def normalize_manifest(manifest_path: Path) -> tuple[int, int]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    images = manifest.get("images", [])

    renamed = 0
    failed = 0
    parent = manifest_path.parent

    for img in images:
        filename = str(img.get("filename", ""))
        if not filename.endswith(".bin"):
            continue

        src = parent / filename
        if not src.exists():
            failed += 1
            continue

        data = src.read_bytes()
        ext = detect_extension(data)

        if ext:
            dst = src.with_suffix(ext)
            src.rename(dst)
        else:
            dst = src.with_suffix(".png")
            ok = convert_with_pillow(src, dst)
            if not ok:
                failed += 1
                continue
            src.unlink(missing_ok=True)

        img["filename"] = dst.name
        img["path"] = str((parent / dst.name))
        renamed += 1

    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return renamed, failed


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize extracted PDF image files and manifests")
    parser.add_argument("--input", required=True, help="Root folder containing manifest.json files")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    setup_logging(args.verbose)
    root = Path(args.input).resolve()
    manifests = sorted(root.rglob("manifest.json"))
    if not manifests:
        logger.warning(f"No manifest.json found under {root}")
        return 0

    total_renamed = 0
    total_failed = 0
    for manifest in manifests:
        renamed, failed = normalize_manifest(manifest)
        total_renamed += renamed
        total_failed += failed
        logger.info(f"{manifest}: renamed={renamed}, failed={failed}")

    logger.info(f"Done. renamed={total_renamed}, failed={total_failed}")
    return 0 if total_failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
