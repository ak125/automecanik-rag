---
entity_type: gamme
title: Ampoule feu arrière
slug: ampoule-feu-arriere
pg_id: 115
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Produit la lumière pour signaler la présence du véhicule à l'arrière
  must_be_true:
    - produire
    - emettre
    - signaler
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
    label: Feu arriere eteint
    description: feu arriere eteint
    risk_level: confort
    evidence:
      - 'Observation: feu arriere eteint'
      - Vérification visuelle ou auditive
  - id: S2
    label: Clignotant rapide si combine
    description: clignotant rapide si combine
    risk_level: confort
    evidence:
      - 'Observation: clignotant rapide si combine'
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
# Ampoule feu arrière - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour signaler la présence du véhicule à l'arrière

**Actions principales:** produire, emettre, signaler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- feu arriere eteint
- clignotant rapide si combine
- refus au controle technique

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu arrière:

1. **Inspection visuelle** - Examiner l'état du ampoule feu arrière
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-avant
- ampoule-feu-clignotant
- ampoule-feu-de-position
- interrupteur-des-feux-de-freins

## Critères de Compatibilité

Pour commander le bon ampoule feu arrière, vous devez connaître:

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
