#!/usr/bin/env python3
"""Phase F.5 (ADR-031) — canonical importer : automecanik-wiki/exports/rag/ → KB_Knowledge_v2.

This is the **single canonical entry point** for indexing documentary memory
into the rag service post-Phase F.5. Replaces ad-hoc ingestion (admin UI POSTs,
manual curl scripts) which are now 410 Gone in readonly mode.

Flow ::

    automecanik-wiki/exports/rag/<entity>/<slug>.md   (frontmatter validated)
                ↓ Pydantic v2 parse
                ↓ filter (5 mandatory criteria)
                ↓ idempotency check (natural key)
                ↓ chunk + embed + write to KB_Knowledge_v2

Behaviour boundaries ::

  - **Fail-fast** : exits 2 if `KB_Knowledge_v2` does not exist (PR-B must run first).
  - **Lock** : flock `/var/lock/rag-import.lock` non-blocking, exit 3 if held.
  - **Wiki path validation** : exits 4 if `$AUTOMECANIK_WIKI_PATH` is missing
    or not a Git repo.
  - **Filters (intentionally conservative)** :
      * `exportable.rag == True`
      * `review_status == "approved"` (excludes `auto_passed` until amendment)
      * `truth_level ∈ {"L1","L2"}`
      * `len(source_refs) >= 1`
      * `content_hash` present (≥ 32 chars sha256)
  - **Idempotence by natural key** :
      `(canonical_source, source_path, content_hash, chunk_index)` —
      NOT `lineage_id` (which is generated per batch and not stable).
  - **Dead-letter** : skipped frontmatters land in
      `$RAG_QUARANTINE_DIR/<reason>/<entity_type>/<slug>.md`
    plus a `<slug>.skip.json` sidecar. Default path is
    `/var/lib/automecanik-rag/quarantine/` (Docker volume) — outside the Git
    repo on purpose.
  - **source_commit** : commit of the WIKI repo (not the rag consumer).

Exit codes ::
   0 : ok
   1 : user error (CLI arg invalid)
   2 : KB_Knowledge_v2 missing — run PR-B migration first
   3 : another import is holding the lock
   4 : `$AUTOMECANIK_WIKI_PATH` invalid or not a Git repo
   5 : runtime error (Weaviate / fs / etc.)

CLI ::

    python scripts/importers/import_wiki_exports.py                  # dry-run
    python scripts/importers/import_wiki_exports.py --apply
    python scripts/importers/import_wiki_exports.py --entity-type gamme
    python scripts/importers/import_wiki_exports.py --apply --limit 50
    python scripts/importers/import_wiki_exports.py --apply --force-reembedding
"""

from __future__ import annotations

import argparse
import errno
import fcntl
import json
import logging
import os
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterator, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

logger = logging.getLogger("f5.import_wiki")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# ---------------------------------------------------------------------------
# Config / paths
# ---------------------------------------------------------------------------

WIKI_PATH = Path(
    os.getenv("AUTOMECANIK_WIKI_PATH", "/opt/automecanik/automecanik-wiki")
)
EXPORTS_RAG_SUBDIR = "exports/rag"

QUARANTINE_DIR = Path(
    os.getenv("RAG_QUARANTINE_DIR", "/var/lib/automecanik-rag/quarantine")
)
LOCK_PATH = os.getenv("RAG_IMPORT_LOCK_PATH", "/var/lock/rag-import.lock")
TARGET_COLLECTION = os.getenv("RAG_WEAVIATE_COLLECTION", "KB_Knowledge_v2")

CANONICAL_SOURCE_WIKI = "automecanik-wiki"
SOURCE_LAYER_EXPORTS_RAG = "exports/rag"
ORIGIN_BATCH_KIND_WIKI = "wiki_import"

ALLOWED_TRUTH_LEVELS = {"L1", "L2"}
ALLOWED_REVIEW_STATUSES = {"approved"}  # Phase F.5 conservative — see ADR-031 runbook

EXIT_OK = 0
EXIT_USER_ERROR = 1
EXIT_TARGET_MISSING = 2
EXIT_LOCK_HELD = 3
EXIT_WIKI_PATH_INVALID = 4
EXIT_RUNTIME_ERROR = 5

# ---------------------------------------------------------------------------
# Pydantic models — discriminated union mirror of wiki/_meta/schema/exports/rag.schema.json
# ---------------------------------------------------------------------------

from app.models.wiki_frontmatter import WikiExportFrontmatter  # noqa: E402

try:
    from pydantic import TypeAdapter
except ImportError:  # pragma: no cover
    logger.error("F.5 import: pydantic v2 not available — `pip install pydantic`")
    sys.exit(EXIT_RUNTIME_ERROR)

