"""Role classifier for RAG chunks (v2.5).

Assigns 6 fields to each chunk:
  - section_key: inferred from heading/chunk_type
  - primary_role: canonical RoleId (R1_ROUTER..R6_SUPPORT)
  - allowed_roles: list of RoleIds this chunk is valid for
  - purity_score: 0-100, penalised by weighted contamination flags
  - contamination_flags: list of detected cross-role signals
  - chunk_kind: content type for retrieval diversification

Config-driven: loads role_map_defaults.json (global) and optional
per-gamme role_map.json overlays from content/gammes/{slug}/.
Falls back to hard-coded heuristics if no config files found.
"""

import copy
import json
import re
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# ── Config paths ──

_CONFIG_DIR = Path(__file__).resolve().parent.parent.parent / "config"
_DEFAULTS_PATH = _CONFIG_DIR / "role_map_defaults.json"
_CONTENT_GAMMES_DIR = Path(__file__).resolve().parent.parent.parent / "content" / "gammes"

# ── Load defaults (module-level, cached) ──

_DEFAULTS: dict = {}

try:
    with open(_DEFAULTS_PATH, "r", encoding="utf-8") as f:
        _DEFAULTS = json.load(f)
    logger.info(
        "Loaded role_map_defaults.json (%d contamination flags)",
        len(_DEFAULTS.get("contamination_flags", {})),
    )
except FileNotFoundError:
    logger.warning(
        "role_map_defaults.json not found at %s — using hard-coded fallbacks",
        _DEFAULTS_PATH,
    )
except Exception as exc:
    logger.error("Failed to load role_map_defaults.json: %s", exc)

# ── Per-gamme config cache ──

_GAMME_CONFIG_CACHE: dict[str, dict] = {}


def _merge_config(base: dict, overrides: dict) -> dict:
    """Shallow-deep merge: for flag dicts, merge per-flag fields."""
    result = base.copy()
    for key, value in overrides.items():
        if key in ("contamination_flags", "table_safety_flags") and isinstance(value, dict):
            merged = result.get(key, {}).copy()
            for flag_name, flag_overrides in value.items():
                if flag_name in merged and isinstance(flag_overrides, dict):
                    merged[flag_name] = {**merged[flag_name], **flag_overrides}
                else:
                    merged[flag_name] = flag_overrides
            result[key] = merged
        else:
            result[key] = value
    return result


def _load_gamme_config(gamme_slug: str) -> dict:
    """Load and cache per-gamme role_map.json, merging with defaults."""
    if gamme_slug in _GAMME_CONFIG_CACHE:
        return _GAMME_CONFIG_CACHE[gamme_slug]

    merged = copy.deepcopy(_DEFAULTS) if _DEFAULTS else {}
    gamme_path = _CONTENT_GAMMES_DIR / gamme_slug / "role_map.json"

    if gamme_path.is_file():
        try:
            with open(gamme_path, "r", encoding="utf-8") as f:
                overrides = json.load(f)
            merged = _merge_config(merged, overrides)
            logger.debug("Loaded per-gamme role_map for '%s'", gamme_slug)
        except Exception as exc:
            logger.warning("Failed to load per-gamme role_map for '%s': %s", gamme_slug, exc)

    _GAMME_CONFIG_CACHE[gamme_slug] = merged
    return merged


def _get_effective_config(gamme_slug: Optional[str]) -> dict:
    """Get the effective config: per-gamme if slug provided, else defaults."""
    if gamme_slug:
        return _load_gamme_config(gamme_slug)
    return _DEFAULTS or {}


# ── Compiled regex cache ──

_COMPILED_RE_CACHE: dict[str, re.Pattern] = {}


def _get_compiled_re(pattern: str) -> re.Pattern:
    """Compile and cache a regex pattern from config."""
    if pattern not in _COMPILED_RE_CACHE:
        _COMPILED_RE_CACHE[pattern] = re.compile(pattern, re.IGNORECASE | re.MULTILINE)
    return _COMPILED_RE_CACHE[pattern]


