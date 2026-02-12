"""LangGraph RAG Flow - Full Pipeline with Guardrails and Generation."""

import logging
from typing import TypedDict, Literal, Optional

from langgraph.graph import StateGraph, END

from app.config import get_settings
from app.services.rag_service import get_rag_service

settings = get_settings()
logger = logging.getLogger(__name__)


class ChatState(TypedDict):
    query: str
    session_id: str
    user_locale: str
    vehicle_context: Optional[dict]

    query_type: Optional[Literal["on_topic", "off_topic", "ambiguous"]]

    results: list[dict]
    context: str
    sources: list[str]
    truth_metadata: dict
    clarify_questions: list[str]

    passed_guardrails: bool
    refusal_reason: Optional[str]

    response: str
    citations: list[str]

    error: Optional[str]


def classify_node(state: ChatState) -> ChatState:
    query = state["query"].lower().strip()

    if not query or len(query) < 3:
        return {**state, "query_type": "off_topic", "refusal_reason": "requete_invalide"}

    off_topic_patterns = [
        "bourse", "investir", "bitcoin", "crypto",
        "recette", "cuisine", "gateau", "chocolat",
        "meteo", "pluie", "pirater", "hacker", "password", "crack",
        "politique", "election", "president", "football", "match", "sport",
    ]
    for pattern in off_topic_patterns:
        if pattern in query:
            return {**state, "query_type": "off_topic", "refusal_reason": "hors_sujet"}

    english_patterns = [
        "brake", "noise", "when", "how to", "what is", "engine", "parts for",
        "car ", "repair", "change oil", "problem with", "issue", "stopping", "the "
    ]
    english_count = sum(1 for p in english_patterns if p in query)
    if english_count >= 2:
        return {**state, "query_type": "off_topic", "refusal_reason": "langue_non_supportee"}

    on_topic_patterns = [
        "frein", "plaquette", "disque", "huile", "filtre", "courroie", "amortisseur", "pneu",
        "batterie", "alternateur", "demarreur", "embrayage", "vidange", "entretien", "diagnostic",
        "panne", "bruit", "vibration", "temoin", "voyant", "fume", "livraison", "retour", "garantie",
        "paiement", "commande", "clio", "peugeot", "renault", "citroen", "volkswagen",
        "ece", "r90", "norme", "definition", "c'est quoi"
    ]
    for pattern in on_topic_patterns:
        if pattern in query:
            return {**state, "query_type": "on_topic"}

    return {**state, "query_type": "ambiguous"}


