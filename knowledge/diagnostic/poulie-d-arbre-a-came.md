---
entity_type: gamme
title: Poulie d'arbre à came
slug: poulie-d-arbre-a-came
pg_id: 1067
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Entrainer l'arbre a cames en synchronisation avec le vilebrequin
  must_be_true:
    - entrainer
    - synchroniser
    - transmettre
  must_not_contain_concepts:
    - vilebrequin
    - accessoire
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_bruit-de-claquement-au-niveau-de
    then: verifier_piece
  - if: symptome_perte-de-puissance-progressive
    then: diagnostic_approfondi
  - if: symptome_moteur-qui-cale-au-ralenti
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Bruit de claquement au niveau de
    description: bruit de claquement au niveau de la culasse
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de claquement au niveau de'
      - Vérification visuelle ou auditive
  - id: S2
    label: Perte de puissance progressive
    description: perte de puissance progressive
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance progressive'
      - Vérification visuelle ou auditive
  - id: S3
    label: Moteur qui cale au ralenti
    description: moteur qui cale au ralenti
    risk_level: immobilisation
    evidence:
      - 'Observation: moteur qui cale au ralenti'
      - Vérification visuelle ou auditive
  - id: S4
    label: Fumee anormale a l echappement
    description: fumee anormale a l echappement
    risk_level: confort
    evidence:
      - 'Observation: fumee anormale a l echappement'
      - Vérification visuelle ou auditive
  - id: S5
    label: Voyant moteur allume codes calage
    description: voyant moteur allume codes calage
    risk_level: immobilisation
    evidence:
      - 'Observation: voyant moteur allume codes calage'
      - Vérification visuelle ou auditive
  - id: S6
    label: Distribution a remplacer selon carnet d
    description: distribution a remplacer selon carnet d entretien
    risk_level: confort
    evidence:
      - 'Observation: distribution a remplacer selon carnet d'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Poulie d'arbre à came - Guide Complet

## Fonction

Entrainer l'arbre a cames en synchronisation avec le vilebrequin

## Symptômes de défaillance

### Bruit de claquement au niveau de

bruit de claquement au niveau de la culasse

### Perte de puissance progressive

perte de puissance progressive

### Moteur qui cale au ralenti

moteur qui cale au ralenti

### Fumee anormale a l echappement

fumee anormale a l echappement

### Voyant moteur allume codes calage

voyant moteur allume codes calage

### Distribution a remplacer selon carnet d

distribution a remplacer selon carnet d entretien

## Diagnostic

Pour diagnostiquer un problème de poulie d'arbre à came:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- arbre-a-came
- capteur-impulsion
- chaine-de-distribution
- courroie-de-distribution
- kit-de-chaine-de-distribution

## Compatibilité

Pour commander le bon poulie d'arbre à came, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