# ── Section key detection (heading → section_key) ──

_SECTION_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("definition", re.compile(r"d[ée]finition|c.est quoi|r[oô]le|fonction", re.IGNORECASE)),
    ("selection", re.compile(r"crit[eè]re|choisir|s[ée]lection|compatibil", re.IGNORECASE)),
    ("symptoms", re.compile(r"sympt[oô]me|signe|bruit|vibration|voyant", re.IGNORECASE)),
    ("timing", re.compile(r"quand|fr[ée]quence|dur[ée]e|intervalle|entretien", re.IGNORECASE)),
    ("trust", re.compile(r"garantie|confiance|avis|qualit[ée]", re.IGNORECASE)),
    ("support", re.compile(r"retour|sav|contact|aide|livraison", re.IGNORECASE)),
]


def heading_to_section_key(heading: Optional[str], chunk_type: str = "text") -> str:
    """Infer section_key from heading text and chunk_type."""
    if chunk_type == "faq":
        return "faq"
    if chunk_type == "procedure":
        return "procedure"

    if not heading:
        return "other"

    for key, pattern in _SECTION_PATTERNS:
        if pattern.search(heading):
            return key

    return "other"


# ── Primary role inference ──
# Hard-coded fallbacks (used when role_map_defaults.json is absent)

_GAMME_SECTION_TO_ROLE: dict[str, str] = {
    "definition": "R4_REFERENCE",
    "selection": "R3_GUIDE",
    "faq": "R3_GUIDE",
    "symptoms": "R5_DIAGNOSTIC",
    "timing": "R3_GUIDE",
    "procedure": "R3_CONSEILS",
    "trust": "R1_ROUTER",
    "support": "R6_SUPPORT",
    "other": "R1_ROUTER",
}

_SOURCE_TYPE_TO_ROLE: dict[str, str] = {
    "diagnostic": "R5_DIAGNOSTIC",
    "guide": "R3_GUIDE",
    "policy": "R6_SUPPORT",
    "faq": "R3_GUIDE",
    "canonical": "R4_REFERENCE",
}


def infer_primary_role(section_key: str, source_type: str, section_role_map: Optional[dict] = None) -> str:
    """Infer the primary role from section_key + source_type.

    Uses config-driven section_role_map if provided, else hard-coded fallback.
    """
    st = (source_type or "").lower()

    # Source-type overrides for non-gamme documents
    if st in _SOURCE_TYPE_TO_ROLE:
        return _SOURCE_TYPE_TO_ROLE[st]

    # Gamme documents: use section_key mapping
    if st in {"gamme", "catalog"}:
        mapping = section_role_map or _GAMME_SECTION_TO_ROLE
        return mapping.get(section_key, "R1_ROUTER")

    # Fallback
    return "R1_ROUTER"


# ── Contamination detection (v2.5: config-driven, weighted) ──
# Hard-coded fallback regexes (used when no config loaded)

_FALLBACK_HOWTO_RE = re.compile(r"installer|monter|d[ée]monter|d[ée]poser|remonter", re.IGNORECASE)
_FALLBACK_DIAG_RE = re.compile(r"sympt[oô]me|panne|diagnostic", re.IGNORECASE)
_FALLBACK_PRICING_RE = re.compile(r"prix|tarif|\u20ac|EUR", re.IGNORECASE)
_FALLBACK_STEP_SEQ_RE = re.compile(r"[ée]tape\s*\d|(?:^|\n)\s*1\.\s|(?:^|\n)\s*2\.\s|(?:^|\n)\s*3\.\s", re.IGNORECASE)

# Phase 4c: table safety (hard-coded fallback)
_FALLBACK_TABLE_IMPERATIVE_RE = re.compile(r"\b(remplacez|installez|d[ée]montez|d[ée]posez)\b", re.IGNORECASE)
_FALLBACK_TABLE_STEP_SEQ_RE = re.compile(r"(?:^|\|)\s*[123]\.\s", re.MULTILINE)


