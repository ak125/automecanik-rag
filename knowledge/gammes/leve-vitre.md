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
  - lever
  - descendre
  - actionner
  must_not_contain_concepts:
  - injection
  - freinage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Monte et descend la vitre de la portière
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "fonctionnement garanti"
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
    question: Comment choisir Lève-vitre compatible avec mon vehicule ?
  - answer: En cas de vitre qui ne monte ou ne descend plus ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Lève-vitre ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Lève-vitre sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Lève-vitre.
  id: 1561
  intro:
    role: Monte et descend la vitre de la portière
    syncParts:
    - lever
    - descendre
    - actionner
    title: A quoi sert Lève-vitre ?
  pgId: '1561'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/leve-vitre.md
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
    title: Pourquoi remplacer Lève-vitre a temps ?
  symptoms:
  - vitre qui ne monte ou ne descend plus
  - vitre tres lente arrete cours
  - bruit de moteur mais vitre immobile cable casse
  - vitre qui descend toute seule mecanisme use
  - grincement ou bruit anormal a la montee descente
  - vitre de travers ou mal guidee dans le rail
  - '**Bruit de moteur mais vitre immobile cable casse**'
  - '**Grincement ou bruit anormal a la montee descente**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1561
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: leve-vitre
source_type: gamme
symptoms:
- description: vitre qui ne monte ou ne descend plus
  evidence:
  - 'Observation: vitre qui ne monte ou ne descend plus'
  - Vérification visuelle ou auditive
  id: S1
  label: Vitre qui ne monte ou ne descend plus
  risk_level: confort
- description: vitre tres lente arrete cours
  evidence:
  - 'Observation: vitre tres lente arrete cours'
  - Vérification visuelle ou auditive
  id: S2
  label: Vitre tres lente arrete cours
  risk_level: confort
- description: bruit de moteur mais vitre immobile cable casse
  evidence:
  - 'Observation: bruit de moteur mais vitre immobile cable casse'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruit de moteur mais vitre immobile cable casse
  risk_level: degats_volant_moteur
- description: vitre qui descend toute seule mecanisme use
  evidence:
  - 'Observation: vitre qui descend toute seule mecanisme use'
  - Vérification visuelle ou auditive
  id: S4
  label: Vitre qui descend toute seule mecanisme use
  risk_level: confort
- description: grincement ou bruit anormal a la montee descente
  evidence:
  - 'Observation: grincement ou bruit anormal a la montee descente'
  - Vérification visuelle ou auditive
  id: S5
  label: Grincement ou bruit anormal a la montee descente
  risk_level: degats_volant_moteur
- description: vitre de travers ou mal guidee dans le rail
  evidence:
  - 'Observation: vitre de travers ou mal guidee dans le rail'
  - Vérification visuelle ou auditive
  id: S6
  label: Vitre de travers ou mal guidee dans le rail
  risk_level: confort
title: Lève-vitre
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Lève-vitre - Guide Diagnostic Complet

## Fonction et Rôle

Monte et descend la vitre de la portière

**Actions principales:** lever, descendre, actionner

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de moteur mais vitre immobile cable casse**
  bruit de moteur mais vitre immobile cable casse
- **Grincement ou bruit anormal a la montee descente**
  grincement ou bruit anormal a la montee descente

### 🟢 Autres Symptômes

- vitre qui ne monte ou ne descend plus
- vitre tres lente arrete cours
- vitre qui descend toute seule mecanisme use
- vitre de travers ou mal guidee dans le rail

## Procédure de Diagnostic

Pour diagnostiquer un problème de lève-vitre:

1. **Inspection visuelle** - Examiner l'état du lève-vitre
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- moteur-leve-vitre
- interrupteur-leve-vitre

## Critères de Compatibilité

Pour commander le bon lève-vitre, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "fonctionnement garanti"