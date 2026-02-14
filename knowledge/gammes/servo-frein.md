---
category: freinage
diagnostic_tree:
- if: vehicule_immobilise_ou_symptome_critique
  then: verification_urgente_piece_et_alimentation
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
  - amplifier
  - assister
  - demultiplier
  must_not_contain_concepts:
  - injection
  - climatisation
  - embrayage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Amplifier l'effort de freinage grace a la depression moteur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "freinage garanti"
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
    question: Comment choisir Servo frein compatible avec mon vehicule ?
  - answer: En cas de pedale de frein tres dure a enfoncer ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Servo frein ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Servo frein sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Servo frein.
  id: 74
  intro:
    role: Amplifier l'effort de freinage grace a la depression moteur
    syncParts:
    - amplifier
    - assister
    - demultiplier
    title: A quoi sert Servo frein ?
  pgId: '74'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/servo-frein.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le servo frein peut être hors service et nécessiter un remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le servo frein peut être hors service et nécessiter
      un remplacement'
    title: Pourquoi remplacer Servo frein a temps ?
  symptoms:
  - pedale de frein tres dure a enfoncer
  - effort au freinage anormalement eleve
  - sifflement au niveau de la pedale
  - pedale qui vibre au freinage
  - moteur qui cale au freinage prise d air
  - '**Moteur qui cale au freinage prise d air**'
  - '**Pedale de frein tres dure a enfoncer**'
  - '**Effort au freinage anormalement eleve**'
  - '**Pedale qui vibre au freinage**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 74
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: servo-frein
source_type: gamme
symptoms:
- description: pedale de frein tres dure a enfoncer
  evidence:
  - 'Observation: pedale de frein tres dure a enfoncer'
  - Vérification visuelle ou auditive
  id: S1
  label: Pedale de frein tres dure a enfoncer
  risk_level: securite
- description: effort au freinage anormalement eleve
  evidence:
  - 'Observation: effort au freinage anormalement eleve'
  - Vérification visuelle ou auditive
  id: S2
  label: Effort au freinage anormalement eleve
  risk_level: securite
- description: sifflement au niveau de la pedale
  evidence:
  - 'Observation: sifflement au niveau de la pedale'
  - Vérification visuelle ou auditive
  id: S3
  label: Sifflement au niveau de la pedale
  risk_level: confort
- description: pedale qui vibre au freinage
  evidence:
  - 'Observation: pedale qui vibre au freinage'
  - Vérification visuelle ou auditive
  id: S4
  label: Pedale qui vibre au freinage
  risk_level: securite
- description: moteur qui cale au freinage prise d air
  evidence:
  - 'Observation: moteur qui cale au freinage prise d air'
  - Vérification visuelle ou auditive
  id: S5
  label: Moteur qui cale au freinage prise d air
  risk_level: immobilisation
title: Servo frein
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Servo frein - Guide Diagnostic Complet

## Fonction et Rôle

Amplifier l'effort de freinage grace a la depression moteur

**Actions principales:** amplifier, assister, demultiplier

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au freinage prise d air**
  moteur qui cale au freinage prise d air

### 🟡 Symptômes de Sécurité

- **Pedale de frein tres dure a enfoncer**
  pedale de frein tres dure a enfoncer
- **Effort au freinage anormalement eleve**
  effort au freinage anormalement eleve
- **Pedale qui vibre au freinage**
  pedale qui vibre au freinage

### 🟢 Autres Symptômes

- sifflement au niveau de la pedale

## Procédure de Diagnostic

Pour diagnostiquer un problème de servo frein:

1. **Inspection visuelle** - Examiner l'état du servo frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le servo frein peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes

## Pièces Associées

Lors du remplacement, vérifier également:

- agregat-de-freinage
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere

## Critères de Compatibilité

Pour commander le bon servo frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage garanti"