---
entity_type: gamme
title: Relais de clignotant
slug: relais-de-clignotant
pg_id: 61
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Commande le clignotement intermittent des feux de direction
  must_be_true:
    - commander
    - activer
    - cadencer
  must_not_contain_concepts:
    - ampoule
    - feu
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_general_detecte
    then: inspection_visuelle_et_test_fonctionnel
symptoms:
  - id: S1
    label: Clignotants ne fonctionnent pas
    description: clignotants ne fonctionnent pas
    risk_level: confort
    evidence:
      - 'Observation: clignotants ne fonctionnent pas'
      - Vérification visuelle ou auditive
  - id: S2
    label: Clignotement trop rapide
    description: clignotement trop rapide
    risk_level: confort
    evidence:
      - 'Observation: clignotement trop rapide'
      - Vérification visuelle ou auditive
  - id: S3
    label: Clignotement irregulier
    description: clignotement irregulier
    risk_level: confort
    evidence:
      - 'Observation: clignotement irregulier'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Relais de clignotant - Guide Diagnostic Complet

## Fonction et Rôle

Commande le clignotement intermittent des feux de direction

**Actions principales:** commander, activer, cadencer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- clignotants ne fonctionnent pas
- clignotement trop rapide
- clignotement irregulier

## Procédure de Diagnostic

Pour diagnostiquer un problème de relais de clignotant:

1. **Inspection visuelle** - Examiner l'état du relais de clignotant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- feu-clignotant
- ampoule-feu-clignotant

## Critères de Compatibilité

Pour commander le bon relais de clignotant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"
