---
entity_type: gamme
title: Attelage
slug: attelage
pg_id: 39
category: accessoires
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Permet de tracter une remorque ou une caravane
  must_be_true:
    - tracter
    - remorquer
    - accrocher
  must_not_contain_concepts:
    - freinage
    - suspension
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
symptoms:
  - id: S1
    label: Boule attelage usee tete attelage
    description: boule attelage usee tete attelage
    risk_level: confort
    evidence:
      - 'Observation: boule attelage usee tete attelage'
      - Vérification visuelle ou auditive
  - id: S2
    label: Corrosion importante sur la traverse ou la boule
    description: corrosion importante sur la traverse ou la boule
    risk_level: confort
    evidence:
      - 'Observation: corrosion importante sur la traverse ou la boule'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fissures visibles sur les soudures
    description: fissures visibles sur les soudures
    risk_level: confort
    evidence:
      - 'Observation: fissures visibles sur les soudures'
      - Vérification visuelle ou auditive
  - id: S4
    label: Faisceau electrique defaillant feux remorque
    description: faisceau electrique defaillant feux remorque
    risk_level: confort
    evidence:
      - 'Observation: faisceau electrique defaillant feux remorque'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruits de claquement lors du tractage
    description: bruits de claquement lors du tractage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruits de claquement lors du tractage'
      - Vérification visuelle ou auditive
  - id: S6
    label: Attelage non homologue controle technique
    description: attelage non homologue controle technique
    risk_level: confort
    evidence:
      - 'Observation: attelage non homologue controle technique'
      - Vérification visuelle ou auditive
  - id: S7
    label: Remorque oscille anormalement route signe
    description: remorque oscille anormalement route signe
    risk_level: confort
    evidence:
      - 'Observation: remorque oscille anormalement route signe'
      - Vérification visuelle ou auditive
  - id: S8
    label: Odeur caoutchouc brule provenant pneus
    description: odeur caoutchouc brule provenant pneus
    risk_level: securite
    evidence:
      - 'Observation: odeur caoutchouc brule provenant pneus'
      - Vérification visuelle ou auditive
  - id: S9
    label: Plus utilisation forte utilisation controle
    description: plus utilisation forte utilisation controle
    risk_level: confort
    evidence:
      - 'Observation: plus utilisation forte utilisation controle'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Attelage - Guide Diagnostic Complet

## Fonction et Rôle

Permet de tracter une remorque ou une caravane

**Actions principales:** tracter, remorquer, accrocher

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruits de claquement lors du tractage**
  bruits de claquement lors du tractage

### 🟡 Symptômes de Sécurité

- **Odeur caoutchouc brule provenant pneus**
  odeur caoutchouc brule provenant pneus

### 🟢 Autres Symptômes

- boule attelage usee tete attelage
- corrosion importante sur la traverse ou la boule
- fissures visibles sur les soudures
- faisceau electrique defaillant feux remorque
- attelage non homologue controle technique
- remorque oscille anormalement route signe

## Procédure de Diagnostic

Pour diagnostiquer un problème de attelage:

1. **Inspection visuelle** - Examiner l'état du attelage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- faisceau attelage
- boule

## Critères de Compatibilité

Pour commander le bon attelage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"
