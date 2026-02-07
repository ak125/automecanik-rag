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
  - if: symptome_rainures-profondes-visibles-interieur-tambour
    then: verifier_piece
  - if: symptome_diametre-interieur-au-dela-du-maximum-grave
    then: diagnostic_approfondi
  - if: symptome_bruit-de-frottement-ou-crissement-a
    then: remplacement_recommande
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
    label: Bruit de frottement ou crissement a
    description: bruit de frottement ou crissement a l arriere
    risk_level: confort
    evidence:
      - 'Observation: bruit de frottement ou crissement a'
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
    label: Frein a main inefficace malgre machoires
    description: frein a main inefficace malgre machoires neuves
    risk_level: securite
    evidence:
      - 'Observation: frein a main inefficace malgre machoires'
      - Vérification visuelle ou auditive
purchase_guardrails:
  requires_vehicle: true
  forbidden_terms:
    - universel
    - tous modèles
    - compatible tout véhicule
    - adaptable
---
# Tambour de frein - Guide Complet

## Fonction

Support interne de freinage par expansion des machoires

## Symptômes de défaillance

### Rainures profondes visibles interieur tambour

rainures profondes visibles interieur tambour

### Diametre interieur au-dela du maximum grave

diametre interieur au-dela du maximum grave

### Bruit de frottement ou crissement a

bruit de frottement ou crissement a l arriere

### Tambour ovalise vibrations au freinage arriere

tambour ovalise vibrations au freinage arriere

### Traces de surchauffe bleuissement du metal

traces de surchauffe bleuissement du metal

### Frein a main inefficace malgre machoires

frein a main inefficace malgre machoires neuves

## Diagnostic

Pour diagnostiquer un problème de tambour de frein:

1. **Inspection visuelle** - Vérifier l'état général de la pièce
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des connexions** - Vérifier les fixations et raccords

## Pièces associées

- cable-de-frein-a-main
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein

## Compatibilité

Pour commander le bon tambour de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## Attention aux fausses promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
