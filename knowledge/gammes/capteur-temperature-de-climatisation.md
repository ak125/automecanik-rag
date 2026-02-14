---
category: climatisation
diagnostic_tree:
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
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
  - injection
  - freinage
  - allumage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Mesurer la temperature de l'air dans l'habitacle
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "refroidit instantanement"
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
    question: Comment choisir Capteur température de climatisation compatible avec
      mon vehicule ?
  - answer: En cas de compresseur qui refuse de s enclencher ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Capteur température de climatisation ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Capteur température de climatisation sans verification
      atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de climatisation pour confirmer Capteur température
    de climatisation.
  id: 2054
  intro:
    role: Mesurer la temperature de l'air dans l'habitacle
    syncParts:
    - mesurer
    - detecter
    - transmettre
    title: A quoi sert Capteur température de climatisation ?
  pgId: '2054'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/capteur-temperature-de-climatisation.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Défaillance électrique** - Problème de connexion, de câblage ou
      de composant électronique'
    title: Pourquoi remplacer Capteur température de climatisation a temps ?
  symptoms:
  - compresseur qui refuse de s enclencher
  - climatisation qui givre l evaporateur
  - regulation automatique de temperature defaillante
  - voyant de climatisation qui clignote
  - code defaut capteur au diagnostic
  - temperature affichee incoherente
  - compresseur climatisation enclenche coupe boucle
  - temperature consigne jamais atteinte habitacle
  - givrage excessif evaporateur provoquant odeur
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 2054
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: capteur-temperature-de-climatisation
source_type: gamme
symptoms:
- description: compresseur qui refuse de s enclencher
  evidence:
  - 'Observation: compresseur qui refuse de s enclencher'
  - Vérification visuelle ou auditive
  id: S1
  label: Compresseur qui refuse de s enclencher
  risk_level: confort
- description: climatisation qui givre l evaporateur
  evidence:
  - 'Observation: climatisation qui givre l evaporateur'
  - Vérification visuelle ou auditive
  id: S2
  label: Climatisation qui givre l evaporateur
  risk_level: confort
- description: regulation automatique de temperature defaillante
  evidence:
  - 'Observation: regulation automatique de temperature defaillante'
  - Vérification visuelle ou auditive
  id: S3
  label: Regulation automatique de temperature defaillante
  risk_level: confort
- description: voyant de climatisation qui clignote
  evidence:
  - 'Observation: voyant de climatisation qui clignote'
  - Vérification visuelle ou auditive
  id: S4
  label: Voyant de climatisation qui clignote
  risk_level: confort
- description: code defaut capteur au diagnostic
  evidence:
  - 'Observation: code defaut capteur au diagnostic'
  - Vérification visuelle ou auditive
  id: S5
  label: Code defaut capteur au diagnostic
  risk_level: confort
- description: temperature affichee incoherente
  evidence:
  - 'Observation: temperature affichee incoherente'
  - Vérification visuelle ou auditive
  id: S6
  label: Temperature affichee incoherente
  risk_level: confort
- description: compresseur climatisation enclenche coupe boucle
  evidence:
  - 'Observation: compresseur climatisation enclenche coupe boucle'
  - Vérification visuelle ou auditive
  id: S7
  label: Compresseur climatisation enclenche coupe boucle
  risk_level: confort
- description: temperature consigne jamais atteinte habitacle
  evidence:
  - 'Observation: temperature consigne jamais atteinte habitacle'
  - Vérification visuelle ou auditive
  id: S8
  label: Temperature consigne jamais atteinte habitacle
  risk_level: confort
- description: givrage excessif evaporateur provoquant odeur
  evidence:
  - 'Observation: givrage excessif evaporateur provoquant odeur'
  - Vérification visuelle ou auditive
  id: S9
  label: Givrage excessif evaporateur provoquant odeur
  risk_level: confort
title: Capteur température de climatisation
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Capteur température de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la temperature de l'air dans l'habitacle

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- compresseur qui refuse de s enclencher
- climatisation qui givre l evaporateur
- regulation automatique de temperature defaillante
- voyant de climatisation qui clignote
- code defaut capteur au diagnostic
- temperature affichee incoherente

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur température de climatisation:

1. **Inspection visuelle** - Examiner l'état du capteur température de climatisation
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- evaporateur-de-climatisation
- compresseur-de-climatisation

## Critères de Compatibilité

Pour commander le bon capteur température de climatisation, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit instantanement"