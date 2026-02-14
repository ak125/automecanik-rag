---
category: accessoires
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
  - supporter
  - maintenir
  - plaquer
  must_not_contain_concepts:
  - caoutchouc
  - lame
  - capteur abs
  - freinage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Supporte et maintient le balai contre le pare-brise
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
    question: Comment choisir Bras d'essuie-glace compatible avec mon vehicule ?
  - answer: En cas de balai qui ne touche plus le pare-brise ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Bras d'essuie-glace ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Bras d'essuie-glace sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Bras d'essuie-glace.
  id: 301
  intro:
    role: Supporte et maintient le balai contre le pare-brise
    syncParts:
    - supporter
    - maintenir
    - plaquer
    title: A quoi sert Bras d'essuie-glace ?
  pgId: '301'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/bras-d-essuie-glace.md
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
    title: Pourquoi remplacer Bras d'essuie-glace a temps ?
  symptoms:
  - balai qui ne touche plus le pare-brise
  - traces ou zones non balayees
  - bras tordu ou rouille
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 301
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: bras-d-essuie-glace
source_type: gamme
symptoms:
- description: balai qui ne touche plus le pare-brise
  evidence:
  - 'Observation: balai qui ne touche plus le pare-brise'
  - Vérification visuelle ou auditive
  id: S1
  label: Balai qui ne touche plus le pare-brise
  risk_level: confort
- description: traces ou zones non balayees
  evidence:
  - 'Observation: traces ou zones non balayees'
  - Vérification visuelle ou auditive
  id: S2
  label: Traces ou zones non balayees
  risk_level: confort
- description: bras tordu ou rouille
  evidence:
  - 'Observation: bras tordu ou rouille'
  - Vérification visuelle ou auditive
  id: S3
  label: Bras tordu ou rouille
  risk_level: confort
title: Bras d'essuie-glace
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Bras d'essuie-glace - Guide Diagnostic Complet

## Fonction et Rôle

Supporte et maintient le balai contre le pare-brise

**Actions principales:** supporter, maintenir, plaquer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- balai qui ne touche plus le pare-brise
- traces ou zones non balayees
- bras tordu ou rouille

## Procédure de Diagnostic

Pour diagnostiquer un problème de bras d'essuie-glace:

1. **Inspection visuelle** - Examiner l'état du bras d'essuie-glace
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-d-essuie-glace
- moteur-d-essuie-glace
- pompe-nettoyage-des-vitres

## Critères de Compatibilité

Pour commander le bon bras d'essuie-glace, vous devez connaître:

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