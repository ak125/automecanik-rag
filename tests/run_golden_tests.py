#!/usr/bin/env python3
"""
Golden Test Runner for RAG Service
Validates RAG responses against expected outcomes before activation.

Usage:
    python run_golden_tests.py [--url URL] [--api-key KEY] [--verbose]

Example:
    python run_golden_tests.py --url http://localhost:8000 --verbose
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import httpx


def load_golden_queries(path: str = "golden_queries.json") -> dict:
    """Load golden test queries from JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_search(
    url: str,
    query: str,
    api_key: str,
    limit: int = 5,
    timeout: int = 30
) -> dict:
    """Execute search query against RAG service."""
    try:
        response = httpx.post(
            f"{url}/search",
            json={"query": query, "limit": limit},
            headers={"X-API-Key": api_key},
            timeout=timeout
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP {e.response.status_code}", "results": []}
    except httpx.RequestError as e:
        return {"error": str(e), "results": []}
    except Exception as e:
        return {"error": str(e), "results": []}


def run_chat(
    url: str,
    query: str,
    api_key: str,
    timeout: int = 30
) -> dict:
    """Execute chat query via LangGraph pipeline (with classification/guardrails)."""
    try:
        response = httpx.post(
            f"{url}/chat/v2",
            json={"message": query},
            headers={"X-API-Key": api_key},
            timeout=timeout
        )
        response.raise_for_status()
        data = response.json()
        # Convert chat response to search-like format for validation
        return {
            "results": data.get("sources", []),
            "query_type": data.get("query_type"),
            "passed_guardrails": data.get("passed_guardrails"),
            "refusal_reason": data.get("refusal_reason"),
            "response": data.get("response", ""),
        }
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP {e.response.status_code}", "results": []}
    except httpx.RequestError as e:
        return {"error": str(e), "results": []}
    except Exception as e:
        return {"error": str(e), "results": []}


def validate_test(test: dict, response: dict, verbose: bool = False) -> dict:
    """
    Validate a single test against its expected outcome.

    Returns:
        dict with keys: passed, test_id, query, category, details, errors
    """
    test_id = test["id"]
    query = test["query"]
    category = test["category"]
    expected = test["expected"]

    result = {
        "test_id": test_id,
        "query": query,
        "category": category,
        "passed": True,
        "details": {},
        "errors": []
    }

    # Check for API errors
    if "error" in response and response.get("error"):
        # Empty query or special chars should fail gracefully
        if expected.get("should_refuse") and query in ["", "!@#$%^&*()"]:
            result["details"]["api_error_expected"] = True
            return result
        result["passed"] = False
        result["errors"].append(f"API error: {response['error']}")
        return result

    results = response.get("results", [])
    num_results = len(results)

    # Handle both search (dict with score) and chat (string sources) responses
    if results and isinstance(results[0], dict):
        top_score = results[0].get("score", 0)
    else:
        top_score = 0  # Chat endpoint doesn't return scores

    result["details"]["num_results"] = num_results
    result["details"]["top_score"] = round(top_score, 4) if top_score else 0

    # Check: has_results
    if "has_results" in expected:
        expected_has = expected["has_results"]
        actual_has = num_results > 0

        if expected_has and not actual_has:
            result["passed"] = False
            result["errors"].append("Expected results but got none")
        elif not expected_has and actual_has:
            # For refusal tests, having low-score results might be OK
            if expected.get("should_refuse"):
                min_score = expected.get("min_score", 0.70)
                if top_score < min_score:
                    result["details"]["low_score_acceptable"] = True
                else:
                    result["passed"] = False
                    result["errors"].append(
                        f"Expected no results (refusal) but got {num_results} "
                        f"with score {top_score:.2f}"
                    )

    # Check: min_score
    if "min_score" in expected and num_results > 0:
        min_score = expected["min_score"]
        if top_score < min_score:
            result["passed"] = False
            result["errors"].append(
                f"Score {top_score:.2f} below minimum {min_score}"
            )

    # Check: min_results
    if "min_results" in expected:
        min_results = expected["min_results"]
        if num_results < min_results:
            result["passed"] = False
            result["errors"].append(
                f"Got {num_results} results, expected at least {min_results}"
            )

    # Check: expected_sources (at least one should match)
    if "expected_sources" in expected and num_results > 0:
        expected_sources = expected["expected_sources"]
        # Handle both search (dict) and chat (string) response formats
        if results and isinstance(results[0], dict):
            actual_sources = [r.get("source_path", "") for r in results]
        else:
            actual_sources = [str(r) for r in results]

        # Check if any expected source appears in actual results
        found_source = False
        for exp_src in expected_sources:
            for act_src in actual_sources:
                if exp_src in act_src:
                    found_source = True
                    result["details"]["matched_source"] = exp_src
                    break
            if found_source:
                break

        if not found_source:
            result["passed"] = False
            result["errors"].append(
                f"None of expected sources {expected_sources} found in "
                f"actual sources: {actual_sources[:3]}"
            )

    # Check: should_refuse (for refusal category)
    if expected.get("should_refuse"):
        # Check if using chat endpoint (has passed_guardrails field)
        if "passed_guardrails" in response:
            # Chat endpoint - check LangGraph classification
            if not response.get("passed_guardrails"):
                result["details"]["refusal_correct"] = True
                result["details"]["query_type"] = response.get("query_type")
                result["details"]["refusal_reason"] = response.get("refusal_reason")
            else:
                result["passed"] = False
                result["errors"].append(
                    f"Should refuse but passed guardrails with query_type={response.get('query_type')}"
                )
        else:
            # Search endpoint - check score threshold
            threshold = 0.70
            if num_results == 0:
                result["details"]["refusal_correct"] = True
            elif top_score < threshold:
                result["details"]["refusal_correct"] = True
                result["details"]["below_threshold"] = True
            else:
                result["passed"] = False
                result["errors"].append(
                    f"Should refuse but got {num_results} results with "
                    f"score {top_score:.2f} (threshold: {threshold})"
                )

    return result


def run_all_tests(
    url: str,
    api_key: str,
    golden_path: str = "golden_queries.json",
    verbose: bool = False
) -> dict:
    """Run all golden tests and return summary."""
    data = load_golden_queries(golden_path)
    tests = data["tests"]
    success_criteria = data.get("success_criteria", {})

    results = []
    passed = 0
    failed = 0
    by_category = {}

    print(f"\n{'='*60}")
    print(f"RAG Golden Tests - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    print(f"URL: {url}")
    print(f"Tests: {len(tests)}")
    print(f"{'='*60}\n")

    for test in tests:
        test_id = test["id"]
        query = test["query"]
        category = test["category"]

        if verbose:
            print(f"[{test_id}] Testing: '{query[:50]}...' ", end="")

        # Use chat endpoint only for refusal tests (LangGraph classification)
        if category == "refusal" or test.get("expected", {}).get("should_refuse"):
            response = run_chat(url, query, api_key)
        else:
            response = run_search(url, query, api_key)
        result = validate_test(test, response, verbose)
        results.append(result)

        # Track by category
        if category not in by_category:
            by_category[category] = {"passed": 0, "failed": 0}

        if result["passed"]:
            passed += 1
            by_category[category]["passed"] += 1
            if verbose:
                print("\033[92mPASS\033[0m")
        else:
            failed += 1
            by_category[category]["failed"] += 1
            if verbose:
                print(f"\033[91mFAIL\033[0m - {result['errors']}")

    # Calculate metrics
    total = len(tests)
    pass_rate = passed / total if total > 0 else 0

    # Calculate average score for tests with results
    scores = [
        r["details"]["top_score"]
        for r in results
        if r["details"].get("top_score", 0) > 0
    ]
    avg_score = sum(scores) / len(scores) if scores else 0

    # Calculate refusal accuracy
    refusal_tests = [r for r in results if r["category"] in ("refusal", "edge_case")]
    refusal_passed = sum(1 for r in refusal_tests if r["passed"])
    refusal_accuracy = refusal_passed / len(refusal_tests) if refusal_tests else 1.0

    # Generate summary
    summary = {
        "timestamp": datetime.now().isoformat(),
        "url": url,
        "total_tests": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": round(pass_rate, 4),
        "average_score": round(avg_score, 4),
        "refusal_accuracy": round(refusal_accuracy, 4),
        "by_category": by_category,
        "success_criteria": success_criteria,
        "criteria_met": {
            "pass_rate": pass_rate >= success_criteria.get("pass_rate_minimum", 0.80),
            "refusal_accuracy": refusal_accuracy >= success_criteria.get("refusal_accuracy", 1.0),
            "average_score": avg_score >= success_criteria.get("average_score_minimum", 0.75)
        },
        "results": results
    }

    # Print summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Total: {total} | Passed: {passed} | Failed: {failed}")
    print(f"Pass Rate: {pass_rate*100:.1f}%")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Refusal Accuracy: {refusal_accuracy*100:.1f}%")
    print(f"\nBy Category:")
    for cat, stats in by_category.items():
        cat_total = stats["passed"] + stats["failed"]
        cat_rate = stats["passed"] / cat_total if cat_total > 0 else 0
        print(f"  {cat}: {stats['passed']}/{cat_total} ({cat_rate*100:.0f}%)")

    print(f"\n{'='*60}")
    print("CRITERIA CHECK")
    print(f"{'='*60}")
    all_criteria_met = all(summary["criteria_met"].values())
    for criterion, met in summary["criteria_met"].items():
        status = "\033[92mPASS\033[0m" if met else "\033[91mFAIL\033[0m"
        print(f"  {criterion}: {status}")

    print(f"\n{'='*60}")
    if all_criteria_met:
        print("\033[92mALL CRITERIA MET - RAG READY FOR ACTIVATION\033[0m")
    else:
        print("\033[91mCRITERIA NOT MET - RAG STAYS IN QUARANTINE\033[0m")
    print(f"{'='*60}\n")

    # Print failed tests details
    if failed > 0:
        print("\nFailed Tests Details:")
        print("-" * 40)
        for r in results:
            if not r["passed"]:
                print(f"\n[{r['test_id']}] {r['query'][:50]}")
                print(f"  Category: {r['category']}")
                print(f"  Errors: {r['errors']}")
                print(f"  Details: {r['details']}")

    return summary


def save_report(summary: dict, output_path: str = "golden_report.json"):
    """Save test report to JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\nReport saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Run RAG golden tests")
    parser.add_argument(
        "--url",
        default="http://localhost:8000",
        help="RAG service URL (default: http://localhost:8000)"
    )
    parser.add_argument(
        "--api-key",
        default="automecanik-rag-dev-2026",
        help="API key for RAG service"
    )
    parser.add_argument(
        "--golden",
        default="golden_queries.json",
        help="Path to golden queries JSON file"
    )
    parser.add_argument(
        "--output",
        default="golden_report.json",
        help="Path to output report JSON file"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print detailed output for each test"
    )

    args = parser.parse_args()

    # Change to script directory
    script_dir = Path(__file__).parent
    golden_path = script_dir / args.golden
    output_path = script_dir / args.output

    # Run tests
    summary = run_all_tests(
        url=args.url,
        api_key=args.api_key,
        golden_path=str(golden_path),
        verbose=args.verbose
    )

    # Save report
    save_report(summary, str(output_path))

    # Exit code based on criteria
    all_met = all(summary["criteria_met"].values())
    sys.exit(0 if all_met else 1)


if __name__ == "__main__":
    main()
