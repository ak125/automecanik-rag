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
  - permettre la rotation
  - supporter
  - guider
  must_not_contain_concepts:
  - direction
  - cremailliere
  - volant
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Permettre la rotation libre de la roue sur son axe - Supporte les
    charges radiales et axiales
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
    question: Comment choisir Roulement de roue compatible avec mon vehicule ?
  - answer: En cas de ronronnement grondement augmente vitesse ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Roulement de roue ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Roulement de roue sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Roulement de roue.
  id: 655
  intro:
    role: Permettre la rotation libre de la roue sur son axe - Supporte les charges
      radiales et axiales
    syncParts:
    - permettre la rotation
    - supporter
    - guider
    title: A quoi sert Roulement de roue ?
  pgId: '655'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/roulement-de-roue.md
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
    title: Pourquoi remplacer Roulement de roue a temps ?
  symptoms:
  - ronronnement grondement augmente vitesse
  - bruit qui change d intensite dans les virages
  - jeu perceptible en secouant la roue montee
  - vibrations dans le volant a certaines vitesses
  - roue anormalement chaude apres roulage
  - bruit de frottement ou de craquement
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 655
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: roulement-de-roue
source_type: gamme
symptoms:
- description: ronronnement grondement augmente vitesse
  evidence:
  - 'Observation: ronronnement grondement augmente vitesse'
  - Vérification visuelle ou auditive
  id: S1
  label: Ronronnement grondement augmente vitesse
  risk_level: confort
- description: bruit qui change d intensite dans les virages
  evidence:
  - 'Observation: bruit qui change d intensite dans les virages'
  - Vérification visuelle ou auditive
  id: S2
  label: Bruit qui change d intensite dans les virages
  risk_level: confort
- description: jeu perceptible en secouant la roue montee
  evidence:
  - 'Observation: jeu perceptible en secouant la roue montee'
  - Vérification visuelle ou auditive
  id: S3
  label: Jeu perceptible en secouant la roue montee
  risk_level: confort
- description: vibrations dans le volant a certaines vitesses
  evidence:
  - 'Observation: vibrations dans le volant a certaines vitesses'
  - Vérification visuelle ou auditive
  id: S4
  label: Vibrations dans le volant a certaines vitesses
  risk_level: confort
- description: roue anormalement chaude apres roulage
  evidence:
  - 'Observation: roue anormalement chaude apres roulage'
  - Vérification visuelle ou auditive
  id: S5
  label: Roue anormalement chaude apres roulage
  risk_level: confort
- description: bruit de frottement ou de craquement
  evidence:
  - 'Observation: bruit de frottement ou de craquement'
  - Vérification visuelle ou auditive
  id: S6
  label: Bruit de frottement ou de craquement
  risk_level: confort
title: Roulement de roue
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Roulement de roue - Guide Diagnostic Complet

## Fonction et Rôle

Permettre la rotation libre de la roue sur son axe - Supporte les charges radiales et axiales

**Actions principales:** permettre la rotation, supporter, guider, rouler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- ronronnement grondement augmente vitesse
- bruit qui change d intensite dans les virages
- jeu perceptible en secouant la roue montee
- vibrations dans le volant a certaines vitesses
- roue anormalement chaude apres roulage
- bruit de frottement ou de craquement

## Procédure de Diagnostic

Pour diagnostiquer un problème de roulement de roue:

1. **Inspection visuelle** - Examiner l'état du roulement de roue
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-abs
- disque-de-frein
- plaquette-de-frein

## Critères de Compatibilité

Pour commander le bon roulement de roue, vous devez connaître:

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