---
category: accessoires
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
  - fixer
  - serrer
  - maintenir
  must_not_contain_concepts:
  - frein
  - moyeu
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Fixe la roue sur le moyeu du véhicule
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "securite garantie"
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
    question: Comment choisir Boulon de roue compatible avec mon vehicule ?
  - answer: En cas de vibrations lors du freinage ou de degradation mesurable, il
      faut controler rapidement avant panne secondaire.
    question: Quand remplacer Boulon de roue ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Boulon de roue sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Boulon de roue.
  id: 657
  intro:
    role: Boulon de roue intervient directement sur compatibilite du vehicule. Un
      choix conforme protege la securite et limite les pannes secondaires.
    syncParts:
    - fixer
    - serrer
    - maintenir
    title: A quoi sert Boulon de roue ?
  pgId: '657'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/boulon-de-roue.md
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
    title: Pourquoi remplacer Boulon de roue a temps ?
  symptoms:
  - vibrations lors du freinage
  - roue qui emet des claquements
  - serrage impossible boulon tourne vide
  - '**Roue qui emet des claquements**'
  - '**Vibrations lors du freinage**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 657
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: boulon-de-roue
source_type: gamme
symptoms:
- description: vibrations lors du freinage
  evidence:
  - 'Observation: vibrations lors du freinage'
  - Vérification visuelle ou auditive
  id: S1
  label: Vibrations lors du freinage
  risk_level: securite
- description: roue qui emet des claquements
  evidence:
  - 'Observation: roue qui emet des claquements'
  - Vérification visuelle ou auditive
  id: S2
  label: Roue qui emet des claquements
  risk_level: degats_volant_moteur
- description: serrage impossible boulon tourne vide
  evidence:
  - 'Observation: serrage impossible boulon tourne vide'
  - Vérification visuelle ou auditive
  id: S3
  label: Serrage impossible boulon tourne vide
  risk_level: confort
title: Boulon de roue
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Boulon de roue - Guide Diagnostic Complet

## Fonction et Rôle

Fixe la roue sur le moyeu du véhicule

**Actions principales:** fixer, serrer, maintenir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Roue qui emet des claquements**
  roue qui emet des claquements

### 🟡 Symptômes de Sécurité

- **Vibrations lors du freinage**
  vibrations lors du freinage

### 🟢 Autres Symptômes

- serrage impossible boulon tourne vide

## Procédure de Diagnostic

Pour diagnostiquer un problème de boulon de roue:

1. **Inspection visuelle** - Examiner l'état du boulon de roue
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- jante
- moyeu

## Critères de Compatibilité

Pour commander le bon boulon de roue, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"