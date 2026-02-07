---
entity_type: gamme
title: Kit d'embrayage
slug: kit-d-embrayage
pg_id: 479
category: embrayage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Transmettre le couple moteur à la boîte de vitesses et permettre la
    séparation temporaire
  must_be_true:
    - transmettre le couple
    - accoupler
    - désaccoupler
  must_not_contain_concepts:
    - sélecteur
    - pommeau
    - levier de vitesses
    - differentiel
    - cardan
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
    label: Embrayage patine regime monte acceleration
    description: embrayage patine regime monte acceleration
    risk_level: confort
    evidence:
      - 'Observation: embrayage patine regime monte acceleration'
      - Vérification visuelle ou auditive
  - id: S2
    label: Odeur brule apres cote demarrage
    description: odeur brule apres cote demarrage
    risk_level: confort
    evidence:
      - 'Observation: odeur brule apres cote demarrage'
      - Vérification visuelle ou auditive
  - id: S3
    label: Pedale d embrayage anormalement haute ou basse
    description: pedale d embrayage anormalement haute ou basse
    risk_level: confort
    evidence:
      - 'Observation: pedale d embrayage anormalement haute ou basse'
      - Vérification visuelle ou auditive
  - id: S4
    label: Vibrations ou a-coups au demarrage
    description: vibrations ou a-coups au demarrage
    risk_level: confort
    evidence:
      - 'Observation: vibrations ou a-coups au demarrage'
      - Vérification visuelle ou auditive
  - id: S5
    label: Difficulte a passer les vitesses craquements
    description: difficulte a passer les vitesses craquements
    risk_level: confort
    evidence:
      - 'Observation: difficulte a passer les vitesses craquements'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km ou conduite urbaine intensive
    description: plus de 150 000 km ou conduite urbaine intensive
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km ou conduite urbaine intensive'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Kit d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le couple moteur à la boîte de vitesses et permettre la séparation temporaire

**Actions principales:** transmettre le couple, accoupler, désaccoupler, permettre le passage des rapports, relier

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- embrayage patine regime monte acceleration
- odeur brule apres cote demarrage
- pedale d embrayage anormalement haute ou basse
- vibrations ou a-coups au demarrage
- difficulte a passer les vitesses craquements
- plus de 150 000 km ou conduite urbaine intensive

## Procédure de Diagnostic

Pour diagnostiquer un problème de kit d'embrayage:

1. **Inspection visuelle** - Examiner l'état du kit d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- butee-d-embrayage
- cable-d-embrayage
- emetteur-d-embrayage
- recepteur-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon kit d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passage parfait"
