"""Application-wide exceptions for the AutoMecanik RAG service.

Phase F.5 (ADR-031) — Runtime hardening exceptions.
"""

from typing import Optional


class RagReadOnlyError(Exception):
    """Raised when a write operation is attempted while the service is in
    Phase F.5 readonly mode (`rag_write_mode="readonly"`).

    This is the L5 service-layer defense-in-depth guard. It fires regardless
    of how the write is invoked (HTTP route, internal cron, queue worker,
    M2M endpoint, ad-hoc Python script). The HTTP layer (L4) catches this
    and returns 410 Gone with Sunset/Deprecation headers ; non-HTTP callers
    see a clean Python exception.

    Attributes:
        operation: human-readable name of the blocked write op
                   (ex "create_document", "ingest_pdf").
        replacement: pointer to the canonical pipeline replacement.
        adr: governance reference (default "ADR-031").
    """

    def __init__(
        self,
        operation: str,
        replacement: str = "automecanik-raw → automecanik-wiki/exports/rag → rag indexer",
        adr: str = "ADR-031",
        detail: Optional[str] = None,
    ) -> None:
        self.operation = operation
        self.replacement = replacement
        self.adr = adr
        self.detail = detail
        msg = (
            f"F.5: write operation {operation!r} blocked "
            f"(rag_write_mode=readonly per {adr}). "
            f"Use the canonical pipeline: {replacement}."
        )
        if detail:
            msg += f" Detail: {detail}"
        super().__init__(msg)
