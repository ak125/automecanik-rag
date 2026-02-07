---
entity_type: gamme
title: Pompe à haute pression
slug: pompe-a-haute-pression
pg_id: 3918
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Mettre le carburant sous tres haute pression pour l'injection directe
  must_be_true:
    - pressuriser
    - comprimer
    - alimenter
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
    label: Demarrage impossible ou tres long
    description: demarrage impossible ou tres long
    risk_level: confort
    evidence:
      - 'Observation: demarrage impossible ou tres long'
      - Vérification visuelle ou auditive
  - id: S2
    label: Perte de puissance brutale
    description: perte de puissance brutale
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance brutale'
      - Vérification visuelle ou auditive
  - id: S3
    label: Limaille dans le filtre a gasoil
    description: limaille dans le filtre a gasoil
    risk_level: confort
    evidence:
      - 'Observation: limaille dans le filtre a gasoil'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe à haute pression - Guide Diagnostic Complet

## Fonction et Rôle

Mettre le carburant sous tres haute pression pour l'injection directe

**Actions principales:** pressuriser, comprimer, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage impossible ou tres long
- perte de puissance brutale
- limaille dans le filtre a gasoil

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à haute pression:

1. **Inspection visuelle** - Examiner l'état du pompe à haute pression
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- rampe-d-injection
- injecteur
- regulateur-de-pression-carburant

## Critères de Compatibilité

Pour commander le bon pompe à haute pression, vous devez connaître:

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
