---
category: freinage
diagnostic_tree:
- if: vehicule_immobilise_ou_symptome_critique
  then: verification_urgente_piece_et_alimentation
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
  - repartir
  - distribuer
  - equilibrer
  must_not_contain_concepts:
  - injection
  - climatisation
  - embrayage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Repartir la pression de freinage entre les essieux
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "freinage garanti"
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
    question: Comment choisir Répartiteur de frein compatible avec mon vehicule ?
  - answer: En cas de roues arriere qui bloquent trop tot au freinage ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Répartiteur de frein ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Répartiteur de frein sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Répartiteur de frein.
  id: 73
  intro:
    role: Repartir la pression de freinage entre les essieux
    syncParts:
    - repartir
    - distribuer
    - equilibrer
    title: A quoi sert Répartiteur de frein ?
  pgId: '73'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/repartiteur-de-frein.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le répartiteur de frein peut être hors service et nécessiter
      un remplacement'
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le répartiteur de frein peut être hors service et
      nécessiter un remplacement'
    title: Pourquoi remplacer Répartiteur de frein a temps ?
  symptoms:
  - roues arriere qui bloquent trop tot au freinage
  - freinage desequilibre avant arriere
  - fuite au niveau du repartiteur
  - echec au controle technique desequilibre
  - desequilibre freinage controle technique valeurs
  - '**Roues arriere qui bloquent trop tot au freinage**'
  - '**Freinage desequilibre avant arriere**'
  - '**Desequilibre freinage controle technique valeurs**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 73
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: repartiteur-de-frein
source_type: gamme
symptoms:
- description: roues arriere qui bloquent trop tot au freinage
  evidence:
  - 'Observation: roues arriere qui bloquent trop tot au freinage'
  - Vérification visuelle ou auditive
  id: S1
  label: Roues arriere qui bloquent trop tot au freinage
  risk_level: immobilisation
- description: freinage desequilibre avant arriere
  evidence:
  - 'Observation: freinage desequilibre avant arriere'
  - Vérification visuelle ou auditive
  id: S2
  label: Freinage desequilibre avant arriere
  risk_level: securite
- description: fuite au niveau du repartiteur
  evidence:
  - 'Observation: fuite au niveau du repartiteur'
  - Vérification visuelle ou auditive
  id: S3
  label: Fuite au niveau du repartiteur
  risk_level: confort
- description: echec au controle technique desequilibre
  evidence:
  - 'Observation: echec au controle technique desequilibre'
  - Vérification visuelle ou auditive
  id: S4
  label: Echec au controle technique desequilibre
  risk_level: confort
- description: desequilibre freinage controle technique valeurs
  evidence:
  - 'Observation: desequilibre freinage controle technique valeurs'
  - Vérification visuelle ou auditive
  id: S5
  label: Desequilibre freinage controle technique valeurs
  risk_level: securite
title: Répartiteur de frein
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Répartiteur de frein - Guide Diagnostic Complet

## Fonction et Rôle

Repartir la pression de freinage entre les essieux

**Actions principales:** repartir, distribuer, equilibrer

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Roues arriere qui bloquent trop tot au freinage**
  roues arriere qui bloquent trop tot au freinage

### 🟡 Symptômes de Sécurité

- **Freinage desequilibre avant arriere**
  freinage desequilibre avant arriere
- **Desequilibre freinage controle technique valeurs**
  desequilibre freinage controle technique valeurs

### 🟢 Autres Symptômes

- fuite au niveau du repartiteur
- echec au controle technique desequilibre

## Procédure de Diagnostic

Pour diagnostiquer un problème de répartiteur de frein:

1. **Inspection visuelle** - Examiner l'état du répartiteur de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits

## Causes Probables

- **Pièce HS** - Le répartiteur de frein peut être hors service et nécessiter un remplacement
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- maitre-cylindre-de-frein
- flexible-de-frein

## Critères de Compatibilité

Pour commander le bon répartiteur de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage garanti"