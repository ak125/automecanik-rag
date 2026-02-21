#!/usr/bin/env python3
"""Ingest log files into knowledge corpus — profile + error patterns only.

Ultra Rule: NEVER index raw log lines.
Only index: error profiles, unique patterns, incident timelines.

Usage:
  ENV=dev python scripts/ingest_logs.py --input /path/to/logs
  ENV=dev python scripts/ingest_logs.py --input /path/to/logs --dry-run
"""

import argparse
import logging
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import get_settings  # noqa: E402
from app.services.knowledge_service import get_knowledge_service  # noqa: E402

logger = logging.getLogger(__name__)
LOG_EXTS = {".log", ".txt", ".out", ".err"}

# Common log patterns
TIMESTAMP_PATTERNS = [
    re.compile(r"(\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2})"),
    re.compile(r"(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})"),
    re.compile(r"(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})"),
]
ERROR_PATTERNS = [
    re.compile(r"\b(ERROR|FATAL|CRITICAL|SEVERE|PANIC)\b", re.IGNORECASE),
    re.compile(r"\b(Exception|Traceback|Error:)\b"),
    re.compile(r"\b(WARN|WARNING)\b", re.IGNORECASE),
]


def setup_logging(verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def _normalize_pattern(line: str) -> str:
    """Normalize log line to extract reusable pattern (remove numbers, hashes, IPs)."""
    s = re.sub(r"\b\d+\b", "N", line)
    s = re.sub(r"\b[0-9a-f]{8,}\b", "HASH", s, flags=re.IGNORECASE)
    s = re.sub(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "IP", s)
    return s.strip()[:150]


def extract_log_profile(content: str, filename: str) -> dict:
    """Extract statistical profile from log content. Never returns raw lines."""
    lines = content.splitlines()
    total = len(lines)

    severity_counts: Counter = Counter()
    error_lines: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        for pat in ERROR_PATTERNS:
            m = pat.search(line)
            if m:
                severity = m.group(1).upper()
                severity_counts[severity] += 1
                if severity in ("ERROR", "FATAL", "CRITICAL", "SEVERE", "PANIC"):
                    error_lines.append((i, line.strip()[:200]))
                break

    # Deduplicate error patterns
    pattern_counter: Counter = Counter()
    for _, line in error_lines:
        pattern_counter[_normalize_pattern(line)] += 1

    # Time range from first and last line
    first_ts, last_ts = None, None
    boundary_lines = []
    if lines:
        boundary_lines.append(lines[0])
    if len(lines) > 1:
        boundary_lines.append(lines[-1])
    for line in boundary_lines:
        for pat in TIMESTAMP_PATTERNS:
            m = pat.search(line)
            if m:
                if first_ts is None:
                    first_ts = m.group(1)
                last_ts = m.group(1)
                break

    return {
        "filename": filename,
        "total_lines": total,
        "severity_counts": dict(severity_counts),
        "unique_error_patterns": pattern_counter.most_common(50),
        "error_count": sum(
            severity_counts.get(s, 0)
            for s in ("ERROR", "FATAL", "CRITICAL", "SEVERE", "PANIC")
        ),
        "warning_count": severity_counts.get("WARN", 0) + severity_counts.get("WARNING", 0),
        "time_range": {"first": first_ts, "last": last_ts},
        "sample_errors": [line for _, line in error_lines[:20]],
    }


def render_profile_markdown(profile: dict) -> str:
    """Render log profile as markdown document (no raw lines)."""
    lines = [
        f"# Log Profile: {profile['filename']}",
        "",
        f"**Lines:** {profile['total_lines']}",
        f"**Errors:** {profile['error_count']} | **Warnings:** {profile['warning_count']}",
        f"**Period:** {profile['time_range']['first'] or '?'} to {profile['time_range']['last'] or '?'}",
        "",
        "## Severity Distribution",
    ]
    for sev, count in sorted(profile["severity_counts"].items(), key=lambda x: -x[1]):
        lines.append(f"- {sev}: {count}")

    if profile["unique_error_patterns"]:
        lines.extend(["", "## Top Error Patterns"])
        for pattern, count in profile["unique_error_patterns"][:30]:
            lines.append(f"- `{pattern}` (x{count})")

    if profile["sample_errors"]:
        lines.extend(["", "## Sample Errors (first 10)"])
        for err in profile["sample_errors"][:10]:
            lines.append(f"- {err}")

    return "\n".join(lines)


def run(args: argparse.Namespace) -> int:
    settings = get_settings()
    if not settings.can_write() and not args.dry_run:
        logger.error("Write blocked (set ENV=dev)")
        return 1

    input_dir = Path(args.input).resolve()
    if not input_dir.exists() or not input_dir.is_dir():
        logger.error(f"Input directory not found: {input_dir}")
        return 1

    log_files = sorted(
        f for f in input_dir.rglob("*")
        if f.is_file() and f.suffix.lower() in LOG_EXTS
    )

    if not log_files:
        logger.warning(f"No log files found under: {input_dir}")
        return 0

    service = get_knowledge_service()
    created = 0
    failed = 0

    logger.info(f"Found {len(log_files)} log file(s)")
    for log_path in log_files:
        rel_name = log_path.relative_to(input_dir)
        try:
            content = log_path.read_text(encoding="utf-8", errors="replace")
            profile = extract_log_profile(content, rel_name.as_posix())
            md = render_profile_markdown(profile)

            if args.dry_run:
                logger.info(
                    f"[DRY-RUN] {rel_name} -> errors={profile['error_count']} "
                    f"patterns={len(profile['unique_error_patterns'])}"
                )
                continue

            doc = service.create_document(
                title=f"Log profile: {rel_name.stem}",
                content=md,
                source_type="diagnostic",
                category="auto",
                truth_level="L4",
                source_uri=f"log://{rel_name.as_posix()}",
            )
            if doc:
                created += 1
                logger.info(f"Ingested {rel_name} -> {doc.source_path}")
            else:
                failed += 1
                logger.error(f"Failed to create doc for {rel_name}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            logger.error(f"Failed to ingest {rel_name}: {exc}")

    logger.info(f"Done. created={created}, failed={failed}, total={len(log_files)}")
    return 0 if failed == 0 else 2


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ingest log files into RAG corpus (profiles + patterns only)"
    )
    parser.add_argument("--input", required=True, help="Directory containing log files")
    parser.add_argument(
        "--truth-level",
        default="L4",
        choices=["L1", "L2", "L3", "L4"],
        help="Truth level (default L4 = heuristic)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logs")
    args = parser.parse_args()

    setup_logging(args.verbose)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
