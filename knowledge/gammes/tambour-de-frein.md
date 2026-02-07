---
entity_type: gamme
title: Tambour de frein
slug: tambour-de-frein
pg_id: 123
category: freinage
truth_level: L2
verification_status: draft
updated_at: '2026-01-14'
intent_targets:
  - diagnostic
  - achat
  - compatibilite
mechanical_rules:
  role_summary: Support interne de freinage par expansion des machoires
  must_be_true:
    - recevoir la friction
    - contenir les machoires
    - ralentir la rotation
  must_not_contain_concepts:
    - disque
    - plaquette
    - etrier
    - ventile
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
  confusion_with: {}
diagnostic_tree:
  - if: bruit_anormal_detecte
    then: localiser_source_et_verifier_usure_mecanique
  - if: vibrations_anormales
    then: verifier_equilibrage_et_fixations
symptoms:
  - id: S1
    label: Rainures profondes visibles interieur tambour
    description: rainures profondes visibles interieur tambour
    risk_level: confort
    evidence:
      - 'Observation: rainures profondes visibles interieur tambour'
      - Vérification visuelle ou auditive
  - id: S2
    label: Diametre interieur au-dela du maximum grave
    description: diametre interieur au-dela du maximum grave
    risk_level: confort
    evidence:
      - 'Observation: diametre interieur au-dela du maximum grave'
      - Vérification visuelle ou auditive
  - id: S3
    label: Bruit de frottement ou crissement a l arriere
    description: bruit de frottement ou crissement a l arriere
    risk_level: confort
    evidence:
      - 'Observation: bruit de frottement ou crissement a l arriere'
      - Vérification visuelle ou auditive
  - id: S4
    label: Tambour ovalise vibrations au freinage arriere
    description: tambour ovalise vibrations au freinage arriere
    risk_level: securite
    evidence:
      - 'Observation: tambour ovalise vibrations au freinage arriere'
      - Vérification visuelle ou auditive
  - id: S5
    label: Traces de surchauffe bleuissement du metal
    description: traces de surchauffe bleuissement du metal
    risk_level: confort
    evidence:
      - 'Observation: traces de surchauffe bleuissement du metal'
      - Vérification visuelle ou auditive
  - id: S6
    label: Frein a main inefficace malgre machoires neuves
    description: frein a main inefficace malgre machoires neuves
    risk_level: securite
    evidence:
      - 'Observation: frein a main inefficace malgre machoires neuves'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Tambour de frein - Guide Diagnostic Complet

## Fonction et Rôle

Support interne de freinage par expansion des machoires

**Actions principales:** recevoir la friction, contenir les machoires, ralentir la rotation, tourner, enfermer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Tambour ovalise vibrations au freinage arriere**
  tambour ovalise vibrations au freinage arriere
- **Frein a main inefficace malgre machoires neuves**
  frein a main inefficace malgre machoires neuves

### 🟢 Autres Symptômes

- rainures profondes visibles interieur tambour
- diametre interieur au-dela du maximum grave
- bruit de frottement ou crissement a l arriere
- traces de surchauffe bleuissement du metal

## Procédure de Diagnostic

Pour diagnostiquer un problème de tambour de frein:

1. **Inspection visuelle** - Examiner l'état du tambour de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere
- machoires-de-frein

## Critères de Compatibilité

Pour commander le bon tambour de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage optimal"
