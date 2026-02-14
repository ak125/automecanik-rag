---
category: embrayage
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
  - actionner
  - pousser
  - deplacer
  must_not_contain_concepts:
  - injection
  - freinage
  - climatisation
  - turbo
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Actionner la butee d'embrayage via la commande
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "passage de vitesse parfait"
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
    question: Comment choisir Fourchette d'embrayage compatible avec mon vehicule
      ?
  - answer: En cas de pedale d embrayage dure ou de degradation mesurable, il faut
      controler rapidement avant panne secondaire.
    question: Quand remplacer Fourchette d'embrayage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Fourchette d'embrayage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Fourchette d'embrayage.
  id: 3419
  intro:
    role: Actionner la butee d'embrayage via la commande
    syncParts:
    - actionner
    - pousser
    - deplacer
    title: A quoi sert Fourchette d'embrayage ?
  pgId: '3419'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/fourchette-d-embrayage.md
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
    title: Pourquoi remplacer Fourchette d'embrayage a temps ?
  symptoms:
  - pedale d embrayage dure
  - difficulte a passer les vitesses
  - bruit de claquement a l embrayage
  - '**Bruit de claquement a l embrayage**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 3419
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: fourchette-d-embrayage
source_type: gamme
symptoms:
- description: pedale d embrayage dure
  evidence:
  - 'Observation: pedale d embrayage dure'
  - Vérification visuelle ou auditive
  id: S1
  label: Pedale d embrayage dure
  risk_level: confort
- description: difficulte a passer les vitesses
  evidence:
  - 'Observation: difficulte a passer les vitesses'
  - Vérification visuelle ou auditive
  id: S2
  label: Difficulte a passer les vitesses
  risk_level: confort
- description: bruit de claquement a l embrayage
  evidence:
  - 'Observation: bruit de claquement a l embrayage'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruit de claquement a l embrayage
  risk_level: degats_volant_moteur
title: Fourchette d'embrayage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Fourchette d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Actionner la butee d'embrayage via la commande

**Actions principales:** actionner, pousser, deplacer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement a l embrayage**
  bruit de claquement a l embrayage

### 🟢 Autres Symptômes

- pedale d embrayage dure
- difficulte a passer les vitesses

## Procédure de Diagnostic

Pour diagnostiquer un problème de fourchette d'embrayage:

1. **Inspection visuelle** - Examiner l'état du fourchette d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- guide-d-embrayage
- tringle-de-vitesses

## Critères de Compatibilité

Pour commander le bon fourchette d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passage de vitesse parfait"