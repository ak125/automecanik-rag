"""Role classifier for RAG chunks (Phase 1 + Phase 2).

Assigns 6 fields to each chunk:
  - section_key: inferred from heading/chunk_type
  - primary_role: canonical RoleId (R1_ROUTER..R6_SUPPORT)
  - allowed_roles: list of RoleIds this chunk is valid for
  - purity_score: 0-100, penalised by contamination
  - contamination_flags: list of detected cross-role signals
  - chunk_kind: content type for retrieval diversification (Phase 2)

All classification is heuristic (regex, no ML).
"""

import json
import re
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# ── Load role_map.json (module-level, cached) ──

_ROLE_MAP_PATH = Path(__file__).resolve().parent.parent.parent / "config" / "role_map.json"
_ROLE_MAP: dict = {}

try:
    with open(_ROLE_MAP_PATH, "r", encoding="utf-8") as f:
        _ROLE_MAP = json.load(f)
    logger.info("Loaded role_map.json with %d roles", len(_ROLE_MAP))
except FileNotFoundError:
    logger.warning("role_map.json not found at %s — role classification disabled", _ROLE_MAP_PATH)
except Exception as exc:
    logger.error("Failed to load role_map.json: %s", exc)

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


def infer_primary_role(section_key: str, source_type: str) -> str:
    """Infer the primary role from section_key + source_type."""
    st = (source_type or "").lower()

    # Source-type overrides for non-gamme documents
    if st in _SOURCE_TYPE_TO_ROLE:
        return _SOURCE_TYPE_TO_ROLE[st]

    # Gamme documents: use section_key mapping
    if st in {"gamme", "catalog"}:
        return _GAMME_SECTION_TO_ROLE.get(section_key, "R1_ROUTER")

    # Fallback
    return "R1_ROUTER"


# ── Contamination detection ──

_HOWTO_RE = re.compile(r"installer|monter|d[ée]monter|d[ée]poser|remonter", re.IGNORECASE)
_DIAG_RE = re.compile(r"sympt[oô]me|panne|diagnostic", re.IGNORECASE)
_PRICING_RE = re.compile(r"prix|tarif|\u20ac|EUR", re.IGNORECASE)
_STEP_SEQ_RE = re.compile(r"[ée]tape\s*\d|(?:^|\n)\s*1\.\s|(?:^|\n)\s*2\.\s|(?:^|\n)\s*3\.\s", re.IGNORECASE)

# Phase 4c: table safety patterns
_TABLE_IMPERATIVE_RE = re.compile(r"\b(remplacez|installez|d[ée]montez|d[ée]posez)\b", re.IGNORECASE)
_TABLE_STEP_SEQ_RE = re.compile(r"(?:^|\|)\s*[123]\.\s", re.MULTILINE)


def validate_table_safety(content: str) -> list[str]:
    """Detect unsafe patterns in table_rows chunks (P4c)."""
    flags: list[str] = []
    if _TABLE_IMPERATIVE_RE.search(content):
        flags.append("TABLE_HAS_IMPERATIVES")
    if _TABLE_STEP_SEQ_RE.search(content):
        flags.append("TABLE_HAS_STEP_SEQUENCE")
    return flags


def detect_contamination(content: str, primary_role: str) -> list[str]:
    """Detect cross-role signals that don't belong to primary_role."""
    flags: list[str] = []

    if primary_role not in {"R3_CONSEILS", "R5_DIAGNOSTIC"} and _HOWTO_RE.search(content):
        flags.append("HAS_HOWTO_MARKERS")

    if primary_role == "R1_ROUTER" and _DIAG_RE.search(content):
        flags.append("HAS_DIAG_WORDS")

    if primary_role != "R2_PRODUCT" and _PRICING_RE.search(content):
        flags.append("HAS_PRICING")

    if primary_role == "R1_ROUTER" and _STEP_SEQ_RE.search(content):
        flags.append("HAS_STEP_SEQUENCE")

    return flags


def compute_purity(contamination_flags: list[str]) -> int:
    """Compute purity score: 100 minus 15 per contamination flag."""
    return max(0, 100 - 15 * len(contamination_flags))


# ── Allowed roles ──

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


def compute_allowed_roles(section_key: str, primary_role: str) -> list[str]:
    """Compute the list of roles this chunk is valid for."""
    tolerant = _SECTION_TOLERANT_ROLES.get(section_key, [])
    # primary_role is always included; dedup while preserving order
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
) -> dict:
    """Classify a chunk and return the 6 role fields.

    Returns:
        dict with keys: section_key, primary_role, allowed_roles,
                        purity_score, contamination_flags, chunk_kind
    """
    section_key = heading_to_section_key(heading, chunk_type)
    primary_role = infer_primary_role(section_key, source_type)
    contamination_flags = detect_contamination(content, primary_role)
    chunk_kind = classify_chunk_kind(heading, chunk_type, content)
    # P4c: table safety flags feed into purity_score
    if chunk_kind == "table_rows":
        contamination_flags.extend(validate_table_safety(content))
    purity_score = compute_purity(contamination_flags)
    allowed_roles = compute_allowed_roles(section_key, primary_role)

    return {
        "section_key": section_key,
        "primary_role": primary_role,
        "allowed_roles": allowed_roles,
        "purity_score": purity_score,
        "contamination_flags": contamination_flags,
        "chunk_kind": chunk_kind,
    }
