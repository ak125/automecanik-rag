"""Tests for strict gamme page contract generation in local RAG repo."""

from app.services.gamme_page_contract import build_and_validate_gamme_page_contract


def test_build_contract_from_frontmatter_and_sections():
    metadata = {
        "source_type": "gamme",
        "title": "Disque de frein",
        "category": "freinage",
        "mechanical_rules": {
            "role_summary": "Le disque de frein convertit l energie cinetique en chaleur.",
            "must_be_true": ["freiner", "ralentir le vehicule", "dissiper la chaleur"],
        },
        "symptoms": [
            {"description": "Vibration au freinage"},
            {"description": "Bruit metallique"},
            {"description": "Distance de freinage allongee"},
        ],
    }
    content = """
# Disque de frein

## Criteres de compatibilite
- Marque du vehicule
- Modele du vehicule
- Type moteur
- Annee

## Causes probables
- Usure normale
- Echauffement excessif

## Erreurs a eviter
- Ne pas melanger les references
- Ne pas remplacer un seul cote
"""

    result = build_and_validate_gamme_page_contract(
        metadata=metadata,
        content=content,
        source_path="gammes/disque-de-frein.md",
    )

    assert result["errors"] == []
    contract = result["contract"]
    assert contract["quality"]["version"] == "GammeContentContract.v1"
    assert isinstance(contract["intro"]["role"], str) and len(contract["intro"]["role"]) >= 40
    assert isinstance(contract["howToChoose"], str) and contract["howToChoose"]
    assert len(contract["symptoms"]) >= 3
    assert len(contract["antiMistakes"]) >= 3
    assert len(contract["faq"]) >= 3
    assert contract["quality"]["score"] >= 50


def test_fallback_flags_when_content_is_sparse():
    metadata = {
        "source_type": "gamme",
        "title": "Kit d embrayage",
        "category": "embrayage",
    }
    content = "# Kit d embrayage\n\nTexte tres court."

    result = build_and_validate_gamme_page_contract(
        metadata=metadata,
        content=content,
        source_path="gammes/kit-d-embrayage.md",
    )

    contract = result["contract"]
    assert "SYMPTOMS_TOO_SMALL" in contract["quality"]["flags"]
    assert "FAQ_TOO_SMALL" in contract["quality"]["flags"]
    assert "TOO_SHORT" in contract["quality"]["flags"]
    assert len(contract["faq"]) >= 3
    assert len(contract["symptoms"]) >= 3
    assert len(contract["antiMistakes"]) >= 3


def test_generic_and_duplicate_content_triggers_section_fallback():
    metadata = {
        "source_type": "gamme",
        "title": "Disque de frein",
        "category": "freinage",
    }
    content = """
# Disque de frein

## Role de la piece
Role essentiel pour le bon fonctionnement.

## Symptomes observables
- Vibrations au freinage
- Vibrations au freinage

## Causes probables
1. Usure avancee
2. Echauffement

## FAQ
Q: Pourquoi changer ?
R: Oui.
Q: Pourquoi changer ?
R: Oui.
"""

    result = build_and_validate_gamme_page_contract(
        metadata=metadata,
        content=content,
        source_path="gammes/disque-de-frein.md",
    )

    assert result["errors"] == []
    contract = result["contract"]
    flags = set(contract["quality"]["flags"])
    assert "GENERIC_PHRASES" in flags
    assert "DUPLICATE_ITEMS" in flags
    assert "SYMPTOMS_TOO_SMALL" in flags
    assert "FAQ_TOO_SMALL" in flags or "TOO_SHORT" in flags
    assert contract["risk"]["explanation"] != "1."
