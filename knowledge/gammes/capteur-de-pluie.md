---
category: accessoires
diagnostic_tree:
- if: symptome_general_detecte
  then: inspection_visuelle_et_test_fonctionnel
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
  - mesurer
  - analyser
  must_not_contain_concepts:
  - balai
  - moteur essuie-glace
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Détecte la présence d'eau sur le pare-brise pour activer automatiquement
    les essuie-glaces
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "visibilite parfaite"
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
    question: Comment choisir Capteur de pluie compatible avec mon vehicule ?
  - answer: En cas de essuie-glaces declenches sans pluie ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Capteur de pluie ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Capteur de pluie sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Capteur de pluie.
  id: 2275
  intro:
    role: Détecte la présence d'eau sur le pare-brise pour activer automatiquement
      les essuie-glaces
    syncParts:
    - detecter
    - mesurer
    - analyser
    title: A quoi sert Capteur de pluie ?
  pgId: '2275'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/capteur-de-pluie.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Défaillance progressive** - Usure normale due à l''utilisation'
    title: Pourquoi remplacer Capteur de pluie a temps ?
  symptoms:
  - essuie-glaces declenches sans pluie
  - essuie-glaces automatiques inactifs
  - vitesse d essuyage inadaptee a l intensite
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 2275
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: capteur-de-pluie
source_type: gamme
symptoms:
- description: essuie-glaces declenches sans pluie
  evidence:
  - 'Observation: essuie-glaces declenches sans pluie'
  - Vérification visuelle ou auditive
  id: S1
  label: Essuie-glaces declenches sans pluie
  risk_level: confort
- description: essuie-glaces automatiques inactifs
  evidence:
  - 'Observation: essuie-glaces automatiques inactifs'
  - Vérification visuelle ou auditive
  id: S2
  label: Essuie-glaces automatiques inactifs
  risk_level: confort
- description: vitesse d essuyage inadaptee a l intensite
  evidence:
  - 'Observation: vitesse d essuyage inadaptee a l intensite'
  - Vérification visuelle ou auditive
  id: S3
  label: Vitesse d essuyage inadaptee a l intensite
  risk_level: confort
title: Capteur de pluie
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Capteur de pluie - Guide Diagnostic Complet

## Fonction et Rôle

Détecte la présence d'eau sur le pare-brise pour activer automatiquement les essuie-glaces

**Actions principales:** detecter, mesurer, analyser

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- essuie-glaces declenches sans pluie
- essuie-glaces automatiques inactifs
- vitesse d essuyage inadaptee a l intensite

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur de pluie:

1. **Inspection visuelle** - Examiner l'état du capteur de pluie
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- moteur-d-essuie-glace
- commande-essuie-glace
- balai-d-essuie-glace

## Critères de Compatibilité

Pour commander le bon capteur de pluie, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"