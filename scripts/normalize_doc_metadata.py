#!/usr/bin/env python3
"""Normalize markdown metadata for strict RAG governance."""

import argparse
import logging
import sys
from pathlib import Path

import frontmatter

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.services.knowledge_service import KnowledgeService  # noqa: E402


logger = logging.getLogger(__name__)

IGNORED_DIRS = {"_raw", "_trash", "__pycache__"}
WEAK_CATEGORY_VALUES = {"", "general", "knowledge", "catalog", "diagnostic"}
ALLOWED_ROOT_DIRS = {
    "canonical",
    "catalog",
    "diagnostic",
    "faq",
    "gammes",
    "guide",
    "guides",
    "knowledge",
    "media",
    "policies",
    "policy",
    "structured",
    "tabular",
    "vehicle",
    "vehicles",
}


def iter_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        rel_parts = path.relative_to(root).parts
        if any(part.startswith(".") or part in IGNORED_DIRS for part in rel_parts):
            continue
        if len(rel_parts) < 2:
            # Ignore top-level markdown files (README, notes, etc.) not part of corpus docs.
            continue
        if rel_parts[0] not in ALLOWED_ROOT_DIRS:
            continue
        files.append(path)
    return sorted(files)


def normalize_one(
    service: KnowledgeService,
    root: Path,
    md_file: Path,
    fix_category: bool,
) -> tuple[dict, bool, str]:
    rel_path = str(md_file.relative_to(root))
    post = frontmatter.load(md_file)
    metadata = dict(post.metadata)

    source_type_raw = str(metadata.get("source_type", "")).strip().lower()
    source_type = source_type_raw or service._infer_source_type(rel_path)  # noqa: SLF001
    if source_type == "auto":
        source_type = service._infer_source_type_from_content(post.content)  # noqa: SLF001

    category_raw = str(metadata.get("category", "")).strip().lower()
    category = category_raw or service._infer_category(rel_path)  # noqa: SLF001

    explicit_doc_family = str(metadata.get("doc_family", "")).strip()
    try:
        doc_family = service._resolve_doc_family(  # noqa: SLF001
            source_type=source_type,
            explicit_doc_family=explicit_doc_family,
            rel_path=rel_path,
        )
    except ValueError:
        doc_family = service._resolve_doc_family(  # noqa: SLF001
            source_type=source_type,
            explicit_doc_family="",
            rel_path=rel_path,
        )

    updates: dict[str, str] = {}
    if source_type_raw != source_type:
        updates["source_type"] = source_type
    if not category_raw:
        updates["category"] = category
    if str(metadata.get("doc_family", "")).strip().lower() != doc_family:
        updates["doc_family"] = doc_family

    if fix_category:
        inferred_category = service._infer_category_from_content(source_type, post.content)  # noqa: SLF001
        if inferred_category and inferred_category != category:
            if category in WEAK_CATEGORY_VALUES or (category == "suspension" and inferred_category == "freinage"):
                updates["category"] = inferred_category

    directory = Path(rel_path).parts[0].lower() if Path(rel_path).parts else ""
    path_valid = True
    path_error = ""
    try:
        service._validate_directory_for_family(directory=directory, doc_family=doc_family)  # noqa: SLF001
    except ValueError as exc:
        path_valid = False
        path_error = str(exc)

    return updates, path_valid, path_error


def write_updates(md_file: Path, updates: dict) -> None:
    post = frontmatter.load(md_file)
    for key, value in updates.items():
        post.metadata[key] = value
    md_file.write_text(frontmatter.dumps(post), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize markdown metadata for strict governance")
    parser.add_argument("--path", default="", help="Knowledge root path")
    parser.add_argument("--apply", action="store_true", help="Write updates to files")
    parser.add_argument("--fix-category", action="store_true", help="Reclassify weak categories from content")
    parser.add_argument("--max-files", type=int, default=0, help="Limit processed files (0 = all)")
    parser.add_argument("--strict-exit", action="store_true", help="Exit non-zero when path-family mismatches are detected")
    parser.add_argument("--verbose", action="store_true", help="Verbose logging")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    default_path = Path.cwd() / "knowledge"
    root = Path(args.path).expanduser().resolve() if args.path else default_path.resolve()
    if not root.exists():
        logger.error("knowledge path not found: %s", root)
        return 1

    service = KnowledgeService()
    service.knowledge_path = root

    files = iter_markdown_files(root)
    if args.max_files > 0:
        files = files[:args.max_files]

    changed = 0
    path_mismatches = 0
    scanned = 0

    for md_file in files:
        scanned += 1
        updates, path_valid, path_error = normalize_one(service, root, md_file, args.fix_category)
        if updates:
            changed += 1
            rel = md_file.relative_to(root).as_posix()
            logger.info("update %s -> %s", rel, updates)
            if args.apply:
                write_updates(md_file, updates)
        if not path_valid:
            path_mismatches += 1
            logger.warning("path mismatch %s: %s", md_file.relative_to(root).as_posix(), path_error)

    logger.info(
        "done scanned=%d changed=%d path_mismatches=%d apply=%s",
        scanned, changed, path_mismatches, args.apply,
    )

    if args.strict_exit and path_mismatches > 0:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
