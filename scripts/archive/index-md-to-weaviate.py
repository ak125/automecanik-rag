#!/usr/bin/env python3
"""
Index .md enrichis → collection Weaviate de test.

Markdown-first, index-second. Ce script ne fait que PROJETER les .md dans Weaviate.
Il ne modifie aucun fichier. Il ne contient rien qui n'existe pas dans les .md.

Architecture A/B :
  Bench_A : corpus nettoyé + embedding actuel (bge-small-en-v1.5)
  Bench_B : corpus nettoyé + embedding multilingual

Garanties :
  - Preflight validation (YAML, doc_id, content_hash, truth_level, corps non vide)
  - Idempotence par UUID déterministe (source_path + chunk_index + content_hash)
  - Exclusion explicite des L4
  - Dry-run
  - Manifest JSON enrichi (chunker params, protocole, git_sha)

Usage :
  python3 index-md-to-weaviate.py --dry-run                                    # Compter
  python3 index-md-to-weaviate.py --collection Bench_A                          # Index A
  python3 index-md-to-weaviate.py --collection Bench_B --model multilingual     # Index B
  python3 index-md-to-weaviate.py --dry-run --only gammes                       # Seulement gammes/
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone

import yaml

sys.path.insert(0, '/opt/automecanik/rag')
from orchestrator.processors.chunker import TokenAwareChunker

# ── Config ──────────────────────────────────────────────────────────────────

KNOWLEDGE_DIR = '/opt/automecanik/rag/knowledge'
BENCHMARK_DIR = '/opt/automecanik/rag/scripts/benchmarks'

WEAVIATE_HOST = '172.21.0.2'
WEAVIATE_PORT = 8080
WEAVIATE_GRPC_PORT = 50051

INDEX_DIRS = ['gammes', 'diagnostic', 'constructeurs', 'guides', 'faq',
              'policies', 'vehicles', 'web', 'web-catalog', 'reference',
              'canonical']

ALLOWED_TRUTH_LEVELS = {'L1', 'L2', 'L3'}

MODELS = {
    'current': 'BAAI/bge-small-en-v1.5',
    'multilingual': 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2',
}

# Chunker params — frozen for benchmark reproducibility
CHUNKER_VERSION = '1.0'
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
FAQ_ATOMIC = True
PROCEDURE_ATOMIC = True

EMBED_BATCH_SIZE = 32

# Weaviate collection schema
COLLECTION_PROPERTIES = [
    {"name": "doc_id", "dataType": ["text"]},
    {"name": "title", "dataType": ["text"]},
    {"name": "content", "dataType": ["text"]},
    {"name": "content_hash", "dataType": ["text"]},
    {"name": "source_type", "dataType": ["text"]},
    {"name": "source_path", "dataType": ["text"]},
    {"name": "truth_level", "dataType": ["text"]},
    {"name": "category", "dataType": ["text"]},
    {"name": "domain", "dataType": ["text"]},
    {"name": "lang", "dataType": ["text"]},
    {"name": "evidence_grade", "dataType": ["text"]},
    {"name": "chunk_index", "dataType": ["int"]},
    {"name": "chunk_type", "dataType": ["text"]},
    {"name": "heading", "dataType": ["text"]},
    {"name": "heading_level", "dataType": ["int"]},
    {"name": "is_atomic", "dataType": ["boolean"]},
    {"name": "intent", "dataType": ["text"]},
]

# ── Helpers ─────────────────────────────────────────────────────────────────

def log(msg):
    ts = time.strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{ts}] {msg}"
    print(line, flush=True)


def get_git_sha():
    try:
        return subprocess.check_output(
            ['git', 'rev-parse', '--short', 'HEAD'],
            cwd='/opt/automecanik/app', stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        return 'unknown'


def parse_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()
    if not raw.startswith('---'):
        return {}, raw
    parts = raw.split('---', 2)
    if len(parts) < 3:
        return {}, raw
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return None, raw  # None = YAML invalid
    return meta, parts[2]


def classify_domain(text):
    t = text.lower()
    domains = {
        'freinage': ['frein', 'plaquette', 'disque', 'étrier', 'abs'],
        'filtration': ['filtre', 'filtration', 'huile moteur'],
        'moteur': ['moteur', 'piston', 'culasse', 'soupape', 'vilebrequin'],
        'transmission': ['embrayage', 'boîte', 'cardan', 'transmission'],
        'suspension': ['amortisseur', 'suspension', 'ressort', 'rotule'],
        'direction': ['direction', 'crémaillère', 'volant'],
        'electrique': ['alternateur', 'démarreur', 'batterie', 'bougie'],
        'refroidissement': ['radiateur', 'refroidissement', 'thermostat'],
        'echappement': ['échappement', 'catalyseur', 'FAP', 'silencieux'],
        'climatisation': ['climatisation', 'compresseur clim', 'condenseur'],
    }
    for domain, keywords in domains.items():
        if any(kw in t for kw in keywords):
            return domain
    return 'general'


def classify_intent(text):
    t = text.lower()
    if any(w in t for w in ['diagnostic', 'symptôme', 'voyant', 'bruit', 'panne']):
        return 'troubleshoot'
    if any(w in t for w in ['comment', 'procédure', 'étape', 'remplacer', 'changer']):
        return 'do'
    if any(w in t for w in ['choisir', 'quel', 'meilleur', 'comparatif']):
        return 'choose'
    if any(w in t for w in ['prix', 'coût', 'budget', 'tarif']):
        return 'cost'
    if any(w in t for w in ['entretien', 'intervalle', 'vidange', 'quand']):
        return 'maintain'
    if any(w in t for w in ['définition', 'rôle', 'fonction']):
        return 'define'
    return 'general'


# ── Preflight validation (Correction #4) ───────────────────────────────────

def preflight_validate(filepath, meta, body):
    """Validate a .md file before indexation. Returns (ok, reasons)."""
    reasons = []

    if meta is None:
        return False, ['yaml_invalid']

    if not meta:
        reasons.append('yaml_empty')

    if not meta.get('doc_id'):
        reasons.append('doc_id_missing')

    if not meta.get('truth_level'):
        reasons.append('truth_level_missing')

    truth = meta.get('truth_level', '')
    if truth not in ALLOWED_TRUTH_LEVELS:
        reasons.append(f'truth_level_excluded:{truth}')

    if not meta.get('source_type'):
        reasons.append('source_type_missing')

    body_stripped = body.strip() if body else ''
    if len(body_stripped) < 50:
        reasons.append(f'body_too_short:{len(body_stripped)}')

    return len(reasons) == 0, reasons


# ── Document collection ────────────────────────────────────────────────────

def collect_documents(dirs_filter=None):
    """Collect .md files, preflight validate, return (docs, skipped, failed)."""
    docs = []
    skipped_l4 = 0
    failed = []
    dirs = dirs_filter if dirs_filter else INDEX_DIRS

    for dirname in dirs:
        dirpath = os.path.join(KNOWLEDGE_DIR, dirname)
        if not os.path.isdir(dirpath):
            continue

        for filename in sorted(os.listdir(dirpath)):
            if not filename.endswith('.md'):
                continue

            filepath = os.path.join(dirpath, filename)
            meta, body = parse_md(filepath)
            rel_path = f"{dirname}/{filename}"

            # Preflight validation
            ok, reasons = preflight_validate(filepath, meta, body)
            if not ok:
                if any('truth_level_excluded' in r for r in reasons):
                    skipped_l4 += 1
                else:
                    failed.append({'file': rel_path, 'reasons': reasons})
                continue

            doc_id = meta.get('doc_id', '')
            if not doc_id:
                doc_id = str(uuid.uuid5(uuid.NAMESPACE_URL, rel_path))

            docs.append({
                'filepath': filepath,
                'rel_path': rel_path,
                'meta': meta,
                'body': body,
                'doc_id': doc_id,
                'content_hash': meta.get('content_hash', ''),
                'truth_level': meta.get('truth_level', 'L2'),
            })

    return docs, skipped_l4, failed


# ── Chunking ───────────────────────────────────────────────────────────────

def chunk_documents(docs):
    chunker = TokenAwareChunker(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    all_chunks = []
    for doc in docs:
        raw_chunks = chunker.chunk(doc['body'])
        meta = doc['meta']
        title = meta.get('title', '')
        source_type = meta.get('source_type', 'unknown')
        category = meta.get('category', '')
        lang = meta.get('lang', 'fr')

        for chunk in raw_chunks:
            content = chunk['content']
            chunk_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()[:16]

            all_chunks.append({
                'doc_id': doc['doc_id'],
                'content_hash': f"sha256:{chunk_hash}",
                'chunk_uuid': str(uuid.uuid5(
                    uuid.NAMESPACE_URL,
                    f"{doc['rel_path']}:{chunk['chunk_index']}:{chunk_hash}"
                )),
                'title': title,
                'content': content,
                'source_type': source_type,
                'source_path': doc['rel_path'],
                'truth_level': doc['truth_level'],
                'category': category,
                'lang': lang,
                'domain': classify_domain(f"{title} {content}"),
                'intent': classify_intent(content),
                'evidence_grade': 'B' if doc['truth_level'] in ('L1', 'L2') else 'C',
                'chunk_index': chunk['chunk_index'],
                'chunk_type': chunk.get('chunk_type', 'text'),
                'heading': chunk.get('heading', ''),
                'heading_level': chunk.get('heading_level', 0) or 0,
                'is_atomic': chunk.get('is_atomic', False),
            })

    return all_chunks


# ── Embedding ──────────────────────────────────────────────────────────────

def embed_chunks(chunks, model_key='current'):
    from fastembed import TextEmbedding
    model_name = MODELS[model_key]
    log(f"  Loading embedding model: {model_name}")
    model = TextEmbedding(model_name=model_name)

    texts = [c['content'] for c in chunks]
    log(f"  Embedding {len(texts)} chunks (batch_size={EMBED_BATCH_SIZE})...")

    vectors = []
    for i in range(0, len(texts), EMBED_BATCH_SIZE):
        batch = texts[i:i + EMBED_BATCH_SIZE]
        batch_vecs = list(model.embed(batch))
        vectors.extend([v.tolist() for v in batch_vecs])
        if (i // EMBED_BATCH_SIZE) % 50 == 0 and i > 0:
            log(f"    {i}/{len(texts)} embedded...")

    log(f"  Embedding complete: {len(vectors)} vectors, dim={len(vectors[0])}")
    return vectors, len(vectors[0])


# ── Weaviate upsert ────────────────────────────────────────────────────────

def ensure_collection(client, collection_name):
    import weaviate.classes.config as wc

    existing = [c for c in client.collections.list_all()]
    if collection_name in existing:
        log(f"  Collection {collection_name} exists — will upsert")
        return

    log(f"  Creating collection {collection_name}...")
    properties = []
    for prop in COLLECTION_PROPERTIES:
        dtype = prop['dataType'][0]
        if dtype == 'text':
            properties.append(wc.Property(name=prop['name'], data_type=wc.DataType.TEXT))
        elif dtype == 'int':
            properties.append(wc.Property(name=prop['name'], data_type=wc.DataType.INT))
        elif dtype == 'boolean':
            properties.append(wc.Property(name=prop['name'], data_type=wc.DataType.BOOL))

    client.collections.create(
        name=collection_name,
        properties=properties,
        vectorizer_config=wc.Configure.Vectorizer.none(),
    )
    log(f"  Collection {collection_name} created")


def upsert_to_weaviate(chunks, vectors, collection_name):
    import weaviate
    client = weaviate.connect_to_custom(
        http_host=WEAVIATE_HOST, http_port=WEAVIATE_PORT, http_secure=False,
        grpc_host=WEAVIATE_HOST, grpc_port=WEAVIATE_GRPC_PORT, grpc_secure=False,
    )

    try:
        ensure_collection(client, collection_name)
        collection = client.collections.get(collection_name)

        inserted = 0
        errors = 0
        batch_size = 100

        for i in range(0, len(chunks), batch_size):
            batch_chunks = chunks[i:i + batch_size]
            batch_vectors = vectors[i:i + batch_size]

            with collection.batch.fixed_size(batch_size=batch_size) as batch:
                for chunk, vector in zip(batch_chunks, batch_vectors):
                    props = {k: v for k, v in chunk.items() if k != 'chunk_uuid'}
                    try:
                        batch.add_object(
                            properties=props,
                            vector=vector,
                            uuid=chunk['chunk_uuid'],
                        )
                        inserted += 1
                    except Exception as e:
                        errors += 1
                        if errors <= 5:
                            log(f"    ERROR upsert: {str(e)[:100]}")

            if (i // batch_size) % 10 == 0 and i > 0:
                log(f"    {i}/{len(chunks)} upserted...")

        log(f"  Upsert complete: {inserted} inserted, {errors} errors")
        return inserted, errors

    finally:
        client.close()


# ── Manifest (Correction #3 + #6) ──────────────────────────────────────────

def save_manifest(tag, model_key, collection_name, docs, chunks,
                  skipped_l4, failed, inserted, embedding_dims,
                  started_at, finished_at):
    os.makedirs(BENCHMARK_DIR, exist_ok=True)

    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    run_id = f"{tag}-{ts}"

    # Per-dir file counts (Correction #1)
    files_by_dir = {}
    for doc in docs:
        dirname = doc['rel_path'].split('/')[0]
        files_by_dir[dirname] = files_by_dir.get(dirname, 0) + 1

    # Per-type chunk counts
    chunks_by_type = {}
    for chunk in chunks:
        ct = chunk.get('chunk_type', 'text')
        chunks_by_type[ct] = chunks_by_type.get(ct, 0) + 1

    manifest = {
        # Identity
        'run_id': run_id,
        'tag': tag,
        'collection_name': collection_name,
        'corpus_version': 'post-clean-p0p1',
        'corpus_root': KNOWLEDGE_DIR,
        'git_sha': get_git_sha(),
        'started_at': started_at,
        'finished_at': finished_at,
        'duration_seconds': round(
            (datetime.fromisoformat(finished_at) -
             datetime.fromisoformat(started_at)).total_seconds(), 1),

        # Embedding
        'embedding_model': MODELS[model_key],
        'model_key': model_key,
        'embedding_dims': embedding_dims,

        # Chunker (Correction #6 — frozen params)
        'chunker_version': CHUNKER_VERSION,
        'chunk_size': CHUNK_SIZE,
        'chunk_overlap': CHUNK_OVERLAP,
        'faq_atomic': FAQ_ATOMIC,
        'procedure_atomic': PROCEDURE_ATOMIC,
        'frontmatter_projection': 'strip (body only)',

        # Counts
        'doc_count_seen': len(docs) + skipped_l4 + len(failed),
        'doc_count_indexed': len(docs),
        'doc_count_skipped_l4': skipped_l4,
        'doc_count_failed': len(failed),
        'chunk_count_total': len(chunks),
        'indexed_count': inserted,

        # Breakdown
        'truth_levels_included': sorted(ALLOWED_TRUTH_LEVELS),
        'directories_indexed': INDEX_DIRS,
        'files_by_dir': files_by_dir,
        'chunks_by_type': chunks_by_type,

        # Failed files (if any)
        'failed_files': failed[:20] if failed else [],
    }

    filepath = os.path.join(BENCHMARK_DIR, f"manifest-{run_id}.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    log(f"  Manifest saved: {filepath}")
    return filepath


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Index .md enrichis → Weaviate (Markdown-first, index-second)')
    parser.add_argument('--dry-run', action='store_true', help='Compter seulement')
    parser.add_argument('--collection', type=str, default='Bench_A',
                        help='Collection Weaviate cible')
    parser.add_argument('--model', type=str, default='current',
                        choices=list(MODELS.keys()),
                        help='Modèle embedding')
    parser.add_argument('--only', type=str,
                        help='Répertoires (comma-separated, ex: gammes,diagnostic)')
    parser.add_argument('--tag', type=str, default='reindex',
                        help='Tag pour le manifest')
    args = parser.parse_args()

    started_at = datetime.now(timezone.utc).isoformat()
    mode = 'DRY-RUN' if args.dry_run else 'EXECUTE'

    log(f"\n{'='*60}")
    log(f"  Index .md → Weaviate — {mode}")
    log(f"  Collection: {args.collection}")
    log(f"  Model: {args.model} ({MODELS[args.model]})")
    log(f"  Chunker: v{CHUNKER_VERSION} ({CHUNK_SIZE}t, {CHUNK_OVERLAP}o, "
        f"faq_atomic={FAQ_ATOMIC}, procedure_atomic={PROCEDURE_ATOMIC})")
    log(f"{'='*60}")

    # 1. Collect + preflight validate
    dirs_filter = args.only.split(',') if args.only else None
    docs, skipped_l4, failed = collect_documents(dirs_filter)

    log(f"  Documents: {len(docs)} indexed, {skipped_l4} L4 skipped, {len(failed)} failed preflight")

    dir_counts = {}
    for doc in docs:
        dirname = doc['rel_path'].split('/')[0]
        dir_counts[dirname] = dir_counts.get(dirname, 0) + 1
    for dirname, count in sorted(dir_counts.items()):
        log(f"    {dirname}/: {count}")

    if failed:
        log(f"  Preflight failures ({len(failed)}):")
        for f in failed[:10]:
            log(f"    {f['file']}: {', '.join(f['reasons'])}")

    # 2. Chunk
    chunks = chunk_documents(docs)
    log(f"  Chunks: {len(chunks)}")

    type_counts = {}
    for c in chunks:
        ct = c.get('chunk_type', 'text')
        type_counts[ct] = type_counts.get(ct, 0) + 1
    for ct, count in sorted(type_counts.items()):
        log(f"    {ct}: {count}")

    if args.dry_run:
        log(f"\n  DRY-RUN — pas d'embedding ni d'upsert")
        finished_at = datetime.now(timezone.utc).isoformat()
        save_manifest(args.tag, args.model, args.collection, docs, chunks,
                      skipped_l4, failed, 0, 0, started_at, finished_at)
        log(f"{'='*60}")
        return

    # 3. Embed
    vectors, embedding_dims = embed_chunks(chunks, model_key=args.model)

    # 4. Upsert
    inserted, errors = upsert_to_weaviate(chunks, vectors, args.collection)

    finished_at = datetime.now(timezone.utc).isoformat()

    # 5. Manifest
    save_manifest(args.tag, args.model, args.collection, docs, chunks,
                  skipped_l4, failed, inserted, embedding_dims,
                  started_at, finished_at)

    log(f"\n{'='*60}")
    log(f"  BILAN")
    log(f"  Documents: {len(docs)} (L4 skipped: {skipped_l4}, failed: {len(failed)})")
    log(f"  Chunks: {len(chunks)}")
    log(f"  Indexed: {inserted} (errors: {errors})")
    log(f"  Collection: {args.collection}")
    log(f"  Model: {MODELS[args.model]} ({embedding_dims}d)")
    log(f"{'='*60}")


if __name__ == '__main__':
    main()
