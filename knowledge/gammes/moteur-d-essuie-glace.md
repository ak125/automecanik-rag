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
  - entrainer
  - actionner
  - alimenter
  must_not_contain_concepts:
  - balai
  - caoutchouc
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Entraîne le mécanisme d'essuyage via la tringlerie
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
    question: Comment choisir Moteur d'essuie-glace compatible avec mon vehicule ?
  - answer: En cas de essuie-glaces totalement inactifs ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Moteur d'essuie-glace ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Moteur d'essuie-glace sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Moteur d'essuie-glace.
  id: 295
  intro:
    role: Entraîne le mécanisme d'essuyage via la tringlerie
    syncParts:
    - entrainer
    - actionner
    - alimenter
    title: A quoi sert Moteur d'essuie-glace ?
  pgId: '295'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/moteur-d-essuie-glace.md
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
    title: Pourquoi remplacer Moteur d'essuie-glace a temps ?
  symptoms:
  - essuie-glaces totalement inactifs
  - mouvement tres lent
  - arret en position aleatoire
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 295
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: moteur-d-essuie-glace
source_type: gamme
symptoms:
- description: essuie-glaces totalement inactifs
  evidence:
  - 'Observation: essuie-glaces totalement inactifs'
  - Vérification visuelle ou auditive
  id: S1
  label: Essuie-glaces totalement inactifs
  risk_level: confort
- description: mouvement tres lent
  evidence:
  - 'Observation: mouvement tres lent'
  - Vérification visuelle ou auditive
  id: S2
  label: Mouvement tres lent
  risk_level: confort
- description: arret en position aleatoire
  evidence:
  - 'Observation: arret en position aleatoire'
  - Vérification visuelle ou auditive
  id: S3
  label: Arret en position aleatoire
  risk_level: confort
title: Moteur d'essuie-glace
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Moteur d'essuie-glace - Guide Diagnostic Complet

## Fonction et Rôle

Entraîne le mécanisme d'essuyage via la tringlerie

**Actions principales:** entrainer, actionner, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- essuie-glaces totalement inactifs
- mouvement tres lent
- arret en position aleatoire

## Procédure de Diagnostic

Pour diagnostiquer un problème de moteur d'essuie-glace:

1. **Inspection visuelle** - Examiner l'état du moteur d'essuie-glace
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- tringlerie
- bras
- balai

## Critères de Compatibilité

Pour commander le bon moteur d'essuie-glace, vous devez connaître:

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