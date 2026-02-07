"""Token-Aware Document Chunker.

Splits documents into chunks of approximately `chunk_size` tokens
with `chunk_overlap` tokens of overlap between consecutive chunks.

Features:
- Token-aware splitting (not just character-based)
- Respects sentence and paragraph boundaries
- Preserves markdown structure where possible
- Strips frontmatter before chunking
"""

import re
import logging
from typing import List, Optional

logger = logging.getLogger(__name__)


class TokenAwareChunker:
    """Token-aware document chunker.

    Uses a simple tokenization approximation (4 chars ≈ 1 token)
    for efficiency. For exact token counts, use a tokenizer like tiktoken.
    """

    # Approximate chars per token (conservative estimate)
    CHARS_PER_TOKEN = 4

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 50,
        min_chunk_size: int = 100,
        respect_sentences: bool = True,
        strip_frontmatter: bool = True,
    ):
        """Initialize chunker.

        Args:
            chunk_size: Target number of tokens per chunk
            chunk_overlap: Number of tokens to overlap between chunks
            min_chunk_size: Minimum tokens for a chunk (avoids tiny chunks)
            respect_sentences: Try to break on sentence boundaries
            strip_frontmatter: Remove YAML frontmatter before chunking
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.min_chunk_size = min_chunk_size
        self.respect_sentences = respect_sentences
        self.strip_frontmatter = strip_frontmatter

    def chunk(self, text: str) -> List[dict]:
        """Chunk text into smaller pieces.

        Args:
            text: Text to chunk

        Returns:
            List of chunk dicts with content, start_char, end_char
        """
        # Strip frontmatter if present
        if self.strip_frontmatter:
            text = self._strip_frontmatter(text)

        # Calculate character limits from token targets
        char_limit = self.chunk_size * self.CHARS_PER_TOKEN
        overlap_chars = self.chunk_overlap * self.CHARS_PER_TOKEN
        min_chars = self.min_chunk_size * self.CHARS_PER_TOKEN

        chunks = []
        start = 0
        chunk_index = 0

        while start < len(text):
            # Calculate end position
            end = min(start + char_limit, len(text))

            # If not at the end, try to find a good break point
            if end < len(text) and self.respect_sentences:
                # Look for sentence boundary
                break_point = self._find_sentence_boundary(text, start, end)
                if break_point and break_point > start + min_chars:
                    end = break_point

            # Extract chunk content
            chunk_content = text[start:end].strip()

            # Only add non-empty chunks
            if chunk_content and len(chunk_content) >= min_chars // 2:
                chunks.append({
                    "content": chunk_content,
                    "chunk_index": chunk_index,
                    "start_char": start,
                    "end_char": end,
                    "token_estimate": len(chunk_content) // self.CHARS_PER_TOKEN,
                })
                chunk_index += 1

            # Move to next chunk position (with overlap)
            if end >= len(text):
                break

            # Calculate next start with overlap
            next_start = end - overlap_chars

            # Ensure we're making progress
            if next_start <= start:
                next_start = start + min_chars

            start = next_start

        return chunks

    def _strip_frontmatter(self, text: str) -> str:
        """Remove YAML frontmatter from text."""
        if not text.startswith("---"):
            return text

        # Find closing ---
        end_match = re.search(r"\n---\s*\n", text[3:])
        if end_match:
            return text[3 + end_match.end():].strip()

        return text

    def _find_sentence_boundary(self, text: str, start: int, end: int) -> Optional[int]:
        """Find the best sentence boundary near the end position.

        Looks for sentence-ending punctuation followed by whitespace.
        """
        # Look backwards from end to find sentence boundary
        search_start = max(start + (end - start) // 2, start)
        search_region = text[search_start:end]

        # Find last sentence boundary in search region
        # Sentence endings: . ! ? followed by space/newline
        pattern = r'[.!?]\s+'
        matches = list(re.finditer(pattern, search_region))

        if matches:
            # Use the last match
            last_match = matches[-1]
            return search_start + last_match.end()

        # Try paragraph boundary (double newline)
        para_matches = list(re.finditer(r'\n\n', search_region))
        if para_matches:
            last_match = para_matches[-1]
            return search_start + last_match.end()

        # No good boundary found
        return None


def chunk_document(document, chunk_size: int = 500, chunk_overlap: int = 50) -> List:
    """Chunk a Document into Chunk objects.

    Args:
        document: Document object to chunk
        chunk_size: Target tokens per chunk
        chunk_overlap: Token overlap between chunks

    Returns:
        List of Chunk objects
    """
    from ..pipeline import Chunk

    chunker = TokenAwareChunker(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    raw_chunks = chunker.chunk(document.content)

    return [
        Chunk(
            document=document,
            content=chunk["content"],
            chunk_index=chunk["chunk_index"],
            start_char=chunk["start_char"],
            end_char=chunk["end_char"],
        )
        for chunk in raw_chunks
    ]


# Convenience function for standalone use
def chunk_text(
    text: str,
    chunk_size: int = 500,
    chunk_overlap: int = 50,
) -> List[str]:
    """Chunk text into smaller pieces (returns just the content).

    Args:
        text: Text to chunk
        chunk_size: Target tokens per chunk
        chunk_overlap: Token overlap between chunks

    Returns:
        List of chunk content strings
    """
    chunker = TokenAwareChunker(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    chunks = chunker.chunk(text)
    return [c["content"] for c in chunks]


if __name__ == "__main__":
    # Quick test
    test_text = """---
title: Test Document
truth_level: L2
---

# Introduction

This is a test document for the chunker. It contains multiple paragraphs
and sentences to test the chunking logic.

## Section 1

Here is some content in section 1. It should be properly chunked based on
token limits while respecting sentence boundaries.

This is another paragraph in section 1. The chunker should handle this well.

## Section 2

Section 2 has more content. The overlap between chunks should ensure
continuity for semantic search.

Final paragraph of the test document.
"""

    chunker = TokenAwareChunker(chunk_size=100, chunk_overlap=20)
    chunks = chunker.chunk(test_text)

    print(f"Created {len(chunks)} chunks:")
    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i} ({chunk['token_estimate']} tokens) ---")
        print(chunk["content"][:200] + "..." if len(chunk["content"]) > 200 else chunk["content"])
