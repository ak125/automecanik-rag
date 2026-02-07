---
entity_type: gamme
title: Soupape d'échappement
slug: soupape-d-echappement
pg_id: 1270
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Ouvrir et fermer le passage des gaz d'echappement
  must_be_true:
    - ouvrir
    - fermer
    - evacuer
  must_not_contain_concepts:
    - admission
    - air frais
    - carburant
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_perte-de-compression-sur-un-cylindre
    then: verifier_piece
  - if: symptome_surchauffe-localisee-du-moteur
    then: diagnostic_approfondi
  - if: symptome_claquement-ou-rate-d-allumage
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Perte de compression sur un cylindre
    description: perte de compression sur un cylindre
    risk_level: confort
    evidence:
      - 'Observation: perte de compression sur un cylindre'
      - Vérification visuelle ou auditive
  - id: S2
    label: Surchauffe localisee du moteur
    description: surchauffe localisee du moteur
    risk_level: confort
    evidence:
      - 'Observation: surchauffe localisee du moteur'
      - Vérification visuelle ou auditive
  - id: S3
    label: Claquement ou rate d allumage
    description: claquement ou rate d allumage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement ou rate d allumage'
      - Vérification visuelle ou auditive
  - id: S4
    label: Soupape grillee ou deformee endoscopie
    description: soupape grillee ou deformee endoscopie
    risk_level: confort
    evidence:
      - 'Observation: soupape grillee ou deformee endoscopie'
      - Vérification visuelle ou auditive
  - id: S5
    label: Perte de puissance notable
    description: perte de puissance notable
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance notable'
      - Vérification visuelle ou auditive
  - id: S6
    label: Refection culasse prevue remplacement preventif
    description: refection culasse prevue remplacement preventif
    risk_level: confort
    evidence:
      - 'Observation: refection culasse prevue remplacement preventif'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Soupape d'échappement - Guide Complet

## Fonction

Ouvrir et fermer le passage des gaz d'echappement

## Symptômes de défaillance

### Perte de compression sur un cylindre

perte de compression sur un cylindre

### Surchauffe localisee du moteur

surchauffe localisee du moteur

### Claquement ou rate d allumage

claquement ou rate d allumage

### Soupape grillee ou deformee endoscopie

soupape grillee ou deformee endoscopie

### Perte de puissance notable

perte de puissance notable

### Refection culasse prevue remplacement preventif

refection culasse prevue remplacement preventif

## Diagnostic

Pour diagnostiquer un problème de soupape d'échappement:

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

Pour commander le bon soupape d'échappement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
