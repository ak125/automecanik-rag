#!/usr/bin/env python3
"""
Benchmark retrieval RAG — jeu fixe de requêtes avec évaluation manuelle assistée.

Mesure :
  - Top-K results (content, score, source, truth_level)
  - Signal quality (pertinent / bruit / faible)
  - Recall@5, Recall@10, MRR, nDCG@10
  - Noise ratio dans le top-5
  - Boilerplate detection

Modes :
  python3 benchmark-retrieval.py --run                    # Exécuter le benchmark
  python3 benchmark-retrieval.py --run --tag pre-clean    # Avec tag pour comparaison
  python3 benchmark-retrieval.py --compare pre-clean post-clean  # Comparer 2 runs
  python3 benchmark-retrieval.py --run --collections KB_Catalog,KB_Knowledge  # Collections spécifiques

Output : /opt/automecanik/rag/scripts/benchmarks/{tag}-{timestamp}.json
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime

# ── Config ──────────────────────────────────────────────────────────────────

WEAVIATE_HOST = "172.21.0.2"
WEAVIATE_PORT = 8080
BENCHMARK_DIR = "/opt/automecanik/rag/scripts/benchmarks"
DEFAULT_COLLECTIONS = ["KB_Catalog", "KB_Knowledge", "KB_Diagnostic"]
TOP_K = 10
ALPHA = 0.7  # hybrid blend: 70% vector, 30% BM25

# ── Benchmark queries ───────────────────────────────────────────────────────
# 40 queries across 4 intents, with expected relevance signals

BENCHMARK_QUERIES = [
    # === INFORMATIONNEL (rôle, fonctionnement, définition) ===
    {"query": "à quoi sert un filtre à huile", "intent": "informationnel",
     "expected_signals": ["filtrer", "huile moteur", "impuretés", "protéger"],
     "expected_source": "gammes/filtre-a-huile.md"},
    {"query": "rôle filtre à huile", "intent": "informationnel",
     "expected_signals": ["filtrer", "huile", "moteur"],
     "expected_source": "gammes/filtre-a-huile.md"},
    {"query": "comment fonctionne un disque de frein", "intent": "informationnel",
     "expected_signals": ["disque", "friction", "étrier", "plaquette"],
     "expected_source": "gammes/disque-de-frein.md"},
    {"query": "à quoi sert la courroie de distribution", "intent": "informationnel",
     "expected_signals": ["distribution", "synchronisation", "arbre à cames"],
     "expected_source": "gammes/courroie-de-distribution.md"},
    {"query": "rôle de l'alternateur", "intent": "informationnel",
     "expected_signals": ["alternateur", "électricité", "batterie", "recharge"],
     "expected_source": "gammes/alternateur.md"},
    {"query": "fonctionnement pompe à eau voiture", "intent": "informationnel",
     "expected_signals": ["pompe", "eau", "refroidissement", "circulation"],
     "expected_source": "gammes/pompe-a-eau.md"},
    {"query": "qu'est-ce qu'une vanne EGR", "intent": "informationnel",
     "expected_signals": ["EGR", "recirculation", "gaz", "échappement"],
     "expected_source": "gammes/vanne-egr.md"},
    {"query": "fonction du turbo sur un moteur diesel", "intent": "informationnel",
     "expected_signals": ["turbo", "suralimentation", "puissance"],
     "expected_source": "gammes/turbo.md"},
    {"query": "rôle des bougies de préchauffage", "intent": "informationnel",
     "expected_signals": ["préchauffage", "diesel", "démarrage", "froid"],
     "expected_source": "gammes/bougie-de-prechauffage.md"},
    {"query": "à quoi sert le FAP", "intent": "informationnel",
     "expected_signals": ["particules", "diesel", "filtre", "échappement"],
     "expected_source": "gammes/fap.md"},

    # === ENTRETIEN / QUAND CHANGER ===
    {"query": "quand changer filtre à huile", "intent": "entretien",
     "expected_signals": ["vidange", "km", "intervalle", "changer"],
     "expected_source": "gammes/filtre-a-huile.md"},
    {"query": "quand remplacer les plaquettes de frein", "intent": "entretien",
     "expected_signals": ["usure", "épaisseur", "km", "plaquette"],
     "expected_source": "gammes/plaquette-de-frein.md"},
    {"query": "fréquence changement courroie de distribution", "intent": "entretien",
     "expected_signals": ["km", "ans", "distribution", "intervalle"],
     "expected_source": "gammes/courroie-de-distribution.md"},
    {"query": "tous les combien changer le filtre à air", "intent": "entretien",
     "expected_signals": ["km", "filtre", "air", "remplacer"],
     "expected_source": "gammes/filtre-a-air.md"},
    {"query": "durée de vie batterie voiture", "intent": "entretien",
     "expected_signals": ["batterie", "ans", "durée", "remplacement"],
     "expected_source": "gammes/batterie.md"},
    {"query": "quand changer amortisseurs", "intent": "entretien",
     "expected_signals": ["amortisseur", "km", "usure"],
     "expected_source": "gammes/amortisseur.md"},
    {"query": "intervalle vidange liquide de frein", "intent": "entretien",
     "expected_signals": ["liquide", "frein", "purge", "ans"],
     "expected_source": None},
    {"query": "fréquence changement filtre habitacle", "intent": "entretien",
     "expected_signals": ["habitacle", "pollen", "km", "remplacer"],
     "expected_source": "gammes/filtre-d-habitacle.md"},
    {"query": "quand changer kit embrayage", "intent": "entretien",
     "expected_signals": ["embrayage", "km", "patine", "remplacement"],
     "expected_source": "gammes/kit-d-embrayage.md"},
    {"query": "durée de vie sonde lambda", "intent": "entretien",
     "expected_signals": ["sonde", "lambda", "km", "durée"],
     "expected_source": "gammes/sonde-lambda.md"},

    # === DIAGNOSTIC / SYMPTÔMES ===
    {"query": "symptômes filtre à huile bouché", "intent": "diagnostic",
     "expected_signals": ["voyant", "huile", "bruit", "cliquetis", "bouché"],
     "expected_source": "gammes/filtre-a-huile.md"},
    {"query": "bruit de grincement au freinage", "intent": "diagnostic",
     "expected_signals": ["grincement", "frein", "plaquette", "disque"],
     "expected_source": "gammes/plaquette-de-frein.md"},
    {"query": "voyant moteur allumé causes", "intent": "diagnostic",
     "expected_signals": ["voyant", "moteur", "cause", "diagnostic"],
     "expected_source": None},
    {"query": "vibration volant au freinage", "intent": "diagnostic",
     "expected_signals": ["vibration", "volant", "disque", "voilé"],
     "expected_source": "gammes/disque-de-frein.md"},
    {"query": "perte de puissance moteur diesel", "intent": "diagnostic",
     "expected_signals": ["puissance", "diesel", "turbo", "EGR", "FAP"],
     "expected_source": None},
    {"query": "bruit claquement direction", "intent": "diagnostic",
     "expected_signals": ["direction", "claquement", "rotule", "crémaillère"],
     "expected_source": None},
    {"query": "fuite liquide de refroidissement", "intent": "diagnostic",
     "expected_signals": ["fuite", "refroidissement", "durite", "radiateur"],
     "expected_source": None},
    {"query": "démarreur qui tourne dans le vide", "intent": "diagnostic",
     "expected_signals": ["démarreur", "vide", "lanceur", "bendix"],
     "expected_source": "gammes/demarreur.md"},
    {"query": "odeur huile brûlée habitacle", "intent": "diagnostic",
     "expected_signals": ["odeur", "huile", "brûlée", "fuite"],
     "expected_source": "gammes/filtre-a-huile.md"},
    {"query": "pédale de frein molle", "intent": "diagnostic",
     "expected_signals": ["pédale", "molle", "liquide", "purge", "maître-cylindre"],
     "expected_source": None},

    # === COMMERCIAL / ACHAT / COMPARAISON ===
    {"query": "meilleur filtre à huile", "intent": "commercial",
     "expected_signals": ["Mann", "Bosch", "Mahle", "qualité", "marque"],
     "expected_source": "gammes/filtre-a-huile.md"},
    {"query": "différence cartouche et spin-on filtre à huile", "intent": "commercial",
     "expected_signals": ["cartouche", "spin-on", "vissable", "différence"],
     "expected_source": "gammes/filtre-a-huile.md"},
    {"query": "plaquettes céramique ou semi-métallique", "intent": "commercial",
     "expected_signals": ["céramique", "semi-métallique", "bruit", "poussière"],
     "expected_source": "gammes/plaquette-de-frein.md"},
    {"query": "filtre à huile OEM ou adaptable", "intent": "commercial",
     "expected_signals": ["OEM", "adaptable", "aftermarket", "qualité", "prix"],
     "expected_source": "gammes/filtre-a-huile.md"},
    {"query": "quel prix plaquettes de frein", "intent": "commercial",
     "expected_signals": ["prix", "EUR", "jeu", "plaquette"],
     "expected_source": "gammes/plaquette-de-frein.md"},
    {"query": "marque Brembo ou TRW freinage", "intent": "commercial",
     "expected_signals": ["Brembo", "TRW", "qualité", "frein"],
     "expected_source": None},
    {"query": "quel filtre à air choisir", "intent": "commercial",
     "expected_signals": ["filtre", "air", "choisir", "compatible"],
     "expected_source": "gammes/filtre-a-air.md"},
    {"query": "kit distribution prix moyen", "intent": "commercial",
     "expected_signals": ["distribution", "kit", "prix"],
     "expected_source": "gammes/kit-de-distribution.md"},

    # === COMPATIBILITÉ VÉHICULE ===
    {"query": "filtre à huile Clio 4 1.5 dCi", "intent": "compatibilite",
     "expected_signals": ["filtre", "huile", "Clio", "dCi"],
     "expected_source": None},
    {"query": "plaquettes de frein Peugeot 308", "intent": "compatibilite",
     "expected_signals": ["plaquette", "frein", "308", "Peugeot"],
     "expected_source": None},
]


# ── Boilerplate detection ───────────────────────────────────────────────────

BOILERPLATE_PATTERNS = [
    re.compile(r'Skip to main content', re.I),
    re.compile(r'Skip to menu', re.I),
    re.compile(r'Partager sur', re.I),
    re.compile(r'Accepter les cookies', re.I),
    re.compile(r'Newsletter', re.I),
    re.compile(r'Nous contacter\s*$', re.I),
    re.compile(r'©\s*\d{4}', re.I),
    re.compile(r'Tous droits réservés', re.I),
]


def has_boilerplate(text):
    return any(p.search(text) for p in BOILERPLATE_PATTERNS)


# ── Weaviate search via Python client ───────────────────────────────────────

MODELS = {
    'current': 'BAAI/bge-small-en-v1.5',
    'multilingual': 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2',
}

_weaviate_client = None
_embedding_model = None
_current_model_key = 'current'


def get_weaviate_client():
    global _weaviate_client
    if _weaviate_client is None:
        import weaviate
        _weaviate_client = weaviate.connect_to_custom(
            http_host=WEAVIATE_HOST, http_port=WEAVIATE_PORT, http_secure=False,
            grpc_host=WEAVIATE_HOST, grpc_port=50051, grpc_secure=False,
        )
    return _weaviate_client


def init_embedding_model(model_key='current'):
    global _embedding_model, _current_model_key
    from fastembed import TextEmbedding
    _current_model_key = model_key
    _embedding_model = TextEmbedding(model_name=MODELS[model_key])
    return _embedding_model


def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        return init_embedding_model(_current_model_key)
    return _embedding_model


def embed_query(query):
    model = get_embedding_model()
    return list(model.embed([query]))[0].tolist()


def vector_search(query, collections, limit=TOP_K):
    """Run nearVector search across multiple collections."""
    client = get_weaviate_client()
    query_vec = embed_query(query)

    all_results = []
    props = ['title', 'content', 'source_type', 'source_path',
             'truth_level', 'category', 'domain', 'evidence_grade']

    for coll_name in collections:
        try:
            coll = client.collections.get(coll_name)
            results = coll.query.near_vector(
                near_vector=query_vec,
                limit=limit,
                return_metadata=['distance'],
                return_properties=props,
            )
            for obj in results.objects:
                r = {}
                for p in props:
                    r[p] = obj.properties.get(p, '')
                # Convert distance to similarity score (lower distance = higher score)
                dist = obj.metadata.distance if obj.metadata else 1.0
                r['score'] = round(max(0, 1.0 - dist), 4)
                r['distance'] = round(dist, 4)
                r['collection'] = coll_name
                all_results.append(r)
        except Exception as e:
            print(f"  ERROR querying {coll_name}: {e}")

    # Sort by score descending, deduplicate
    all_results.sort(key=lambda x: x["score"], reverse=True)

    seen = set()
    deduped = []
    for r in all_results:
        content_key = hashlib.md5((r.get("content", "") or "")[:200].encode()).hexdigest()
        if content_key not in seen:
            seen.add(content_key)
            deduped.append(r)

    return deduped[:limit]


def cleanup_client():
    global _weaviate_client
    if _weaviate_client:
        _weaviate_client.close()
        _weaviate_client = None


# ── Scoring ─────────────────────────────────────────────────────────────────

def auto_judge(result, query_info):
    """Auto-judge a result based on expected signals and source."""
    content = (result.get("content", "") or "").lower()
    title = (result.get("title", "") or "").lower()
    source_path = result.get("source_path", "") or ""
    text = f"{title} {content}"

    # Check signal match
    signals = query_info["expected_signals"]
    matched = sum(1 for s in signals if s.lower() in text)
    signal_ratio = matched / max(len(signals), 1)

    # Check source match
    expected = query_info.get("expected_source")
    source_match = expected and expected in source_path

    # Check boilerplate
    is_noisy = has_boilerplate(content)

    # Check empty/thin content
    is_thin = len(content.strip()) < 50

    # Scoring
    if is_thin or is_noisy:
        relevance = "noise"
    elif source_match and signal_ratio >= 0.5:
        relevance = "perfect"
    elif signal_ratio >= 0.6:
        relevance = "good"
    elif signal_ratio >= 0.3:
        relevance = "partial"
    else:
        relevance = "weak"

    return {
        "relevance": relevance,
        "signal_ratio": round(signal_ratio, 2),
        "signals_matched": matched,
        "signals_total": len(signals),
        "source_match": source_match,
        "has_boilerplate": is_noisy,
        "is_thin": is_thin,
    }


def compute_metrics(query_results):
    """Compute IR metrics from judged results."""
    # Relevance mapping: perfect/good = relevant, partial = marginal, weak/noise = irrelevant
    relevance_map = {"perfect": 3, "good": 2, "partial": 1, "weak": 0, "noise": 0}

    metrics = {
        "recall_at_5": 0,
        "recall_at_10": 0,
        "mrr": 0,
        "ndcg_at_10": 0,
        "noise_at_5": 0,
        "signal_at_5": 0,
        "boilerplate_at_5": 0,
    }

    judgments = query_results.get("judgments", [])
    if not judgments:
        return metrics

    # Recall@K: fraction of top-K results that are at least "partial"
    relevant_at_5 = sum(1 for j in judgments[:5] if j["relevance"] in ("perfect", "good", "partial"))
    relevant_at_10 = sum(1 for j in judgments[:10] if j["relevance"] in ("perfect", "good", "partial"))
    metrics["recall_at_5"] = round(relevant_at_5 / min(5, len(judgments)), 3)
    metrics["recall_at_10"] = round(relevant_at_10 / min(10, len(judgments)), 3)

    # MRR: reciprocal rank of first relevant result
    for i, j in enumerate(judgments):
        if j["relevance"] in ("perfect", "good"):
            metrics["mrr"] = round(1.0 / (i + 1), 3)
            break

    # nDCG@10
    import math
    dcg = sum(relevance_map.get(j["relevance"], 0) / math.log2(i + 2) for i, j in enumerate(judgments[:10]))
    ideal = sorted([relevance_map.get(j["relevance"], 0) for j in judgments[:10]], reverse=True)
    idcg = sum(v / math.log2(i + 2) for i, v in enumerate(ideal))
    metrics["ndcg_at_10"] = round(dcg / idcg, 3) if idcg > 0 else 0

    # Noise/signal at 5
    noise_5 = sum(1 for j in judgments[:5] if j["relevance"] in ("noise", "weak"))
    signal_5 = sum(1 for j in judgments[:5] if j["relevance"] in ("perfect", "good"))
    bp_5 = sum(1 for j in judgments[:5] if j.get("has_boilerplate"))
    metrics["noise_at_5"] = round(noise_5 / min(5, len(judgments)), 3)
    metrics["signal_at_5"] = round(signal_5 / min(5, len(judgments)), 3)
    metrics["boilerplate_at_5"] = round(bp_5 / min(5, len(judgments)), 3)

    return metrics


# ── Main ────────────────────────────────────────────────────────────────────

def run_benchmark(tag, collections):
    """Run the full benchmark."""
    os.makedirs(BENCHMARK_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{tag}-{timestamp}.json"
    filepath = os.path.join(BENCHMARK_DIR, filename)

    print(f"\n{'='*60}")
    print(f"  RAG Retrieval Benchmark — {tag}")
    print(f"  Collections: {', '.join(collections)}")
    print(f"  Queries: {len(BENCHMARK_QUERIES)}")
    print(f"  Top-K: {TOP_K}, Alpha: {ALPHA}")
    print(f"{'='*60}\n")

    all_query_results = []
    agg_metrics = {
        "recall_at_5": [], "recall_at_10": [], "mrr": [],
        "ndcg_at_10": [], "noise_at_5": [], "signal_at_5": [],
        "boilerplate_at_5": [],
    }

    for i, q in enumerate(BENCHMARK_QUERIES):
        query = q["query"]
        intent = q["intent"]

        print(f"  [{i+1}/{len(BENCHMARK_QUERIES)}] {intent:15s} | {query}")

        results = vector_search(query, collections)

        # Auto-judge each result
        judgments = []
        for r in results:
            j = auto_judge(r, q)
            j["title"] = (r.get("title") or "")[:80]
            j["source_path"] = r.get("source_path", "")
            j["score"] = r.get("score", 0)
            j["truth_level"] = r.get("truth_level", "")
            j["collection"] = r.get("collection", "")
            j["content_preview"] = (r.get("content") or "")[:200]
            judgments.append(j)

        query_result = {
            "query": query,
            "intent": intent,
            "expected_source": q.get("expected_source"),
            "judgments": judgments,
            "result_count": len(results),
        }

        # Compute metrics
        metrics = compute_metrics(query_result)
        query_result["metrics"] = metrics

        # Accumulate
        for k in agg_metrics:
            agg_metrics[k].append(metrics[k])

        # Print summary
        top3_labels = [j["relevance"][:4] for j in judgments[:3]]
        print(f"           → top3: {' '.join(top3_labels):12s} | "
              f"R@5={metrics['recall_at_5']:.2f} MRR={metrics['mrr']:.2f} "
              f"noise={metrics['noise_at_5']:.0%}")

        all_query_results.append(query_result)

    # Aggregate metrics
    avg_metrics = {}
    for k, values in agg_metrics.items():
        avg_metrics[k] = round(sum(values) / max(len(values), 1), 3)

    # Per-intent breakdown
    intent_metrics = {}
    for intent in ["informationnel", "entretien", "diagnostic", "commercial", "compatibilite"]:
        intent_qs = [qr for qr in all_query_results if qr["intent"] == intent]
        if intent_qs:
            intent_metrics[intent] = {}
            for k in agg_metrics:
                vals = [qr["metrics"][k] for qr in intent_qs]
                intent_metrics[intent][k] = round(sum(vals) / len(vals), 3)

    # Build report (Correction #3 — frozen protocol in manifest)
    report = {
        "meta": {
            "tag": tag,
            "timestamp": timestamp,
            "collections": collections,
            "query_count": len(BENCHMARK_QUERIES),
            "query_set_version": "v1.0-40q-5intents",
            "relevance_judgments_version": "auto-v1.0-signal-match",
            # Protocol
            "search_mode": "near_vector",
            "hybrid_alpha": ALPHA,
            "top_k": TOP_K,
            "reranker_enabled": False,
            "filters_enabled": False,
            "query_normalization": "none",
            # Embedding
            "query_embedding_model": MODELS[_current_model_key],
            "query_model_key": _current_model_key,
            # Infra
            "weaviate_host": WEAVIATE_HOST,
        },
        "aggregate_metrics": avg_metrics,
        "intent_metrics": intent_metrics,
        "queries": all_query_results,
    }

    # Save
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    # Print summary
    print(f"\n{'='*60}")
    print(f"  RÉSULTATS AGRÉGÉS")
    print(f"{'='*60}")
    print(f"  Recall@5:      {avg_metrics['recall_at_5']:.3f}")
    print(f"  Recall@10:     {avg_metrics['recall_at_10']:.3f}")
    print(f"  MRR:           {avg_metrics['mrr']:.3f}")
    print(f"  nDCG@10:       {avg_metrics['ndcg_at_10']:.3f}")
    print(f"  Signal@5:      {avg_metrics['signal_at_5']:.1%}")
    print(f"  Noise@5:       {avg_metrics['noise_at_5']:.1%}")
    print(f"  Boilerplate@5: {avg_metrics['boilerplate_at_5']:.1%}")

    print(f"\n  PAR INTENTION:")
    for intent, m in intent_metrics.items():
        print(f"    {intent:18s} R@5={m['recall_at_5']:.2f}  MRR={m['mrr']:.2f}  "
              f"noise={m['noise_at_5']:.0%}  signal={m['signal_at_5']:.0%}")

    print(f"\n  Rapport sauvé: {filepath}")
    print(f"{'='*60}")

    cleanup_client()
    return filepath


def compare_benchmarks(tag1, tag2):
    """Compare two benchmark runs."""
    # Find latest files matching tags
    files = sorted(os.listdir(BENCHMARK_DIR))

    def find_latest(tag):
        matches = [f for f in files if f.startswith(tag + "-")]
        return os.path.join(BENCHMARK_DIR, matches[-1]) if matches else None

    f1, f2 = find_latest(tag1), find_latest(tag2)
    if not f1 or not f2:
        print(f"  ERROR: Cannot find benchmarks for '{tag1}' and/or '{tag2}'")
        print(f"  Available: {files}")
        return

    with open(f1) as fh:
        r1 = json.load(fh)
    with open(f2) as fh:
        r2 = json.load(fh)

    m1, m2 = r1["aggregate_metrics"], r2["aggregate_metrics"]

    print(f"\n{'='*60}")
    print(f"  COMPARAISON: {tag1} vs {tag2}")
    print(f"{'='*60}")
    print(f"  {'Metric':20s} {'':>10s} {'':>10s} {'Delta':>10s}")
    print(f"  {'':20s} {tag1:>10s} {tag2:>10s} {'':>10s}")
    print(f"  {'-'*50}")

    for k in ["recall_at_5", "recall_at_10", "mrr", "ndcg_at_10", "signal_at_5", "noise_at_5", "boilerplate_at_5"]:
        v1, v2 = m1.get(k, 0), m2.get(k, 0)
        delta = v2 - v1
        arrow = "↑" if delta > 0.01 else "↓" if delta < -0.01 else "="
        # For noise/boilerplate, lower is better
        if k in ("noise_at_5", "boilerplate_at_5"):
            arrow = "↓" if delta < -0.01 else "↑" if delta > 0.01 else "="
            color = "✅" if delta < 0 else "⚠️" if delta > 0 else "  "
        else:
            color = "✅" if delta > 0 else "⚠️" if delta < 0 else "  "
        print(f"  {k:20s} {v1:10.3f} {v2:10.3f} {delta:+10.3f} {arrow} {color}")

    # Per-intent comparison
    i1, i2 = r1.get("intent_metrics", {}), r2.get("intent_metrics", {})
    print(f"\n  PAR INTENTION (MRR):")
    for intent in ["informationnel", "entretien", "diagnostic", "commercial", "compatibilite"]:
        v1 = i1.get(intent, {}).get("mrr", 0)
        v2 = i2.get(intent, {}).get("mrr", 0)
        delta = v2 - v1
        arrow = "↑" if delta > 0.01 else "↓" if delta < -0.01 else "="
        print(f"    {intent:18s} {v1:.3f} → {v2:.3f} ({delta:+.3f} {arrow})")

    print(f"{'='*60}")


def main():
    parser = argparse.ArgumentParser(description='RAG Retrieval Benchmark')
    parser.add_argument('--run', action='store_true', help='Exécuter le benchmark')
    parser.add_argument('--tag', type=str, default='baseline', help='Tag pour identifier ce run')
    parser.add_argument('--collections', type=str, help='Collections Weaviate (comma-separated)')
    parser.add_argument('--model', type=str, default='current',
                        choices=list(MODELS.keys()),
                        help='Modèle embedding pour les requêtes (current ou multilingual)')
    parser.add_argument('--compare', nargs=2, metavar=('TAG1', 'TAG2'), help='Comparer 2 runs')
    args = parser.parse_args()

    if args.compare:
        compare_benchmarks(args.compare[0], args.compare[1])
    elif args.run:
        # Init embedding model matching the index being tested
        init_embedding_model(args.model)
        collections = args.collections.split(',') if args.collections else DEFAULT_COLLECTIONS
        run_benchmark(args.tag, collections)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
