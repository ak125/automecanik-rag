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
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Claquement metallique au ralenti a froid
    description: claquement metallique au ralenti a froid
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement metallique au ralenti a froid'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de tac-tac au niveau de la culasse
    description: bruit de tac-tac au niveau de la culasse
    risk_level: confort
    evidence:
      - 'Observation: bruit de tac-tac au niveau de la culasse'
      - Vérification visuelle ou auditive
  - id: S3
    label: Claquement qui persiste meme a chaud
    description: claquement qui persiste meme a chaud
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement qui persiste meme a chaud'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit qui s amplifie avec le regime moteur
    description: bruit qui s amplifie avec le regime moteur
    risk_level: confort
    evidence:
      - 'Observation: bruit qui s amplifie avec le regime moteur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Perte de puissance legere jeu excessif
    description: perte de puissance legere jeu excessif
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance legere jeu excessif'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km et claquement recurrent
    description: plus de 150 000 km et claquement recurrent
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: plus de 150 000 km et claquement recurrent'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Poussoir de soupape - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le mouvement de l'arbre a cames aux soupapes

**Actions principales:** transmettre, actionner, amortir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement metallique au ralenti a froid**
  claquement metallique au ralenti a froid
- **Claquement qui persiste meme a chaud**
  claquement qui persiste meme a chaud
- **Plus de 150 000 km et claquement recurrent**
  plus de 150 000 km et claquement recurrent

### 🟢 Autres Symptômes

- bruit de tac-tac au niveau de la culasse
- bruit qui s amplifie avec le regime moteur
- perte de puissance legere jeu excessif

## Procédure de Diagnostic

Pour diagnostiquer un problème de poussoir de soupape:

1. **Inspection visuelle** - Examiner l'état du poussoir de soupape
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- joint-de-cache-culbuteurs
- joint-de-collecteur
- joint-de-culasse
- soupape-d-admission
- soupape-d-echappement

## Critères de Compatibilité

Pour commander le bon poussoir de soupape, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"
