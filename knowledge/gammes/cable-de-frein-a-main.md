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
  role_summary: Transmet la commande du frein de stationnement
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "meilleur freinage"
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
    question: Comment choisir Câble de frein à main compatible avec mon vehicule ?
  - answer: En cas de frein a main qui ne tient plus en cote ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Câble de frein à main ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Câble de frein à main sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Câble de frein à main.
  id: 124
  intro:
    role: Transmet la commande du frein de stationnement
    syncParts:
    - transmettre
    - actionner
    - maintenir
    title: A quoi sert Câble de frein à main ?
  pgId: '124'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/cable-de-frein-a-main.md
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
    title: Pourquoi remplacer Câble de frein à main a temps ?
  symptoms:
  - frein a main qui ne tient plus en cote
  - course du levier excessive plus de 7 clics
  - vehicule roule alors frein main
  - cable visible effiloche ou rouille
  - bruit de frottement a l arriere en roulant
  - levier de frein a main mou ou sans resistance
  - '**Frein a main qui ne tient plus en cote**'
  - '**Vehicule roule alors frein main**'
  - '**Levier de frein a main mou ou sans resistance**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 124
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: cable-de-frein-a-main
source_type: gamme
symptoms:
- description: frein a main qui ne tient plus en cote
  evidence:
  - 'Observation: frein a main qui ne tient plus en cote'
  - Vérification visuelle ou auditive
  id: S1
  label: Frein a main qui ne tient plus en cote
  risk_level: securite
- description: course du levier excessive plus de 7 clics
  evidence:
  - 'Observation: course du levier excessive plus de 7 clics'
  - Vérification visuelle ou auditive
  id: S2
  label: Course du levier excessive plus de 7 clics
  risk_level: confort
- description: vehicule roule alors frein main
  evidence:
  - 'Observation: vehicule roule alors frein main'
  - Vérification visuelle ou auditive
  id: S3
  label: Vehicule roule alors frein main
  risk_level: securite
- description: cable visible effiloche ou rouille
  evidence:
  - 'Observation: cable visible effiloche ou rouille'
  - Vérification visuelle ou auditive
  id: S4
  label: Cable visible effiloche ou rouille
  risk_level: confort
- description: bruit de frottement a l arriere en roulant
  evidence:
  - 'Observation: bruit de frottement a l arriere en roulant'
  - Vérification visuelle ou auditive
  id: S5
  label: Bruit de frottement a l arriere en roulant
  risk_level: confort
- description: levier de frein a main mou ou sans resistance
  evidence:
  - 'Observation: levier de frein a main mou ou sans resistance'
  - Vérification visuelle ou auditive
  id: S6
  label: Levier de frein a main mou ou sans resistance
  risk_level: securite
title: Câble de frein à main
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
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