---
entity_type: gamme
title: Guide d'embrayage
slug: guide-d-embrayage
pg_id: 4688
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Guider l'arbre primaire dans le volant moteur
  must_be_true:
    - guider
    - centrer
    - positionner
  must_not_contain_concepts:
    - injection
    - freinage
    - climatisation
    - turbo
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Embrayage mal centre
    description: embrayage mal centre
    risk_level: confort
    evidence:
      - 'Observation: embrayage mal centre'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vibrations au demarrage
    description: vibrations au demarrage
    risk_level: confort
    evidence:
      - 'Observation: vibrations au demarrage'
      - Vérification visuelle ou auditive
  - id: S3
    label: Usure prematuree du disque
    description: usure prematuree du disque
    risk_level: confort
    evidence:
      - 'Observation: usure prematuree du disque'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Guide d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Guider l'arbre primaire dans le volant moteur

**Actions principales:** guider, centrer, positionner

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- embrayage mal centre
- vibrations au demarrage
- usure prematuree du disque

## Procédure de Diagnostic

Pour diagnostiquer un problème de guide d'embrayage:

1. **Inspection visuelle** - Examiner l'état du guide d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- fourchette-d-embrayage
- tringle-de-vitesses

## Critères de Compatibilité

Pour commander le bon guide d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passage de vitesse parfait"
