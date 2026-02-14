---
category: capteurs
diagnostic_tree:
- if: vehicule_immobilise_ou_symptome_critique
  then: verification_urgente_piece_et_alimentation
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - detecter
  - compter
  - transmettre
  must_not_contain_concepts:
  - reparation
  - regeneration
  - nettoyage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Detecter les impulsions du vilebrequin ou de l'arbre a cames
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "mesure parfaite"
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
    question: Comment choisir Capteur impulsion compatible avec mon vehicule ?
  - answer: En cas de moteur qui ne demarre pas du tout ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Capteur impulsion ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Capteur impulsion sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Capteur impulsion.
  id: 4813
  intro:
    role: Detecter les impulsions du vilebrequin ou de l'arbre a cames
    syncParts:
    - detecter
    - compter
    - transmettre
    title: A quoi sert Capteur impulsion ?
  pgId: '4813'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/capteur-impulsion.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le capteur impulsion peut être hors service et nécessiter un
      remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le capteur impulsion peut être hors service et nécessiter
      un remplacement'
    title: Pourquoi remplacer Capteur impulsion a temps ?
  symptoms:
  - moteur qui ne demarre pas du tout
  - calages repetes au ralenti ou en roulant
  - claquement ou rate d allumage
  - voyant moteur avec codes p0335 p0336
  - odeur d essence injection non synchronisee
  - plus demarrages difficiles recurrents
  - '**Moteur qui ne demarre pas du tout**'
  - '**Calages repetes au ralenti ou en roulant**'
  - '**Claquement ou rate d allumage**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 4813
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: capteur-impulsion
source_type: gamme
symptoms:
- description: moteur qui ne demarre pas du tout
  evidence:
  - 'Observation: moteur qui ne demarre pas du tout'
  - Vérification visuelle ou auditive
  id: S1
  label: Moteur qui ne demarre pas du tout
  risk_level: immobilisation
- description: calages repetes au ralenti ou en roulant
  evidence:
  - 'Observation: calages repetes au ralenti ou en roulant'
  - Vérification visuelle ou auditive
  id: S2
  label: Calages repetes au ralenti ou en roulant
  risk_level: immobilisation
- description: claquement ou rate d allumage
  evidence:
  - 'Observation: claquement ou rate d allumage'
  - Vérification visuelle ou auditive
  id: S3
  label: Claquement ou rate d allumage
  risk_level: degats_volant_moteur
- description: voyant moteur avec codes p0335 p0336
  evidence:
  - 'Observation: voyant moteur avec codes p0335 p0336'
  - Vérification visuelle ou auditive
  id: S4
  label: Voyant moteur avec codes p0335 p0336
  risk_level: confort
- description: odeur d essence injection non synchronisee
  evidence:
  - 'Observation: odeur d essence injection non synchronisee'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur d essence injection non synchronisee
  risk_level: confort
- description: plus demarrages difficiles recurrents
  evidence:
  - 'Observation: plus demarrages difficiles recurrents'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus demarrages difficiles recurrents
  risk_level: confort
title: Capteur impulsion
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Capteur impulsion - Guide Diagnostic Complet

## Fonction et Rôle

Detecter les impulsions du vilebrequin ou de l'arbre a cames

**Actions principales:** detecter, compter, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui ne demarre pas du tout**
  moteur qui ne demarre pas du tout
- **Calages repetes au ralenti ou en roulant**
  calages repetes au ralenti ou en roulant

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement ou rate d allumage**
  claquement ou rate d allumage

### 🟢 Autres Symptômes

- voyant moteur avec codes p0335 p0336
- odeur d essence injection non synchronisee
- plus demarrages difficiles recurrents

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur impulsion:

1. **Inspection visuelle** - Examiner l'état du capteur impulsion
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Pièce HS** - Le capteur impulsion peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-de-cognement
- capteur-impulsion
- poulie-d-arbre-a-came
- poulie-vilebrequin
- volant-moteur

## Critères de Compatibilité

Pour commander le bon capteur impulsion, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "mesure parfaite"