async def retrieve_node(state: ChatState) -> ChatState:
    if state.get("query_type") == "off_topic":
        return {
            **state,
            "results": [],
            "context": "",
            "sources": [],
            "truth_metadata": {},
            "clarify_questions": [],
        }

    rag_service = get_rag_service()

    search_query = state["query"]
    vehicle = state.get("vehicle_context")
    routing = None
    if vehicle:
        routing = vehicle.get("intent_routing")
        parts = [v for v in [vehicle.get("brand"), vehicle.get("model"), vehicle.get("engine")] if v]
        if parts:
            search_query = f"{' '.join(parts)} : {search_query}"

    namespace = "knowledge:faq"
    if isinstance(routing, dict):
        family = routing.get("intentFamily")
        if family == "catalog":
            namespace = "knowledge:gamme"
        elif family == "diagnostic":
            namespace = "knowledge:diagnostic"
        elif family == "knowledge":
            namespace = "knowledge:faq"
        elif family == "router_memory":
            namespace = "knowledge:router"

    try:
        result = await rag_service.search(
            query=search_query,
            limit=settings.retrieval_top_k,
            namespace=namespace,
            routing=routing,
        )

        return {
            **state,
            "results": result.results,
            "context": result.context,
            "sources": [r.get("source_path", "") for r in result.results],
            "clarify_questions": result.clarify_questions,
            "truth_metadata": {
                "composition": result.truth_metadata.composition,
                "dominant_level": result.truth_metadata.dominant_level,
                "composite_confidence": result.truth_metadata.composite_confidence,
                "mixing_warning": result.truth_metadata.mixing_warning,
                "contradictions": result.truth_metadata.contradictions,
                "reasoning_chain": result.truth_metadata.reasoning_chain,
                "clarify_questions": result.clarify_questions,
                "needs_clarification": result.needs_clarification,
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
            "clarify_questions": [],
            "error": str(e),
        }


def guardrails_node(state: ChatState) -> ChatState:
    if state.get("query_type") == "off_topic":
        return {**state, "passed_guardrails": False, "refusal_reason": state.get("refusal_reason", "hors_sujet")}

    results = state.get("results", [])
    min_results = settings.min_results_required
    min_score = settings.min_score_threshold
    truth = state.get("truth_metadata", {}) or {}
    needs_clarification = bool(truth.get("needs_clarification", False))
    confidence = float(truth.get("composite_confidence", 0.0) or 0.0)

    if not results:
        return {**state, "passed_guardrails": False, "refusal_reason": "pas_de_resultats"}

    # Adaptive guardrail: for ambiguous but well-supported answers, allow with 2+ results.
    required_results = min_results
    if state.get("query_type") == "ambiguous":
        required_results = min(2, min_results)

    if len(results) < required_results and not (confidence >= min_score and not needs_clarification):
        return {**state, "passed_guardrails": False, "refusal_reason": "resultats_insuffisants"}

    top_score = results[0].get("score", 0) if results else 0
    if top_score < min_score:
        return {**state, "passed_guardrails": False, "refusal_reason": "score_faible"}

    return {**state, "passed_guardrails": True, "refusal_reason": None}


def refuse_node(state: ChatState) -> ChatState:
    locale = state.get("user_locale", "fr")
    reason = state.get("refusal_reason", "inconnu")

    messages = {
        "fr": {
            "hors_sujet": "Je suis un assistant specialise dans les pieces automobiles et le service apres-vente. Je ne peux pas repondre a cette question.",
            "requete_invalide": "Votre question semble incomplete. Pouvez-vous la reformuler ?",
            "pas_de_resultats": "Je n'ai pas trouve d'informations pertinentes dans ma base de connaissances. Veuillez contacter notre support.",
            "resultats_insuffisants": "Je n'ai pas assez d'informations fiables pour repondre.",
            "score_faible": "Je n'ai pas assez d'informations fiables pour repondre a cette question.",
            "langue_non_supportee": "Desolee, je ne reponds qu'en francais. Veuillez reformuler votre question en francais.",
            "inconnu": "Je ne suis pas en mesure de repondre a cette question. Veuillez contacter notre support.",
        },
        "en": {
            "hors_sujet": "I'm an assistant specialized in auto parts and customer service. I cannot answer this question.",
            "requete_invalide": "Your question seems incomplete. Could you please rephrase it?",
            "pas_de_resultats": "I couldn't find relevant information in my knowledge base. Please contact our support.",
            "resultats_insuffisants": "I don't have enough reliable information to answer.",
            "score_faible": "I don't have enough reliable information to answer this question.",
            "langue_non_supportee": "Sorry, I only respond in French. Please rephrase your question in French.",
            "inconnu": "I'm not able to answer this question. Please contact our support.",
        },
    }

    locale_messages = messages.get(locale, messages["fr"])
    response = locale_messages.get(reason, locale_messages["inconnu"])

    clarify = (state.get("clarify_questions") or [])[:2]
    if clarify:
        response = response + "\n\nPour avancer, j'ai besoin de :\n- " + "\n- ".join(clarify)

    return {**state, "response": response, "citations": []}


async def generate_node(state: ChatState) -> ChatState:
    context = state.get("context", "")
    sources = state.get("sources", [])
    truth_metadata = state.get("truth_metadata", {})

    if not context:
        return {**state, "response": "Je n'ai pas trouve d'informations pertinentes.", "citations": []}

    dominant_level = truth_metadata.get("dominant_level", "L3")
    confidence = truth_metadata.get("composite_confidence", 0.5)

    level_indicators = {
        "L1": "Information verifiee",
        "L2": "Regle metier",
        "L3": "Information indicative",
        "L4": "Suggestion",
    }

    indicator = level_indicators.get(dominant_level, "Information")
    confidence_pct = int(confidence * 100)

    response = f"[{indicator} - Confiance: {confidence_pct}%]\n\n{context}"

    citations: list[str] = []
    seen: set[str] = set()
    for result in state.get("results", [])[:5]:
        src = str(result.get("source_uri") or result.get("source_path") or "").strip()
        if not src or src in seen:
            continue
        seen.add(src)
        citations.append(f"Source: {src}")
        if len(citations) >= 3:
            break

    if not citations:
        citations = [f"Source: {src}" for src in sources[:3]]

    return {**state, "response": response, "citations": citations}


def route_after_guardrails(state: ChatState) -> str:
    return "generate" if state.get("passed_guardrails") else "refuse"


def build_chat_graph() -> StateGraph:
    graph = StateGraph(ChatState)
    graph.add_node("classify", classify_node)
    graph.add_node("retrieve", retrieve_node)
    graph.add_node("guardrails", guardrails_node)
    graph.add_node("generate", generate_node)
    graph.add_node("refuse", refuse_node)

    graph.set_entry_point("classify")
    graph.add_edge("classify", "retrieve")
    graph.add_edge("retrieve", "guardrails")
    graph.add_conditional_edges("guardrails", route_after_guardrails, {"generate": "generate", "refuse": "refuse"})
    graph.add_edge("generate", END)
    graph.add_edge("refuse", END)
    return graph.compile()


_chat_graph = None


def get_chat_graph():
    global _chat_graph
    if _chat_graph is None:
        _chat_graph = build_chat_graph()
    return _chat_graph


async def run_chat_pipeline(
    query: str,
    session_id: str = "",
    user_locale: str = "fr",
    vehicle_context: Optional[dict] = None,
) -> dict:
    graph = get_chat_graph()

    initial_state: ChatState = {
        "query": query,
        "session_id": session_id,
        "user_locale": user_locale,
        "vehicle_context": vehicle_context,
        "query_type": None,
        "results": [],
        "context": "",
        "sources": [],
        "truth_metadata": {},
        "clarify_questions": [],
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
            "clarify_questions": result.get("clarify_questions", []),
            "error": result.get("error"),
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
            "clarify_questions": [],
            "error": str(e),
        }
