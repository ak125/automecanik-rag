---
entity_type: gamme
title: Ampoule feu éclaireur de plaque
slug: ampoule-feu-eclaireur-de-plaque
pg_id: 112
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Produit la lumière pour éclairer la plaque d'immatriculation
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
    label: Plaque d immatriculation non eclairee
    description: plaque d immatriculation non eclairee
    risk_level: confort
    evidence:
      - 'Observation: plaque d immatriculation non eclairee'
      - Vérification visuelle ou auditive
  - id: S2
    label: Eclairage faible ou clignotant
    description: eclairage faible ou clignotant
    risk_level: confort
    evidence:
      - 'Observation: eclairage faible ou clignotant'
      - Vérification visuelle ou auditive
  - id: S3
    label: Refus au controle technique
    description: refus au controle technique
    risk_level: confort
    evidence:
      - 'Observation: refus au controle technique'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Ampoule feu éclaireur de plaque - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour éclairer la plaque d'immatriculation

**Actions principales:** produire, emettre, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- plaque d immatriculation non eclairee
- eclairage faible ou clignotant
- refus au controle technique

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu éclaireur de plaque:

1. **Inspection visuelle** - Examiner l'état du ampoule feu éclaireur de plaque
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- feu-arriere
- ampoule-feu-arriere

## Critères de Compatibilité

Pour commander le bon ampoule feu éclaireur de plaque, vous devez connaître:

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
