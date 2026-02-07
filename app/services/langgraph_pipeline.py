"""LangGraph RAG Pipeline - Context-Only Mode.

Architecture:
- StateGraph avec routing intelligent
- Nodes: classify, search_products, search_knowledge
- Pas de génération LLM - retourne contexte uniquement
- Truth Level awareness dans le contexte
"""

import logging
from typing import TypedDict, Literal, Optional
from langgraph.graph import StateGraph, END

from app.services.rag_service import get_rag_service

logger = logging.getLogger(__name__)


class RAGState(TypedDict):
    """State for the RAG pipeline."""
    # Input
    query: str
    session_id: str

    # Classification
    query_type: Optional[Literal["product", "knowledge", "hybrid"]]

    # Search results
    product_results: list[dict]
    knowledge_results: list[dict]

    # Context (no response - context-only mode)
    context: str

    # Metadata
    sources: list[str]
    truth_metadata: dict


def classify_query(state: RAGState) -> RAGState:
    """Classify the query type to route to appropriate search."""
    query = state["query"].lower()

    product_keywords = [
        "piece", "pièce", "reference", "référence", "prix",
        "compatible", "remplacer", "acheter", "commander",
        "plaquette", "filtre", "courroie", "amortisseur", "batterie"
    ]

    knowledge_keywords = [
        "comment", "pourquoi", "quand", "diagnostic", "probleme", "problème",
        "bruit", "vibration", "temoin", "témoin", "symptome", "symptôme",
        "livraison", "retour", "garantie", "delai", "délai"
    ]

    has_product = any(kw in query for kw in product_keywords)
    has_knowledge = any(kw in query for kw in knowledge_keywords)

    if has_product and has_knowledge:
        query_type = "hybrid"
    elif has_product:
        query_type = "product"
    else:
        query_type = "knowledge"

    logger.info(f"Query classified as: {query_type}")
    return {**state, "query_type": query_type}


async def search_products(state: RAGState) -> RAGState:
    """Search for products in Weaviate."""
    if state["query_type"] not in ["product", "hybrid"]:
        return {**state, "product_results": []}

    logger.info("Product search: delegating to main app")
    return {**state, "product_results": []}


async def search_knowledge(state: RAGState) -> RAGState:
    """Search knowledge base with Truth Level awareness."""
    rag_service = get_rag_service()

    try:
        result = await rag_service.search(
            query=state["query"],
            limit=5,
            namespace="knowledge:faq",
        )

        knowledge_results = result.results
        truth_metadata = {
            "composition": result.truth_metadata.composition,
            "dominant_level": result.truth_metadata.dominant_level,
            "composite_confidence": result.truth_metadata.composite_confidence,
            "mixing_warning": result.truth_metadata.mixing_warning,
        }

        logger.info(f"Knowledge search: {len(knowledge_results)} results")

        return {
            **state,
            "knowledge_results": knowledge_results,
            "context": result.context,
            "sources": [r.get("source_path", "") for r in knowledge_results],
            "truth_metadata": truth_metadata,
        }

    except Exception as e:
        logger.error(f"Knowledge search failed: {e}")
        return {
            **state,
            "knowledge_results": [],
            "context": "",
            "sources": [],
            "truth_metadata": {},
        }


def route_after_classify(state: RAGState) -> str:
    """Route to appropriate search based on classification."""
    query_type = state.get("query_type", "knowledge")
    if query_type in ["product", "hybrid"]:
        return "search_products"
    return "search_knowledge"


def route_after_products(state: RAGState) -> str:
    """Route after product search."""
    if state.get("query_type") == "hybrid":
        return "search_knowledge"
    return END


def build_rag_graph() -> StateGraph:
    """Build the RAG pipeline graph (Context-Only Mode)."""
    graph = StateGraph(RAGState)

    graph.add_node("classify", classify_query)
    graph.add_node("search_products", search_products)
    graph.add_node("search_knowledge", search_knowledge)

    graph.set_entry_point("classify")

    graph.add_conditional_edges(
        "classify",
        route_after_classify,
        {"search_products": "search_products", "search_knowledge": "search_knowledge"}
    )

    graph.add_conditional_edges(
        "search_products",
        route_after_products,
        {"search_knowledge": "search_knowledge", END: END}
    )

    graph.add_edge("search_knowledge", END)

    return graph.compile()


_rag_graph = None


def get_rag_graph():
    """Get or create the RAG graph singleton."""
    global _rag_graph
    if _rag_graph is None:
        _rag_graph = build_rag_graph()
    return _rag_graph


async def run_rag_pipeline(query: str, session_id: str = "") -> dict:
    """Run the full RAG pipeline (Context-Only Mode)."""
    graph = get_rag_graph()

    initial_state: RAGState = {
        "query": query,
        "session_id": session_id,
        "query_type": None,
        "product_results": [],
        "knowledge_results": [],
        "context": "",
        "sources": [],
        "truth_metadata": {},
    }

    result = await graph.ainvoke(initial_state)

    return {
        "context": result["context"],
        "sources": result["sources"],
        "query_type": result["query_type"],
        "truth_metadata": result["truth_metadata"],
    }
