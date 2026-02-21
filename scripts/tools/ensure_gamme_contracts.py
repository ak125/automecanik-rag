#!/usr/bin/env python3
"""Ensure strict gamme page contracts are materialized in markdown frontmatter.

Usage:
  python scripts/ensure_gamme_contracts.py --dry-run
  python scripts/ensure_gamme_contracts.py --apply
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any

import frontmatter

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.services.gamme_page_contract import build_and_validate_gamme_page_contract


logger = logging.getLogger(__name__)

IGNORED_DIRS = {"_raw", "_trash", "__pycache__"}
ALLOWED_ROOTS = {
    "catalog",
    "gamme",
    "gammes",
    "knowledge",
}


def setup_logging(verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def iter_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        rel_parts = path.relative_to(root).parts
        if any(part.startswith(".") or part in IGNORED_DIRS for part in rel_parts):
            continue
        if len(rel_parts) < 2:
            continue
        if rel_parts[0] not in ALLOWED_ROOTS:
            continue
        files.append(path)
    return sorted(files)


def is_gamme_document(metadata: dict[str, Any], rel_path: str) -> bool:
    source_type = str(metadata.get("source_type", "")).strip().lower()
    entity_type = str(metadata.get("entity_type", "")).strip().lower()

    if source_type == "gamme" or entity_type == "gamme":
        return True

    rel_norm = rel_path.replace("\\", "/").lower()
    return "/gammes/" in f"/{rel_norm}" or "/catalog/" in f"/{rel_norm}"


def normalize_for_compare(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def process_file(md_file: Path, root: Path, apply: bool) -> tuple[str, int, int]:
    rel_path = md_file.relative_to(root).as_posix()
    post = frontmatter.load(md_file)
    metadata = dict(post.metadata)

    if not is_gamme_document(metadata, rel_path):
        return "skipped", 0, 0

    result = build_and_validate_gamme_page_contract(
        metadata=metadata,
        content=post.content,
        source_path=rel_path,
    )

    contract = result["contract"]
    errors = result["errors"]
    warnings = result["warnings"]

    for warning in warnings:
        logger.warning("%s: %s", rel_path, warning)

    if errors:
        for error in errors:
            logger.error("%s: %s", rel_path, error)
        return "error", len(errors), len(warnings)

    existing = metadata.get("page_contract")
    if normalize_for_compare(existing) == normalize_for_compare(contract):
        return "unchanged", 0, len(warnings)

    if apply:
        post.metadata["page_contract"] = contract
        md_file.write_text(frontmatter.dumps(post), encoding="utf-8")
        logger.info("updated %s", rel_path)
        return "updated", 0, len(warnings)

    logger.info("would-update %s", rel_path)
    return "would_update", 0, len(warnings)


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize gamme page contracts in frontmatter")
    parser.add_argument("--path", default="", help="Knowledge root path (default: <repo>/knowledge)")
    parser.add_argument("--apply", action="store_true", help="Write updates to files")
    parser.add_argument("--max-files", type=int, default=0, help="Limit processed files (0 = all)")
    parser.add_argument("--strict-exit", action="store_true", help="Exit non-zero if contract errors are found")
    parser.add_argument("--verbose", action="store_true", help="Verbose logging")
    args = parser.parse_args()

    setup_logging(args.verbose)

    root = Path(args.path).resolve() if args.path else (ROOT_DIR / "knowledge").resolve()
    if not root.exists():
        logger.error("knowledge path not found: %s", root)
        return 1

    files = iter_markdown_files(root)
    if args.max_files > 0:
        files = files[: args.max_files]

    stats = {
        "updated": 0,
        "would_update": 0,
        "unchanged": 0,
        "skipped": 0,
        "error": 0,
        "errors_count": 0,
        "warnings_count": 0,
    }

    for md_file in files:
        status, errors_count, warnings_count = process_file(md_file, root, args.apply)
        stats[status] = stats.get(status, 0) + 1
        stats["errors_count"] += errors_count
        stats["warnings_count"] += warnings_count

    logger.info(
        "done scanned=%d updated=%d would_update=%d unchanged=%d skipped=%d errors=%d warnings=%d apply=%s",
        len(files),
        stats["updated"],
        stats["would_update"],
        stats["unchanged"],
        stats["skipped"],
        stats["errors_count"],
        stats["warnings_count"],
        args.apply,
    )

    if args.strict_exit and stats["error"] > 0:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
