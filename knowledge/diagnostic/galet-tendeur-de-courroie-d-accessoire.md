---
entity_type: gamme
title: Galet tendeur de courroie d'accessoire
slug: galet-tendeur-de-courroie-d-accessoire
pg_id: 310
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Maintient la tension de la courroie d'accessoire
  must_be_true:
    - tendre
    - maintenir
    - guider
  must_not_contain_concepts:
    - freinage
    - climatisation
    - turbo
    - injection
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_sifflement-de-la-courroie
    then: verifier_piece
  - if: symptome_bruit-de-roulement-cote-accessoires
    then: diagnostic_approfondi
  - if: symptome_courroie-qui-patine-temoin-batterie
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Sifflement de la courroie
    description: sifflement de la courroie
    risk_level: confort
    evidence:
      - 'Observation: sifflement de la courroie'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de roulement cote accessoires
    description: bruit de roulement cote accessoires
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement cote accessoires'
      - Vérification visuelle ou auditive
  - id: S3
    label: Courroie qui patine temoin batterie
    description: courroie qui patine temoin batterie
    risk_level: confort
    evidence:
      - 'Observation: courroie qui patine temoin batterie'
      - Vérification visuelle ou auditive
  - id: S4
    label: Galet qui ne bouge plus tendeur
    description: galet qui ne bouge plus tendeur bloque
    risk_level: immobilisation
    evidence:
      - 'Observation: galet qui ne bouge plus tendeur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Vibrations dans le moteur
    description: vibrations dans le moteur
    risk_level: confort
    evidence:
      - 'Observation: vibrations dans le moteur'
      - Vérification visuelle ou auditive
  - id: S6
    label: Bruit de claquement courroie detendue
    description: bruit de claquement courroie detendue
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de claquement courroie detendue'
      - Vérification visuelle ou auditive
  - id: S7
    label: Courroie qui saute de son logement
    description: courroie qui saute de son logement
    risk_level: confort
    evidence:
      - 'Observation: courroie qui saute de son logement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Galet tendeur de courroie d'accessoire - Guide Complet

## Fonction

Maintient la tension de la courroie d'accessoire

## Symptômes de défaillance

### Sifflement de la courroie

sifflement de la courroie

### Bruit de roulement cote accessoires

bruit de roulement cote accessoires

### Courroie qui patine temoin batterie

courroie qui patine temoin batterie

### Galet qui ne bouge plus tendeur

galet qui ne bouge plus tendeur bloque

### Vibrations dans le moteur

vibrations dans le moteur

### Bruit de claquement courroie detendue

bruit de claquement courroie detendue

### Courroie qui saute de son logement

courroie qui saute de son logement

## Diagnostic

Pour diagnostiquer un problème de galet tendeur de courroie d'accessoire:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- alternateur
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- pompe-de-direction-assistee

## Compatibilité

Pour commander le bon galet tendeur de courroie d'accessoire, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
