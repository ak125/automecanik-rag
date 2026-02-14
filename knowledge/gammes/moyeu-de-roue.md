---
category: direction
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
  - supporter
  - fixer
  - transmettre
  must_not_contain_concepts:
  - direction
  - cremailliere
  - volant
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Supporter la roue et transmettre la rotation - Fixe la roue au roulement
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
    question: Comment choisir Moyeu de roue compatible avec mon vehicule ?
  - answer: En cas de jeu anormal de la roue ou de degradation mesurable, il faut
      controler rapidement avant panne secondaire.
    question: Quand remplacer Moyeu de roue ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Moyeu de roue sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Moyeu de roue.
  id: 653
  intro:
    role: Supporter la roue et transmettre la rotation - Fixe la roue au roulement
    syncParts:
    - supporter
    - fixer
    - transmettre
    title: A quoi sert Moyeu de roue ?
  pgId: '653'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/moyeu-de-roue.md
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
    title: Pourquoi remplacer Moyeu de roue a temps ?
  symptoms:
  - jeu anormal de la roue
  - vibrations a vitesse constante
  - bruits sourds en roulant
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 653
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: moyeu-de-roue
source_type: gamme
symptoms:
- description: jeu anormal de la roue
  evidence:
  - 'Observation: jeu anormal de la roue'
  - Vérification visuelle ou auditive
  id: S1
  label: Jeu anormal de la roue
  risk_level: confort
- description: vibrations a vitesse constante
  evidence:
  - 'Observation: vibrations a vitesse constante'
  - Vérification visuelle ou auditive
  id: S2
  label: Vibrations a vitesse constante
  risk_level: confort
- description: bruits sourds en roulant
  evidence:
  - 'Observation: bruits sourds en roulant'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruits sourds en roulant
  risk_level: confort
title: Moyeu de roue
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Moyeu de roue - Guide Diagnostic Complet

## Fonction et Rôle

Supporter la roue et transmettre la rotation - Fixe la roue au roulement

**Actions principales:** supporter, fixer, transmettre, recevoir la roue

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- jeu anormal de la roue
- vibrations a vitesse constante
- bruits sourds en roulant

## Procédure de Diagnostic

Pour diagnostiquer un problème de moyeu de roue:

1. **Inspection visuelle** - Examiner l'état du moyeu de roue
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- roulement-de-roue
- disque-de-frein

## Critères de Compatibilité

Pour commander le bon moyeu de roue, vous devez connaître:

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