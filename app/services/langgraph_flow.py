"""LangGraph RAG Flow - Full Pipeline with Guardrails and Generation.

Extends the context-only pipeline with:
- Guardrails: Score and result count validation
- Generate: Claude response generation with citations
- Refusal: Graceful handling of low-confidence queries

Flow:
    START -> classify -> retrieve -> guardrails -> generate -> END
                                        |
                                        v
                                     refuse -> END
"""

import logging
from typing import TypedDict, Literal, Optional

from langgraph.graph import StateGraph, END

from app.config import get_settings

settings = get_settings()
from app.services.rag_service import get_rag_service

logger = logging.getLogger(__name__)


class ChatState(TypedDict):
    """State for the full chat pipeline."""
    # Input
    query: str
    session_id: str
    user_locale: str

    # Classification
    query_type: Optional[Literal["on_topic", "off_topic", "ambiguous"]]

    # Retrieval
    results: list[dict]
    context: str
    sources: list[str]
    truth_metadata: dict

    # Guardrails
    passed_guardrails: bool
    refusal_reason: Optional[str]

    # Generation
    response: str
    citations: list[str]

    # Metadata
    error: Optional[str]


def classify_node(state: ChatState) -> ChatState:
    """
    Classify query as on-topic, off-topic, or ambiguous.

    Off-topic examples:
    - Stock prices, weather, recipes
    - Non-automotive topics
    - Malicious queries (hacking, etc.)
    """
    query = state["query"].lower().strip()

    # Empty or invalid queries
    if not query or len(query) < 3:
        return {**state, "query_type": "off_topic", "refusal_reason": "requete_invalide"}

    # Off-topic keywords (French)
    off_topic_patterns = [
        "bourse", "investir", "bitcoin", "crypto",
        "recette", "cuisine", "gateau", "chocolat",
        "meteo", "pluie",
        "pirater", "hacker", "password", "crack",
        "politique", "election", "president",
        "football", "match", "sport",
    ]

    for pattern in off_topic_patterns:
        if pattern in query:
            return {**state, "query_type": "off_topic", "refusal_reason": "hors_sujet"}

    # English patterns - refuse non-French queries
    english_patterns = [
        "brake", "noise", "when", "how to", "what is",
        "engine", "parts for", "car ", "repair", "change oil",
        "problem with", "issue", "stopping", "the "
    ]

    english_count = sum(1 for p in english_patterns if p in query)
    if english_count >= 2:
        return {**state, "query_type": "off_topic", "refusal_reason": "langue_non_supportee"}

    # On-topic keywords (automotive/SAV)
    on_topic_patterns = [
        "frein", "plaquette", "disque", "huile", "filtre", "courroie",
        "amortisseur", "pneu", "batterie", "alternateur", "demarreur",
        "embrayage", "vidange", "entretien", "diagnostic", "panne",
        "bruit", "vibration", "temoin", "voyant", "fume",
        "livraison", "retour", "garantie", "paiement", "commande",
        "clio", "peugeot", "renault", "citroen", "volkswagen"
    ]

    for pattern in on_topic_patterns:
        if pattern in query:
            return {**state, "query_type": "on_topic"}

    # Default to ambiguous - let retrieval decide
    return {**state, "query_type": "ambiguous"}


async def retrieve_node(state: ChatState) -> ChatState:
    """
    Retrieve relevant documents from Weaviate.
    """
    if state.get("query_type") == "off_topic":
        return {
            **state,
            "results": [],
            "context": "",
            "sources": [],
            "truth_metadata": {}
        }

    rag_service = get_rag_service()

    try:
        result = await rag_service.search(
            query=state["query"],
            limit=settings.retrieval_top_k,
            namespace="knowledge:faq",
        )

        return {
            **state,
            "results": result.results,
            "context": result.context,
            "sources": [r.get("source_path", "") for r in result.results],
            "truth_metadata": {
                "composition": result.truth_metadata.composition,
                "dominant_level": result.truth_metadata.dominant_level,
                "composite_confidence": result.truth_metadata.composite_confidence,
                "mixing_warning": result.truth_metadata.mixing_warning,
            },
        }

    except Exception as e:
        logger.error(f"Retrieve failed: {e}")
        return {
            **state,
            "results": [],
            "context": "",
            "sources": [],
            "truth_metadata": {},
            "error": str(e)
        }


def guardrails_node(state: ChatState) -> ChatState:
    """
    Validate retrieval results against quality thresholds.

    Checks:
    - Score >= min_score_threshold (0.70)
    - Result count >= min_results_required (3)
    - Off-topic classification
    """
    # Already classified as off-topic
    if state.get("query_type") == "off_topic":
        return {
            **state,
            "passed_guardrails": False,
            "refusal_reason": state.get("refusal_reason", "hors_sujet")
        }

    results = state.get("results", [])
    min_results = settings.min_results_required
    min_score = settings.min_score_threshold

    # No results
    if not results:
        return {
            **state,
            "passed_guardrails": False,
            "refusal_reason": "pas_de_resultats"
        }

    # Check result count
    if len(results) < min_results:
        # For ambiguous queries, be strict
        if state.get("query_type") == "ambiguous":
            return {
                **state,
                "passed_guardrails": False,
                "refusal_reason": "resultats_insuffisants"
            }

    # Check top score
    top_score = results[0].get("score", 0) if results else 0
    if top_score < min_score:
        return {
            **state,
            "passed_guardrails": False,
            "refusal_reason": "score_faible"
        }

    # All checks passed
    return {**state, "passed_guardrails": True, "refusal_reason": None}


