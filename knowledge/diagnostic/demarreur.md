---
entity_type: gamme
title: Démarreur
slug: demarreur
pg_id: 2
category: electrique
subcategory: demarrage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Appliquer une rotation initiale au moteur pour declencher le demarrage
  must_be_true:
    - lancer le moteur
    - entrainer
    - demarrer
  must_not_contain_concepts:
    - charge
    - recharge
    - alimentation electrique
    - alternateur
    - universel
    - tous modèles
    - adaptable tous
  confusion_with:
    alternateur:
      key_difference: >-
        Démarreur = lance le moteur (au démarrage), Alternateur = recharge
        batterie (moteur tournant)
    batterie:
      key_difference: >-
        Batterie faible peut simuler un démarreur HS - toujours tester la
        batterie d'abord
diagnostic_tree:
  - if: symptome_claquement-contact-demarrage-solenoide
    then: verifier_piece
  - if: symptome_demarreur-tourne-mais-moteur-lance
    then: diagnostic_approfondi
  - if: symptome_aucune-reaction-au-contact-moteur-electrique
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Claquement contact demarrage solenoide
    description: claquement contact demarrage solenoide
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement contact demarrage solenoide'
      - Vérification visuelle ou auditive
  - id: S2
    label: Demarreur tourne mais moteur lance
    description: demarreur tourne mais moteur lance
    risk_level: confort
    evidence:
      - 'Observation: demarreur tourne mais moteur lance'
      - Vérification visuelle ou auditive
  - id: S3
    label: Aucune reaction au contact moteur electrique
    description: aucune reaction au contact moteur electrique hs
    risk_level: immobilisation
    evidence:
      - 'Observation: aucune reaction au contact moteur electrique'
      - Vérification visuelle ou auditive
  - id: S4
    label: Grincement ou bruit anormal au demarrage
    description: grincement ou bruit anormal au demarrage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: grincement ou bruit anormal au demarrage'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de brule electrique au demarrage
    description: odeur de brule electrique au demarrage
    risk_level: confort
    evidence:
      - 'Observation: odeur de brule electrique au demarrage'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus demarrages difficiles recurrents
    description: plus demarrages difficiles recurrents
    risk_level: confort
    evidence:
      - 'Observation: plus demarrages difficiles recurrents'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - adaptable tous
---
# Démarreur - Guide Complet

## Fonction

Appliquer une rotation initiale au moteur pour declencher le demarrage

## Symptômes de défaillance

### Claquement contact demarrage solenoide

claquement contact demarrage solenoide

### Demarreur tourne mais moteur lance

demarreur tourne mais moteur lance

### Aucune reaction au contact moteur electrique

aucune reaction au contact moteur electrique hs

### Grincement ou bruit anormal au demarrage

grincement ou bruit anormal au demarrage

### Odeur de brule electrique au demarrage

odeur de brule electrique au demarrage

### Plus demarrages difficiles recurrents

plus demarrages difficiles recurrents

## Diagnostic

Pour diagnostiquer un problème de démarreur:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- neiman
- contacteur-demarreur

## Ne pas confondre avec

| Pièce confondue | Distinction |
|-----------------|-------------|
| alternateur | Démarreur = lance le moteur (au démarrage), Alternateur = recharge batterie (moteur tournant) |
| batterie | Batterie faible peut simuler un démarreur HS - toujours tester la batterie d'abord |

## Compatibilité

Pour commander le bon démarreur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "démarrage garanti"
- ❌ "homologué CT"
- ❌ "sécurité garantie"
