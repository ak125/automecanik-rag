"""Build and validate strict GammeContentContract with per-section quality gate."""

from __future__ import annotations

import re
import unicodedata
from typing import Any

CONTRACT_VERSION = "GammeContentContract.v1"

QUALITY_FLAGS = {
    "GENERIC_PHRASES",
    "MISSING_REQUIRED_TERMS",
    "TOO_SHORT",
    "TOO_LONG",
    "FAQ_TOO_SMALL",
    "SYMPTOMS_TOO_SMALL",
    "DUPLICATE_ITEMS",
}

FLAG_PENALTIES = {
    "GENERIC_PHRASES": 18,
    "MISSING_REQUIRED_TERMS": 16,
    "TOO_SHORT": 10,
    "TOO_LONG": 8,
    "FAQ_TOO_SMALL": 14,
    "SYMPTOMS_TOO_SMALL": 12,
    "DUPLICATE_ITEMS": 8,
}

DEFAULT_REQUIRED_FIELDS = ["marque", "modele", "type", "motorisation"]

DEFAULT_FALLBACK_SYMPTOMS = [
    "Perte progressive de performance dans les usages courants.",
    "Bruits ou comportements anormaux qui augmentent avec le temps.",
    "Alertes ou ressenti de conduite degrade demandant un controle rapide.",
]

DEFAULT_FALLBACK_ANTI_MISTAKES = [
    "Ne pas commander sans verifier la compatibilite vehicule.",
    "Ne pas ignorer les preconisations constructeur de montage.",
    "Ne pas differer le remplacement en cas de symptomes persistants.",
]

DEFAULT_FALLBACK_CONSEQUENCES = [
    "Risque de panne secondaire si la piece reste degradee.",
    "Risque d immobilisation et de surcout atelier.",
    "Risque de baisse de securite et de fiabilite globale.",
]

GENERIC_PHRASES = [
    "role essentiel",
    "entretien regulier",
    "piece importante",
    "bon fonctionnement",
    "il est recommande",
    "il est conseille",
    "en bon etat",
    "piece indispensable",
]