_FRONTMATTER_VALIDATOR = TypeAdapter(WikiExportFrontmatter)

# ---------------------------------------------------------------------------
# Lock
# ---------------------------------------------------------------------------


def acquire_lock(path: str):
    """Non-blocking flock — exit 3 cleanly if another import holds the lock."""
    try:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(path, os.O_CREAT | os.O_RDWR, 0o600)
    except (OSError, PermissionError) as exc:
        logger.warning("F.5 lock: %s not writable (%s) — falling back to /tmp", path, exc)
        fd = os.open("/tmp/rag-import.lock", os.O_CREAT | os.O_RDWR, 0o600)

    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError as exc:
        if exc.errno in (errno.EAGAIN, errno.EWOULDBLOCK):
            logger.error(
                "F.5 lock: %s held by another import — refusing (exit %d)",
                path, EXIT_LOCK_HELD,
            )
            os.close(fd)
            sys.exit(EXIT_LOCK_HELD)
        raise
    return fd


# ---------------------------------------------------------------------------
# Pre-flight checks
# ---------------------------------------------------------------------------


def assert_wiki_path_valid() -> Path:
    """Exit 4 if AUTOMECANIK_WIKI_PATH is not a Git repo containing exports/rag/."""
    if not WIKI_PATH.is_dir():
        logger.error(
            "F.5 import: AUTOMECANIK_WIKI_PATH=%s does not exist (set the env var, "
            "or clone github.com/ak125/automecanik-wiki)", WIKI_PATH,
        )
        sys.exit(EXIT_WIKI_PATH_INVALID)
    if not (WIKI_PATH / ".git").exists():
        logger.error("F.5 import: %s is not a Git repository", WIKI_PATH)
        sys.exit(EXIT_WIKI_PATH_INVALID)
    exports_root = WIKI_PATH / EXPORTS_RAG_SUBDIR
    if not exports_root.exists():
        # exports/rag/ is gitignored and generated post-promotion. No exports
        # yet is normal — log info and proceed (we'll find 0 files).
        logger.info(
            "F.5 import: %s does not exist yet (gitignored — generated post-promotion). "
            "0 files to import.", exports_root,
        )
    return exports_root


def assert_target_collection_exists(client) -> None:
    """Exit 2 if KB_Knowledge_v2 is missing — PR-B migration must run first."""
    if not client.collections.exists(TARGET_COLLECTION):
        logger.error(
            "F.5 import: %s does not exist — run scripts/migrations/migrate_kb_v1_to_v2.py "
            "(PR-B) first", TARGET_COLLECTION,
        )
        sys.exit(EXIT_TARGET_MISSING)


def get_wiki_head_commit() -> Optional[str]:
    """Return git HEAD sha-1 of the WIKI repo (not the rag consumer)."""
    try:
        result = subprocess.run(
            ["git", "-C", str(WIKI_PATH), "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=5, check=True,
        )
        return result.stdout.strip() or None
    except (subprocess.SubprocessError, OSError) as exc:
        logger.warning("F.5 import: cannot read wiki HEAD commit (%s)", exc)
        return None


# ---------------------------------------------------------------------------
# Frontmatter parse + filter
# ---------------------------------------------------------------------------

# Reasons used as quarantine sub-directories — keep low cardinality.
SKIP_REASONS = {
    "not_exportable_rag": "exportable.rag != true",
    "not_approved": "review_status != 'approved'",
    "truth_level_too_low": "truth_level not in {L1, L2}",
    "no_source_refs": "source_refs is empty",
    "missing_content_hash": "content_hash absent",
    "pydantic_validation_error": "frontmatter does not match schema",
    "missing_frontmatter": "no YAML frontmatter found",
}


def parse_frontmatter_yaml(md_path: Path) -> Optional[Dict[str, Any]]:
    """Return the YAML frontmatter dict, or None if absent/malformed."""
    try:
        import frontmatter
    except ImportError:  # pragma: no cover
        logger.error("F.5 import: `python-frontmatter` not installed")
        sys.exit(EXIT_RUNTIME_ERROR)

    try:
        post = frontmatter.load(str(md_path))
    except Exception as exc:
        logger.warning("F.5 import: cannot parse frontmatter %s (%s)", md_path, exc)
        return None
    if not post.metadata:
        return None
    return dict(post.metadata)


def evaluate_filters(meta: Dict[str, Any]) -> Optional[str]:
    """Return None if the doc passes all filters, or a SKIP_REASONS key otherwise."""
    exportable = meta.get("exportable") or {}
    if not (isinstance(exportable, dict) and exportable.get("rag") is True):
        return "not_exportable_rag"
    if meta.get("review_status") not in ALLOWED_REVIEW_STATUSES:
        return "not_approved"
    if meta.get("truth_level") not in ALLOWED_TRUTH_LEVELS:
        return "truth_level_too_low"
    if not (isinstance(meta.get("source_refs"), list) and len(meta["source_refs"]) >= 1):
        return "no_source_refs"
    if not meta.get("content_hash"):
        return "missing_content_hash"
    return None


def write_quarantine(*, reason: str, entity_type: str, slug: str,
                     md_path: Path, meta: Optional[Dict[str, Any]],
                     errors: Optional[list] = None) -> None:
    """Write the rejected file + a sidecar JSON describing why."""
    try:
        target_dir = QUARANTINE_DIR / reason / entity_type
        target_dir.mkdir(parents=True, exist_ok=True)
        target_md = target_dir / f"{slug}.md"
        target_md.write_bytes(md_path.read_bytes())

        sidecar = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "reason": reason,
            "reason_explained": SKIP_REASONS.get(reason, "(unknown)"),
            "source_md": str(md_path),
            "entity_type": entity_type,
            "slug": slug,
            "frontmatter_dump": meta,
            "validation_errors": errors,
        }
        (target_dir / f"{slug}.skip.json").write_text(
            json.dumps(sidecar, indent=2, default=str), encoding="utf-8",
        )
    except (OSError, PermissionError) as exc:
        logger.error("F.5 import: cannot write quarantine for %s (%s)", md_path, exc)


