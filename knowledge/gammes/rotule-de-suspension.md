---
category: direction
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: kilometrage_eleve_ou_usure_visible
  then: remplacement_preventif_recommande
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - supporter la charge
  - articuler
  - maintenir
  must_not_contain_concepts:
  - direction
  - cremailliere
  - volant
  - braquage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Articuler le bras de suspension et la fusee - Supporte la charge verticale.
    NE DIRIGE PAS!
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "securite garantie"
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
    question: Comment choisir Rotule de suspension compatible avec mon vehicule ?
  - answer: En cas de claquements sourds sur dos d ane ou nids de poule ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Rotule de suspension ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Rotule de suspension sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Rotule de suspension.
  id: 2462
  intro:
    role: Articuler le bras de suspension et la fusee - Supporte la charge verticale.
      NE DIRIGE PAS!
    syncParts:
    - supporter la charge
    - articuler
    - maintenir
    title: A quoi sert Rotule de suspension ?
  pgId: '2462'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/rotule-de-suspension.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Rotule de suspension a temps ?
  symptoms:
  - claquements sourds sur dos d ane ou nids de poule
  - vehicule qui tire d un cote
  - jeu visible en soulevant la roue a la main
  - craquements en braquant a fond
  - soufflet de rotule dechire ou absent
  - usure anormale des pneus avant
  - '**Claquements sourds sur dos d ane ou nids de poule**'
  - '**Soufflet de rotule dechire ou absent**'
  - '**Usure anormale des pneus avant**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 2462
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: rotule-de-suspension
source_type: gamme
symptoms:
- description: claquements sourds sur dos d ane ou nids de poule
  evidence:
  - 'Observation: claquements sourds sur dos d ane ou nids de poule'
  - Vérification visuelle ou auditive
  id: S1
  label: Claquements sourds sur dos d ane ou nids de poule
  risk_level: degats_volant_moteur
- description: vehicule qui tire d un cote
  evidence:
  - 'Observation: vehicule qui tire d un cote'
  - Vérification visuelle ou auditive
  id: S2
  label: Vehicule qui tire d un cote
  risk_level: confort
- description: jeu visible en soulevant la roue a la main
  evidence:
  - 'Observation: jeu visible en soulevant la roue a la main'
  - Vérification visuelle ou auditive
  id: S3
  label: Jeu visible en soulevant la roue a la main
  risk_level: confort
- description: craquements en braquant a fond
  evidence:
  - 'Observation: craquements en braquant a fond'
  - Vérification visuelle ou auditive
  id: S4
  label: Craquements en braquant a fond
  risk_level: confort
- description: soufflet de rotule dechire ou absent
  evidence:
  - 'Observation: soufflet de rotule dechire ou absent'
  - Vérification visuelle ou auditive
  id: S5
  label: Soufflet de rotule dechire ou absent
  risk_level: securite
- description: usure anormale des pneus avant
  evidence:
  - 'Observation: usure anormale des pneus avant'
  - Vérification visuelle ou auditive
  id: S6
  label: Usure anormale des pneus avant
  risk_level: securite
title: Rotule de suspension
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Rotule de suspension - Guide Diagnostic Complet

## Fonction et Rôle

Articuler le bras de suspension et la fusee - Supporte la charge verticale. NE DIRIGE PAS!

**Actions principales:** supporter la charge, articuler, maintenir, pivoter, supporter le poids

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements sourds sur dos d ane ou nids de poule**
  claquements sourds sur dos d ane ou nids de poule

### 🟡 Symptômes de Sécurité

- **Soufflet de rotule dechire ou absent**
  soufflet de rotule dechire ou absent
- **Usure anormale des pneus avant**
  usure anormale des pneus avant

### 🟢 Autres Symptômes

- vehicule qui tire d un cote
- jeu visible en soulevant la roue a la main
- craquements en braquant a fond

## Procédure de Diagnostic

Pour diagnostiquer un problème de rotule de suspension:

1. **Inspection visuelle** - Examiner l'état du rotule de suspension
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- amortisseur
- barre-stabilisatrice
- bras-de-suspension
- ressort-de-suspension
- rotule-de-direction

## Critères de Compatibilité

Pour commander le bon rotule de suspension, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"