---
category: freinage
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
- if: kilometrage_eleve_ou_usure_visible
  then: remplacement_preventif_recommande
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - appliquer la pression
  - maintenir les plaquettes
  - serrer
  must_not_contain_concepts:
  - tambour
  - machoire
  - thermique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Appliquer la pression hydraulique sur les plaquettes
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "freinage direct"
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
    question: Comment choisir Étrier de frein compatible avec mon vehicule ?
  - answer: En cas de usure asymetrique plaquettes plus usee ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Étrier de frein ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Étrier de frein sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Étrier de frein.
  id: 78
  intro:
    role: Appliquer la pression hydraulique sur les plaquettes
    syncParts:
    - appliquer la pression
    - maintenir les plaquettes
    - serrer
    title: A quoi sert Étrier de frein ?
  pgId: '78'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/etrier-de-frein.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Étrier de frein a temps ?
  symptoms:
  - usure asymetrique plaquettes plus usee
  - vehicule qui tire d un cote au freinage
  - roue anormalement chaude apres roulage
  - fuite de liquide de frein au niveau de l etrier
  - pedale de frein dure ou spongieuse
  - bruit de frottement permanent piston grippe
  - '**Vehicule qui tire d un cote au freinage**'
  - '**Fuite de liquide de frein au niveau de l etrier**'
  - '**Pedale de frein dure ou spongieuse**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 78
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: etrier-de-frein
source_type: gamme
subcategory: etriers
symptoms:
- description: usure asymetrique plaquettes plus usee
  evidence:
  - 'Observation: usure asymetrique plaquettes plus usee'
  - Vérification visuelle ou auditive
  id: S1
  label: Usure asymetrique plaquettes plus usee
  risk_level: confort
- description: vehicule qui tire d un cote au freinage
  evidence:
  - 'Observation: vehicule qui tire d un cote au freinage'
  - Vérification visuelle ou auditive
  id: S2
  label: Vehicule qui tire d un cote au freinage
  risk_level: securite
- description: roue anormalement chaude apres roulage
  evidence:
  - 'Observation: roue anormalement chaude apres roulage'
  - Vérification visuelle ou auditive
  id: S3
  label: Roue anormalement chaude apres roulage
  risk_level: confort
- description: fuite de liquide de frein au niveau de l etrier
  evidence:
  - 'Observation: fuite de liquide de frein au niveau de l etrier'
  - Vérification visuelle ou auditive
  id: S4
  label: Fuite de liquide de frein au niveau de l etrier
  risk_level: securite
- description: pedale de frein dure ou spongieuse
  evidence:
  - 'Observation: pedale de frein dure ou spongieuse'
  - Vérification visuelle ou auditive
  id: S5
  label: Pedale de frein dure ou spongieuse
  risk_level: securite
- description: bruit de frottement permanent piston grippe
  evidence:
  - 'Observation: bruit de frottement permanent piston grippe'
  - Vérification visuelle ou auditive
  id: S6
  label: Bruit de frottement permanent piston grippe
  risk_level: confort
title: Étrier de frein
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Étrier de frein - Guide Diagnostic Complet

## Fonction et Rôle

Appliquer la pression hydraulique sur les plaquettes

**Actions principales:** appliquer la pression, maintenir les plaquettes, serrer, relacher, pincer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Vehicule qui tire d un cote au freinage**
  vehicule qui tire d un cote au freinage
- **Fuite de liquide de frein au niveau de l etrier**
  fuite de liquide de frein au niveau de l etrier
- **Pedale de frein dure ou spongieuse**
  pedale de frein dure ou spongieuse

### 🟢 Autres Symptômes

- usure asymetrique plaquettes plus usee
- roue anormalement chaude apres roulage
- bruit de frottement permanent piston grippe

## Procédure de Diagnostic

Pour diagnostiquer un problème de étrier de frein:

1. **Inspection visuelle** - Examiner l'état du étrier de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- disque-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins
- maitre-cylindre-de-frein
- plaquette-de-frein
- servo-frein

## Critères de Compatibilité

Pour commander le bon étrier de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage direct"