#!/usr/bin/env python3
"""
Keyword Prompt Generator v2 — module RAG admin.

Génère des prompts prêts à copier-coller dans Claude Chrome pour extraire
mots-clés et intentions de recherche par gamme, pour les rôles R1-R8.

Architecture :
  1. Lit les 221 gammes actives depuis __seo_gamme_purchase_guide (source de vérité)
  2. Enrichit avec pieces_gamme (pg_alias, pg_name), gamme_aggregates, et RAG .md
  3. Applique le template du rôle demandé
  4. Produit un fichier .txt prêt à coller dans Claude Chrome

Usage :
  # Une gamme, un rôle
  python kp_prompt_generator.py --gamme disque-de-frein --role R3

  # Une gamme, tous les rôles
  python kp_prompt_generator.py --gamme disque-de-frein --role all

  # Batch : les 20 gammes les plus prioritaires
  python kp_prompt_generator.py --batch top20 --role R3

  # Lister les 221 gammes actives
  python kp_prompt_generator.py --list

  # Afficher le prompt en console (sans fichier)
  python kp_prompt_generator.py --gamme disque-de-frein --role R3 --print

Résultat :
  Les prompts sont écrits dans output/prompts/{pg_alias}_{role}.txt
  Chaque prompt contient :
    - Le contexte complet de la gamme (DB + RAG)
    - Les termes interdits (anti-cannibalisation)
    - Le format JSON strict attendu en sortie

Workflow complet :
  1. Lancer ce script → prompt .txt
  2. Copier le prompt dans Claude Chrome
  3. Récupérer le JSON retourné
  4. Importer avec kp_import.py → UPSERT en DB

Gammes actives :
  Source de vérité = __seo_gamme_purchase_guide (221 gammes).
  Pas pieces_gamme (9000+) qui contient toutes les gammes TecDoc.
"""

import argparse
import json
import os
import sys
import yaml
from pathlib import Path
from datetime import datetime, timezone

# ── Paths ────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
RAG_ROOT = SCRIPT_DIR.parent.parent  # /opt/automecanik/rag
RAG_GAMMES_DIR = RAG_ROOT / "knowledge" / "gammes"
TEMPLATES_DIR = SCRIPT_DIR / "kp_templates"
OUTPUT_DIR = SCRIPT_DIR.parent.parent.parent / "app" / "output" / "prompts"

ALL_ROLES = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]

ROLE_LABELS = {
    "R1": "Router (transactionnel)",
    "R2": "Product (listing véhicule)",
    "R3": "Conseils (how-to/entretien)",
    "R4": "Référence (encyclopédique)",
    "R5": "Diagnostic (symptômes)",
    "R6": "Guide Achat (choix qualité)",
    "R7": "Brand (hub marque)",
    "R8": "Vehicle (hub véhicule)",
}


# ── DB connection ────────────────────────────────────────

def get_supabase():
    """Connect to Supabase using backend .env credentials."""
    from dotenv import load_dotenv
    from supabase import create_client

    # Load all .env files (override=False → first value wins, so load backend last)
    load_dotenv(Path("/opt/automecanik/app/backend/.env"), override=False)
    load_dotenv(RAG_ROOT / ".env", override=False)

    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not url or not key:
        print("[ERREUR] SUPABASE_URL ou SUPABASE_SERVICE_ROLE_KEY manquant dans .env")
        sys.exit(1)
    return create_client(url, key)


# ── Data loaders ─────────────────────────────────────────

def load_active_gammes(sb) -> list[dict]:
    """Load all 221 active gammes from purchase_guide + pieces_gamme.

    Returns list of {pg_id, pg_alias, pg_name, sgpg_pg_id} for active gammes only.
    """
    # Source de vérité : __seo_gamme_purchase_guide
    res = sb.table("__seo_gamme_purchase_guide").select(
        "sgpg_pg_id"
    ).execute()
    active_ids = [r["sgpg_pg_id"] for r in res.data]

    if not active_ids:
        return []

    # Enrichir avec pieces_gamme pour avoir pg_alias + pg_name
    pg_res = sb.table("pieces_gamme").select(
        "pg_id, pg_alias, pg_name"
    ).in_("pg_id", active_ids).execute()

    # Index par pg_id
    pg_map = {str(r["pg_id"]): r for r in pg_res.data}

    gammes = []
    for pid in active_ids:
        pg = pg_map.get(str(pid), {})
        gammes.append({
            "pg_id": int(pid) if pid else 0,
            "pg_alias": pg.get("pg_alias", ""),
            "pg_name": pg.get("pg_name", f"Gamme #{pid}"),
        })

    # Trier par nom
    gammes.sort(key=lambda g: g["pg_name"])
    return gammes


