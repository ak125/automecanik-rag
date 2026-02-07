---
entity_type: gamme
title: Pompe à injection
slug: pompe-a-injection
pg_id: 3904
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Mettre le carburant sous haute pression pour alimenter les injecteurs
  must_be_true:
    - pressuriser
    - alimenter
    - comprimer
  must_not_contain_concepts:
    - basse pression
    - reservoir
    - air
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
    label: Demarrage difficile
    description: demarrage difficile
    risk_level: confort
    evidence:
      - 'Observation: demarrage difficile'
      - Vérification visuelle ou auditive
  - id: S2
    label: Perte de puissance
    description: perte de puissance
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fumee
    description: fumee
    risk_level: confort
    evidence:
      - 'Observation: fumee'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe à injection - Guide Diagnostic Complet

## Fonction et Rôle

Mettre le carburant sous haute pression pour alimenter les injecteurs

**Actions principales:** pressuriser, alimenter, comprimer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage difficile
- perte de puissance
- fumee

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à injection:

1. **Inspection visuelle** - Examiner l'état du pompe à injection
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-pression-de-carburant
- injecteur

## Critères de Compatibilité

Pour commander le bon pompe à injection, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"
