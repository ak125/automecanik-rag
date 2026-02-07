---
entity_type: gamme
title: Courroie d'accessoire
slug: courroie-d-accessoire
pg_id: 10
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Entraîne les accessoires moteur
  must_be_true:
    - entrainer
    - transmettre
  must_not_contain_concepts:
    - freinage
    - climatisation
    - turbo
    - injection
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_sifflement-au-demarrage-ou-a-l
    then: verifier_piece
  - if: symptome_courroie-fissuree-ou-effilochee-visible
    then: diagnostic_approfondi
  - if: symptome_voyant-batterie-allume-alternateur-non-entraine
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Sifflement au demarrage ou a l
    description: sifflement au demarrage ou a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: sifflement au demarrage ou a l'
      - Vérification visuelle ou auditive
  - id: S2
    label: Courroie fissuree ou effilochee visible
    description: courroie fissuree ou effilochee visible
    risk_level: confort
    evidence:
      - 'Observation: courroie fissuree ou effilochee visible'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant batterie allume alternateur non entraine
    description: voyant batterie allume alternateur non entraine
    risk_level: confort
    evidence:
      - 'Observation: voyant batterie allume alternateur non entraine'
      - Vérification visuelle ou auditive
  - id: S4
    label: Perte de direction assistee si sur
    description: perte de direction assistee si sur meme courroie
    risk_level: securite
    evidence:
      - 'Observation: perte de direction assistee si sur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de caoutchouc brule
    description: odeur de caoutchouc brule
    risk_level: confort
    evidence:
      - 'Observation: odeur de caoutchouc brule'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 60 000 km ou
    description: plus de 60 000 km ou 5 ans depuis le remplacement
    risk_level: confort
    evidence:
      - 'Observation: plus de 60 000 km ou'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Courroie d'accessoire - Guide Complet

## Fonction

Entraîne les accessoires moteur

## Symptômes de défaillance

### Sifflement au demarrage ou a l

sifflement au demarrage ou a l acceleration

### Courroie fissuree ou effilochee visible

courroie fissuree ou effilochee visible

### Voyant batterie allume alternateur non entraine

voyant batterie allume alternateur non entraine

### Perte de direction assistee si sur

perte de direction assistee si sur meme courroie

### Odeur de caoutchouc brule

odeur de caoutchouc brule

### Plus de 60 000 km ou

plus de 60 000 km ou 5 ans depuis le remplacement

## Diagnostic

Pour diagnostiquer un problème de courroie d'accessoire:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- alternateur
- compresseur-de-climatisation
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-a-eau

## Compatibilité

Pour commander le bon courroie d'accessoire, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
