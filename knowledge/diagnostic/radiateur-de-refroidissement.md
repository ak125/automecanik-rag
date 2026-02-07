---
entity_type: gamme
title: Radiateur de refroidissement
slug: radiateur-de-refroidissement
pg_id: 470
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Dissiper la chaleur du liquide de refroidissement vers l'air exterieur
  must_be_true:
    - dissiper
    - echanger
    - refroidir
  must_not_contain_concepts:
    - chauffage
    - habitacle
    - huile
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_flaque-de-liquide-colore-sous-l
    then: verifier_piece
  - if: symptome_traces-de-corrosion-sur-les-tubes
    then: diagnostic_approfondi
  - if: symptome_sifflement-d-air-ou-de-vapeur
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Flaque de liquide colore sous l
    description: flaque de liquide colore sous l avant
    risk_level: confort
    evidence:
      - 'Observation: flaque de liquide colore sous l'
      - Vérification visuelle ou auditive
  - id: S2
    label: Traces de corrosion sur les tubes
    description: traces de corrosion sur les tubes du radiateur
    risk_level: confort
    evidence:
      - 'Observation: traces de corrosion sur les tubes'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement d air ou de vapeur
    description: sifflement d air ou de vapeur a l avant
    risk_level: confort
    evidence:
      - 'Observation: sifflement d air ou de vapeur'
      - Vérification visuelle ou auditive
  - id: S4
    label: Surchauffe au ralenti ou en embouteillage
    description: surchauffe au ralenti ou en embouteillage
    risk_level: confort
    evidence:
      - 'Observation: surchauffe au ralenti ou en embouteillage'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de liquide de refroidissement chaud
    description: odeur de liquide de refroidissement chaud
    risk_level: confort
    evidence:
      - 'Observation: odeur de liquide de refroidissement chaud'
      - Vérification visuelle ou auditive
  - id: S6
    label: Radiateur visiblement deforme ou perce
    description: radiateur visiblement deforme ou perce
    risk_level: confort
    evidence:
      - 'Observation: radiateur visiblement deforme ou perce'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Radiateur de refroidissement - Guide Complet

## Fonction

Dissiper la chaleur du liquide de refroidissement vers l'air exterieur

## Symptômes de défaillance

### Flaque de liquide colore sous l

flaque de liquide colore sous l avant

### Traces de corrosion sur les tubes

traces de corrosion sur les tubes du radiateur

### Sifflement d air ou de vapeur

sifflement d air ou de vapeur a l avant

### Surchauffe au ralenti ou en embouteillage

surchauffe au ralenti ou en embouteillage

### Odeur de liquide de refroidissement chaud

odeur de liquide de refroidissement chaud

### Radiateur visiblement deforme ou perce

radiateur visiblement deforme ou perce

## Diagnostic

Pour diagnostiquer un problème de radiateur de refroidissement:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- bouchon-de-radiateur
- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-chauffage
- sonde-de-refroidissement

## Compatibilité

Pour commander le bon radiateur de refroidissement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
