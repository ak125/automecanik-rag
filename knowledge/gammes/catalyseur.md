---
entity_type: gamme
title: Catalyseur
slug: catalyseur
pg_id: 429
category: echappement
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Transforme les gaz polluants (CO, HC, NOx) en gaz moins nocifs par réaction
    chimique
  must_be_true:
    - transformer
    - convertir
    - reduire
  must_not_contain_concepts:
    - fap
    - filtre a particules
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
    label: Voyant moteur allume codes p0420 p0430
    description: voyant moteur allume codes p0420 p0430
    risk_level: confort
    evidence:
      - 'Observation: voyant moteur allume codes p0420 p0430'
      - Vérification visuelle ou auditive
  - id: S2
    label: Perte de puissance progressive du moteur
    description: perte de puissance progressive du moteur
    risk_level: confort
    evidence:
      - 'Observation: perte de puissance progressive du moteur'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit metallique de ferraille sous le vehicule
    description: bruit metallique de ferraille sous le vehicule
    risk_level: degats_volant_moteur
    evidence:
      - 'Observation: bruit metallique de ferraille sous le vehicule'
      - Vérification visuelle ou auditive
  - id: S4
    label: Odeur d uf pourri soufre a l echappement
    description: odeur d uf pourri soufre a l echappement
    risk_level: confort
    evidence:
      - 'Observation: odeur d uf pourri soufre a l echappement'
      - Vérification visuelle ou auditive
  - id: S5
    label: Echec au controle technique pollution
    description: echec au controle technique pollution
    risk_level: confort
    evidence:
      - 'Observation: echec au controle technique pollution'
      - Vérification visuelle ou auditive
  - id: S6
    label: Surconsommation de carburant
    description: surconsommation de carburant
    risk_level: confort
    evidence:
      - 'Observation: surconsommation de carburant'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Catalyseur - Guide Diagnostic Complet

## Fonction et Rôle

Transforme les gaz polluants (CO, HC, NOx) en gaz moins nocifs par réaction chimique

**Actions principales:** transformer, convertir, reduire, traiter

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit metallique de ferraille sous le vehicule**
  bruit metallique de ferraille sous le vehicule

### 🟢 Autres Symptômes

- voyant moteur allume codes p0420 p0430
- perte de puissance progressive du moteur
- odeur d uf pourri soufre a l echappement
- echec au controle technique pollution
- surconsommation de carburant

## Procédure de Diagnostic

Pour diagnostiquer un problème de catalyseur:

1. **Inspection visuelle** - Examiner l'état du catalyseur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-temperature-d-air-admission
- fap
- sonde-lambda
- tube-d-echappement
- vanne-egr

## Critères de Compatibilité

Pour commander le bon catalyseur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passe le controle technique"
