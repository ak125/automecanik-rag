---
entity_type: gamme
title: Soupape d'admission
slug: soupape-d-admission
pg_id: 1269
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Ouvrir et fermer le passage des gaz d'admission
  must_be_true:
    - ouvrir
    - fermer
    - admettre
  must_not_contain_concepts:
    - echappement
    - carburant
    - injection
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
    label: Perte de compression sur un ou plusieurs cylindres
    description: perte de compression sur un ou plusieurs cylindres
    risk_level: confort
    evidence:
      - 'Observation: perte de compression sur un ou plusieurs cylindres'
      - Vérification visuelle ou auditive
  - id: S2
    label: Rates d allumage persistants
    description: rates d allumage persistants
    risk_level: confort
    evidence:
      - 'Observation: rates d allumage persistants'
      - Vérification visuelle ou auditive
  - id: S3
    label: Claquement au niveau de la culasse
    description: claquement au niveau de la culasse
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: claquement au niveau de la culasse'
      - Vérification visuelle ou auditive
  - id: S4
    label: Consommation d huile anormale guides uses
    description: consommation d huile anormale guides uses
    risk_level: confort
    evidence:
      - 'Observation: consommation d huile anormale guides uses'
      - Vérification visuelle ou auditive
  - id: S5
    label: Fumee bleue a l echappement
    description: fumee bleue a l echappement
    risk_level: confort
    evidence:
      - 'Observation: fumee bleue a l echappement'
      - Vérification visuelle ou auditive
  - id: S6
    label: Casse de courroie de distribution controle
    description: casse de courroie de distribution controle
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: casse de courroie de distribution controle'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Soupape d'admission - Guide Diagnostic Complet

## Fonction et Rôle

Ouvrir et fermer le passage des gaz d'admission

**Actions principales:** ouvrir, fermer, admettre

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement au niveau de la culasse**
  claquement au niveau de la culasse
- **Casse de courroie de distribution controle**
  casse de courroie de distribution controle

### 🟢 Autres Symptômes

- perte de compression sur un ou plusieurs cylindres
- rates d allumage persistants
- consommation d huile anormale guides uses
- fumee bleue a l echappement

## Procédure de Diagnostic

Pour diagnostiquer un problème de soupape d'admission:

1. **Inspection visuelle** - Examiner l'état du soupape d'admission
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bagues-d-etancheite-moteur
- joint-de-cache-culbuteurs
- joint-de-collecteur
- joint-de-culasse
- poulie-d-arbre-a-came
- poussoir-de-soupape
- soupape-d-echappement

## Critères de Compatibilité

Pour commander le bon soupape d'admission, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"
