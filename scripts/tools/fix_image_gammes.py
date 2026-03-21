#!/usr/bin/env python3
"""Fix misclassified image gammes in .prompt.md sidecars.

Lists images grouped by source_url to identify misclassifications,
then allows targeted correction by source_url or domain.

Usage:
    python fix_image_gammes.py --report              # Show current state
    python fix_image_gammes.py --fix-url URL GAMME   # Fix all images from URL
    python fix_image_gammes.py --fix-domain DOMAIN GAMME  # Fix all from domain
    python fix_image_gammes.py --reset-domain DOMAIN  # Reset gamme to null
"""

import argparse
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

KNOWLEDGE_PATH = os.getenv("KNOWLEDGE_PATH", "/opt/automecanik/rag/knowledge")


def scan_sidecars(img_dir: str) -> list[dict]:
    """Scan all .prompt.md sidecars and return their metadata."""
    sidecars = []
    for f in sorted(os.listdir(img_dir)):
        if not f.endswith(".prompt.md"):
            continue
        filepath = os.path.join(img_dir, f)
        try:
            content = Path(filepath).read_text(encoding="utf-8")
            if not content.startswith("---"):
                continue
            end = content.find("---", 3)
            if end == -1:
                continue
            fm = yaml.safe_load(content[3:end]) or {}
            sidecars.append({
                "file": f,
                "path": filepath,
                "hash": fm.get("hash", ""),
                "source_url": fm.get("source_url", ""),
                "current_gamme": fm.get("gamme"),
                "alt_text": fm.get("alt_text", ""),
                "content": content,
            })
        except Exception:
            continue
    return sidecars


def report(sidecars: list[dict]):
    """Print report grouped by source domain and URL."""
    by_domain: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for sc in sidecars:
        try:
            domain = urlparse(sc["source_url"]).hostname or "unknown"
        except Exception:
            domain = "unknown"
        by_domain[domain][sc["source_url"]].append(sc)

    print(f"\n{'='*80}")
    print(f"IMAGE GAMME REPORT — {len(sidecars)} sidecars")
    print(f"{'='*80}")

    for domain in sorted(by_domain.keys()):
        urls = by_domain[domain]
        total = sum(len(v) for v in urls.values())
        gammes = set()
        for url_images in urls.values():
            for sc in url_images:
                gammes.add(sc["current_gamme"] or "null")

        print(f"\n--- {domain} ({total} images, gammes: {', '.join(sorted(gammes))}) ---")
        for url in sorted(urls.keys()):
            images = urls[url]
            g = images[0]["current_gamme"] or "null"
            mixed = len(set(sc["current_gamme"] for sc in images)) > 1
            flag = " ⚠ MIXED" if mixed else ""
            print(f"  [{len(images):3d}] gamme={g:30s} {url}{flag}")


def fix_by_url(sidecars: list[dict], target_url: str, new_gamme: str, apply: bool) -> int:
    """Fix gamme for all images from a specific source_url."""
    count = 0
    for sc in sidecars:
        if sc["source_url"] != target_url:
            continue
        if sc["current_gamme"] == new_gamme:
            continue
        count += 1
        if apply:
            _update_gamme(sc, new_gamme)
    return count


def fix_by_domain(sidecars: list[dict], domain: str, new_gamme: str | None, apply: bool) -> int:
    """Fix gamme for all images from a domain."""
    count = 0
    for sc in sidecars:
        try:
            sc_domain = urlparse(sc["source_url"]).hostname or ""
        except Exception:
            continue
        if sc_domain != domain:
            continue
        target = new_gamme
        if target is None:
            # Reset to null
            if sc["current_gamme"] is not None:
                count += 1
                if apply:
                    _reset_gamme(sc)
        else:
            if sc["current_gamme"] != target:
                count += 1
                if apply:
                    _update_gamme(sc, target)
    return count


def _update_gamme(sc: dict, new_gamme: str):
    content = sc["content"]
    updated = re.sub(
        r'gamme:\s*(?:null|"[^"]*")',
        f'gamme: "{new_gamme}"',
        content,
    )
    if updated != content:
        Path(sc["path"]).write_text(updated, encoding="utf-8")


def _reset_gamme(sc: dict):
    content = sc["content"]
    updated = re.sub(
        r'gamme:\s*"[^"]*"',
        "gamme: null",
        content,
    )
    if updated != content:
        Path(sc["path"]).write_text(updated, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Fix image gamme classifications")
    parser.add_argument("--report", action="store_true", help="Show current state report")
    parser.add_argument("--fix-url", nargs=2, metavar=("URL", "GAMME"), help="Fix all images from URL")
    parser.add_argument("--fix-domain", nargs=2, metavar=("DOMAIN", "GAMME"), help="Fix all from domain")
    parser.add_argument("--reset-domain", metavar="DOMAIN", help="Reset all gammes from domain to null")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    parser.add_argument("--knowledge-path", default=KNOWLEDGE_PATH)
    args = parser.parse_args()

    img_dir = os.path.join(args.knowledge_path, "_raw", "web-images")
    if not os.path.isdir(img_dir):
        print(f"Error: {img_dir} not found")
        sys.exit(1)

    sidecars = scan_sidecars(img_dir)
    print(f"Scanned {len(sidecars)} .prompt.md sidecars")

    if args.report or not any([args.fix_url, args.fix_domain, args.reset_domain]):
        report(sidecars)
        return

    if args.fix_url:
        url, gamme = args.fix_url
        count = fix_by_url(sidecars, url, gamme, args.apply)
        action = "Fixed" if args.apply else "Would fix"
        print(f"{action} {count} sidecars for URL: {url} -> gamme: {gamme}")

    if args.fix_domain:
        domain, gamme = args.fix_domain
        count = fix_by_domain(sidecars, domain, gamme, args.apply)
        action = "Fixed" if args.apply else "Would fix"
        print(f"{action} {count} sidecars for domain: {domain} -> gamme: {gamme}")

    if args.reset_domain:
        count = fix_by_domain(sidecars, args.reset_domain, None, args.apply)
        action = "Reset" if args.apply else "Would reset"
        print(f"{action} {count} sidecars for domain: {args.reset_domain} -> gamme: null")

    if not args.apply:
        print("\n[DRY-RUN] Use --apply to write changes.")


if __name__ == "__main__":
    main()
