---
entity_type: gamme
title: Durite de refroidissement
slug: durite-de-refroidissement
pg_id: 475
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Acheminer le liquide de refroidissement entre les elements du circuit
  must_be_true:
    - acheminer
    - conduire
    - relier
  must_not_contain_concepts:
    - huile
    - carburant
    - frein
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
    label: Traces de liquide colore sous le vehicule
    description: traces de liquide colore sous le vehicule
    risk_level: confort
    evidence:
      - 'Observation: traces de liquide colore sous le vehicule'
      - Vérification visuelle ou auditive
  - id: S2
    label: Durite visiblement gonflee ou craquelee
    description: durite visiblement gonflee ou craquelee
    risk_level: confort
    evidence:
      - 'Observation: durite visiblement gonflee ou craquelee'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement ou gargouillement dans le circuit
    description: sifflement ou gargouillement dans le circuit
    risk_level: confort
    evidence:
      - 'Observation: sifflement ou gargouillement dans le circuit'
      - Vérification visuelle ou auditive
  - id: S4
    label: Niveau de liquide qui baisse regulierement
    description: niveau de liquide qui baisse regulierement
    risk_level: confort
    evidence:
      - 'Observation: niveau de liquide qui baisse regulierement'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur sucree de liquide de refroidissement
    description: odeur sucree de liquide de refroidissement
    risk_level: confort
    evidence:
      - 'Observation: odeur sucree de liquide de refroidissement'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 100 000 km ou 8 ans sans remplacement
    description: plus de 100 000 km ou 8 ans sans remplacement
    risk_level: confort
    evidence:
      - 'Observation: plus de 100 000 km ou 8 ans sans remplacement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Durite de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Acheminer le liquide de refroidissement entre les elements du circuit

**Actions principales:** acheminer, conduire, relier, transporter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- traces de liquide colore sous le vehicule
- durite visiblement gonflee ou craquelee
- sifflement ou gargouillement dans le circuit
- niveau de liquide qui baisse regulierement
- odeur sucree de liquide de refroidissement
- plus de 100 000 km ou 8 ans sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de durite de refroidissement:

1. **Inspection visuelle** - Examiner l'état du durite de refroidissement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- thermostat
- vase-d-expansion
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon durite de refroidissement, vous devez connaître:

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
