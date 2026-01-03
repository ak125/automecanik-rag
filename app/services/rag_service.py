"""RAG Service - Search with Truth Levels (Semantic Brain L1-L4)."""

import logging
from typing import Optional
from dataclasses import dataclass, field

from app.services.weaviate_client import get_weaviate_client
from app.config import get_settings

logger = logging.getLogger(__name__)

# Truth Level definitions
TRUTH_LEVELS = {
    "L1": {"name": "Faits vérifiés", "emoji": "✅", "weight": 1.0, "certainty": "affirme avec certitude"},
    "L2": {"name": "Règles métier", "emoji": "📋", "weight": 0.9, "certainty": "selon notre politique"},
    "L3": {"name": "Hypothèses", "emoji": "❓", "weight": 0.6, "certainty": "probablement"},
    "L4": {"name": "Heuristiques", "emoji": "💭", "weight": 0.4, "certainty": "en général"},
}

# Mixing rules: which combinations are allowed
MIXING_RULES = {
    ("L1", "L2"): {"allowed": True, "warning": None},
    ("L1", "L3"): {"allowed": True, "warning": "⚠️ Mélange faits vérifiés et hypothèses"},
    ("L1", "L4"): {"allowed": False, "warning": "❌ Mélange interdit: faits et heuristiques"},
    ("L2", "L3"): {"allowed": True, "warning": "⚠️ Mélange règles métier et hypothèses"},
    ("L2", "L4"): {"allowed": True, "warning": "⚠️ Mélange règles métier et heuristiques"},
    ("L3", "L4"): {"allowed": False, "warning": "❌ Mélange interdit: trop incertain"},
}


@dataclass
class TruthMetadata:
    """Truth level metadata for search results."""
    composition: dict = field(default_factory=dict)  # {"L1": 2, "L2": 1, ...}
    dominant_level: str = "L3"
    composite_confidence: float = 0.5
    mixing_warning: Optional[str] = None
    reasoning_chain: list = field(default_factory=list)
    contradictions: list = field(default_factory=list)


@dataclass
class SearchResponse:
    """Response from search endpoint with Truth Level metadata."""
    results: list[dict]
    query: str
    total: int
    context: str  # Formatted context for Claude CLI
    # Truth Level metadata (Semantic Brain)
    truth_metadata: TruthMetadata = field(default_factory=TruthMetadata)
    # P1: RAG Gating - True if insufficient results for confident answer
    needs_clarification: bool = False
    # P1: Citations - Mandatory sources section
    sources_citation: str = ""


