---
entity_type: gamme
title: Pompe à huile
slug: pompe-a-huile
pg_id: 596
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Alimenter le circuit de lubrification en huile sous pression
  must_be_true:
    - alimenter
    - pressuriser
    - distribuer
  must_not_contain_concepts:
    - freinage
    - climatisation
    - direction
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_voyant-huile-allume-moteur-chaud
    then: verifier_piece
  - if: symptome_pression-d-huile-insuffisante
    then: diagnostic_approfondi
  - if: symptome_bruit-de-cliquetis-moteur
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Voyant huile allume moteur chaud
    description: voyant huile allume moteur chaud
    risk_level: confort
    evidence:
      - 'Observation: voyant huile allume moteur chaud'
      - Vérification visuelle ou auditive
  - id: S2
    label: Pression d huile insuffisante
    description: pression d huile insuffisante
    risk_level: confort
    evidence:
      - 'Observation: pression d huile insuffisante'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de cliquetis moteur
    description: bruit de cliquetis moteur
    risk_level: confort
    evidence:
      - 'Observation: bruit de cliquetis moteur'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe à huile - Guide Complet

## Fonction

Alimenter le circuit de lubrification en huile sous pression

## Symptômes de défaillance

### Voyant huile allume moteur chaud

voyant huile allume moteur chaud

### Pression d huile insuffisante

pression d huile insuffisante

### Bruit de cliquetis moteur

bruit de cliquetis moteur

## Diagnostic

Pour diagnostiquer un problème de pompe à huile:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- bagues-d-etancheite-moteur
- capteur-niveau-d-huile-moteur
- capteur-pression-et-temperature-d-huile
- carter-d-huile
- pressostat-d-huile

## Compatibilité

Pour commander le bon pompe à huile, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
