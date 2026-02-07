---
entity_type: gamme
title: Soupape d'aspiration d'air secondaire
slug: soupape-d-aspiration-d-air-secondaire
pg_id: 1136
category: alimentation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Admettre l'air secondaire pour la depollution a froid
  must_be_true:
    - aspirer
    - admettre
    - controler
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
    label: Voyant moteur avec code air secondaire
    description: voyant moteur avec code air secondaire
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur avec code air secondaire'
      - Vérification visuelle ou auditive
  - id: S2
    label: Bruit anormal au demarrage a froid
    description: bruit anormal au demarrage a froid
    risk_level: confort
    evidence:
      - 'Observation: bruit anormal au demarrage a froid'
      - Vérification visuelle ou auditive
  - id: S3
    label: Ralenti irregulier a froid
    description: ralenti irregulier a froid
    risk_level: confort
    evidence:
      - 'Observation: ralenti irregulier a froid'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Soupape d'aspiration d'air secondaire - Guide Diagnostic Complet

## Fonction et Rôle

Admettre l'air secondaire pour la depollution a froid

**Actions principales:** aspirer, admettre, controler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant moteur avec code air secondaire
- bruit anormal au demarrage a froid
- ralenti irregulier a froid

## Procédure de Diagnostic

Pour diagnostiquer un problème de soupape d'aspiration d'air secondaire:

1. **Inspection visuelle** - Examiner l'état du soupape d'aspiration d'air secondaire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- intercooler
- pompe-a-air
- soupape-d-air-secondaire

## Critères de Compatibilité

Pour commander le bon soupape d'aspiration d'air secondaire, vous devez connaître:

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
