---
entity_type: gamme
title: Soufflet de direction
slug: soufflet-de-direction
pg_id: 191
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Proteger la cremailliere des impuretes et retenir la graisse - Piece d'usure
    a verifier regulierement
  must_be_true:
    - proteger
    - etancher
    - retenir
  must_not_contain_concepts:
    - suspension
    - amortisseur
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Soufflet visiblement fissure ou dechire
    description: soufflet visiblement fissure ou dechire
    risk_level: confort
    evidence:
      - 'Observation: soufflet visiblement fissure ou dechire'
      - Vérification visuelle ou auditive
  - id: S2
    label: Graisse noire qui s echappe du soufflet
    description: graisse noire qui s echappe du soufflet
    risk_level: confort
    evidence:
      - 'Observation: graisse noire qui s echappe du soufflet'
      - Vérification visuelle ou auditive
  - id: S3
    label: Controle technique refuse pour soufflet defectueux
    description: controle technique refuse pour soufflet defectueux
    risk_level: confort
    evidence:
      - 'Observation: controle technique refuse pour soufflet defectueux'
      - Vérification visuelle ou auditive
  - id: S4
    label: Claquements dans la direction rotule exposee
    description: claquements dans la direction rotule exposee
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements dans la direction rotule exposee'
      - Vérification visuelle ou auditive
  - id: S5
    label: Traces graisse jante passage roue
    description: traces graisse jante passage roue
    risk_level: confort
    evidence:
      - 'Observation: traces graisse jante passage roue'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 100 000 km sans verification
    description: plus de 100 000 km sans verification
    risk_level: confort
    evidence:
      - 'Observation: plus de 100 000 km sans verification'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Soufflet de direction - Guide Diagnostic Complet

## Fonction et Rôle

Proteger la cremailliere des impuretes et retenir la graisse - Piece d'usure a verifier regulierement

**Actions principales:** proteger, etancher, retenir, preserver

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements dans la direction rotule exposee**
  claquements dans la direction rotule exposee

### 🟢 Autres Symptômes

- soufflet visiblement fissure ou dechire
- graisse noire qui s echappe du soufflet
- controle technique refuse pour soufflet defectueux
- traces graisse jante passage roue
- plus de 100 000 km sans verification

## Procédure de Diagnostic

Pour diagnostiquer un problème de soufflet de direction:

1. **Inspection visuelle** - Examiner l'état du soufflet de direction
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- barre-de-direction
- cremailliere-de-direction
- rotule-de-direction

## Critères de Compatibilité

Pour commander le bon soufflet de direction, vous devez connaître:

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
