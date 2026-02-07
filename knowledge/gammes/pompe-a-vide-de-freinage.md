---
entity_type: gamme
title: Pompe à vide de freinage
slug: pompe-a-vide-de-freinage
pg_id: 387
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Assister l'effort du conducteur sur la pedale de frein
  must_be_true:
    - assister le freinage
    - reduire l'effort
    - fournir une depression
  must_not_contain_concepts:
    - friction
    - hydraulique directe
    - ABS
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
    label: Pedale de frein tres dure
    description: pedale de frein tres dure
    risk_level: securite
    evidence:
      - 'Observation: pedale de frein tres dure'
      - Vérification visuelle ou auditive
  - id: S2
    label: Assistance au freinage defaillante
    description: assistance au freinage defaillante
    risk_level: securite
    evidence:
      - 'Observation: assistance au freinage defaillante'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement au niveau du moteur
    description: sifflement au niveau du moteur
    risk_level: confort
    evidence:
      - 'Observation: sifflement au niveau du moteur'
      - Vérification visuelle ou auditive
  - id: S4
    label: Voyant defaut frein allume
    description: voyant defaut frein allume
    risk_level: securite
    evidence:
      - 'Observation: voyant defaut frein allume'
      - Vérification visuelle ou auditive
  - id: S5
    label: Pedale dure surtout freinage depression
    description: pedale dure surtout freinage depression
    risk_level: securite
    evidence:
      - 'Observation: pedale dure surtout freinage depression'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe à vide de freinage - Guide Diagnostic Complet

## Fonction et Rôle

Assister l'effort du conducteur sur la pedale de frein

**Actions principales:** assister le freinage, reduire l'effort, fournir une depression, creer le vide, alimenter le servofrein

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Pedale de frein tres dure**
  pedale de frein tres dure
- **Assistance au freinage defaillante**
  assistance au freinage defaillante
- **Voyant defaut frein allume**
  voyant defaut frein allume
- **Pedale dure surtout freinage depression**
  pedale dure surtout freinage depression

### 🟢 Autres Symptômes

- sifflement au niveau du moteur

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à vide de freinage:

1. **Inspection visuelle** - Examiner l'état du pompe à vide de freinage
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- maitre-cylindre-de-frein
- servo-frein

## Critères de Compatibilité

Pour commander le bon pompe à vide de freinage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage direct"
