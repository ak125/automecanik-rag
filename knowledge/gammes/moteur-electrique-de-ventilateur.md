---
category: refroidissement
diagnostic_tree:
- if: vehicule_immobilise_ou_symptome_critique
  then: verification_urgente_piece_et_alimentation
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - entrainer
  - tourner
  - ventiler
  must_not_contain_concepts:
  - injection
  - freinage
  - embrayage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Entrainer les pales du ventilateur de refroidissement
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "refroidissement optimal"
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
    question: Comment choisir Moteur électrique de ventilateur compatible avec mon
      vehicule ?
  - answer: En cas de ventilateur qui ne tourne pas ou de degradation mesurable, il
      faut controler rapidement avant panne secondaire.
    question: Quand remplacer Moteur électrique de ventilateur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Moteur électrique de ventilateur sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Moteur électrique
    de ventilateur.
  id: 792
  intro:
    role: Entrainer les pales du ventilateur de refroidissement
    syncParts:
    - entrainer
    - tourner
    - ventiler
    title: A quoi sert Moteur électrique de ventilateur ?
  pgId: '792'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/moteur-electrique-de-ventilateur.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le moteur électrique de ventilateur peut être hors service et
      nécessiter un remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le moteur électrique de ventilateur peut être hors
      service et nécessiter un remplacement'
    title: Pourquoi remplacer Moteur électrique de ventilateur a temps ?
  symptoms:
  - ventilateur qui ne tourne pas
  - surchauffe en circulation lente
  - bruit de roulement du ventilateur
  - '**Ventilateur qui ne tourne pas**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 792
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: moteur-electrique-de-ventilateur
source_type: gamme
symptoms:
- description: ventilateur qui ne tourne pas
  evidence:
  - 'Observation: ventilateur qui ne tourne pas'
  - Vérification visuelle ou auditive
  id: S1
  label: Ventilateur qui ne tourne pas
  risk_level: immobilisation
- description: surchauffe en circulation lente
  evidence:
  - 'Observation: surchauffe en circulation lente'
  - Vérification visuelle ou auditive
  id: S2
  label: Surchauffe en circulation lente
  risk_level: confort
- description: bruit de roulement du ventilateur
  evidence:
  - 'Observation: bruit de roulement du ventilateur'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruit de roulement du ventilateur
  risk_level: confort
title: Moteur électrique de ventilateur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Moteur électrique de ventilateur - Guide Diagnostic Complet

## Fonction et Rôle

Entrainer les pales du ventilateur de refroidissement

**Actions principales:** entrainer, tourner, ventiler

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Ventilateur qui ne tourne pas**
  ventilateur qui ne tourne pas

### 🟢 Autres Symptômes

- surchauffe en circulation lente
- bruit de roulement du ventilateur

## Procédure de Diagnostic

Pour diagnostiquer un problème de moteur électrique de ventilateur:

1. **Inspection visuelle** - Examiner l'état du moteur électrique de ventilateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le moteur électrique de ventilateur peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes

## Pièces Associées

Lors du remplacement, vérifier également:

- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon moteur électrique de ventilateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidissement optimal"