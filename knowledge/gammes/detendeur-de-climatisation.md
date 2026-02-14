---
category: climatisation
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
  - detendre
  - reguler
  - abaisser la pression
  must_not_contain_concepts:
  - injection
  - freinage
  - allumage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Détend le fluide frigorigène avant l'évaporateur
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
    question: Comment choisir Détendeur de climatisation compatible avec mon vehicule
      ?
  - answer: En cas de evaporateur qui givre anormalement ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Détendeur de climatisation ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Détendeur de climatisation sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de climatisation pour confirmer Détendeur de climatisation.
  id: 183
  intro:
    role: Détend le fluide frigorigène avant l'évaporateur
    syncParts:
    - detendre
    - reguler
    - abaisser la pression
    title: A quoi sert Détendeur de climatisation ?
  pgId: '183'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/detendeur-de-climatisation.md
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
    title: Pourquoi remplacer Détendeur de climatisation a temps ?
  symptoms:
  - evaporateur qui givre anormalement
  - refroidissement irregulier chaud puis froid
  - sifflement ou bruit de detente audible
  - compresseur qui cycle en permanence
  - odeur de gaz refrigerant dans l habitacle
  - clim qui fonctionne puis s arrete brusquement
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 183
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: detendeur-de-climatisation
source_type: gamme
symptoms:
- description: evaporateur qui givre anormalement
  evidence:
  - 'Observation: evaporateur qui givre anormalement'
  - Vérification visuelle ou auditive
  id: S1
  label: Evaporateur qui givre anormalement
  risk_level: confort
- description: refroidissement irregulier chaud puis froid
  evidence:
  - 'Observation: refroidissement irregulier chaud puis froid'
  - Vérification visuelle ou auditive
  id: S2
  label: Refroidissement irregulier chaud puis froid
  risk_level: confort
- description: sifflement ou bruit de detente audible
  evidence:
  - 'Observation: sifflement ou bruit de detente audible'
  - Vérification visuelle ou auditive
  id: S3
  label: Sifflement ou bruit de detente audible
  risk_level: confort
- description: compresseur qui cycle en permanence
  evidence:
  - 'Observation: compresseur qui cycle en permanence'
  - Vérification visuelle ou auditive
  id: S4
  label: Compresseur qui cycle en permanence
  risk_level: confort
- description: odeur de gaz refrigerant dans l habitacle
  evidence:
  - 'Observation: odeur de gaz refrigerant dans l habitacle'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de gaz refrigerant dans l habitacle
  risk_level: confort
- description: clim qui fonctionne puis s arrete brusquement
  evidence:
  - 'Observation: clim qui fonctionne puis s arrete brusquement'
  - Vérification visuelle ou auditive
  id: S6
  label: Clim qui fonctionne puis s arrete brusquement
  risk_level: confort
title: Détendeur de climatisation
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Détendeur de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Détend le fluide frigorigène avant l'évaporateur

**Actions principales:** detendre, reguler, abaisser la pression

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- evaporateur qui givre anormalement
- refroidissement irregulier chaud puis froid
- sifflement ou bruit de detente audible
- compresseur qui cycle en permanence
- odeur de gaz refrigerant dans l habitacle
- clim qui fonctionne puis s arrete brusquement

## Procédure de Diagnostic

Pour diagnostiquer un problème de détendeur de climatisation:

1. **Inspection visuelle** - Examiner l'état du détendeur de climatisation
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
- condenseur-de-climatisation
- evaporateur-de-climatisation
- filtre-d-habitacle

## Critères de Compatibilité

Pour commander le bon détendeur de climatisation, vous devez connaître:

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