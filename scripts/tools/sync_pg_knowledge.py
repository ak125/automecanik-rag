#!/usr/bin/env python3
"""Sync filesystem knowledge docs → __rag_knowledge (PG via Supabase REST).

Scans /knowledge/, compares with PG, reports gaps.
Dry-run by default. Pass --commit to apply inserts.

Usage:
    python scripts/tools/sync_pg_knowledge.py --supabase-url URL --supabase-key KEY
    python scripts/tools/sync_pg_knowledge.py --commit --supabase-url URL --supabase-key KEY
"""

import argparse
import hashlib
import json
import logging
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import frontmatter
import requests

logger = logging.getLogger("sync_pg_knowledge")
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

# --- Constants ---

IGNORED_DIRS = {"_trash", "_raw", "__pycache__", "_quarantine"}

SKIP_PREFIXES = [
    "seo-data/",
    "structured/entity_snapshots/",
    "structured/profiles/",
    "tabular/entity_snapshots/",
    "tabular/profiles/",
]

SECTION_PATTERN = re.compile(r"-s\d+\.md$")


# --- Filesystem scanner ---


def iter_fs_docs(knowledge_path: str) -> List[Dict[str, Any]]:
    """Scan filesystem for .md docs, parse frontmatter, return list."""
    path = Path(knowledge_path)
    if not path.exists():
        logger.error(f"Knowledge path not found: {knowledge_path}")
        return []

    docs = []
    for md_file in sorted(path.rglob("*.md")):
        if md_file.name == "README.md" or ".backup" in str(md_file):
            continue
        rel_parts = md_file.relative_to(path).parts
        if any(part in IGNORED_DIRS for part in rel_parts):
            continue

        relative_path = str(md_file.relative_to(path))

        # Skip known non-business prefixes
        if any(relative_path.startswith(prefix) for prefix in SKIP_PREFIXES):
            continue

        try:
            post = frontmatter.load(str(md_file))
            meta = dict(post.metadata)
            content = post.content.strip()

            docs.append({
                "source": relative_path,
                "title": str(meta.get("title", md_file.stem)),
                "content": content,
                "truth_level": str(meta.get("truth_level", "L2")),
                "domain": str(meta.get("domain", meta.get("doc_family", ""))),
                "category": str(meta.get("category", "")),
            })
        except Exception as e:
            logger.warning(f"Failed to parse {relative_path}: {e}")

    return docs


def compute_fingerprint(content: str) -> str:
    """SHA-256 fingerprint matching RagCleanupService.computeFingerprint()."""
    normalized = re.sub(r"[^\w\s]", "", content.lower(), flags=re.UNICODE)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return hashlib.sha256(normalized.encode()).hexdigest()[:16]


# --- Supabase REST client ---


class SupabaseRest:
    """Minimal PostgREST client for __rag_knowledge."""

    def __init__(self, url: str, key: str):
        self.base = url.rstrip("/")
        self.headers = {
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "Prefer": "return=representation",
        }

    def get_pg_sources(self) -> Dict[str, str]:
        """Return {source: status} for all rows."""
        sources = {}
        offset = 0
        limit = 1000
        while True:
            resp = requests.get(
                f"{self.base}/rest/v1/__rag_knowledge",
                headers={**self.headers, "Range": f"{offset}-{offset + limit - 1}"},
                params={"select": "source,status"},
            )
            resp.raise_for_status()
            rows = resp.json()
            if not rows:
                break
            for row in rows:
                sources[row["source"]] = row["status"]
            if len(rows) < limit:
                break
            offset += limit
        return sources

    def insert_doc(self, doc: Dict[str, Any]) -> bool:
        """Insert a single doc into __rag_knowledge."""
        payload = {
            "title": doc["title"],
            "content": doc["content"],
            "source": doc["source"],
            "truth_level": doc["truth_level"],
            "domain": doc["domain"] or None,
            "category": doc["category"] or None,
            "status": "active",
            "retrievable": True,
            "fingerprint": compute_fingerprint(doc["content"]),
        }
        resp = requests.post(
            f"{self.base}/rest/v1/__rag_knowledge",
            headers={**self.headers, "Prefer": "return=minimal"},
            json=payload,
        )
        if resp.status_code in (200, 201):
            return True
        logger.error(f"INSERT failed for {doc['source']}: {resp.status_code} {resp.text}")
        return False


# --- Main logic ---


def find_gaps(
    fs_docs: List[Dict[str, Any]],
    pg_sources: Dict[str, str],
) -> List[Dict[str, Any]]:
    """Find filesystem docs not in PG (active or merged)."""
    gaps = []
    for doc in fs_docs:
        source = doc["source"]

        # Already in PG (any status)
        if source in pg_sources:
            continue

        # Section file whose parent is merged in PG
        if SECTION_PATTERN.search(source):
            parent = SECTION_PATTERN.sub("", source)
            if parent in pg_sources:
                continue
            # Also check without .md
            parent_no_ext = parent.replace(".md", "")
            if parent_no_ext in pg_sources:
                continue

        gaps.append(doc)

    return gaps


def main():
    parser = argparse.ArgumentParser(description="Sync filesystem → __rag_knowledge")
    parser.add_argument("--path", default=os.environ.get("KNOWLEDGE_PATH", "/knowledge"))
    parser.add_argument("--supabase-url", default=os.environ.get("SUPABASE_URL", ""))
    parser.add_argument("--supabase-key", default=os.environ.get("SUPABASE_SERVICE_ROLE_KEY", ""))
    parser.add_argument("--commit", action="store_true", help="Apply inserts (default: dry-run)")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    if not args.supabase_url or not args.supabase_key:
        logger.error("--supabase-url and --supabase-key are required (or set SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY)")
        sys.exit(1)

    # Step 1: Scan filesystem
    logger.info(f"Scanning filesystem: {args.path}")
    fs_docs = iter_fs_docs(args.path)
    logger.info(f"Filesystem: {len(fs_docs)} docs (after skip filters)")

    # Step 2: Load PG sources
    client = SupabaseRest(args.supabase_url, args.supabase_key)
    pg_sources = client.get_pg_sources()
    active_count = sum(1 for s in pg_sources.values() if s == "active")
    logger.info(f"PG: {len(pg_sources)} total rows, {active_count} active")

    # Step 3: Find gaps
    gaps = find_gaps(fs_docs, pg_sources)
    logger.info(f"Gap: {len(gaps)} docs on filesystem but not in PG")

    if args.verbose or gaps:
        for doc in gaps:
            logger.info(f"  MISSING: {doc['source']} [{doc['truth_level']}] {doc['title'][:60]}")

    # Step 4: Apply or report
    if not gaps:
        logger.info("No gaps found. Filesystem and PG are aligned.")
        return

    if not args.commit:
        logger.info(f"[DRY RUN] Would insert {len(gaps)} docs. Use --commit to apply.")
        return

    inserted = 0
    errors = 0
    for doc in gaps:
        if client.insert_doc(doc):
            inserted += 1
            logger.info(f"  INSERTED: {doc['source']}")
        else:
            errors += 1

    logger.info("=" * 50)
    logger.info(f"Sync complete: {inserted} inserted, {errors} errors")


if __name__ == "__main__":
    main()
