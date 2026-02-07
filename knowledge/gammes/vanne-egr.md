---
entity_type: gamme
title: Vanne EGR
slug: vanne-egr
pg_id: 1145
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Recycler une partie des gaz d'echappement vers l'admission pour reduire les
    emissions de NOx
  must_be_true:
    - recycler
    - ouvrir
    - fermer
  must_not_contain_concepts:
    - carburant
    - injection
    - injecteur
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Perte de puissance a bas et moyen regime
    description: perte de puissance a bas et moyen regime
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance a bas et moyen regime'
      - Vérification visuelle ou auditive
  - id: S2
    label: Fumee noire a l acceleration
    description: fumee noire a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: fumee noire a l acceleration'
      - Vérification visuelle ou auditive
  - id: S3
    label: Ralenti irregulier ou moteur qui broute
    description: ralenti irregulier ou moteur qui broute
    risk_level: confort
    evidence:
      - 'Observation: ralenti irregulier ou moteur qui broute'
      - Vérification visuelle ou auditive
  - id: S4
    label: Voyant moteur allume codes p0400-p0409
    description: voyant moteur allume codes p0400-p0409
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur allume codes p0400-p0409'
      - Vérification visuelle ou auditive
  - id: S5
    label: A-coups a bas regime
    description: a-coups a bas regime
    risk_level: confort
    evidence:
      - 'Observation: a-coups a bas regime'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 80 000 km sans nettoyage diesel
    description: plus de 80 000 km sans nettoyage diesel
    risk_level: confort
    evidence:
      - 'Observation: plus de 80 000 km sans nettoyage diesel'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Vanne EGR - Guide Diagnostic Complet

## Fonction et Rôle

Recycler une partie des gaz d'echappement vers l'admission pour reduire les emissions de NOx

**Actions principales:** recycler, ouvrir, fermer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- perte de puissance a bas et moyen regime
- fumee noire a l acceleration
- ralenti irregulier ou moteur qui broute
- voyant moteur allume codes p0400-p0409
- a-coups a bas regime
- plus de 80 000 km sans nettoyage diesel

## Procédure de Diagnostic

Pour diagnostiquer un problème de vanne egr:

1. **Inspection visuelle** - Examiner l'état du vanne egr
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- catalyseur
- fap
- injecteur
- turbo

## Critères de Compatibilité

Pour commander le bon vanne egr, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "nettoie le moteur"
