---
entity_type: gamme
title: Câble d'accélérateur
slug: cable-d-accelerateur
pg_id: 618
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmet la commande d'accélération de la pédale au papillon
  must_be_true:
    - transmettre
    - actionner
    - commander
  must_not_contain_concepts:
    - injection
    - papillon electronique
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
    label: Pedale d accelerateur dure ou rigide
    description: pedale d accelerateur dure ou rigide
    risk_level: confort
    evidence:
      - 'Observation: pedale d accelerateur dure ou rigide'
      - Vérification visuelle ou auditive
  - id: S2
    label: Reponse moteur retardee a l acceleration
    description: reponse moteur retardee a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: reponse moteur retardee a l acceleration'
      - Vérification visuelle ou auditive
  - id: S3
    label: Point dur lors de l enfoncement de la pedale
    description: point dur lors de l enfoncement de la pedale
    risk_level: confort
    evidence:
      - 'Observation: point dur lors de l enfoncement de la pedale'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Câble d'accélérateur - Guide Diagnostic Complet

## Fonction et Rôle

Transmet la commande d'accélération de la pédale au papillon

**Actions principales:** transmettre, actionner, commander

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- pedale d accelerateur dure ou rigide
- reponse moteur retardee a l acceleration
- point dur lors de l enfoncement de la pedale

## Procédure de Diagnostic

Pour diagnostiquer un problème de câble d'accélérateur:

1. **Inspection visuelle** - Examiner l'état du câble d'accélérateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- pedale
- papillon

## Critères de Compatibilité

Pour commander le bon câble d'accélérateur, vous devez connaître:

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
