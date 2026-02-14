---
category: direction
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
  - diriger
  - guider
  - transmettre
  must_not_contain_concepts:
  - injection
  - freinage
  - distribution
  - turbo
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transforme la rotation du volant en déplacement des roues
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "meilleure tenue de route"
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
    question: Comment choisir Crémaillière de direction compatible avec mon vehicule
      ?
  - answer: En cas de fuite liquide direction visible sous ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Crémaillière de direction ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Crémaillière de direction sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Crémaillière de
    direction.
  id: 286
  intro:
    role: Transforme la rotation du volant en déplacement des roues
    syncParts:
    - diriger
    - guider
    - transmettre
    title: A quoi sert Crémaillière de direction ?
  pgId: '286'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/cremailliere-de-direction.md
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
    title: Pourquoi remplacer Crémaillière de direction a temps ?
  symptoms:
  - fuite liquide direction visible sous
  - direction dure ou assistance intermittente
  - jeu excessif dans le volant
  - bruit de grincement ou de couinement en tournant
  - soufflets de cremaillere fissures ou dechires
  - niveau de liquide de direction qui baisse
  - '**Bruit de grincement ou de couinement en tournant**'
  - '**Fuite liquide direction visible sous**'
  - '**Direction dure ou assistance intermittente**'
  - '**Niveau de liquide de direction qui baisse**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 286
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: cremailliere-de-direction
source_type: gamme
symptoms:
- description: fuite liquide direction visible sous
  evidence:
  - 'Observation: fuite liquide direction visible sous'
  - Vérification visuelle ou auditive
  id: S1
  label: Fuite liquide direction visible sous
  risk_level: securite
- description: direction dure ou assistance intermittente
  evidence:
  - 'Observation: direction dure ou assistance intermittente'
  - Vérification visuelle ou auditive
  id: S2
  label: Direction dure ou assistance intermittente
  risk_level: securite
- description: jeu excessif dans le volant
  evidence:
  - 'Observation: jeu excessif dans le volant'
  - Vérification visuelle ou auditive
  id: S3
  label: Jeu excessif dans le volant
  risk_level: confort
- description: bruit de grincement ou de couinement en tournant
  evidence:
  - 'Observation: bruit de grincement ou de couinement en tournant'
  - Vérification visuelle ou auditive
  id: S4
  label: Bruit de grincement ou de couinement en tournant
  risk_level: degats_volant_moteur
- description: soufflets de cremaillere fissures ou dechires
  evidence:
  - 'Observation: soufflets de cremaillere fissures ou dechires'
  - Vérification visuelle ou auditive
  id: S5
  label: Soufflets de cremaillere fissures ou dechires
  risk_level: confort
- description: niveau de liquide de direction qui baisse
  evidence:
  - 'Observation: niveau de liquide de direction qui baisse'
  - Vérification visuelle ou auditive
  id: S6
  label: Niveau de liquide de direction qui baisse
  risk_level: securite
title: Crémaillière de direction
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Crémaillière de direction - Guide Diagnostic Complet

## Fonction et Rôle

Transforme la rotation du volant en déplacement des roues

**Actions principales:** diriger, guider, transmettre

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de grincement ou de couinement en tournant**
  bruit de grincement ou de couinement en tournant

### 🟡 Symptômes de Sécurité

- **Fuite liquide direction visible sous**
  fuite liquide direction visible sous
- **Direction dure ou assistance intermittente**
  direction dure ou assistance intermittente
- **Niveau de liquide de direction qui baisse**
  niveau de liquide de direction qui baisse

### 🟢 Autres Symptômes

- jeu excessif dans le volant
- soufflets de cremaillere fissures ou dechires

## Procédure de Diagnostic

Pour diagnostiquer un problème de crémaillière de direction:

1. **Inspection visuelle** - Examiner l'état du crémaillière de direction
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- barre-de-direction
- bras-de-suspension
- colonne-de-direction
- pompe-de-direction-assistee
- rotule-de-direction
- rotule-de-suspension
- soufflet-de-direction

## Critères de Compatibilité

Pour commander le bon crémaillière de direction, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure tenue de route"