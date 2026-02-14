# RAG Runbook (Ops)

Reference rapide pour exploiter le RAG au quotidien.

## 1) Endpoints utiles

- Health: `http://46.224.118.55:8000/health`
- OpenAPI: `http://46.224.118.55:8000/openapi.json`
- Swagger UI: `http://46.224.118.55:8000/docs`

## 2) Services attendus

Commande:

```bash
docker ps --format '{{.Names}}\t{{.Status}}'
```

Doivent etre OK:

- `rag-api-prod` (healthy)
- `weaviate-prod` (healthy)
- `redis-rag-prod` (running)

## 3) Ingestion PDF (auto)

Batch complet:

```bash
cd /opt/automecanik/rag
./scripts/import_and_index_pdfs.sh /opt/automecanik/rag/pdfs L2
```

Test cible (1 PDF):

```bash
mkdir -p /tmp/rag_pdf_test
cp /opt/automecanik/rag/pdfs/bosch_disc_brakes_tips_tests_repair.pdf /tmp/rag_pdf_test/
./scripts/import_and_index_pdfs.sh /tmp/rag_pdf_test L2
```

## 4) Requetes de validation

Search:

```bash
curl -sS -X POST http://127.0.0.1:8000/search \
  -H "Content-Type: application/json" \
  -H "X-RAG-API-Key: $RAG_API_KEY" \
  -d '{"query":"disque de frein ATE","limit":5}'
```

Chat v2:

```bash
curl -sS -X POST http://127.0.0.1:8000/chat/v2 \
  -H "Content-Type: application/json" \
  -H "X-RAG-API-Key: $RAG_API_KEY" \
  -d '{"message":"Quel disque de frein ATE pour ma 208 ?","locale":"fr"}'
```

## 5) Qualite (Eval Gate)

```bash
cd /opt/automecanik/rag
RAG_API_KEY="..." make eval-gate
```

Seuils gate:

- `KB_Catalog recall >= 0.90`
- `KB_Knowledge recall >= 0.95`
- `KB_Diagnostic recall >= 0.95`
- `no_evidence_rate <= 0.05`
- `satisfaction >= 0.90`

## 6) Depannage rapide

- `429 Too Many Requests` pendant eval:
  - relancer `make eval-gate` (retry/backoff integre).
- Conteneur one-shot bloque:
  - `docker stop <container_name>`
- `/docs` indisponible:
  - verifier `app/main.py` (`docs_url="/docs"`) puis redeployer `rag-api`.

