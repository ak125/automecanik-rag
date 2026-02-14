"""Unit tests for pipeline enrichment functions.

These functions are executed on EVERY chunk at indexation time.
A silent regression would corrupt the entire vector database.

Run: cd /opt/automecanik/rag && .venv/bin/python -m unittest tests.test_pipeline_enrichment -v
"""

import sys
import os
import unittest

# Ensure orchestrator package is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from orchestrator.pipeline import (
    classify_domain,
    classify_intent,
    extract_entities,
    compute_evidence_grade,
    compute_doc_weight,
    infer_doc_family,
)


# ──────────────────────────────────────────────
#  classify_domain
# ──────────────────────────────────────────────


class TestClassifyDomain(unittest.TestCase):
    def test_freinage(self):
        self.assertEqual(classify_domain("Remplacement des plaquettes de frein avant"), "freinage")

    def test_moteur(self):
        self.assertEqual(classify_domain("Le turbo du moteur a une fuite d'huile"), "moteur")

    def test_transmission(self):
        self.assertEqual(classify_domain("Kit embrayage pour boite de vitesse manuelle"), "transmission")

    def test_suspension(self):
        self.assertEqual(classify_domain("Amortisseur arriere et silent-bloc de bras de suspension"), "suspension")

    def test_eclairage(self):
        self.assertEqual(classify_domain("Ampoule phare xenon et feux clignotant"), "eclairage")

    def test_filtration(self):
        self.assertEqual(classify_domain("Filtre a huile et filtre a air moteur"), "filtration")

    def test_refroidissement(self):
        self.assertEqual(classify_domain("Radiateur et pompe a eau thermostat"), "refroidissement")

    def test_distribution(self):
        self.assertEqual(classify_domain("Kit distribution courroie et galet tendeur"), "distribution")

    def test_echappement(self):
        self.assertEqual(classify_domain("Catalyseur FAP DPF echappement"), "echappement")

    def test_direction(self):
        self.assertEqual(classify_domain("Cremaillere de direction et rotule de direction"), "direction")

    def test_electricite(self):
        self.assertEqual(classify_domain("Batterie et alternateur demarreur capteur"), "electricite")

    def test_carrosserie(self):
        self.assertEqual(classify_domain("Pare-chocs avant et retroviseur calandre"), "carrosserie")

    def test_fallback_general(self):
        self.assertEqual(classify_domain("Bonjour comment ca va aujourd'hui"), "general")

    def test_empty_string(self):
        self.assertEqual(classify_domain(""), "general")

    def test_case_insensitive(self):
        self.assertEqual(classify_domain("PLAQUETTES DE FREIN AVANT"), "freinage")

    def test_highest_score_wins(self):
        result = classify_domain("frein plaquette disque de frein moteur")
        self.assertEqual(result, "freinage")


# ──────────────────────────────────────────────
#  classify_intent
# ──────────────────────────────────────────────


class TestClassifyIntent(unittest.TestCase):
    def test_diagnostic(self):
        self.assertEqual(classify_intent("Symptome de panne voyant moteur allume"), "diagnostic")

    def test_guide(self):
        self.assertEqual(classify_intent("Comment remplacer un filtre etape par etape procedure"), "guide")

    def test_comparaison(self):
        self.assertEqual(classify_intent("Comparatif Bosch versus Brembo difference"), "comparaison")

    def test_compatibilite(self):
        self.assertEqual(classify_intent("Compatible avec Peugeot 308 fitment OEM"), "compatibilite")

    def test_tarification(self):
        self.assertEqual(classify_intent("Prix tarif cout devis pour plaquettes"), "tarification")

    def test_specification(self):
        self.assertEqual(classify_intent("Reference technique dimension specification fiche"), "specification")

    def test_no_match(self):
        self.assertEqual(classify_intent("Bonjour le monde"), "")

    def test_empty_input(self):
        self.assertEqual(classify_intent(""), "")

    def test_case_insensitive(self):
        self.assertEqual(classify_intent("SYMPTOME DE PANNE"), "diagnostic")