FAMILY_REQUIRED_TERMS = {
    "freinage": ["frein", "freinage", "distance", "securite"],
    "moteur": ["moteur", "combustion", "lubrification", "fiabilite"],
    "suspension": ["suspension", "stabilite", "amortissement", "tenue"],
    "transmission": ["transmission", "couple", "embrayage", "motricite"],
    "electrique": ["electrique", "charge", "alimentation", "batterie"],
    "climatisation": ["climatisation", "froid", "pression", "compresseur"],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _clean_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    return re.sub(r"\s+", " ", text).strip()



def _parse_int(value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    text = _clean_text(value)
    if not text:
        return None
    try:
        return int(text)
    except ValueError:
        return None



def _normalize_key(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = ascii_text.lower().strip()
    ascii_text = re.sub(r"[^a-z0-9]+", "-", ascii_text)
    return ascii_text.strip("-")



def _dedupe_non_empty(values: list[Any]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        text = _clean_text(value)
        if not text:
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        output.append(text)
    return output



def _dedupe_with_duplicate_flag(values: list[str]) -> tuple[list[str], bool]:
    out: list[str] = []
    seen: set[str] = set()
    duplicate_found = False
    for value in values:
        text = _clean_text(value)
        if not text:
            continue
        key = text.lower()
        if key in seen:
            duplicate_found = True
            continue
        seen.add(key)
        out.append(text)
    return out, duplicate_found



def _extract_heading_sections(markdown: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current_heading = ""
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_heading, current_lines
        if not current_heading:
            current_lines = []
            return
        key = _normalize_key(current_heading)
        if key:
            sections[key] = list(current_lines)
        current_lines = []

    for line in markdown.splitlines():
        if re.match(r"^##+\s+", line):
            flush()
            current_heading = re.sub(r"^##+\s+", "", line).strip()
            continue
        if current_heading:
            current_lines.append(line)

    flush()
    return sections



def _extract_bullets(lines: list[str]) -> list[str]:
    bullets: list[str] = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^[-*]\s+", stripped):
            bullets.append(re.sub(r"^[-*]\s+", "", stripped).strip())
            continue
        if re.match(r"^\d+[.)]\s+", stripped):
            bullets.append(re.sub(r"^\d+[.)]\s+", "", stripped).strip())
            continue
    return _dedupe_non_empty(bullets)



def _extract_first_sentence(lines: list[str]) -> str:
    text = _clean_text(" ".join(lines))
    if not text:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", text)
    return _clean_text(parts[0] if parts else text)



def _extract_primary_fact(lines: list[str]) -> str:
    bullets = _extract_bullets(lines)
    if bullets:
        return _clean_text(re.sub(r"^\d+[.)]\s*", "", bullets[0]))
    sentence = _extract_first_sentence(lines)
    return _clean_text(re.sub(r"^\d+[.)]\s*", "", sentence))



def _find_section_keys(sections: dict[str, list[str]], patterns: list[str]) -> list[str]:
    keys: list[str] = []
    for key in sections.keys():
        for pattern in patterns:
            if pattern in key:
                keys.append(key)
                break
    return keys



def _extract_frontmatter_symptoms(metadata: dict[str, Any]) -> list[str]:
    raw = metadata.get("symptoms")
    if not isinstance(raw, list):
        return []

    out: list[str] = []
    for item in raw:
        if isinstance(item, dict):
            desc = _clean_text(item.get("description") or item.get("label"))
            if desc:
                out.append(desc)
        else:
            text = _clean_text(item)
            if text:
                out.append(text)
    return _dedupe_non_empty(out)



def _extract_required_fields(lines: list[str]) -> list[str]:
    bullets = [b.lower() for b in _extract_bullets(lines)]
    fields: list[str] = []

    def add(field: str) -> None:
        if field not in fields:
            fields.append(field)

    for bullet in bullets:
        if "marque" in bullet or "brand" in bullet:
            add("marque")
        if "modele" in bullet or "model" in bullet:
            add("modele")
        if "type" in bullet or "annee" in bullet or "an" in bullet:
            add("type")
        if "motor" in bullet or "moteur" in bullet or "motorisation" in bullet:
            add("motorisation")

    return fields or list(DEFAULT_REQUIRED_FIELDS)



def _extract_faq_items(lines: list[str]) -> tuple[list[dict[str, str]], bool]:
    items: list[dict[str, str]] = []
    question = ""
    answer_lines: list[str] = []

    def flush() -> None:
        nonlocal question, answer_lines
        q = _clean_text(question)
        a = _clean_text(" ".join(answer_lines))
        if q and a:
            items.append({"question": q, "answer": a})
        question = ""
        answer_lines = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        if re.match(r"^(q(?:uestion)?\s*[:\-])", stripped, flags=re.IGNORECASE):
            flush()
            question = re.sub(r"^(q(?:uestion)?\s*[:\-])", "", stripped, flags=re.IGNORECASE).strip()
            continue

        if stripped.endswith("?") and not question:
            flush()
            question = stripped
            continue

        if re.match(r"^(r(?:eponse)?\s*[:\-])", stripped, flags=re.IGNORECASE):
            answer_lines.append(
                re.sub(r"^(r(?:eponse)?\s*[:\-])", "", stripped, flags=re.IGNORECASE).strip()
            )
            continue

        if question:
            answer_lines.append(stripped)

    flush()

    deduped: list[dict[str, str]] = []
    seen: set[str] = set()
    duplicate_found = False
    for item in items:
        key = _clean_text(item.get("question")).lower()
        if not key:
            continue
        if key in seen:
            duplicate_found = True
            continue
        seen.add(key)
        deduped.append(
            {
                "question": _clean_text(item.get("question")),
                "answer": _clean_text(item.get("answer")),
            }
        )
    return deduped, duplicate_found



def _contains_generic_phrase(text: str) -> bool:
    lower = _clean_text(text).lower()
    if not lower:
        return False
    return any(phrase in lower for phrase in GENERIC_PHRASES)



def _resolve_family_key(metadata: dict[str, Any]) -> str:
    category = _clean_text(metadata.get("category")).lower()
    subcategory = _clean_text(metadata.get("subcategory")).lower()

    for candidate in [category, subcategory]:
        if candidate in FAMILY_REQUIRED_TERMS:
            return candidate

    for key in FAMILY_REQUIRED_TERMS.keys():
        if key in category or key in subcategory:
            return key

    return ""



def _fallback_intro_role(gamme_name: str, family_key: str) -> str:
    terms = FAMILY_REQUIRED_TERMS.get(family_key) or ["compatibilite", "securite"]
    return (
        f"{gamme_name} intervient directement sur {terms[0]} du vehicule. "
        f"Un choix conforme protege la {terms[min(1, len(terms)-1)]} et limite les pannes secondaires."
    )



def _fallback_risk(gamme_name: str) -> dict[str, Any]:
    return {
        "title": f"Pourquoi remplacer {gamme_name} a temps ?",
        "explanation": (
            f"Reporter le remplacement de {gamme_name} augmente progressivement le risque de panne, "
            "de perte de performance et de surcout atelier."
        ),
        "consequences": list(DEFAULT_FALLBACK_CONSEQUENCES),
        "costRange": "120 a 1200 EUR selon vehicule et niveau de panne.",
        "conclusion": "Un controle precoce reduit le risque technique et financier.",
    }



def _fallback_timing() -> dict[str, str]:
    return {
        "title": "Quand intervenir ?",
        "years": "Controle annuel recommande",
        "km": "Controle a chaque revision constructeur",
        "note": "Ne pas attendre la panne complete pour intervenir.",
    }



def _fallback_arguments() -> list[dict[str, str]]:
    return [
        {
            "title": "Compatibilite verifiee",
            "content": "Selection guidee par vehicule et references techniques.",
            "icon": "check-circle",
        },
        {
            "title": "Priorite securite",
            "content": "Un remplacement a temps limite les risques de panne secondaire.",
            "icon": "shield-check",
        },
        {
            "title": "Decision rapide",
            "content": "Le guide structure les controles avant commande.",
            "icon": "clock",
        },
        {
            "title": "Montage maitrise",
            "content": "La verification des pieces associees reduit les retours atelier.",
            "icon": "list-check",
        },
    ]



def _fallback_how_to_choose(gamme_name: str, required_fields: list[str], family_key: str) -> str:
    terms = FAMILY_REQUIRED_TERMS.get(family_key) or ["compatibilite"]
    fields = required_fields or list(DEFAULT_REQUIRED_FIELDS)
    return (
        f"Renseignez {', '.join(fields)} puis comparez references et dimensions. "
        f"Validez ensuite les contraintes de {terms[0]} pour confirmer {gamme_name}."
    )



def _build_default_faq(gamme_name: str, symptoms: list[str]) -> list[dict[str, str]]:
    symptom_hint = symptoms[0] if symptoms else "des symptomes anormaux"
    return [
        {
            "question": f"Comment choisir {gamme_name} compatible avec mon vehicule ?",
            "answer": "Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.",
        },
        {
            "question": f"Quand remplacer {gamme_name} ?",
            "answer": f"En cas de {symptom_hint.lower()} ou de degradation mesurable, il faut controler rapidement avant panne secondaire.",
        },
        {
            "question": f"Puis-je monter {gamme_name} sans verification atelier ?",
            "answer": "Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.",
        },
    ]


# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------


def build_gamme_page_contract(
    metadata: dict[str, Any],
    content: str,
    source_path: str,
) -> dict[str, Any]:
    source_type = _clean_text(metadata.get("source_type") or metadata.get("entity_type")).lower()
    if source_type != "gamme":
        raise ValueError("build_gamme_page_contract requires source_type=gamme")

    sections = _extract_heading_sections(content)
    family_key = _resolve_family_key(metadata)

    raw_title = _clean_text(metadata.get("title") or metadata.get("slug") or "cette piece")
    gamme_name = re.sub(r"\s*:\s*fiche\s+gamme$", "", raw_title, flags=re.IGNORECASE).strip() or raw_title

    pg_id_raw = _clean_text(metadata.get("pg_id"))
    pg_id = pg_id_raw or "0"
    contract_id = _parse_int(metadata.get("id"))
    if contract_id is None:
        contract_id = _parse_int(metadata.get("pg_id")) or 0

    mechanical_rules = metadata.get("mechanical_rules") if isinstance(metadata.get("mechanical_rules"), dict) else {}

    role_keys = _find_section_keys(sections, ["fonction", "role", "piece"])
    role_lines = sections[role_keys[0]] if role_keys else []
    role_summary = _clean_text(mechanical_rules.get("role_summary"))
    intro_role = role_summary or _extract_primary_fact(role_lines)

    symptom_keys = _find_section_keys(sections, ["symptome", "defaillance"])
    symptom_lines: list[str] = []
    for key in symptom_keys:
        symptom_lines.extend(_extract_bullets(sections.get(key, [])))

    symptoms_source = _dedupe_non_empty(_extract_frontmatter_symptoms(metadata) + symptom_lines)

    error_keys = _find_section_keys(sections, ["erreur", "attention", "eviter"])
    error_lines = sections[error_keys[0]] if error_keys else []
    error_bullets = _extract_bullets(error_lines)

    solution_keys = _find_section_keys(sections, ["solution", "remplacer"])
    solution_lines = sections[solution_keys[0]] if solution_keys else []
    solution_bullets = _extract_bullets(solution_lines)

    anti_mistakes_source = _dedupe_non_empty(error_bullets + solution_bullets[:3])

    causes_keys = _find_section_keys(sections, ["cause", "probable"])
    causes_lines = sections[causes_keys[0]] if causes_keys else []
    causes_bullets = _extract_bullets(causes_lines)

    compat_keys = _find_section_keys(sections, ["compatibil", "critere", "vehicule"])
    compat_lines = sections[compat_keys[0]] if compat_keys else []
    required_fields = _extract_required_fields(compat_lines)

    faq_keys = _find_section_keys(sections, ["faq", "question"])
    faq_lines: list[str] = []
    for key in faq_keys:
        faq_lines.extend(sections.get(key, []))
    faq_source, faq_has_duplicates = _extract_faq_items(faq_lines)

    intro_sync_parts = _dedupe_non_empty((mechanical_rules.get("must_be_true") or [])[:4])
    if not intro_sync_parts:
        intro_sync_parts = [
            "Verifier les pieces associees au montage.",
            "Controler la reference exacte.",
        ]

    risk_explanation = _extract_primary_fact(causes_lines)
    risk_consequences = _dedupe_non_empty(causes_bullets + anti_mistakes_source[:2])

    cost_range = _clean_text(metadata.get("cost_range") or metadata.get("risk_cost_range"))

    timing_keys = _find_section_keys(sections, ["quand", "interval", "timing", "remplacement"])
    timing_lines = sections[timing_keys[0]] if timing_keys else []
    timing_note = _extract_primary_fact(timing_lines) or _extract_primary_fact(solution_lines)

    timing_years = _clean_text(metadata.get("timing_years")) or "Controle annuel recommande"
    timing_km = _clean_text(metadata.get("timing_km")) or "Controle a chaque revision constructeur"

    contract = {
        "id": contract_id,
        "pgId": pg_id,
        "intro": {
            "title": f"A quoi sert {gamme_name} ?",
            "role": intro_role,
            "syncParts": intro_sync_parts,
        },
        "risk": {
            "title": f"Pourquoi remplacer {gamme_name} a temps ?",
            "explanation": risk_explanation,
            "consequences": risk_consequences,
            "costRange": cost_range,
            "conclusion": "Un diagnostic precoce reduit le risque technique et financier.",
        },
        "timing": {
            "title": "Quand intervenir ?",
            "years": timing_years,
            "km": timing_km,
            "note": timing_note,
        },
        "arguments": _fallback_arguments(),
        "howToChoose": _fallback_how_to_choose(gamme_name, required_fields, family_key),
        "symptoms": symptoms_source,
        "antiMistakes": anti_mistakes_source,
        "faq": faq_source,
        "quality": {
            "score": 100,
            "flags": [],
            "version": CONTRACT_VERSION,
            "source": f"reindex:{source_path}",
        },
    }

    flags: set[str] = set()

    def add_flag(flag: str) -> None:
        if flag in QUALITY_FLAGS:
            flags.add(flag)

    # 1) Generic phrases + length gates on text sections (section-level fallback)
    intro_role_text = _clean_text(contract["intro"].get("role"))
    if _contains_generic_phrase(intro_role_text):
        add_flag("GENERIC_PHRASES")
        contract["intro"]["role"] = _fallback_intro_role(gamme_name, family_key)
    elif len(intro_role_text) < 40:
        add_flag("TOO_SHORT")
        contract["intro"]["role"] = _fallback_intro_role(gamme_name, family_key)
    elif len(intro_role_text) > 420:
        add_flag("TOO_LONG")
        contract["intro"]["role"] = _fallback_intro_role(gamme_name, family_key)

    risk_explanation_text = _clean_text(contract["risk"].get("explanation"))
    if _contains_generic_phrase(risk_explanation_text):
        add_flag("GENERIC_PHRASES")
        contract["risk"] = _fallback_risk(gamme_name)
    elif len(risk_explanation_text) < 40:
        add_flag("TOO_SHORT")
        contract["risk"] = _fallback_risk(gamme_name)
    elif len(risk_explanation_text) > 420:
        add_flag("TOO_LONG")
        contract["risk"] = _fallback_risk(gamme_name)
    else:
        consequences = contract["risk"].get("consequences") if isinstance(contract["risk"].get("consequences"), list) else []
        consequences_clean, duplicates = _dedupe_with_duplicate_flag([_clean_text(c) for c in consequences])
        if duplicates:
            add_flag("DUPLICATE_ITEMS")
        if len(consequences_clean) < 3:
            add_flag("TOO_SHORT")
            contract["risk"] = _fallback_risk(gamme_name)
        else:
            contract["risk"]["consequences"] = consequences_clean[:6]
            contract["risk"]["costRange"] = _clean_text(contract["risk"].get("costRange")) or _fallback_risk(gamme_name)["costRange"]

    timing_note_text = _clean_text(contract["timing"].get("note"))
    if _contains_generic_phrase(timing_note_text):
        add_flag("GENERIC_PHRASES")
        contract["timing"] = _fallback_timing()
    elif len(timing_note_text) < 25:
        add_flag("TOO_SHORT")
        contract["timing"] = _fallback_timing()
    elif len(timing_note_text) > 260:
        add_flag("TOO_LONG")
        contract["timing"] = _fallback_timing()
    else:
        if not _clean_text(contract["timing"].get("years")) and not _clean_text(contract["timing"].get("km")):
            add_flag("TOO_SHORT")
            contract["timing"] = _fallback_timing()

    how_to_choose_text = _clean_text(contract.get("howToChoose"))
    if _contains_generic_phrase(how_to_choose_text):
        add_flag("GENERIC_PHRASES")
        contract["howToChoose"] = _fallback_how_to_choose(gamme_name, required_fields, family_key)
    elif len(how_to_choose_text) < 45:
        add_flag("TOO_SHORT")
        contract["howToChoose"] = _fallback_how_to_choose(gamme_name, required_fields, family_key)
    elif len(how_to_choose_text) > 320:
        add_flag("TOO_LONG")
        contract["howToChoose"] = _fallback_how_to_choose(gamme_name, required_fields, family_key)

    # 2) Family required terms gate (fallback only KO sections)
    required_terms = FAMILY_REQUIRED_TERMS.get(family_key, [])
    if required_terms:
        combined = " ".join(
            [
                _clean_text(contract["intro"].get("role")),
                _clean_text(contract["risk"].get("explanation")),
                _clean_text(contract.get("howToChoose")),
                " ".join(contract.get("symptoms") or []),
            ]
        ).lower()
        matched_count = sum(1 for term in required_terms if term in combined)
        if matched_count < min(2, len(required_terms)):
            add_flag("MISSING_REQUIRED_TERMS")
            if not any(term in _clean_text(contract["intro"].get("role")).lower() for term in required_terms):
                contract["intro"]["role"] = _fallback_intro_role(gamme_name, family_key)
            if not any(term in _clean_text(contract.get("howToChoose")).lower() for term in required_terms):
                contract["howToChoose"] = _fallback_how_to_choose(gamme_name, required_fields, family_key)

    # 3) Symptoms gate
    symptoms = [_clean_text(item) for item in (contract.get("symptoms") or [])]
    symptoms_clean, symptoms_duplicates = _dedupe_with_duplicate_flag(symptoms)
    if symptoms_duplicates:
        add_flag("DUPLICATE_ITEMS")
    if len(symptoms_clean) < 3:
        add_flag("SYMPTOMS_TOO_SMALL")
        contract["symptoms"] = list(DEFAULT_FALLBACK_SYMPTOMS)
    else:
        contract["symptoms"] = symptoms_clean[:12]

    # 4) Anti mistakes gate
    anti = [_clean_text(item) for item in (contract.get("antiMistakes") or [])]
    anti_clean, anti_duplicates = _dedupe_with_duplicate_flag(anti)
    if anti_duplicates:
        add_flag("DUPLICATE_ITEMS")
    if len(anti_clean) < 3:
        add_flag("TOO_SHORT")
        contract["antiMistakes"] = list(DEFAULT_FALLBACK_ANTI_MISTAKES)
    else:
        contract["antiMistakes"] = anti_clean[:12]

    # 5) FAQ gate
    faq_items = contract.get("faq") if isinstance(contract.get("faq"), list) else []
    faq_clean: list[dict[str, str]] = []
    seen_questions: set[str] = set()
    duplicate_question = faq_has_duplicates
    for item in faq_items:
        if not isinstance(item, dict):
            continue
        q = _clean_text(item.get("question"))
        a = _clean_text(item.get("answer"))
        if not q or not a:
            continue
        key = q.lower()
        if key in seen_questions:
            duplicate_question = True
            continue
        seen_questions.add(key)
        faq_clean.append({"question": q, "answer": a})

    if duplicate_question:
        add_flag("DUPLICATE_ITEMS")

    short_answers = [item for item in faq_clean if len(_clean_text(item.get("answer"))) < 45]
    if len(faq_clean) < 3:
        add_flag("FAQ_TOO_SMALL")
        contract["faq"] = _build_default_faq(gamme_name, contract.get("symptoms") or [])
    elif short_answers:
        add_flag("TOO_SHORT")
        contract["faq"] = _build_default_faq(gamme_name, contract.get("symptoms") or [])
    else:
        contract["faq"] = faq_clean[:10]

    # 6) Arguments gate
    arguments = contract.get("arguments") if isinstance(contract.get("arguments"), list) else []
    if len(arguments) < 3:
        add_flag("TOO_SHORT")
        contract["arguments"] = _fallback_arguments()
    elif len(arguments) > 8:
        add_flag("TOO_LONG")
        contract["arguments"] = arguments[:8]

    # score + quality
    penalties = sum(FLAG_PENALTIES.get(flag, 0) for flag in flags)
    score = max(0, min(100, 100 - penalties))

    contract["quality"] = {
        "score": score,
        "flags": sorted(flags),
        "version": CONTRACT_VERSION,
        "source": f"reindex:{source_path}",
    }

    return contract


# ---------------------------------------------------------------------------
# Validator
# ---------------------------------------------------------------------------


def validate_gamme_page_contract(contract: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(contract, dict):
        return ["contract must be an object"], warnings

    if "h1" in contract:
        errors.append("contract must not contain h1")

    if not isinstance(contract.get("id"), int):
        errors.append("id must be an integer")

    pg_id = _clean_text(contract.get("pgId"))
    if not pg_id:
        errors.append("pgId is required")

    intro = contract.get("intro") if isinstance(contract.get("intro"), dict) else {}
    role = _clean_text(intro.get("role"))
    if len(role) < 40:
        errors.append("intro.role too short")

    risk = contract.get("risk") if isinstance(contract.get("risk"), dict) else {}
    if len(_clean_text(risk.get("explanation"))) < 40:
        errors.append("risk.explanation too short")

    timing = contract.get("timing") if isinstance(contract.get("timing"), dict) else {}
    timing_note = _clean_text(timing.get("note"))
    if len(timing_note) < 25:
        errors.append("timing.note too short")

    how_to_choose = _clean_text(contract.get("howToChoose"))
    if len(how_to_choose) < 45:
        errors.append("howToChoose too short")

    arguments = contract.get("arguments") if isinstance(contract.get("arguments"), list) else []
    if len(arguments) < 3:
        errors.append("arguments requires >=3 items")

    symptoms = contract.get("symptoms") if isinstance(contract.get("symptoms"), list) else []
    if len(symptoms) < 3:
        errors.append("symptoms requires >=3 items")

    anti_mistakes = contract.get("antiMistakes") if isinstance(contract.get("antiMistakes"), list) else []
    if len(anti_mistakes) < 3:
        errors.append("antiMistakes requires >=3 items")

    faq = contract.get("faq") if isinstance(contract.get("faq"), list) else []
    if len(faq) < 3:
        errors.append("faq requires >=3 items")

    quality = contract.get("quality") if isinstance(contract.get("quality"), dict) else {}
    score = quality.get("score")
    if not isinstance(score, int):
        errors.append("quality.score must be integer")
    elif score < 40:
        warnings.append(f"quality.score low={score}")

    flags = quality.get("flags") if isinstance(quality.get("flags"), list) else []
    invalid_flags = [flag for flag in flags if flag not in QUALITY_FLAGS]
    if invalid_flags:
        errors.append(f"quality.flags invalid={invalid_flags}")

    if quality.get("version") != CONTRACT_VERSION:
        errors.append(f"quality.version invalid={quality.get('version')}")

    if not _clean_text(quality.get("source")):
        errors.append("quality.source missing")

    return errors, warnings



def build_and_validate_gamme_page_contract(
    metadata: dict[str, Any],
    content: str,
    source_path: str,
) -> dict[str, Any]:
    contract = build_gamme_page_contract(metadata=metadata, content=content, source_path=source_path)
    errors, warnings = validate_gamme_page_contract(contract)
    return {
        "contract": contract,
        "errors": errors,
        "warnings": warnings,
    }
