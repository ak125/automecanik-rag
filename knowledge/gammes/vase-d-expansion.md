---
category: refroidissement
diagnostic_tree:
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
  - compenser
  - stocker
  - indiquer
  must_not_contain_concepts:
  - radiateur
  - pompe
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Compenser les variations de volume du liquide de refroidissement
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "evite la casse moteur"
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
    question: Comment choisir Vase d'expansion compatible avec mon vehicule ?
  - answer: En cas de fuite ou de degradation mesurable, il faut controler rapidement
      avant panne secondaire.
    question: Quand remplacer Vase d'expansion ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Vase d'expansion sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Vase d'expansion.
  id: 397
  intro:
    role: Compenser les variations de volume du liquide de refroidissement
    syncParts:
    - compenser
    - stocker
    - indiquer
    title: A quoi sert Vase d'expansion ?
  pgId: '397'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/vase-d-expansion.md
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
    title: Pourquoi remplacer Vase d'expansion a temps ?
  symptoms:
  - fuite
  - fissure
  - niveau bas
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 397
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: vase-d-expansion
source_type: gamme
symptoms:
- description: fuite
  evidence:
  - 'Observation: fuite'
  - Vérification visuelle ou auditive
  id: S1
  label: Fuite
  risk_level: confort
- description: fissure
  evidence:
  - 'Observation: fissure'
  - Vérification visuelle ou auditive
  id: S2
  label: Fissure
  risk_level: confort
- description: niveau bas
  evidence:
  - 'Observation: niveau bas'
  - Vérification visuelle ou auditive
  id: S3
  label: Niveau bas
  risk_level: confort
title: Vase d'expansion
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Vase d'expansion - Guide Diagnostic Complet

## Fonction et Rôle

Compenser les variations de volume du liquide de refroidissement

**Actions principales:** compenser, stocker, indiquer, reguler la pression

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- fuite
- fissure
- niveau bas

## Procédure de Diagnostic

Pour diagnostiquer un problème de vase d'expansion:

1. **Inspection visuelle** - Examiner l'état du vase d'expansion
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bouchon-vase-d-expansion

## Critères de Compatibilité

Pour commander le bon vase d'expansion, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "evite la casse moteur"