---
entity_type: gamme
title: Galet tendeur de courroie de distribution
slug: galet-tendeur-de-courroie-de-distribution
pg_id: 308
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Maintenir la tension de la courroie de distribution
  must_be_true:
    - tendre
    - maintenir
    - ajuster
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
  - if: symptome_sifflement-ou-couinement-cote-distribution
    then: verifier_piece
  - if: symptome_bruit-de-roulement-au-ralenti
    then: diagnostic_approfondi
  - if: symptome_jeu-excessif-dans-le-galet-controle
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Sifflement ou couinement cote distribution
    description: sifflement ou couinement cote distribution
    risk_level: confort
    evidence:
      - 'Observation: sifflement ou couinement cote distribution'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de roulement au ralenti
    description: bruit de roulement au ralenti
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement au ralenti'
      - Vérification visuelle ou auditive
  - id: S3
    label: Jeu excessif dans le galet controle
    description: jeu excessif dans le galet controle main
    risk_level: confort
    evidence:
      - 'Observation: jeu excessif dans le galet controle'
      - Vérification visuelle ou auditive
  - id: S4
    label: Traces de rouille sur le galet
    description: traces de rouille sur le galet
    risk_level: confort
    evidence:
      - 'Observation: traces de rouille sur le galet'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruit qui varie avec le regime
    description: bruit qui varie avec le regime moteur
    risk_level: confort
    evidence:
      - 'Observation: bruit qui varie avec le regime'
      - Vérification visuelle ou auditive
  - id: S6
    label: Grincement au demarrage a froid
    description: grincement au demarrage a froid
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: grincement au demarrage a froid'
      - Vérification visuelle ou auditive
  - id: S7
    label: Courroie qui saute cas extreme
    description: courroie qui saute cas extreme
    risk_level: confort
    evidence:
      - 'Observation: courroie qui saute cas extreme'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Galet tendeur de courroie de distribution - Guide Complet

## Fonction

Maintenir la tension de la courroie de distribution

## Symptômes de défaillance

### Sifflement ou couinement cote distribution

sifflement ou couinement cote distribution

### Bruit de roulement au ralenti

bruit de roulement au ralenti

### Jeu excessif dans le galet controle

jeu excessif dans le galet controle main

### Traces de rouille sur le galet

traces de rouille sur le galet

### Bruit qui varie avec le regime

bruit qui varie avec le regime moteur

### Grincement au demarrage a froid

grincement au demarrage a froid

### Courroie qui saute cas extreme

courroie qui saute cas extreme

## Diagnostic

Pour diagnostiquer un problème de galet tendeur de courroie de distribution:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- courroie-de-distribution

## Compatibilité

Pour commander le bon galet tendeur de courroie de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
