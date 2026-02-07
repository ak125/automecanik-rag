---
entity_type: gamme
title: Câble de frein à main
slug: cable-de-frein-a-main
pg_id: 124
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Transmet la commande du frein de stationnement
  must_be_true:
    - transmettre
    - actionner
    - maintenir
  must_not_contain_concepts:
    - injection
    - climatisation
    - embrayage
    - distribution
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
    label: Frein a main qui ne tient plus en cote
    description: frein a main qui ne tient plus en cote
    risk_level: securite
    evidence:
      - 'Observation: frein a main qui ne tient plus en cote'
      - Vérification visuelle ou auditive
  - id: S2
    label: Course du levier excessive plus de 7 clics
    description: course du levier excessive plus de 7 clics
    risk_level: confort
    evidence:
      - 'Observation: course du levier excessive plus de 7 clics'
      - Vérification visuelle ou auditive
  - id: S3
    label: Vehicule roule alors frein main
    description: vehicule roule alors frein main
    risk_level: securite
    evidence:
      - 'Observation: vehicule roule alors frein main'
      - Vérification visuelle ou auditive
  - id: S4
    label: Cable visible effiloche ou rouille
    description: cable visible effiloche ou rouille
    risk_level: confort
    evidence:
      - 'Observation: cable visible effiloche ou rouille'
      - Vérification visuelle ou auditive
  - id: S5
    label: Bruit de frottement a l arriere en roulant
    description: bruit de frottement a l arriere en roulant
    risk_level: confort
    evidence:
      - 'Observation: bruit de frottement a l arriere en roulant'
      - Vérification visuelle ou auditive
  - id: S6
    label: Levier de frein a main mou ou sans resistance
    description: levier de frein a main mou ou sans resistance
    risk_level: securite
    evidence:
      - 'Observation: levier de frein a main mou ou sans resistance'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Câble de frein à main - Guide Diagnostic Complet

## Fonction et Rôle

Transmet la commande du frein de stationnement

**Actions principales:** transmettre, actionner, maintenir

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Frein a main qui ne tient plus en cote**
  frein a main qui ne tient plus en cote
- **Vehicule roule alors frein main**
  vehicule roule alors frein main
- **Levier de frein a main mou ou sans resistance**
  levier de frein a main mou ou sans resistance

### 🟢 Autres Symptômes

- course du levier excessive plus de 7 clics
- cable visible effiloche ou rouille
- bruit de frottement a l arriere en roulant

## Procédure de Diagnostic

Pour diagnostiquer un problème de câble de frein à main:

1. **Inspection visuelle** - Examiner l'état du câble de frein à main
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-abs
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere
- machoires-de-frein
- plaquette-de-frein
- tambour-de-frein

## Critères de Compatibilité

Pour commander le bon câble de frein à main, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur freinage"
