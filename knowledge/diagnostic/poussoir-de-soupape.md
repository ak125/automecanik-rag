---
entity_type: gamme
title: Poussoir de soupape
slug: poussoir-de-soupape
pg_id: 1216
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmettre le mouvement de l'arbre a cames aux soupapes
  must_be_true:
    - transmettre
    - actionner
    - amortir
  must_not_contain_concepts:
    - culbuteur
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_claquement-metallique-au-ralenti-a-froid
    then: verifier_piece
  - if: symptome_bruit-de-tac-tac-au-niveau-de
    then: diagnostic_approfondi
  - if: symptome_claquement-qui-persiste-meme-a-chaud
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Claquement metallique au ralenti a froid
    description: claquement metallique au ralenti a froid
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement metallique au ralenti a froid'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de tac-tac au niveau de
    description: bruit de tac-tac au niveau de la culasse
    risk_level: confort
    evidence:
      - 'Observation: bruit de tac-tac au niveau de'
      - Vérification visuelle ou auditive
  - id: S3
    label: Claquement qui persiste meme a chaud
    description: claquement qui persiste meme a chaud
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement qui persiste meme a chaud'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit qui s amplifie avec le
    description: bruit qui s amplifie avec le regime moteur
    risk_level: confort
    evidence:
      - 'Observation: bruit qui s amplifie avec le'
      - Vérification visuelle ou auditive
  - id: S5
    label: Perte de puissance legere jeu excessif
    description: perte de puissance legere jeu excessif
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance legere jeu excessif'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km et
    description: plus de 150 000 km et claquement recurrent
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: plus de 150 000 km et'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Poussoir de soupape - Guide Complet

## Fonction

Transmettre le mouvement de l'arbre a cames aux soupapes

## Symptômes de défaillance

### Claquement metallique au ralenti a froid

claquement metallique au ralenti a froid

### Bruit de tac-tac au niveau de

bruit de tac-tac au niveau de la culasse

### Claquement qui persiste meme a chaud

claquement qui persiste meme a chaud

### Bruit qui s amplifie avec le

bruit qui s amplifie avec le regime moteur

### Perte de puissance legere jeu excessif

perte de puissance legere jeu excessif

### Plus de 150 000 km et

plus de 150 000 km et claquement recurrent

## Diagnostic

Pour diagnostiquer un problème de poussoir de soupape:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- joint-de-cache-culbuteurs
- joint-de-collecteur
- joint-de-culasse
- soupape-d-admission
- soupape-d-echappement

## Compatibilité

Pour commander le bon poussoir de soupape, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
