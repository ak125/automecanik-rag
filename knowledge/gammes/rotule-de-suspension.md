---
entity_type: gamme
title: Rotule de suspension
slug: rotule-de-suspension
pg_id: 2462
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
    Articuler le bras de suspension et la fusee - Supporte la charge verticale.
    NE DIRIGE PAS!
  must_be_true:
    - supporter la charge
    - articuler
    - maintenir
  must_not_contain_concepts:
    - direction
    - cremailliere
    - volant
    - braquage
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
    label: Claquements sourds sur dos d ane ou nids de poule
    description: claquements sourds sur dos d ane ou nids de poule
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquements sourds sur dos d ane ou nids de poule'
      - Vérification visuelle ou auditive
  - id: S2
    label: Vehicule qui tire d un cote
    description: vehicule qui tire d un cote
    risk_level: confort
    evidence:
      - 'Observation: vehicule qui tire d un cote'
      - Vérification visuelle ou auditive
  - id: S3
    label: Jeu visible en soulevant la roue a la main
    description: jeu visible en soulevant la roue a la main
    risk_level: confort
    evidence:
      - 'Observation: jeu visible en soulevant la roue a la main'
      - Vérification visuelle ou auditive
  - id: S4
    label: Craquements en braquant a fond
    description: craquements en braquant a fond
    risk_level: confort
    evidence:
      - 'Observation: craquements en braquant a fond'
      - Vérification visuelle ou auditive
  - id: S5
    label: Soufflet de rotule dechire ou absent
    description: soufflet de rotule dechire ou absent
    risk_level: securite
    evidence:
      - 'Observation: soufflet de rotule dechire ou absent'
      - Vérification visuelle ou auditive
  - id: S6
    label: Usure anormale des pneus avant
    description: usure anormale des pneus avant
    risk_level: securite
    evidence:
      - 'Observation: usure anormale des pneus avant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Rotule de suspension - Guide Diagnostic Complet

## Fonction et Rôle

Articuler le bras de suspension et la fusee - Supporte la charge verticale. NE DIRIGE PAS!

**Actions principales:** supporter la charge, articuler, maintenir, pivoter, supporter le poids

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements sourds sur dos d ane ou nids de poule**
  claquements sourds sur dos d ane ou nids de poule

### 🟡 Symptômes de Sécurité

- **Soufflet de rotule dechire ou absent**
  soufflet de rotule dechire ou absent
- **Usure anormale des pneus avant**
  usure anormale des pneus avant

### 🟢 Autres Symptômes

- vehicule qui tire d un cote
- jeu visible en soulevant la roue a la main
- craquements en braquant a fond

## Procédure de Diagnostic

Pour diagnostiquer un problème de rotule de suspension:

1. **Inspection visuelle** - Examiner l'état du rotule de suspension
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- amortisseur
- barre-stabilisatrice
- bras-de-suspension
- ressort-de-suspension
- rotule-de-direction

## Critères de Compatibilité

Pour commander le bon rotule de suspension, vous devez connaître:

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
