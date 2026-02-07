---
entity_type: gamme
title: Câble de frein à main
slug: cable-de-frein-a-main
pg_id: 124
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmet la commande du frein de stationnement
  must_be_true:
    - transmettre
    - actionner
    - maintenir
  must_not_contain_concepts:
    - injection
    - climatisation
    - embrayage
    - distribution
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_frein-a-main-qui-ne-tient
    then: verifier_piece
  - if: symptome_course-du-levier-excessive-plus-de
    then: diagnostic_approfondi
  - if: symptome_vehicule-roule-alors-frein-main
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Frein a main qui ne tient
    description: frein a main qui ne tient plus en cote
    risk_level: securite
    evidence:
      - 'Observation: frein a main qui ne tient'
      - Vérification visuelle ou auditive
  - id: S2
    label: Course du levier excessive plus de
    description: course du levier excessive plus de 7 clics
    risk_level: confort
    evidence:
      - 'Observation: course du levier excessive plus de'
      - Vérification visuelle ou auditive
  - id: S3
    label: Vehicule roule alors frein main
    description: vehicule roule alors frein main
    risk_level: securite
    evidence:
      - 'Observation: vehicule roule alors frein main'
      - Vérification visuelle ou auditive
  - id: S4
    label: Cable visible effiloche ou rouille
    description: cable visible effiloche ou rouille
    risk_level: confort
    evidence:
      - 'Observation: cable visible effiloche ou rouille'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruit de frottement a l arriere
    description: bruit de frottement a l arriere en roulant
    risk_level: confort
    evidence:
      - 'Observation: bruit de frottement a l arriere'
      - Vérification visuelle ou auditive
  - id: S6
    label: Levier de frein a main mou
    description: levier de frein a main mou ou sans resistance
    risk_level: securite
    evidence:
      - 'Observation: levier de frein a main mou'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Câble de frein à main - Guide Complet

## Fonction

Transmet la commande du frein de stationnement

## Symptômes de défaillance

### Frein a main qui ne tient

frein a main qui ne tient plus en cote

### Course du levier excessive plus de

course du levier excessive plus de 7 clics

### Vehicule roule alors frein main

vehicule roule alors frein main

### Cable visible effiloche ou rouille

cable visible effiloche ou rouille

### Bruit de frottement a l arriere

bruit de frottement a l arriere en roulant

### Levier de frein a main mou

levier de frein a main mou ou sans resistance

## Diagnostic

Pour diagnostiquer un problème de câble de frein à main:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- capteur-abs
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere

## Compatibilité

Pour commander le bon câble de frein à main, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
