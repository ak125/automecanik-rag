---
entity_type: gamme
title: Poulie d'alternateur
slug: poulie-d-alternateur
pg_id: 1108
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmet le mouvement à l'alternateur
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
  - if: symptome_sifflement-aigu-au-demarrage-a-froid
    then: verifier_piece
  - if: symptome_courroie-d-accessoire-qui-saute-ou
    then: diagnostic_approfondi
  - if: symptome_vibrations-moteur-au-ralenti
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Sifflement aigu au demarrage a froid
    description: sifflement aigu au demarrage a froid
    risk_level: confort
    evidence:
      - 'Observation: sifflement aigu au demarrage a froid'
      - Vérification visuelle ou auditive
  - id: S2
    label: Courroie d accessoire qui saute ou
    description: courroie d accessoire qui saute ou patine
    risk_level: confort
    evidence:
      - 'Observation: courroie d accessoire qui saute ou'
      - Vérification visuelle ou auditive
  - id: S3
    label: Vibrations moteur au ralenti
    description: vibrations moteur au ralenti
    risk_level: confort
    evidence:
      - 'Observation: vibrations moteur au ralenti'
      - Vérification visuelle ou auditive
  - id: S4
    label: Bruit de roulement au niveau de
    description: bruit de roulement au niveau de l alternateur
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement au niveau de'
      - Vérification visuelle ou auditive
  - id: S5
    label: Alternateur qui charge mal par intermittence
    description: alternateur qui charge mal par intermittence
    risk_level: confort
    evidence:
      - 'Observation: alternateur qui charge mal par intermittence'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 120 000 km sans
    description: plus de 120 000 km sans remplacement
    risk_level: confort
    evidence:
      - 'Observation: plus de 120 000 km sans'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Poulie d'alternateur - Guide Complet

## Fonction

Transmet le mouvement à l'alternateur

## Symptômes de défaillance

### Sifflement aigu au demarrage a froid

sifflement aigu au demarrage a froid

### Courroie d accessoire qui saute ou

courroie d accessoire qui saute ou patine

### Vibrations moteur au ralenti

vibrations moteur au ralenti

### Bruit de roulement au niveau de

bruit de roulement au niveau de l alternateur

### Alternateur qui charge mal par intermittence

alternateur qui charge mal par intermittence

### Plus de 120 000 km sans

plus de 120 000 km sans remplacement

## Diagnostic

Pour diagnostiquer un problème de poulie d'alternateur:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- alternateur
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- poulie-vilebrequin

## Compatibilité

Pour commander le bon poulie d'alternateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
