---
category: capteurs
diagnostic_tree:
- if: vehicule_immobilise_ou_symptome_critique
  then: verification_urgente_piece_et_alimentation
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
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
  - calorstat
  - thermostat
  - pompe a eau
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Mesurer la temperature du liquide de refroidissement et informer le
    calculateur pour le pilotage moteur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "corrige la surchauffe"
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
    question: Comment choisir Sonde de refroidissement compatible avec mon vehicule
      ?
  - answer: En cas de indicateur temperature bloque froid maximum ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Sonde de refroidissement ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Sonde de refroidissement sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Sonde de refroidissement.
  id: 830
  intro:
    role: Mesurer la temperature du liquide de refroidissement et informer le calculateur
      pour le pilotage moteur
    syncParts:
    - mesurer
    - detecter
    - transmettre
    title: A quoi sert Sonde de refroidissement ?
  pgId: '830'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/sonde-de-refroidissement.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le sonde de refroidissement peut être hors service et nécessiter
      un remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le sonde de refroidissement peut être hors service
      et nécessiter un remplacement'
    title: Pourquoi remplacer Sonde de refroidissement a temps ?
  symptoms:
  - indicateur temperature bloque froid maximum
  - ventilateur qui tourne en permanence ou jamais
  - bruit de ventilateur qui s emballe au demarrage
  - surconsommation et demarrage difficile a froid
  - odeur de liquide de refroidissement surchauffe
  - plus de 200 000 km sans controle du circuit
  - '**Indicateur temperature bloque froid maximum**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 830
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: sonde-de-refroidissement
source_type: gamme
symptoms:
- description: indicateur temperature bloque froid maximum
  evidence:
  - 'Observation: indicateur temperature bloque froid maximum'
  - Vérification visuelle ou auditive
  id: S1
  label: Indicateur temperature bloque froid maximum
  risk_level: immobilisation
- description: ventilateur qui tourne en permanence ou jamais
  evidence:
  - 'Observation: ventilateur qui tourne en permanence ou jamais'
  - Vérification visuelle ou auditive
  id: S2
  label: Ventilateur qui tourne en permanence ou jamais
  risk_level: confort
- description: bruit de ventilateur qui s emballe au demarrage
  evidence:
  - 'Observation: bruit de ventilateur qui s emballe au demarrage'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruit de ventilateur qui s emballe au demarrage
  risk_level: confort
- description: surconsommation et demarrage difficile a froid
  evidence:
  - 'Observation: surconsommation et demarrage difficile a froid'
  - Vérification visuelle ou auditive
  id: S4
  label: Surconsommation et demarrage difficile a froid
  risk_level: confort
- description: odeur de liquide de refroidissement surchauffe
  evidence:
  - 'Observation: odeur de liquide de refroidissement surchauffe'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de liquide de refroidissement surchauffe
  risk_level: confort
- description: plus de 200 000 km sans controle du circuit
  evidence:
  - 'Observation: plus de 200 000 km sans controle du circuit'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 200 000 km sans controle du circuit
  risk_level: confort
title: Sonde de refroidissement
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Sonde de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la temperature du liquide de refroidissement et informer le calculateur pour le pilotage moteur

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Indicateur temperature bloque froid maximum**
  indicateur temperature bloque froid maximum

### 🟢 Autres Symptômes

- ventilateur qui tourne en permanence ou jamais
- bruit de ventilateur qui s emballe au demarrage
- surconsommation et demarrage difficile a froid
- odeur de liquide de refroidissement surchauffe
- plus de 200 000 km sans controle du circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de sonde de refroidissement:

1. **Inspection visuelle** - Examiner l'état du sonde de refroidissement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le sonde de refroidissement peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-a-eau
- radiateur-de-refroidissement
- thermostat
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon sonde de refroidissement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la surchauffe"