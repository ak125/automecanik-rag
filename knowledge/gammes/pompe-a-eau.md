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
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Fuite de liquide au niveau de la pompe
    description: fuite de liquide au niveau de la pompe
    risk_level: confort
    evidence:
      - 'Observation: fuite de liquide au niveau de la pompe'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de roulement cote distribution
    description: bruit de roulement cote distribution
    risk_level: confort
    evidence:
      - 'Observation: bruit de roulement cote distribution'
      - Vérification visuelle ou auditive
  - id: S3
    label: Jeu perceptible dans la poulie de pompe
    description: jeu perceptible dans la poulie de pompe
    risk_level: confort
    evidence:
      - 'Observation: jeu perceptible dans la poulie de pompe'
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
# Pompe à eau - Guide Diagnostic Complet

## Fonction et Rôle

Faire circuler le liquide de refroidissement dans le circuit moteur

**Actions principales:** faire circuler, pomper, alimenter, assurer la circulation

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Surchauffe moteur malgre niveau correct**
  surchauffe moteur malgre niveau correct

### 🟢 Autres Symptômes

- fuite de liquide au niveau de la pompe
- bruit de roulement cote distribution
- jeu perceptible dans la poulie de pompe
- odeur de liquide de refroidissement chaud
- echeance distribution approche preventif

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à eau:

1. **Inspection visuelle** - Examiner l'état du pompe à eau
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- chaine-de-distribution
- courroie-d-accessoire
- courroie-de-distribution
- durite-de-refroidissement
- kit-de-chaine-de-distribution
- kit-de-distribution
- radiateur-de-refroidissement
- sonde-de-refroidissement

## Critères de Compatibilité

Pour commander le bon pompe à eau, vous devez connaître:

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
