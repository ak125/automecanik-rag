---
category: electrique
diagnostic_tree:
- if: vehicule_immobilise_ou_symptome_critique
  then: verification_urgente_piece_et_alimentation
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - verrouiller
  - alimenter
  - securiser
  must_not_contain_concepts:
  - injection
  - climatisation
  - freinage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Verrouiller la direction et alimenter les circuits electriques
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "demarrage garanti"
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
    question: Comment choisir Neiman compatible avec mon vehicule ?
  - answer: En cas de tableau de bord qui ne s allume pas au contact ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Neiman ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Neiman sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de electrique pour confirmer Neiman.
  id: 1367
  intro:
    role: Verrouiller la direction et alimenter les circuits electriques
    syncParts:
    - verrouiller
    - alimenter
    - securiser
    title: A quoi sert Neiman ?
  pgId: '1367'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/neiman.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le neiman peut être hors service et nécessiter un remplacement'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le neiman peut être hors service et nécessiter un
      remplacement'
    title: Pourquoi remplacer Neiman a temps ?
  symptoms:
  - tableau de bord qui ne s allume pas au contact
  - cle qui tourne dans le vide sans effet
  - direction bloquee impossible a debloquer
  - contact electrique intermittent coupures
  - odeur de plastique brule court-circuit interne
  - difficulte recurrente a tourner la cle
  - '**Direction bloquee impossible a debloquer**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1367
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: neiman
source_type: gamme
symptoms:
- description: tableau de bord qui ne s allume pas au contact
  evidence:
  - 'Observation: tableau de bord qui ne s allume pas au contact'
  - Vérification visuelle ou auditive
  id: S1
  label: Tableau de bord qui ne s allume pas au contact
  risk_level: confort
- description: cle qui tourne dans le vide sans effet
  evidence:
  - 'Observation: cle qui tourne dans le vide sans effet'
  - Vérification visuelle ou auditive
  id: S2
  label: Cle qui tourne dans le vide sans effet
  risk_level: confort
- description: direction bloquee impossible a debloquer
  evidence:
  - 'Observation: direction bloquee impossible a debloquer'
  - Vérification visuelle ou auditive
  id: S3
  label: Direction bloquee impossible a debloquer
  risk_level: immobilisation
- description: contact electrique intermittent coupures
  evidence:
  - 'Observation: contact electrique intermittent coupures'
  - Vérification visuelle ou auditive
  id: S4
  label: Contact electrique intermittent coupures
  risk_level: confort
- description: odeur de plastique brule court-circuit interne
  evidence:
  - 'Observation: odeur de plastique brule court-circuit interne'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de plastique brule court-circuit interne
  risk_level: confort
- description: difficulte recurrente a tourner la cle
  evidence:
  - 'Observation: difficulte recurrente a tourner la cle'
  - Vérification visuelle ou auditive
  id: S6
  label: Difficulte recurrente a tourner la cle
  risk_level: confort
title: Neiman
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Neiman - Guide Diagnostic Complet

## Fonction et Rôle

Verrouiller la direction et alimenter les circuits electriques

**Actions principales:** verrouiller, alimenter, securiser

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Direction bloquee impossible a debloquer**
  direction bloquee impossible a debloquer

### 🟢 Autres Symptômes

- tableau de bord qui ne s allume pas au contact
- cle qui tourne dans le vide sans effet
- contact electrique intermittent coupures
- odeur de plastique brule court-circuit interne
- difficulte recurrente a tourner la cle

## Procédure de Diagnostic

Pour diagnostiquer un problème de neiman:

1. **Inspection visuelle** - Examiner l'état du neiman
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé

## Causes Probables

- **Pièce HS** - Le neiman peut être hors service et nécessiter un remplacement
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- colonne-de-direction
- demarreur

## Critères de Compatibilité

Pour commander le bon neiman, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "demarrage garanti"