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
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Aiguille de temperature dans le rouge rapidement
    description: aiguille de temperature dans le rouge rapidement
    risk_level: confort
    evidence:
      - 'Observation: aiguille de temperature dans le rouge rapidement'
      - Vérification visuelle ou auditive
  - id: S2
    label: Moteur qui ne chauffe jamais aiguille basse
    description: moteur qui ne chauffe jamais aiguille basse
    risk_level: confort
    evidence:
      - 'Observation: moteur qui ne chauffe jamais aiguille basse'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement ou vapeur s echappant du capot
    description: sifflement ou vapeur s echappant du capot
    risk_level: confort
    evidence:
      - 'Observation: sifflement ou vapeur s echappant du capot'
      - Vérification visuelle ou auditive
  - id: S4
    label: Chauffage qui reste froid tres longtemps
    description: chauffage qui reste froid tres longtemps
    risk_level: confort
    evidence:
      - 'Observation: chauffage qui reste froid tres longtemps'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de liquide de refroidissement en surchauffe
    description: odeur de liquide de refroidissement en surchauffe
    risk_level: confort
    evidence:
      - 'Observation: odeur de liquide de refroidissement en surchauffe'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 100 000 km sans remplacement
    description: plus de 100 000 km sans remplacement
    risk_level: confort
    evidence:
      - 'Observation: plus de 100 000 km sans remplacement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Thermostat - Guide Diagnostic Complet

## Fonction et Rôle

Reguler le flux de liquide de refroidissement selon la temperature moteur

**Actions principales:** reguler, ouvrir, fermer, controler le flux

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- aiguille de temperature dans le rouge rapidement
- moteur qui ne chauffe jamais aiguille basse
- sifflement ou vapeur s echappant du capot
- chauffage qui reste froid tres longtemps
- odeur de liquide de refroidissement en surchauffe
- plus de 100 000 km sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de thermostat:

1. **Inspection visuelle** - Examiner l'état du thermostat
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- vase-d-expansion
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon thermostat, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "evite la casse moteur"
