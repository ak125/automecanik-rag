"""RAG Service - Ultra Query Pipeline (router -> multi-pass -> evidence)."""

import logging
import re
import json
from typing import Optional
from dataclasses import dataclass, field

from app.services.weaviate_client import get_weaviate_client
from app.config import get_settings

logger = logging.getLogger(__name__)

TRUTH_LEVELS = {
    "L1": {"name": "Faits vérifiés", "emoji": "✅", "weight": 1.0, "certainty": "affirme avec certitude"},
    "L2": {"name": "Règles métier", "emoji": "📋", "weight": 0.9, "certainty": "selon notre politique"},
    "L3": {"name": "Hypothèses", "emoji": "❓", "weight": 0.6, "certainty": "probablement"},
    "L4": {"name": "Heuristiques", "emoji": "💭", "weight": 0.4, "certainty": "en général"},
}

MIXING_RULES = {
    ("L1", "L2"): {"allowed": True, "warning": None},
    ("L1", "L3"): {"allowed": True, "warning": "⚠️ Mélange faits vérifiés et hypothèses"},
    ("L1", "L4"): {"allowed": False, "warning": "❌ Mélange interdit: faits et heuristiques"},
    ("L2", "L3"): {"allowed": True, "warning": "⚠️ Mélange règles métier et hypothèses"},
    ("L2", "L4"): {"allowed": True, "warning": "⚠️ Mélange règles métier et heuristiques"},
    ("L3", "L4"): {"allowed": False, "warning": "❌ Mélange interdit: trop incertain"},
}

INTENTS = {"define", "choose", "do", "maintain", "compare", "cost", "policy", "troubleshoot", "fitment"}

def _detect_intent_rules_first(question: str) -> str:
    s = question.lower()
    if any(x in s for x in ["c'est quoi", "définition", "definition", "signifie", "veut dire"]):
        return "define"
    # Fitment intent also covers "quelle piece pour <vehicule/modele>" patterns.
    if any(x in s for x in ["quelle", "quelles", "quel", "quels"]) and " pour " in s and any(
        x in s for x in ["plaquette", "plaquettes", "disque", "disques", "filtre", "amortisseur", "embrayage", "batterie"]
    ):
        return "fitment"
    if any(x in s for x in ["compatible", "compatibilité", "compatibilite", "pour ma", "pour mon", "immatriculation", "vin"]):
        return "fitment"
    if any(x in s for x in ["bruit", "vibration", "voyant", "ne freine", "pédale", "pedale", "grincement"]):
        return "troubleshoot"
    if any(x in s for x in ["quand", "intervalle", "km", "durée", "duree", "entretien"]):
        return "maintain"
    if any(x in s for x in ["choisir", "lequel", "meilleur", "recommande"]):
        return "choose"
    if any(x in s for x in ["comment", "remplacer", "monter", "installer", "purger"]):
        return "do"
    if any(x in s for x in ["comparer", "différence", "difference", "vs"]):
        return "compare"
    if any(x in s for x in ["prix", "coût", "cout", "combien"]):
        return "cost"
    if any(x in s for x in ["livraison", "retour", "garantie", "remboursement"]):
        return "policy"
    return "choose"


DOMAIN_KEYWORDS = {
    "freinage": ["frein", "plaquette", "disque", "étrier", "etrier", "purge"],
    "filtration": ["filtre", "huile", "air", "habitacle"],
    "suspension": ["amort", "suspension", "triangle", "biellette", "rotule"],
    "transmission": ["embrayage", "boîte", "boite", "cardan"],
    "electric": ["batterie", "alternateur", "démarreur", "demarreur", "capteur"],
    "moteur": ["moteur", "turbo", "injecteur", "bougie"],
}


@dataclass
class TruthMetadata:
    composition: dict = field(default_factory=dict)
    dominant_level: str = "L3"
    composite_confidence: float = 0.5
    mixing_warning: Optional[str] = None
    reasoning_chain: list = field(default_factory=list)
    contradictions: list = field(default_factory=list)


