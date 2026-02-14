---
category: alimentation
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
  - pressuriser
  - alimenter
  - comprimer
  must_not_contain_concepts:
  - basse pression
  - reservoir
  - air
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Mettre le carburant sous haute pression pour alimenter les injecteurs
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
    question: Comment choisir Pompe à injection compatible avec mon vehicule ?
  - answer: En cas de demarrage difficile ou de degradation mesurable, il faut controler
      rapidement avant panne secondaire.
    question: Quand remplacer Pompe à injection ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Pompe à injection sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Pompe à injection.
  id: 3904
  intro:
    role: Mettre le carburant sous haute pression pour alimenter les injecteurs
    syncParts:
    - pressuriser
    - alimenter
    - comprimer
    title: A quoi sert Pompe à injection ?
  pgId: '3904'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/pompe-a-injection.md
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
    title: Pourquoi remplacer Pompe à injection a temps ?
  symptoms:
  - demarrage difficile
  - perte de puissance
  - fumee
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 3904
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: pompe-a-injection
source_type: gamme
symptoms:
- description: demarrage difficile
  evidence:
  - 'Observation: demarrage difficile'
  - Vérification visuelle ou auditive
  id: S1
  label: Demarrage difficile
  risk_level: confort
- description: perte de puissance
  evidence:
  - 'Observation: perte de puissance'
  - Vérification visuelle ou auditive
  id: S2
  label: Perte de puissance
  risk_level: confort
- description: fumee
  evidence:
  - 'Observation: fumee'
  - Vérification visuelle ou auditive
  id: S3
  label: Fumee
  risk_level: confort
title: Pompe à injection
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Pompe à injection - Guide Diagnostic Complet

## Fonction et Rôle

Mettre le carburant sous haute pression pour alimenter les injecteurs

**Actions principales:** pressuriser, alimenter, comprimer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage difficile
- perte de puissance
- fumee

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à injection:

1. **Inspection visuelle** - Examiner l'état du pompe à injection
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-pression-de-carburant
- injecteur

## Critères de Compatibilité

Pour commander le bon pompe à injection, vous devez connaître:

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