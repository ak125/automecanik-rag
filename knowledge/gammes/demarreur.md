---
category: electrique
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
  confusion_with:
    alternateur:
      key_difference: Démarreur = lance le moteur (au démarrage), Alternateur = recharge
        batterie (moteur tournant)
    batterie:
      key_difference: Batterie faible peut simuler un démarreur HS - toujours tester
        la batterie d'abord
  must_be_true:
  - lancer le moteur
  - entrainer
  - demarrer
  must_not_contain_concepts:
  - charge
  - recharge
  - alimentation electrique
  - alternateur
  - universel
  - tous modèles
  - adaptable tous
  role_summary: Appliquer une rotation initiale au moteur pour declencher le demarrage
page_contract:
  antiMistakes:
  - ❌ "démarrage garanti"
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
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
    question: Comment choisir Démarreur compatible avec mon vehicule ?
  - answer: En cas de claquement contact demarrage solenoide ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Démarreur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Démarreur sans verification atelier ?
  howToChoose: Renseignez marque, modele, motorisation, type puis comparez references
    et dimensions. Validez ensuite les contraintes de electrique pour confirmer Démarreur.
  id: 2
  intro:
    role: Démarreur intervient directement sur electrique du vehicule. Un choix conforme
      protege la charge et limite les pannes secondaires.
    syncParts:
    - lancer le moteur
    - entrainer
    - demarrer
    title: A quoi sert Démarreur ?
  pgId: '2'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/demarreur.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le démarreur peut être hors service et nécessiter un remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "démarrage garanti"
    - ❌ "homologué CT"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le démarreur peut être hors service et nécessiter
      un remplacement'
    title: Pourquoi remplacer Démarreur a temps ?
  symptoms:
  - claquement contact demarrage solenoide
  - demarreur tourne mais moteur lance
  - aucune reaction au contact moteur electrique hs
  - grincement ou bruit anormal au demarrage
  - odeur de brule electrique au demarrage
  - plus demarrages difficiles recurrents
  - '**Aucune reaction au contact moteur electrique hs**'
  - '**Claquement contact demarrage solenoide**'
  - '**Grincement ou bruit anormal au demarrage**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 2
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - adaptable tous
  requires_vehicle: true
slug: demarreur
source_type: gamme
subcategory: demarrage
symptoms:
- description: claquement contact demarrage solenoide
  evidence:
  - 'Observation: claquement contact demarrage solenoide'
  - Vérification visuelle ou auditive
  id: S1
  label: Claquement contact demarrage solenoide
  risk_level: degats_volant_moteur
- description: demarreur tourne mais moteur lance
  evidence:
  - 'Observation: demarreur tourne mais moteur lance'
  - Vérification visuelle ou auditive
  id: S2
  label: Demarreur tourne mais moteur lance
  risk_level: confort
- description: aucune reaction au contact moteur electrique hs
  evidence:
  - 'Observation: aucune reaction au contact moteur electrique hs'
  - Vérification visuelle ou auditive
  id: S3
  label: Aucune reaction au contact moteur electrique hs
  risk_level: immobilisation
- description: grincement ou bruit anormal au demarrage
  evidence:
  - 'Observation: grincement ou bruit anormal au demarrage'
  - Vérification visuelle ou auditive
  id: S4
  label: Grincement ou bruit anormal au demarrage
  risk_level: degats_volant_moteur
- description: odeur de brule electrique au demarrage
  evidence:
  - 'Observation: odeur de brule electrique au demarrage'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de brule electrique au demarrage
  risk_level: confort
- description: plus demarrages difficiles recurrents
  evidence:
  - 'Observation: plus demarrages difficiles recurrents'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus demarrages difficiles recurrents
  risk_level: confort
title: Démarreur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Démarreur - Guide Diagnostic Complet

## Fonction et Rôle

Appliquer une rotation initiale au moteur pour declencher le demarrage

**Actions principales:** lancer le moteur, entrainer, demarrer, mettre en rotation, entrainer le vilebrequin

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Aucune reaction au contact moteur electrique hs**
  aucune reaction au contact moteur electrique hs

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement contact demarrage solenoide**
  claquement contact demarrage solenoide
- **Grincement ou bruit anormal au demarrage**
  grincement ou bruit anormal au demarrage

### 🟢 Autres Symptômes

- demarreur tourne mais moteur lance
- odeur de brule electrique au demarrage
- plus demarrages difficiles recurrents

## Procédure de Diagnostic

Pour diagnostiquer un problème de démarreur:

1. **Inspection visuelle** - Examiner l'état du démarreur
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le démarreur peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- neiman
- contacteur-demarreur

## ⚠️ Ne Pas Confondre Avec

### alternateur
**Distinction:** Démarreur = lance le moteur (au démarrage), Alternateur = recharge batterie (moteur tournant)

### batterie
**Distinction:** Batterie faible peut simuler un démarreur HS - toujours tester la batterie d'abord

## Critères de Compatibilité

Pour commander le bon démarreur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "démarrage garanti"
- ❌ "homologué CT"
- ❌ "sécurité garantie"