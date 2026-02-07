---
entity_type: gamme
title: Mécatronique boîte automatique
slug: mecatronique-boite-automatique
pg_id: 3072
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Piloter electroniquement les passages de vitesses
  must_be_true:
    - piloter
    - commander
    - controler
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
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Passages de rapports brutaux
    description: passages de rapports brutaux
    risk_level: confort
    evidence:
      - 'Observation: passages de rapports brutaux'
      - Vérification visuelle ou auditive
  - id: S2
    label: Boite en mode degrade
    description: boite en mode degrade
    risk_level: confort
    evidence:
      - 'Observation: boite en mode degrade'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant boite de vitesses allume
    description: voyant boite de vitesses allume
    risk_level: confort
    evidence:
      - 'Observation: voyant boite de vitesses allume'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Mécatronique boîte automatique - Guide Diagnostic Complet

## Fonction et Rôle

Piloter electroniquement les passages de vitesses

**Actions principales:** piloter, commander, controler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- passages de rapports brutaux
- boite en mode degrade
- voyant boite de vitesses allume

## Procédure de Diagnostic

Pour diagnostiquer un problème de mécatronique boîte automatique:

1. **Inspection visuelle** - Examiner l'état du mécatronique boîte automatique
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- boite-automatique
- calculateur-bva

## Critères de Compatibilité

Pour commander le bon mécatronique boîte automatique, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"
