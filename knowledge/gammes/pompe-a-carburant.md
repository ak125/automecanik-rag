---
entity_type: gamme
title: Pompe à carburant
slug: pompe-a-carburant
pg_id: 458
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Acheminer le carburant du reservoir vers le systeme d'injection a basse
    pression
  must_be_true:
    - alimenter
    - acheminer
    - pomper
  must_not_contain_concepts:
    - haute pression
    - injection
    - injecteur
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
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Moteur qui refuse de demarrer pas d amorcage
    description: moteur qui refuse de demarrer pas d amorcage
    risk_level: confort
    evidence:
      - 'Observation: moteur qui refuse de demarrer pas d amorcage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Calages repetes a chaud ou en cote
    description: calages repetes a chaud ou en cote
    risk_level: immobilisation
    evidence:
      - 'Observation: calages repetes a chaud ou en cote'
      - Vérification visuelle ou auditive
  - id: S3
    label: A-coups a l acceleration
    description: a-coups a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: a-coups a l acceleration'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit de gemissement dans le reservoir
    description: bruit de gemissement dans le reservoir
    risk_level: confort
    evidence:
      - 'Observation: bruit de gemissement dans le reservoir'
      - Vérification visuelle ou auditive
  - id: S5
    label: Perte de puissance en montee
    description: perte de puissance en montee
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance en montee'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 200 000 km ou reservoir souvent vide
    description: plus de 200 000 km ou reservoir souvent vide
    risk_level: confort
    evidence:
      - 'Observation: plus de 200 000 km ou reservoir souvent vide'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe à carburant - Guide Diagnostic Complet

## Fonction et Rôle

Acheminer le carburant du reservoir vers le systeme d'injection a basse pression

**Actions principales:** alimenter, acheminer, pomper

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Calages repetes a chaud ou en cote**
  calages repetes a chaud ou en cote

### 🟢 Autres Symptômes

- moteur qui refuse de demarrer pas d amorcage
- a-coups a l acceleration
- bruit de gemissement dans le reservoir
- perte de puissance en montee
- plus de 200 000 km ou reservoir souvent vide

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à carburant:

1. **Inspection visuelle** - Examiner l'état du pompe à carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le pompe à carburant peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-pression-de-carburant
- filtre-a-carburant
- injecteur

## Critères de Compatibilité

Pour commander le bon pompe à carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"
