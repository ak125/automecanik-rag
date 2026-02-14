---
category: turbo
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
- if: kilometrage_eleve_ou_usure_visible
  then: remplacement_preventif_recommande
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - comprimer
  - suralimenter
  - pressuriser
  must_not_contain_concepts:
  - climatisation
  - freinage
  - distribution
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Comprime l'air d'admission grâce aux gaz d'échappement
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de puissance"
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
    question: Comment choisir Turbo compatible avec mon vehicule ?
  - answer: En cas de fumee bleue ou noire excessive a l echappement ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Turbo ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Turbo sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Turbo.
  id: 2234
  intro:
    role: Comprime l'air d'admission grâce aux gaz d'échappement
    syncParts:
    - comprimer
    - suralimenter
    - pressuriser
    title: A quoi sert Turbo ?
  pgId: '2234'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/turbo.md
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
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Turbo a temps ?
  symptoms:
  - fumee bleue ou noire excessive a l echappement
  - sifflement ou bruit metallique du turbo
  - perte de puissance importante a l acceleration
  - consommation d huile anormale 1l 1000km
  - voyant moteur allume codes p0234 p0299
  - jeu perceptible dans l axe du turbo
  - '**Sifflement ou bruit metallique du turbo**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 2234
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: turbo
source_type: gamme
symptoms:
- description: fumee bleue ou noire excessive a l echappement
  evidence:
  - 'Observation: fumee bleue ou noire excessive a l echappement'
  - Vérification visuelle ou auditive
  id: S1
  label: Fumee bleue ou noire excessive a l echappement
  risk_level: confort
- description: sifflement ou bruit metallique du turbo
  evidence:
  - 'Observation: sifflement ou bruit metallique du turbo'
  - Vérification visuelle ou auditive
  id: S2
  label: Sifflement ou bruit metallique du turbo
  risk_level: degats_volant_moteur
- description: perte de puissance importante a l acceleration
  evidence:
  - 'Observation: perte de puissance importante a l acceleration'
  - Vérification visuelle ou auditive
  id: S3
  label: Perte de puissance importante a l acceleration
  risk_level: confort
- description: consommation d huile anormale 1l 1000km
  evidence:
  - 'Observation: consommation d huile anormale 1l 1000km'
  - Vérification visuelle ou auditive
  id: S4
  label: Consommation d huile anormale 1l 1000km
  risk_level: confort
- description: voyant moteur allume codes p0234 p0299
  evidence:
  - 'Observation: voyant moteur allume codes p0234 p0299'
  - Vérification visuelle ou auditive
  id: S5
  label: Voyant moteur allume codes p0234 p0299
  risk_level: confort
- description: jeu perceptible dans l axe du turbo
  evidence:
  - 'Observation: jeu perceptible dans l axe du turbo'
  - Vérification visuelle ou auditive
  id: S6
  label: Jeu perceptible dans l axe du turbo
  risk_level: confort
title: Turbo
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Turbo - Guide Diagnostic Complet

## Fonction et Rôle

Comprime l'air d'admission grâce aux gaz d'échappement

**Actions principales:** comprimer, suralimenter, pressuriser

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Sifflement ou bruit metallique du turbo**
  sifflement ou bruit metallique du turbo

### 🟢 Autres Symptômes

- fumee bleue ou noire excessive a l echappement
- perte de puissance importante a l acceleration
- consommation d huile anormale 1l 1000km
- voyant moteur allume codes p0234 p0299
- jeu perceptible dans l axe du turbo

## Procédure de Diagnostic

Pour diagnostiquer un problème de turbo:

1. **Inspection visuelle** - Examiner l'état du turbo
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-de-pression-turbo
- filtre-a-air
- filtre-a-huile
- gaine-de-turbo
- intercooler
- valve-de-turbo
- vanne-egr

## Critères de Compatibilité

Pour commander le bon turbo, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"