def resolve_gamme(sb, pg_alias: str) -> dict | None:
    """Resolve pg_alias → gamme info. Only returns if gamme is active (in purchase_guide)."""
    # D'abord trouver dans pieces_gamme
    res = sb.table("pieces_gamme").select(
        "pg_id, pg_alias, pg_name"
    ).eq("pg_alias", pg_alias).limit(1).execute()

    if not res.data:
        # Fuzzy
        res = sb.table("pieces_gamme").select(
            "pg_id, pg_alias, pg_name"
        ).ilike("pg_alias", f"%{pg_alias}%").limit(1).execute()

    if not res.data:
        return None

    pg = res.data[0]
    pg_id = pg["pg_id"]

    # Vérifier que c'est une gamme active (dans purchase_guide)
    check = sb.table("__seo_gamme_purchase_guide").select(
        "sgpg_pg_id"
    ).eq("sgpg_pg_id", str(pg_id)).limit(1).execute()

    if not check.data:
        print(f"  [WARN] '{pg_alias}' (pg_id={pg_id}) existe mais n'est PAS dans les gammes actives")
        print(f"         Seules les 221 gammes de __seo_gamme_purchase_guide sont éligibles")
        return None

    return pg


def load_purchase_guide(sb, pg_id: int) -> dict:
    """Load rich gamme data from __seo_gamme_purchase_guide."""
    res = sb.table("__seo_gamme_purchase_guide").select(
        "sgpg_pg_id, sgpg_intro_title, sgpg_intro_role, sgpg_intro_sync_parts, "
        "sgpg_symptoms, sgpg_selection_criteria, sgpg_risk_cost_range, "
        "sgpg_risk_explanation, sgpg_risk_consequences, "
        "sgpg_faq, sgpg_brands_guide, sgpg_when_pro, sgpg_how_to_choose, "
        "sgpg_h1_override, sgpg_hero_subtitle, sgpg_micro_seo_block, "
        "sgpg_decision_tree, sgpg_use_cases, sgpg_anti_mistakes, "
        "sgpg_compatibility_axes, sgpg_interest_nuggets"
    ).eq("sgpg_pg_id", str(pg_id)).limit(1).execute()
    return res.data[0] if res.data else {}


def load_aggregates(sb, pg_id: int) -> dict:
    """Load gamme aggregates (products, brands, priority)."""
    res = sb.table("gamme_aggregates").select(
        "products_total, top_brands, demand_level, difficulty_level, "
        "priority_score, intent_type, content_depth, vehicle_coverage"
    ).eq("ga_pg_id", pg_id).limit(1).execute()
    return res.data[0] if res.data else {}


def load_rag(slug: str) -> dict:
    """Parse RAG YAML frontmatter from gamme .md file."""
    path = RAG_GAMMES_DIR / f"{slug}.md"
    if not path.exists():
        return {}

    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {"raw": content}

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {"raw": content}

    try:
        fm = yaml.safe_load(parts[1])
        fm["body"] = parts[2].strip()
        return fm
    except yaml.YAMLError:
        return {"raw": content}


def check_existing_kp(sb, pg_id: int, role: str) -> dict | None:
    """Check if a keyword plan already exists for this gamme+role."""
    table_map = {
        "R1": ("__seo_r1_keyword_plan", "rkp_pg_id", "rkp_status,rkp_quality_score,rkp_pipeline_phase"),
        "R2": ("__seo_r2_keyword_plan", "r2kp_pg_id", "r2kp_status,r2kp_quality_score,r2kp_pipeline_phase"),
        "R3": ("__seo_r3_keyword_plan", "skp_pg_id", "skp_status,skp_quality_score,skp_pipeline_phase"),
        "R4": ("__seo_r4_keyword_plan", "r4kp_pg_id", "r4kp_status,r4kp_quality_score,r4kp_pipeline_phase"),
        "R5": ("__seo_r5_keyword_plan", "rkp_pg_id", "rkp_status,rkp_quality_score"),
        "R6": ("__seo_r6_keyword_plan", "r6kp_pg_id", "r6kp_status,r6kp_quality_score,r6kp_pipeline_phase"),
        "R7": ("__seo_r7_keyword_plan", "r7kp_pg_id", "r7kp_status,r7kp_quality_score"),
        "R8": ("__seo_r8_keyword_plan", "type_id", "status,quality"),
    }
    if role not in table_map:
        return None

    table, id_col, select_cols = table_map[role]
    try:
        res = sb.table(table).select(f"{id_col},{select_cols}").eq(id_col, pg_id).limit(1).execute()
        return res.data[0] if res.data else None
    except Exception:
        return None


