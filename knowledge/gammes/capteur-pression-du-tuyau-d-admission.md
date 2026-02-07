---
entity_type: gamme
title: Capteur pression du tuyau d'admission
slug: capteur-pression-du-tuyau-d-admission
pg_id: 3947
category: capteurs
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Mesurer la pression dans le collecteur d'admission
  must_be_true:
    - mesurer
    - detecter
    - transmettre
  must_not_contain_concepts:
    - reparation
    - regeneration
    - nettoyage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Ralenti instable ou irregulier
    description: ralenti instable ou irregulier
    risk_level: confort
    evidence:
      - 'Observation: ralenti instable ou irregulier'
      - Vérification visuelle ou auditive
  - id: S2
    label: Perte de puissance a l acceleration
    description: perte de puissance a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance a l acceleration'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement au niveau du collecteur d admission
    description: sifflement au niveau du collecteur d admission
    risk_level: confort
    evidence:
      - 'Observation: sifflement au niveau du collecteur d admission'
      - Vérification visuelle ou auditive
  - id: S4
    label: Voyant moteur avec codes p0105-p0109
    description: voyant moteur avec codes p0105-p0109
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur avec codes p0105-p0109'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de carburant melange mal dose
    description: odeur de carburant melange mal dose
    risk_level: confort
    evidence:
      - 'Observation: odeur de carburant melange mal dose'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km sans nettoyage
    description: plus de 150 000 km sans nettoyage
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km sans nettoyage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Capteur pression du tuyau d'admission - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la pression dans le collecteur d'admission

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- ralenti instable ou irregulier
- perte de puissance a l acceleration
- sifflement au niveau du collecteur d admission
- voyant moteur avec codes p0105-p0109
- odeur de carburant melange mal dose
- plus de 150 000 km sans nettoyage

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur pression du tuyau d'admission:

1. **Inspection visuelle** - Examiner l'état du capteur pression du tuyau d'admission
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-temperature-d-air-admission
- corps-papillon
- debitmetre-d-air
- filtre-a-air

## Critères de Compatibilité

Pour commander le bon capteur pression du tuyau d'admission, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "mesure parfaite"
