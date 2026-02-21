#!/usr/bin/env python3
"""Ingest DB knowledge views (schema docs + fact snapshots) into corpus.

This script deliberately avoids indexing raw full DB dumps.
It builds:
- db/schema/db_schema_docs.md (knowledge, typically L2)
- db/entity_snapshots/*.json + *.md (catalog facts)
"""

import argparse
import hashlib
import json
import logging
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import get_settings  # noqa: E402


logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def sha1_text(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()  # noqa: S324


def slugify(value: str) -> str:
    txt = re.sub(r"[^a-zA-Z0-9_-]+", "-", value).strip("-").lower()
    return txt or "snapshot"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def detect_driver(db_url: str) -> str:
    u = (db_url or "").lower()
    if u.startswith("postgresql://") or u.startswith("postgres://"):
        return "postgres"
    if u.startswith("mysql://") or u.startswith("mysql+pymysql://"):
        return "mysql"
    raise ValueError("Unsupported DB URL. Use postgresql:// or mysql://")


def connect_db(db_url: str):
    driver = detect_driver(db_url)
    if driver == "postgres":
        try:
            import psycopg  # type: ignore
        except Exception as exc:  # noqa: BLE001
            raise RuntimeError("psycopg is required for PostgreSQL. pip install psycopg[binary]") from exc
        return psycopg.connect(db_url), driver
    try:
        import pymysql  # type: ignore
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError("pymysql is required for MySQL. pip install PyMySQL") from exc

    # Parse mysql://user:pass@host:port/db
    import urllib.parse

    parsed = urllib.parse.urlparse(db_url)
    return (
        pymysql.connect(
            host=parsed.hostname or "localhost",
            port=parsed.port or 3306,
            user=urllib.parse.unquote(parsed.username or ""),
            password=urllib.parse.unquote(parsed.password or ""),
            database=(parsed.path or "/").lstrip("/"),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        ),
        driver,
    )


POSTGRES_SCHEMA_QUERY = """
SELECT
  t.table_name,
  c.column_name,
  c.data_type,
  c.is_nullable,
  c.column_default
FROM information_schema.tables t
JOIN information_schema.columns c
  ON c.table_schema = t.table_schema
 AND c.table_name = t.table_name
WHERE t.table_schema = current_schema()
  AND t.table_type = 'BASE TABLE'
ORDER BY t.table_name, c.ordinal_position;
"""

POSTGRES_FK_QUERY = """
SELECT
  tc.table_name,
  kcu.column_name,
  ccu.table_name AS foreign_table_name,
  ccu.column_name AS foreign_column_name
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
 AND tc.table_schema = kcu.table_schema
JOIN information_schema.constraint_column_usage ccu
  ON ccu.constraint_name = tc.constraint_name
 AND ccu.table_schema = tc.table_schema
WHERE tc.constraint_type = 'FOREIGN KEY'
  AND tc.table_schema = current_schema()
ORDER BY tc.table_name, kcu.column_name;
"""

MYSQL_SCHEMA_QUERY = """
SELECT
  c.table_name,
  c.column_name,
  c.data_type,
  c.is_nullable,
  c.column_default
FROM information_schema.columns c
WHERE c.table_schema = DATABASE()
ORDER BY c.table_name, c.ordinal_position;
"""

MYSQL_FK_QUERY = """
SELECT
  k.table_name,
  k.column_name,
  k.referenced_table_name AS foreign_table_name,
  k.referenced_column_name AS foreign_column_name
FROM information_schema.key_column_usage k
WHERE k.table_schema = DATABASE()
  AND k.referenced_table_name IS NOT NULL
ORDER BY k.table_name, k.column_name;
"""


def query_rows(conn, sql: str, params: tuple | None = None) -> list[dict[str, Any]]:
    params = params or ()
    cur = conn.cursor()
    try:
        cur.execute(sql, params)
        rows = cur.fetchall()
    finally:
        cur.close()

    # psycopg default row tuple -> map with description
    if rows and not isinstance(rows[0], dict):
        # For tuple rows, rebuild dicts
        cols = []
        cur2 = conn.cursor()
        try:
            cur2.execute(sql, params)
            cols = [d[0] for d in (cur2.description or [])]
            tup_rows = cur2.fetchall()
        finally:
            cur2.close()
        rows = [dict(zip(cols, r)) for r in tup_rows]
    return [dict(r) for r in rows]


def build_schema_markdown(schema_rows: list[dict[str, Any]], fk_rows: list[dict[str, Any]], provider: str) -> str:
    by_table: dict[str, list[dict[str, Any]]] = {}
    for r in schema_rows:
        by_table.setdefault(str(r.get("table_name", "")), []).append(r)
    by_fk: dict[str, list[dict[str, Any]]] = {}
    for r in fk_rows:
        by_fk.setdefault(str(r.get("table_name", "")), []).append(r)

    lines = [
        "# DB Schema Documentation",
        "",
        f"Provider: {provider}",
        "",
        "## Tables",
        "",
    ]
    for table in sorted(by_table.keys()):
        lines.append(f"### {table}")
        lines.append("")
        lines.append("| Column | Type | Nullable | Default |")
        lines.append("| --- | --- | --- | --- |")
        for c in by_table[table]:
            lines.append(
                "| {col} | {typ} | {nul} | {dft} |".format(
                    col=str(c.get("column_name", "")),
                    typ=str(c.get("data_type", "")),
                    nul=str(c.get("is_nullable", "")),
                    dft=str(c.get("column_default", "")),
                )
            )
        fks = by_fk.get(table, [])
        if fks:
            lines.append("")
            lines.append("Foreign keys:")
            for fk in fks:
                lines.append(
                    "- {col} -> {ft}.{fc}".format(
                        col=str(fk.get("column_name", "")),
                        ft=str(fk.get("foreign_table_name", "")),
                        fc=str(fk.get("foreign_column_name", "")),
                    )
                )
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def write_markdown_doc(
    path: Path,
    title: str,
    content: str,
    source_type: str,
    category: str,
    truth_level: str,
    source_uri: str,
    source_ref: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    meta = {
        "title": title,
        "source_type": source_type,
        "category": category,
        "truth_level": truth_level,
        "verification_status": "unverified",
        "source_uri": source_uri,
        "source_ref": source_ref,
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }
    payload = "---\n" + yaml.safe_dump(meta, allow_unicode=False, sort_keys=False).strip() + "\n---\n\n" + content
    path.write_text(payload, encoding="utf-8")


def parse_fact_query(spec: str) -> tuple[str, str, str]:
    # format: name::id_col::SQL
    parts = spec.split("::", 2)
    if len(parts) != 3:
        raise ValueError("Invalid --fact-query format. Use name::id_col::SQL")
    name, id_col, sql = parts
    name = name.strip()
    id_col = id_col.strip()
    sql = sql.strip()
    if not name or not id_col or not sql:
        raise ValueError("Invalid --fact-query format. Empty name/id_col/sql.")
    return name, id_col, sql


def run(args: argparse.Namespace) -> int:
    settings = get_settings()
    if not settings.can_write() and not args.dry_run:
        logger.error("Write operations are blocked in this environment (set ENV=dev/ci/staging).")
        return 1

    db_url = args.db_url or os.environ.get("DB_URL", "")
    if not db_url:
        logger.error("Missing DB URL. Use --db-url or DB_URL env var.")
        return 1

    source_uri = f"db:{args.provider}"
    knowledge_root = Path(args.knowledge_path or settings.knowledge_path).resolve()
    schema_md_path = knowledge_root / "db" / "schema" / "db_schema_docs.md"
    snapshots_dir = knowledge_root / "db" / "entity_snapshots"

    try:
        conn, driver = connect_db(db_url)
    except Exception as exc:  # noqa: BLE001
        logger.error(f"DB connection failed: {exc}")
        return 1

    created = 0
    failed = 0
    query_count = 0

    try:
        # A) Schema docs (L2 by default)
        schema_q = POSTGRES_SCHEMA_QUERY if driver == "postgres" else MYSQL_SCHEMA_QUERY
        fk_q = POSTGRES_FK_QUERY if driver == "postgres" else MYSQL_FK_QUERY
        schema_rows = query_rows(conn, schema_q)
        fk_rows = query_rows(conn, fk_q)
        schema_md = build_schema_markdown(schema_rows, fk_rows, args.provider)

        if args.dry_run:
            logger.info(f"[DRY-RUN] schema rows={len(schema_rows)} fk_rows={len(fk_rows)}")
        else:
            write_markdown_doc(
                path=schema_md_path,
                title="DB Schema Documentation",
                content=schema_md,
                source_type="guide",
                category="knowledge",
                truth_level=args.schema_truth_level,
                source_uri=source_uri,
                source_ref="table=*",
            )
            created += 1

        # B) Fact snapshots (catalog)
        fact_specs = args.fact_query or []
        for spec in fact_specs:
            name, id_col, sql = parse_fact_query(spec)
            qhash = sha1_text(sql)[:12]
            try:
                rows = query_rows(conn, sql)
            except Exception as exc:  # noqa: BLE001
                if args.skip_query_errors:
                    logger.warning(f"Fact query '{name}' skipped: {exc}")
                    continue
                raise
            query_count += 1

            for row in rows:
                rid = str(row.get(id_col, "")).strip()
                if not rid:
                    rid = sha1_text(json.dumps(row, sort_keys=True, ensure_ascii=True))[:10]
                slug = slugify(f"{name}-{rid}")
                json_path = snapshots_dir / f"{slug}.json"
                md_path = snapshots_dir / f"{slug}.md"
                source_ref = f"table={name} row_id={rid} query_hash={qhash}"

                if args.dry_run:
                    continue

                snapshots_dir.mkdir(parents=True, exist_ok=True)
                json_path.write_text(json.dumps(row, ensure_ascii=True, indent=2), encoding="utf-8")

                md_body = "\n".join(
                    [
                        "## Entity Snapshot",
                        "",
                        f"- Table/View: {name}",
                        f"- Row ID: {rid}",
                        f"- Query hash: {qhash}",
                        "",
                        "```json",
                        json.dumps(row, ensure_ascii=True, indent=2),
                        "```",
                        "",
                    ]
                )
                write_markdown_doc(
                    path=md_path,
                    title=f"{name} snapshot {rid}",
                    content=md_body,
                    source_type="gamme",
                    category="catalog",
                    truth_level=args.facts_truth_level,
                    source_uri=source_uri,
                    source_ref=source_ref,
                )
                created += 1

            logger.info(f"Fact query '{name}': rows={len(rows)}")

    except Exception as exc:  # noqa: BLE001
        failed += 1
        logger.error(f"Ingestion failed: {exc}")
    finally:
        conn.close()

    logger.info(
        f"Done. created={created}, failed={failed}, fact_queries={query_count}, dry_run={args.dry_run}"
    )
    return 0 if failed == 0 else 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest DB schema docs and fact snapshots")
    parser.add_argument("--db-url", help="DB URL (postgresql://... or mysql://...)")
    parser.add_argument("--provider", default="supabase", help="Provider name for source_uri db:<provider>")
    parser.add_argument(
        "--schema-truth-level",
        default="L2",
        choices=["L1", "L2", "L3", "L4"],
        help="Truth level for schema docs",
    )
    parser.add_argument(
        "--facts-truth-level",
        default="L3",
        choices=["L1", "L2", "L3", "L4"],
        help="Truth level for facts snapshots",
    )
    parser.add_argument(
        "--fact-query",
        action="append",
        help="Fact query spec: name::id_col::SQL (repeatable)",
    )
    parser.add_argument(
        "--skip-query-errors",
        action="store_true",
        help="Continue even if a fact query fails (missing table/column, etc.)",
    )
    parser.add_argument("--knowledge-path", help="Override knowledge path")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logs")
    args = parser.parse_args()

    setup_logging(args.verbose)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