# ── Context builder ──────────────────────────────────────

def _safe_json(obj, indent=2) -> str:
    """JSON dump with None safety."""
    return json.dumps(obj or [], ensure_ascii=False, indent=indent) if isinstance(obj, (list, dict)) else str(obj or "")


def _rag_get(rag: dict, *keys, default=None):
    """Nested dict access for RAG data."""
    d = rag
    for k in keys:
        if isinstance(d, dict):
            d = d.get(k, default)
        else:
            return default
    return d if d is not None else default


def build_context(gamme_info: dict, guide: dict, agg: dict, rag: dict, existing_kp: dict | None) -> dict:
    """Build unified context dict for template rendering."""
    return {
        # Identity
        "gamme_name": gamme_info.get("pg_name", "?"),
        "pg_id": gamme_info.get("pg_id", 0),
        "pg_alias": gamme_info.get("pg_alias", ""),
        # Purchase guide
        "intro_role": guide.get("sgpg_intro_role", ""),
        "intro_title": guide.get("sgpg_intro_title", ""),
        "symptoms": _safe_json(guide.get("sgpg_symptoms")),
        "selection_criteria": _safe_json(guide.get("sgpg_selection_criteria")),
        "cost_range": guide.get("sgpg_risk_cost_range") or "non renseigné",
        "risk_explanation": guide.get("sgpg_risk_explanation", ""),
        "risk_consequences": guide.get("sgpg_risk_consequences", ""),
        "faq": _safe_json(guide.get("sgpg_faq")),
        "brands_guide": _safe_json(guide.get("sgpg_brands_guide")),
        "when_pro": _safe_json(guide.get("sgpg_when_pro")),
        "how_to_choose": guide.get("sgpg_how_to_choose", ""),
        "h1_override": guide.get("sgpg_h1_override", ""),
        "micro_seo_block": guide.get("sgpg_micro_seo_block", ""),
        "sync_parts": guide.get("sgpg_intro_sync_parts", ""),
        "decision_tree": _safe_json(guide.get("sgpg_decision_tree")),
        "use_cases": _safe_json(guide.get("sgpg_use_cases")),
        "anti_mistakes": _safe_json(guide.get("sgpg_anti_mistakes")),
        "compatibility_axes": _safe_json(guide.get("sgpg_compatibility_axes")),
        "interest_nuggets": _safe_json(guide.get("sgpg_interest_nuggets")),
        # Aggregates
        "products_total": agg.get("products_total", 0),
        "top_brands": _safe_json(agg.get("top_brands")),
        "demand_level": agg.get("demand_level", "?"),
        "difficulty_level": agg.get("difficulty_level", "?"),
        "priority_score": agg.get("priority_score", 0),
        "intent_type": agg.get("intent_type", "?"),
        "content_depth": agg.get("content_depth", "?"),
        "vehicle_coverage": agg.get("vehicle_coverage", "?"),
        # RAG
        "rag_domain_role": _rag_get(rag, "domain", "role", default=""),
        "rag_must_be_true": _safe_json(_rag_get(rag, "domain", "must_be_true", default=[])),
        "rag_must_not_contain": _safe_json(_rag_get(rag, "domain", "must_not_contain", default=[])),
        "rag_confusion_with": _safe_json(_rag_get(rag, "domain", "confusion_with", default=[])),
        "rag_related_parts": _safe_json(_rag_get(rag, "domain", "related_parts", default=[])),
        "rag_norms": _safe_json(_rag_get(rag, "domain", "norms", default=[])),
        "rag_cross_gammes": _safe_json(_rag_get(rag, "domain", "cross_gammes", default=[])),
        "rag_diagnostic_symptoms": _safe_json(_rag_get(rag, "diagnostic", "symptoms", default=[])),
        "rag_diagnostic_causes": _safe_json(_rag_get(rag, "diagnostic", "causes", default=[])),
        "rag_selection_criteria": _safe_json(_rag_get(rag, "selection", "criteria", default=[])),
        "rag_maintenance": str(_rag_get(rag, "maintenance", "interval", default="")),
        # Existing KP
        "existing_kp": _safe_json(existing_kp) if existing_kp else "aucun",
        "mode": "refresh" if existing_kp else "creation",
    }


