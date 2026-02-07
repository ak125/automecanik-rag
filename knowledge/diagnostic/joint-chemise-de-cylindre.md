---
entity_type: gamme
title: Joint chemise de cylindre
slug: joint-chemise-de-cylindre
pg_id: 128
category: moteur
subcategory: joints
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Assurer l'etancheite entre la chemise et le bloc moteur
  must_be_true:
    - assurer l'etancheite
    - isoler
  must_not_contain_concepts:
    - freinage
    - climatisation
    - direction
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_melange-eau-huile-mayonnaise
    then: verifier_piece
  - if: symptome_surchauffe-moteur-sans-fuite-visible
    then: diagnostic_approfondi
  - if: symptome_perte-de-compression-sur-un-cylindre
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Melange eau-huile mayonnaise
    description: melange eau-huile mayonnaise
    risk_level: confort
    evidence:
      - 'Observation: melange eau-huile mayonnaise'
      - Vérification visuelle ou auditive
  - id: S2
    label: Surchauffe moteur sans fuite visible
    description: surchauffe moteur sans fuite visible
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: surchauffe moteur sans fuite visible'
      - Vérification visuelle ou auditive
  - id: S3
    label: Perte de compression sur un cylindre
    description: perte de compression sur un cylindre
    risk_level: confort
    evidence:
      - 'Observation: perte de compression sur un cylindre'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Joint chemise de cylindre - Guide Complet

## Fonction

Assurer l'etancheite entre la chemise et le bloc moteur

## Symptômes de défaillance

### Melange eau-huile mayonnaise

melange eau-huile mayonnaise

### Surchauffe moteur sans fuite visible

surchauffe moteur sans fuite visible

### Perte de compression sur un cylindre

perte de compression sur un cylindre

## Diagnostic

Pour diagnostiquer un problème de joint chemise de cylindre:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- chemise-de-cylindre
- joint-de-culasse

## Compatibilité

Pour commander le bon joint chemise de cylindre, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
