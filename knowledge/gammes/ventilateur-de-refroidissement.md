---
entity_type: gamme
title: Ventilateur de refroidissement
slug: ventilateur-de-refroidissement
pg_id: 508
category: refroidissement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Forcer le passage de l'air a travers le radiateur quand le vehicule est a
    l'arret ou a faible vitesse
  must_be_true:
    - forcer
    - ventiler
    - refroidir
  must_not_contain_concepts:
    - pulseur
    - habitacle
    - chauffage
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
    label: Surchauffe uniquement au ralenti ou en ville
    description: surchauffe uniquement au ralenti ou en ville
    risk_level: confort
    evidence:
      - 'Observation: surchauffe uniquement au ralenti ou en ville'
      - Vérification visuelle ou auditive
  - id: S2
    label: Ventilateur qui ne demarre jamais silence
    description: ventilateur qui ne demarre jamais silence
    risk_level: confort
    evidence:
      - 'Observation: ventilateur qui ne demarre jamais silence'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de roulement ou grincement au demarrage
    description: bruit de roulement ou grincement au demarrage
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit de roulement ou grincement au demarrage'
      - Vérification visuelle ou auditive
  - id: S4
    label: Pales de ventilateur fissurees ou cassees
    description: pales de ventilateur fissurees ou cassees
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: pales de ventilateur fissurees ou cassees'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de plastique chaud pres du radiateur
    description: odeur de plastique chaud pres du radiateur
    risk_level: confort
    evidence:
      - 'Observation: odeur de plastique chaud pres du radiateur'
      - Vérification visuelle ou auditive
  - id: S6
    label: Clim moins efficace ventilateur partage
    description: clim moins efficace ventilateur partage
    risk_level: confort
    evidence:
      - 'Observation: clim moins efficace ventilateur partage'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Ventilateur de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Forcer le passage de l'air a travers le radiateur quand le vehicule est a l'arret ou a faible vitesse

**Actions principales:** forcer, ventiler, refroidir, brasser l'air

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de roulement ou grincement au demarrage**
  bruit de roulement ou grincement au demarrage
- **Pales de ventilateur fissurees ou cassees**
  pales de ventilateur fissurees ou cassees

### 🟢 Autres Symptômes

- surchauffe uniquement au ralenti ou en ville
- ventilateur qui ne demarre jamais silence
- odeur de plastique chaud pres du radiateur
- clim moins efficace ventilateur partage

## Procédure de Diagnostic

Pour diagnostiquer un problème de ventilateur de refroidissement:

1. **Inspection visuelle** - Examiner l'état du ventilateur de refroidissement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- vase-d-expansion
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon ventilateur de refroidissement, vous devez connaître:

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