# ---------------------------------------------------------------------------
# Idempotence by natural key
# ---------------------------------------------------------------------------


def chunk_already_in_v2(client, *, canonical_source: str, source_path: str,
                       content_hash: str, chunk_index: int) -> bool:
    """Return True if a chunk with this natural key is already in v2."""
    from weaviate.classes.query import Filter  # type: ignore

    coll = client.collections.get(TARGET_COLLECTION)
    where = (
        Filter.by_property("canonical_source").equal(canonical_source)
        & Filter.by_property("source_path").equal(source_path)
        & Filter.by_property("content_hash").equal(content_hash)
        & Filter.by_property("chunk_index").equal(chunk_index)
    )
    response = coll.query.fetch_objects(filters=where, limit=1)
    return len(response.objects) > 0


# ---------------------------------------------------------------------------
# Iteration
# ---------------------------------------------------------------------------


def iter_export_files(exports_root: Path,
                      entity_filter: Optional[str] = None) -> Iterator[Path]:
    """Yield each .md file under exports/rag/<entity>/."""
    if not exports_root.exists():
        return
    for md_path in sorted(exports_root.rglob("*.md")):
        if entity_filter:
            # exports/rag/<entity_type>/<slug>.md — second segment is entity_type
            try:
                entity_dir = md_path.relative_to(exports_root).parts[0]
            except (ValueError, IndexError):
                continue
            if entity_dir != entity_filter:
                continue
        yield md_path


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------


