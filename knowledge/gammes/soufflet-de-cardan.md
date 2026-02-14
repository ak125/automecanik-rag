---
category: transmission
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: vibrations_anormales
  then: verifier_equilibrage_et_fixations
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - proteger
  - etancher
  - contenir
  must_not_contain_concepts:
  - injection
  - freinage
  - climatisation
  - allumage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Protege le joint de cardan et retient la graisse de lubrification
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "transmission parfaite"
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
    question: Comment choisir Soufflet de Cardan compatible avec mon vehicule ?
  - answer: En cas de graisse noire visible sur la jante interieure ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Soufflet de Cardan ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Soufflet de Cardan sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de transmission pour confirmer Soufflet de Cardan.
  id: 193
  intro:
    role: Soufflet de Cardan intervient directement sur transmission du vehicule.
      Un choix conforme protege la couple et limite les pannes secondaires.
    syncParts:
    - proteger
    - etancher
    - contenir
    title: A quoi sert Soufflet de Cardan ?
  pgId: '193'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/soufflet-de-cardan.md
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
    title: Pourquoi remplacer Soufflet de Cardan a temps ?
  symptoms:
  - graisse noire visible sur la jante interieure
  - soufflet fendu dechire ou decolle visible
  - claquement en braquant joint deja endommage
  - odeur de graisse brulee pres de la roue
  - vibrations au volant a vitesse constante
  - plus controle visuel soufflets
  - '**Claquement en braquant joint deja endommage**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 193
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: soufflet-de-cardan
source_type: gamme
symptoms:
- description: graisse noire visible sur la jante interieure
  evidence:
  - 'Observation: graisse noire visible sur la jante interieure'
  - Vérification visuelle ou auditive
  id: S1
  label: Graisse noire visible sur la jante interieure
  risk_level: confort
- description: soufflet fendu dechire ou decolle visible
  evidence:
  - 'Observation: soufflet fendu dechire ou decolle visible'
  - Vérification visuelle ou auditive
  id: S2
  label: Soufflet fendu dechire ou decolle visible
  risk_level: confort
- description: claquement en braquant joint deja endommage
  evidence:
  - 'Observation: claquement en braquant joint deja endommage'
  - Vérification visuelle ou auditive
  id: S3
  label: Claquement en braquant joint deja endommage
  risk_level: degats_volant_moteur
- description: odeur de graisse brulee pres de la roue
  evidence:
  - 'Observation: odeur de graisse brulee pres de la roue'
  - Vérification visuelle ou auditive
  id: S4
  label: Odeur de graisse brulee pres de la roue
  risk_level: confort
- description: vibrations au volant a vitesse constante
  evidence:
  - 'Observation: vibrations au volant a vitesse constante'
  - Vérification visuelle ou auditive
  id: S5
  label: Vibrations au volant a vitesse constante
  risk_level: confort
- description: plus controle visuel soufflets
  evidence:
  - 'Observation: plus controle visuel soufflets'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus controle visuel soufflets
  risk_level: confort
title: Soufflet de Cardan
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Soufflet de Cardan - Guide Diagnostic Complet

## Fonction et Rôle

Protege le joint de cardan et retient la graisse de lubrification

**Actions principales:** proteger, etancher, contenir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement en braquant joint deja endommage**
  claquement en braquant joint deja endommage

### 🟢 Autres Symptômes

- graisse noire visible sur la jante interieure
- soufflet fendu dechire ou decolle visible
- odeur de graisse brulee pres de la roue
- vibrations au volant a vitesse constante
- plus controle visuel soufflets

## Procédure de Diagnostic

Pour diagnostiquer un problème de soufflet de cardan:

1. **Inspection visuelle** - Examiner l'état du soufflet de cardan
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cardan

## Critères de Compatibilité

Pour commander le bon soufflet de cardan, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "transmission parfaite"