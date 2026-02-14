---
category: echappement
diagnostic_tree:
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
  - collecter
  - acheminer
  - rassembler
  must_not_contain_concepts:
  - fap
  - sonde lambda
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Collecte les gaz d'échappement sortant des cylindres et les achemine
    vers le catalyseur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "passe le controle technique"
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
    question: Comment choisir Collecteur d'échappement compatible avec mon vehicule
      ?
  - answer: En cas de bruit metallique demarrage diminue chaud ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Collecteur d'échappement ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Collecteur d'échappement sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Collecteur d'échappement.
  id: 1543
  intro:
    role: Collecte les gaz d'échappement sortant des cylindres et les achemine vers
      le catalyseur
    syncParts:
    - collecter
    - acheminer
    - rassembler
    title: A quoi sert Collecteur d'échappement ?
  pgId: '1543'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/collecteur-d-echappement.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Collecteur d'échappement a temps ?
  symptoms:
  - bruit metallique demarrage diminue chaud
  - odeur echappement habitacle sous capot
  - traces de suie noire autour du collecteur visuel
  - perte puissance mauvais rendement moteur
  - voyant moteur allume - codes sonde lambda visuel
  - controle technique refuse pollution excessive
  - '**Bruit metallique demarrage diminue chaud**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1543
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: collecteur-d-echappement
source_type: gamme
symptoms:
- description: bruit metallique demarrage diminue chaud
  evidence:
  - 'Observation: bruit metallique demarrage diminue chaud'
  - Vérification visuelle ou auditive
  id: S1
  label: Bruit metallique demarrage diminue chaud
  risk_level: degats_volant_moteur
- description: odeur echappement habitacle sous capot
  evidence:
  - 'Observation: odeur echappement habitacle sous capot'
  - Vérification visuelle ou auditive
  id: S2
  label: Odeur echappement habitacle sous capot
  risk_level: confort
- description: traces de suie noire autour du collecteur visuel
  evidence:
  - 'Observation: traces de suie noire autour du collecteur visuel'
  - Vérification visuelle ou auditive
  id: S3
  label: Traces de suie noire autour du collecteur visuel
  risk_level: confort
- description: perte puissance mauvais rendement moteur
  evidence:
  - 'Observation: perte puissance mauvais rendement moteur'
  - Vérification visuelle ou auditive
  id: S4
  label: Perte puissance mauvais rendement moteur
  risk_level: confort
- description: voyant moteur allume - codes sonde lambda visuel
  evidence:
  - 'Observation: voyant moteur allume - codes sonde lambda visuel'
  - Vérification visuelle ou auditive
  id: S5
  label: Voyant moteur allume - codes sonde lambda visuel
  risk_level: confort
- description: controle technique refuse pollution excessive
  evidence:
  - 'Observation: controle technique refuse pollution excessive'
  - Vérification visuelle ou auditive
  id: S6
  label: Controle technique refuse pollution excessive
  risk_level: confort
title: Collecteur d'échappement
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Collecteur d'échappement - Guide Diagnostic Complet

## Fonction et Rôle

Collecte les gaz d'échappement sortant des cylindres et les achemine vers le catalyseur

**Actions principales:** collecter, acheminer, rassembler

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit metallique demarrage diminue chaud**
  bruit metallique demarrage diminue chaud

### 🟢 Autres Symptômes

- odeur echappement habitacle sous capot
- traces de suie noire autour du collecteur visuel
- perte puissance mauvais rendement moteur
- voyant moteur allume - codes sonde lambda visuel
- controle technique refuse pollution excessive

## Procédure de Diagnostic

Pour diagnostiquer un problème de collecteur d'échappement:

1. **Inspection visuelle** - Examiner l'état du collecteur d'échappement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- joint-d-echappement
- catalyseur

## Critères de Compatibilité

Pour commander le bon collecteur d'échappement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passe le controle technique"