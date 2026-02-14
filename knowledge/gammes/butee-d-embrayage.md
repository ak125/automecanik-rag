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
  - actionner
  - débrayer
  - pousser
  must_not_contain_concepts:
  - disque
  - volant
  - couple
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Actionner le mécanisme d'embrayage pour permettre le débrayage
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "débrayage parfait"
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
    question: Comment choisir Butée d'embrayage compatible avec mon vehicule ?
  - answer: En cas de bruit roulement quand appuie pedale ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Butée d'embrayage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Butée d'embrayage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Butée d'embrayage.
  id: 48
  intro:
    role: Actionner le mécanisme d'embrayage pour permettre le débrayage
    syncParts:
    - actionner
    - débrayer
    - pousser
    title: A quoi sert Butée d'embrayage ?
  pgId: '48'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/butee-d-embrayage.md
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
    title: Pourquoi remplacer Butée d'embrayage a temps ?
  symptoms:
  - bruit roulement quand appuie pedale
  - sifflement grondement disparait relachant pedale
  - pedale d embrayage qui vibre sous le pied
  - embrayage qui accroche par a-coups
  - difficulte a passer les vitesses butee grippee
  - plus changement embrayage
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 48
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: butee-d-embrayage
source_type: gamme
symptoms:
- description: bruit roulement quand appuie pedale
  evidence:
  - 'Observation: bruit roulement quand appuie pedale'
  - Vérification visuelle ou auditive
  id: S1
  label: Bruit roulement quand appuie pedale
  risk_level: confort
- description: sifflement grondement disparait relachant pedale
  evidence:
  - 'Observation: sifflement grondement disparait relachant pedale'
  - Vérification visuelle ou auditive
  id: S2
  label: Sifflement grondement disparait relachant pedale
  risk_level: confort
- description: pedale d embrayage qui vibre sous le pied
  evidence:
  - 'Observation: pedale d embrayage qui vibre sous le pied'
  - Vérification visuelle ou auditive
  id: S3
  label: Pedale d embrayage qui vibre sous le pied
  risk_level: confort
- description: embrayage qui accroche par a-coups
  evidence:
  - 'Observation: embrayage qui accroche par a-coups'
  - Vérification visuelle ou auditive
  id: S4
  label: Embrayage qui accroche par a-coups
  risk_level: confort
- description: difficulte a passer les vitesses butee grippee
  evidence:
  - 'Observation: difficulte a passer les vitesses butee grippee'
  - Vérification visuelle ou auditive
  id: S5
  label: Difficulte a passer les vitesses butee grippee
  risk_level: confort
- description: plus changement embrayage
  evidence:
  - 'Observation: plus changement embrayage'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus changement embrayage
  risk_level: confort
title: Butée d'embrayage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Butée d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Actionner le mécanisme d'embrayage pour permettre le débrayage

**Actions principales:** actionner, débrayer, pousser, libérer le disque, appuyer sur le mécanisme

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- bruit roulement quand appuie pedale
- sifflement grondement disparait relachant pedale
- pedale d embrayage qui vibre sous le pied
- embrayage qui accroche par a-coups
- difficulte a passer les vitesses butee grippee
- plus changement embrayage

## Procédure de Diagnostic

Pour diagnostiquer un problème de butée d'embrayage:

1. **Inspection visuelle** - Examiner l'état du butée d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- emetteur-d-embrayage
- kit-d-embrayage
- recepteur-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon butée d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "débrayage parfait"