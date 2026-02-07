---
entity_type: gamme
title: Durite de refroidissement
slug: durite-de-refroidissement
pg_id: 475
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Acheminer le liquide de refroidissement entre les elements du circuit
  must_be_true:
    - acheminer
    - conduire
    - relier
  must_not_contain_concepts:
    - huile
    - carburant
    - frein
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_traces-de-liquide-colore-sous-le
    then: verifier_piece
  - if: symptome_durite-visiblement-gonflee-ou-craquelee
    then: diagnostic_approfondi
  - if: symptome_sifflement-ou-gargouillement-dans-le-circuit
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Traces de liquide colore sous le
    description: traces de liquide colore sous le vehicule
    risk_level: confort
    evidence:
      - 'Observation: traces de liquide colore sous le'
      - Vérification visuelle ou auditive
  - id: S2
    label: Durite visiblement gonflee ou craquelee
    description: durite visiblement gonflee ou craquelee
    risk_level: confort
    evidence:
      - 'Observation: durite visiblement gonflee ou craquelee'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement ou gargouillement dans le circuit
    description: sifflement ou gargouillement dans le circuit
    risk_level: confort
    evidence:
      - 'Observation: sifflement ou gargouillement dans le circuit'
      - Vérification visuelle ou auditive
  - id: S4
    label: Niveau de liquide qui baisse regulierement
    description: niveau de liquide qui baisse regulierement
    risk_level: confort
    evidence:
      - 'Observation: niveau de liquide qui baisse regulierement'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur sucree de liquide de refroidissement
    description: odeur sucree de liquide de refroidissement
    risk_level: confort
    evidence:
      - 'Observation: odeur sucree de liquide de refroidissement'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 100 000 km ou
    description: plus de 100 000 km ou 8 ans sans remplacement
    risk_level: confort
    evidence:
      - 'Observation: plus de 100 000 km ou'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Durite de refroidissement - Guide Complet

## Fonction

Acheminer le liquide de refroidissement entre les elements du circuit

## Symptômes de défaillance

### Traces de liquide colore sous le

traces de liquide colore sous le vehicule

### Durite visiblement gonflee ou craquelee

durite visiblement gonflee ou craquelee

### Sifflement ou gargouillement dans le circuit

sifflement ou gargouillement dans le circuit

### Niveau de liquide qui baisse regulierement

niveau de liquide qui baisse regulierement

### Odeur sucree de liquide de refroidissement

odeur sucree de liquide de refroidissement

### Plus de 100 000 km ou

plus de 100 000 km ou 8 ans sans remplacement

## Diagnostic

Pour diagnostiquer un problème de durite de refroidissement:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- thermostat
- vase-d-expansion

## Compatibilité

Pour commander le bon durite de refroidissement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
