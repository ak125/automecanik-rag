---
entity_type: gamme
title: Courroie d'accessoire
slug: courroie-d-accessoire
pg_id: 10
category: distribution
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Entraîne les accessoires moteur
  must_be_true:
    - entrainer
    - transmettre
  must_not_contain_concepts:
    - freinage
    - climatisation
    - turbo
    - injection
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
  - if: kilometrage_eleve_ou_usure_visible
    then: remplacement_preventif_recommande
symptoms:
  - id: S1
    label: Sifflement au demarrage ou a l acceleration
    description: sifflement au demarrage ou a l acceleration
    risk_level: confort
    evidence:
      - 'Observation: sifflement au demarrage ou a l acceleration'
      - Vérification visuelle ou auditive
  - id: S2
    label: Courroie fissuree ou effilochee visible
    description: courroie fissuree ou effilochee visible
    risk_level: confort
    evidence:
      - 'Observation: courroie fissuree ou effilochee visible'
      - Vérification visuelle ou auditive
  - id: S3
    label: Voyant batterie allume alternateur non entraine
    description: voyant batterie allume alternateur non entraine
    risk_level: confort
    evidence:
      - 'Observation: voyant batterie allume alternateur non entraine'
      - Vérification visuelle ou auditive
  - id: S4
    label: Perte de direction assistee si sur meme courroie
    description: perte de direction assistee si sur meme courroie
    risk_level: securite
    evidence:
      - 'Observation: perte de direction assistee si sur meme courroie'
      - Vérification visuelle ou auditive
  - id: S5
    label: Odeur de caoutchouc brule
    description: odeur de caoutchouc brule
    risk_level: confort
    evidence:
      - 'Observation: odeur de caoutchouc brule'
      - Vérification visuelle ou auditive
  - id: S6
    label: Plus de 60 000 km ou 5 ans depuis le remplacement
    description: plus de 60 000 km ou 5 ans depuis le remplacement
    risk_level: confort
    evidence:
      - 'Observation: plus de 60 000 km ou 5 ans depuis le remplacement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Courroie d'accessoire - Guide Diagnostic Complet

## Fonction et Rôle

Entraîne les accessoires moteur

**Actions principales:** entrainer, transmettre

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Perte de direction assistee si sur meme courroie**
  perte de direction assistee si sur meme courroie

### 🟢 Autres Symptômes

- sifflement au demarrage ou a l acceleration
- courroie fissuree ou effilochee visible
- voyant batterie allume alternateur non entraine
- odeur de caoutchouc brule
- plus de 60 000 km ou 5 ans depuis le remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de courroie d'accessoire:

1. **Inspection visuelle** - Examiner l'état du courroie d'accessoire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- compresseur-de-climatisation
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-a-eau
- pompe-de-direction-assistee
- poulie-d-alternateur
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon courroie d'accessoire, vous devez connaître:

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
