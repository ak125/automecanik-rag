#!/usr/bin/env python3
"""Phase F.5 (ADR-031) — migrate KB_Knowledge (v1) → KB_Knowledge_v2.

Versioning, not in-place mutation : v2 is a new collection ; v1 is preserved
for 30 days then dropped if usage metrics confirm zero hits (cf. runbook
Phase F.5 §"Drop criterion J+30+").

Idempotent : skip already-migrated chunks via the natural-key
``(canonical_source, source_path, content_hash, chunk_index)``. Re-running
is a no-op (counter "skipped_idempotent" climbs, "imported" stays 0).

Concurrency : ``flock /var/lock/rag-migrate.lock`` non-blocking. Two parallel
invocations refuse the second one cleanly (exit code 3) instead of doubling
chunks.

Usage :
    python scripts/migrations/migrate_kb_v1_to_v2.py            # dry-run by default
    python scripts/migrations/migrate_kb_v1_to_v2.py --apply
    python scripts/migrations/migrate_kb_v1_to_v2.py --apply --batch-size 250
    python scripts/migrations/migrate_kb_v1_to_v2.py --apply --limit 500

Default values for the 6 F.5 properties on migrated chunks :
    canonical_source = "legacy-rag-knowledge"
    source_layer     = "knowledge"
    source_commit    = (best-effort from __rag_knowledge.created_at + git log,
                        else None)
    lineage_id       = single UUIDv7 shared by THE ENTIRE migration batch
                       (so a future "rollback all v1-migrated chunks" is one
                       Weaviate WHERE lineage_id = X delete)
    embedding_model  = settings.embedding_model (current global default)
    origin_batch_kind= "legacy_migration"
"""

from __future__ import annotations

import argparse
import errno
import fcntl
import logging
import os
import sys
import uuid
from pathlib import Path
from typing import Iterator, Optional

# Make the repo root importable when invoked as a script.
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

logger = logging.getLogger("f5.migrate_kb")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

LOCK_PATH = os.getenv("RAG_MIGRATE_LOCK_PATH", "/var/lock/rag-migrate.lock")

EXIT_OK = 0
EXIT_USER_ERROR = 1
EXIT_TARGET_MISSING = 2
EXIT_LOCK_HELD = 3
EXIT_RUNTIME_ERROR = 4


def acquire_lock(path: str):
    """Open + non-blocking flock on the given path. Returns the file descriptor.

    The file descriptor must be kept open for the life of the migration.
    Closing it (or process exit) releases the lock.
    """
    try:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(path, os.O_CREAT | os.O_RDWR, 0o600)
    except (OSError, PermissionError) as exc:
        logger.error("F.5 lock: cannot open %s: %s", path, exc)
        # Fall back to a writable tmp lock so dev/CI without /var/lock still works.
        tmp_path = "/tmp/rag-migrate.lock"
        logger.warning("F.5 lock: falling back to %s", tmp_path)
        fd = os.open(tmp_path, os.O_CREAT | os.O_RDWR, 0o600)

    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError as exc:
        if exc.errno in (errno.EAGAIN, errno.EWOULDBLOCK):
            logger.error(
                "F.5 lock: %s is already held by another migrate run — refusing to proceed (exit %d)",
                path,
                EXIT_LOCK_HELD,
            )
            os.close(fd)
            sys.exit(EXIT_LOCK_HELD)
        raise
    return fd


def iter_v1_chunks(client, *, limit: Optional[int] = None) -> Iterator[dict]:
    """Yield each v1 chunk as a {"id":..., "props":...} dict.

    Uses Weaviate cursor pagination so memory stays bounded for large corpuses.
    """
    from weaviate.collections.classes.grpc import MetadataQuery  # type: ignore

    v1 = client.collections.get("KB_Knowledge")
    yielded = 0
    after = None
    while True:
        response = v1.query.fetch_objects(
            limit=200,
            after=after,
            return_metadata=MetadataQuery(creation_time=True),
        )
        if not response.objects:
            return
        for obj in response.objects:
            yield {"id": str(obj.uuid), "props": obj.properties}
            yielded += 1
            if limit is not None and yielded >= limit:
                return
        after = str(response.objects[-1].uuid)


def chunk_already_in_v2(client, *, canonical_source: str, source_path: str,
                       content_hash: str, chunk_index: int) -> bool:
    """Return True if a chunk with this natural key is already in v2."""
    from weaviate.classes.query import Filter  # type: ignore

    v2 = client.collections.get("KB_Knowledge_v2")
    where = (
        Filter.by_property("canonical_source").equal(canonical_source)
        & Filter.by_property("source_path").equal(source_path)
        & Filter.by_property("content_hash").equal(content_hash)
        & Filter.by_property("chunk_index").equal(chunk_index)
    )
    response = v2.query.fetch_objects(filters=where, limit=1)
    return len(response.objects) > 0


