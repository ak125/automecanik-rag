---
entity_type: gamme
title: Capteur de pluie
slug: capteur-de-pluie
pg_id: 2275
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Détecte la présence d'eau sur le pare-brise pour activer automatiquement les
    essuie-glaces
  must_be_true:
    - detecter
    - mesurer
    - analyser
  must_not_contain_concepts:
    - balai
    - moteur essuie-glace
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
    label: Essuie-glaces declenches sans pluie
    description: essuie-glaces declenches sans pluie
    risk_level: confort
    evidence:
      - 'Observation: essuie-glaces declenches sans pluie'
      - Vérification visuelle ou auditive
  - id: S2
    label: Essuie-glaces automatiques inactifs
    description: essuie-glaces automatiques inactifs
    risk_level: confort
    evidence:
      - 'Observation: essuie-glaces automatiques inactifs'
      - Vérification visuelle ou auditive
  - id: S3
    label: Vitesse d essuyage inadaptee a l intensite
    description: vitesse d essuyage inadaptee a l intensite
    risk_level: confort
    evidence:
      - 'Observation: vitesse d essuyage inadaptee a l intensite'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Capteur de pluie - Guide Diagnostic Complet

## Fonction et Rôle

Détecte la présence d'eau sur le pare-brise pour activer automatiquement les essuie-glaces

**Actions principales:** detecter, mesurer, analyser

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- essuie-glaces declenches sans pluie
- essuie-glaces automatiques inactifs
- vitesse d essuyage inadaptee a l intensite

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur de pluie:

1. **Inspection visuelle** - Examiner l'état du capteur de pluie
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- moteur-d-essuie-glace
- commande-essuie-glace
- balai-d-essuie-glace

## Critères de Compatibilité

Pour commander le bon capteur de pluie, vous devez connaître:

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
