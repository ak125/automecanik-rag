---
entity_type: gamme
title: Ventilateur de refroidissement
slug: ventilateur-de-refroidissement
pg_id: 508
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
    Forcer le passage de l'air a travers le radiateur quand le vehicule est a
    l'arret ou a faible vitesse
  must_be_true:
    - forcer
    - ventiler
    - refroidir
  must_not_contain_concepts:
    - pulseur
    - habitacle
    - chauffage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_surchauffe-uniquement-au-ralenti-ou-en
    then: verifier_piece
  - if: symptome_ventilateur-qui-ne-demarre-jamais-silence
    then: diagnostic_approfondi
  - if: symptome_bruit-de-roulement-ou-grincement-au
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Surchauffe uniquement au ralenti ou en
    description: surchauffe uniquement au ralenti ou en ville
    risk_level: confort
    evidence:
      - 'Observation: surchauffe uniquement au ralenti ou en'
      - Vérification visuelle ou auditive
  - id: S2
    label: Ventilateur qui ne demarre jamais silence
    description: ventilateur qui ne demarre jamais silence
    risk_level: confort
    evidence:
      - 'Observation: ventilateur qui ne demarre jamais silence'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de roulement ou grincement au
    description: bruit de roulement ou grincement au demarrage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de roulement ou grincement au'
      - Vérification visuelle ou auditive
  - id: S4
    label: Pales de ventilateur fissurees ou cassees
    description: pales de ventilateur fissurees ou cassees
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: pales de ventilateur fissurees ou cassees'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de plastique chaud pres du
    description: odeur de plastique chaud pres du radiateur
    risk_level: confort
    evidence:
      - 'Observation: odeur de plastique chaud pres du'
      - Vérification visuelle ou auditive
  - id: S6
    label: Clim moins efficace ventilateur partage
    description: clim moins efficace ventilateur partage
    risk_level: confort
    evidence:
      - 'Observation: clim moins efficace ventilateur partage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Ventilateur de refroidissement - Guide Complet

## Fonction

Forcer le passage de l'air a travers le radiateur quand le vehicule est a l'arret ou a faible vitesse

## Symptômes de défaillance

### Surchauffe uniquement au ralenti ou en

surchauffe uniquement au ralenti ou en ville

### Ventilateur qui ne demarre jamais silence

ventilateur qui ne demarre jamais silence

### Bruit de roulement ou grincement au

bruit de roulement ou grincement au demarrage

### Pales de ventilateur fissurees ou cassees

pales de ventilateur fissurees ou cassees

### Odeur de plastique chaud pres du

odeur de plastique chaud pres du radiateur

### Clim moins efficace ventilateur partage

clim moins efficace ventilateur partage

## Diagnostic

Pour diagnostiquer un problème de ventilateur de refroidissement:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- vase-d-expansion

## Compatibilité

Pour commander le bon ventilateur de refroidissement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
