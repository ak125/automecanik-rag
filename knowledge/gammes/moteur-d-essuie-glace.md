---
entity_type: gamme
title: Moteur d'essuie-glace
slug: moteur-d-essuie-glace
pg_id: 295
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Entraîne le mécanisme d'essuyage via la tringlerie
  must_be_true:
    - entrainer
    - actionner
    - alimenter
  must_not_contain_concepts:
    - balai
    - caoutchouc
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
    label: Essuie-glaces totalement inactifs
    description: essuie-glaces totalement inactifs
    risk_level: confort
    evidence:
      - 'Observation: essuie-glaces totalement inactifs'
      - Vérification visuelle ou auditive
  - id: S2
    label: Mouvement tres lent
    description: mouvement tres lent
    risk_level: confort
    evidence:
      - 'Observation: mouvement tres lent'
      - Vérification visuelle ou auditive
  - id: S3
    label: Arret en position aleatoire
    description: arret en position aleatoire
    risk_level: confort
    evidence:
      - 'Observation: arret en position aleatoire'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Moteur d'essuie-glace - Guide Diagnostic Complet

## Fonction et Rôle

Entraîne le mécanisme d'essuyage via la tringlerie

**Actions principales:** entrainer, actionner, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- essuie-glaces totalement inactifs
- mouvement tres lent
- arret en position aleatoire

## Procédure de Diagnostic

Pour diagnostiquer un problème de moteur d'essuie-glace:

1. **Inspection visuelle** - Examiner l'état du moteur d'essuie-glace
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- tringlerie
- bras
- balai

## Critères de Compatibilité

Pour commander le bon moteur d'essuie-glace, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"