# ──────────────────────────────────────────────
#  extract_entities
# ──────────────────────────────────────────────


class TestExtractEntities(unittest.TestCase):
    def test_brand_names(self):
        entities = extract_entities("Les plaquettes Bosch et Brembo sont compatibles")
        self.assertIn("Bosch", entities)
        self.assertIn("Brembo", entities)

    def test_oem_refs(self):
        entities = extract_entities("Reference GDB1726 et P68052 disponibles")
        self.assertIn("GDB1726", entities)
        self.assertIn("P68052", entities)

    def test_hyphenated_refs(self):
        entities = extract_entities("Ref TRW-GDB1726 pour ce vehicule")
        self.assertIn("TRW-GDB1726", entities)

    def test_brand_standalone_and_hyphenated(self):
        """Brand matched standalone even when also in hyphenated ref."""
        entities = extract_entities("TRW fabrique le TRW-GDB1726")
        self.assertIn("TRW", entities)
        self.assertIn("TRW-GDB1726", entities)

    def test_car_brands(self):
        entities = extract_entities("Compatible Peugeot 308 et Renault Megane")
        self.assertIn("Peugeot", entities)
        self.assertIn("Renault", entities)

    def test_dedup(self):
        entities = extract_entities("Bosch Bosch Bosch Bosch")
        self.assertEqual(entities.count("Bosch"), 1)

    def test_no_false_positives(self):
        """Common French words should NOT be extracted as entities."""
        entities = extract_entities(
            "Le kit est compatible avec ce modele. "
            "Cette reference est disponible en stock."
        )
        for word in ["Le", "kit", "est", "compatible", "avec", "ce", "Cette"]:
            self.assertNotIn(word, entities, f"False positive: '{word}' should not be an entity")

    def test_cap_at_30(self):
        refs = " ".join(f"REF{1000 + i}" for i in range(50))
        entities = extract_entities(refs)
        self.assertLessEqual(len(entities), 30)

    def test_empty_input(self):
        entities = extract_entities("")
        self.assertEqual(entities, [])

    def test_ate_brand(self):
        entities = extract_entities("Disques ATE et Ferodo haute performance")
        self.assertIn("ATE", entities)
        self.assertIn("Ferodo", entities)


# ──────────────────────────────────────────────
#  compute_evidence_grade
# ──────────────────────────────────────────────

GRADE_ORDER = {"A": 4, "B": 3, "C": 2, "D": 1}


