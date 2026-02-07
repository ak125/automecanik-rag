---
entity_type: gamme
title: Soupape d'admission
slug: soupape-d-admission
pg_id: 1269
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Ouvrir et fermer le passage des gaz d'admission
  must_be_true:
    - ouvrir
    - fermer
    - admettre
  must_not_contain_concepts:
    - echappement
    - carburant
    - injection
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_perte-de-compression-sur-un-ou
    then: verifier_piece
  - if: symptome_rates-d-allumage-persistants
    then: diagnostic_approfondi
  - if: symptome_claquement-au-niveau-de-la-culasse
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Perte de compression sur un ou
    description: perte de compression sur un ou plusieurs cylindres
    risk_level: confort
    evidence:
      - 'Observation: perte de compression sur un ou'
      - Vérification visuelle ou auditive
  - id: S2
    label: Rates d allumage persistants
    description: rates d allumage persistants
    risk_level: confort
    evidence:
      - 'Observation: rates d allumage persistants'
      - Vérification visuelle ou auditive
  - id: S3
    label: Claquement au niveau de la culasse
    description: claquement au niveau de la culasse
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement au niveau de la culasse'
      - Vérification visuelle ou auditive
  - id: S4
    label: Consommation d huile anormale guides uses
    description: consommation d huile anormale guides uses
    risk_level: confort
    evidence:
      - 'Observation: consommation d huile anormale guides uses'
      - Vérification visuelle ou auditive
  - id: S5
    label: Fumee bleue a l echappement
    description: fumee bleue a l echappement
    risk_level: confort
    evidence:
      - 'Observation: fumee bleue a l echappement'
      - Vérification visuelle ou auditive
  - id: S6
    label: Casse de courroie de distribution controle
    description: casse de courroie de distribution controle
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: casse de courroie de distribution controle'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Soupape d'admission - Guide Complet

## Fonction

Ouvrir et fermer le passage des gaz d'admission

## Symptômes de défaillance

### Perte de compression sur un ou

perte de compression sur un ou plusieurs cylindres

### Rates d allumage persistants

rates d allumage persistants

### Claquement au niveau de la culasse

claquement au niveau de la culasse

### Consommation d huile anormale guides uses

consommation d huile anormale guides uses

### Fumee bleue a l echappement

fumee bleue a l echappement

### Casse de courroie de distribution controle

casse de courroie de distribution controle

## Diagnostic

Pour diagnostiquer un problème de soupape d'admission:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- bagues-d-etancheite-moteur
- joint-de-cache-culbuteurs
- joint-de-collecteur
- joint-de-culasse
- poulie-d-arbre-a-came

## Compatibilité

Pour commander le bon soupape d'admission, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