def refuse_node(state: ChatState) -> ChatState:
    """
    Generate a refusal response with helpful guidance.
    """
    locale = state.get("user_locale", "fr")
    reason = state.get("refusal_reason", "inconnu")

    messages = {
        "fr": {
            "hors_sujet": "Je suis un assistant specialise dans les pieces automobiles et le service apres-vente. Je ne peux pas repondre a cette question.",
            "requete_invalide": "Votre question semble incomplete. Pouvez-vous la reformuler ?",
            "pas_de_resultats": "Je n'ai pas trouve d'informations pertinentes dans ma base de connaissances. Veuillez contacter notre support.",
            "resultats_insuffisants": "Je n'ai pas assez d'informations fiables pour repondre. Pouvez-vous preciser votre question ?",
            "score_faible": "Je n'ai pas assez d'informations fiables pour repondre a cette question. Veuillez contacter notre support au 01 XX XX XX XX.",
            "langue_non_supportee": "Desolee, je ne reponds qu'en francais. Veuillez reformuler votre question en francais.",
            "inconnu": "Je ne suis pas en mesure de repondre a cette question. Veuillez contacter notre support."
        },
        "en": {
            "hors_sujet": "I'm an assistant specialized in auto parts and customer service. I cannot answer this question.",
            "requete_invalide": "Your question seems incomplete. Could you please rephrase it?",
            "pas_de_resultats": "I couldn't find relevant information in my knowledge base. Please contact our support.",
            "resultats_insuffisants": "I don't have enough reliable information to answer. Could you please be more specific?",
            "score_faible": "I don't have enough reliable information to answer this question. Please contact our support.",
            "langue_non_supportee": "Sorry, I only respond in French. Please rephrase your question in French.",
            "inconnu": "I'm not able to answer this question. Please contact our support."
        }
    }

    locale_messages = messages.get(locale, messages["fr"])
    response = locale_messages.get(reason, locale_messages["inconnu"])

    return {
        **state,
        "response": response,
        "citations": []
    }


async def generate_node(state: ChatState) -> ChatState:
    """
    Generate response using Claude with context and citations.

    Note: This is a placeholder for future LLM integration.
    Currently returns formatted context with citations.
    """
    context = state.get("context", "")
    sources = state.get("sources", [])
    truth_metadata = state.get("truth_metadata", {})

    if not context:
        return {
            **state,
            "response": "Je n'ai pas trouve d'informations pertinentes.",
            "citations": []
        }

    # For now, return the context with citations
    # Future: Use Claude to generate a natural response
    dominant_level = truth_metadata.get("dominant_level", "L3")
    confidence = truth_metadata.get("composite_confidence", 0.5)

    # Build response with truth level indicator
    level_indicators = {
        "L1": "Information verifiee",
        "L2": "Regle metier",
        "L3": "Information indicative",
        "L4": "Suggestion"
    }

    indicator = level_indicators.get(dominant_level, "Information")
    confidence_pct = int(confidence * 100)

    response = f"[{indicator} - Confiance: {confidence_pct}%]\n\n{context}"

    # Add citations
    citations = [f"Source: {src}" for src in sources[:3]]

    return {
        **state,
        "response": response,
        "citations": citations
    }


def route_after_guardrails(state: ChatState) -> str:
    """Route based on guardrails result."""
    if state.get("passed_guardrails"):
        return "generate"
    return "refuse"


def build_chat_graph() -> StateGraph:
    """Build the full chat pipeline graph."""
    graph = StateGraph(ChatState)

    # Add nodes
    graph.add_node("classify", classify_node)
    graph.add_node("retrieve", retrieve_node)
    graph.add_node("guardrails", guardrails_node)
    graph.add_node("generate", generate_node)
    graph.add_node("refuse", refuse_node)

    # Set entry point
    graph.set_entry_point("classify")

    # Add edges
    graph.add_edge("classify", "retrieve")
    graph.add_edge("retrieve", "guardrails")

    # Conditional edge after guardrails
    graph.add_conditional_edges(
        "guardrails",
        route_after_guardrails,
        {"generate": "generate", "refuse": "refuse"}
    )

    graph.add_edge("generate", END)
    graph.add_edge("refuse", END)

    return graph.compile()


# Singleton graph
_chat_graph = None


def get_chat_graph():
    """Get or create the chat graph singleton."""
    global _chat_graph
    if _chat_graph is None:
        _chat_graph = build_chat_graph()
    return _chat_graph


async def run_chat_pipeline(
    query: str,
    session_id: str = "",
    user_locale: str = "fr"
) -> dict:
    """
    Run the full chat pipeline.

    Args:
        query: User query
        session_id: Session identifier
        user_locale: User locale (fr/en)

    Returns:
        dict with response, citations, and metadata
    """
    graph = get_chat_graph()

    initial_state: ChatState = {
        "query": query,
        "session_id": session_id,
        "user_locale": user_locale,
        "query_type": None,
        "results": [],
        "context": "",
        "sources": [],
        "truth_metadata": {},
        "passed_guardrails": False,
        "refusal_reason": None,
        "response": "",
        "citations": [],
        "error": None,
    }

    try:
        result = await graph.ainvoke(initial_state)

        return {
            "response": result["response"],
            "citations": result["citations"],
            "query_type": result["query_type"],
            "passed_guardrails": result["passed_guardrails"],
            "refusal_reason": result["refusal_reason"],
            "truth_metadata": result["truth_metadata"],
            "sources": result["sources"],
            "error": result.get("error")
        }

    except Exception as e:
        logger.error(f"Chat pipeline failed: {e}")
        return {
            "response": "Une erreur s'est produite. Veuillez reessayer.",
            "citations": [],
            "query_type": None,
            "passed_guardrails": False,
            "refusal_reason": "erreur_systeme",
            "truth_metadata": {},
            "sources": [],
            "error": str(e)
        }
