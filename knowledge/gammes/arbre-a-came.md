---
category: moteur
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
  - commander
  - synchroniser
  - actionner les soupapes
  must_not_contain_concepts:
  - vilebrequin
  - boite de vitesses
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Commander l'ouverture et la fermeture des soupapes
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare le moteur"
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
    question: Comment choisir Arbre à came compatible avec mon vehicule ?
  - answer: En cas de bruit moteur ou de degradation mesurable, il faut controler
      rapidement avant panne secondaire.
    question: Quand remplacer Arbre à came ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Arbre à came sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de moteur pour confirmer Arbre à came.
  id: 566
  intro:
    role: Arbre à came intervient directement sur moteur du vehicule. Un choix conforme
      protege la combustion et limite les pannes secondaires.
    syncParts:
    - commander
    - synchroniser
    - actionner les soupapes
    title: A quoi sert Arbre à came ?
  pgId: '566'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/arbre-a-came.md
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
    title: Pourquoi remplacer Arbre à came a temps ?
  symptoms:
  - bruit moteur
  - claquement
  - perte puissance
  - '**Claquement**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 566
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: arbre-a-came
source_type: gamme
symptoms:
- description: bruit moteur
  evidence:
  - 'Observation: bruit moteur'
  - Vérification visuelle ou auditive
  id: S1
  label: Bruit moteur
  risk_level: confort
- description: claquement
  evidence:
  - 'Observation: claquement'
  - Vérification visuelle ou auditive
  id: S2
  label: Claquement
  risk_level: degats_volant_moteur
- description: perte puissance
  evidence:
  - 'Observation: perte puissance'
  - Vérification visuelle ou auditive
  id: S3
  label: Perte puissance
  risk_level: confort
title: Arbre à came
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Arbre à came - Guide Diagnostic Complet

## Fonction et Rôle

Commander l'ouverture et la fermeture des soupapes

**Actions principales:** commander, synchroniser, actionner les soupapes

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement**
  claquement

### 🟢 Autres Symptômes

- bruit moteur
- perte puissance

## Procédure de Diagnostic

Pour diagnostiquer un problème de arbre à came:

1. **Inspection visuelle** - Examiner l'état du arbre à came
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-de-distribution
- culbuteur
- kit-de-poussoir-culbuteur
- poulie-d-arbre-a-came
- poussoir-de-soupape

## Critères de Compatibilité

Pour commander le bon arbre à came, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"