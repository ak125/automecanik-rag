PYTHON ?= python3
RAG_URL ?= http://127.0.0.1:8000
EVAL_SET ?= tests/eval_set.json
EVAL_OUT ?= tests/eval_report.json
KNOWLEDGE_PATH ?= knowledge

.PHONY: eval eval-gate normalize-metadata normalize-metadata-apply gamme-contract-check gamme-contract-apply

eval:
	@if [ -z "$(RAG_API_KEY)" ]; then echo "RAG_API_KEY is required"; exit 1; fi
	$(PYTHON) tests/run_eval_set.py --url "$(RAG_URL)" --eval-set "$(EVAL_SET)" --out "$(EVAL_OUT)"

eval-gate: eval
	$(PYTHON) tests/check_eval_thresholds.py --report "$(EVAL_OUT)"

normalize-metadata:
	$(PYTHON) scripts/normalize_doc_metadata.py --path "$(KNOWLEDGE_PATH)"

normalize-metadata-apply:
	$(PYTHON) scripts/normalize_doc_metadata.py --path "$(KNOWLEDGE_PATH)" --apply --fix-category

gamme-contract-check:
	$(PYTHON) scripts/ensure_gamme_contracts.py --path "$(KNOWLEDGE_PATH)" --strict-exit

gamme-contract-apply:
	$(PYTHON) scripts/ensure_gamme_contracts.py --path "$(KNOWLEDGE_PATH)" --strict-exit --apply
