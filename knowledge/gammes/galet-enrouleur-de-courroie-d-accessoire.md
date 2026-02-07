---
entity_type: gamme
title: Galet enrouleur de courroie d'accessoire
slug: galet-enrouleur-de-courroie-d-accessoire
pg_id: 312
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Guide la courroie d'accessoire
  must_be_true:
    - guider
    - enrouler
    - maintenir
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
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Courroie d accessoire visiblement usee ou fissuree
    description: courroie d accessoire visiblement usee ou fissuree
    risk_level: confort
    evidence:
      - 'Observation: courroie d accessoire visiblement usee ou fissuree'
      - Vérification visuelle ou auditive
  - id: S2
    label: Sifflement ou grondement au niveau de la courroie
    description: sifflement ou grondement au niveau de la courroie
    risk_level: confort
    evidence:
      - 'Observation: sifflement ou grondement au niveau de la courroie'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perceptible faisant tourner galet main
    description: perceptible faisant tourner galet main
    risk_level: confort
    evidence:
      - 'Observation: perceptible faisant tourner galet main'
      - Vérification visuelle ou auditive
  - id: S4
    label: Perte de tension de la courroie
    description: perte de tension de la courroie
    risk_level: confort
    evidence:
      - 'Observation: perte de tension de la courroie'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de caoutchouc chaud
    description: odeur de caoutchouc chaud
    risk_level: confort
    evidence:
      - 'Observation: odeur de caoutchouc chaud'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 80 000 km depuis le dernier changement
    description: plus de 80 000 km depuis le dernier changement
    risk_level: confort
    evidence:
      - 'Observation: plus de 80 000 km depuis le dernier changement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Galet enrouleur de courroie d'accessoire - Guide Diagnostic Complet

## Fonction et Rôle

Guide la courroie d'accessoire

**Actions principales:** guider, enrouler, maintenir

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- courroie d accessoire visiblement usee ou fissuree
- sifflement ou grondement au niveau de la courroie
- perceptible faisant tourner galet main
- perte de tension de la courroie
- odeur de caoutchouc chaud
- plus de 80 000 km depuis le dernier changement

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet enrouleur de courroie d'accessoire:

1. **Inspection visuelle** - Examiner l'état du galet enrouleur de courroie d'accessoire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-a-eau
- pompe-de-direction-assistee

## Critères de Compatibilité

Pour commander le bon galet enrouleur de courroie d'accessoire, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de durée de vie"