def map_v1_to_v2_props(
    v1_props: dict,
    *,
    batch_lineage_id: str,
    embedding_model: str,
) -> dict:
    """Project a v1 chunk into the 14 v2 properties with defaults.

    A v1 chunk is missing the 6 F.5 fields by definition, so we synthesise
    sensible defaults that mark it as a legacy-migration chunk.
    """
    return {
        # 8 carried over (some may be missing if v1 was looser — None propagates)
        "content": v1_props.get("content"),
        "title": v1_props.get("title"),
        "source_path": v1_props.get("source_path") or "",
        "source_type": v1_props.get("source_type"),
        "truth_level": v1_props.get("truth_level"),
        "namespace": v1_props.get("namespace"),
        "chunk_index": v1_props.get("chunk_index", 0),
        "content_hash": v1_props.get("content_hash") or "",
        # 6 F.5 fields — synthesised
        "canonical_source": "legacy-rag-knowledge",
        "source_layer": "knowledge",
        "source_commit": v1_props.get("source_commit"),  # best-effort, often None
        "lineage_id": batch_lineage_id,
        "embedding_model": embedding_model,
        "origin_batch_kind": "legacy_migration",
    }


def migrate(*, apply: bool, batch_size: int, limit: Optional[int]) -> dict:
    """Run the migration. Returns counters."""
    from app.config import get_settings
    settings = get_settings()

    try:
        from app.services.weaviate_client import WeaviateClient
    except ImportError as exc:
        logger.error("F.5 migrate: cannot import WeaviateClient (%s)", exc)
        sys.exit(EXIT_RUNTIME_ERROR)

    wc = WeaviateClient()
    client = wc.client

    if not client.collections.exists("KB_Knowledge_v2"):
        logger.error(
            "F.5 migrate: KB_Knowledge_v2 missing — create it first via "
            "`from app.services.weaviate_v2_schema import create_kb_knowledge_v2`"
        )
        sys.exit(EXIT_TARGET_MISSING)

    if not client.collections.exists("KB_Knowledge"):
        logger.warning("F.5 migrate: KB_Knowledge (v1) does not exist — nothing to do")
        return {"imported": 0, "skipped_idempotent": 0, "errors": 0, "v2_count_after": 0}

    batch_lineage_id = str(uuid.uuid4())  # one UUID for THIS migration run
    embedding_model = settings.embedding_model

    counters = {"imported": 0, "skipped_idempotent": 0, "errors": 0}
    v2 = client.collections.get("KB_Knowledge_v2")

    logger.info(
        "F.5 migrate: starting (apply=%s, batch_size=%d, limit=%s, lineage_id=%s)",
        apply, batch_size, limit, batch_lineage_id,
    )

    pending = []
    for record in iter_v1_chunks(client, limit=limit):
        v1_props = record["props"]
        target = map_v1_to_v2_props(
            v1_props,
            batch_lineage_id=batch_lineage_id,
            embedding_model=embedding_model,
        )

        # Idempotence by natural key
        if chunk_already_in_v2(
            client,
            canonical_source=target["canonical_source"],
            source_path=target["source_path"],
            content_hash=target["content_hash"],
            chunk_index=target["chunk_index"],
        ):
            counters["skipped_idempotent"] += 1
            continue

        if apply:
            pending.append(target)
            if len(pending) >= batch_size:
                _flush_batch(v2, pending, counters)
                pending = []
        else:
            counters["imported"] += 1  # would-be in dry-run

    if apply and pending:
        _flush_batch(v2, pending, counters)

    counters["v2_count_after"] = v2.aggregate.over_all(total_count=True).total_count
    logger.info("F.5 migrate: done — counters=%s", counters)
    return counters


def _flush_batch(v2_collection, batch: list[dict], counters: dict) -> None:
    """Write a batch to v2, updating counters."""
    try:
        with v2_collection.batch.dynamic() as b:
            for props in batch:
                b.add_object(properties=props)
        counters["imported"] += len(batch)
    except Exception as exc:  # pragma: no cover — defensive
        logger.error("F.5 migrate: batch write failed: %s", exc)
        counters["errors"] += len(batch)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Actually write to v2 (default: dry-run)")
    parser.add_argument("--batch-size", type=int, default=500)
    parser.add_argument("--limit", type=int, default=None, help="Stop after N v1 chunks (test mode)")
    args = parser.parse_args()

    if args.batch_size < 1 or args.batch_size > 5000:
        logger.error("F.5 migrate: --batch-size must be between 1 and 5000")
        return EXIT_USER_ERROR

    lock_fd = acquire_lock(LOCK_PATH)
    try:
        counters = migrate(apply=args.apply, batch_size=args.batch_size, limit=args.limit)
    finally:
        # Releases the lock when fd is closed (or on process exit)
        os.close(lock_fd)

    # Echo summary so CI / cron capture it
    print({"f5.migrate.summary": counters})
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
