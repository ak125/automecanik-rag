---
category: freinage
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: vibrations_anormales
  then: verifier_equilibrage_et_fixations
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
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
  role_summary: Support interne de freinage par expansion des machoires
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "freinage optimal"
  arguments:
  - content: Selection guidee par vehicule et references techniques.
    icon: check-circle
    title: Compatibilite verifiee
  - content: Un remplacement a temps limite les risques de panne secondaire.
    icon: shield-check
    title: Priorite securite
  - content: Le guide structure les controles avant commande.
    icon: clock
    title: Decision rapide
  - content: La verification des pieces associees reduit les retours atelier.
    icon: list-check
    title: Montage maitrise
  faq:
  - answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference
      exacte avant montage.
    question: Comment choisir Tambour de frein compatible avec mon vehicule ?
  - answer: En cas de rainures profondes visibles interieur tambour ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Tambour de frein ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Tambour de frein sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Tambour de frein.
  id: 123
  intro:
    role: Support interne de freinage par expansion des machoires
    syncParts:
    - recevoir la friction
    - contenir les machoires
    - ralentir la rotation
    title: A quoi sert Tambour de frein ?
  pgId: '123'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/tambour-de-frein.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Tambour de frein a temps ?
  symptoms:
  - rainures profondes visibles interieur tambour
  - diametre interieur au-dela du maximum grave
  - bruit de frottement ou crissement a l arriere
  - tambour ovalise vibrations au freinage arriere
  - traces de surchauffe bleuissement du metal
  - frein a main inefficace malgre machoires neuves
  - '**Tambour ovalise vibrations au freinage arriere**'
  - '**Frein a main inefficace malgre machoires neuves**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 123
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: tambour-de-frein
source_type: gamme
symptoms:
- description: rainures profondes visibles interieur tambour
  evidence:
  - 'Observation: rainures profondes visibles interieur tambour'
  - Vérification visuelle ou auditive
  id: S1
  label: Rainures profondes visibles interieur tambour
  risk_level: confort
- description: diametre interieur au-dela du maximum grave
  evidence:
  - 'Observation: diametre interieur au-dela du maximum grave'
  - Vérification visuelle ou auditive
  id: S2
  label: Diametre interieur au-dela du maximum grave
  risk_level: confort
- description: bruit de frottement ou crissement a l arriere
  evidence:
  - 'Observation: bruit de frottement ou crissement a l arriere'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruit de frottement ou crissement a l arriere
  risk_level: confort
- description: tambour ovalise vibrations au freinage arriere
  evidence:
  - 'Observation: tambour ovalise vibrations au freinage arriere'
  - Vérification visuelle ou auditive
  id: S4
  label: Tambour ovalise vibrations au freinage arriere
  risk_level: securite
- description: traces de surchauffe bleuissement du metal
  evidence:
  - 'Observation: traces de surchauffe bleuissement du metal'
  - Vérification visuelle ou auditive
  id: S5
  label: Traces de surchauffe bleuissement du metal
  risk_level: confort
- description: frein a main inefficace malgre machoires neuves
  evidence:
  - 'Observation: frein a main inefficace malgre machoires neuves'
  - Vérification visuelle ou auditive
  id: S6
  label: Frein a main inefficace malgre machoires neuves
  risk_level: securite
title: Tambour de frein
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
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