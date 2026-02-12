PYTHON ?= python3
RAG_URL ?= http://127.0.0.1:8000
EVAL_SET ?= tests/eval_set.json
EVAL_OUT ?= tests/eval_report.json

.PHONY: eval eval-gate

eval:
	@if [ -z "$(RAG_API_KEY)" ]; then echo "RAG_API_KEY is required"; exit 1; fi
	$(PYTHON) tests/run_eval_set.py --url "$(RAG_URL)" --eval-set "$(EVAL_SET)" --out "$(EVAL_OUT)"

eval-gate: eval
	$(PYTHON) tests/check_eval_thresholds.py --report "$(EVAL_OUT)"
