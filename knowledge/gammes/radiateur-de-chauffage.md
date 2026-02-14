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
  - chauffer
  - transferer
  - diffuser
  must_not_contain_concepts:
  - refroidissement moteur
  - ventilateur moteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transferer la chaleur du liquide de refroidissement vers l'habitacle
    pour le confort des passagers. NE REFROIDIT PAS LE MOTEUR!
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
    question: Comment choisir Radiateur de chauffage compatible avec mon vehicule
      ?
  - answer: En cas de buee grasse persistante sur le pare-brise ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Radiateur de chauffage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Radiateur de chauffage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Radiateur de chauffage.
  id: 467
  intro:
    role: Transferer la chaleur du liquide de refroidissement vers l'habitacle pour
      le confort des passagers. NE REFROIDIT PAS LE MOTEUR!
    syncParts:
    - chauffer
    - transferer
    - diffuser
    title: A quoi sert Radiateur de chauffage ?
  pgId: '467'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/radiateur-de-chauffage.md
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
    title: Pourquoi remplacer Radiateur de chauffage a temps ?
  symptoms:
  - buee grasse persistante sur le pare-brise
  - odeur sucree de liquide dans l habitacle
  - moquette humide cote passager avant
  - chauffage qui ne chauffe plus ou peu
  - gargouillement dans le tableau de bord
  - plus de 15 ans ou fuite averee
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 467
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: radiateur-de-chauffage
source_type: gamme
symptoms:
- description: buee grasse persistante sur le pare-brise
  evidence:
  - 'Observation: buee grasse persistante sur le pare-brise'
  - Vérification visuelle ou auditive
  id: S1
  label: Buee grasse persistante sur le pare-brise
  risk_level: confort
- description: odeur sucree de liquide dans l habitacle
  evidence:
  - 'Observation: odeur sucree de liquide dans l habitacle'
  - Vérification visuelle ou auditive
  id: S2
  label: Odeur sucree de liquide dans l habitacle
  risk_level: confort
- description: moquette humide cote passager avant
  evidence:
  - 'Observation: moquette humide cote passager avant'
  - Vérification visuelle ou auditive
  id: S3
  label: Moquette humide cote passager avant
  risk_level: confort
- description: chauffage qui ne chauffe plus ou peu
  evidence:
  - 'Observation: chauffage qui ne chauffe plus ou peu'
  - Vérification visuelle ou auditive
  id: S4
  label: Chauffage qui ne chauffe plus ou peu
  risk_level: confort
- description: gargouillement dans le tableau de bord
  evidence:
  - 'Observation: gargouillement dans le tableau de bord'
  - Vérification visuelle ou auditive
  id: S5
  label: Gargouillement dans le tableau de bord
  risk_level: confort
- description: plus de 15 ans ou fuite averee
  evidence:
  - 'Observation: plus de 15 ans ou fuite averee'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 15 ans ou fuite averee
  risk_level: confort
title: Radiateur de chauffage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Radiateur de chauffage - Guide Diagnostic Complet

## Fonction et Rôle

Transferer la chaleur du liquide de refroidissement vers l'habitacle pour le confort des passagers. NE REFROIDIT PAS LE MOTEUR!

**Actions principales:** chauffer, transferer, diffuser, rechauffer l'habitacle

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- buee grasse persistante sur le pare-brise
- odeur sucree de liquide dans l habitacle
- moquette humide cote passager avant
- chauffage qui ne chauffe plus ou peu
- gargouillement dans le tableau de bord
- plus de 15 ans ou fuite averee

## Procédure de Diagnostic

Pour diagnostiquer un problème de radiateur de chauffage:

1. **Inspection visuelle** - Examiner l'état du radiateur de chauffage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-de-ventilation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle
- radiateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon radiateur de chauffage, vous devez connaître:

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