class TestComputeEvidenceGrade(unittest.TestCase):
    def _long_content(self, words: int = 250) -> str:
        base = "plaquettes de frein Bosch P68052 Brembo GDB1726 ATE Ferodo Textar performance "
        repeats = (words // len(base.split())) + 1
        return base * repeats

    def test_grade_a_full_score(self):
        """L1 + many entities + long content + heading + specific domain = A."""
        content = self._long_content(250)
        entities = extract_entities(content)
        grade = compute_evidence_grade(
            content=content, truth_level="L1", domain="freinage",
            entities=entities, heading="Plaquettes de frein avant",
        )
        self.assertEqual(grade, "A")

    def test_grade_d_minimal(self):
        """L4 + no entities + very short + no heading + general = D."""
        grade = compute_evidence_grade(
            content="ok", truth_level="L4", domain="general",
            entities=[], heading=None,
        )
        self.assertEqual(grade, "D")

    def test_grade_b_medium(self):
        """L2 + some entities + medium content = B."""
        content = "Plaquettes Bosch GDB1726 compatible Peugeot. " * 15
        entities = extract_entities(content)
        grade = compute_evidence_grade(
            content=content, truth_level="L2", domain="freinage",
            entities=entities, heading=None,
        )
        self.assertEqual(grade, "B")

    def test_grade_c_moderate(self):
        """L3 + some entities + moderate content + domain = C."""
        # Score: L3=14 + 3 entities=18 + ~45 words=8 + domain=10 = 50 -> C (>=35)
        content = "Filtre a huile Bosch pour Renault Clio moteur essence. " * 5
        grade = compute_evidence_grade(
            content=content, truth_level="L3", domain="filtration",
            entities=["Renault", "Bosch", "P68052"], heading=None,
        )
        self.assertEqual(grade, "C")

    def test_truth_level_impact(self):
        kwargs = dict(content="mot " * 50, domain="general", entities=[], heading=None)
        grade_l1 = compute_evidence_grade(truth_level="L1", **kwargs)
        grade_l4 = compute_evidence_grade(truth_level="L4", **kwargs)
        self.assertGreaterEqual(GRADE_ORDER[grade_l1], GRADE_ORDER[grade_l4])

    def test_heading_impact(self):
        kwargs = dict(content="mot " * 50, truth_level="L3", domain="general", entities=[])
        grade_with = compute_evidence_grade(heading="Section title", **kwargs)
        grade_without = compute_evidence_grade(heading=None, **kwargs)
        self.assertGreaterEqual(GRADE_ORDER[grade_with], GRADE_ORDER[grade_without])

    def test_domain_impact(self):
        kwargs = dict(content="mot " * 50, truth_level="L3", entities=[], heading=None)
        grade_specific = compute_evidence_grade(domain="freinage", **kwargs)
        grade_general = compute_evidence_grade(domain="general", **kwargs)
        self.assertGreaterEqual(GRADE_ORDER[grade_specific], GRADE_ORDER[grade_general])

    def test_entity_richness_impact(self):
        kwargs = dict(content="mot " * 50, truth_level="L3", domain="general", heading=None)
        grade_many = compute_evidence_grade(
            entities=["Bosch", "Brembo", "ATE", "TRW", "Valeo"], **kwargs
        )
        grade_none = compute_evidence_grade(entities=[], **kwargs)
        self.assertGreaterEqual(GRADE_ORDER[grade_many], GRADE_ORDER[grade_none])


# ──────────────────────────────────────────────
#  compute_doc_weight
# ──────────────────────────────────────────────


class TestComputeDocWeight(unittest.TestCase):
    def test_l1_canonical(self):
        self.assertEqual(compute_doc_weight("L1", is_canonical=True), 1.0)

    def test_l2_non_canonical(self):
        self.assertEqual(compute_doc_weight("L2", is_canonical=False), 0.85)

    def test_l3_default(self):
        self.assertEqual(compute_doc_weight("L3", is_canonical=False), 0.7)

    def test_l4_low(self):
        self.assertEqual(compute_doc_weight("L4", is_canonical=False), 0.5)

    def test_canonical_bonus_capped(self):
        self.assertLessEqual(compute_doc_weight("L1", is_canonical=True), 1.0)

    def test_unknown_truth_level(self):
        self.assertEqual(compute_doc_weight("L99", is_canonical=False), 0.7)


# ──────────────────────────────────────────────
#  infer_doc_family
# ──────────────────────────────────────────────


class TestInferDocFamily(unittest.TestCase):
    def test_diagnostic_namespace(self):
        self.assertEqual(infer_doc_family("guide", "diagnostic"), "diagnostic")

    def test_diagnostic_source_type(self):
        self.assertEqual(infer_doc_family("diagnostic", "general"), "diagnostic")

    def test_catalog_namespace(self):
        self.assertEqual(infer_doc_family("guide", "gamme-freinage"), "catalog")

    def test_catalog_source_type(self):
        self.assertEqual(infer_doc_family("gamme", "general"), "catalog")

    def test_media_namespace(self):
        self.assertEqual(infer_doc_family("guide", "media-images"), "media")

    def test_router_memory(self):
        self.assertEqual(infer_doc_family("guide", "router-logs"), "router_memory")

    def test_default_knowledge(self):
        self.assertEqual(infer_doc_family("guide", "general"), "knowledge")


if __name__ == "__main__":
    unittest.main()
