#!/usr/bin/env python3
"""Fail-fast gate for eval report quality thresholds."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate eval report thresholds")
    parser.add_argument("--report", default="tests/eval_report_throttled_postfix3.json")
    parser.add_argument("--min-catalog-recall", type=float, default=0.90)
    parser.add_argument("--min-knowledge-recall", type=float, default=0.95)
    parser.add_argument("--min-diagnostic-recall", type=float, default=0.95)
    parser.add_argument("--max-no-evidence-rate", type=float, default=0.05)
    parser.add_argument("--min-satisfaction", type=float, default=0.90)
    args = parser.parse_args()

    path = Path(args.report)
    if not path.exists():
        raise SystemExit(f"Report not found: {path}")

    payload = json.loads(path.read_text(encoding="utf-8"))
    summary = payload.get("summary", {})
    recall = summary.get("recall_at_k_by_collection", {})

    checks = [
        ("KB_Catalog recall", float(recall.get("KB_Catalog", 0.0)), args.min_catalog_recall, ">="),
        ("KB_Knowledge recall", float(recall.get("KB_Knowledge", 0.0)), args.min_knowledge_recall, ">="),
        ("KB_Diagnostic recall", float(recall.get("KB_Diagnostic", 0.0)), args.min_diagnostic_recall, ">="),
        ("no_evidence_rate", float(summary.get("no_evidence_rate", 1.0)), args.max_no_evidence_rate, "<="),
        ("satisfaction", float(summary.get("satisfaction", 0.0)), args.min_satisfaction, ">="),
    ]

    failed = []
    for label, value, target, op in checks:
        ok = value >= target if op == ">=" else value <= target
        status = "OK" if ok else "FAIL"
        print(f"[{status}] {label}: {value:.4f} {op} {target:.4f}")
        if not ok:
            failed.append((label, value, op, target))

    if failed:
        print("\nGate failed:")
        for label, value, op, target in failed:
            print(f"- {label}: {value:.4f} (expected {op} {target:.4f})")
        return 1

    print("\nGate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

