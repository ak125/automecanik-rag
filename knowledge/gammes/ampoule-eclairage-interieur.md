---
entity_type: gamme
title: Ampoule éclairage intérieur
slug: ampoule-eclairage-interieur
pg_id: 117
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Produit la lumière pour éclairer l'intérieur de l'habitacle
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
    label: Plafonnier qui ne s allume plus
    description: plafonnier qui ne s allume plus
    risk_level: confort
    evidence:
      - 'Observation: plafonnier qui ne s allume plus'
      - Vérification visuelle ou auditive
  - id: S2
    label: Lumiere qui clignote ou vacille
    description: lumiere qui clignote ou vacille
    risk_level: confort
    evidence:
      - 'Observation: lumiere qui clignote ou vacille'
      - Vérification visuelle ou auditive
  - id: S3
    label: Eclairage tres faible
    description: eclairage tres faible
    risk_level: confort
    evidence:
      - 'Observation: eclairage tres faible'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Ampoule éclairage intérieur - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour éclairer l'intérieur de l'habitacle

**Actions principales:** produire, emettre, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- plafonnier qui ne s allume plus
- lumiere qui clignote ou vacille
- eclairage tres faible

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule éclairage intérieur:

1. **Inspection visuelle** - Examiner l'état du ampoule éclairage intérieur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- plafonnier
- interrupteur-eclairage

## Critères de Compatibilité

Pour commander le bon ampoule éclairage intérieur, vous devez connaître:

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
