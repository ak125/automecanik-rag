---
entity_type: gamme
title: Chaîne de distribution
slug: chaine-de-distribution
pg_id: 1123
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Synchroniser la rotation de l'arbre a cames avec le vilebrequin de maniere
    durable
  must_be_true:
    - synchroniser
    - entrainer
    - transmettre
  must_not_contain_concepts:
    - courroie
    - caoutchouc
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_bruit-de-cliquetis-metallique-au-demarrage
    then: verifier_piece
  - if: symptome_claquement-qui-disparait-apres-quelques-secondes
    then: diagnostic_approfondi
  - if: symptome_voyant-moteur-allume-codes-calage
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Bruit de cliquetis metallique au demarrage
    description: bruit de cliquetis metallique au demarrage a froid
    risk_level: confort
    evidence:
      - 'Observation: bruit de cliquetis metallique au demarrage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Claquement qui disparait apres quelques secondes
    description: claquement qui disparait apres quelques secondes
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement qui disparait apres quelques secondes'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant moteur allume codes calage
    description: voyant moteur allume codes calage
    risk_level: immobilisation
    evidence:
      - 'Observation: voyant moteur allume codes calage'
      - Vérification visuelle ou auditive
  - id: S4
    label: Moteur qui manque de puissance
    description: moteur qui manque de puissance
    risk_level: confort
    evidence:
      - 'Observation: moteur qui manque de puissance'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruit de ferraille permanent cote distribution
    description: bruit de ferraille permanent cote distribution
    risk_level: confort
    evidence:
      - 'Observation: bruit de ferraille permanent cote distribution'
      - Vérification visuelle ou auditive
  - id: S6
    label: Difficultes de demarrage
    description: difficultes de demarrage
    risk_level: confort
    evidence:
      - 'Observation: difficultes de demarrage'
      - Vérification visuelle ou auditive
  - id: S7
    label: Consommation huile anormale tendeur hydraulique
    description: consommation huile anormale tendeur hydraulique
    risk_level: confort
    evidence:
      - 'Observation: consommation huile anormale tendeur hydraulique'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Chaîne de distribution - Guide Complet

## Fonction

Synchroniser la rotation de l'arbre a cames avec le vilebrequin de maniere durable

## Symptômes de défaillance

### Bruit de cliquetis metallique au demarrage

bruit de cliquetis metallique au demarrage a froid

### Claquement qui disparait apres quelques secondes

claquement qui disparait apres quelques secondes

### Voyant moteur allume codes calage

voyant moteur allume codes calage

### Moteur qui manque de puissance

moteur qui manque de puissance

### Bruit de ferraille permanent cote distribution

bruit de ferraille permanent cote distribution

### Difficultes de demarrage

difficultes de demarrage

### Consommation huile anormale tendeur hydraulique

consommation huile anormale tendeur hydraulique

## Diagnostic

Pour diagnostiquer un problème de chaîne de distribution:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- courroie-d-accessoire
- kit-de-chaine-de-distribution
- pompe-a-eau
- pompe-a-injection
- poulie-d-arbre-a-came

## Compatibilité

Pour commander le bon chaîne de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
