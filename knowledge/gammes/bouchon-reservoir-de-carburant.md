---
entity_type: gamme
title: Bouchon réservoir de carburant
slug: bouchon-reservoir-de-carburant
pg_id: 602
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Ferme hermétiquement le réservoir de carburant
  must_be_true:
    - fermer
    - etancheifier
    - proteger
  must_not_contain_concepts:
    - pompe
    - injection
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
    label: Odeur de carburant persistante
    description: odeur de carburant persistante
    risk_level: confort
    evidence:
      - 'Observation: odeur de carburant persistante'
      - Vérification visuelle ou auditive
  - id: S2
    label: Voyant defaut evaporation allume
    description: voyant defaut evaporation allume
    risk_level: confort
    evidence:
      - 'Observation: voyant defaut evaporation allume'
      - Vérification visuelle ou auditive
  - id: S3
    label: Difficultes a refermer le bouchon
    description: difficultes a refermer le bouchon
    risk_level: confort
    evidence:
      - 'Observation: difficultes a refermer le bouchon'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bouchon réservoir de carburant - Guide Diagnostic Complet

## Fonction et Rôle

Ferme hermétiquement le réservoir de carburant

**Actions principales:** fermer, etancheifier, proteger

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- odeur de carburant persistante
- voyant defaut evaporation allume
- difficultes a refermer le bouchon

## Procédure de Diagnostic

Pour diagnostiquer un problème de bouchon réservoir de carburant:

1. **Inspection visuelle** - Examiner l'état du bouchon réservoir de carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- reservoir
- trappe

## Critères de Compatibilité

Pour commander le bon bouchon réservoir de carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "economie carburant"
