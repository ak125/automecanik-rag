#!/usr/bin/env python3
"""Translate markdown corpus files from English to French using Anthropic.

Features:
- Keeps YAML frontmatter
- Preserves markdown structure
- Adds metadata: locale=fr, translated_from, translated_at

Usage:
  ENV=dev ANTHROPIC_API_KEY=... python scripts/translate_md_en_to_fr.py --input /knowledge/diagnostic
  ENV=dev ANTHROPIC_API_KEY=... python scripts/translate_md_en_to_fr.py --input /knowledge --suffix -fr
  ENV=dev ANTHROPIC_API_KEY=... python scripts/translate_md_en_to_fr.py --input /knowledge --dry-run
"""

import argparse
import logging
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import frontmatter
from anthropic import Anthropic


logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def list_markdown_files(input_path: Path) -> list[Path]:
    if input_path.is_file() and input_path.suffix.lower() == ".md":
        return [input_path]
    if input_path.is_dir():
        return sorted(input_path.rglob("*.md"))
    return []


def looks_english(text: str) -> bool:
    """Lightweight heuristic to avoid re-translating French files."""
    sample = text[:4000].lower()
    english_markers = [
        r"\bthe\b", r"\band\b", r"\bwith\b", r"\bbrake\b", r"\bvehicle\b",
        r"\bcheck\b", r"\binstallation\b", r"\bguide\b", r"\bmanual\b",
    ]
    french_markers = [
        r"\ble\b", r"\bla\b", r"\bavec\b", r"\bfrein\b", r"\bv[ée]hicule\b",
        r"\bcontr[ôo]le\b", r"\bguide\b", r"\bmanuel\b",
    ]
    en = sum(1 for p in english_markers if re.search(p, sample))
    fr = sum(1 for p in french_markers if re.search(p, sample))
    return en >= fr


def translate_markdown(client: Anthropic, model: str, content: str) -> str:
    prompt = (
        "Translate the following markdown content from English to French.\n"
        "Rules:\n"
        "- Keep markdown structure exactly (headings, lists, tables, code blocks).\n"
        "- Keep part numbers, references, units, and product names unchanged.\n"
        "- Use clear technical automotive French.\n"
        "- Return ONLY translated markdown body text.\n\n"
        "CONTENT:\n"
        f"{content}"
    )

    response = client.messages.create(
        model=model,
        max_tokens=4096,
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Translate markdown files EN->FR")
    parser.add_argument("--input", required=True, help="Input .md file or directory")
    parser.add_argument("--suffix", default="-fr", help="Suffix for translated filename (default: -fr)")
    parser.add_argument("--model", default=os.getenv("TRANSLATE_MODEL", "claude-3-5-haiku-20241022"))
    parser.add_argument("--dry-run", action="store_true", help="Only show what would be translated")
    parser.add_argument("--force", action="store_true", help="Translate even if file does not look English")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    setup_logging(args.verbose)

    api_key = os.getenv("ANTHROPIC_API_KEY", "")
    if not api_key and not args.dry_run:
        logger.error("ANTHROPIC_API_KEY is required unless --dry-run is used")
        return 1

    input_path = Path(args.input).resolve()
    files = list_markdown_files(input_path)
    if not files:
        logger.error(f"No markdown files found: {input_path}")
        return 1

    client = Anthropic(api_key=api_key) if not args.dry_run else None
    translated = 0
    skipped = 0
    failed = 0

    for src in files:
        if src.name.endswith(f"{args.suffix}.md"):
            skipped += 1
            continue

        try:
            post = frontmatter.load(src)
            body = post.content.strip()
            if not body:
                skipped += 1
                continue

            if not args.force and not looks_english(body):
                logger.info(f"Skip (not english): {src}")
                skipped += 1
                continue

            dst = src.with_name(f"{src.stem}{args.suffix}.md")
            if args.dry_run:
                logger.info(f"[DRY-RUN] {src} -> {dst}")
                translated += 1
                continue

            translated_body = translate_markdown(client, args.model, body)
            out = frontmatter.Post(translated_body)
            out.metadata = dict(post.metadata)
            out.metadata["locale"] = "fr"
            out.metadata["translated_from"] = str(src.name)
            out.metadata["translated_at"] = datetime.now(timezone.utc).isoformat()

            dst.write_text(frontmatter.dumps(out), encoding="utf-8")
            logger.info(f"Translated: {src} -> {dst}")
            translated += 1
        except Exception as exc:  # noqa: BLE001
            failed += 1
            logger.error(f"Failed: {src}: {exc}")

    logger.info(f"Done. translated={translated}, skipped={skipped}, failed={failed}")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
