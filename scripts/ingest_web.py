#!/usr/bin/env python3
"""Ingest web URLs into clean markdown corpus for RAG.

Pipeline:
- fetch URL HTML and archive immutable raw.html
- readable extraction (remove nav/footer/scripts/noise)
- markdown normalization (H1/H2/H3, paragraphs, lists, tables)
- section splitting with provenance url#section=...&line=...
- write markdown docs under /knowledge/web and /knowledge/web-catalog
"""

import argparse
import hashlib
import html
import json
import logging
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import get_settings  # noqa: E402


logger = logging.getLogger(__name__)

NOISE_BLOCK_RE = re.compile(
    r"<(script|style|noscript|svg|canvas|iframe|nav|footer|header|aside|form)[^>]*>.*?</\1>",
    flags=re.IGNORECASE | re.DOTALL,
)
COMMENT_RE = re.compile(r"<!--.*?-->", flags=re.DOTALL)
TABLE_RE = re.compile(r"<table[^>]*>.*?</table>", flags=re.IGNORECASE | re.DOTALL)
ROW_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", flags=re.IGNORECASE | re.DOTALL)
CELL_RE = re.compile(r"<t[hd][^>]*>(.*?)</t[hd]>", flags=re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>", flags=re.DOTALL)
TOKEN_RE = re.compile(
    r"(?is)"
    r"(<h1[^>]*>.*?</h1>|<h2[^>]*>.*?</h2>|<h3[^>]*>.*?</h3>|"
    r"<p[^>]*>.*?</p>|<li[^>]*>.*?</li>|<table[^>]*>.*?</table>)"
)


def setup_logging(verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def slugify(value: str) -> str:
    lowered = normalize_space(value).lower()
    lowered = re.sub(r"[^a-z0-9\s-]", "", lowered)
    lowered = re.sub(r"[\s-]+", "-", lowered).strip("-")
    return lowered or "section"


def strip_tags(fragment: str) -> str:
    text = TAG_RE.sub(" ", fragment or "")
    text = html.unescape(text)
    return normalize_space(text)


def extract_title(raw_html: str, fallback: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", raw_html, flags=re.IGNORECASE | re.DOTALL)
    if m:
        title = strip_tags(m.group(1))
        if title:
            return title
    return fallback


def clean_html(raw_html: str) -> str:
    out = COMMENT_RE.sub(" ", raw_html)
    out = NOISE_BLOCK_RE.sub(" ", out)
    return out


def table_to_markdown(table_html: str) -> str:
    rows = []
    for row_html in ROW_RE.findall(table_html):
        cells = [strip_tags(c) for c in CELL_RE.findall(row_html)]
        cells = [c for c in cells if c]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    header = rows[0]
    sep = ["---"] * width
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(sep) + " |",
    ]
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def html_to_markdown(raw_html: str, page_title: str) -> str:
    body = clean_html(raw_html)
    tokens = TOKEN_RE.findall(body)
    lines = [f"# {page_title}", ""]

    for tok in tokens:
        lower = tok.lower()
        if lower.startswith("<h1"):
            text = strip_tags(tok)
            if text and text != page_title:
                lines.extend([f"# {text}", ""])
        elif lower.startswith("<h2"):
            text = strip_tags(tok)
            if text:
                lines.extend([f"## {text}", ""])
        elif lower.startswith("<h3"):
            text = strip_tags(tok)
            if text:
                lines.extend([f"### {text}", ""])
        elif lower.startswith("<p"):
            text = strip_tags(tok)
            if len(text) >= 2:
                lines.extend([text, ""])
        elif lower.startswith("<li"):
            text = strip_tags(tok)
            if text:
                lines.extend([f"- {text}", ""])
        elif lower.startswith("<table"):
            table_md = table_to_markdown(tok)
            if table_md:
                lines.extend([table_md, ""])

    content = "\n".join(lines)
    # collapse aggressive blank lines
    content = re.sub(r"\n{3,}", "\n\n", content).strip()
    return content


def split_sections(markdown: str) -> list[dict]:
    lines = markdown.splitlines()
    sections = []
    cur_title = "section-1"
    cur_lines = []
    section_idx = 0
    start_line = 1

    def flush(end_line: int) -> None:
        nonlocal section_idx, cur_title, cur_lines, start_line
        text = "\n".join(cur_lines).strip()
        if not text:
            return
        section_idx += 1
        sections.append(
            {
                "idx": section_idx,
                "title": cur_title,
                "slug": slugify(cur_title) or f"section-{section_idx}",
                "start_line": start_line,
                "end_line": end_line,
                "content": text,
            }
        )

    for i, line in enumerate(lines, start=1):
        if line.startswith("## ") or line.startswith("### "):
            if cur_lines:
                flush(i - 1)
            cur_title = line.lstrip("#").strip() or f"section-{section_idx + 1}"
            cur_lines = [line]
            start_line = i
        else:
            cur_lines.append(line)

    if cur_lines:
        flush(len(lines))
    return sections


def fetch_with_playwright(url: str, timeout_ms: int = 15000) -> str | None:
    """Fetch URL with JavaScript rendering via Playwright (optional).

    Returns rendered HTML or None if Playwright is not installed or fails.
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        logger.warning("Playwright not installed, falling back to static fetch")
        return None

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, wait_until="networkidle", timeout=timeout_ms)
            html_content = page.content()
            browser.close()
            return html_content
    except Exception as exc:  # noqa: BLE001
        logger.warning(f"Playwright render failed: {exc}")
        return None


def fetch_url(url: str, timeout: int, user_agent: str, render_js: bool = False) -> str:
    """Fetch URL content. Uses Playwright for JS rendering if --render-js is set."""
    if render_js:
        rendered = fetch_with_playwright(url, timeout_ms=timeout * 1000)
        if rendered:
            logger.info(f"Fetched {url} with Playwright JS rendering")
            return rendered
        logger.info("Playwright unavailable, falling back to static fetch")

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def classify_catalog(markdown: str, title: str) -> bool:
    text = f"{title}\n{markdown}".lower()
    terms = [
        "catalog",
        "catalogue",
        "gamme",
        "reference",
        "référence",
        "oem",
        "sku",
        "compatibil",
        "fitment",
        "prix",
        "tarif",
        "part number",
    ]
    score = sum(1 for t in terms if t in text)
    return score >= 3


def archive_raw_html(knowledge_root: Path, url: str, raw_html: str) -> tuple[Path, str]:
    digest = sha256_text(raw_html)
    raw_dir = knowledge_root / "_raw" / "web"
    raw_dir.mkdir(parents=True, exist_ok=True)

    raw_path = raw_dir / f"{digest}.html"
    if not raw_path.exists():
        raw_path.write_text(raw_html, encoding="utf-8")

    sidecar = raw_dir / f"{digest}.json"
    if not sidecar.exists():
        sidecar.write_text(
            json.dumps(
                {
                    "sha256": digest,
                    "url": url,
                    "fetched_at": datetime.now(timezone.utc).isoformat(),
                },
                ensure_ascii=True,
                indent=2,
            ),
            encoding="utf-8",
        )
    return raw_path, digest


def write_doc(
    out_dir: Path,
    title: str,
    content: str,
    source_type: str,
    category: str,
    truth_level: str,
    source_uri: str,
    url: str,
    page_hash: str,
    section_idx: int,
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    fname = f"{page_hash[:12]}-s{section_idx:03d}.md"
    path = out_dir / fname
    now = datetime.now(timezone.utc).isoformat()
    frontmatter = {
        "title": title,
        "source_type": source_type,
        "category": category,
        "truth_level": truth_level,
        "verification_status": "unverified",
        "source_uri": source_uri,
        "source_url": url,
        "created_at": now,
        "updated_at": now,
    }
    payload = "---\n" + yaml.safe_dump(frontmatter, allow_unicode=False, sort_keys=False).strip() + "\n---\n\n" + content.strip() + "\n"
    path.write_text(payload, encoding="utf-8")
    return path


def collect_urls(args: argparse.Namespace) -> list[str]:
    urls = []
    for u in args.url or []:
        txt = (u or "").strip()
        if txt:
            urls.append(txt)
    if args.urls_file:
        f = Path(args.urls_file).resolve()
        if f.exists():
            for line in f.read_text(encoding="utf-8").splitlines():
                txt = line.strip()
                if txt and not txt.startswith("#"):
                    urls.append(txt)
    dedup = []
    seen = set()
    for u in urls:
        if u not in seen:
            seen.add(u)
            dedup.append(u)
    return dedup


def run(args: argparse.Namespace) -> int:
    settings = get_settings()
    if not settings.can_write() and not args.dry_run:
        logger.error("Write operations are blocked in this environment (set ENV=dev/ci/staging).")
        return 1

    urls = collect_urls(args)
    if not urls:
        logger.warning("No URLs provided.")
        return 0

    knowledge_root = Path(args.knowledge_path or settings.knowledge_path).resolve()
    web_dir = knowledge_root / "web"
    catalog_dir = knowledge_root / "web-catalog"
    created = 0
    failed = 0

    for url in urls:
        try:
            parsed = urllib.parse.urlparse(url)
            if parsed.scheme not in {"http", "https"}:
                logger.warning(f"Skipping unsupported URL scheme: {url}")
                continue

            raw_html = fetch_url(
                url, timeout=args.timeout, user_agent=args.user_agent,
                render_js=args.render_js,
            )
            page_hash = sha256_text(url)
            page_title = extract_title(raw_html, fallback=parsed.netloc or "web page")
            markdown = html_to_markdown(raw_html, page_title)
            sections = split_sections(markdown)
            is_catalog = classify_catalog(markdown, page_title)

            if args.dry_run:
                logger.info(
                    f"[DRY-RUN] url={url} sections={len(sections)} catalog={is_catalog}"
                )
                continue

            _, raw_sha = archive_raw_html(knowledge_root, url, raw_html)
            out_dir = catalog_dir if is_catalog else web_dir
            source_type = "gamme" if is_catalog else "guide"
            category = "catalog" if is_catalog else "knowledge"

            for sec in sections:
                anchor = sec["slug"]
                sline = sec["start_line"]
                eline = sec["end_line"]
                source_uri = f"{url}#section={anchor}&line={sline}-{eline}"
                doc_title = f"{page_title} - {sec['title']}"
                write_doc(
                    out_dir=out_dir,
                    title=doc_title,
                    content=sec["content"],
                    source_type=source_type,
                    category=category,
                    truth_level=args.truth_level,
                    source_uri=source_uri,
                    url=url,
                    page_hash=page_hash,
                    section_idx=sec["idx"],
                )
                created += 1

            logger.info(
                f"Ingested url={url} sections={len(sections)} catalog={is_catalog} raw_sha256={raw_sha}"
            )
        except urllib.error.URLError as exc:
            failed += 1
            logger.error(f"Fetch failed for {url}: {exc}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            logger.error(f"Failed to ingest {url}: {exc}")

    logger.info(f"Done. created={created}, failed={failed}, total_urls={len(urls)}")
    return 0 if failed == 0 else 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest web pages into clean markdown corpus")
    parser.add_argument("--url", action="append", help="URL to ingest (repeatable)")
    parser.add_argument("--urls-file", help="Text file: one URL per line")
    parser.add_argument(
        "--truth-level",
        default="L3",
        choices=["L1", "L2", "L3", "L4"],
        help="Truth level for generated docs",
    )
    parser.add_argument("--knowledge-path", help="Override KNOWLEDGE_PATH")
    parser.add_argument("--timeout", type=int, default=30, help="Fetch timeout seconds")
    parser.add_argument(
        "--user-agent",
        default="AutoMecanikRAG-WebIngest/1.0 (+https://automecanik.com)",
        help="HTTP User-Agent header",
    )
    parser.add_argument("--render-js", action="store_true", help="Render JavaScript with Playwright before extraction")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logs")
    args = parser.parse_args()

    setup_logging(args.verbose)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
