---
category: climatisation
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - dissiper la chaleur
  must_not_contain_concepts:
  - radiateur moteur
  - refroidissement
  - eau
  - liquide
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Dissipe la chaleur du fluide frigorigene comprime - Distinct du radiateur
    moteur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "refroidit le moteur"
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
    question: Comment choisir Condenseur de climatisation compatible avec mon vehicule
      ?
  - answer: En cas de climatisation moins efficace qu avant ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Condenseur de climatisation ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Condenseur de climatisation sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de climatisation pour confirmer Condenseur de
    climatisation.
  id: 448
  intro:
    role: Condenseur de climatisation intervient directement sur climatisation du
      vehicule. Un choix conforme protege la froid et limite les pannes secondaires.
    syncParts:
    - dissiper la chaleur
    title: A quoi sert Condenseur de climatisation ?
  pgId: '448'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/condenseur-de-climatisation.md
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
    title: Pourquoi remplacer Condenseur de climatisation a temps ?
  symptoms:
  - climatisation moins efficace qu avant
  - recharges de gaz frequentes necessaires
  - traces d huile verdatre sur le condenseur
  - condenseur visiblement deforme ou perce
  - odeur de gaz refrigerant a l avant
  - choc frontal recent meme leger
  - bruit ventilateur condenseur tourne permanence
  - climatisation inefficace temps chaud embouteillages
  - plus controle circuit climatisation preventif
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 448
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: condenseur-de-climatisation
source_type: gamme
symptoms:
- description: climatisation moins efficace qu avant
  evidence:
  - 'Observation: climatisation moins efficace qu avant'
  - Vérification visuelle ou auditive
  id: S1
  label: Climatisation moins efficace qu avant
  risk_level: confort
- description: recharges de gaz frequentes necessaires
  evidence:
  - 'Observation: recharges de gaz frequentes necessaires'
  - Vérification visuelle ou auditive
  id: S2
  label: Recharges de gaz frequentes necessaires
  risk_level: confort
- description: traces d huile verdatre sur le condenseur
  evidence:
  - 'Observation: traces d huile verdatre sur le condenseur'
  - Vérification visuelle ou auditive
  id: S3
  label: Traces d huile verdatre sur le condenseur
  risk_level: confort
- description: condenseur visiblement deforme ou perce
  evidence:
  - 'Observation: condenseur visiblement deforme ou perce'
  - Vérification visuelle ou auditive
  id: S4
  label: Condenseur visiblement deforme ou perce
  risk_level: confort
- description: odeur de gaz refrigerant a l avant
  evidence:
  - 'Observation: odeur de gaz refrigerant a l avant'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de gaz refrigerant a l avant
  risk_level: confort
- description: choc frontal recent meme leger
  evidence:
  - 'Observation: choc frontal recent meme leger'
  - Vérification visuelle ou auditive
  id: S6
  label: Choc frontal recent meme leger
  risk_level: confort
- description: bruit ventilateur condenseur tourne permanence
  evidence:
  - 'Observation: bruit ventilateur condenseur tourne permanence'
  - Vérification visuelle ou auditive
  id: S7
  label: Bruit ventilateur condenseur tourne permanence
  risk_level: confort
- description: climatisation inefficace temps chaud embouteillages
  evidence:
  - 'Observation: climatisation inefficace temps chaud embouteillages'
  - Vérification visuelle ou auditive
  id: S8
  label: Climatisation inefficace temps chaud embouteillages
  risk_level: confort
- description: plus controle circuit climatisation preventif
  evidence:
  - 'Observation: plus controle circuit climatisation preventif'
  - Vérification visuelle ou auditive
  id: S9
  label: Plus controle circuit climatisation preventif
  risk_level: confort
title: Condenseur de climatisation
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Condenseur de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Dissipe la chaleur du fluide frigorigene comprime - Distinct du radiateur moteur

**Actions principales:** dissiper la chaleur

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- climatisation moins efficace qu avant
- recharges de gaz frequentes necessaires
- traces d huile verdatre sur le condenseur
- condenseur visiblement deforme ou perce
- odeur de gaz refrigerant a l avant
- choc frontal recent meme leger

## Procédure de Diagnostic

Pour diagnostiquer un problème de condenseur de climatisation:

1. **Inspection visuelle** - Examiner l'état du condenseur de climatisation
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bouteille-deshydratante
- commande-de-ventilation
- compresseur-de-climatisation
- detendeur-de-climatisation
- evaporateur-de-climatisation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle

## Critères de Compatibilité

Pour commander le bon condenseur de climatisation, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit le moteur"