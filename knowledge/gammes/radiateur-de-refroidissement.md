---
entity_type: gamme
title: Radiateur de refroidissement
slug: radiateur-de-refroidissement
pg_id: 470
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Dissiper la chaleur du liquide de refroidissement vers l'air exterieur
  must_be_true:
    - dissiper
    - echanger
    - refroidir
  must_not_contain_concepts:
    - chauffage
    - habitacle
    - huile
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
symptoms:
  - id: S1
    label: Flaque de liquide colore sous l avant
    description: flaque de liquide colore sous l avant
    risk_level: confort
    evidence:
      - 'Observation: flaque de liquide colore sous l avant'
      - Vérification visuelle ou auditive
  - id: S2
    label: Traces de corrosion sur les tubes du radiateur
    description: traces de corrosion sur les tubes du radiateur
    risk_level: confort
    evidence:
      - 'Observation: traces de corrosion sur les tubes du radiateur'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement d air ou de vapeur a l avant
    description: sifflement d air ou de vapeur a l avant
    risk_level: confort
    evidence:
      - 'Observation: sifflement d air ou de vapeur a l avant'
      - Vérification visuelle ou auditive
  - id: S4
    label: Surchauffe au ralenti ou en embouteillage
    description: surchauffe au ralenti ou en embouteillage
    risk_level: confort
    evidence:
      - 'Observation: surchauffe au ralenti ou en embouteillage'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de liquide de refroidissement chaud
    description: odeur de liquide de refroidissement chaud
    risk_level: confort
    evidence:
      - 'Observation: odeur de liquide de refroidissement chaud'
      - Vérification visuelle ou auditive
  - id: S6
    label: Radiateur visiblement deforme ou perce
    description: radiateur visiblement deforme ou perce
    risk_level: confort
    evidence:
      - 'Observation: radiateur visiblement deforme ou perce'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Radiateur de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Dissiper la chaleur du liquide de refroidissement vers l'air exterieur

**Actions principales:** dissiper, echanger, refroidir, evacuer la chaleur

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- flaque de liquide colore sous l avant
- traces de corrosion sur les tubes du radiateur
- sifflement d air ou de vapeur a l avant
- surchauffe au ralenti ou en embouteillage
- odeur de liquide de refroidissement chaud
- radiateur visiblement deforme ou perce

## Procédure de Diagnostic

Pour diagnostiquer un problème de radiateur de refroidissement:

1. **Inspection visuelle** - Examiner l'état du radiateur de refroidissement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bouchon-de-radiateur
- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-chauffage
- sonde-de-refroidissement
- thermostat
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon radiateur de refroidissement, vous devez connaître:

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
