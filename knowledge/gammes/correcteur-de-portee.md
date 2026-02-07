---
entity_type: gamme
title: Correcteur de portée
slug: correcteur-de-portee
pg_id: 700
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Règle la hauteur du faisceau lumineux en fonction de la charge du véhicule
  must_be_true:
    - regler
    - ajuster
    - adapter
  must_not_contain_concepts:
    - ampoule
    - feu
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
    label: Phares mal orientés
    description: phares mal orientés
    risk_level: confort
    evidence:
      - 'Observation: phares mal orientés'
      - Vérification visuelle ou auditive
  - id: S2
    label: Eblouissement
    description: eblouissement
    risk_level: confort
    evidence:
      - 'Observation: eblouissement'
      - Vérification visuelle ou auditive
  - id: S3
    label: Reglage impossible
    description: reglage impossible
    risk_level: confort
    evidence:
      - 'Observation: reglage impossible'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Correcteur de portée - Guide Diagnostic Complet

## Fonction et Rôle

Règle la hauteur du faisceau lumineux en fonction de la charge du véhicule

**Actions principales:** regler, ajuster, adapter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- phares mal orientés
- eblouissement
- reglage impossible

## Procédure de Diagnostic

Pour diagnostiquer un problème de correcteur de portée:

1. **Inspection visuelle** - Examiner l'état du correcteur de portée
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- feu-avant
- commande-correcteur-de-portee

## Critères de Compatibilité

Pour commander le bon correcteur de portée, vous devez connaître:

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
