#!/usr/bin/env python3
"""Select top storyboard shots for fast video editing.

Reads storyboard CSV and outputs a filtered CSV with the best visual shots.

Usage:
  python scripts/select_top_shots.py \
    --input /opt/automecanik/rag/pdf-images/storyboard/storyboard.csv \
    --output /opt/automecanik/rag/pdf-images/storyboard/shots_selected.csv
"""

import argparse
import csv
from pathlib import Path


def to_int(value: str, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return default


def select_rows(rows: list[dict], min_score: int, max_per_doc: int) -> list[dict]:
    # Keep rows above score threshold first.
    filtered = [r for r in rows if to_int(r.get("visual_score", "0")) >= min_score]

    # Sort by document, then score desc, then page asc.
    filtered.sort(
        key=lambda r: (
            r.get("doc_slug", ""),
            -to_int(r.get("visual_score", "0")),
            to_int(r.get("page", "0")),
            to_int(r.get("index_on_page", "0")),
        )
    )

    # Cap per document for editability.
    selected = []
    per_doc_count: dict[str, int] = {}
    for row in filtered:
        slug = row.get("doc_slug", "")
        count = per_doc_count.get(slug, 0)
        if count >= max_per_doc:
            continue
        per_doc_count[slug] = count + 1
        selected.append(row)
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description="Select top storyboard shots")
    parser.add_argument("--input", required=True, help="Input storyboard CSV")
    parser.add_argument("--output", required=True, help="Output selected CSV")
    parser.add_argument("--min-score", type=int, default=70, help="Minimum visual score")
    parser.add_argument("--max-per-doc", type=int, default=20, help="Max selected shots per document")
    args = parser.parse_args()

    input_csv = Path(args.input).resolve()
    output_csv = Path(args.output).resolve()
    output_csv.parent.mkdir(parents=True, exist_ok=True)

    with input_csv.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    selected = select_rows(rows, min_score=args.min_score, max_per_doc=args.max_per_doc)

    if not selected:
        # keep header if available
        fieldnames = reader.fieldnames or []
        with output_csv.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if fieldnames:
                writer.writeheader()
        return 0

    fieldnames = list(selected[0].keys())
    with output_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(selected)

    print(f"selected={len(selected)} output={output_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
