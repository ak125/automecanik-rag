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
  - if: vehicule_immobilise_ou_symptome_critique
    then: verification_urgente_piece_et_alimentation
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Roues arriere qui bloquent trop tot au freinage
    description: roues arriere qui bloquent trop tot au freinage
    risk_level: immobilisation
    evidence:
      - 'Observation: roues arriere qui bloquent trop tot au freinage'
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
# Répartiteur de frein - Guide Diagnostic Complet

## Fonction et Rôle

Repartir la pression de freinage entre les essieux

**Actions principales:** repartir, distribuer, equilibrer

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Roues arriere qui bloquent trop tot au freinage**
  roues arriere qui bloquent trop tot au freinage

### 🟡 Symptômes de Sécurité

- **Freinage desequilibre avant arriere**
  freinage desequilibre avant arriere
- **Desequilibre freinage controle technique valeurs**
  desequilibre freinage controle technique valeurs

### 🟢 Autres Symptômes

- fuite au niveau du repartiteur
- echec au controle technique desequilibre

## Procédure de Diagnostic

Pour diagnostiquer un problème de répartiteur de frein:

1. **Inspection visuelle** - Examiner l'état du répartiteur de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits

## Causes Probables

- **Pièce HS** - Le répartiteur de frein peut être hors service et nécessiter un remplacement
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- maitre-cylindre-de-frein
- flexible-de-frein

## Critères de Compatibilité

Pour commander le bon répartiteur de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage garanti"