# ── Template rendering ───────────────────────────────────

class SafeDict(dict):
    """Dict that returns {key} for missing keys instead of raising KeyError."""
    def __missing__(self, key):
        return f"{{{key}}}"


def render_template(role: str, ctx: dict) -> str:
    """Load and render a role template with context."""
    template_path = TEMPLATES_DIR / f"{role.lower()}_template.txt"
    if not template_path.exists():
        return f"[ERREUR] Template manquant : {template_path}\n\nTemplates disponibles : {list(TEMPLATES_DIR.glob('*.txt'))}"

    template = template_path.read_text(encoding="utf-8")
    return template.format_map(SafeDict(ctx))


# ── Coverage report ──────────────────────────────────────

def get_coverage_report(sb, gammes: list[dict]) -> dict:
    """Build a coverage report: which gammes have KP for which roles."""
    tables = {
        "R1": ("__seo_r1_keyword_plan", "rkp_pg_id"),
        "R3": ("__seo_r3_keyword_plan", "skp_pg_id"),
        "R4": ("__seo_r4_keyword_plan", "r4kp_pg_id"),
        "R6": ("__seo_r6_keyword_plan", "r6kp_pg_id"),
    }
    coverage = {}
    for role, (table, col) in tables.items():
        try:
            res = sb.table(table).select(col).execute()
            coverage[role] = {str(r[col]) for r in res.data}
        except Exception:
            coverage[role] = set()
    return coverage


# ── Main logic ───────────────────────────────────────────

def generate_prompt(sb, pg_alias: str, role: str, verbose: bool = False) -> str | None:
    """Generate a single prompt for one gamme + one role."""
    # 1. Resolve gamme (must be active)
    gamme_info = resolve_gamme(sb, pg_alias)
    if not gamme_info:
        return None

    pg_id = gamme_info["pg_id"]
    pg_name = gamme_info["pg_name"]
    slug = gamme_info["pg_alias"]

    # 2. Load all data sources
    guide = load_purchase_guide(sb, pg_id)
    agg = load_aggregates(sb, pg_id)
    rag = load_rag(slug)
    existing_kp = check_existing_kp(sb, pg_id, role)

    # 3. Report data completeness
    sources = []
    if guide: sources.append("purchase_guide")
    if agg: sources.append("aggregates")
    if rag: sources.append("RAG")
    if existing_kp: sources.append(f"KP_{role}_existant")

    if verbose:
        print(f"  Sources : {', '.join(sources) or 'AUCUNE'}")
        if not guide:
            print(f"  [WARN] Pas de purchase_guide pour pg_id={pg_id}")
        if not rag:
            print(f"  [WARN] Pas de fichier RAG pour {slug}.md")

    # 4. Build context & render
    ctx = build_context(gamme_info, guide, agg, rag, existing_kp)
    prompt = render_template(role, ctx)

    # 5. Output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"{slug}_{role}.txt"
    output_file.write_text(prompt, encoding="utf-8")

    mode_label = "REFRESH" if existing_kp else "CREATION"
    print(f"  [{mode_label}] {pg_name} → {role} ({ROLE_LABELS.get(role, '')}) → {output_file.name}")

    return prompt


