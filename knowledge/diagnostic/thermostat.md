---
entity_type: gamme
title: Thermostat
slug: thermostat
pg_id: 316
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Reguler le flux de liquide de refroidissement selon la temperature moteur
  must_be_true:
    - reguler
    - ouvrir
    - fermer
  must_not_contain_concepts:
    - sonde
    - capteur
    - electronique
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: symptome_aiguille-de-temperature-dans-le-rouge
    then: verifier_piece
  - if: symptome_moteur-qui-ne-chauffe-jamais-aiguille
    then: diagnostic_approfondi
  - if: symptome_sifflement-ou-vapeur-s-echappant-du
    then: remplacement_recommande
symptoms:
  - id: S1
    label: Aiguille de temperature dans le rouge
    description: aiguille de temperature dans le rouge rapidement
    risk_level: confort
    evidence:
      - 'Observation: aiguille de temperature dans le rouge'
      - Vérification visuelle ou auditive
  - id: S2
    label: Moteur qui ne chauffe jamais aiguille
    description: moteur qui ne chauffe jamais aiguille basse
    risk_level: confort
    evidence:
      - 'Observation: moteur qui ne chauffe jamais aiguille'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement ou vapeur s echappant du
    description: sifflement ou vapeur s echappant du capot
    risk_level: confort
    evidence:
      - 'Observation: sifflement ou vapeur s echappant du'
      - Vérification visuelle ou auditive
  - id: S4
    label: Chauffage qui reste froid tres longtemps
    description: chauffage qui reste froid tres longtemps
    risk_level: confort
    evidence:
      - 'Observation: chauffage qui reste froid tres longtemps'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de liquide de refroidissement en
    description: odeur de liquide de refroidissement en surchauffe
    risk_level: confort
    evidence:
      - 'Observation: odeur de liquide de refroidissement en'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 100 000 km sans
    description: plus de 100 000 km sans remplacement
    risk_level: confort
    evidence:
      - 'Observation: plus de 100 000 km sans'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Thermostat - Guide Complet

## Fonction

Reguler le flux de liquide de refroidissement selon la temperature moteur

## Symptômes de défaillance

### Aiguille de temperature dans le rouge

aiguille de temperature dans le rouge rapidement

### Moteur qui ne chauffe jamais aiguille

moteur qui ne chauffe jamais aiguille basse

### Sifflement ou vapeur s echappant du

sifflement ou vapeur s echappant du capot

### Chauffage qui reste froid tres longtemps

chauffage qui reste froid tres longtemps

### Odeur de liquide de refroidissement en

odeur de liquide de refroidissement en surchauffe

### Plus de 100 000 km sans

plus de 100 000 km sans remplacement

## Diagnostic

Pour diagnostiquer un problème de thermostat:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- vase-d-expansion

## Compatibilité

Pour commander le bon thermostat, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
