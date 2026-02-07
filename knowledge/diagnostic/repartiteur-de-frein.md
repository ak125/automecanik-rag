---
entity_type: gamme
title: Répartiteur de frein
slug: repartiteur-de-frein
pg_id: 73
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Repartir la pression de freinage entre les essieux
  must_be_true:
    - repartir
    - distribuer
    - equilibrer
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
  - if: symptome_roues-arriere-qui-bloquent-trop-tot
    then: verifier_piece
  - if: symptome_freinage-desequilibre-avant-arriere
    then: diagnostic_approfondi
  - if: symptome_fuite-au-niveau-du-repartiteur
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Roues arriere qui bloquent trop tot
    description: roues arriere qui bloquent trop tot au freinage
    risk_level: immobilisation
    evidence:
      - 'Observation: roues arriere qui bloquent trop tot'
      - Vérification visuelle ou auditive
  - id: S2
    label: Freinage desequilibre avant arriere
    description: freinage desequilibre avant arriere
    risk_level: securite
    evidence:
      - 'Observation: freinage desequilibre avant arriere'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fuite au niveau du repartiteur
    description: fuite au niveau du repartiteur
    risk_level: confort
    evidence:
      - 'Observation: fuite au niveau du repartiteur'
      - Vérification visuelle ou auditive
  - id: S4
    label: Echec au controle technique desequilibre
    description: echec au controle technique desequilibre
    risk_level: confort
    evidence:
      - 'Observation: echec au controle technique desequilibre'
      - Vérification visuelle ou auditive
  - id: S5
    label: Desequilibre freinage controle technique valeurs
    description: desequilibre freinage controle technique valeurs
    risk_level: securite
    evidence:
      - 'Observation: desequilibre freinage controle technique valeurs'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Répartiteur de frein - Guide Complet

## Fonction

Repartir la pression de freinage entre les essieux

## Symptômes de défaillance

### Roues arriere qui bloquent trop tot

roues arriere qui bloquent trop tot au freinage

### Freinage desequilibre avant arriere

freinage desequilibre avant arriere

### Fuite au niveau du repartiteur

fuite au niveau du repartiteur

### Echec au controle technique desequilibre

echec au controle technique desequilibre

### Desequilibre freinage controle technique valeurs

desequilibre freinage controle technique valeurs

## Diagnostic

Pour diagnostiquer un problème de répartiteur de frein:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- maitre-cylindre-de-frein
- flexible-de-frein

## Compatibilité

Pour commander le bon répartiteur de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
