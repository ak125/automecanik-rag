---
category: freinage
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - frotter
  - exercer une pression interne
  - s'user progressivement
  must_not_contain_concepts:
  - disque
  - plaquette
  - etrier
  - ventile
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Creer la friction a l'interieur du tambour
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "remplacement plaquettes"
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
    question: Comment choisir Mâchoires de frein compatible avec mon vehicule ?
  - answer: En cas de frein a main qui ne tient plus ou mal ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Mâchoires de frein ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Mâchoires de frein sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Mâchoires de frein.
  id: 70
  intro:
    role: Creer la friction a l'interieur du tambour
    syncParts:
    - frotter
    - exercer une pression interne
    - s'user progressivement
    title: A quoi sert Mâchoires de frein ?
  pgId: '70'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/machoires-de-frein.md
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
    title: Pourquoi remplacer Mâchoires de frein a temps ?
  symptoms:
  - frein a main qui ne tient plus ou mal
  - bruit de frottement metallique a l arriere
  - tambour raye ou strie a l interieur
  - epaisseur de garniture inferieure a 2mm
  - freinage arriere desequilibre tire d un cote
  - poussiere frein noire excessive jantes
  - '**Frein a main qui ne tient plus ou mal**'
  - '**Freinage arriere desequilibre tire d un cote**'
  - '**Poussiere frein noire excessive jantes**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 70
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: machoires-de-frein
source_type: gamme
symptoms:
- description: frein a main qui ne tient plus ou mal
  evidence:
  - 'Observation: frein a main qui ne tient plus ou mal'
  - Vérification visuelle ou auditive
  id: S1
  label: Frein a main qui ne tient plus ou mal
  risk_level: securite
- description: bruit de frottement metallique a l arriere
  evidence:
  - 'Observation: bruit de frottement metallique a l arriere'
  - Vérification visuelle ou auditive
  id: S2
  label: Bruit de frottement metallique a l arriere
  risk_level: confort
- description: tambour raye ou strie a l interieur
  evidence:
  - 'Observation: tambour raye ou strie a l interieur'
  - Vérification visuelle ou auditive
  id: S3
  label: Tambour raye ou strie a l interieur
  risk_level: confort
- description: epaisseur de garniture inferieure a 2mm
  evidence:
  - 'Observation: epaisseur de garniture inferieure a 2mm'
  - Vérification visuelle ou auditive
  id: S4
  label: Epaisseur de garniture inferieure a 2mm
  risk_level: confort
- description: freinage arriere desequilibre tire d un cote
  evidence:
  - 'Observation: freinage arriere desequilibre tire d un cote'
  - Vérification visuelle ou auditive
  id: S5
  label: Freinage arriere desequilibre tire d un cote
  risk_level: securite
- description: poussiere frein noire excessive jantes
  evidence:
  - 'Observation: poussiere frein noire excessive jantes'
  - Vérification visuelle ou auditive
  id: S6
  label: Poussiere frein noire excessive jantes
  risk_level: securite
title: Mâchoires de frein
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Mâchoires de frein - Guide Diagnostic Complet

## Fonction et Rôle

Creer la friction a l'interieur du tambour

**Actions principales:** frotter, exercer une pression interne, s'user progressivement, s'ecarter, plaquer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Frein a main qui ne tient plus ou mal**
  frein a main qui ne tient plus ou mal
- **Freinage arriere desequilibre tire d un cote**
  freinage arriere desequilibre tire d un cote
- **Poussiere frein noire excessive jantes**
  poussiere frein noire excessive jantes

### 🟢 Autres Symptômes

- bruit de frottement metallique a l arriere
- tambour raye ou strie a l interieur
- epaisseur de garniture inferieure a 2mm

## Procédure de Diagnostic

Pour diagnostiquer un problème de mâchoires de frein:

1. **Inspection visuelle** - Examiner l'état du mâchoires de frein
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
- flexible-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere
- maitre-cylindre-de-frein

## Critères de Compatibilité

Pour commander le bon mâchoires de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "remplacement plaquettes"