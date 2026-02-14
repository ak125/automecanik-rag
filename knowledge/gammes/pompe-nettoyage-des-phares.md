---
category: accessoires
diagnostic_tree:
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
  - projeter
  - pulveriser
  - alimenter
  must_not_contain_concepts:
  - balai
  - essuie-glace
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Projette le liquide de nettoyage sur les optiques de phares
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "visibilite parfaite"
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
    question: Comment choisir Pompe nettoyage des phares compatible avec mon vehicule
      ?
  - answer: En cas de jets de phares inactifs ou de degradation mesurable, il faut
      controler rapidement avant panne secondaire.
    question: Quand remplacer Pompe nettoyage des phares ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Pompe nettoyage des phares sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Pompe nettoyage
    des phares.
  id: 795
  intro:
    role: Projette le liquide de nettoyage sur les optiques de phares
    syncParts:
    - projeter
    - pulveriser
    - alimenter
    title: A quoi sert Pompe nettoyage des phares ?
  pgId: '795'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/pompe-nettoyage-des-phares.md
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
    title: Pourquoi remplacer Pompe nettoyage des phares a temps ?
  symptoms:
  - jets de phares inactifs
  - phares sales malgre l activation
  - bruit de pompe sans projection
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 795
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: pompe-nettoyage-des-phares
source_type: gamme
symptoms:
- description: jets de phares inactifs
  evidence:
  - 'Observation: jets de phares inactifs'
  - Vérification visuelle ou auditive
  id: S1
  label: Jets de phares inactifs
  risk_level: confort
- description: phares sales malgre l activation
  evidence:
  - 'Observation: phares sales malgre l activation'
  - Vérification visuelle ou auditive
  id: S2
  label: Phares sales malgre l activation
  risk_level: confort
- description: bruit de pompe sans projection
  evidence:
  - 'Observation: bruit de pompe sans projection'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruit de pompe sans projection
  risk_level: confort
title: Pompe nettoyage des phares
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Pompe nettoyage des phares - Guide Diagnostic Complet

## Fonction et Rôle

Projette le liquide de nettoyage sur les optiques de phares

**Actions principales:** projeter, pulveriser, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- jets de phares inactifs
- phares sales malgre l activation
- bruit de pompe sans projection

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe nettoyage des phares:

1. **Inspection visuelle** - Examiner l'état du pompe nettoyage des phares
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- gicleur
- phare

## Critères de Compatibilité

Pour commander le bon pompe nettoyage des phares, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"