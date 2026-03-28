#!/usr/bin/env python3
"""
Keyword Plan Import v2 — parse le JSON Claude Chrome et UPSERT en DB.

Workflow :
  1. kp_prompt_generator.py génère un prompt → l'utilisateur le colle dans Claude Chrome
  2. Claude Chrome retourne un JSON structuré
  3. Ce script valide le JSON et l'injecte dans la table __seo_r*_keyword_plan

Usage :
  # Depuis un fichier
  python kp_import.py --file output/prompts/disque-de-frein_R3_result.json

  # Collage interactif (Ctrl+D pour terminer)
  python kp_import.py --role R3 --gamme disque-de-frein --paste

  # Pipe stdin
  cat result.json | python kp_import.py --role R3 --gamme disque-de-frein --stdin

  # Validation seule (pas d'écriture DB)
  python kp_import.py --file result.json --dry-run

Validation :
  - Structure JSON (champs requis)
  - Sections requises par rôle
  - Détection termes interdits (anti-cannibalisation)
  - Score qualité automatique (0-100)
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
RAG_ROOT = SCRIPT_DIR.parent.parent

# ── DB ───────────────────────────────────────────────────

def get_supabase():
    from dotenv import load_dotenv
    from supabase import create_client
    load_dotenv(Path("/opt/automecanik/app/backend/.env"), override=False)
    load_dotenv(RAG_ROOT / ".env", override=False)
    return create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_ROLE_KEY"])


# ── Role config ──────────────────────────────────────────

ROLE_CONFIG = {
    "R1": {
        "table": "__seo_r1_keyword_plan",
        "id_col": "rkp_pg_id",
        "score_col": "rkp_quality_score",
        "ts_col": "rkp_built_at",
        "mapping": {
            "pg_id": "rkp_pg_id", "gamme_name": "rkp_gamme_name",
            "primary_intent": "rkp_primary_intent", "secondary_intents": "rkp_secondary_intents",
            "query_clusters": "rkp_query_clusters", "section_terms": "rkp_section_terms",
            "boundaries": "rkp_boundaries",
        },
        "defaults": {"rkp_status": "draft", "rkp_pipeline_phase": "KP0_AUDIT", "rkp_version": 1, "rkp_built_by": "kp-prompt-import"},
        "required_sections": ["S0_SERP", "S1_HERO", "S4_MICRO_SEO", "S9_FAQ"],
    },
    "R2": {
        "table": "__seo_r2_keyword_plan",
        "id_col": "r2kp_pg_id",
        "score_col": "r2kp_quality_score",
        "ts_col": "r2kp_built_at",
        "mapping": {
            "pg_id": "r2kp_pg_id", "gamme_name": "r2kp_gamme_name",
            "primary_intent": "r2kp_primary_intent", "secondary_intents": "r2kp_secondary_intents",
            "query_clusters": "r2kp_query_clusters", "section_terms": "r2kp_section_terms",
            "boundaries": "r2kp_boundaries", "schema_types": "r2kp_schema_types",
        },
        "defaults": {"r2kp_status": "draft", "r2kp_pipeline_phase": "P0_AUDIT_FINDER", "r2kp_version": 1, "r2kp_built_by": "kp-prompt-import"},
        "required_sections": ["S_HERO", "S_LISTING_GROUPS", "S_FAQ"],
    },
    "R3": {
        "table": "__seo_r3_keyword_plan",
        "id_col": "skp_pg_id",
        "score_col": "skp_quality_score",
        "ts_col": "skp_built_at",
        "mapping": {
            "pg_id": "skp_pg_id", "gamme_name": "skp_gamme_name",
            "primary_intent": "skp_primary_intent", "secondary_intents": "skp_secondary_intents",
            "query_clusters": "skp_query_clusters", "section_terms": "skp_section_terms",
            "seo_brief": "skp_seo_brief", "boundaries": "skp_boundaries",
        },
        "defaults": {"skp_status": "draft", "skp_pipeline_phase": "P0", "skp_version": 1, "skp_built_by": "kp-prompt-import"},
        "required_sections": ["S1", "S2", "S3", "S5", "S8"],
    },
    "R4": {
        "table": "__seo_r4_keyword_plan",
        "id_col": "r4kp_pg_id",
        "score_col": "r4kp_quality_score",
        "ts_col": "r4kp_built_at",
        "mapping": {
            "pg_id": "r4kp_pg_id", "gamme_name": "r4kp_gamme_name",
            "primary_intent": "r4kp_primary_intent",
            "query_clusters": "r4kp_query_clusters", "section_terms": "r4kp_section_terms",
            "keyword_universe": "r4kp_keyword_universe", "link_out_plan": "r4kp_link_out_plan",
            "boundaries": "r4kp_boundaries",
        },
        "defaults": {"r4kp_status": "draft", "r4kp_pipeline_phase": "R4P6_PERSIST", "r4kp_version": 1, "r4kp_built_by": "kp-prompt-import"},
        "required_sections": ["S_DEFINITION", "S_ROLE", "S_VARIANTS"],
    },
    "R5": {
        "table": "__seo_r5_keyword_plan",
        "id_col": "rkp_pg_id",
        "score_col": "rkp_quality_score",
        "ts_col": "rkp_updated_at",
        "mapping": {
            "pg_id": "rkp_pg_id",
            "primary_intent": "rkp_intent_map", "observable_map": "rkp_observable_map",
            "hypothesis_map": "rkp_hypothesis_map", "section_terms": "rkp_section_terms",
            "caution_level": "rkp_caution_level", "safety_gate": "rkp_safety_gate",
        },
        "defaults": {"rkp_status": "draft", "rkp_built_by": "kp-prompt-import"},
        "required_sections": ["S_SYMPTOMS", "S_HYPOTHESES", "S_WHEN_PRO"],
    },
    "R6": {
        "table": "__seo_r6_keyword_plan",
        "id_col": "r6kp_pg_id",
        "score_col": "r6kp_quality_score",
        "ts_col": "r6kp_built_at",
        "mapping": {
            "pg_id": "r6kp_pg_id", "gamme_name": "r6kp_gamme_name",
            "primary_intent": "r6kp_keyword_plan", "section_terms": "r6kp_section_terms",
            "editorial_brief": "r6kp_editorial_brief", "boundaries": "r6kp_gate_report",
        },
        "defaults": {"r6kp_status": "draft", "r6kp_pipeline_phase": "P0_AUDIT", "r6kp_version": 1, "r6kp_built_by": "kp-prompt-import"},
        "required_sections": ["hero_decision", "quality_tiers", "faq_r6"],
    },
    "R7": {
        "table": "__seo_r7_keyword_plan",
        "id_col": "r7kp_pg_id",
        "score_col": "r7kp_quality_score",
        "ts_col": "r7kp_built_at",
        "mapping": {"pg_id": "r7kp_pg_id", "section_terms": "r7kp_section_terms"},
        "defaults": {"r7kp_status": "draft", "r7kp_built_by": "kp-prompt-import"},
        "required_sections": [],
    },
    "R8": {
        "table": "__seo_r8_keyword_plan",
        "id_col": "type_id",
        "score_col": None,
        "ts_col": None,
        "mapping": {"pg_id": "type_id", "sections": "sections", "query_clusters": "clusters", "quality": "quality"},
        "defaults": {"status": "draft", "pipeline_phase": "P0"},
        "required_sections": [],
    },
}

FORBIDDEN_TERMS = {
    "R1": ["étape", "pas-à-pas", "tutoriel", "démonter", "couple de serrage", "purge", "symptôme", "panne", "diagnostic", "code OBD"],
    "R2": ["comment changer", "tutoriel", "étapes de montage", "couple de serrage", "purge", "dépose/repose", "symptômes", "code OBD", "définition complète"],
    "R3": ["acheter", "commander", "en stock", "ajouter au panier", "prix", "livraison"],
    "R4": ["acheter", "prix", "tutoriel", "étapes", "symptôme", "diagnostic"],
    "R5": ["acheter", "tutoriel", "étapes de montage", "définition", "guide d'achat"],
    "R6": ["couple de serrage", "clé dynamométrique", "purge", "chandelles", "dépose/repose", "étape 1", "outillage requis", "tutoriel"],
    "R7": ["ajouter au panier", "tutoriel", "symptôme"],
    "R8": ["ajouter au panier", "tutoriel détaillé", "diagnostic approfondi"],
}


# ── Validation ───────────────────────────────────────────

def validate_json(data: dict, role: str) -> dict:
    """Validate imported JSON and compute quality score."""
    config = ROLE_CONFIG[role]
    warnings, errors = [], []
    score = 100

    # Check sections
    sections = data.get("section_terms") or data.get("sections") or {}
    if not sections:
        errors.append("Champ 'section_terms' ou 'sections' manquant")
        score -= 40

    for req in config["required_sections"]:
        if req not in sections:
            warnings.append(f"Section requise manquante : {req}")
            score -= 10

    # Check forbidden terms
    all_terms = []
    for sd in sections.values():
        if isinstance(sd, dict):
            for t in sd.get("include_terms", []):
                if isinstance(t, str):
                    all_terms.append(t.lower())

    hits = [f for f in FORBIDDEN_TERMS.get(role, []) if any(f.lower() in t for t in all_terms)]
    if hits:
        warnings.append(f"Termes interdits : {hits}")
        score -= 5 * len(hits)

    # Check terms density
    thin_sections = []
    for sid, sd in sections.items():
        if isinstance(sd, dict):
            n = len(sd.get("include_terms", []))
            if n < 2:
                thin_sections.append(f"{sid}({n})")
                score -= 3
    if thin_sections:
        warnings.append(f"Sections thin : {', '.join(thin_sections)}")

    if "primary_intent" not in data:
        warnings.append("Champ 'primary_intent' manquant")
        score -= 5

    return {
        "valid": len(errors) == 0,
        "quality_score": max(0, min(100, score)),
        "errors": errors,
        "warnings": warnings,
        "sections_found": list(sections.keys()),
        "total_terms": len(all_terms),
        "forbidden_hits": hits,
    }


# ── DB write ─────────────────────────────────────────────

def upsert_to_db(sb, data: dict, role: str, quality_score: int) -> bool:
    config = ROLE_CONFIG[role]
    row = {}

    for json_key, db_col in config["mapping"].items():
        if json_key in data:
            row[db_col] = data[json_key]

    row.update(config["defaults"])

    if config["score_col"]:
        row[config["score_col"]] = quality_score
    if config["ts_col"]:
        row[config["ts_col"]] = datetime.now(timezone.utc).isoformat()

    if not data.get("pg_id"):
        print("  [ERREUR] pg_id manquant")
        return False

    try:
        sb.table(config["table"]).upsert(row, on_conflict=config["id_col"]).execute()
        print(f"  [OK] {config['table']} — pg_id={data['pg_id']} — score={quality_score}")
        return True
    except Exception as e:
        print(f"  [ERREUR] {e}")
        return False


# ── CLI ──────────────────────────────────────────────────

def resolve_role(raw: str, data: dict = None) -> str | None:
    """Normalize role string to R1-R8."""
    if not raw and data:
        raw = data.get("role", "")
    if not raw:
        return None
    r = raw.upper().strip()
    # "R3_CONSEILS" → "R3"
    for prefix in ALL_ROLES:
        if r.startswith(prefix):
            return prefix
    return None

ALL_ROLES = list(ROLE_CONFIG.keys())


def main():
    parser = argparse.ArgumentParser(
        description="Keyword Plan Import — valide + injecte le JSON Claude Chrome en DB",
        epilog="Pipe : cat result.json | python kp_import.py --role R3"
    )
    parser.add_argument("--file", type=str, help="Fichier JSON résultat")
    parser.add_argument("--role", type=str, help="Rôle (R1-R8)")
    parser.add_argument("--gamme", type=str, help="Slug gamme (contexte)")
    parser.add_argument("--paste", action="store_true", help="Coller le JSON (Ctrl+D)")
    parser.add_argument("--stdin", action="store_true", help="Lire depuis stdin")
    parser.add_argument("--dry-run", action="store_true", help="Valider sans écrire")
    args = parser.parse_args()

    # Load JSON
    if args.file:
        path = Path(args.file)
        if not path.exists():
            print(f"Fichier non trouvé : {path}")
            sys.exit(1)
        raw = path.read_text(encoding="utf-8")
    elif args.paste:
        print("Collez le JSON puis Ctrl+D :")
        raw = sys.stdin.read()
    elif args.stdin or not sys.stdin.isatty():
        raw = sys.stdin.read()
    else:
        parser.print_help()
        sys.exit(1)

    # Clean markdown code blocks
    raw = raw.strip()
    if raw.startswith("```"):
        lines = raw.split("\n")
        lines = lines[1:]  # remove ```json
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        raw = "\n".join(lines)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"  [ERREUR] JSON invalide : {e}")
        print(f"  Premiers 200 chars : {raw[:200]}")
        sys.exit(1)

    role = resolve_role(args.role, data)
    if not role:
        print("  [ERREUR] Rôle non résolu. Utilisez --role R1|R2|...|R8")
        sys.exit(1)

    print(f"\n{'═'*50}")
    print(f"  Import KP {role}")
    print(f"{'═'*50}\n")

    v = validate_json(data, role)

    print(f"  Score qualité   : {v['quality_score']}/100")
    print(f"  Sections        : {', '.join(v['sections_found'])}")
    print(f"  Termes totaux   : {v['total_terms']}")

    if v["errors"]:
        print(f"\n  ERREURS :")
        for e in v["errors"]:
            print(f"    x {e}")
    if v["warnings"]:
        print(f"\n  WARNINGS :")
        for w in v["warnings"]:
            print(f"    ! {w}")

    if not v["valid"]:
        print(f"\n  [BLOQUE] Import annulé\n")
        sys.exit(1)

    if args.dry_run:
        print(f"\n  [DRY-RUN] OK — pas d'écriture DB\n")
        return

    sb = get_supabase()
    ok = upsert_to_db(sb, data, role, v["quality_score"])
    print(f"\n  {'OK' if ok else 'ECHEC'}\n")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
