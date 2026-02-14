---
category: freinage
diagnostic_tree:
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
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
  - generer la pression
  - alimenter le circuit
  - commander le freinage
  must_not_contain_concepts:
  - friction
  - thermique
  - ABS
  - electronique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transformer l'action de la pedale en pression hydraulique
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "efficacite garantie"
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
    question: Comment choisir Maître cylindre de frein compatible avec mon vehicule
      ?
  - answer: En cas de pedale de frein qui s enfonce lentement a l arret ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Maître cylindre de frein ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Maître cylindre de frein sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Maître cylindre de frein.
  id: 258
  intro:
    role: Transformer l'action de la pedale en pression hydraulique
    syncParts:
    - generer la pression
    - alimenter le circuit
    - commander le freinage
    title: A quoi sert Maître cylindre de frein ?
  pgId: '258'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/maitre-cylindre-de-frein.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Défaillance électrique** - Problème de connexion, de câblage ou
      de composant électronique'
    title: Pourquoi remplacer Maître cylindre de frein a temps ?
  symptoms:
  - pedale de frein qui s enfonce lentement a l arret
  - niveau liquide baisse fuite visible
  - pedale de frein molle malgre une purge recente
  - liquide de frein qui fuit dans l habitacle servo
  - perte de freinage progressive sur un circuit
  - voyant niveau liquide de frein allume
  - '**Pedale de frein qui s enfonce lentement a l arret**'
  - '**Pedale de frein molle malgre une purge recente**'
  - '**Liquide de frein qui fuit dans l habitacle servo**'
  - '**Perte de freinage progressive sur un circuit**'
  - '**Voyant niveau liquide de frein allume**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 258
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: maitre-cylindre-de-frein
source_type: gamme
symptoms:
- description: pedale de frein qui s enfonce lentement a l arret
  evidence:
  - 'Observation: pedale de frein qui s enfonce lentement a l arret'
  - Vérification visuelle ou auditive
  id: S1
  label: Pedale de frein qui s enfonce lentement a l arret
  risk_level: securite
- description: niveau liquide baisse fuite visible
  evidence:
  - 'Observation: niveau liquide baisse fuite visible'
  - Vérification visuelle ou auditive
  id: S2
  label: Niveau liquide baisse fuite visible
  risk_level: confort
- description: pedale de frein molle malgre une purge recente
  evidence:
  - 'Observation: pedale de frein molle malgre une purge recente'
  - Vérification visuelle ou auditive
  id: S3
  label: Pedale de frein molle malgre une purge recente
  risk_level: securite
- description: liquide de frein qui fuit dans l habitacle servo
  evidence:
  - 'Observation: liquide de frein qui fuit dans l habitacle servo'
  - Vérification visuelle ou auditive
  id: S4
  label: Liquide de frein qui fuit dans l habitacle servo
  risk_level: securite
- description: perte de freinage progressive sur un circuit
  evidence:
  - 'Observation: perte de freinage progressive sur un circuit'
  - Vérification visuelle ou auditive
  id: S5
  label: Perte de freinage progressive sur un circuit
  risk_level: securite
- description: voyant niveau liquide de frein allume
  evidence:
  - 'Observation: voyant niveau liquide de frein allume'
  - Vérification visuelle ou auditive
  id: S6
  label: Voyant niveau liquide de frein allume
  risk_level: securite
title: Maître cylindre de frein
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Maître cylindre de frein - Guide Diagnostic Complet

## Fonction et Rôle

Transformer l'action de la pedale en pression hydraulique

**Actions principales:** generer la pression, alimenter le circuit, commander le freinage, convertir, pousser le liquide

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Pedale de frein qui s enfonce lentement a l arret**
  pedale de frein qui s enfonce lentement a l arret
- **Pedale de frein molle malgre une purge recente**
  pedale de frein molle malgre une purge recente
- **Liquide de frein qui fuit dans l habitacle servo**
  liquide de frein qui fuit dans l habitacle servo
- **Perte de freinage progressive sur un circuit**
  perte de freinage progressive sur un circuit
- **Voyant niveau liquide de frein allume**
  voyant niveau liquide de frein allume

### 🟢 Autres Symptômes

- niveau liquide baisse fuite visible

## Procédure de Diagnostic

Pour diagnostiquer un problème de maître cylindre de frein:

1. **Inspection visuelle** - Examiner l'état du maître cylindre de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- agregat-de-freinage
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere

## Critères de Compatibilité

Pour commander le bon maître cylindre de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "efficacite garantie"