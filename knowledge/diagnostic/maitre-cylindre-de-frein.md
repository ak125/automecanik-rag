---
entity_type: gamme
title: Maître cylindre de frein
slug: maitre-cylindre-de-frein
pg_id: 258
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transformer l'action de la pedale en pression hydraulique
  must_be_true:
    - generer la pression
    - alimenter le circuit
    - commander le freinage
  must_not_contain_concepts:
    - friction
    - thermique
    - ABS
    - electronique
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_pedale-de-frein-qui-s-enfonce
    then: verifier_piece
  - if: symptome_niveau-liquide-baisse-fuite-visible
    then: diagnostic_approfondi
  - if: symptome_pedale-de-frein-molle-malgre-une
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Pedale de frein qui s enfonce
    description: pedale de frein qui s enfonce lentement a l arret
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein qui s enfonce'
      - Vérification visuelle ou auditive
  - id: S2
    label: Niveau liquide baisse fuite visible
    description: niveau liquide baisse fuite visible
    risk_level: confort
    evidence:
      - 'Observation: niveau liquide baisse fuite visible'
      - Vérification visuelle ou auditive
  - id: S3
    label: Pedale de frein molle malgre une
    description: pedale de frein molle malgre une purge recente
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein molle malgre une'
      - Vérification visuelle ou auditive
  - id: S4
    label: Liquide de frein qui fuit dans
    description: liquide de frein qui fuit dans l habitacle servo
    risk_level: securite
    evidence:
      - 'Observation: liquide de frein qui fuit dans'
      - Vérification visuelle ou auditive
  - id: S5
    label: Perte de freinage progressive sur un
    description: perte de freinage progressive sur un circuit
    risk_level: securite
    evidence:
      - 'Observation: perte de freinage progressive sur un'
      - Vérification visuelle ou auditive
  - id: S6
    label: Voyant niveau liquide de frein allume
    description: voyant niveau liquide de frein allume
    risk_level: securite
    evidence:
      - 'Observation: voyant niveau liquide de frein allume'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Maître cylindre de frein - Guide Complet

## Fonction

Transformer l'action de la pedale en pression hydraulique

## Symptômes de défaillance

### Pedale de frein qui s enfonce

pedale de frein qui s enfonce lentement a l arret

### Niveau liquide baisse fuite visible

niveau liquide baisse fuite visible

### Pedale de frein molle malgre une

pedale de frein molle malgre une purge recente

### Liquide de frein qui fuit dans

liquide de frein qui fuit dans l habitacle servo

### Perte de freinage progressive sur un

perte de freinage progressive sur un circuit

### Voyant niveau liquide de frein allume

voyant niveau liquide de frein allume

## Diagnostic

Pour diagnostiquer un problème de maître cylindre de frein:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- agregat-de-freinage
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein

## Compatibilité

Pour commander le bon maître cylindre de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
