---
category: transmission
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
  - assurer l'etancheite
  - empecher les fuites
  must_not_contain_concepts:
  - moteur
  - culasse
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Assurer l'etancheite de la transmission au niveau du cardan
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare la transmission"
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
    question: Comment choisir Bague d'étanchéité cardan compatible avec mon vehicule
      ?
  - answer: En cas de graisse projetee sur la roue ou de degradation mesurable, il
      faut controler rapidement avant panne secondaire.
    question: Quand remplacer Bague d'étanchéité cardan ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Bague d'étanchéité cardan sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de transmission pour confirmer Bague d'étanchéité
    cardan.
  id: 624
  intro:
    role: Assurer l'etancheite de la transmission au niveau du cardan
    syncParts:
    - assurer l'etancheite
    - empecher les fuites
    title: A quoi sert Bague d'étanchéité cardan ?
  pgId: '624'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/bague-d-etancheite-cardan.md
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
    title: Pourquoi remplacer Bague d'étanchéité cardan a temps ?
  symptoms:
  - graisse projetee sur la roue
  - claquements en braquage
  - joint homocinetique bruyant
  - '**Claquements en braquage**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 624
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: bague-d-etancheite-cardan
source_type: gamme
symptoms:
- description: graisse projetee sur la roue
  evidence:
  - 'Observation: graisse projetee sur la roue'
  - Vérification visuelle ou auditive
  id: S1
  label: Graisse projetee sur la roue
  risk_level: confort
- description: claquements en braquage
  evidence:
  - 'Observation: claquements en braquage'
  - Vérification visuelle ou auditive
  id: S2
  label: Claquements en braquage
  risk_level: degats_volant_moteur
- description: joint homocinetique bruyant
  evidence:
  - 'Observation: joint homocinetique bruyant'
  - Vérification visuelle ou auditive
  id: S3
  label: Joint homocinetique bruyant
  risk_level: confort
title: Bague d'étanchéité cardan
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Bague d'étanchéité cardan - Guide Diagnostic Complet

## Fonction et Rôle

Assurer l'etancheite de la transmission au niveau du cardan

**Actions principales:** assurer l'etancheite, empecher les fuites

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements en braquage**
  claquements en braquage

### 🟢 Autres Symptômes

- graisse projetee sur la roue
- joint homocinetique bruyant

## Procédure de Diagnostic

Pour diagnostiquer un problème de bague d'étanchéité cardan:

1. **Inspection visuelle** - Examiner l'état du bague d'étanchéité cardan
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cardan

## Critères de Compatibilité

Pour commander le bon bague d'étanchéité cardan, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare la transmission"