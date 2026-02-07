---
entity_type: gamme
title: Ressort de suspension
slug: ressort-de-suspension
pg_id: 188
category: suspension
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Supporter la charge du vehicule et maintenir la hauteur de caisse. Stocke et
    restitue l'energie. N'AMORTIT PAS!
  must_be_true:
    - supporter
    - maintenir la hauteur
    - porter
  must_not_contain_concepts:
    - direction
    - freinage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Vehicule affaisse d un cote avant ou arriere
    description: vehicule affaisse d un cote avant ou arriere
    risk_level: confort
    evidence:
      - 'Observation: vehicule affaisse d un cote avant ou arriere'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de claquement metallique sur bosses
    description: bruit de claquement metallique sur bosses
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de claquement metallique sur bosses'
      - Vérification visuelle ou auditive
  - id: S3
    label: Spire de ressort visiblement cassee ou fissuree
    description: spire de ressort visiblement cassee ou fissuree
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: spire de ressort visiblement cassee ou fissuree'
      - Vérification visuelle ou auditive
  - id: S4
    label: Tenue de route degradee en virage et freinage
    description: tenue de route degradee en virage et freinage
    risk_level: securite
    evidence:
      - 'Observation: tenue de route degradee en virage et freinage'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur metallique ressort frotte contre
    description: odeur metallique ressort frotte contre
    risk_level: confort
    evidence:
      - 'Observation: odeur metallique ressort frotte contre'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 150 000 km ou controle technique refuse
    description: plus de 150 000 km ou controle technique refuse
    risk_level: confort
    evidence:
      - 'Observation: plus de 150 000 km ou controle technique refuse'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Ressort de suspension - Guide Diagnostic Complet

## Fonction et Rôle

Supporter la charge du vehicule et maintenir la hauteur de caisse. Stocke et restitue l'energie. N'AMORTIT PAS!

**Actions principales:** supporter, maintenir la hauteur, porter, stocker l'energie, restituer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement metallique sur bosses**
  bruit de claquement metallique sur bosses
- **Spire de ressort visiblement cassee ou fissuree**
  spire de ressort visiblement cassee ou fissuree

### 🟡 Symptômes de Sécurité

- **Tenue de route degradee en virage et freinage**
  tenue de route degradee en virage et freinage

### 🟢 Autres Symptômes

- vehicule affaisse d un cote avant ou arriere
- odeur metallique ressort frotte contre
- plus de 150 000 km ou controle technique refuse

## Procédure de Diagnostic

Pour diagnostiquer un problème de ressort de suspension:

1. **Inspection visuelle** - Examiner l'état du ressort de suspension
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- amortisseur
- kit-de-butee-de-suspension

## Critères de Compatibilité

Pour commander le bon ressort de suspension, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "tenue de route parfaite"
