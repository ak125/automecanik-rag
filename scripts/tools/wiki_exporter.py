#!/usr/bin/env python3
"""
Wiki.js Exporter - Export wiki content for RAG ingestion.

Supports two modes:
1. Git sync: Clone/pull wiki backup repository
2. GraphQL API: Query Wiki.js GraphQL endpoint

Usage:
    python wiki_exporter.py --mode git [--repo URL] [--branch main]
    python wiki_exporter.py --mode graphql [--url URL]
"""

import argparse
import json
import logging
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import yaml

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("wiki_exporter")


def load_config() -> dict:
    """Load configuration from rag_config.yml."""
    config_path = Path(__file__).parent.parent / "rag_config.yml"
    if config_path.exists():
        with open(config_path) as f:
            return yaml.safe_load(f)
    return {}


class WikiExporter:
    """Export wiki content for RAG ingestion."""

    def __init__(
        self,
        export_path: str = "/opt/automecanik/rag/wiki_export",
        git_repo: Optional[str] = None,
        branch: str = "main",
        graphql_url: Optional[str] = None
    ):
        self.export_path = Path(export_path)
        self.git_repo = git_repo
        self.branch = branch
        self.graphql_url = graphql_url

        # Create export directory
        self.export_path.mkdir(parents=True, exist_ok=True)

    def export_via_git(self) -> dict:
        """
        Export wiki content via Git sync.

        Wiki.js can auto-commit to a Git repository.
        We clone/pull that repository to get the latest content.
        """
        if not self.git_repo:
            raise ValueError("Git repository URL is required for git mode")

        logger.info(f"Exporting wiki via Git: {self.git_repo}")

        git_dir = self.export_path / "git_repo"

        if git_dir.exists() and (git_dir / ".git").exists():
            # Pull latest changes
            logger.info("Pulling latest changes...")
            result = subprocess.run(
                ["git", "-C", str(git_dir), "pull", "origin", self.branch],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                logger.error(f"Git pull failed: {result.stderr}")
                raise RuntimeError(f"Git pull failed: {result.stderr}")
        else:
            # Clone repository
            logger.info("Cloning repository...")
            git_dir.mkdir(parents=True, exist_ok=True)
            result = subprocess.run(
                ["git", "clone", "--branch", self.branch, self.git_repo, str(git_dir)],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                logger.error(f"Git clone failed: {result.stderr}")
                raise RuntimeError(f"Git clone failed: {result.stderr}")

        # Collect markdown files
        md_files = list(git_dir.glob("**/*.md"))
        logger.info(f"Found {len(md_files)} markdown files")

        # Parse and collect documents
        documents = []
        for md_file in md_files:
            doc = self._parse_markdown_file(md_file, git_dir)
            if doc:
                documents.append(doc)

        # Save manifest
        manifest = {
            "source": "git",
            "repository": self.git_repo,
            "branch": self.branch,
            "exported_at": datetime.now().isoformat(),
            "document_count": len(documents),
            "documents": documents
        }

        manifest_path = self.export_path / "manifest.json"
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        logger.info(f"Exported {len(documents)} documents to {manifest_path}")
        return manifest

    def export_via_graphql(self) -> dict:
        """
        Export wiki content via GraphQL API.

        Requires Wiki.js GraphQL API to be enabled.
        """
        if not self.graphql_url:
            raise ValueError("GraphQL URL is required for graphql mode")

        logger.info(f"Exporting wiki via GraphQL: {self.graphql_url}")

        try:
            import httpx
        except ImportError:
            raise ImportError("httpx is required for GraphQL mode: pip install httpx")

        # Query all pages
        query = """
        query {
            pages {
                list {
                    id
                    path
                    title
                    description
                    content
                    contentType
                    createdAt
                    updatedAt
                    tags {
                        tag
                    }
                }
            }
        }
        """

        response = httpx.post(
            self.graphql_url,
            json={"query": query},
            timeout=60
        )
        response.raise_for_status()

        data = response.json()
        pages = data.get("data", {}).get("pages", {}).get("list", [])

        logger.info(f"Found {len(pages)} pages via GraphQL")

        # Parse and collect documents
        documents = []
        for page in pages:
            doc = {
                "id": page.get("id"),
                "path": page.get("path", ""),
                "title": page.get("title", ""),
                "description": page.get("description", ""),
                "content": page.get("content", ""),
                "content_type": page.get("contentType", "markdown"),
                "created_at": page.get("createdAt"),
                "updated_at": page.get("updatedAt"),
                "tags": [t.get("tag") for t in page.get("tags", [])],
                "source": "graphql",
                "source_path": f"wiki/{page.get('path', 'unknown')}.md"
            }

            # Extract frontmatter-like metadata from content if present
            doc = self._extract_frontmatter(doc)
            documents.append(doc)

        # Save manifest
        manifest = {
            "source": "graphql",
            "url": self.graphql_url,
            "exported_at": datetime.now().isoformat(),
            "document_count": len(documents),
            "documents": documents
        }

        manifest_path = self.export_path / "manifest.json"
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        # Also save individual markdown files
        md_dir = self.export_path / "pages"
        md_dir.mkdir(exist_ok=True)
        for doc in documents:
            safe_path = doc["path"].replace("/", "_") or "index"
            md_path = md_dir / f"{safe_path}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(doc.get("content", ""))

        logger.info(f"Exported {len(documents)} documents to {manifest_path}")
        return manifest

    def _parse_markdown_file(self, md_file: Path, base_dir: Path) -> Optional[dict]:
        """Parse a markdown file and extract metadata."""
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception as e:
            logger.warning(f"Failed to read {md_file}: {e}")
            return None

        # Calculate relative path
        rel_path = md_file.relative_to(base_dir)

        # Extract frontmatter if present
        frontmatter = {}
        body = content

        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                    body = parts[2].strip()
                except yaml.YAMLError:
                    pass

        # Build document
        doc = {
            "path": str(rel_path),
            "title": frontmatter.get("title", md_file.stem.replace("-", " ").replace("_", " ").title()),
            "description": frontmatter.get("description", ""),
            "content": body,
            "content_type": "markdown",
            "source": "git",
            "source_path": f"wiki/{rel_path}",
            # Metadata from frontmatter
            "doc_type": frontmatter.get("doc_type", self._infer_doc_type(str(rel_path))),
            "truth_level": frontmatter.get("truth_level", "L3"),
            "tags": frontmatter.get("tags", []),
            "updated_at": frontmatter.get("updated_at"),
        }

        return doc

    def _extract_frontmatter(self, doc: dict) -> dict:
        """Extract frontmatter from content if present."""
        content = doc.get("content", "")
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                    doc["content"] = parts[2].strip()
                    doc["doc_type"] = frontmatter.get("doc_type", doc.get("doc_type"))
                    doc["truth_level"] = frontmatter.get("truth_level", "L3")
                    if "tags" in frontmatter:
                        doc["tags"] = frontmatter["tags"]
                except yaml.YAMLError:
                    pass
        return doc

    def _infer_doc_type(self, path: str) -> str:
        """Infer document type from path."""
        path_lower = path.lower()
        if "faq" in path_lower:
            return "faq"
        elif "diagnostic" in path_lower:
            return "diagnostic"
        elif "polic" in path_lower or "retour" in path_lower or "garantie" in path_lower:
            return "policy"
        elif "guide" in path_lower:
            return "guide"
        elif "vehicle" in path_lower or "voiture" in path_lower:
            return "vehicle"
        return "general"


def main():
    parser = argparse.ArgumentParser(description="Export Wiki.js content for RAG")
    parser.add_argument(
        "--mode",
        choices=["git", "graphql"],
        default="git",
        help="Export mode (default: git)"
    )
    parser.add_argument(
        "--repo",
        help="Git repository URL (for git mode)"
    )
    parser.add_argument(
        "--branch",
        default="main",
        help="Git branch (default: main)"
    )
    parser.add_argument(
        "--url",
        help="GraphQL URL (for graphql mode)"
    )
    parser.add_argument(
        "--output",
        default="/opt/automecanik/rag/wiki_export",
        help="Output directory"
    )

    args = parser.parse_args()

    # Load config for defaults
    config = load_config()
    wiki_config = config.get("wiki", {})

    # Build exporter
    exporter = WikiExporter(
        export_path=args.output,
        git_repo=args.repo or wiki_config.get("git_repo"),
        branch=args.branch,
        graphql_url=args.url or wiki_config.get("graphql_url")
    )

    # Export
    if args.mode == "git":
        manifest = exporter.export_via_git()
    else:
        manifest = exporter.export_via_graphql()

    print(f"\nExport complete:")
    print(f"  Documents: {manifest['document_count']}")
    print(f"  Manifest: {args.output}/manifest.json")


if __name__ == "__main__":
    main()
