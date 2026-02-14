"""Token-Aware Document Chunker with H2/H3 heading awareness.

Splits documents into chunks of approximately `chunk_size` tokens
with `chunk_overlap` tokens of overlap between consecutive chunks.

Features:
- **Heading-aware splitting** (H1/H2/H3 are primary boundaries)
- Token-aware splitting within sections that exceed chunk_size
- Respects sentence and paragraph boundaries
- Preserves heading context as prefix in each chunk
- Strips frontmatter before chunking
"""

import re
import logging
from typing import List, Optional

logger = logging.getLogger(__name__)

# Regex to match markdown headings (H1-H3)
_HEADING_RE = re.compile(r"^(#{1,3})\s+(.+)$", re.MULTILINE)


class TokenAwareChunker:
    """Token-aware document chunker with heading awareness.

    Primary strategy: split on markdown headings (H1/H2/H3).
    Secondary strategy: token-based splitting for oversized sections.

    Uses a simple tokenization approximation (4 chars ~ 1 token)
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
        respect_headings: bool = True,
    ):
        """Initialize chunker.

        Args:
            chunk_size: Target number of tokens per chunk
            chunk_overlap: Number of tokens to overlap between chunks
            min_chunk_size: Minimum tokens for a chunk (avoids tiny chunks)
            respect_sentences: Try to break on sentence boundaries
            strip_frontmatter: Remove YAML frontmatter before chunking
            respect_headings: Split on H1/H2/H3 headings first (default True)
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.min_chunk_size = min_chunk_size
        self.respect_sentences = respect_sentences
        self.strip_frontmatter = strip_frontmatter
        self.respect_headings = respect_headings

    def chunk(self, text: str) -> List[dict]:
        """Chunk text into smaller pieces.

        Strategy:
        1. Strip frontmatter
        2. Split by markdown headings (H1/H2/H3) into sections
        3. For each section: if within chunk_size, emit as one chunk;
           otherwise apply token-based sub-splitting
        4. Each chunk carries its parent heading as metadata

        Args:
            text: Text to chunk

        Returns:
            List of chunk dicts with content, start_char, end_char,
            heading (str|None), heading_level (int|None)
        """
        if self.strip_frontmatter:
            text = self._strip_frontmatter(text)

        if self.respect_headings and _HEADING_RE.search(text):
            return self._chunk_by_headings(text)

        return self._chunk_by_tokens(text)

    def _chunk_by_headings(self, text: str) -> List[dict]:
        """Split text by headings, then sub-chunk oversized sections."""
        sections = self._split_into_sections(text)
        char_limit = self.chunk_size * self.CHARS_PER_TOKEN

        chunks: List[dict] = []
        chunk_index = 0

        for section in sections:
            heading = section.get("heading")
            heading_level = section.get("heading_level")
            body = section["content"].strip()
            section_start = section["start_char"]

            if not body:
                continue

            # Build content: prefix heading into the chunk body for context
            if heading:
                prefix = f"{'#' * heading_level} {heading}\n\n"
                full_content = prefix + body
            else:
                full_content = body

            if len(full_content) <= char_limit:
                # Section fits in one chunk
                min_chars = self.min_chunk_size * self.CHARS_PER_TOKEN
                if len(full_content.strip()) >= min_chars // 2:
                    chunks.append({
                        "content": full_content.strip(),
                        "chunk_index": chunk_index,
                        "start_char": section_start,
                        "end_char": section_start + len(body),
                        "token_estimate": len(full_content.strip()) // self.CHARS_PER_TOKEN,
                        "heading": heading,
                        "heading_level": heading_level,
                    })
                    chunk_index += 1
            else:
                # Section too large: sub-chunk by tokens within section
                sub_chunks = self._chunk_by_tokens(body, base_offset=section_start)
                for sc in sub_chunks:
                    # Prefix heading for context
                    if heading:
                        prefix = f"{'#' * heading_level} {heading}\n\n"
                        sc["content"] = prefix + sc["content"]
                        sc["token_estimate"] = len(sc["content"]) // self.CHARS_PER_TOKEN
                    sc["chunk_index"] = chunk_index
                    sc["heading"] = heading
                    sc["heading_level"] = heading_level
                    chunks.append(sc)
                    chunk_index += 1

        return chunks

    def _split_into_sections(self, text: str) -> List[dict]:
        """Split text into sections based on heading positions.

        Returns list of dicts:
            { heading: str|None, heading_level: int|None,
              content: str, start_char: int }
        """
        matches = list(_HEADING_RE.finditer(text))

        if not matches:
            return [{"heading": None, "heading_level": None,
                     "content": text, "start_char": 0}]

        sections: List[dict] = []

        # Content before first heading (preamble)
        if matches[0].start() > 0:
            preamble = text[: matches[0].start()]
            if preamble.strip():
                sections.append({
                    "heading": None,
                    "heading_level": None,
                    "content": preamble,
                    "start_char": 0,
                })

        # Each heading starts a section that runs until the next heading
        for i, match in enumerate(matches):
            heading_level = len(match.group(1))
            heading_text = match.group(2).strip()
            body_start = match.end()
            body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)

            body = text[body_start:body_end]
            sections.append({
                "heading": heading_text,
                "heading_level": heading_level,
                "content": body,
                "start_char": match.start(),
            })

        return sections

    def _chunk_by_tokens(self, text: str, base_offset: int = 0) -> List[dict]:
        """Token-based chunking (original algorithm).

        Used as fallback for non-heading text or for sub-chunking
        oversized sections.
        """
        char_limit = self.chunk_size * self.CHARS_PER_TOKEN
        overlap_chars = self.chunk_overlap * self.CHARS_PER_TOKEN
        min_chars = self.min_chunk_size * self.CHARS_PER_TOKEN

        chunks = []
        start = 0
        chunk_index = 0

        while start < len(text):
            end = min(start + char_limit, len(text))

            if end < len(text) and self.respect_sentences:
                break_point = self._find_sentence_boundary(text, start, end)
                if break_point and break_point > start + min_chars:
                    end = break_point

            chunk_content = text[start:end].strip()

            if chunk_content and len(chunk_content) >= min_chars // 2:
                chunks.append({
                    "content": chunk_content,
                    "chunk_index": chunk_index,
                    "start_char": base_offset + start,
                    "end_char": base_offset + end,
                    "token_estimate": len(chunk_content) // self.CHARS_PER_TOKEN,
                    "heading": None,
                    "heading_level": None,
                })
                chunk_index += 1

            if end >= len(text):
                break

            next_start = end - overlap_chars
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
            heading=chunk.get("heading"),
            heading_level=chunk.get("heading_level"),
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

### Subsection 2.1

Details about subsection 2.1 with technical content.

Final paragraph of the test document.
"""

    print("=== Heading-Aware Chunking ===")
    chunker = TokenAwareChunker(chunk_size=100, chunk_overlap=20)
    chunks = chunker.chunk(test_text)

    print(f"Created {len(chunks)} chunks:")
    for i, chunk in enumerate(chunks):
        heading = chunk.get("heading") or "(no heading)"
        level = chunk.get("heading_level") or "-"
        print(f"\n--- Chunk {i} [H{level}: {heading}] ({chunk['token_estimate']} tokens) ---")
        print(chunk["content"][:200] + "..." if len(chunk["content"]) > 200 else chunk["content"])

    print("\n=== Token-Only Chunking (respect_headings=False) ===")
    chunker2 = TokenAwareChunker(chunk_size=100, chunk_overlap=20, respect_headings=False)
    chunks2 = chunker2.chunk(test_text)
    print(f"Created {len(chunks2)} chunks (no heading awareness)")
