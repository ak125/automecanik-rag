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
  - transmettre
  - articuler
  - relier
  must_not_contain_concepts:
  - injection
  - freinage
  - climatisation
  - allumage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transmettre le couple entre les elements de transmission
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
    question: Comment choisir Joint arbre longitudinal compatible avec mon vehicule
      ?
  - answer: En cas de vibrations a vitesse constante ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Joint arbre longitudinal ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Joint arbre longitudinal sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de transmission pour confirmer Joint arbre longitudinal.
  id: 1427
  intro:
    role: Transmettre le couple entre les elements de transmission
    syncParts:
    - transmettre
    - articuler
    - relier
    title: A quoi sert Joint arbre longitudinal ?
  pgId: '1427'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/joint-arbre-longitudinal.md
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
    title: Pourquoi remplacer Joint arbre longitudinal a temps ?
  symptoms:
  - vibrations a vitesse constante
  - claquements en acceleration deceleration
  - bruits de roulement sous le vehicule
  - '**Claquements en acceleration deceleration**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1427
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: joint-arbre-longitudinal
source_type: gamme
symptoms:
- description: vibrations a vitesse constante
  evidence:
  - 'Observation: vibrations a vitesse constante'
  - Vérification visuelle ou auditive
  id: S1
  label: Vibrations a vitesse constante
  risk_level: confort
- description: claquements en acceleration deceleration
  evidence:
  - 'Observation: claquements en acceleration deceleration'
  - Vérification visuelle ou auditive
  id: S2
  label: Claquements en acceleration deceleration
  risk_level: degats_volant_moteur
- description: bruits de roulement sous le vehicule
  evidence:
  - 'Observation: bruits de roulement sous le vehicule'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruits de roulement sous le vehicule
  risk_level: confort
title: Joint arbre longitudinal
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Joint arbre longitudinal - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le couple entre les elements de transmission

**Actions principales:** transmettre, articuler, relier

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements en acceleration deceleration**
  claquements en acceleration deceleration

### 🟢 Autres Symptômes

- vibrations a vitesse constante
- bruits de roulement sous le vehicule

## Procédure de Diagnostic

Pour diagnostiquer un problème de joint arbre longitudinal:

1. **Inspection visuelle** - Examiner l'état du joint arbre longitudinal
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cardan
- soufflet-de-cardan

## Critères de Compatibilité

Pour commander le bon joint arbre longitudinal, vous devez connaître:

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