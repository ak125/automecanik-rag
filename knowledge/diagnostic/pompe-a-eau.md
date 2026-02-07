---
entity_type: gamme
title: Pompe à eau
slug: pompe-a-eau
pg_id: 1260
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Faire circuler le liquide de refroidissement dans le circuit moteur
  must_be_true:
    - faire circuler
    - pomper
    - alimenter
  must_not_contain_concepts:
    - huile
    - carburant
    - direction
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_fuite-de-liquide-au-niveau-de
    then: verifier_piece
  - if: symptome_bruit-de-roulement-cote-distribution
    then: diagnostic_approfondi
  - if: symptome_jeu-perceptible-dans-la-poulie-de
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Fuite de liquide au niveau de
    description: fuite de liquide au niveau de la pompe
    risk_level: confort
    evidence:
      - 'Observation: fuite de liquide au niveau de'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de roulement cote distribution
    description: bruit de roulement cote distribution
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement cote distribution'
      - Vérification visuelle ou auditive
  - id: S3
    label: Jeu perceptible dans la poulie de
    description: jeu perceptible dans la poulie de pompe
    risk_level: confort
    evidence:
      - 'Observation: jeu perceptible dans la poulie de'
      - Vérification visuelle ou auditive
  - id: S4
    label: Surchauffe moteur malgre niveau correct
    description: surchauffe moteur malgre niveau correct
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: surchauffe moteur malgre niveau correct'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de liquide de refroidissement chaud
    description: odeur de liquide de refroidissement chaud
    risk_level: confort
    evidence:
      - 'Observation: odeur de liquide de refroidissement chaud'
      - Vérification visuelle ou auditive
  - id: S6
    label: Echeance distribution approche preventif
    description: echeance distribution approche preventif
    risk_level: confort
    evidence:
      - 'Observation: echeance distribution approche preventif'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe à eau - Guide Complet

## Fonction

Faire circuler le liquide de refroidissement dans le circuit moteur

## Symptômes de défaillance

### Fuite de liquide au niveau de

fuite de liquide au niveau de la pompe

### Bruit de roulement cote distribution

bruit de roulement cote distribution

### Jeu perceptible dans la poulie de

jeu perceptible dans la poulie de pompe

### Surchauffe moteur malgre niveau correct

surchauffe moteur malgre niveau correct

### Odeur de liquide de refroidissement chaud

odeur de liquide de refroidissement chaud

### Echeance distribution approche preventif

echeance distribution approche preventif

## Diagnostic

Pour diagnostiquer un problème de pompe à eau:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- chaine-de-distribution
- courroie-d-accessoire
- courroie-de-distribution
- durite-de-refroidissement
- kit-de-chaine-de-distribution

## Compatibilité

Pour commander le bon pompe à eau, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
