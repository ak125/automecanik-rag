---
entity_type: gamme
title: Pompe nettoyage des phares
slug: pompe-nettoyage-des-phares
pg_id: 795
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Projette le liquide de nettoyage sur les optiques de phares
  must_be_true:
    - projeter
    - pulveriser
    - alimenter
  must_not_contain_concepts:
    - balai
    - essuie-glace
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
symptoms:
  - id: S1
    label: Jets de phares inactifs
    description: jets de phares inactifs
    risk_level: confort
    evidence:
      - 'Observation: jets de phares inactifs'
      - Vérification visuelle ou auditive
  - id: S2
    label: Phares sales malgre l activation
    description: phares sales malgre l activation
    risk_level: confort
    evidence:
      - 'Observation: phares sales malgre l activation'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de pompe sans projection
    description: bruit de pompe sans projection
    risk_level: confort
    evidence:
      - 'Observation: bruit de pompe sans projection'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe nettoyage des phares - Guide Diagnostic Complet

## Fonction et Rôle

Projette le liquide de nettoyage sur les optiques de phares

**Actions principales:** projeter, pulveriser, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- jets de phares inactifs
- phares sales malgre l activation
- bruit de pompe sans projection

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe nettoyage des phares:

1. **Inspection visuelle** - Examiner l'état du pompe nettoyage des phares
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- gicleur
- phare

## Critères de Compatibilité

Pour commander le bon pompe nettoyage des phares, vous devez connaître:

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
