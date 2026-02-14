---
category: eclairage
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
  - regler
  - ajuster
  - adapter
  must_not_contain_concepts:
  - ampoule
  - feu
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Règle la hauteur du faisceau lumineux en fonction de la charge du
    véhicule
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
    question: Comment choisir Correcteur de portée compatible avec mon vehicule ?
  - answer: En cas de phares mal orientés ou de degradation mesurable, il faut controler
      rapidement avant panne secondaire.
    question: Quand remplacer Correcteur de portée ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Correcteur de portée sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Correcteur de
    portée.
  id: 700
  intro:
    role: Règle la hauteur du faisceau lumineux en fonction de la charge du véhicule
    syncParts:
    - regler
    - ajuster
    - adapter
    title: A quoi sert Correcteur de portée ?
  pgId: '700'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/correcteur-de-portee.md
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
    title: Pourquoi remplacer Correcteur de portée a temps ?
  symptoms:
  - phares mal orientés
  - eblouissement
  - reglage impossible
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 700
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: correcteur-de-portee
source_type: gamme
symptoms:
- description: phares mal orientés
  evidence:
  - 'Observation: phares mal orientés'
  - Vérification visuelle ou auditive
  id: S1
  label: Phares mal orientés
  risk_level: confort
- description: eblouissement
  evidence:
  - 'Observation: eblouissement'
  - Vérification visuelle ou auditive
  id: S2
  label: Eblouissement
  risk_level: confort
- description: reglage impossible
  evidence:
  - 'Observation: reglage impossible'
  - Vérification visuelle ou auditive
  id: S3
  label: Reglage impossible
  risk_level: confort
title: Correcteur de portée
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Correcteur de portée - Guide Diagnostic Complet

## Fonction et Rôle

Règle la hauteur du faisceau lumineux en fonction de la charge du véhicule

**Actions principales:** regler, ajuster, adapter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- phares mal orientés
- eblouissement
- reglage impossible

## Procédure de Diagnostic

Pour diagnostiquer un problème de correcteur de portée:

1. **Inspection visuelle** - Examiner l'état du correcteur de portée
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- feu-avant
- commande-correcteur-de-portee

## Critères de Compatibilité

Pour commander le bon correcteur de portée, vous devez connaître:

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