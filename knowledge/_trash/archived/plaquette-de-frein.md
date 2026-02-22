---
category: freinage
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
- if: kilometrage_eleve_ou_usure_visible
  then: remplacement_preventif_recommande
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with:
    disque-de-frein:
      key_difference: Plaquettes = garnitures qui s'usent, Disques = surfaces de friction
        à contrôler
    machoire-de-frein:
      key_difference: Plaquettes = freins à disque, Mâchoires = freins à tambour
  must_be_true:
  - freiner
  - creer la friction
  - ralentir le vehicule
  must_not_contain_concepts:
  - tambour
  - machoire
  - hydraulique
  - pression
  - universel
  - tous véhicules
  - adaptable tous
  role_summary: Creer la friction contre le disque pour ralentir le vehicule
page_contract:
  antiMistakes:
  - ❌ "sécurité garantie"
  - ❌ "arrêt immédiat"
  - ❌ "zéro accident"
  - ❌ "garanti CT"
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
    question: Comment choisir Plaquette de frein compatible avec mon vehicule ?
  - answer: En cas de sifflement metallique au freinage temoin d usure ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Plaquette de frein ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Plaquette de frein sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Plaquette de frein.
  id: 402
  intro:
    role: Creer la friction contre le disque pour ralentir le vehicule
    syncParts:
    - freiner
    - creer la friction
    - ralentir le vehicule
    title: A quoi sert Plaquette de frein ?
  pgId: '402'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/plaquette-de-frein.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "sécurité garantie"
    - ❌ "arrêt immédiat"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Plaquette de frein a temps ?
  symptoms:
  - sifflement metallique au freinage temoin d usure
  - voyant frein allume au tableau de bord
  - epaisseur visible inferieure travers jante
  - distances de freinage allongees
  - pedale de frein qui s enfonce plus que d habitude
  - plus de 30 000 km depuis le dernier changement
  - '**Sifflement metallique au freinage temoin d usure**'
  - '**Voyant frein allume au tableau de bord**'
  - '**Distances de freinage allongees**'
  - '**Pedale de frein qui s enfonce plus que d habitude**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 402
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous véhicules
  - adaptable tous
  requires_vehicle: true
slug: plaquette-de-frein
source_type: gamme
subcategory: plaquettes
symptoms:
- description: sifflement metallique au freinage temoin d usure
  evidence:
  - 'Observation: sifflement metallique au freinage temoin d usure'
  - Vérification visuelle ou auditive
  id: S1
  label: Sifflement metallique au freinage temoin d usure
  risk_level: securite
- description: voyant frein allume au tableau de bord
  evidence:
  - 'Observation: voyant frein allume au tableau de bord'
  - Vérification visuelle ou auditive
  id: S2
  label: Voyant frein allume au tableau de bord
  risk_level: securite
- description: epaisseur visible inferieure travers jante
  evidence:
  - 'Observation: epaisseur visible inferieure travers jante'
  - Vérification visuelle ou auditive
  id: S3
  label: Epaisseur visible inferieure travers jante
  risk_level: confort
- description: distances de freinage allongees
  evidence:
  - 'Observation: distances de freinage allongees'
  - Vérification visuelle ou auditive
  id: S4
  label: Distances de freinage allongees
  risk_level: securite
- description: pedale de frein qui s enfonce plus que d habitude
  evidence:
  - 'Observation: pedale de frein qui s enfonce plus que d habitude'
  - Vérification visuelle ou auditive
  id: S5
  label: Pedale de frein qui s enfonce plus que d habitude
  risk_level: securite
- description: plus de 30 000 km depuis le dernier changement
  evidence:
  - 'Observation: plus de 30 000 km depuis le dernier changement'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 30 000 km depuis le dernier changement
  risk_level: confort
title: Plaquette de frein
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Plaquette de frein - Guide Diagnostic Complet

## Fonction et Rôle

Creer la friction contre le disque pour ralentir le vehicule

**Actions principales:** freiner, creer la friction, ralentir le vehicule, presser le disque, s'user progressivement

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Sifflement metallique au freinage temoin d usure**
  sifflement metallique au freinage temoin d usure
- **Voyant frein allume au tableau de bord**
  voyant frein allume au tableau de bord
- **Distances de freinage allongees**
  distances de freinage allongees
- **Pedale de frein qui s enfonce plus que d habitude**
  pedale de frein qui s enfonce plus que d habitude

### 🟢 Autres Symptômes

- epaisseur visible inferieure travers jante
- plus de 30 000 km depuis le dernier changement

## Procédure de Diagnostic

Pour diagnostiquer un problème de plaquette de frein:

1. **Inspection visuelle** - Examiner l'état du plaquette de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins
- servo-frein
- temoin-d-usure

## ⚠️ Ne Pas Confondre Avec

### disque-de-frein
**Distinction:** Plaquettes = garnitures qui s'usent, Disques = surfaces de friction à contrôler

### machoire-de-frein
**Distinction:** Plaquettes = freins à disque, Mâchoires = freins à tambour

## Critères de Compatibilité

Pour commander le bon plaquette de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule
- **Position** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "sécurité garantie"
- ❌ "arrêt immédiat"
- ❌ "zéro accident"
- ❌ "garanti CT"