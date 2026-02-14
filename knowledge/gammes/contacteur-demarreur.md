---
category: electrique
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
  - commuter
  - activer
  - alimenter
  must_not_contain_concepts:
  - injection
  - climatisation
  - freinage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Commuter le circuit electrique du demarreur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "demarrage garanti"
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
    question: Comment choisir Contacteur démarreur compatible avec mon vehicule ?
  - answer: En cas de aucune reaction a la cle de contact ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Contacteur démarreur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Contacteur démarreur sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de electrique pour confirmer Contacteur démarreur.
  id: 682
  intro:
    role: Commuter le circuit electrique du demarreur
    syncParts:
    - commuter
    - activer
    - alimenter
    title: A quoi sert Contacteur démarreur ?
  pgId: '682'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/contacteur-demarreur.md
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
    title: Pourquoi remplacer Contacteur démarreur a temps ?
  symptoms:
  - aucune reaction a la cle de contact
  - demarrage intermittent
  - tableau de bord qui ne s allume pas
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 682
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: contacteur-demarreur
source_type: gamme
subcategory: demarrage
symptoms:
- description: aucune reaction a la cle de contact
  evidence:
  - 'Observation: aucune reaction a la cle de contact'
  - Vérification visuelle ou auditive
  id: S1
  label: Aucune reaction a la cle de contact
  risk_level: confort
- description: demarrage intermittent
  evidence:
  - 'Observation: demarrage intermittent'
  - Vérification visuelle ou auditive
  id: S2
  label: Demarrage intermittent
  risk_level: confort
- description: tableau de bord qui ne s allume pas
  evidence:
  - 'Observation: tableau de bord qui ne s allume pas'
  - Vérification visuelle ou auditive
  id: S3
  label: Tableau de bord qui ne s allume pas
  risk_level: confort
title: Contacteur démarreur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Contacteur démarreur - Guide Diagnostic Complet

## Fonction et Rôle

Commuter le circuit electrique du demarreur

**Actions principales:** commuter, activer, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- aucune reaction a la cle de contact
- demarrage intermittent
- tableau de bord qui ne s allume pas

## Procédure de Diagnostic

Pour diagnostiquer un problème de contacteur démarreur:

1. **Inspection visuelle** - Examiner l'état du contacteur démarreur
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- demarreur
- batterie

## Critères de Compatibilité

Pour commander le bon contacteur démarreur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "demarrage garanti"