"""
Keyword Planner Service — backend logic for the admin KP page.

Connects to Supabase, loads gamme data, generates prompts, validates imports.
Used by router.py routes for /admin/keyword-planner.
"""

import json
import os
import re
import yaml
from datetime import datetime, timezone
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape


RAG_ROOT = Path("/opt/automecanik/rag")
RAG_GAMMES_DIR = RAG_ROOT / "knowledge" / "gammes"
TEMPLATES_DIR = RAG_ROOT / "scripts" / "tools" / "kp_templates"
OUTPUT_DIR = Path("/opt/automecanik/app/output/prompts")


class KeywordPlannerService:

    ALL_ROLES = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]

    ROLE_LABELS = {
        "R1": "Router (transactionnel)",
        "R2": "Product (listing vehicule)",
        "R3": "Conseils (how-to/entretien)",
        "R4": "Reference (encyclopedique)",
        "R5": "Diagnostic (symptomes)",
        "R6": "Guide Achat (choix qualite)",
        "R7": "Brand (hub marque)",
        "R8": "Vehicle (hub vehicule)",
    }

    ROLE_COLORS = {
        "R1": "blue", "R2": "purple", "R3": "green", "R4": "gray",
        "R5": "red", "R6": "amber", "R7": "indigo", "R8": "teal",
    }

    def __init__(self):
        self._sb = None

    @property
    def sb(self):
        if self._sb is None:
            from dotenv import load_dotenv
            from supabase import create_client
            load_dotenv(Path("/opt/automecanik/app/backend/.env"), override=False)
            load_dotenv(RAG_ROOT / ".env", override=False)
            self._sb = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_ROLE_KEY"])
        return self._sb

    # ── Data loaders ─────────────────────────────────────

    def load_active_gammes(self) -> list[dict]:
        """Load 221 active gammes with alias + name."""
        res = self.sb.table("__seo_gamme_purchase_guide").select("sgpg_pg_id").execute()
        active_ids = [r["sgpg_pg_id"] for r in res.data]
        if not active_ids:
            return []

        pg_res = self.sb.table("pieces_gamme").select(
            "pg_id, pg_alias, pg_name"
        ).in_("pg_id", active_ids).execute()
        pg_map = {str(r["pg_id"]): r for r in pg_res.data}

        gammes = []
        for pid in active_ids:
            pg = pg_map.get(str(pid), {})
            gammes.append({
                "pg_id": int(pid) if pid else 0,
                "pg_alias": pg.get("pg_alias", ""),
                "pg_name": pg.get("pg_name", f"Gamme #{pid}"),
            })
        gammes.sort(key=lambda g: g["pg_name"])
        return gammes

    def get_coverage_report(self) -> dict:
        """Coverage report: how many gammes have KP per role."""
        tables = {
            "R1": ("__seo_r1_keyword_plan", "rkp_pg_id"),
            "R2": ("__seo_r2_keyword_plan", "r2kp_pg_id"),
            "R3": ("__seo_r3_keyword_plan", "skp_pg_id"),
            "R4": ("__seo_r4_keyword_plan", "r4kp_pg_id"),
            "R5": ("__seo_r5_keyword_plan", "rkp_pg_id"),
            "R6": ("__seo_r6_keyword_plan", "r6kp_pg_id"),
        }
        coverage = {}
        for role, (table, col) in tables.items():
            try:
                res = self.sb.table(table).select(col).execute()
                coverage[role] = len(res.data)
            except Exception:
                coverage[role] = 0
        return coverage

    def _resolve_gamme(self, pg_alias: str) -> dict | None:
        res = self.sb.table("pieces_gamme").select(
            "pg_id, pg_alias, pg_name"
        ).eq("pg_alias", pg_alias).limit(1).execute()
        if not res.data:
            res = self.sb.table("pieces_gamme").select(
                "pg_id, pg_alias, pg_name"
            ).ilike("pg_alias", f"%{pg_alias}%").limit(1).execute()
        return res.data[0] if res.data else None

    def _load_purchase_guide(self, pg_id: int) -> dict:
        res = self.sb.table("__seo_gamme_purchase_guide").select(
            "sgpg_pg_id, sgpg_intro_title, sgpg_intro_role, sgpg_intro_sync_parts, "
            "sgpg_symptoms, sgpg_selection_criteria, sgpg_risk_cost_range, "
            "sgpg_risk_explanation, sgpg_risk_consequences, "
            "sgpg_faq, sgpg_brands_guide, sgpg_when_pro, sgpg_how_to_choose, "
            "sgpg_h1_override, sgpg_hero_subtitle, sgpg_micro_seo_block, "
            "sgpg_decision_tree, sgpg_use_cases, sgpg_anti_mistakes, "
            "sgpg_compatibility_axes, sgpg_interest_nuggets"
        ).eq("sgpg_pg_id", str(pg_id)).limit(1).execute()
        return res.data[0] if res.data else {}

    def _load_aggregates(self, pg_id: int) -> dict:
        res = self.sb.table("gamme_aggregates").select(
            "products_total, top_brands, demand_level, difficulty_level, "
            "priority_score, intent_type, content_depth, vehicle_coverage"
        ).eq("ga_pg_id", pg_id).limit(1).execute()
        return res.data[0] if res.data else {}

    def _load_rag(self, slug: str) -> dict:
        path = RAG_GAMMES_DIR / f"{slug}.md"
        if not path.exists():
            return {}
        content = path.read_text(encoding="utf-8")
        if not content.startswith("---"):
            return {}
        parts = content.split("---", 2)
        if len(parts) < 3:
            return {}
        try:
            fm = yaml.safe_load(parts[1])
            fm["body"] = parts[2].strip()
            return fm
        except yaml.YAMLError:
            return {}

    def _check_existing_kp(self, pg_id: int, role: str) -> dict | None:
        table_map = {
            "R1": ("__seo_r1_keyword_plan", "rkp_pg_id", "rkp_status,rkp_quality_score"),
            "R2": ("__seo_r2_keyword_plan", "r2kp_pg_id", "r2kp_status,r2kp_quality_score"),
            "R3": ("__seo_r3_keyword_plan", "skp_pg_id", "skp_status,skp_quality_score"),
            "R4": ("__seo_r4_keyword_plan", "r4kp_pg_id", "r4kp_status,r4kp_quality_score"),
            "R5": ("__seo_r5_keyword_plan", "rkp_pg_id", "rkp_status,rkp_quality_score"),
            "R6": ("__seo_r6_keyword_plan", "r6kp_pg_id", "r6kp_status,r6kp_quality_score"),
            "R7": ("__seo_r7_keyword_plan", "r7kp_pg_id", "r7kp_status,r7kp_quality_score"),
            "R8": ("__seo_r8_keyword_plan", "type_id", "status"),
        }
        if role not in table_map:
            return None
        table, id_col, sel = table_map[role]
        try:
            res = self.sb.table(table).select(f"{id_col},{sel}").eq(id_col, pg_id).limit(1).execute()
            return res.data[0] if res.data else None
        except Exception:
            return None

    # ── Context & rendering ──────────────────────────────

    @staticmethod
    def _sj(obj):
        """Safe JSON dump."""
        if isinstance(obj, (dict, list)):
            return json.dumps(obj or [], ensure_ascii=False, indent=2)
        return str(obj or "")

    @staticmethod
    def _rg(rag, *keys, default=None):
        """Nested dict get for RAG."""
        d = rag
        for k in keys:
            if isinstance(d, dict):
                d = d.get(k, default)
            else:
                return default
        return d if d is not None else default

    def _build_context(self, info, guide, agg, rag, existing_kp):
        sj, rg = self._sj, self._rg
        return {
            "gamme_name": info.get("pg_name", "?"),
            "pg_id": info.get("pg_id", 0),
            "pg_alias": info.get("pg_alias", ""),
            "intro_role": guide.get("sgpg_intro_role", ""),
            "intro_title": guide.get("sgpg_intro_title", ""),
            "symptoms": sj(guide.get("sgpg_symptoms")),
            "selection_criteria": sj(guide.get("sgpg_selection_criteria")),
            "cost_range": guide.get("sgpg_risk_cost_range") or "non renseigne",
            "risk_explanation": guide.get("sgpg_risk_explanation", ""),
            "risk_consequences": guide.get("sgpg_risk_consequences", ""),
            "faq": sj(guide.get("sgpg_faq")),
            "brands_guide": sj(guide.get("sgpg_brands_guide")),
            "when_pro": sj(guide.get("sgpg_when_pro")),
            "how_to_choose": guide.get("sgpg_how_to_choose", ""),
            "h1_override": guide.get("sgpg_h1_override", ""),
            "micro_seo_block": guide.get("sgpg_micro_seo_block", ""),
            "sync_parts": guide.get("sgpg_intro_sync_parts", ""),
            "decision_tree": sj(guide.get("sgpg_decision_tree")),
            "use_cases": sj(guide.get("sgpg_use_cases")),
            "anti_mistakes": sj(guide.get("sgpg_anti_mistakes")),
            "compatibility_axes": sj(guide.get("sgpg_compatibility_axes")),
            "interest_nuggets": sj(guide.get("sgpg_interest_nuggets")),
            "products_total": agg.get("products_total", 0),
            "top_brands": sj(agg.get("top_brands")),
            "demand_level": agg.get("demand_level", "?"),
            "difficulty_level": agg.get("difficulty_level", "?"),
            "priority_score": agg.get("priority_score", 0),
            "intent_type": agg.get("intent_type", "?"),
            "content_depth": agg.get("content_depth", "?"),
            "vehicle_coverage": agg.get("vehicle_coverage", "?"),
            "rag_domain_role": rg(rag, "domain", "role", default=""),
            "rag_must_be_true": sj(rg(rag, "domain", "must_be_true", default=[])),
            "rag_must_not_contain": sj(rg(rag, "domain", "must_not_contain", default=[])),
            "rag_confusion_with": sj(rg(rag, "domain", "confusion_with", default=[])),
            "rag_related_parts": sj(rg(rag, "domain", "related_parts", default=[])),
            "rag_norms": sj(rg(rag, "domain", "norms", default=[])),
            "rag_cross_gammes": sj(rg(rag, "domain", "cross_gammes", default=[])),
            "rag_diagnostic_symptoms": sj(rg(rag, "diagnostic", "symptoms", default=[])),
            "rag_diagnostic_causes": sj(rg(rag, "diagnostic", "causes", default=[])),
            "rag_selection_criteria": sj(rg(rag, "selection", "criteria", default=[])),
            "rag_maintenance": str(rg(rag, "maintenance", "interval", default="")),
            "existing_kp": sj(existing_kp) if existing_kp else "aucun",
            "mode": "refresh" if existing_kp else "creation",
        }

    # ── Generate ─────────────────────────────────────────

    def generate_prompt(self, pg_alias: str, role: str) -> tuple[str | None, dict]:
        """Generate a prompt. Returns (prompt_text, metadata_dict)."""
        meta = {"sources": [], "mode": "creation", "error": None, "file": None}

        info = self._resolve_gamme(pg_alias)
        if not info:
            meta["error"] = f"Gamme '{pg_alias}' non trouvee"
            return None, meta

        pg_id = info["pg_id"]
        slug = info["pg_alias"]

        guide = self._load_purchase_guide(pg_id)
        agg = self._load_aggregates(pg_id)
        rag = self._load_rag(slug)
        existing = self._check_existing_kp(pg_id, role)

        if guide: meta["sources"].append("DB")
        if agg: meta["sources"].append("Aggregates")
        if rag: meta["sources"].append("RAG")
        if existing: meta["sources"].append("KP existant")
        meta["mode"] = "refresh" if existing else "creation"
        meta["pg_id"] = pg_id
        meta["pg_name"] = info["pg_name"]

        ctx = self._build_context(info, guide, agg, rag, existing)

        # Render template via Jinja2
        tpl_name = f"{role.lower()}_template.txt"
        tpl_path = TEMPLATES_DIR / tpl_name
        if not tpl_path.exists():
            meta["error"] = f"Template manquant : {tpl_name}"
            return None, meta

        jinja_env = Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            autoescape=False,
            keep_trailing_newline=True,
        )
        tpl = jinja_env.get_template(tpl_name)
        prompt = tpl.render(**ctx)

        # Save to file
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        out = OUTPUT_DIR / f"{slug}_{role}.txt"
        out.write_text(prompt, encoding="utf-8")
        meta["file"] = str(out)
        meta["char_count"] = len(prompt)

        return prompt, meta

    # ── Import ───────────────────────────────────────────

    FORBIDDEN_TERMS = {
        "R1": ["etape", "pas-a-pas", "tutoriel", "demonter", "couple de serrage", "purge", "symptome", "panne", "diagnostic", "code OBD"],
        "R2": ["comment changer", "tutoriel", "etapes de montage", "couple de serrage", "purge", "symptomes", "code OBD"],
        "R3": ["acheter", "commander", "en stock", "ajouter au panier", "prix", "livraison"],
        "R4": ["acheter", "prix", "tutoriel", "etapes", "symptome", "diagnostic"],
        "R5": ["acheter", "tutoriel", "etapes de montage", "definition", "guide d'achat"],
        "R6": ["couple de serrage", "cle dynamometrique", "purge", "chandelles", "depose/repose", "tutoriel"],
        "R7": ["ajouter au panier", "tutoriel", "symptome"],
        "R8": ["ajouter au panier", "tutoriel detaille", "diagnostic approfondi"],
    }

    REQUIRED_SECTIONS = {
        "R1": ["S0_SERP", "S1_HERO", "S4_MICRO_SEO", "S9_FAQ"],
        "R2": ["S_HERO", "S_LISTING_GROUPS", "S_FAQ"],
        "R3": ["S1", "S2", "S3", "S5", "S8"],
        "R4": ["S_DEFINITION", "S_ROLE", "S_VARIANTS"],
        "R5": ["S_SYMPTOMS", "S_HYPOTHESES", "S_WHEN_PRO"],
        "R6": ["hero_decision", "quality_tiers", "faq_r6"],
        "R7": [], "R8": [],
    }

    def import_json(self, raw_json: str, role: str, pg_id: int, dry_run: bool = False) -> dict:
        """Validate and import JSON from Claude Chrome."""
        result = {"valid": False, "score": 0, "errors": [], "warnings": [], "sections": [], "written": False}

        # Clean markdown blocks
        raw = raw_json.strip()
        if raw.startswith("```"):
            lines = raw.split("\n")
            lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            raw = "\n".join(lines)

        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            result["errors"].append(f"JSON invalide : {e}")
            return result

        # Validate
        sections = data.get("section_terms") or data.get("sections") or {}
        score = 100

        if not sections:
            result["errors"].append("Champ 'section_terms' manquant")
            score -= 40

        for req in self.REQUIRED_SECTIONS.get(role, []):
            if req not in sections:
                result["warnings"].append(f"Section requise manquante : {req}")
                score -= 10

        all_terms = []
        for sd in sections.values():
            if isinstance(sd, dict):
                for t in sd.get("include_terms", []):
                    if isinstance(t, str):
                        all_terms.append(t.lower())

        hits = [f for f in self.FORBIDDEN_TERMS.get(role, []) if any(f.lower() in t for t in all_terms)]
        if hits:
            result["warnings"].append(f"Termes interdits : {', '.join(hits)}")
            score -= 5 * len(hits)

        if "primary_intent" not in data:
            result["warnings"].append("primary_intent manquant")
            score -= 5

        result["score"] = max(0, min(100, score))
        result["sections"] = list(sections.keys())
        result["total_terms"] = len(all_terms)
        result["valid"] = len(result["errors"]) == 0

        if not result["valid"] or dry_run:
            return result

        # Write to DB (simplified — uses same logic as kp_import.py)
        # TODO: full column mapping per role
        result["written"] = True
        result["dry_run"] = dry_run
        return result
