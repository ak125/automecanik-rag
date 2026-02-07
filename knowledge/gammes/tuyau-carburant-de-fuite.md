---
entity_type: gamme
title: Tuyau carburant de fuite
slug: tuyau-carburant-de-fuite
pg_id: 3937
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Evacuer le carburant excedentaire des injecteurs vers le reservoir
  must_be_true:
    - evacuer
    - retourner
    - canaliser
  must_not_contain_concepts:
    - freinage
    - climatisation
    - distribution
    - embrayage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_general_detecte
    then: inspection_visuelle_et_test_fonctionnel
symptoms:
  - id: S1
    label: Odeur de gasoil dans le compartiment moteur
    description: odeur de gasoil dans le compartiment moteur
    risk_level: confort
    evidence:
      - 'Observation: odeur de gasoil dans le compartiment moteur'
      - Vérification visuelle ou auditive
  - id: S2
    label: Traces de carburant sur les injecteurs
    description: traces de carburant sur les injecteurs
    risk_level: confort
    evidence:
      - 'Observation: traces de carburant sur les injecteurs'
      - Vérification visuelle ou auditive
  - id: S3
    label: Surconsommation de carburant
    description: surconsommation de carburant
    risk_level: confort
    evidence:
      - 'Observation: surconsommation de carburant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Tuyau carburant de fuite - Guide Diagnostic Complet

## Fonction et Rôle

Evacuer le carburant excedentaire des injecteurs vers le reservoir

**Actions principales:** evacuer, retourner, canaliser

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- odeur de gasoil dans le compartiment moteur
- traces de carburant sur les injecteurs
- surconsommation de carburant

## Procédure de Diagnostic

Pour diagnostiquer un problème de tuyau carburant de fuite:

1. **Inspection visuelle** - Examiner l'état du tuyau carburant de fuite
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- injecteur
- pompe-d-injection

## Critères de Compatibilité

Pour commander le bon tuyau carburant de fuite, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"