def detect_contamination(content: str, primary_role: str, config: dict) -> dict[str, bool]:
    """Detect cross-role contamination signals.

    Returns dict of {flag_name: True} for each detected flag.
    Config-driven: reads patterns and role scoping from config.
    Falls back to hard-coded regexes if config is empty.
    """
    flag_defs = config.get("contamination_flags", {})

    # Config-driven detection
    if flag_defs:
        flags: dict[str, bool] = {}
        for flag_name, flag_def in flag_defs.items():
            excluded = flag_def.get("excluded_roles", [])
            if excluded and primary_role in excluded:
                continue
            trigger = flag_def.get("trigger_roles")
            if trigger and primary_role not in trigger:
                continue
            pattern = flag_def.get("pattern", "")
            if not pattern:
                continue
            if _get_compiled_re(pattern).search(content):
                flags[flag_name] = True
        return flags

    # Hard-coded fallback (no config loaded)
    flags = {}
    if primary_role not in {"R3_CONSEILS", "R5_DIAGNOSTIC"} and _FALLBACK_HOWTO_RE.search(content):
        flags["HAS_HOWTO_MARKERS"] = True
    if primary_role == "R1_ROUTER" and _FALLBACK_DIAG_RE.search(content):
        flags["HAS_DIAG_MARKERS"] = True
    if primary_role != "R2_PRODUCT" and _FALLBACK_PRICING_RE.search(content):
        flags["HAS_PRICE_PUSH"] = True
    if primary_role == "R1_ROUTER" and _FALLBACK_STEP_SEQ_RE.search(content):
        flags["HAS_HOWTO_MARKERS"] = True  # folded into HOWTO
    return flags


def validate_table_safety(content: str, config: dict) -> dict[str, bool]:
    """Detect unsafe patterns in table_rows chunks (P4c).

    Config-driven with hard-coded fallback.
    """
    table_defs = config.get("table_safety_flags", {})

    if table_defs:
        flags: dict[str, bool] = {}
        for flag_name, flag_def in table_defs.items():
            pattern = flag_def.get("pattern", "")
            if not pattern:
                continue
            if _get_compiled_re(pattern).search(content):
                flags[flag_name] = True
        return flags

    # Hard-coded fallback
    flags = {}
    if _FALLBACK_TABLE_IMPERATIVE_RE.search(content):
        flags["TABLE_HAS_IMPERATIVES"] = True
    if _FALLBACK_TABLE_STEP_SEQ_RE.search(content):
        flags["TABLE_HAS_STEP_SEQUENCE"] = True
    return flags


def compute_purity(contamination_flags: dict[str, bool], config: dict) -> int:
    """Compute purity score using weighted penalties from config.

    Each detected flag subtracts its configured weight from 100.
    Falls back to flat -15 per flag if weight not found in config.
    """
    if not contamination_flags:
        return 100

    flag_defs = config.get("contamination_flags", {})
    table_defs = config.get("table_safety_flags", {})
    all_defs = {**flag_defs, **table_defs}

    total_penalty = 0
    for flag_name in contamination_flags:
        weight = all_defs.get(flag_name, {}).get("weight", 15)
        total_penalty += weight

    return max(0, 100 - total_penalty)


# ── Allowed roles ──
# Hard-coded fallback (used when config absent)

_SECTION_TOLERANT_ROLES: dict[str, list[str]] = {
    "definition": ["R1_ROUTER", "R4_REFERENCE"],
    "selection": ["R3_GUIDE", "R1_ROUTER"],
    "faq": ["R3_GUIDE", "R1_ROUTER", "R3_CONSEILS"],
    "symptoms": ["R5_DIAGNOSTIC", "R3_CONSEILS"],
    "trust": ["R1_ROUTER", "R3_GUIDE"],
    "procedure": ["R3_CONSEILS", "R5_DIAGNOSTIC"],  # NEVER R1_ROUTER
    "timing": ["R3_GUIDE", "R3_CONSEILS"],
    "support": ["R6_SUPPORT"],
    "other": [],
}


