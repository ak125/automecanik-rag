#!/usr/bin/env python3
"""Phase F.5 (ADR-031) — coverage + cost estimation before migrating v1 → v2.

Run this BEFORE ``migrate_kb_v1_to_v2.py --apply`` to know what you're getting
into. Output is a JSON summary suitable for CI artefacts or dashboards.

Usage :
    python scripts/migrations/estimate_v1_to_v2.py
    python scripts/migrations/estimate_v1_to_v2.py --json-out /tmp/estimate.json

Produces :
    {
      "v1_chunks_count":        <int>,
      "v2_chunks_count":        <int>,
      "remaining_to_migrate":   <int>,   # v1 count - v2 already-migrated
      "estimated_duration_sec": <float>, # crude lower-bound, batch-size-driven
      "embedding_model":        <str>,
      "estimated_cost_usd":     <float>  # 0 for the local FastEmbed model
    }
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

logger = logging.getLogger("f5.estimate_kb")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Crude per-chunk migration time : empirical for FastEmbed on the dev VPS
# is sub-millisecond (no embeddings recompute since we copy v1 vectors).
# For a Weaviate write-only batch of 500, ~50ms total round-trip.
SECONDS_PER_CHUNK = 0.001
SECONDS_PER_BATCH_OVERHEAD = 0.05
DEFAULT_BATCH_SIZE = 500

# FastEmbed (BAAI/bge-small-en-v1.5 + all-MiniLM-L6-v2) is local — $0/chunk.
# If a future PR switches to a hosted embedding API, plumb the per-1k-tokens
# cost here.
COST_USD_PER_CHUNK_BY_MODEL = {
    "all-MiniLM-L6-v2": 0.0,
    "BAAI/bge-small-en-v1.5": 0.0,
    # "text-embedding-3-small": 0.00002,  # OpenAI hypothetical
}


def estimate() -> dict:
    """Compute the estimation summary."""
    from app.config import get_settings
    settings = get_settings()

    try:
        from app.services.weaviate_client import WeaviateClient
    except ImportError as exc:
        logger.error("F.5 estimate: cannot import WeaviateClient (%s)", exc)
        return {"error": str(exc)}

    wc = WeaviateClient()
    client = wc.client

    v1_count = 0
    v2_count = 0

    if client.collections.exists("KB_Knowledge"):
        v1_count = client.collections.get(
            "KB_Knowledge"
        ).aggregate.over_all(total_count=True).total_count

    if client.collections.exists("KB_Knowledge_v2"):
        v2_count = client.collections.get(
            "KB_Knowledge_v2"
        ).aggregate.over_all(total_count=True).total_count

    # Remaining ≥ 0 (v2 may have natively-imported chunks too)
    remaining = max(0, v1_count - v2_count)

    n_batches = max(1, (remaining + DEFAULT_BATCH_SIZE - 1) // DEFAULT_BATCH_SIZE)
    est_duration = (
        remaining * SECONDS_PER_CHUNK
        + n_batches * SECONDS_PER_BATCH_OVERHEAD
    )

    cost_per_chunk = COST_USD_PER_CHUNK_BY_MODEL.get(settings.embedding_model, 0.0)
    est_cost = remaining * cost_per_chunk

    return {
        "v1_chunks_count": v1_count,
        "v2_chunks_count": v2_count,
        "remaining_to_migrate": remaining,
        "estimated_duration_sec": round(est_duration, 2),
        "embedding_model": settings.embedding_model,
        "estimated_cost_usd": round(est_cost, 4),
        "batch_size": DEFAULT_BATCH_SIZE,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-out", default=None,
                        help="Optional path to write the JSON summary")
    args = parser.parse_args()

    summary = estimate()
    rendered = json.dumps(summary, indent=2)
    print(rendered)

    if args.json_out:
        Path(args.json_out).write_text(rendered + "\n", encoding="utf-8")
        logger.info("F.5 estimate: wrote summary to %s", args.json_out)

    return 0


if __name__ == "__main__":
    sys.exit(main())
