#!/usr/bin/env python3
"""Ingest JSON/XML exports into structure profile + controlled snapshots.

Golden rule:
- Keep raw as source of truth (DB/files), not in vector index.
- Index only knowledge docs (structure/profile/rules) + optional snapshots.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

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


def infer_scalar_type(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        return "str"
    if isinstance(value, list):
        return "list"
    if isinstance(value, dict):
        return "object"
    return "unknown"


def flatten_json(obj: Any, prefix: str = "") -> dict[str, Any]:
    out: dict[str, Any] = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            nk = f"{prefix}.{k}" if prefix else str(k)
            out.update(flatten_json(v, nk))
    elif isinstance(obj, list):
        out[prefix or "$"] = f"list(len={len(obj)})"
        if obj and isinstance(obj[0], (dict, list)):
            out.update(flatten_json(obj[0], f"{prefix}[]"))
    else:
        out[prefix or "$"] = obj
    return out


def to_records_from_json(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return [r for r in payload if isinstance(r, dict)]
    if isinstance(payload, dict):
        # common export shape: {"data":[...]} or {"items":[...]}
        for key in ("data", "items", "results", "rows"):
            val = payload.get(key)
            if isinstance(val, list) and val and isinstance(val[0], dict):
                return [r for r in val if isinstance(r, dict)]
        return [payload]
    return []


def xml_element_to_dict(elem: ET.Element) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for k, v in elem.attrib.items():
        out[f"@{k}"] = v
    children = list(elem)
    if children:
        by_tag: dict[str, list[Any]] = {}
        for c in children:
            by_tag.setdefault(c.tag, []).append(xml_element_to_dict(c))
        for tag, vals in by_tag.items():
            out[tag] = vals[0] if len(vals) == 1 else vals
    text = (elem.text or "").strip()
    if text:
        out["#text"] = text
    return out


def to_records_from_xml(path: Path) -> list[dict[str, Any]]:
    root = ET.parse(path).getroot()
    # choose repeating child nodes when possible
    children = list(root)
    if children:
        tags = Counter(c.tag for c in children)
        main_tag, count = tags.most_common(1)[0]
        if count >= 2:
            return [xml_element_to_dict(c) for c in children if c.tag == main_tag]
    return [xml_element_to_dict(root)]


def profile_records(records: list[dict[str, Any]], sample_limit: int = 3000) -> dict[str, Any]:
    sample = records[:sample_limit]
    fields: dict[str, dict[str, Any]] = {}
    all_keys: set[str] = set()
    flat_rows: list[dict[str, Any]] = []
    for rec in sample:
        flat = flatten_json(rec)
        flat_rows.append(flat)
        all_keys.update(flat.keys())

    for key in sorted(all_keys):
        vals = [row.get(key) for row in flat_rows]
        types = Counter(infer_scalar_type(v) for v in vals)
        non_null = [v for v in vals if v is not None and v != ""]
        top_values = Counter(str(v) for v in non_null).most_common(5)
        null_ratio = 1.0 if not vals else (len(vals) - len(non_null)) / len(vals)
        anomalies: list[str] = []
        if null_ratio > 0.5:
            anomalies.append(f"high_null_ratio={null_ratio:.2f}")
        fields[key] = {
            "dominant_type": types.most_common(1)[0][0] if types else "unknown",
            "types": dict(types),
            "sample_non_null_count": len(non_null),
            "sample_distinct_count": len(set(str(v) for v in non_null)),
            "sample_top_values": top_values,
            "sample_null_ratio": round(null_ratio, 4),
            "anomalies": anomalies,
        }

    return {
        "records_total": len(records),
        "records_profiled": len(sample),
        "fields": fields,
        "field_count": len(fields),
    }


def detect_snapshot_key(profile_fields: dict[str, Any]) -> str | None:
    ordered = ["id", "product_id", "sku", "part_number", "reference", "code"]
    normalized = {normalize_key(k): k for k in profile_fields.keys()}
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
    if ext == ".json":
        records = to_records_from_json(src)
        source_type = "json"
    elif ext == ".xml":
        records = to_records_from_xml(src)
        source_type = "xml"
    else:
        raise ValueError("Unsupported input format. Use .json or .xml")

    profile = profile_records(records, sample_limit=args.profile_sample_rows)
    profile_fields = profile.get("fields", {})
    snapshot_key = args.snapshot_key or detect_snapshot_key(profile_fields)
    snapshots_enabled = bool(snapshot_key and args.snapshot_top_n > 0)
    index_raw = bool(args.index_raw)

    slug = normalize_key(src.stem) or "structured"
    profile_md_path = knowledge_root / "structured" / "profiles" / f"{slug}_structure_profile.md"
    snapshots_dir = knowledge_root / "structured" / "entity_snapshots" / slug

    lines = [
        f"# Structure Profile: {src.name}",
        "",
        "## Decision",
        "",
        "- index_knowledge: true",
        f"- index_snapshots: {str(snapshots_enabled).lower()}",
        f"- index_raw_data: {str(index_raw).lower()} (default=false recommended)",
        "",
        "## Overview",
        "",
        f"- source_type: {source_type}",
        f"- records_total: {profile['records_total']}",
        f"- records_profiled: {profile['records_profiled']}",
        f"- field_count: {profile['field_count']}",
        "",
        "## Fields",
        "",
    ]
    for field_name, fd in profile_fields.items():
        lines.append(f"### {field_name}")
        lines.append(f"- dominant_type: {fd['dominant_type']}")
        lines.append(f"- sample_non_null_count: {fd['sample_non_null_count']}")
        lines.append(f"- sample_distinct_count: {fd['sample_distinct_count']}")
        lines.append(f"- sample_null_ratio: {fd['sample_null_ratio']}")
        lines.append(f"- sample_top_values: {fd['sample_top_values']}")
        if fd.get("anomalies"):
            lines.append(f"- anomalies: {fd['anomalies']}")
        lines.append("")

    if args.dry_run:
        logger.info(
            "[DRY-RUN] source=%s records=%s snapshots_enabled=%s snapshot_key=%s",
            src.name,
            profile["records_total"],
            snapshots_enabled,
            snapshot_key,
        )
        return 0

    write_markdown_doc(
        path=profile_md_path,
        meta={
            "title": f"Structure profile {src.name}",
            "source_type": source_type,
            "category": "knowledge",
            "truth_level": args.profile_truth_level,
            "verification_status": "unverified",
            "source_uri": str(src),
            "source_ref": "structure_profile",
            "created_at": now_iso(),
            "updated_at": now_iso(),
        },
        body="\n".join(lines).strip() + "\n",
    )

    snapshot_count = 0
    if snapshots_enabled and snapshot_key:
        snapshots_dir.mkdir(parents=True, exist_ok=True)
        for i, rec in enumerate(records[: args.snapshot_top_n], start=1):
            flat = flatten_json(rec)
            entity = str(flat.get(snapshot_key, "")).strip()
            if not entity:
                continue
            entity_slug = normalize_key(entity) or f"row_{i}"
            json_path = snapshots_dir / f"{entity_slug}.json"
            md_path = snapshots_dir / f"{entity_slug}.md"

            json_path.write_text(json.dumps(rec, ensure_ascii=True, indent=2), encoding="utf-8")
            write_markdown_doc(
                path=md_path,
                meta={
                    "title": f"{src.stem} snapshot {entity}",
                    "source_type": source_type,
                    "category": "catalog",
                    "truth_level": args.snapshot_truth_level,
                    "verification_status": "unverified",
                    "source_uri": str(src),
                    "source_ref": f"record={i}",
                    "created_at": now_iso(),
                    "updated_at": now_iso(),
                },
                body=(
                    f"# Snapshot {entity}\n\n"
                    f"Source: {src.name}\n\n"
                    "```json\n"
                    + json.dumps(rec, ensure_ascii=True, indent=2)
                    + "\n```\n"
                ),
            )
            snapshot_count += 1

    append_jsonl(
        ingest_root / "logs" / "ingest_jobs.jsonl",
        {
            "event": "ingest_structured",
            "timestamp": now_iso(),
            "source": str(src),
            "source_type": source_type,
            "records_total": profile["records_total"],
            "profile_path": str(profile_md_path),
            "snapshots_enabled": snapshots_enabled,
            "snapshot_key": snapshot_key or "",
            "snapshot_count": snapshot_count,
            "index_raw_data": index_raw,
        },
    )

    logger.info(
        "Ingested structured source=%s profile=%s snapshots=%s key=%s",
        src.name,
        profile_md_path,
        snapshot_count,
        snapshot_key,
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest JSON/XML into structure profile + controlled snapshots")
    parser.add_argument("--input", required=True, help="JSON/XML path")
    parser.add_argument("--knowledge-path", help="Override knowledge root")
    parser.add_argument("--ingest-root", help="Override ingest root for logs")
    parser.add_argument("--profile-sample-rows", type=int, default=3000)
    parser.add_argument("--profile-truth-level", default="L3")
    parser.add_argument("--snapshot-truth-level", default="L3")
    parser.add_argument("--snapshot-key", help="Entity key field")
    parser.add_argument("--snapshot-top-n", type=int, default=200)
    parser.add_argument("--index-raw", action="store_true", help="Reserved flag. Raw indexing is discouraged.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    setup_logging(args.verbose)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