# ── CLI ──────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Keyword Prompt Generator — génère des prompts Claude Chrome pour keyword research SEO",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples :
  %(prog)s --gamme disque-de-frein --role R3     # Un prompt R3 pour disque-de-frein
  %(prog)s --gamme disque-de-frein --role all     # 8 prompts (R1-R8) pour disque-de-frein
  %(prog)s --batch top20 --role R3                # Top 20 gammes prioritaires, rôle R3
  %(prog)s --list                                 # Liste des 221 gammes actives
  %(prog)s --coverage                             # Rapport couverture KP par rôle
        """
    )
    parser.add_argument("--gamme", type=str, help="Slug de la gamme (ex: disque-de-frein)")
    parser.add_argument("--batch", type=str, help="Mode batch: top20, top50, all")
    parser.add_argument("--role", type=str, default="all", help="R1, R2, ..., R8, ou all (défaut: all)")
    parser.add_argument("--print", action="store_true", dest="print_prompt", help="Afficher le prompt en console")
    parser.add_argument("--list", action="store_true", help="Lister les gammes actives")
    parser.add_argument("--coverage", action="store_true", help="Rapport de couverture KP par rôle")
    parser.add_argument("-v", "--verbose", action="store_true", help="Afficher les détails de chargement")
    args = parser.parse_args()

    sb = get_supabase()
    roles = ALL_ROLES if args.role.lower() == "all" else [args.role.upper()]

    # ── List ──
    if args.list:
        gammes = load_active_gammes(sb)
        print(f"\n  {'ID':>5}  {'Slug':<45} {'Nom'}")
        print(f"  {'─'*5}  {'─'*45} {'─'*30}")
        for g in gammes:
            alias = g["pg_alias"] or "(sans alias)"
            print(f"  {g['pg_id']:>5}  {alias:<45} {g['pg_name']}")
        print(f"\n  Total : {len(gammes)} gammes actives\n")
        return

    # ── Coverage ──
    if args.coverage:
        gammes = load_active_gammes(sb)
        coverage = get_coverage_report(sb, gammes)
        total = len(gammes)
        print(f"\n  Couverture Keyword Plans ({total} gammes actives)\n")
        print(f"  {'Rôle':<8} {'KP existants':>12} {'Couverture':>12} {'Manquants':>10}")
        print(f"  {'─'*8} {'─'*12} {'─'*12} {'─'*10}")
        for role in ["R1", "R3", "R4", "R6"]:
            count = len(coverage.get(role, set()))
            pct = count / total * 100 if total else 0
            miss = total - count
            print(f"  {role:<8} {count:>12} {pct:>11.1f}% {miss:>10}")
        print()
        return

    # ── Single gamme ──
    if args.gamme:
        print(f"\n{'═'*60}")
        print(f"  Keyword Prompt Generator — {args.gamme}")
        print(f"  Rôles : {', '.join(roles)}")
        print(f"{'═'*60}\n")

        for role in roles:
            prompt = generate_prompt(sb, args.gamme, role, verbose=args.verbose)
            if prompt and args.print_prompt:
                print(f"\n{'─'*60}")
                print(f"  PROMPT {role} — {args.gamme}")
                print(f"{'─'*60}\n")
                print(prompt)
                print(f"\n{'─'*60}\n")

        print(f"\n  Fichiers dans : {OUTPUT_DIR}/\n")

    # ── Batch ──
    elif args.batch:
        gammes = load_active_gammes(sb)

        # Trier par priorité si aggregates dispo
        if args.batch.startswith("top"):
            try:
                limit = int(args.batch.replace("top", ""))
            except ValueError:
                limit = 20
            # Load priority scores
            agg_res = sb.table("gamme_aggregates").select(
                "ga_pg_id, priority_score"
            ).order("priority_score", desc=True).limit(500).execute()
            priority_map = {r["ga_pg_id"]: r["priority_score"] for r in agg_res.data}
            gammes.sort(key=lambda g: priority_map.get(g["pg_id"], 0), reverse=True)
            gammes = gammes[:limit]
        elif args.batch == "all":
            pass  # toutes les gammes
        else:
            gammes = gammes[:20]

        print(f"\n{'═'*60}")
        print(f"  Batch : {len(gammes)} gammes × {len(roles)} rôles = {len(gammes) * len(roles)} prompts")
        print(f"{'═'*60}\n")

        generated = 0
        skipped = 0
        for g in gammes:
            slug = g["pg_alias"]
            if not slug:
                skipped += 1
                continue
            for role in roles:
                result = generate_prompt(sb, slug, role, verbose=args.verbose)
                if result:
                    generated += 1
                else:
                    skipped += 1

        print(f"\n  Résultat : {generated} générés, {skipped} ignorés")
        print(f"  Fichiers dans : {OUTPUT_DIR}/\n")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