class RAGService:
    """
    RAG Service - Search with Truth Levels (Semantic Brain L1-L4).

    Returns context for Claude CLI with truth level metadata.
    100% gratuit - embeddings locaux via sentence-transformers.

    Truth Levels:
    - L1: Faits vérifiés (documentation officielle)
    - L2: Règles métier (procédures établies)
    - L3: Hypothèses (inférences raisonnées)
    - L4: Heuristiques (approximations empiriques)
    """

    def __init__(self):
        """Initialize RAG service."""
        self.weaviate = get_weaviate_client()
        self.settings = get_settings()

    async def search(
        self,
        query: str,
        limit: int = 10,
        filters: Optional[dict] = None,
        namespace: Optional[str] = None,
    ) -> SearchResponse:
        """
        Perform semantic search with truth level analysis.

        Args:
            query: Search query
            limit: Max results
            filters: Optional filters
            namespace: Namespace to search in (validated by NamespaceGuard)

        Returns:
            SearchResponse with results, context, and truth metadata
        """
        logger.info(f"Processing search query: {query[:100]}... namespace={namespace}")

        results = await self.weaviate.hybrid_search(
            query=query,
            limit=limit,
        )

        # P1: Apply minimum score threshold
        min_score = self.settings.min_score_threshold
        filtered_results = [r for r in results if r.get("score", 0) >= min_score]

        # P1: Check minimum results requirement
        min_results = self.settings.min_results_required
        needs_clarification = len(filtered_results) < min_results

        if needs_clarification:
            logger.warning(
                f"RAG Gating: Only {len(filtered_results)} results above threshold "
                f"(min={min_results}, score>={min_score})"
            )

        # Use filtered results for analysis
        results = filtered_results if filtered_results else results[:1]

        # Analyze truth levels
        truth_metadata = self._analyze_truth_levels(results)

        # Format context with truth level indicators
        context = self._format_context_with_truth(results, truth_metadata)

        # P1: Generate mandatory sources citation
        sources_citation = self._generate_sources_citation(results)

        return SearchResponse(
            results=results,
            query=query,
            total=len(results),
            context=context,
            truth_metadata=truth_metadata,
            needs_clarification=needs_clarification,
            sources_citation=sources_citation,
        )

    def _analyze_truth_levels(self, results: list[dict]) -> TruthMetadata:
        """
        Analyze truth levels of search results.

        Detects mixing violations and calculates composite confidence.
        """
        if not results:
            return TruthMetadata()

        # Count truth levels
        composition = {"L1": 0, "L2": 0, "L3": 0, "L4": 0}
        for r in results:
            level = r.get("truth_level", "L3")
            if level in composition:
                composition[level] += 1

        # Find dominant level
        dominant_level = max(composition, key=composition.get) if any(composition.values()) else "L3"

        # Calculate composite confidence
        total_weight = 0
        total_count = 0
        for level, count in composition.items():
            if count > 0:
                weight = TRUTH_LEVELS.get(level, {}).get("weight", 0.5)
                total_weight += weight * count
                total_count += count

        composite_confidence = total_weight / total_count if total_count > 0 else 0.5

        # Check for mixing violations
        mixing_warning = self._check_mixing_rules(composition)

        # Detect contradictions (basic implementation)
        contradictions = self._detect_contradictions(results)

        # Build reasoning chain
        reasoning_chain = self._build_reasoning_chain(results)

        return TruthMetadata(
            composition=composition,
            dominant_level=dominant_level,
            composite_confidence=round(composite_confidence, 2),
            mixing_warning=mixing_warning,
            reasoning_chain=reasoning_chain,
            contradictions=contradictions,
        )

    def _check_mixing_rules(self, composition: dict) -> Optional[str]:
        """Check if truth level mixing violates rules."""
        present_levels = [level for level, count in composition.items() if count > 0]

        if len(present_levels) <= 1:
            return None  # No mixing

        # Check high levels (L1, L2) with low levels (L3, L4)
        has_high = any(level in ["L1", "L2"] for level in present_levels)
        has_low = any(level in ["L3", "L4"] for level in present_levels)

        if has_high and has_low:
            # Check specific rule
            for high in ["L1", "L2"]:
                for low in ["L3", "L4"]:
                    if high in present_levels and low in present_levels:
                        key = (high, low)
                        rule = MIXING_RULES.get(key, {})
                        if rule.get("warning"):
                            return rule["warning"]

        return None

    def _detect_contradictions(self, results: list[dict]) -> list[str]:
        """
        Detect potential contradictions between sources.

        Basic implementation: flag when same category has different truth levels.
        """
        contradictions = []
        category_levels = {}

        for r in results:
            category = r.get("category", "unknown")
            level = r.get("truth_level", "L3")
            title = r.get("title", "Sans titre")

            if category in category_levels:
                existing_level, existing_title = category_levels[category]
                if existing_level != level:
                    contradictions.append(
                        f"Conflit potentiel [{category}]: '{existing_title}' ({existing_level}) vs '{title}' ({level})"
                    )
            else:
                category_levels[category] = (level, title)

        return contradictions

    def _build_reasoning_chain(self, results: list[dict]) -> list[str]:
        """Build explainable reasoning chain from results."""
        chain = []
        for i, r in enumerate(results[:5], 1):  # Top 5 sources
            level = r.get("truth_level", "L3")
            title = r.get("title", "Sans titre")
            score = r.get("score", 0)
            level_info = TRUTH_LEVELS.get(level, {})
            emoji = level_info.get("emoji", "❓")
            certainty = level_info.get("certainty", "")

            chain.append(f"{i}. {emoji} [{level}] {title} (score: {score:.2f}) → {certainty}")

        return chain

    def _format_context_with_truth(self, results: list[dict], truth_metadata: TruthMetadata) -> str:
        """
        Format search results with truth level indicators for LLM.

        Includes truth level metadata header and per-source indicators.
        """
        if not results:
            return ""

        # Build header with truth level summary
        header_parts = ["=== SEMANTIC BRAIN - CONTEXT ===\n"]

        # Add truth level composition
        header_parts.append("📊 Niveaux de vérité des sources:")
        for level, count in truth_metadata.composition.items():
            if count > 0:
                info = TRUTH_LEVELS.get(level, {})
                emoji = info.get("emoji", "❓")
                name = info.get("name", level)
                header_parts.append(f"  {emoji} {level} ({name}): {count}")

        header_parts.append(f"\n🎯 Confiance composite: {truth_metadata.composite_confidence:.0%}")
        header_parts.append(f"📌 Niveau dominant: {truth_metadata.dominant_level}")

        # Add warnings if any
        if truth_metadata.mixing_warning:
            header_parts.append(f"\n{truth_metadata.mixing_warning}")

        if truth_metadata.contradictions:
            header_parts.append("\n⚠️ Contradictions détectées:")
            for contradiction in truth_metadata.contradictions[:3]:
                header_parts.append(f"  - {contradiction}")

        header_parts.append("\n" + "=" * 40 + "\n")

        # Format each source with truth level indicator
        context_parts = []
        for i, result in enumerate(results, 1):
            title = result.get("title", "Sans titre")
            content = result.get("content", "")
            source = result.get("source_path", "")
            score = result.get("score", 0)
            truth_level = result.get("truth_level", "L3")
            verification = result.get("verification_status", "unverified")

            level_info = TRUTH_LEVELS.get(truth_level, {})
            emoji = level_info.get("emoji", "❓")
            certainty = level_info.get("certainty", "")

            context_parts.append(
                f"[Source {i}] {emoji} [{truth_level}] {title}\n"
                f"Niveau: {truth_level} ({level_info.get('name', '')}) | Vérification: {verification}\n"
                f"Pertinence: {score:.2f} | Certainty: {certainty}\n"
                f"Fichier: {source}\n"
                f"Contenu:\n{content}\n"
            )

        return "\n".join(header_parts) + "\n---\n".join(context_parts)

    def _format_context(self, results: list[dict]) -> str:
        """
        Format search results into context string for LLM.

        Args:
            results: List of search results

        Returns:
            Formatted context string
        """
        if not results:
            return ""

        context_parts = []
        for i, result in enumerate(results, 1):
            title = result.get("title", "Sans titre")
            content = result.get("content", "")
            source = result.get("source_path", "")
            score = result.get("score", 0)

            context_parts.append(
                f"[Source {i}] {title}\n"
                f"Pertinence: {score:.2f}\n"
                f"Fichier: {source}\n"
                f"Contenu:\n{content}\n"
            )

        return "\n---\n".join(context_parts)

    def _generate_sources_citation(self, results: list[dict]) -> str:
        """
        Generate mandatory sources citation section.

        P1 RULE: JAMAIS répondre sans citer sources.

        Format:
        ## Sources
        1. [L1] document-title.md - Vérification: verified
        2. [L2] autre-document.md - Vérification: unverified

        Args:
            results: Search results with source information

        Returns:
            Formatted sources citation string
        """
        if not results:
            return "## Sources\nAucune source trouvée pour cette requête."

        lines = ["## Sources"]
        for i, result in enumerate(results, 1):
            title = result.get("title", "Sans titre")
            source_path = result.get("source_path", "unknown")
            truth_level = result.get("truth_level", "L3")
            verification = result.get("verification_status", "unverified")
            score = result.get("score", 0)

            # Extract filename from path
            filename = source_path.split("/")[-1] if source_path else "unknown"

            lines.append(
                f"{i}. [{truth_level}] {title} ({filename}) - "
                f"Vérification: {verification} | Score: {score:.2f}"
            )

        return "\n".join(lines)


# Singleton instance
_rag_service: Optional[RAGService] = None


def get_rag_service() -> RAGService:
    """Get or create RAG service instance."""
    global _rag_service
    if _rag_service is None:
        _rag_service = RAGService()
    return _rag_service
