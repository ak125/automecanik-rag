---
entity_type: gamme
title: Bougie de préchauffage
slug: bougie-de-prechauffage
pg_id: 243
category: allumage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Chauffer la chambre de combustion a froid pour faciliter le demarrage diesel
    - N'agit qu'au demarrage
  must_be_true:
    - chauffer
    - prechauffer
    - rechauffer
  must_not_contain_concepts:
    - essence
    - etincelle
    - allumage
    - haute tension
    - bobine
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Demarrage long ou difficile par temps froid
    description: demarrage long ou difficile par temps froid
    risk_level: confort
    evidence:
      - 'Observation: demarrage long ou difficile par temps froid'
      - Vérification visuelle ou auditive
  - id: S2
    label: Voyant prechauffage allume plus reste
    description: voyant prechauffage allume plus reste
    risk_level: confort
    evidence:
      - 'Observation: voyant prechauffage allume plus reste'
      - Vérification visuelle ou auditive
  - id: S3
    label: Fumee blanche au demarrage qui persiste
    description: fumee blanche au demarrage qui persiste
    risk_level: confort
    evidence:
      - 'Observation: fumee blanche au demarrage qui persiste'
      - Vérification visuelle ou auditive
  - id: S4
    label: Rates moteur a froid les premieres secondes
    description: rates moteur a froid les premieres secondes
    risk_level: confort
    evidence:
      - 'Observation: rates moteur a froid les premieres secondes'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de gazole non brule au demarrage
    description: odeur de gazole non brule au demarrage
    risk_level: confort
    evidence:
      - 'Observation: odeur de gazole non brule au demarrage'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 100 000 km sans remplacement diesel
    description: plus de 100 000 km sans remplacement diesel
    risk_level: confort
    evidence:
      - 'Observation: plus de 100 000 km sans remplacement diesel'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bougie de préchauffage - Guide Diagnostic Complet

## Fonction et Rôle

Chauffer la chambre de combustion a froid pour faciliter le demarrage diesel - N'agit qu'au demarrage

**Actions principales:** chauffer, prechauffer, rechauffer, porter a temperature, faciliter le demarrage

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage long ou difficile par temps froid
- voyant prechauffage allume plus reste
- fumee blanche au demarrage qui persiste
- rates moteur a froid les premieres secondes
- odeur de gazole non brule au demarrage
- plus de 100 000 km sans remplacement diesel

## Procédure de Diagnostic

Pour diagnostiquer un problème de bougie de préchauffage:

1. **Inspection visuelle** - Examiner l'état du bougie de préchauffage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- boitier-de-prechauffage
- demarreur
- filtre-a-carburant

## Critères de Compatibilité

Pour commander le bon bougie de préchauffage, vous devez connaître:

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
