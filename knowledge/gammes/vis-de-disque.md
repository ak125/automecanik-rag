---
category: freinage
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
  - fixer
  - maintenir
  - bloquer
  must_not_contain_concepts:
  - injection
  - climatisation
  - embrayage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Fixer le disque de frein sur le moyeu de roue
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
    question: Comment choisir Vis de disque compatible avec mon vehicule ?
  - answer: En cas de vis grippee impossible a devisser ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Vis de disque ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Vis de disque sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Vis de disque.
  id: 54
  intro:
    role: Fixer le disque de frein sur le moyeu de roue
    syncParts:
    - fixer
    - maintenir
    - bloquer
    title: A quoi sert Vis de disque ?
  pgId: '54'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/vis-de-disque.md
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
    title: Pourquoi remplacer Vis de disque a temps ?
  symptoms:
  - vis grippee impossible a devisser
  - tete de vis arrondie ou endommagee
  - vis rouillee visible a travers la jante
  - disque qui bouge legerement vis desserree
  - bruit claquement freinage cassee absente
  - '**Bruit claquement freinage cassee absente**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 54
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: vis-de-disque
source_type: gamme
subcategory: disques
symptoms:
- description: vis grippee impossible a devisser
  evidence:
  - 'Observation: vis grippee impossible a devisser'
  - Vérification visuelle ou auditive
  id: S1
  label: Vis grippee impossible a devisser
  risk_level: confort
- description: tete de vis arrondie ou endommagee
  evidence:
  - 'Observation: tete de vis arrondie ou endommagee'
  - Vérification visuelle ou auditive
  id: S2
  label: Tete de vis arrondie ou endommagee
  risk_level: confort
- description: vis rouillee visible a travers la jante
  evidence:
  - 'Observation: vis rouillee visible a travers la jante'
  - Vérification visuelle ou auditive
  id: S3
  label: Vis rouillee visible a travers la jante
  risk_level: confort
- description: disque qui bouge legerement vis desserree
  evidence:
  - 'Observation: disque qui bouge legerement vis desserree'
  - Vérification visuelle ou auditive
  id: S4
  label: Disque qui bouge legerement vis desserree
  risk_level: confort
- description: bruit claquement freinage cassee absente
  evidence:
  - 'Observation: bruit claquement freinage cassee absente'
  - Vérification visuelle ou auditive
  id: S5
  label: Bruit claquement freinage cassee absente
  risk_level: degats_volant_moteur
title: Vis de disque
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Vis de disque - Guide Diagnostic Complet

## Fonction et Rôle

Fixer le disque de frein sur le moyeu de roue

**Actions principales:** fixer, maintenir, bloquer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit claquement freinage cassee absente**
  bruit claquement freinage cassee absente

### 🟢 Autres Symptômes

- vis grippee impossible a devisser
- tete de vis arrondie ou endommagee
- vis rouillee visible a travers la jante
- disque qui bouge legerement vis desserree

## Procédure de Diagnostic

Pour diagnostiquer un problème de vis de disque:

1. **Inspection visuelle** - Examiner l'état du vis de disque
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- disque-de-frein

## Critères de Compatibilité

Pour commander le bon vis de disque, vous devez connaître:

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