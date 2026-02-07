---
entity_type: gamme
title: Pompe de direction assistée
slug: pompe-de-direction-assistee
pg_id: 12
category: direction
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: >-
    Fournir la pression hydraulique pour assister l'effort de braquage - Reduit
    l'effort au volant
  must_be_true:
    - assister
    - fournir la pression
    - alimenter
  must_not_contain_concepts:
    - suspension
    - amortisseur
    - electrique
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: fuite_detectee_ou_niveau_bas
    then: identifier_origine_fuite_et_verifier_joints
symptoms:
  - id: S1
    label: Bruit grognement gemissement tournant volant
    description: bruit grognement gemissement tournant volant
    risk_level: confort
    evidence:
      - 'Observation: bruit grognement gemissement tournant volant'
      - Vérification visuelle ou auditive
  - id: S2
    label: Direction dure en man uvre a basse vitesse
    description: direction dure en man uvre a basse vitesse
    risk_level: securite
    evidence:
      - 'Observation: direction dure en man uvre a basse vitesse'
      - Vérification visuelle ou auditive
  - id: S3
    label: Sifflement aigu au demarrage qui s attenue
    description: sifflement aigu au demarrage qui s attenue
    risk_level: confort
    evidence:
      - 'Observation: sifflement aigu au demarrage qui s attenue'
      - Vérification visuelle ou auditive
  - id: S4
    label: Mousse ou bulles dans le bocal de liquide
    description: mousse ou bulles dans le bocal de liquide
    risk_level: confort
    evidence:
      - 'Observation: mousse ou bulles dans le bocal de liquide'
      - Vérification visuelle ou auditive
  - id: S5
    label: Fuite de liquide au niveau de la pompe
    description: fuite de liquide au niveau de la pompe
    risk_level: confort
    evidence:
      - 'Observation: fuite de liquide au niveau de la pompe'
      - Vérification visuelle ou auditive
  - id: S6
    label: Niveau de liquide qui baisse regulierement
    description: niveau de liquide qui baisse regulierement
    risk_level: confort
    evidence:
      - 'Observation: niveau de liquide qui baisse regulierement'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Pompe de direction assistée - Guide Diagnostic Complet

## Fonction et Rôle

Fournir la pression hydraulique pour assister l'effort de braquage - Reduit l'effort au volant

**Actions principales:** assister, fournir la pression, alimenter, reduire l'effort

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Direction dure en man uvre a basse vitesse**
  direction dure en man uvre a basse vitesse

### 🟢 Autres Symptômes

- bruit grognement gemissement tournant volant
- sifflement aigu au demarrage qui s attenue
- mousse ou bulles dans le bocal de liquide
- fuite de liquide au niveau de la pompe
- niveau de liquide qui baisse regulierement

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe de direction assistée:

1. **Inspection visuelle** - Examiner l'état du pompe de direction assistée
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- colonne-de-direction
- courroie-d-accessoire
- cremailliere-de-direction
- poulie-vilebrequin
- rotule-de-direction
- rotule-de-suspension

## Critères de Compatibilité

Pour commander le bon pompe de direction assistée, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"
