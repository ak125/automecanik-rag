---
entity_type: gamme
title: Feu avant
slug: feu-avant
pg_id: 259
category: eclairage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Éclaire la route devant le véhicule
  must_be_true:
    - eclairer
    - illuminer
  must_not_contain_concepts:
    - injection
    - freinage
    - embrayage
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
    label: Eclairage insuffisant nuit malgre ampoules
    description: eclairage insuffisant nuit malgre ampoules
    risk_level: confort
    evidence:
      - 'Observation: eclairage insuffisant nuit malgre ampoules'
      - Vérification visuelle ou auditive
  - id: S2
    label: Phare qui ne s allume plus ou par intermittence
    description: phare qui ne s allume plus ou par intermittence
    risk_level: confort
    evidence:
      - 'Observation: phare qui ne s allume plus ou par intermittence'
      - Vérification visuelle ou auditive
  - id: S3
    label: Condensation ou eau a l interieur du bloc optique
    description: condensation ou eau a l interieur du bloc optique
    risk_level: confort
    evidence:
      - 'Observation: condensation ou eau a l interieur du bloc optique'
      - Vérification visuelle ou auditive
  - id: S4
    label: Reglage impossible phares faisceau toujours
    description: reglage impossible phares faisceau toujours
    risk_level: confort
    evidence:
      - 'Observation: reglage impossible phares faisceau toujours'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de plastique brule au niveau du phare
    description: odeur de plastique brule au niveau du phare
    risk_level: confort
    evidence:
      - 'Observation: odeur de plastique brule au niveau du phare'
      - Vérification visuelle ou auditive
  - id: S6
    label: Phare opaque couleur jaunie reduisant
    description: phare opaque couleur jaunie reduisant
    risk_level: confort
    evidence:
      - 'Observation: phare opaque couleur jaunie reduisant'
      - Vérification visuelle ou auditive
  - id: S7
    label: Grincement ou bruit metallique du reglage de phare
    description: grincement ou bruit metallique du reglage de phare
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: grincement ou bruit metallique du reglage de phare'
      - Vérification visuelle ou auditive
  - id: S8
    label: Perte luminosite progressive meme ampoules
    description: perte luminosite progressive meme ampoules
    risk_level: confort
    evidence:
      - 'Observation: perte luminosite progressive meme ampoules'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Feu avant - Guide Diagnostic Complet

## Fonction et Rôle

Éclaire la route devant le véhicule

**Actions principales:** eclairer, illuminer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Grincement ou bruit metallique du reglage de phare**
  grincement ou bruit metallique du reglage de phare

### 🟢 Autres Symptômes

- eclairage insuffisant nuit malgre ampoules
- phare qui ne s allume plus ou par intermittence
- condensation ou eau a l interieur du bloc optique
- reglage impossible phares faisceau toujours
- odeur de plastique brule au niveau du phare
- phare opaque couleur jaunie reduisant

## Procédure de Diagnostic

Pour diagnostiquer un problème de feu avant:

1. **Inspection visuelle** - Examiner l'état du feu avant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-avant
- commande-d-eclairage
- feu-arriere
- feu-clignotant

## Critères de Compatibilité

Pour commander le bon feu avant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure visibilité garantie"
