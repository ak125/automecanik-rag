---
entity_type: gamme
title: Ampoule feu de recul
slug: ampoule-feu-de-recul
pg_id: 114
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Produit la lumière pour signaler la marche arrière et éclairer derrière le
    véhicule
  must_be_true:
    - produire
    - emettre
    - eclairer
  must_not_contain_concepts:
    - feu complet
    - optique
    - relais
    - commande
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
    label: Feu de recul inactif
    description: feu de recul inactif
    risk_level: confort
    evidence:
      - 'Observation: feu de recul inactif'
      - Vérification visuelle ou auditive
  - id: S2
    label: Camera de recul sans eclairage
    description: camera de recul sans eclairage
    risk_level: confort
    evidence:
      - 'Observation: camera de recul sans eclairage'
      - Vérification visuelle ou auditive
  - id: S3
    label: Stationnement nocturne difficile
    description: stationnement nocturne difficile
    risk_level: confort
    evidence:
      - 'Observation: stationnement nocturne difficile'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Ampoule feu de recul - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour signaler la marche arrière et éclairer derrière le véhicule

**Actions principales:** produire, emettre, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- feu de recul inactif
- camera de recul sans eclairage
- stationnement nocturne difficile

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu de recul:

1. **Inspection visuelle** - Examiner l'état du ampoule feu de recul
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- contacteur-feu-de-recul
- feu-arriere

## Critères de Compatibilité

Pour commander le bon ampoule feu de recul, vous devez connaître:

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
