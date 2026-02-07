"""MinIO Extractor - Extract documents from S3-compatible storage.

Supports:
- PDF files (requires pypdf or pdfplumber)
- DOCX files (requires python-docx)
- Markdown files
- Text files

The extractor downloads files from MinIO buckets, converts them to markdown,
and returns them for chunking and indexing.
"""

import logging
from typing import List, Optional
from pathlib import Path
import tempfile
import os

logger = logging.getLogger(__name__)


class MinIOExtractor:
    """Extract documents from MinIO S3-compatible storage."""

    def __init__(
        self,
        endpoint: str = "minio:9000",
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        buckets: Optional[List[str]] = None,
        secure: bool = False,
    ):
        """Initialize MinIO extractor.

        Args:
            endpoint: MinIO server endpoint
            access_key: Access key (or from MINIO_ACCESS_KEY env)
            secret_key: Secret key (or from MINIO_SECRET_KEY env)
            buckets: List of buckets to extract from
            secure: Use HTTPS
        """
        self.endpoint = endpoint
        self.access_key = access_key or os.getenv("MINIO_ACCESS_KEY", "")
        self.secret_key = secret_key or os.getenv("MINIO_SECRET_KEY", "")
        self.buckets = buckets or ["docs", "exports"]
        self.secure = secure
        self._client = None
        self._temp_dir = tempfile.mkdtemp(prefix="minio_")

    def _get_client(self):
        """Get or create MinIO client."""
        if self._client is None:
            try:
                from minio import Minio

                self._client = Minio(
                    self.endpoint,
                    access_key=self.access_key,
                    secret_key=self.secret_key,
                    secure=self.secure,
                )
            except ImportError:
                logger.error("minio package not installed")
                return None
        return self._client

    async def extract(self) -> List[dict]:
        """Extract all documents from configured buckets.

        Returns:
            List of document dicts with content and metadata.
        """
        docs = []
        client = self._get_client()

        if client is None:
            return docs

        for bucket_name in self.buckets:
            bucket_docs = await self._extract_bucket(client, bucket_name)
            docs.extend(bucket_docs)

        return docs

    async def _extract_bucket(self, client, bucket_name: str) -> List[dict]:
        """Extract documents from a single bucket."""
        docs = []

        try:
            # Check if bucket exists
            if not client.bucket_exists(bucket_name):
                logger.warning(f"Bucket not found: {bucket_name}")
                return docs

            # List all objects
            objects = client.list_objects(bucket_name, recursive=True)

            for obj in objects:
                try:
                    doc = await self._extract_object(client, bucket_name, obj.object_name)
                    if doc:
                        docs.append(doc)
                except Exception as e:
                    logger.error(f"Failed to extract {bucket_name}/{obj.object_name}: {e}")

        except Exception as e:
            logger.error(f"Failed to list bucket {bucket_name}: {e}")

        return docs

    async def _extract_object(self, client, bucket_name: str, object_name: str) -> Optional[dict]:
        """Extract content from a single object."""
        # Determine file type
        ext = Path(object_name).suffix.lower()

        # Only process supported file types
        supported_extensions = {".md", ".txt", ".pdf", ".docx"}
        if ext not in supported_extensions:
            logger.debug(f"Skipping unsupported file type: {object_name}")
            return None

        # Download to temp file
        local_path = Path(self._temp_dir) / Path(object_name).name
        try:
            client.fget_object(bucket_name, object_name, str(local_path))
        except Exception as e:
            logger.error(f"Failed to download {object_name}: {e}")
            return None

        # Extract content based on file type
        content = None
        try:
            if ext == ".md" or ext == ".txt":
                content = local_path.read_text(encoding="utf-8")
            elif ext == ".pdf":
                content = self._extract_pdf(local_path)
            elif ext == ".docx":
                content = self._extract_docx(local_path)
        finally:
            # Cleanup temp file
            if local_path.exists():
                local_path.unlink()

        if not content:
            return None

        return {
            "source_path": f"minio/{bucket_name}/{object_name}",
            "content": content,
            "title": Path(object_name).stem,
            "source_type": "minio",
            "metadata": {
                "bucket": bucket_name,
                "object_name": object_name,
                "file_type": ext,
            },
        }

    def _extract_pdf(self, file_path: Path) -> Optional[str]:
        """Extract text from PDF file."""
        try:
            # Try pypdf first
            try:
                from pypdf import PdfReader

                reader = PdfReader(str(file_path))
                text_parts = []
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        text_parts.append(text)
                return "\n\n".join(text_parts)
            except ImportError:
                pass

            # Fallback to pdfplumber
            try:
                import pdfplumber

                with pdfplumber.open(str(file_path)) as pdf:
                    text_parts = []
                    for page in pdf.pages:
                        text = page.extract_text()
                        if text:
                            text_parts.append(text)
                    return "\n\n".join(text_parts)
            except ImportError:
                pass

            logger.warning("No PDF extraction library available (pypdf or pdfplumber)")
            return None

        except Exception as e:
            logger.error(f"PDF extraction failed: {e}")
            return None

    def _extract_docx(self, file_path: Path) -> Optional[str]:
        """Extract text from DOCX file."""
        try:
            from docx import Document

            doc = Document(str(file_path))
            text_parts = []

            for para in doc.paragraphs:
                if para.text.strip():
                    text_parts.append(para.text)

            # Also extract text from tables
            for table in doc.tables:
                for row in table.rows:
                    row_text = " | ".join(cell.text.strip() for cell in row.cells if cell.text.strip())
                    if row_text:
                        text_parts.append(row_text)

            return "\n\n".join(text_parts)

        except ImportError:
            logger.warning("python-docx not installed")
            return None
        except Exception as e:
            logger.error(f"DOCX extraction failed: {e}")
            return None

    def cleanup(self):
        """Cleanup temp directory."""
        import shutil

        if Path(self._temp_dir).exists():
            shutil.rmtree(self._temp_dir)


async def extract_minio_documents(config) -> List:
    """Extract documents from MinIO using config.

    Args:
        config: PipelineConfig with MinIO settings.

    Returns:
        List of Document objects.
    """
    from ..pipeline import Document

    extractor = MinIOExtractor(
        endpoint=config.minio_endpoint,
        access_key=config.minio_access_key,
        secret_key=config.minio_secret_key,
        buckets=config.minio_buckets,
    )

    try:
        raw_docs = await extractor.extract()
        logger.info(f"Extracted {len(raw_docs)} documents from MinIO")

        return [
            Document(
                source_path=doc["source_path"],
                content=doc["content"],
                title=doc["title"],
                source_type="minio",
                truth_level="L3",  # MinIO docs default to L3 (Hypotheses)
                metadata=doc.get("metadata", {}),
            )
            for doc in raw_docs
        ]
    finally:
        extractor.cleanup()