def compute_allowed_roles(section_key: str, primary_role: str, tolerant_map: Optional[dict] = None) -> list[str]:
    """Compute the list of roles this chunk is valid for.

    Uses config-driven tolerant_map if provided, else hard-coded fallback.
    """
    mapping = tolerant_map or _SECTION_TOLERANT_ROLES
    tolerant = mapping.get(section_key, [])
    roles = [primary_role]
    for r in tolerant:
        if r not in roles:
            roles.append(r)
    return roles


# ── Chunk kind classification (Phase 2) ──

CHUNK_KIND_VALUES = [
    "definition", "selection_checks", "faq", "table_rows",
    "trust", "support", "procedure", "other",
]

_SECTION_KEY_TO_CHUNK_KIND: dict[str, str] = {
    "definition": "definition",
    "selection": "selection_checks",
    "faq": "faq",
    "symptoms": "other",
    "timing": "other",
    "trust": "trust",
    "support": "support",
    "procedure": "procedure",
    "other": "other",
}

_TABLE_RE = re.compile(r"^\s*\|.+\|", re.MULTILINE)


def classify_chunk_kind(heading: Optional[str], chunk_type: str, content: str) -> str:
    """Classify chunk content type for retrieval diversification.

    Returns one of CHUNK_KIND_VALUES.
    table_rows detection has priority over heading-based classification.
    """
    # Table detection: ≥3 lines with pipe-delimited content → table_rows
    if _TABLE_RE.findall(content) and len(_TABLE_RE.findall(content)) >= 3:
        return "table_rows"

    section_key = heading_to_section_key(heading, chunk_type)
    return _SECTION_KEY_TO_CHUNK_KIND.get(section_key, "other")


# ── Combined entry point ──


def classify_chunk(
    heading: Optional[str],
    chunk_type: str,
    content: str,
    source_type: str,
    gamme_slug: Optional[str] = None,
) -> dict:
    """Classify a chunk and return the 6 role fields.

    Args:
        heading: Section heading text (may be None)
        chunk_type: Chunk type (text, faq, procedure, etc.)
        content: Raw chunk content
        source_type: Document source type (gamme, diagnostic, etc.)
        gamme_slug: Optional gamme slug for per-gamme config overrides

    Returns:
        dict with keys: section_key, primary_role, allowed_roles,
                        purity_score, contamination_flags, chunk_kind
    """
    config = _get_effective_config(gamme_slug)

    section_key = heading_to_section_key(heading, chunk_type)

    # Primary role: config-driven section_to_role if available
    section_role_map = config.get("section_to_role") or None
    primary_role = infer_primary_role(section_key, source_type, section_role_map)

    # Contamination: config-driven with weighted penalties
    contamination_flags = detect_contamination(content, primary_role, config)
    chunk_kind = classify_chunk_kind(heading, chunk_type, content)

    # P4c: table safety flags feed into purity_score
    if chunk_kind == "table_rows":
        table_flags = validate_table_safety(content, config)
        contamination_flags.update(table_flags)

    purity_score = compute_purity(contamination_flags, config)

    # Allowed roles: config-driven tolerant map if available
    tolerant_map = config.get("section_tolerant_roles") or None
    allowed_roles = compute_allowed_roles(section_key, primary_role, tolerant_map)

    # Convert dict[str, bool] → list[str] for Weaviate TEXT_ARRAY compatibility
    contamination_flags_list = [k for k, v in contamination_flags.items() if v]

    return {
        "section_key": section_key,
        "primary_role": primary_role,
        "allowed_roles": allowed_roles,
        "purity_score": purity_score,
        "contamination_flags": contamination_flags_list,
        "chunk_kind": chunk_kind,
    }
