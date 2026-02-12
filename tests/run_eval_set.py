#!/usr/bin/env python3
"""Run Ultra eval set and compute key retrieval metrics."""

import argparse
import json
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import httpx


def load_eval_set(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def post_json(
    url: str,
    endpoint: str,
    payload: dict,
    api_key: str,
    timeout: int = 30,
    max_retries: int = 30,
    retry_delay: float = 2.0,
) -> dict:
    for attempt in range(max_retries):
        r = httpx.post(
            f"{url}{endpoint}",
            json=payload,
            headers={"X-RAG-API-Key": api_key},
            timeout=timeout,
        )
        if r.status_code == 429 and attempt < (max_retries - 1):
            import time
            retry_after = r.headers.get("Retry-After")
            if retry_after:
                try:
                    delay = float(retry_after)
                except ValueError:
                    delay = min(retry_delay * (1.3 ** attempt), 30.0)
            else:
                delay = min(retry_delay * (1.3 ** attempt), 30.0)
            time.sleep(delay)
            continue
        r.raise_for_status()
        return r.json()
    raise RuntimeError(f"Request failed after retries: {endpoint}")


def infer_fallback(chat_truth_metadata: dict) -> bool:
    chain = chat_truth_metadata.get("reasoning_chain", []) or []
    for item in chain:
        if isinstance(item, str) and "fallback=True" in item:
            return True
    return False


def infer_mode(chat_payload: dict) -> str:
    if not chat_payload.get("passed_guardrails", False):
        if chat_payload.get("clarify_questions"):
            return "clarify"
        return "refuse"
    return "answer"


def run_eval(base_url: str, api_key: str, eval_data: dict) -> dict:
    k = int(eval_data.get("k", 5))
    items = eval_data.get("items", [])

    by_collection_total = defaultdict(int)
    by_collection_hit = defaultdict(int)

    fallback_count = 0
    no_evidence_count = 0
    satisfied_count = 0

    detailed = []
    import time

    for item in items:
        query = item["query"]
        expected_collections = item.get("expected_collections", [])
        expected_mode = item.get("expected_mode", "answer")
        min_conf = float(item.get("min_confidence", 0.55))

        search_resp = post_json(base_url, "/search", {"query": query, "limit": k}, api_key)
        time.sleep(0.8)
        chat_resp = post_json(base_url, "/chat/v2", {"message": query, "locale": "fr"}, api_key)
        time.sleep(1.2)

        top_results = search_resp.get("results", [])[:k]
        retrieved_collections = {r.get("collection", "") for r in top_results if r.get("collection")}

        for c in expected_collections:
            by_collection_total[c] += 1
            if c in retrieved_collections:
                by_collection_hit[c] += 1

        truth = chat_resp.get("truth_metadata", {})
        conf = float(truth.get("composite_confidence", 0.0) or 0.0)
        needs_clarification = bool(truth.get("needs_clarification", False))
        fallback = infer_fallback(truth)
        mode = infer_mode(chat_resp)

        if fallback:
            fallback_count += 1
        if needs_clarification:
            no_evidence_count += 1

        satisfied = False
        if expected_mode == "answer":
            satisfied = mode == "answer" and conf >= min_conf and not needs_clarification
        elif expected_mode == "clarify":
            satisfied = mode == "clarify"
        elif expected_mode == "refuse":
            satisfied = mode == "refuse"

        if satisfied:
            satisfied_count += 1

        detailed.append(
            {
                "id": item.get("id"),
                "query": query,
                "expected_collections": expected_collections,
                "retrieved_collections": sorted(retrieved_collections),
                "mode": mode,
                "fallback": fallback,
                "needs_clarification": needs_clarification,
                "confidence": round(conf, 4),
                "satisfied": satisfied,
            }
        )

    n = max(1, len(items))

    recall_at_k_by_collection = {}
    for c, total in by_collection_total.items():
        hit = by_collection_hit[c]
        recall_at_k_by_collection[c] = round(hit / total, 4) if total else 0.0

    summary = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "total_queries": len(items),
        "k": k,
        "recall_at_k_by_collection": recall_at_k_by_collection,
        "fallback_rate": round(fallback_count / n, 4),
        "no_evidence_rate": round(no_evidence_count / n, 4),
        "satisfaction": round(satisfied_count / n, 4),
    }

    return {"summary": summary, "details": detailed}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Ultra eval set")
    parser.add_argument("--url", default="http://127.0.0.1:8000")
    parser.add_argument("--api-key", default="")
    parser.add_argument("--eval-set", default="tests/eval_set.json")
    parser.add_argument("--out", default="tests/eval_report.json")
    args = parser.parse_args()

    eval_path = Path(args.eval_set)
    if not eval_path.exists():
        raise SystemExit(f"Eval set not found: {eval_path}")

    api_key = args.api_key or os.getenv("RAG_API_KEY", "")
    if not api_key:
        raise SystemExit("Missing API key: pass --api-key or set RAG_API_KEY")

    data = load_eval_set(eval_path)
    report = run_eval(args.url, api_key, data)

    out = Path(args.out)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    print(f"Report written to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
