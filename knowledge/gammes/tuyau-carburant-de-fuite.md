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
  - evacuer
  - retourner
  - canaliser
  must_not_contain_concepts:
  - freinage
  - climatisation
  - distribution
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Evacuer le carburant excedentaire des injecteurs vers le reservoir
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare l'injection"
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
    question: Comment choisir Tuyau carburant de fuite compatible avec mon vehicule
      ?
  - answer: En cas de odeur de gasoil dans le compartiment moteur ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Tuyau carburant de fuite ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Tuyau carburant de fuite sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Tuyau carburant
    de fuite.
  id: 3937
  intro:
    role: Evacuer le carburant excedentaire des injecteurs vers le reservoir
    syncParts:
    - evacuer
    - retourner
    - canaliser
    title: A quoi sert Tuyau carburant de fuite ?
  pgId: '3937'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/tuyau-carburant-de-fuite.md
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
    title: Pourquoi remplacer Tuyau carburant de fuite a temps ?
  symptoms:
  - odeur de gasoil dans le compartiment moteur
  - traces de carburant sur les injecteurs
  - surconsommation de carburant
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 3937
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: tuyau-carburant-de-fuite
source_type: gamme
symptoms:
- description: odeur de gasoil dans le compartiment moteur
  evidence:
  - 'Observation: odeur de gasoil dans le compartiment moteur'
  - Vérification visuelle ou auditive
  id: S1
  label: Odeur de gasoil dans le compartiment moteur
  risk_level: confort
- description: traces de carburant sur les injecteurs
  evidence:
  - 'Observation: traces de carburant sur les injecteurs'
  - Vérification visuelle ou auditive
  id: S2
  label: Traces de carburant sur les injecteurs
  risk_level: confort
- description: surconsommation de carburant
  evidence:
  - 'Observation: surconsommation de carburant'
  - Vérification visuelle ou auditive
  id: S3
  label: Surconsommation de carburant
  risk_level: confort
title: Tuyau carburant de fuite
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Tuyau carburant de fuite - Guide Diagnostic Complet

## Fonction et Rôle

Evacuer le carburant excedentaire des injecteurs vers le reservoir

**Actions principales:** evacuer, retourner, canaliser

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- odeur de gasoil dans le compartiment moteur
- traces de carburant sur les injecteurs
- surconsommation de carburant

## Procédure de Diagnostic

Pour diagnostiquer un problème de tuyau carburant de fuite:

1. **Inspection visuelle** - Examiner l'état du tuyau carburant de fuite
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- injecteur
- pompe-d-injection

## Critères de Compatibilité

Pour commander le bon tuyau carburant de fuite, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"