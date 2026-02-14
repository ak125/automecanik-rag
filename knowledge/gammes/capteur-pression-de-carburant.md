---
category: capteurs
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
  - mesurer
  - detecter
  - transmettre
  must_not_contain_concepts:
  - pompe
  - injecteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Mesurer la pression du carburant dans la rampe d'injection et transmettre
    l'information au calculateur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "corrige la panne"
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
    question: Comment choisir Capteur pression de carburant compatible avec mon vehicule
      ?
  - answer: En cas de perte de puissance a l acceleration ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Capteur pression de carburant ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Capteur pression de carburant sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Capteur pression
    de carburant.
  id: 817
  intro:
    role: Mesurer la pression du carburant dans la rampe d'injection et transmettre
      l'information au calculateur
    syncParts:
    - mesurer
    - detecter
    - transmettre
    title: A quoi sert Capteur pression de carburant ?
  pgId: '817'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/capteur-pression-de-carburant.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure normale** - Après un certain kilométrage, le remplacement
      préventif est recommandé'
    title: Pourquoi remplacer Capteur pression de carburant a temps ?
  symptoms:
  - perte de puissance a l acceleration
  - a-coups ou hesitations du moteur
  - cliquetis cognement moteur injection defaillante
  - voyant moteur avec codes p0190-p0194
  - odeur carburant anormale fuite mauvaise
  - plus de 150 000 km sur moteur diesel hdi tdi
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 817
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: capteur-pression-de-carburant
source_type: gamme
symptoms:
- description: perte de puissance a l acceleration
  evidence:
  - 'Observation: perte de puissance a l acceleration'
  - Vérification visuelle ou auditive
  id: S1
  label: Perte de puissance a l acceleration
  risk_level: confort
- description: a-coups ou hesitations du moteur
  evidence:
  - 'Observation: a-coups ou hesitations du moteur'
  - Vérification visuelle ou auditive
  id: S2
  label: A-coups ou hesitations du moteur
  risk_level: confort
- description: cliquetis cognement moteur injection defaillante
  evidence:
  - 'Observation: cliquetis cognement moteur injection defaillante'
  - Vérification visuelle ou auditive
  id: S3
  label: Cliquetis cognement moteur injection defaillante
  risk_level: confort
- description: voyant moteur avec codes p0190-p0194
  evidence:
  - 'Observation: voyant moteur avec codes p0190-p0194'
  - Vérification visuelle ou auditive
  id: S4
  label: Voyant moteur avec codes p0190-p0194
  risk_level: confort
- description: odeur carburant anormale fuite mauvaise
  evidence:
  - 'Observation: odeur carburant anormale fuite mauvaise'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur carburant anormale fuite mauvaise
  risk_level: confort
- description: plus de 150 000 km sur moteur diesel hdi tdi
  evidence:
  - 'Observation: plus de 150 000 km sur moteur diesel hdi tdi'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 150 000 km sur moteur diesel hdi tdi
  risk_level: confort
title: Capteur pression de carburant
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Capteur pression de carburant - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la pression du carburant dans la rampe d'injection et transmettre l'information au calculateur

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- perte de puissance a l acceleration
- a-coups ou hesitations du moteur
- cliquetis cognement moteur injection defaillante
- voyant moteur avec codes p0190-p0194
- odeur carburant anormale fuite mauvaise
- plus de 150 000 km sur moteur diesel hdi tdi

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur pression de carburant:

1. **Inspection visuelle** - Examiner l'état du capteur pression de carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-a-carburant
- pompe-a-injection

## Critères de Compatibilité

Pour commander le bon capteur pression de carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la panne"