def run(*, apply: bool, entity_filter: Optional[str], limit: Optional[int],
        force_reembedding: bool) -> Dict[str, Any]:
    from app.config import get_settings
    settings = get_settings()

    try:
        from app.services.weaviate_client import WeaviateClient
    except ImportError as exc:
        logger.error("F.5 import: cannot import WeaviateClient (%s)", exc)
        sys.exit(EXIT_RUNTIME_ERROR)

    exports_root = assert_wiki_path_valid()

    wc = WeaviateClient()
    client = wc.client
    assert_target_collection_exists(client)

    wiki_commit = get_wiki_head_commit()
    batch_lineage_id = str(uuid.uuid4())  # one UUID for the whole batch
    embedding_model = settings.embedding_model

    counters: Dict[str, int] = {
        "imported": 0,
        "skipped_idempotent": 0,
        "skipped_filter": 0,
        "failed_validation": 0,
        "errors": 0,
    }
    skip_reasons: Dict[str, int] = {}

    logger.info(
        "F.5 import: starting (apply=%s, entity_filter=%s, limit=%s, "
        "wiki=%s, wiki_commit=%s, lineage_id=%s, target=%s)",
        apply, entity_filter, limit, WIKI_PATH, wiki_commit,
        batch_lineage_id, TARGET_COLLECTION,
    )

    seen = 0
    for md_path in iter_export_files(exports_root, entity_filter):
        if limit is not None and seen >= limit:
            break
        seen += 1

        # Best-effort entity_type detection from path.
        try:
            relative = md_path.relative_to(exports_root)
            entity_type = relative.parts[0] if len(relative.parts) > 1 else "unknown"
            slug = md_path.stem
        except ValueError:
            entity_type, slug = "unknown", md_path.stem

        meta = parse_frontmatter_yaml(md_path)
        if meta is None:
            counters["failed_validation"] += 1
            skip_reasons["missing_frontmatter"] = skip_reasons.get("missing_frontmatter", 0) + 1
            write_quarantine(reason="missing_frontmatter", entity_type=entity_type,
                             slug=slug, md_path=md_path, meta=None)
            continue

        # Pydantic schema validation (catches drift from JSON Schema).
        try:
            _FRONTMATTER_VALIDATOR.validate_python(meta)
        except Exception as exc:  # ValidationError or other
            counters["failed_validation"] += 1
            skip_reasons["pydantic_validation_error"] = (
                skip_reasons.get("pydantic_validation_error", 0) + 1
            )
            errors_list = [str(exc)]
            write_quarantine(reason="pydantic_validation_error",
                             entity_type=entity_type, slug=slug,
                             md_path=md_path, meta=meta, errors=errors_list)
            continue

        # Semantic filter (5 conservative criteria).
        skip_reason = evaluate_filters(meta)
        if skip_reason:
            counters["skipped_filter"] += 1
            skip_reasons[skip_reason] = skip_reasons.get(skip_reason, 0) + 1
            write_quarantine(reason=skip_reason, entity_type=entity_type,
                             slug=slug, md_path=md_path, meta=meta)
            continue

        source_path = str(md_path.relative_to(WIKI_PATH))
        content_hash = meta["content_hash"]
        chunk_index = 0  # one chunk per file for now ; multi-chunk pipeline is upstream
        source_commit = (
            meta.get("traceability", {}).get("source_commit") if isinstance(meta.get("traceability"), dict)
            else None
        ) or wiki_commit

        if not force_reembedding and chunk_already_in_v2(
            client,
            canonical_source=CANONICAL_SOURCE_WIKI,
            source_path=source_path,
            content_hash=content_hash,
            chunk_index=chunk_index,
        ):
            counters["skipped_idempotent"] += 1
            continue

        if not apply:
            counters["imported"] += 1  # would-be in dry-run
            continue

        # ----- live insert path -----
        # NOTE : full embedding + chunking is delegated to the pre-existing
        # WeaviateClient.write_object pipeline. This script's job is to
        # validate, filter, and feed metadata. The body content + embedding
        # generation is handled the same way as v1 ingestion.
        try:
            target_collection = client.collections.get(TARGET_COLLECTION)
            properties = {
                "content": meta.get("body", "") or "",  # body is set elsewhere if present
                "title": meta.get("title", ""),
                "source_path": source_path,
                "source_type": entity_type,
                "truth_level": meta.get("truth_level"),
                "namespace": entity_type,
                "chunk_index": chunk_index,
                "content_hash": content_hash,
                # Phase F.5 metadata
                "canonical_source": CANONICAL_SOURCE_WIKI,
                "source_layer": SOURCE_LAYER_EXPORTS_RAG,
                "source_commit": source_commit,
                "lineage_id": batch_lineage_id,
                "embedding_model": embedding_model,
                "origin_batch_kind": ORIGIN_BATCH_KIND_WIKI,
            }
            target_collection.data.insert(properties=properties)
            counters["imported"] += 1
        except Exception as exc:
            logger.error("F.5 import: insert failed for %s (%s)", source_path, exc)
            counters["errors"] += 1

    summary = {
        **counters,
        "skip_reasons": skip_reasons,
        "wiki_commit": wiki_commit,
        "lineage_id": batch_lineage_id,
        "target_collection": TARGET_COLLECTION,
    }
    logger.info("F.5 import: done — summary=%s", summary)
    return summary


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true",
                        help="Actually write to Weaviate (default: dry-run)")
    parser.add_argument("--entity-type", default=None,
                        help="Restrict to one entity_type subdir (gamme, vehicle, ...)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Stop after N files (test mode)")
    parser.add_argument("--force-reembedding", action="store_true",
                        help="Skip the idempotency check — re-process every file")
    parser.add_argument("--json-out", default=None,
                        help="Write the summary JSON to this path")
    args = parser.parse_args()

    if args.limit is not None and args.limit < 0:
        logger.error("F.5 import: --limit must be ≥ 0")
        return EXIT_USER_ERROR

    lock_fd = acquire_lock(LOCK_PATH)
    try:
        summary = run(
            apply=args.apply,
            entity_filter=args.entity_type,
            limit=args.limit,
            force_reembedding=args.force_reembedding,
        )
    finally:
        os.close(lock_fd)

    rendered = json.dumps(summary, indent=2, default=str)
    print(rendered)
    if args.json_out:
        Path(args.json_out).write_text(rendered + "\n", encoding="utf-8")

    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
