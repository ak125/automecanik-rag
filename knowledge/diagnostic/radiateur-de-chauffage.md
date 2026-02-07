---
entity_type: gamme
title: Radiateur de chauffage
slug: radiateur-de-chauffage
pg_id: 467
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Transferer la chaleur du liquide de refroidissement vers l'habitacle pour le
    confort des passagers. NE REFROIDIT PAS LE MOTEUR!
  must_be_true:
    - chauffer
    - transferer
    - diffuser
  must_not_contain_concepts:
    - refroidissement moteur
    - ventilateur moteur
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_buee-grasse-persistante-sur-le-pare-brise
    then: verifier_piece
  - if: symptome_odeur-sucree-de-liquide-dans-l
    then: diagnostic_approfondi
  - if: symptome_moquette-humide-cote-passager-avant
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Buee grasse persistante sur le pare-brise
    description: buee grasse persistante sur le pare-brise
    risk_level: confort
    evidence:
      - 'Observation: buee grasse persistante sur le pare-brise'
      - Vérification visuelle ou auditive
  - id: S2
    label: Odeur sucree de liquide dans l
    description: odeur sucree de liquide dans l habitacle
    risk_level: confort
    evidence:
      - 'Observation: odeur sucree de liquide dans l'
      - Vérification visuelle ou auditive
  - id: S3
    label: Moquette humide cote passager avant
    description: moquette humide cote passager avant
    risk_level: confort
    evidence:
      - 'Observation: moquette humide cote passager avant'
      - Vérification visuelle ou auditive
  - id: S4
    label: Chauffage qui ne chauffe plus ou
    description: chauffage qui ne chauffe plus ou peu
    risk_level: confort
    evidence:
      - 'Observation: chauffage qui ne chauffe plus ou'
      - Vérification visuelle ou auditive
  - id: S5
    label: Gargouillement dans le tableau de bord
    description: gargouillement dans le tableau de bord
    risk_level: confort
    evidence:
      - 'Observation: gargouillement dans le tableau de bord'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 15 ans ou fuite
    description: plus de 15 ans ou fuite averee
    risk_level: confort
    evidence:
      - 'Observation: plus de 15 ans ou fuite'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Radiateur de chauffage - Guide Complet

## Fonction

Transferer la chaleur du liquide de refroidissement vers l'habitacle pour le confort des passagers. NE REFROIDIT PAS LE MOTEUR!

## Symptômes de défaillance

### Buee grasse persistante sur le pare-brise

buee grasse persistante sur le pare-brise

### Odeur sucree de liquide dans l

odeur sucree de liquide dans l habitacle

### Moquette humide cote passager avant

moquette humide cote passager avant

### Chauffage qui ne chauffe plus ou

chauffage qui ne chauffe plus ou peu

### Gargouillement dans le tableau de bord

gargouillement dans le tableau de bord

### Plus de 15 ans ou fuite

plus de 15 ans ou fuite averee

## Diagnostic

Pour diagnostiquer un problème de radiateur de chauffage:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- commande-de-ventilation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle
- radiateur-de-refroidissement

## Compatibilité

Pour commander le bon radiateur de chauffage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
