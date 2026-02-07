"""Wiki.js Extractor - Extract documents from Wiki.js.

Supports two modes:
- git: Clone/pull wiki repo and read markdown files
- graphql: Query Wiki.js GraphQL API directly

This is a wrapper around the existing wiki_exporter.py script.
"""

import logging
from typing import List, Optional
from pathlib import Path
import asyncio
import subprocess
import tempfile

logger = logging.getLogger(__name__)


class WikiExtractor:
    """Extract documents from Wiki.js."""

    def __init__(
        self,
        mode: str = "git",
        repo_url: Optional[str] = None,
        repo_path: Optional[str] = None,
        graphql_url: Optional[str] = None,
        graphql_token: Optional[str] = None,
    ):
        """Initialize Wiki extractor.

        Args:
            mode: Extraction mode ('git' or 'graphql')
            repo_url: Git repository URL for wiki backup
            repo_path: Local path for cloned repo
            graphql_url: Wiki.js GraphQL endpoint
            graphql_token: API token for GraphQL
        """
        self.mode = mode
        self.repo_url = repo_url
        self.repo_path = repo_path or tempfile.mkdtemp(prefix="wiki_")
        self.graphql_url = graphql_url
        self.graphql_token = graphql_token

    async def extract(self) -> List[dict]:
        """Extract all documents from Wiki.

        Returns:
            List of document dicts with content and metadata.
        """
        if self.mode == "git":
            return await self._extract_git()
        elif self.mode == "graphql":
            return await self._extract_graphql()
        else:
            logger.error(f"Unknown wiki mode: {self.mode}")
            return []

    async def _extract_git(self) -> List[dict]:
        """Extract documents via Git clone/pull."""
        docs = []

        if not self.repo_url:
            logger.warning("No wiki repo URL configured")
            return docs

        try:
            # Clone or pull the repo
            repo_path = Path(self.repo_path)

            if (repo_path / ".git").exists():
                # Pull latest changes
                logger.info(f"Pulling wiki repo: {self.repo_path}")
                subprocess.run(
                    ["git", "pull"],
                    cwd=self.repo_path,
                    check=True,
                    capture_output=True,
                )
            else:
                # Clone the repo
                logger.info(f"Cloning wiki repo: {self.repo_url}")
                subprocess.run(
                    ["git", "clone", self.repo_url, self.repo_path],
                    check=True,
                    capture_output=True,
                )

            # Read all markdown files
            for md_file in repo_path.rglob("*.md"):
                try:
                    content = md_file.read_text(encoding="utf-8")
                    relative_path = md_file.relative_to(repo_path)

                    docs.append(
                        {
                            "source_path": f"wiki/{relative_path}",
                            "content": content,
                            "title": md_file.stem,
                            "source_type": "wiki",
                            "metadata": {
                                "wiki_path": str(relative_path),
                                "extraction_mode": "git",
                            },
                        }
                    )
                except Exception as e:
                    logger.error(f"Failed to read wiki file {md_file}: {e}")

        except subprocess.CalledProcessError as e:
            logger.error(f"Git operation failed: {e.stderr.decode()}")
        except Exception as e:
            logger.error(f"Wiki git extraction failed: {e}")

        return docs

    async def _extract_graphql(self) -> List[dict]:
        """Extract documents via GraphQL API."""
        docs = []

        if not self.graphql_url:
            logger.warning("No wiki GraphQL URL configured")
            return docs

        try:
            import httpx

            headers = {}
            if self.graphql_token:
                headers["Authorization"] = f"Bearer {self.graphql_token}"

            # Query all pages
            query = """
            query {
                pages {
                    list {
                        id
                        path
                        title
                        content
                        updatedAt
                        contentType
                    }
                }
            }
            """

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.graphql_url,
                    json={"query": query},
                    headers=headers,
                    timeout=60.0,
                )
                response.raise_for_status()
                data = response.json()

                pages = data.get("data", {}).get("pages", {}).get("list", [])

                for page in pages:
                    # Only include markdown pages
                    if page.get("contentType") == "markdown":
                        docs.append(
                            {
                                "source_path": f"wiki/{page['path']}",
                                "content": page.get("content", ""),
                                "title": page.get("title", page["path"]),
                                "source_type": "wiki",
                                "metadata": {
                                    "wiki_id": page["id"],
                                    "wiki_path": page["path"],
                                    "updated_at": page.get("updatedAt"),
                                    "extraction_mode": "graphql",
                                },
                            }
                        )

        except ImportError:
            logger.error("httpx not installed for GraphQL extraction")
        except Exception as e:
            logger.error(f"Wiki GraphQL extraction failed: {e}")

        return docs


async def extract_wiki_documents(config) -> List:
    """Extract documents from Wiki.js using config.

    Args:
        config: PipelineConfig with wiki settings.

    Returns:
        List of Document objects.
    """
    from ..pipeline import Document

    extractor = WikiExtractor(
        mode=config.wiki_mode,
        repo_path=config.wiki_repo_path,
        graphql_url=config.wiki_graphql_url,
    )

    raw_docs = await extractor.extract()
    logger.info(f"Extracted {len(raw_docs)} documents from Wiki")

    return [
        Document(
            source_path=doc["source_path"],
            content=doc["content"],
            title=doc["title"],
            source_type="wiki",
            truth_level=doc.get("metadata", {}).get("truth_level", "L2"),
            metadata=doc.get("metadata", {}),
        )
        for doc in raw_docs
    ]
