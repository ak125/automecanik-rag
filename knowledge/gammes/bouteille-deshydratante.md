---
entity_type: gamme
title: Bouteille déshydratante
slug: bouteille-deshydratante
pg_id: 851
category: climatisation
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Filtre et assèche le fluide frigorigène
  must_be_true:
    - filtrer
    - assecher
    - retenir l'humidite
  must_not_contain_concepts:
    - injection
    - freinage
    - allumage
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
    label: Circuit de clim ouvert recemment intervention
    description: circuit de clim ouvert recemment intervention
    risk_level: confort
    evidence:
      - 'Observation: circuit de clim ouvert recemment intervention'
      - Vérification visuelle ou auditive
  - id: S2
    label: Clim moins performante apres une reparation
    description: clim moins performante apres une reparation
    risk_level: confort
    evidence:
      - 'Observation: clim moins performante apres une reparation'
      - Vérification visuelle ou auditive
  - id: S3
    label: Compresseur qui fait un bruit anormal
    description: compresseur qui fait un bruit anormal
    risk_level: confort
    evidence:
      - 'Observation: compresseur qui fait un bruit anormal'
      - Vérification visuelle ou auditive
  - id: S4
    label: Humidite visible dans le voyant du deshydrateur
    description: humidite visible dans le voyant du deshydrateur
    risk_level: confort
    evidence:
      - 'Observation: humidite visible dans le voyant du deshydrateur'
      - Vérification visuelle ou auditive
  - id: S5
    label: Gaz recupere trouble ou avec impuretes
    description: gaz recupere trouble ou avec impuretes
    risk_level: confort
    evidence:
      - 'Observation: gaz recupere trouble ou avec impuretes'
      - Vérification visuelle ou auditive
  - id: S6
    label: Remplacement de compresseur prevu preventif
    description: remplacement de compresseur prevu preventif
    risk_level: confort
    evidence:
      - 'Observation: remplacement de compresseur prevu preventif'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Bouteille déshydratante - Guide Diagnostic Complet

## Fonction et Rôle

Filtre et assèche le fluide frigorigène

**Actions principales:** filtrer, assecher, retenir l'humidite

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- circuit de clim ouvert recemment intervention
- clim moins performante apres une reparation
- compresseur qui fait un bruit anormal
- humidite visible dans le voyant du deshydrateur
- gaz recupere trouble ou avec impuretes
- remplacement de compresseur prevu preventif

## Procédure de Diagnostic

Pour diagnostiquer un problème de bouteille déshydratante:

1. **Inspection visuelle** - Examiner l'état du bouteille déshydratante
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-de-ventilation
- compresseur-de-climatisation
- condenseur-de-climatisation
- detendeur-de-climatisation
- evaporateur-de-climatisation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle

## Critères de Compatibilité

Pour commander le bon bouteille déshydratante, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit le moteur"
