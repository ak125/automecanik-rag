# RAG Scripts — Inventaire par domaine

> Derniere mise a jour : 2026-02-20

## Pipeline actif (production)

| Script | Role | Declencheur |
|--------|------|-------------|
| `watch-inbox.sh` | Watcher inotifywait sur `pdfs/inbox/` | systemd `rag-watcher.service` |
| `auto-enrich-pipeline.sh` | Pipeline 4 etapes (ingest → category → enrich → archive) | Appele par watch-inbox |
| `reindex.py` | Indexeur principal Weaviate (1309 lignes) | Appele par tous les importers + cron |
| `reindex_low_memory.sh` | Wrapper reindex.py avec limites memoire | Manuel |
| `load-env.sh` | Charge les variables d'environnement | Source par watch-inbox |
| `safe-extract.sh` | Extraction securisee de fichiers archives | Appele par le pipeline |
| `init_schema.py` | Initialisation schema Weaviate | One-shot au setup |
| `init_ingest_tree.sh` | Creation arborescence knowledge-import | One-shot au setup |

## Importers (architecture multi-sources — tous prevus)

| Script | Source | Ingesteur associe |
|--------|--------|-------------------|
| `import_and_index_pdfs.sh` | PDFs techniques | `ingest_pdfs.py` |
| `import_and_index_web.sh` | Pages web scrapees | `ingest_web.py` |
| `import_and_index_db.sh` | Base de donnees Supabase | `ingest_db.py` |
| `import_and_index_db_starter.sh` | DB starter (wrapper db.sh) | `ingest_db.py` |
| `import_and_index_images.sh` | Images produit/schemas | `ingest_images.py` |
| `import_and_index_videos.sh` | Videos produit | `ingest_videos.py` |
| `import_and_index_structured.sh` | Donnees structurees (JSON-LD) | `ingest_structured.py` |
| `import_and_index_tabular.sh` | Donnees tabulaires (CSV/XLSX) | `ingest_tabular.py` |

## Ingesteurs Python (extraction + normalisation)

| Script | Role |
|--------|------|
| `ingest_pdfs.py` | Extraction PDF → markdown + metadata |
| `ingest_web.py` | Scraping web → markdown + metadata |
| `ingest_db.py` | Export DB → fichiers knowledge |
| `ingest_images.py` | Traitement images → metadata + embeddings |
| `ingest_videos.py` | Traitement videos → transcription + metadata |
| `ingest_structured.py` | Import donnees structurees |
| `ingest_tabular.py` | Import donnees tabulaires (CSV/XLSX) |
| `ingest_logs.py` | Import logs pour analyse |

## Video (feature a reprendre — recyclage videos avec prompts)

| Script | Role | Statut |
|--------|------|--------|
| `select_top_shots.py` | Selection des meilleurs plans video | Non finalise |
| `build_voiceover_script.py` | Generation script voix-off | Non finalise |
| `build_voiceover_variants.py` | Variantes de voix-off | Non finalise |
| `build_video_storyboard.py` | Generation storyboard video | Non finalise |

> Intention : recycler des videos existantes et les regenerer avec un prompt LLM.

## Outils reutilisables

| Script | Role | Statut |
|--------|------|--------|
| `wiki_exporter.py` | Export contenu au format wiki | Fonctionnel |
| `wiki_ingester.py` | Import contenu depuis wiki | Fonctionnel |
| `translate_md_en_to_fr.py` | Traduction markdown EN → FR | Fonctionnel |
| `extract_pdf_images.py` | Extraction images/schemas des PDF (site + RAG) | Non finalise |
| `normalize_pdf_images.py` | Normalisation images extraites | Fonctionnel |
| `normalize_doc_metadata.py` | Normalisation metadata documents | Fonctionnel |
| `ensure_gamme_contracts.py` | Verification/creation contrats gammes | Fonctionnel |
| `build_index.py` | Construction index knowledge (CI/CD) | Fonctionnel |

## Archive (approche remplacee)

| Script | Role | Remplace par |
|--------|------|-------------|
| `build_nanobanana_prompts.py` | Prompts LLM pour contenu SEO | `.claude/agents/content-batch.md` |

## SQL

| Script | Role |
|--------|------|
| `create_rbac_roles.sql` | Creation roles RBAC Supabase |

## CLI

| Script | Role |
|--------|------|
| `rag-query.sh` | Requete manuelle vers l'API RAG |
| `run_orchestrator.py` | Orchestrateur CLI (multi-sources) |
