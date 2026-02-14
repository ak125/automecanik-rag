#!/usr/bin/env python3
"""Ingest CSV/XLSX into knowledge profiles + optional controlled snapshots.

Golden rule:
- Never index raw rows by default.
- Always generate a dataset profile (KB_Knowledge target).
- Generate entity snapshots only when useful (KB_Catalog target).
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
from typing import Any

try:
    import yaml
except Exception:  # noqa: BLE001
    yaml = None

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from app.config import get_settings
except Exception:  # noqa: BLE001
    get_settings = None

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_key(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "_" for ch in value).strip("_")


def infer_type(value: str) -> str:
    v = (value or "").strip()
    if not v:
        return "null"
    low = v.lower()
    if low in {"true", "false", "yes", "no", "0", "1"}:
        return "bool"
    try:
        int(v)
        return "int"
    except Exception:  # noqa: BLE001
        pass
    try:
        float(v)
        return "float"
    except Exception:  # noqa: BLE001
        pass
    return "str"


def load_csv(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return [dict(r) for r in csv.DictReader(f)]


def load_xlsx(path: Path) -> list[dict[str, Any]]:
    try:
        import openpyxl  # type: ignore
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(
            "XLSX support requires openpyxl. Install with: pip install openpyxl"
        ) from exc

    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return []
    headers = [str(h).strip() if h is not None else "" for h in rows[0]]
    out: list[dict[str, Any]] = []
    for row in rows[1:]:
        rec: dict[str, Any] = {}
        for i, key in enumerate(headers):
            if not key:
                continue
            rec[key] = row[i] if i < len(row) else None
        out.append(rec)
    return out


def coerce_str(v: Any) -> str:
    return "" if v is None else str(v).strip()


def profile_rows(rows: list[dict[str, Any]], sample_limit: int = 5000) -> dict[str, Any]:
    sample = rows[:sample_limit]
    fields: dict[str, dict[str, Any]] = {}
    columns = sorted({k for r in sample for k in r.keys()})

    for col in columns:
        values = [coerce_str(r.get(col)) for r in sample]
        non_empty = [v for v in values if v != ""]
        type_counts = Counter(infer_type(v) for v in values)
        top_values = Counter(v for v in non_empty).most_common(5)
        null_ratio = 1.0 if not values else (len(values) - len(non_empty)) / len(values)

        numeric_values: list[float] = []
        for v in non_empty:
            try:
                numeric_values.append(float(v))
            except Exception:  # noqa: BLE001
                continue

        anomalies: list[str] = []
        if null_ratio > 0.5:
            anomalies.append(f"high_null_ratio={null_ratio:.2f}")
        if len(numeric_values) >= 10:
            sorted_vals = sorted(numeric_values)
            q1 = sorted_vals[len(sorted_vals) // 4]
            q3 = sorted_vals[(3 * len(sorted_vals)) // 4]
            iqr = q3 - q1
            if iqr > 0:
                lo = q1 - 1.5 * iqr
                hi = q3 + 1.5 * iqr
                outliers = sum(1 for x in sorted_vals if x < lo or x > hi)
                if outliers > 0:
                    anomalies.append(f"outliers={outliers}")

        fields[col] = {
            "types": dict(type_counts),
            "dominant_type": type_counts.most_common(1)[0][0] if type_counts else "unknown",
            "sample_non_null_count": len(non_empty),
            "sample_distinct_count": len(set(non_empty)),
            "sample_top_values": top_values,
            "sample_null_ratio": round(null_ratio, 4),
            "sample_median": round(median(numeric_values), 4) if numeric_values else None,
            "anomalies": anomalies,
        }

    relations = []
    id_cols = [c for c in columns if c.lower().endswith("_id") or c.lower() == "id"]
    for left in id_cols:
        left_set = {coerce_str(r.get(left)) for r in sample if coerce_str(r.get(left))}
        if not left_set:
            continue
        for right in columns:
            if left == right:
                continue
            right_set = {coerce_str(r.get(right)) for r in sample if coerce_str(r.get(right))}
            if right_set and left_set & right_set and len(left_set & right_set) >= min(10, len(left_set)):
                relations.append({"from": left, "to": right, "overlap": len(left_set & right_set)})

    return {
        "rows_total": len(rows),
        "rows_profiled": len(sample),
        "columns": columns,
        "fields": fields,
        "relations_detected": relations[:20],
    }


def detect_snapshot_key(columns: list[str]) -> str | None:
    ordered = [
        "product_id",
        "sku",
        "part_number",
        "gamme_id",
        "brand_id",
        "id",
    ]
    normalized = {normalize_key(c): c for c in columns}
    for key in ordered:
        if key in normalized:
            return normalized[key]
    return None


def write_markdown_doc(path: Path, meta: dict[str, Any], body: str) -> None:
    if yaml is None:
        raise RuntimeError("PyYAML is required to write markdown docs. Install with: pip install pyyaml")
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = "---\n" + yaml.safe_dump(meta, allow_unicode=False, sort_keys=False).strip() + "\n---\n\n" + body
    path.write_text(payload, encoding="utf-8")


def append_jsonl(path: Path, event: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=True) + "\n")


def run(args: argparse.Namespace) -> int:
    if args.knowledge_path:
        knowledge_root = Path(args.knowledge_path).resolve()
    elif os.getenv("KNOWLEDGE_PATH"):
        knowledge_root = Path(os.environ["KNOWLEDGE_PATH"]).resolve()
    elif get_settings is not None:
        knowledge_root = Path(get_settings().knowledge_path).resolve()
    else:
        knowledge_root = Path("/opt/automecanik/rag/knowledge").resolve()
    ingest_root = Path(args.ingest_root or "/opt/automecanik/rag/ingest").resolve()

    src = Path(args.input).resolve()
    ext = src.suffix.lower()
    if ext == ".csv":
        rows = load_csv(src)
        source_type = "csv"
    elif ext in {".xlsx", ".xlsm"}:
        rows = load_xlsx(src)
        source_type = "xlsx"
    else:
        raise ValueError("Unsupported input format. Use .csv or .xlsx")

    profile = profile_rows(rows, sample_limit=args.profile_sample_rows)
    columns = profile.get("columns", [])
    snapshot_key = args.snapshot_key or detect_snapshot_key(columns)
    snapshots_enabled = bool(snapshot_key and args.snapshot_top_n > 0)
    index_raw = bool(args.index_raw)

    dataset_slug = normalize_key(src.stem) or "dataset"
    profile_md_path = knowledge_root / "tabular" / "profiles" / f"{dataset_slug}_dataset_profile.md"
    snapshots_dir = knowledge_root / "tabular" / "entity_snapshots" / dataset_slug

    profile_lines = [
        f"# Dataset Profile: {src.name}",
        "",
        "## Decision",
        "",
        f"- index_knowledge: true",
        f"- index_snapshots: {str(snapshots_enabled).lower()}",
        f"- index_raw_data: {str(index_raw).lower()} (default=false recommended)",
        "",
        "## Overview",
        "",
        f"- source_type: {source_type}",
        f"- rows_total: {profile['rows_total']}",
        f"- rows_profiled: {profile['rows_profiled']}",
        "",
        "## Fields",
        "",
    ]
    for col in columns:
        fd = profile["fields"][col]
        profile_lines.append(f"### {col}")
        profile_lines.append(f"- dominant_type: {fd['dominant_type']}")
        profile_lines.append(f"- sample_non_null_count: {fd['sample_non_null_count']}")
        profile_lines.append(f"- sample_distinct_count: {fd['sample_distinct_count']}")
        profile_lines.append(f"- sample_null_ratio: {fd['sample_null_ratio']}")
        profile_lines.append(f"- sample_top_values: {fd['sample_top_values']}")
        if fd.get("anomalies"):
            profile_lines.append(f"- anomalies: {fd['anomalies']}")
        profile_lines.append("")

    if profile["relations_detected"]:
        profile_lines.append("## Relations Detected")
        profile_lines.append("")
        for rel in profile["relations_detected"]:
            profile_lines.append(
                f"- {rel['from']} -> {rel['to']} (overlap={rel['overlap']})"
            )
        profile_lines.append("")

    if args.dry_run:
        logger.info(
            "[DRY-RUN] dataset=%s rows=%s snapshots_enabled=%s snapshot_key=%s",
            src.name,
            profile["rows_total"],
            snapshots_enabled,
            snapshot_key,
        )
        return 0

    write_markdown_doc(
        path=profile_md_path,
        meta={
            "title": f"Dataset profile {src.name}",
            "source_type": source_type,
            "category": "knowledge",
            "truth_level": args.profile_truth_level,
            "verification_status": "unverified",
            "source_uri": str(src),
            "source_ref": "profile",
            "created_at": now_iso(),
            "updated_at": now_iso(),
        },
        body="\n".join(profile_lines).strip() + "\n",
    )

    snapshot_count = 0
    if snapshots_enabled and snapshot_key:
        snapshots_dir.mkdir(parents=True, exist_ok=True)
        for i, row in enumerate(rows[: args.snapshot_top_n], start=1):
            entity_id = coerce_str(row.get(snapshot_key))
            if not entity_id:
                continue
            slug = normalize_key(f"{entity_id}") or f"row_{i}"
            json_path = snapshots_dir / f"{slug}.json"
            md_path = snapshots_dir / f"{slug}.md"

            json_path.write_text(
                json.dumps(row, ensure_ascii=True, indent=2),
                encoding="utf-8",
            )
            write_markdown_doc(
                path=md_path,
                meta={
                    "title": f"{src.stem} snapshot {entity_id}",
                    "source_type": source_type,
                    "category": "catalog",
                    "truth_level": args.snapshot_truth_level,
                    "verification_status": "unverified",
                    "source_uri": str(src),
                    "source_ref": f"row={i}",
                    "created_at": now_iso(),
                    "updated_at": now_iso(),
                },
                body=(
                    f"# Snapshot {entity_id}\n\n"
                    f"Source: {src.name}\n\n"
                    "```json\n"
                    + json.dumps(row, ensure_ascii=True, indent=2)
                    + "\n```\n"
                ),
            )
            snapshot_count += 1

    append_jsonl(
        ingest_root / "logs" / "ingest_jobs.jsonl",
        {
            "event": "ingest_tabular",
            "timestamp": now_iso(),
            "source": str(src),
            "source_type": source_type,
            "rows_total": profile["rows_total"],
            "profile_path": str(profile_md_path),
            "snapshots_enabled": snapshots_enabled,
            "snapshot_key": snapshot_key or "",
            "snapshot_count": snapshot_count,
            "index_raw_data": index_raw,
        },
    )

    logger.info(
        "Ingested tabular source=%s profile=%s snapshots=%s key=%s",
        src.name,
        profile_md_path,
        snapshot_count,
        snapshot_key,
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest CSV/XLSX into profile + controlled snapshots")
    parser.add_argument("--input", required=True, help="CSV/XLSX path")
    parser.add_argument("--knowledge-path", help="Override knowledge root")
    parser.add_argument("--ingest-root", help="Override ingest root for logs")
    parser.add_argument("--profile-sample-rows", type=int, default=5000)
    parser.add_argument("--profile-truth-level", default="L3")
    parser.add_argument("--snapshot-truth-level", default="L3")
    parser.add_argument("--snapshot-key", help="Entity key column (e.g. sku, product_id)")
    parser.add_argument("--snapshot-top-n", type=int, default=200)
    parser.add_argument("--index-raw", action="store_true", help="Reserved flag. Raw indexing is discouraged.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    setup_logging(args.verbose)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
