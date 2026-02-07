---
entity_type: gamme
title: Commande d'éclairage
slug: commande-d-eclairage
pg_id: 809
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Commande les différents feux du véhicule
  must_be_true:
    - commander
    - activer
    - regler
  must_not_contain_concepts:
    - injection
    - freinage
    - embrayage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: vehicule_immobilise_ou_symptome_critique
    then: verification_urgente_piece_et_alimentation
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
symptoms:
  - id: S1
    label: Feux croisement route allument plus
    description: feux croisement route allument plus
    risk_level: confort
    evidence:
      - 'Observation: feux croisement route allument plus'
      - Vérification visuelle ou auditive
  - id: S2
    label: Commodo bloque ou difficile a tourner
    description: commodo bloque ou difficile a tourner
    risk_level: immobilisation
    evidence:
      - 'Observation: commodo bloque ou difficile a tourner'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fonctions aleatoires s allument puis s eteignent
    description: fonctions aleatoires s allument puis s eteignent
    risk_level: confort
    evidence:
      - 'Observation: fonctions aleatoires s allument puis s eteignent'
      - Vérification visuelle ou auditive
  - id: S4
    label: Clignotants fonctionnent plus depuis commodo
    description: clignotants fonctionnent plus depuis commodo
    risk_level: confort
    evidence:
      - 'Observation: clignotants fonctionnent plus depuis commodo'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruit de craquement en actionnant l interrupteur
    description: bruit de craquement en actionnant l interrupteur
    risk_level: confort
    evidence:
      - 'Observation: bruit de craquement en actionnant l interrupteur'
      - Vérification visuelle ou auditive
  - id: S6
    label: Fusibles ok mais feux inoperants
    description: fusibles ok mais feux inoperants
    risk_level: confort
    evidence:
      - 'Observation: fusibles ok mais feux inoperants'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Commande d'éclairage - Guide Diagnostic Complet

## Fonction et Rôle

Commande les différents feux du véhicule

**Actions principales:** commander, activer, regler

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Commodo bloque ou difficile a tourner**
  commodo bloque ou difficile a tourner

### 🟢 Autres Symptômes

- feux croisement route allument plus
- fonctions aleatoires s allument puis s eteignent
- clignotants fonctionnent plus depuis commodo
- bruit de craquement en actionnant l interrupteur
- fusibles ok mais feux inoperants

## Procédure de Diagnostic

Pour diagnostiquer un problème de commande d'éclairage:

1. **Inspection visuelle** - Examiner l'état du commande d'éclairage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le commande d'éclairage peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-d-essuie-glace
- feu-arriere
- feu-avant
- feu-clignotant

## Critères de Compatibilité

Pour commander le bon commande d'éclairage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur éclairage"
