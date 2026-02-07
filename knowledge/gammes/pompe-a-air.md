---
entity_type: gamme
title: Pompe à air
slug: pompe-a-air
pg_id: 903
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Injecter de l'air frais dans l'echappement pour accelerer le rechauffement
    du catalyseur
  must_be_true:
    - insuffler
    - injecter
    - alimenter
  must_not_contain_concepts:
    - freinage
    - climatisation
    - distribution
    - embrayage
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: voyant_tableau_bord_allume
    then: lecture_codes_defaut_obd_et_diagnostic_electronique
symptoms:
  - id: S1
    label: Voyant moteur au demarrage a froid
    description: voyant moteur au demarrage a froid
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur au demarrage a froid'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit de soufflerie anormal au demarrage
    description: bruit de soufflerie anormal au demarrage
    risk_level: confort
    evidence:
      - 'Observation: bruit de soufflerie anormal au demarrage'
      - Vérification visuelle ou auditive
  - id: S3
    label: Code defaut systeme air secondaire
    description: code defaut systeme air secondaire
    risk_level: confort
    evidence:
      - 'Observation: code defaut systeme air secondaire'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe à air - Guide Diagnostic Complet

## Fonction et Rôle

Injecter de l'air frais dans l'echappement pour accelerer le rechauffement du catalyseur

**Actions principales:** insuffler, injecter, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant moteur au demarrage a froid
- bruit de soufflerie anormal au demarrage
- code defaut systeme air secondaire

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à air:

1. **Inspection visuelle** - Examiner l'état du pompe à air
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- intercooler
- soupape-d-air-secondaire
- soupape-d-aspiration-d-air-secondaire

## Critères de Compatibilité

Pour commander le bon pompe à air, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"
