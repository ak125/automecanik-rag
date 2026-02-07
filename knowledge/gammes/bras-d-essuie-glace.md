---
entity_type: gamme
title: Bras d'essuie-glace
slug: bras-d-essuie-glace
pg_id: 301
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Supporte et maintient le balai contre le pare-brise
  must_be_true:
    - supporter
    - maintenir
    - plaquer
  must_not_contain_concepts:
    - caoutchouc
    - lame
    - capteur abs
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
    label: Balai qui ne touche plus le pare-brise
    description: balai qui ne touche plus le pare-brise
    risk_level: confort
    evidence:
      - 'Observation: balai qui ne touche plus le pare-brise'
      - Vérification visuelle ou auditive
  - id: S2
    label: Traces ou zones non balayees
    description: traces ou zones non balayees
    risk_level: confort
    evidence:
      - 'Observation: traces ou zones non balayees'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bras tordu ou rouille
    description: bras tordu ou rouille
    risk_level: confort
    evidence:
      - 'Observation: bras tordu ou rouille'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bras d'essuie-glace - Guide Diagnostic Complet

## Fonction et Rôle

Supporte et maintient le balai contre le pare-brise

**Actions principales:** supporter, maintenir, plaquer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- balai qui ne touche plus le pare-brise
- traces ou zones non balayees
- bras tordu ou rouille

## Procédure de Diagnostic

Pour diagnostiquer un problème de bras d'essuie-glace:

1. **Inspection visuelle** - Examiner l'état du bras d'essuie-glace
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-d-essuie-glace
- moteur-d-essuie-glace
- pompe-nettoyage-des-vitres

## Critères de Compatibilité

Pour commander le bon bras d'essuie-glace, vous devez connaître:

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
