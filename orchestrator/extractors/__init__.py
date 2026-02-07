"""Extractors package - Data extraction from various sources.

Supported sources:
- MinIO S3-compatible storage (PDFs, documents, exports)
- Wiki.js (Git sync or GraphQL API)
- Local knowledge folder (Markdown files)
"""

from .wiki_extractor import extract_wiki_documents, WikiExtractor
from .minio_extractor import extract_minio_documents, MinIOExtractor

__all__ = [
    "extract_wiki_documents",
    "WikiExtractor",
    "extract_minio_documents",
    "MinIOExtractor",
]
