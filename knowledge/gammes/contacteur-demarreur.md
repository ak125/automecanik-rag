---
entity_type: gamme
title: Contacteur démarreur
slug: contacteur-demarreur
pg_id: 682
category: electrique
subcategory: demarrage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Commuter le circuit electrique du demarreur
  must_be_true:
    - commuter
    - activer
    - alimenter
  must_not_contain_concepts:
    - injection
    - climatisation
    - freinage
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
    label: Aucune reaction a la cle de contact
    description: aucune reaction a la cle de contact
    risk_level: confort
    evidence:
      - 'Observation: aucune reaction a la cle de contact'
      - Vérification visuelle ou auditive
  - id: S2
    label: Demarrage intermittent
    description: demarrage intermittent
    risk_level: confort
    evidence:
      - 'Observation: demarrage intermittent'
      - Vérification visuelle ou auditive
  - id: S3
    label: Tableau de bord qui ne s allume pas
    description: tableau de bord qui ne s allume pas
    risk_level: confort
    evidence:
      - 'Observation: tableau de bord qui ne s allume pas'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Contacteur démarreur - Guide Diagnostic Complet

## Fonction et Rôle

Commuter le circuit electrique du demarreur

**Actions principales:** commuter, activer, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- aucune reaction a la cle de contact
- demarrage intermittent
- tableau de bord qui ne s allume pas

## Procédure de Diagnostic

Pour diagnostiquer un problème de contacteur démarreur:

1. **Inspection visuelle** - Examiner l'état du contacteur démarreur
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- demarreur
- batterie

## Critères de Compatibilité

Pour commander le bon contacteur démarreur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "demarrage garanti"
