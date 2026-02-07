---
entity_type: gamme
title: Interrupteur verrouilage des portes
slug: interrupteur-verrouilage-des-portes
pg_id: 864
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Commande le verrouillage/déverrouillage centralisé des portes
  must_be_true:
    - commander
    - activer
    - verrouiller
  must_not_contain_concepts:
    - serrure
    - cle
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
    label: Centralisation qui ne repond plus
    description: centralisation qui ne repond plus
    risk_level: confort
    evidence:
      - 'Observation: centralisation qui ne repond plus'
      - Vérification visuelle ou auditive
  - id: S2
    label: Une porte ne se verrouille pas
    description: une porte ne se verrouille pas
    risk_level: confort
    evidence:
      - 'Observation: une porte ne se verrouille pas'
      - Vérification visuelle ou auditive
  - id: S3
    label: Verrouillage deverrouillage intempestif
    description: verrouillage deverrouillage intempestif
    risk_level: confort
    evidence:
      - 'Observation: verrouillage deverrouillage intempestif'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Interrupteur verrouilage des portes - Guide Diagnostic Complet

## Fonction et Rôle

Commande le verrouillage/déverrouillage centralisé des portes

**Actions principales:** commander, activer, verrouiller

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- centralisation qui ne repond plus
- une porte ne se verrouille pas
- verrouillage deverrouillage intempestif

## Procédure de Diagnostic

Pour diagnostiquer un problème de interrupteur verrouilage des portes:

1. **Inspection visuelle** - Examiner l'état du interrupteur verrouilage des portes
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- serrure
- moteur centralisation

## Critères de Compatibilité

Pour commander le bon interrupteur verrouilage des portes, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"
