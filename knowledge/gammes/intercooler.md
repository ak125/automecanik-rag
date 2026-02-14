---
category: turbo
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - refroidir
  - echanger
  - densifier
  must_not_contain_concepts:
  - climatisation
  - freinage
  - distribution
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Refroidit l'air comprimé par le turbo
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de puissance"
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
    question: Comment choisir Intercooler compatible avec mon vehicule ?
  - answer: En cas de perte de puissance a l acceleration ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Intercooler ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Intercooler sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Intercooler.
  id: 468
  intro:
    role: Intercooler intervient directement sur compatibilite du vehicule. Un choix
      conforme protege la securite et limite les pannes secondaires.
    syncParts:
    - refroidir
    - echanger
    - densifier
    title: A quoi sert Intercooler ?
  pgId: '468'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/intercooler.md
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
    title: Pourquoi remplacer Intercooler a temps ?
  symptoms:
  - perte de puissance a l acceleration
  - fumee a l acceleration huile dans admission
  - fuite d air audible sifflement
  - intercooler gras ou huileux a l exterieur
  - ailettes ecrasees ou deformees choc
  - surconsommation apres casse turbo
  - '**Surconsommation apres casse turbo**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 468
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: intercooler
source_type: gamme
symptoms:
- description: perte de puissance a l acceleration
  evidence:
  - 'Observation: perte de puissance a l acceleration'
  - Vérification visuelle ou auditive
  id: S1
  label: Perte de puissance a l acceleration
  risk_level: confort
- description: fumee a l acceleration huile dans admission
  evidence:
  - 'Observation: fumee a l acceleration huile dans admission'
  - Vérification visuelle ou auditive
  id: S2
  label: Fumee a l acceleration huile dans admission
  risk_level: confort
- description: fuite d air audible sifflement
  evidence:
  - 'Observation: fuite d air audible sifflement'
  - Vérification visuelle ou auditive
  id: S3
  label: Fuite d air audible sifflement
  risk_level: confort
- description: intercooler gras ou huileux a l exterieur
  evidence:
  - 'Observation: intercooler gras ou huileux a l exterieur'
  - Vérification visuelle ou auditive
  id: S4
  label: Intercooler gras ou huileux a l exterieur
  risk_level: confort
- description: ailettes ecrasees ou deformees choc
  evidence:
  - 'Observation: ailettes ecrasees ou deformees choc'
  - Vérification visuelle ou auditive
  id: S5
  label: Ailettes ecrasees ou deformees choc
  risk_level: confort
- description: surconsommation apres casse turbo
  evidence:
  - 'Observation: surconsommation apres casse turbo'
  - Vérification visuelle ou auditive
  id: S6
  label: Surconsommation apres casse turbo
  risk_level: degats_volant_moteur
title: Intercooler
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Intercooler - Guide Diagnostic Complet

## Fonction et Rôle

Refroidit l'air comprimé par le turbo

**Actions principales:** refroidir, echanger, densifier

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Surconsommation apres casse turbo**
  surconsommation apres casse turbo

### 🟢 Autres Symptômes

- perte de puissance a l acceleration
- fumee a l acceleration huile dans admission
- fuite d air audible sifflement
- intercooler gras ou huileux a l exterieur
- ailettes ecrasees ou deformees choc

## Procédure de Diagnostic

Pour diagnostiquer un problème de intercooler:

1. **Inspection visuelle** - Examiner l'état du intercooler
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- turbo

## Critères de Compatibilité

Pour commander le bon intercooler, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"