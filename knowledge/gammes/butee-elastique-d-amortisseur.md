---
entity_type: gamme
title: Butée élastique d'amortisseur
slug: butee-elastique-d-amortisseur
pg_id: 1182
category: suspension
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Limiter la course de l'amortisseur en fin de detente
  must_be_true:
    - absorber
    - limiter
    - amortir
  must_not_contain_concepts:
    - injection
    - freinage
    - climatisation
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
    label: Bruit sourd de talonnement sur gros nids-de-poule
    description: bruit sourd de talonnement sur gros nids-de-poule
    risk_level: confort
    evidence:
      - 'Observation: bruit sourd de talonnement sur gros nids-de-poule'
      - Vérification visuelle ou auditive
  - id: S2
    label: Butee visible fissuree ou ecrasee
    description: butee visible fissuree ou ecrasee
    risk_level: confort
    evidence:
      - 'Observation: butee visible fissuree ou ecrasee'
      - Vérification visuelle ou auditive
  - id: S3
    label: Amortisseur qui tape en fin de course
    description: amortisseur qui tape en fin de course
    risk_level: confort
    evidence:
      - 'Observation: amortisseur qui tape en fin de course'
      - Vérification visuelle ou auditive
  - id: S4
    label: Sensation rebonds amortis grosses bosses
    description: sensation rebonds amortis grosses bosses
    risk_level: confort
    evidence:
      - 'Observation: sensation rebonds amortis grosses bosses'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de caoutchouc chaud si butee frotte
    description: odeur de caoutchouc chaud si butee frotte
    risk_level: confort
    evidence:
      - 'Observation: odeur de caoutchouc chaud si butee frotte'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 80 000 km ou changement amortisseurs prevu
    description: plus de 80 000 km ou changement amortisseurs prevu
    risk_level: confort
    evidence:
      - 'Observation: plus de 80 000 km ou changement amortisseurs prevu'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Butée élastique d'amortisseur - Guide Diagnostic Complet

## Fonction et Rôle

Limiter la course de l'amortisseur en fin de detente

**Actions principales:** absorber, limiter, amortir

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- bruit sourd de talonnement sur gros nids-de-poule
- butee visible fissuree ou ecrasee
- amortisseur qui tape en fin de course
- sensation rebonds amortis grosses bosses
- odeur de caoutchouc chaud si butee frotte
- plus de 80 000 km ou changement amortisseurs prevu

## Procédure de Diagnostic

Pour diagnostiquer un problème de butée élastique d'amortisseur:

1. **Inspection visuelle** - Examiner l'état du butée élastique d'amortisseur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- amortisseur
- kit-de-butee-de-suspension
- ressort-de-suspension

## Critères de Compatibilité

Pour commander le bon butée élastique d'amortisseur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "confort parfait"
