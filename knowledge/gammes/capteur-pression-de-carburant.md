---
category: capteurs
slug: capteur-pression-de-carburant
title: Capteur pression de carburant
pg_id: 817
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-01'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v4_converted
  last_enriched_by: script:rag-enrich-metier-templates
  last_enriched_at: '2026-03-26'
domain:
  role: Mesurer la pression du carburant dans la rampe d'injection et transmettre l'information au calculateur
  must_be_true:
  - mesurer
  - detecter
  - transmettre
  must_not_contain:
  - pompe
  - injecteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - alternateur
  - batterie
  - demarreur
  - bougie-d-allumage
  - bobine-d-allumage
  - poulie-d-alternateur
  confusion_with:
  - term: piece-electrique-voisine
    difference: Les pieces electriques ont des connecteurs specifiques. Verifier le nombre de broches et le voltage.
selection:
  criteria:
  - Marque de votre véhicule
  - Modele de votre véhicule
  - Annee de votre véhicule
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "corrige la panne"
  cost_range:
    min: 40
    max: 150
    currency: EUR
    unit: capteur
    source: catalogue automecanik
  brands:
    premium:
    - Bosch
    - Valeo
    - Denso
    standard:
    - Hella
    - NGK
    - Delphi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Perte de puissance a l acceleration
    severity: confort
  - id: S2
    label: A-coups ou hesitations du moteur
    severity: confort
  - id: S3
    label: Cliquetis cognement moteur injection defaillante
    severity: confort
  - id: S4
    label: Voyant moteur avec codes p0190-p0194
    severity: confort
  - id: S5
    label: Odeur carburant anormale fuite mauvaise
    severity: confort
  - id: S6
    label: Plus de 150 000 km sur moteur diesel hdi tdi
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : perte de puissance a l acceleration ?'
  - 'Observer : a-coups ou hesitations du moteur ?'
  - 'Observer : cliquetis cognement moteur injection defaillante ?'
  - Voyant moteur avec codes p0190-p0194 ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Perte de puissance a l acceleration
  - A-coups ou hesitations du moteur
  - Cliquetis cognement moteur injection defaillante
  - Voyant moteur avec codes p0190-p0194
  - Odeur carburant anormale fuite mauvaise
  - Plus de 150 000 km sur moteur diesel hdi tdi
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '817'
  intro_title: A quoi sert Capteur pression de carburant ?
  risk_title: Pourquoi remplacer Capteur pression de carburant a temps ?
  risk_explanation: '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  risk_consequences:
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  risk_conclusion: Un diagnostic precoce reduit le risque technique et financier.
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
  - question: Capteur pression carburant OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (Bosch, Delphi, Denso) pour les systèmes haute pression diesel. Les adaptables sont risqués
      sur rampe common rail.
  - question: Comment savoir si mon capteur de pression carburant est HS ?
    answer: Perte de puissance, à-coups, démarrage difficile, voyant moteur avec codes P0190 à P0194, fumée noire ou blanche.
  - question: Tous les combien changer le capteur de pression carburant ?
    answer: Pas de périodicité. Durée de vie variable selon qualité du carburant. Peut durer 200 000+ km ou moins si carburant
      de mauvaise qualité.
  - question: Peut-on changer le capteur de pression carburant soi-même ?
    answer: 'Possible mais attention : système sous haute pression (diesel). Dépressuriser avant intervention. Joint neuf
      obligatoire.'
  - question: Quelle erreur éviter avec le capteur de pression carburant ?
    answer: Ne jamais réutiliser le joint. Respecter le couple de serrage. Ne pas confondre avec le régulateur de pression.
  quality:
    score: 76
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: 0ff788ec-f3b9-5277-9fc0-831d0193c308
content_hash: sha256:67409cc68aca2a70
lang: fr
variants:
- name: Piece neuve OE/OES
  aliases:
  - neuf
  - OE
  - OES
  functional_differences:
  - Garantie constructeur ou equipementier
  - Calibration d usine
- name: Piece echange standard
  aliases:
  - echange standard
  - reconditionne
  functional_differences:
  - Moins cher
  - Piece d origine reconditionnee
location_on_vehicle:
  area: Compartiment moteur (alternateur, demarreur) ou peripherie
  access: Par le dessus (capot) ou par le dessous selon modele
  adjacent_parts:
  - faisceau electrique
  - batterie
  - fusibles
installation:
  difficulty: facile a moyen
  time: 15min a 1h
  tools:
  - cle a douille
  - multimetre
  - tournevis
  prerequisite: Debrancher la batterie avant intervention
---

# Capteur pression de carburant - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la pression du carburant dans la rampe d'injection et transmettre l'information au calculateur

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- perte de puissance a l acceleration
- a-coups ou hesitations du moteur
- cliquetis cognement moteur injection defaillante
- voyant moteur avec codes p0190-p0194
- odeur carburant anormale fuite mauvaise
- plus de 150 000 km sur moteur diesel hdi tdi

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur pression de carburant:

1. **Inspection visuelle** - Examiner l'état du capteur pression de carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-a-carburant
- pompe-a-injection

## Critères de Compatibilité

Pour commander le bon capteur pression de carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la panne"

## FAQ

**Capteur pression carburant OE ou adaptable ?**
Privilégiez l'OE ou OES (Bosch, Delphi, Denso) pour les systèmes haute pression diesel. Les adaptables sont risqués sur rampe common rail.

**Comment savoir si mon capteur de pression carburant est HS ?**
Perte de puissance, à-coups, démarrage difficile, voyant moteur avec codes P0190 à P0194, fumée noire ou blanche.

**Tous les combien changer le capteur de pression carburant ?**
Pas de périodicité. Durée de vie variable selon qualité du carburant. Peut durer 200 000+ km ou moins si carburant de mauvaise qualité.

**Peut-on changer le capteur de pression carburant soi-même ?**
Possible mais attention : système sous haute pression (diesel). Dépressuriser avant intervention. Joint neuf obligatoire.

**Quelle erreur éviter avec le capteur de pression carburant ?**
Ne jamais réutiliser le joint. Respecter le couple de serrage. Ne pas confondre avec le régulateur de pression.
