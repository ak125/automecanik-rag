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
  - if: symptome_embrayage-patine-regime-monte-acceleration
    then: verifier_piece
  - if: symptome_odeur-brule-apres-cote-demarrage
    then: diagnostic_approfondi
  - if: symptome_pedale-d-embrayage-anormalement-haute-ou
    then: remplacement_recommande
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
    label: Pedale d embrayage anormalement haute ou
    description: pedale d embrayage anormalement haute ou basse
    risk_level: confort
    evidence:
      - 'Observation: pedale d embrayage anormalement haute ou'
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
    label: Plus de 150 000 km ou
    description: plus de 150 000 km ou conduite urbaine intensive
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km ou'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Kit d'embrayage - Guide Complet

## Fonction

Transmettre le couple moteur à la boîte de vitesses et permettre la séparation temporaire

## Symptômes de défaillance

### Embrayage patine regime monte acceleration

embrayage patine regime monte acceleration

### Odeur brule apres cote demarrage

odeur brule apres cote demarrage

### Pedale d embrayage anormalement haute ou

pedale d embrayage anormalement haute ou basse

### Vibrations ou a-coups au demarrage

vibrations ou a-coups au demarrage

### Difficulte a passer les vitesses craquements

difficulte a passer les vitesses craquements

### Plus de 150 000 km ou

plus de 150 000 km ou conduite urbaine intensive

## Diagnostic

Pour diagnostiquer un problème de kit d'embrayage:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- butee-d-embrayage
- cable-d-embrayage
- emetteur-d-embrayage
- recepteur-d-embrayage
- volant-moteur

## Compatibilité

Pour commander le bon kit d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
