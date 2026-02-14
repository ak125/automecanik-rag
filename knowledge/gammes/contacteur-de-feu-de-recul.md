---
category: eclairage
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
  - activer
  - signaler
  - commander
  must_not_contain_concepts:
  - injection
  - freinage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Active les feux de recul en marche arrière
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "sécurité maximale"
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
    question: Comment choisir Contacteur feu de recul compatible avec mon vehicule
      ?
  - answer: En cas de feux recul allument plus marche ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Contacteur feu de recul ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Contacteur feu de recul sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Contacteur feu
    de recul.
  id: 807
  intro:
    role: Active les feux de recul en marche arrière
    syncParts:
    - activer
    - signaler
    - commander
    title: A quoi sert Contacteur feu de recul ?
  pgId: '807'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/contacteur-de-feu-de-recul.md
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
    title: Pourquoi remplacer Contacteur feu de recul a temps ?
  symptoms:
  - feux recul allument plus marche
  - feux de recul toujours allumes moteur demarre
  - fuite huile visible niveau contacteur
  - camera de recul inactive car contacteur defaillant
  - odeur huile boite vitesses autour
  - claquement bruit passage marche arriere
  - difficulte enclencher marche arriere contacteur
  - contacteur place depuis plus controle
  - '**Claquement bruit passage marche arriere**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 807
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: contacteur-de-feu-de-recul
source_type: gamme
symptoms:
- description: feux recul allument plus marche
  evidence:
  - 'Observation: feux recul allument plus marche'
  - Vérification visuelle ou auditive
  id: S1
  label: Feux recul allument plus marche
  risk_level: confort
- description: feux de recul toujours allumes moteur demarre
  evidence:
  - 'Observation: feux de recul toujours allumes moteur demarre'
  - Vérification visuelle ou auditive
  id: S2
  label: Feux de recul toujours allumes moteur demarre
  risk_level: confort
- description: fuite huile visible niveau contacteur
  evidence:
  - 'Observation: fuite huile visible niveau contacteur'
  - Vérification visuelle ou auditive
  id: S3
  label: Fuite huile visible niveau contacteur
  risk_level: confort
- description: camera de recul inactive car contacteur defaillant
  evidence:
  - 'Observation: camera de recul inactive car contacteur defaillant'
  - Vérification visuelle ou auditive
  id: S4
  label: Camera de recul inactive car contacteur defaillant
  risk_level: confort
- description: odeur huile boite vitesses autour
  evidence:
  - 'Observation: odeur huile boite vitesses autour'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur huile boite vitesses autour
  risk_level: confort
- description: claquement bruit passage marche arriere
  evidence:
  - 'Observation: claquement bruit passage marche arriere'
  - Vérification visuelle ou auditive
  id: S6
  label: Claquement bruit passage marche arriere
  risk_level: degats_volant_moteur
- description: difficulte enclencher marche arriere contacteur
  evidence:
  - 'Observation: difficulte enclencher marche arriere contacteur'
  - Vérification visuelle ou auditive
  id: S7
  label: Difficulte enclencher marche arriere contacteur
  risk_level: confort
- description: contacteur place depuis plus controle
  evidence:
  - 'Observation: contacteur place depuis plus controle'
  - Vérification visuelle ou auditive
  id: S8
  label: Contacteur place depuis plus controle
  risk_level: confort
title: Contacteur feu de recul
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Contacteur feu de recul - Guide Diagnostic Complet

## Fonction et Rôle

Active les feux de recul en marche arrière

**Actions principales:** activer, signaler, commander

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement bruit passage marche arriere**
  claquement bruit passage marche arriere

### 🟢 Autres Symptômes

- feux recul allument plus marche
- feux de recul toujours allumes moteur demarre
- fuite huile visible niveau contacteur
- camera de recul inactive car contacteur defaillant
- odeur huile boite vitesses autour
- difficulte enclencher marche arriere contacteur

## Procédure de Diagnostic

Pour diagnostiquer un problème de contacteur feu de recul:

1. **Inspection visuelle** - Examiner l'état du contacteur feu de recul
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-arriere
- commande-d-eclairage
- feu-arriere
- feu-avant
- feu-clignotant

## Critères de Compatibilité

Pour commander le bon contacteur feu de recul, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "sécurité maximale"