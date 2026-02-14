---
category: embrayage
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
  - transmettre l'effort
  - tirer
  - pousser
  must_not_contain_concepts:
  - disque
  - volant
  - couple
  - hydraulique
  - liquide
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transmettre l'effort mécanique de la pédale vers la fourchette
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "effort parfait"
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
    question: Comment choisir Câble d'embrayage compatible avec mon vehicule ?
  - answer: En cas de pedale d embrayage dure ou difficile a enfoncer ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Câble d'embrayage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Câble d'embrayage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Câble d'embrayage.
  id: 478
  intro:
    role: Transmettre l'effort mécanique de la pédale vers la fourchette
    syncParts:
    - transmettre l'effort
    - tirer
    - pousser
    title: A quoi sert Câble d'embrayage ?
  pgId: '478'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/cable-d-embrayage.md
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
    title: Pourquoi remplacer Câble d'embrayage a temps ?
  symptoms:
  - pedale d embrayage dure ou difficile a enfoncer
  - point de patinage tres haut ou tres bas
  - craquement ou grincement en appuyant sur la pedale
  - cable visible effiloche ou rouille
  - embrayage qui ne debraye pas completement
  - pedale qui reste enfoncee cable casse
  - '**Craquement ou grincement en appuyant sur la pedale**'
  - '**Pedale qui reste enfoncee cable casse**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 478
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: cable-d-embrayage
source_type: gamme
symptoms:
- description: pedale d embrayage dure ou difficile a enfoncer
  evidence:
  - 'Observation: pedale d embrayage dure ou difficile a enfoncer'
  - Vérification visuelle ou auditive
  id: S1
  label: Pedale d embrayage dure ou difficile a enfoncer
  risk_level: confort
- description: point de patinage tres haut ou tres bas
  evidence:
  - 'Observation: point de patinage tres haut ou tres bas'
  - Vérification visuelle ou auditive
  id: S2
  label: Point de patinage tres haut ou tres bas
  risk_level: confort
- description: craquement ou grincement en appuyant sur la pedale
  evidence:
  - 'Observation: craquement ou grincement en appuyant sur la pedale'
  - Vérification visuelle ou auditive
  id: S3
  label: Craquement ou grincement en appuyant sur la pedale
  risk_level: degats_volant_moteur
- description: cable visible effiloche ou rouille
  evidence:
  - 'Observation: cable visible effiloche ou rouille'
  - Vérification visuelle ou auditive
  id: S4
  label: Cable visible effiloche ou rouille
  risk_level: confort
- description: embrayage qui ne debraye pas completement
  evidence:
  - 'Observation: embrayage qui ne debraye pas completement'
  - Vérification visuelle ou auditive
  id: S5
  label: Embrayage qui ne debraye pas completement
  risk_level: confort
- description: pedale qui reste enfoncee cable casse
  evidence:
  - 'Observation: pedale qui reste enfoncee cable casse'
  - Vérification visuelle ou auditive
  id: S6
  label: Pedale qui reste enfoncee cable casse
  risk_level: degats_volant_moteur
title: Câble d'embrayage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Câble d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre l'effort mécanique de la pédale vers la fourchette

**Actions principales:** transmettre l'effort, tirer, pousser, relier, actionner

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Craquement ou grincement en appuyant sur la pedale**
  craquement ou grincement en appuyant sur la pedale
- **Pedale qui reste enfoncee cable casse**
  pedale qui reste enfoncee cable casse

### 🟢 Autres Symptômes

- pedale d embrayage dure ou difficile a enfoncer
- point de patinage tres haut ou tres bas
- cable visible effiloche ou rouille
- embrayage qui ne debraye pas completement

## Procédure de Diagnostic

Pour diagnostiquer un problème de câble d'embrayage:

1. **Inspection visuelle** - Examiner l'état du câble d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- butee-d-embrayage
- kit-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon câble d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "effort parfait"