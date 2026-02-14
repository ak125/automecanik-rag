---
category: distribution
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
  - guider
  - enrouler
  - maintenir
  must_not_contain_concepts:
  - freinage
  - climatisation
  - turbo
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Guide la courroie d'accessoire
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de durée de vie"
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
    question: Comment choisir Galet enrouleur de courroie d'accessoire compatible
      avec mon vehicule ?
  - answer: En cas de courroie d accessoire visiblement usee ou fissuree ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Galet enrouleur de courroie d'accessoire ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Galet enrouleur de courroie d'accessoire sans verification
      atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Galet enrouleur
    de courroie d'accessoire.
  id: 312
  intro:
    role: Galet enrouleur de courroie d'accessoire intervient directement sur compatibilite
      du vehicule. Un choix conforme protege la securite et limite les pannes secondaires.
    syncParts:
    - guider
    - enrouler
    - maintenir
    title: A quoi sert Galet enrouleur de courroie d'accessoire ?
  pgId: '312'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/galet-enrouleur-de-courroie-d-accessoire.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Galet enrouleur de courroie d'accessoire a temps ?
  symptoms:
  - courroie d accessoire visiblement usee ou fissuree
  - sifflement ou grondement au niveau de la courroie
  - perceptible faisant tourner galet main
  - perte de tension de la courroie
  - odeur de caoutchouc chaud
  - plus de 80 000 km depuis le dernier changement
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 312
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: galet-enrouleur-de-courroie-d-accessoire
source_type: gamme
symptoms:
- description: courroie d accessoire visiblement usee ou fissuree
  evidence:
  - 'Observation: courroie d accessoire visiblement usee ou fissuree'
  - Vérification visuelle ou auditive
  id: S1
  label: Courroie d accessoire visiblement usee ou fissuree
  risk_level: confort
- description: sifflement ou grondement au niveau de la courroie
  evidence:
  - 'Observation: sifflement ou grondement au niveau de la courroie'
  - Vérification visuelle ou auditive
  id: S2
  label: Sifflement ou grondement au niveau de la courroie
  risk_level: confort
- description: perceptible faisant tourner galet main
  evidence:
  - 'Observation: perceptible faisant tourner galet main'
  - Vérification visuelle ou auditive
  id: S3
  label: Perceptible faisant tourner galet main
  risk_level: confort
- description: perte de tension de la courroie
  evidence:
  - 'Observation: perte de tension de la courroie'
  - Vérification visuelle ou auditive
  id: S4
  label: Perte de tension de la courroie
  risk_level: confort
- description: odeur de caoutchouc chaud
  evidence:
  - 'Observation: odeur de caoutchouc chaud'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de caoutchouc chaud
  risk_level: confort
- description: plus de 80 000 km depuis le dernier changement
  evidence:
  - 'Observation: plus de 80 000 km depuis le dernier changement'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 80 000 km depuis le dernier changement
  risk_level: confort
title: Galet enrouleur de courroie d'accessoire
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Galet enrouleur de courroie d'accessoire - Guide Diagnostic Complet

## Fonction et Rôle

Guide la courroie d'accessoire

**Actions principales:** guider, enrouler, maintenir

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- courroie d accessoire visiblement usee ou fissuree
- sifflement ou grondement au niveau de la courroie
- perceptible faisant tourner galet main
- perte de tension de la courroie
- odeur de caoutchouc chaud
- plus de 80 000 km depuis le dernier changement

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet enrouleur de courroie d'accessoire:

1. **Inspection visuelle** - Examiner l'état du galet enrouleur de courroie d'accessoire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-a-eau
- pompe-de-direction-assistee

## Critères de Compatibilité

Pour commander le bon galet enrouleur de courroie d'accessoire, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de durée de vie"