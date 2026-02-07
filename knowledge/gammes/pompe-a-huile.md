---
entity_type: gamme
title: Pompe à huile
slug: pompe-a-huile
pg_id: 596
category: moteur
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Alimenter le circuit de lubrification en huile sous pression
  must_be_true:
    - alimenter
    - pressuriser
    - distribuer
  must_not_contain_concepts:
    - freinage
    - climatisation
    - direction
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
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Voyant huile allume moteur chaud
    description: voyant huile allume moteur chaud
    risk_level: confort
    evidence:
      - 'Observation: voyant huile allume moteur chaud'
      - Vérification visuelle ou auditive
  - id: S2
    label: Pression d huile insuffisante
    description: pression d huile insuffisante
    risk_level: confort
    evidence:
      - 'Observation: pression d huile insuffisante'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de cliquetis moteur
    description: bruit de cliquetis moteur
    risk_level: confort
    evidence:
      - 'Observation: bruit de cliquetis moteur'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe à huile - Guide Diagnostic Complet

## Fonction et Rôle

Alimenter le circuit de lubrification en huile sous pression

**Actions principales:** alimenter, pressuriser, distribuer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant huile allume moteur chaud
- pression d huile insuffisante
- bruit de cliquetis moteur

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à huile:

1. **Inspection visuelle** - Examiner l'état du pompe à huile
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- bagues-d-etancheite-moteur
- capteur-niveau-d-huile-moteur
- capteur-pression-et-temperature-d-huile
- carter-d-huile
- pressostat-d-huile

## Critères de Compatibilité

Pour commander le bon pompe à huile, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"
