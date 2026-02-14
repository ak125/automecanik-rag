---
category: moteur
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
  - transmettre
  - actionner
  - lever
  must_not_contain_concepts:
  - freinage
  - climatisation
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transmettre le mouvement de l'arbre a cames aux soupapes
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare le moteur"
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
    question: Comment choisir Kit de poussoir culbuteur compatible avec mon vehicule
      ?
  - answer: En cas de claquement moteur au demarrage ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Kit de poussoir culbuteur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Kit de poussoir culbuteur sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de moteur pour confirmer Kit de poussoir culbuteur.
  id: 3320
  intro:
    role: Kit de poussoir culbuteur intervient directement sur moteur du vehicule.
      Un choix conforme protege la combustion et limite les pannes secondaires.
    syncParts:
    - transmettre
    - actionner
    - lever
    title: A quoi sert Kit de poussoir culbuteur ?
  pgId: '3320'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/kit-de-poussoir-culbuteur.md
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
    title: Pourquoi remplacer Kit de poussoir culbuteur a temps ?
  symptoms:
  - claquement moteur au demarrage
  - bruit qui persiste a chaud
  - perte de puissance legere
  - '**Claquement moteur au demarrage**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 3320
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: kit-de-poussoir-culbuteur
source_type: gamme
symptoms:
- description: claquement moteur au demarrage
  evidence:
  - 'Observation: claquement moteur au demarrage'
  - Vérification visuelle ou auditive
  id: S1
  label: Claquement moteur au demarrage
  risk_level: degats_volant_moteur
- description: bruit qui persiste a chaud
  evidence:
  - 'Observation: bruit qui persiste a chaud'
  - Vérification visuelle ou auditive
  id: S2
  label: Bruit qui persiste a chaud
  risk_level: confort
- description: perte de puissance legere
  evidence:
  - 'Observation: perte de puissance legere'
  - Vérification visuelle ou auditive
  id: S3
  label: Perte de puissance legere
  risk_level: confort
title: Kit de poussoir culbuteur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Kit de poussoir culbuteur - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le mouvement de l'arbre a cames aux soupapes

**Actions principales:** transmettre, actionner, lever

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement moteur au demarrage**
  claquement moteur au demarrage

### 🟢 Autres Symptômes

- bruit qui persiste a chaud
- perte de puissance legere

## Procédure de Diagnostic

Pour diagnostiquer un problème de kit de poussoir culbuteur:

1. **Inspection visuelle** - Examiner l'état du kit de poussoir culbuteur
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- arbre-a-came
- culbuteur
- poussoir-de-soupape
- soupape-d-admission
- soupape-d-echappement

## Critères de Compatibilité

Pour commander le bon kit de poussoir culbuteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"