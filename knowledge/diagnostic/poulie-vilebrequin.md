---
entity_type: gamme
title: Poulie vilebrequin
slug: poulie-vilebrequin
pg_id: 3213
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmet le mouvement du vilebrequin aux accessoires
  must_be_true:
    - entrainer
    - transmettre
    - amortir
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
  - if: symptome_vibrations-moteur-importantes-au-ralenti
    then: verifier_piece
  - if: symptome_caoutchouc-de-la-poulie-fissure-ou
    then: diagnostic_approfondi
  - if: symptome_courroie-d-accessoire-qui-deraille
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Vibrations moteur importantes au ralenti
    description: vibrations moteur importantes au ralenti
    risk_level: confort
    evidence:
      - 'Observation: vibrations moteur importantes au ralenti'
      - Vérification visuelle ou auditive
  - id: S2
    label: Caoutchouc de la poulie fissure ou
    description: caoutchouc de la poulie fissure ou decolle
    risk_level: confort
    evidence:
      - 'Observation: caoutchouc de la poulie fissure ou'
      - Vérification visuelle ou auditive
  - id: S3
    label: Courroie d accessoire qui deraille
    description: courroie d accessoire qui deraille
    risk_level: confort
    evidence:
      - 'Observation: courroie d accessoire qui deraille'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit sourd au niveau du bas
    description: bruit sourd au niveau du bas moteur
    risk_level: confort
    evidence:
      - 'Observation: bruit sourd au niveau du bas'
      - Vérification visuelle ou auditive
  - id: S5
    label: Reperes de calage impossibles a aligner
    description: reperes de calage impossibles a aligner
    risk_level: immobilisation
    evidence:
      - 'Observation: reperes de calage impossibles a aligner'
      - Vérification visuelle ou auditive
  - id: S6
    label: Voyant moteur codes vibrations vilebrequin
    description: voyant moteur codes vibrations vilebrequin
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur codes vibrations vilebrequin'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Poulie vilebrequin - Guide Complet

## Fonction

Transmet le mouvement du vilebrequin aux accessoires

## Symptômes de défaillance

### Vibrations moteur importantes au ralenti

vibrations moteur importantes au ralenti

### Caoutchouc de la poulie fissure ou

caoutchouc de la poulie fissure ou decolle

### Courroie d accessoire qui deraille

courroie d accessoire qui deraille

### Bruit sourd au niveau du bas

bruit sourd au niveau du bas moteur

### Reperes de calage impossibles a aligner

reperes de calage impossibles a aligner

### Voyant moteur codes vibrations vilebrequin

voyant moteur codes vibrations vilebrequin

## Diagnostic

Pour diagnostiquer un problème de poulie vilebrequin:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- alternateur
- capteur-impulsion
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire

## Compatibilité

Pour commander le bon poulie vilebrequin, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
