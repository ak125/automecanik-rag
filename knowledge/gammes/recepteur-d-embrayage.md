---
category: embrayage
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
  - recevoir la pression
  - actionner la butée
  - pousser la fourchette
  must_not_contain_concepts:
  - disque
  - volant
  - couple
  - câble
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Recevoir la pression hydraulique et actionner la butée ou la fourchette
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "action parfaite"
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
    question: Comment choisir Récepteur d'embrayage compatible avec mon vehicule ?
  - answer: En cas de pedale d embrayage molle ou spongieuse ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Récepteur d'embrayage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Récepteur d'embrayage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Récepteur d'embrayage.
  id: 620
  intro:
    role: Recevoir la pression hydraulique et actionner la butée ou la fourchette
    syncParts:
    - recevoir la pression
    - actionner la butée
    - pousser la fourchette
    title: A quoi sert Récepteur d'embrayage ?
  pgId: '620'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/recepteur-d-embrayage.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le récepteur d''embrayage peut être hors service et nécessiter
      un remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le récepteur d''embrayage peut être hors service
      et nécessiter un remplacement'
    title: Pourquoi remplacer Récepteur d'embrayage a temps ?
  symptoms:
  - pedale d embrayage molle ou spongieuse
  - fuite de liquide visible sous la boite de vitesses
  - bruit de grincement au niveau de la fourchette
  - odeur de liquide de frein brule sous la voiture
  - embrayage qui ne debraye plus piston bloque
  - plus de 150 000 km sans verification du circuit
  - '**Embrayage qui ne debraye plus piston bloque**'
  - '**Bruit de grincement au niveau de la fourchette**'
  - '**Odeur de liquide de frein brule sous la voiture**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 620
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: recepteur-d-embrayage
source_type: gamme
symptoms:
- description: pedale d embrayage molle ou spongieuse
  evidence:
  - 'Observation: pedale d embrayage molle ou spongieuse'
  - Vérification visuelle ou auditive
  id: S1
  label: Pedale d embrayage molle ou spongieuse
  risk_level: confort
- description: fuite de liquide visible sous la boite de vitesses
  evidence:
  - 'Observation: fuite de liquide visible sous la boite de vitesses'
  - Vérification visuelle ou auditive
  id: S2
  label: Fuite de liquide visible sous la boite de vitesses
  risk_level: confort
- description: bruit de grincement au niveau de la fourchette
  evidence:
  - 'Observation: bruit de grincement au niveau de la fourchette'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruit de grincement au niveau de la fourchette
  risk_level: degats_volant_moteur
- description: odeur de liquide de frein brule sous la voiture
  evidence:
  - 'Observation: odeur de liquide de frein brule sous la voiture'
  - Vérification visuelle ou auditive
  id: S4
  label: Odeur de liquide de frein brule sous la voiture
  risk_level: securite
- description: embrayage qui ne debraye plus piston bloque
  evidence:
  - 'Observation: embrayage qui ne debraye plus piston bloque'
  - Vérification visuelle ou auditive
  id: S5
  label: Embrayage qui ne debraye plus piston bloque
  risk_level: immobilisation
- description: plus de 150 000 km sans verification du circuit
  evidence:
  - 'Observation: plus de 150 000 km sans verification du circuit'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 150 000 km sans verification du circuit
  risk_level: confort
title: Récepteur d'embrayage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Récepteur d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Recevoir la pression hydraulique et actionner la butée ou la fourchette

**Actions principales:** recevoir la pression, actionner la butée, pousser la fourchette, convertir

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Embrayage qui ne debraye plus piston bloque**
  embrayage qui ne debraye plus piston bloque

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de grincement au niveau de la fourchette**
  bruit de grincement au niveau de la fourchette

### 🟡 Symptômes de Sécurité

- **Odeur de liquide de frein brule sous la voiture**
  odeur de liquide de frein brule sous la voiture

### 🟢 Autres Symptômes

- pedale d embrayage molle ou spongieuse
- fuite de liquide visible sous la boite de vitesses
- plus de 150 000 km sans verification du circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de récepteur d'embrayage:

1. **Inspection visuelle** - Examiner l'état du récepteur d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le récepteur d'embrayage peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- butee-d-embrayage
- emetteur-d-embrayage
- kit-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon récepteur d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "action parfaite"