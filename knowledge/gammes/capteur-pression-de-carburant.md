---
entity_type: gamme
title: Capteur pression de carburant
slug: capteur-pression-de-carburant
pg_id: 817
category: capteurs
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Mesurer la pression du carburant dans la rampe d'injection et transmettre
    l'information au calculateur
  must_be_true:
    - mesurer
    - detecter
    - transmettre
  must_not_contain_concepts:
    - pompe
    - injecteur
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
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Perte de puissance a l acceleration
    description: perte de puissance a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance a l acceleration'
      - Vérification visuelle ou auditive
  - id: S2
    label: A-coups ou hesitations du moteur
    description: a-coups ou hesitations du moteur
    risk_level: confort
    evidence:
      - 'Observation: a-coups ou hesitations du moteur'
      - Vérification visuelle ou auditive
  - id: S3
    label: Cliquetis cognement moteur injection defaillante
    description: cliquetis cognement moteur injection defaillante
    risk_level: confort
    evidence:
      - 'Observation: cliquetis cognement moteur injection defaillante'
      - Vérification visuelle ou auditive
  - id: S4
    label: Voyant moteur avec codes p0190-p0194
    description: voyant moteur avec codes p0190-p0194
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur avec codes p0190-p0194'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur carburant anormale fuite mauvaise
    description: odeur carburant anormale fuite mauvaise
    risk_level: confort
    evidence:
      - 'Observation: odeur carburant anormale fuite mauvaise'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km sur moteur diesel hdi tdi
    description: plus de 150 000 km sur moteur diesel hdi tdi
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km sur moteur diesel hdi tdi'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Capteur pression de carburant - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la pression du carburant dans la rampe d'injection et transmettre l'information au calculateur

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- perte de puissance a l acceleration
- a-coups ou hesitations du moteur
- cliquetis cognement moteur injection defaillante
- voyant moteur avec codes p0190-p0194
- odeur carburant anormale fuite mauvaise
- plus de 150 000 km sur moteur diesel hdi tdi

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur pression de carburant:

1. **Inspection visuelle** - Examiner l'état du capteur pression de carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-a-carburant
- pompe-a-injection

## Critères de Compatibilité

Pour commander le bon capteur pression de carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la panne"