@dataclass
class SearchResponse:
    results: list[dict]
    query: str
    total: int
    context: str
    truth_metadata: TruthMetadata = field(default_factory=TruthMetadata)
    needs_clarification: bool = False
    sources_citation: str = ""
    clarify_questions: list[str] = field(default_factory=list)
    response_mode: str = "answer"


class RAGService:
    def __init__(self):
        self.weaviate = get_weaviate_client()
        self.settings = get_settings()

    async def search(
        self,
        query: str,
        limit: int = 10,
        filters: Optional[dict] = None,
        namespace: Optional[str] = None,
        routing: Optional[dict] = None,
    ) -> SearchResponse:
        plan = self._build_router_plan(query=query, routing=routing, namespace=namespace)

        logger.info(
            "Ultra query plan: intent=%s domain=%s source_plan=%s",
            plan["primary_intent"],
            plan["domain"],
            plan["source_plan"],
        )

        raw_results, pass_info = await self._run_multi_pass_retrieval(
            query=query,
            source_plan=plan["source_plan"],
            domain=plan["domain"],
            primary_intent=plan["primary_intent"],
            limit=limit,
        )

        required_evidence = self._required_evidence_count(query=query, router_plan=plan)
        evidence = self._build_evidence(raw_results, min_chunks=required_evidence, limit=limit)

        diversified_evidence = self._count_diversified_evidence(evidence)
        needs_clarification = diversified_evidence < required_evidence
        clarify_questions = self._build_clarification_questions(query=query, plan=plan)[:2] if needs_clarification else []

        if needs_clarification:
            logger.warning(
                "Evidence insufficient: got=%s expected>=%s",
                diversified_evidence,
                required_evidence,
            )

        truth_metadata = self._analyze_truth_levels(evidence)

        real_confidence, confidence_factors = self._compute_real_confidence(
            results=evidence,
            router_plan=plan,
            pass_info=pass_info,
            required_evidence=required_evidence,
        )
        truth_metadata.composite_confidence = round(real_confidence, 2)
        truth_metadata.reasoning_chain.extend(confidence_factors)

        fallback_used = any(p.get("fallback") or p.get("pass") == 3 for p in pass_info.get("passes", []))
        fallback_reason = "low_scores_or_low_evidence" if fallback_used else "none"
        response_mode = "partial" if needs_clarification and evidence else ("clarify" if needs_clarification else "answer")
        canonical_hint = (
            self._build_canonical_chunk_suggestion(plan=plan, evidence=evidence)
            if needs_clarification else None
        )

        truth_metadata.reasoning_chain.append(
            f"mode={response_mode} fallback={fallback_used} reason={fallback_reason}"
        )
        truth_metadata.reasoning_chain.append(
            f"evidence_diversified={diversified_evidence}/{required_evidence}"
        )

        if needs_clarification and clarify_questions:
            truth_metadata.reasoning_chain.append(
                "Clarification requise: " + " | ".join(clarify_questions)
            )
        if canonical_hint:
            truth_metadata.reasoning_chain.append(canonical_hint)

        context = self._format_context_with_truth(evidence, truth_metadata)
        sources_citation = self._generate_sources_citation(evidence)

        self._log_query_observability(
            query=query,
            plan=plan,
            pass_info=pass_info,
            evidence=evidence,
            response_mode=response_mode,
            fallback_reason=fallback_reason,
            needs_clarification=needs_clarification,
        )

        return SearchResponse(
            results=evidence,
            query=query,
            total=len(evidence),
            context=context,
            truth_metadata=truth_metadata,
            needs_clarification=needs_clarification,
            sources_citation=sources_citation,
            clarify_questions=clarify_questions,
            response_mode=response_mode,
        )

    def _build_router_plan(self, query: str, routing: Optional[dict], namespace: Optional[str]) -> dict:
        q = query.lower()

        primary_intent = _detect_intent_rules_first(q)
        if routing and isinstance(routing, dict):
            user_intent = routing.get("userIntent")
            if isinstance(user_intent, str) and user_intent in INTENTS:
                primary_intent = user_intent

        domain = self._infer_domain(q)
        entities = self._extract_entities(query)

        source_plan_map = {
            "troubleshoot": [self.settings.weaviate_collection_diagnostic, self.settings.weaviate_collection_knowledge],
            "fitment": [self.settings.weaviate_collection_catalog, self.settings.weaviate_collection_knowledge],
            "policy": [self.settings.weaviate_collection_knowledge],
            "define": [self.settings.weaviate_collection_knowledge, self.settings.weaviate_collection_catalog],
            "choose": [self.settings.weaviate_collection_knowledge, self.settings.weaviate_collection_catalog],
            "do": [self.settings.weaviate_collection_knowledge, self.settings.weaviate_collection_catalog],
            "maintain": [self.settings.weaviate_collection_knowledge, self.settings.weaviate_collection_catalog],
            "compare": [self.settings.weaviate_collection_knowledge, self.settings.weaviate_collection_catalog],
            # Price/cost questions are usually product-oriented: favor catalog first.
            "cost": [self.settings.weaviate_collection_catalog, self.settings.weaviate_collection_knowledge],
        }

        source_plan = source_plan_map.get(primary_intent, [self.settings.weaviate_collection_knowledge])

        if namespace or routing:
            forced = self.weaviate.resolve_collection(namespace=namespace, routing=routing)
            if forced not in source_plan:
                source_plan = [forced] + source_plan

        # Keep order, dedup
        uniq_plan = []
        seen = set()
        for c in source_plan:
            if c not in seen:
                seen.add(c)
                uniq_plan.append(c)

        clarify = []
        if primary_intent == "fitment" and not entities:
            clarify = [
                "Quel est le modele exact (marque + modele + annee) ?",
                "Avez-vous la motorisation ou le VIN ?",
            ]
        elif primary_intent == "troubleshoot" and not any(k in q for k in ["bruit", "vibration", "voyant", "panne"]):
            clarify = [
                "Quel symptome principal observez-vous ?",
                "Dans quelles conditions le probleme apparait-il ?",
            ]

        return {
            "primary_intent": primary_intent,
            "source_plan": uniq_plan,
            "domain": domain,
            "entities": entities,
            "clarify": clarify,
        }

    def _infer_domain(self, text: str) -> str:
        best_domain = "general"
        best_score = 0
        for domain, keys in DOMAIN_KEYWORDS.items():
            score = sum(1 for k in keys if k in text)
            if score > best_score:
                best_score = score
                best_domain = domain
        # Keep compatibility with indexed French label if needed.
        return "electrique" if best_domain == "electric" else best_domain

    def _extract_entities(self, text: str) -> list[str]:
        raw = re.findall(r"\b[A-Z]{2,6}\d{1,6}[A-Z0-9-]*\b", text)
        car_models = re.findall(r"\b(\d{3,4}|clio|megane|208|308|c3|c4|golf)\b", text.lower())
        entities = raw + [m.upper() for m in car_models]
        dedup = []
        seen = set()
        for e in entities:
            if e not in seen:
                seen.add(e)
                dedup.append(e)
        return dedup[:10]

    async def _run_multi_pass_retrieval(
        self,
        query: str,
        source_plan: list[str],
        domain: str,
        primary_intent: str,
        limit: int,
    ) -> tuple[list[dict], dict]:
        min_score = self.settings.min_score_threshold
        min_required = max(3, self.settings.min_results_required)

        all_results: list[dict] = []
        pass_info = {"passes": []}

        if not source_plan:
            source_plan = [self.settings.weaviate_collection_knowledge]

        pass_num = 0

        def collection_query(base_query: str, collection: str) -> str:
            # Cost queries are often noisy for catalog retrieval; keep product/vehicle signal.
            if primary_intent == "cost" and collection == self.settings.weaviate_collection_catalog:
                q = base_query.lower()
                q = re.sub(r"\b(prix|co[uû]t|combien|avant|arriere|arri[eè]re)\b", " ", q)
                q = re.sub(r"\s+", " ", q).strip()
                if q:
                    return q
            return base_query

        async def run_pass(
            collection: str,
            strict: bool,
            fallback: bool = False,
            min_score_override: Optional[float] = None,
        ) -> None:
            nonlocal pass_num
            pass_num += 1
            q = collection_query(query, collection)
            res = await self.weaviate.hybrid_search(
                query=q,
                limit=limit,
                collection_name=collection,
                domain=domain if strict else None,
                exclude_disputed=strict,
                min_score=min_score_override,
            )
            pass_info["passes"].append(
                {
                    "pass": pass_num,
                    "collection": collection,
                    "count": len(res),
                    "strict": strict,
                    "fallback": fallback,
                }
            )
            all_results.extend(res)

        # pass 1 + pass 2 (strict):
        # always run secondary collection when present, then evaluate stop conditions.
        strict_plan = source_plan[:2]
        for idx, collection in enumerate(strict_plan):
            await run_pass(collection=collection, strict=True)
            if idx == 0 and len(strict_plan) > 1:
                continue
            strong = [r for r in all_results if r.get("score", 0) >= min_score]
            if len(strong) >= min_required:
                break

        # pass 3 fallback hub (strict)
        strong = [r for r in all_results if r.get("score", 0) >= min_score]
        if len(strong) < min_required:
            await run_pass(collection=self.settings.weaviate_collection_knowledge, strict=True, fallback=True)

        # If secondary strict pass produced nothing, run it once without domain filter.
        if len(source_plan) > 1:
            secondary = source_plan[1]
            secondary_strict_count = 0
            for p in pass_info.get("passes", []):
                if p.get("collection") == secondary and p.get("strict") is True:
                    secondary_strict_count += int(p.get("count", 0) or 0)
            if secondary_strict_count == 0:
                await run_pass(collection=secondary, strict=False, fallback=True, min_score_override=0.0)

        # pass 4+ relaxed recovery if evidence remains weak
        strong = [r for r in all_results if r.get("score", 0) >= min_score]
        if len(strong) < min_required:
            relaxed_plan = list(source_plan[:2])
            if self.settings.weaviate_collection_knowledge not in relaxed_plan:
                relaxed_plan.append(self.settings.weaviate_collection_knowledge)
            for collection in relaxed_plan:
                await run_pass(collection=collection, strict=False, fallback=True)

        # dedupe by chunk_id then source_path
        deduped: list[dict] = []
        seen = set()
        for r in sorted(all_results, key=lambda x: x.get("score", 0), reverse=True):
            key = r.get("chunk_id") or r.get("source_path")
            if key and key not in seen:
                seen.add(key)
                deduped.append(r)

        return deduped[: limit * 3], pass_info


    def _build_evidence(self, results: list[dict], min_chunks: int, limit: int) -> list[dict]:
        diversified: list[dict] = []
        used_diversity_keys = set()

        sorted_results = sorted(results, key=lambda x: x.get("score", 0), reverse=True)

        # pass A: maximize diversity by provenance (source + ref + collection)
        for r in sorted_results:
            diversity_key = self._evidence_diversity_key(r)
            if diversity_key in used_diversity_keys:
                continue
            diversified.append(r)
            used_diversity_keys.add(diversity_key)
            if len(diversified) >= limit:
                break

        # pass B: fill up if too strict
        if len(diversified) < min_chunks:
            existing = {r.get("chunk_id") or r.get("source_path") for r in diversified}
            for r in sorted_results:
                key = r.get("chunk_id") or r.get("source_path")
                if key in existing:
                    continue
                diversified.append(r)
                if len(diversified) >= limit:
                    break

        return diversified[:limit]

    def _evidence_diversity_key(self, result: dict) -> tuple[str, str, str]:
        source = result.get("source_path") or result.get("source_uri") or ""
        source_ref = result.get("source_ref") or ""
        collection = result.get("collection") or ""
        return source, source_ref, collection

    def _count_diversified_evidence(self, results: list[dict]) -> int:
        if not results:
            return 0
        keys = {self._evidence_diversity_key(r) for r in results}
        return len(keys)

    def _required_evidence_count(self, query: str, router_plan: dict) -> int:
        if self._is_simple_query(query=query, router_plan=router_plan):
            # For short define/policy/cost questions, 2 diversified chunks are enough.
            return 2
        return max(3, self.settings.min_results_required)

    def _is_simple_query(self, query: str, router_plan: dict) -> bool:
        tokens = re.findall(r"\w+", query.lower())
        if not tokens:
            return True

        intent = router_plan.get("primary_intent", "choose")
        simple_intents = {"define", "policy", "cost", "compare"}
        complex_markers = {"comment", "pourquoi", "vs", "compare", "diagnostic", "compatible", "compatibilite"}

        has_complex_marker = any(marker in query.lower() for marker in complex_markers)
        has_entities = bool(router_plan.get("entities"))

        return len(tokens) <= 8 and intent in simple_intents and not has_complex_marker and not has_entities

    def _build_clarification_questions(self, query: str, plan: dict) -> list[str]:
        specific = plan.get("clarify", [])
        if specific:
            return specific

        intent = plan.get("primary_intent", "choose")
        if intent == "define":
            return [
                "Voulez-vous une definition courte ou detaillee ?",
                "Vous parlez de quel composant exactement ?",
            ]
        if intent == "policy":
            return [
                "Quelle politique cherchez-vous (livraison, retour, garantie) ?",
                "Souhaitez-vous la regle generale ou un cas precis ?",
            ]
        return [
            "Quel est le contexte exact de votre question ?",
            "Avez-vous une reference precise (modele, norme, piece) ?",
        ]

    def _build_canonical_chunk_suggestion(self, plan: dict, evidence: list[dict]) -> str:
        intent = plan.get("primary_intent", "choose")
        domain = plan.get("domain", "general")
        existing = sum(1 for r in evidence if r.get("is_canonical"))
        return (
            "Auto-improvement: proposer un chunk canonical "
            f"(intent={intent}, domain={domain}, canonical_hits={existing})"
        )

    def _analyze_truth_levels(self, results: list[dict]) -> TruthMetadata:
        if not results:
            return TruthMetadata()

        composition = {"L1": 0, "L2": 0, "L3": 0, "L4": 0}
        for r in results:
            level = r.get("truth_level", "L3")
            if level in composition:
                composition[level] += 1

        dominant_level = max(composition, key=composition.get) if any(composition.values()) else "L3"

        total_weight = 0.0
        total_count = 0
        for level, count in composition.items():
            if count > 0:
                total_weight += TRUTH_LEVELS.get(level, {}).get("weight", 0.5) * count
                total_count += count
        composite_confidence = total_weight / total_count if total_count else 0.5

        mixing_warning = self._check_mixing_rules(composition)
        contradictions = self._detect_contradictions(results)
        reasoning_chain = self._build_reasoning_chain(results)

        return TruthMetadata(
            composition=composition,
            dominant_level=dominant_level,
            composite_confidence=round(composite_confidence, 2),
            mixing_warning=mixing_warning,
            reasoning_chain=reasoning_chain,
            contradictions=contradictions,
        )

    def _compute_real_confidence(
        self,
        results: list[dict],
        router_plan: dict,
        pass_info: dict,
        required_evidence: int,
    ) -> tuple[float, list[str]]:
        if not results:
            return 0.0, ["confidence=0.00 (no results)"]

        top_n = results[: max(1, min(5, len(results)))]

        # 1) retriever score + diversity
        avg_score = sum(r.get("score", 0.0) for r in top_n) / len(top_n)
        uniq_sources = len({r.get("source_path", "") for r in top_n if r.get("source_path")})
        diversity = uniq_sources / len(top_n)

        # 2) intent/domain/entities match
        intent_target = router_plan.get("primary_intent", "")
        domain_target = router_plan.get("domain", "general")
        entities_target = set(router_plan.get("entities", []))

        intent_match = sum(1 for r in top_n if r.get("intent") == intent_target) / len(top_n)
        domain_match = sum(1 for r in top_n if r.get("domain") == domain_target or domain_target == "general") / len(top_n)
        if entities_target:
            entity_hits = 0
            for r in top_n:
                r_entities = set(r.get("entities", []) or [])
                if r_entities & entities_target:
                    entity_hits += 1
            entity_match = entity_hits / len(top_n)
        else:
            entity_match = 0.6  # neutral if no entities available

        # 3) truth + verification
        truth_scores = []
        for r in top_n:
            lvl = r.get("truth_level", "L3")
            base = TRUTH_LEVELS.get(lvl, {}).get("weight", 0.5)
            verif = r.get("verification_status", "unverified")
            if verif == "verified":
                base = min(1.0, base + 0.08)
            elif verif == "disputed":
                base = max(0.0, base - 0.20)
            truth_scores.append(base)
        truth_factor = sum(truth_scores) / len(truth_scores)

        # 4) canonical boost
        canonical_ratio = sum(1 for r in top_n if r.get("is_canonical")) / len(top_n)
        canonical_factor = min(1.0, 0.65 + 0.35 * canonical_ratio)

        # pass penalty if needed fallback pass3+
        used_fallback = any(p.get("fallback") or p.get("pass") == 3 for p in pass_info.get("passes", []))
        fallback_factor = 0.92 if used_fallback else 1.0

        # explicit penalty when evidence is below target minimum
        evidence_factor = min(1.0, self._count_diversified_evidence(results) / float(max(1, required_evidence)))

        confidence = (
            0.30 * avg_score +
            0.15 * diversity +
            0.20 * ((intent_match + domain_match + entity_match) / 3.0) +
            0.25 * truth_factor +
            0.10 * canonical_factor
        ) * fallback_factor * evidence_factor

        confidence = max(0.0, min(1.0, confidence))
        factors = [
            f"confidence_factors: avg_score={avg_score:.2f}",
            f"confidence_factors: diversity={diversity:.2f}",
            f"confidence_factors: intent={intent_match:.2f} domain={domain_match:.2f} entities={entity_match:.2f}",
            f"confidence_factors: truth={truth_factor:.2f} canonical={canonical_factor:.2f}",
            f"confidence_factors: fallback_factor={fallback_factor:.2f} evidence_factor={evidence_factor:.2f} final={confidence:.2f}",
        ]
        return confidence, factors

    def _check_mixing_rules(self, composition: dict) -> Optional[str]:
        present_levels = [level for level, count in composition.items() if count > 0]
        if len(present_levels) <= 1:
            return None

        has_high = any(level in ["L1", "L2"] for level in present_levels)
        has_low = any(level in ["L3", "L4"] for level in present_levels)
        if has_high and has_low:
            for high in ["L1", "L2"]:
                for low in ["L3", "L4"]:
                    if high in present_levels and low in present_levels:
                        rule = MIXING_RULES.get((high, low), {})
                        if rule.get("warning"):
                            return rule["warning"]
        return None

    def _detect_contradictions(self, results: list[dict]) -> list[str]:
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
        chain = []
        for i, r in enumerate(results[:5], 1):
            level = r.get("truth_level", "L3")
            title = r.get("title", "Sans titre")
            score = r.get("score", 0)
            level_info = TRUTH_LEVELS.get(level, {})
            emoji = level_info.get("emoji", "❓")
            certainty = level_info.get("certainty", "")
            chain.append(f"{i}. {emoji} [{level}] {title} (score: {score:.2f}) → {certainty}")
        return chain

    def _log_query_observability(
        self,
        query: str,
        plan: dict,
        pass_info: dict,
        evidence: list[dict],
        response_mode: str,
        fallback_reason: str,
        needs_clarification: bool,
    ) -> None:
        top = [
            {
                "chunk_id": r.get("chunk_id", ""),
                "score": round(float(r.get("score", 0.0)), 4),
                "collection": r.get("collection", ""),
            }
            for r in evidence[:5]
        ]
        logger.info(
            "observability: query=%s router=%s passes=%s top=%s mode=%s fallback_reason=%s no_evidence=%s",
            query,
            {
                "intent": plan.get("primary_intent"),
                "domain": plan.get("domain"),
                "source_plan": plan.get("source_plan"),
                "entities": plan.get("entities", []),
                "clarify": plan.get("clarify", []),
            },
            pass_info.get("passes", []),
            top,
            response_mode,
            fallback_reason,
            len(evidence) == 0 or needs_clarification,
        )

    def _format_context_with_truth(self, results: list[dict], truth_metadata: TruthMetadata) -> str:
        if not results:
            return ""

        header_parts = ["=== SEMANTIC BRAIN - CONTEXT ===\n"]
        header_parts.append("📊 Niveaux de vérité des sources:")
        for level, count in truth_metadata.composition.items():
            if count > 0:
                info = TRUTH_LEVELS.get(level, {})
                header_parts.append(f"  {info.get('emoji', '❓')} {level} ({info.get('name', level)}): {count}")

        header_parts.append(f"\n🎯 Confiance composite: {truth_metadata.composite_confidence:.0%}")
        header_parts.append(f"📌 Niveau dominant: {truth_metadata.dominant_level}")

        if truth_metadata.mixing_warning:
            header_parts.append(f"\n{truth_metadata.mixing_warning}")

        if truth_metadata.contradictions:
            header_parts.append("\n⚠️ Contradictions détectées:")
            for contradiction in truth_metadata.contradictions[:3]:
                header_parts.append(f"  - {contradiction}")

        header_parts.append("\n" + "=" * 40 + "\n")

        context_parts = []
        for i, result in enumerate(results, 1):
            level = result.get("truth_level", "L3")
            info = TRUTH_LEVELS.get(level, {})
            context_parts.append(
                f"[Source {i}] {info.get('emoji', '❓')} [{level}] {result.get('title', 'Sans titre')}\n"
                f"Niveau: {level} ({info.get('name', '')}) | Vérification: {result.get('verification_status', 'unverified')}\n"
                f"Pertinence: {result.get('score', 0):.2f} | Certainty: {info.get('certainty', '')}\n"
                f"Fichier: {result.get('source_path', '')}\n"
                f"Contenu:\n{result.get('content', '')}\n"
            )

        return "\n".join(header_parts) + "\n---\n".join(context_parts)

    def _generate_sources_citation(self, results: list[dict]) -> str:
        if not results:
            return "## Sources\nAucune source trouvée pour cette requête."

        lines = ["## Sources"]
        for i, result in enumerate(results, 1):
            filename = result.get("source_path", "unknown").split("/")[-1]
            lines.append(
                f"{i}. [{result.get('truth_level', 'L3')}] {result.get('title', 'Sans titre')} ({filename}) - "
                f"Vérification: {result.get('verification_status', 'unverified')} | Score: {result.get('score', 0):.2f}"
            )
        return "\n".join(lines)


_rag_service: Optional[RAGService] = None


def get_rag_service() -> RAGService:
    global _rag_service
    if _rag_service is None:
        _rag_service = RAGService()
    return _rag_service
