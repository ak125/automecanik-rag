---
category: capteurs
slug: capteur-de-pedale-d-accelerateur
title: Capteur de pédale d'accélérateur
pg_id: 3908
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
  role: Mesurer la position de la pedale d'accelerateur et transmettre la demande du conducteur au calculateur
  must_be_true:
  - mesurer
  - detecter
  - transmettre
  must_not_contain:
  - papillon
  - admission
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
    min: 80
    max: 300
    currency: EUR
    unit: l'unite
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
    label: Accelerations irregulieres ou saccadees
    severity: confort
  - id: S2
    label: Mode degrade moteur active
    severity: confort
  - id: S3
    label: Voyant moteur avec code pedale
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'Usure ou defaillance causant : accelerations irregulieres ou saccadees'
  quick_checks:
  - 'Observer : accelerations irregulieres ou saccadees ?'
  - 'Observer : mode degrade moteur active ?'
  - Voyant moteur avec code pedale ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Accelerations irregulieres ou saccadees
  - Mode degrade moteur active
  - Voyant moteur avec code pedale
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '3908'
  intro_title: A quoi sert Capteur de pédale d'accélérateur ?
  risk_title: Pourquoi remplacer Capteur de pédale d'accélérateur a temps ?
  risk_explanation: '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  risk_consequences:
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  - '**Défaillance progressive** - Usure normale due à l''utilisation'
  - '**Conditions d''utilisation** - Sollicitations excessives ou environnement défavorable'
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
  - question: Comment choisir Capteur de pédale d'accélérateur compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Capteur de pédale d'accélérateur ?
    answer: En cas de accelerations irregulieres ou saccadees ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Capteur de pédale d'accélérateur sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
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
doc_id: 2985cb6a-3075-554c-bce7-6dddac8e76f4
content_hash: sha256:20997b1c58742f35
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

# Capteur de pédale d'accélérateur - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la position de la pedale d'accelerateur et transmettre la demande du conducteur au calculateur

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- accelerations irregulieres ou saccadees
- mode degrade moteur active
- voyant moteur avec code pedale

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur de pédale d'accélérateur:

1. **Inspection visuelle** - Examiner l'état du capteur de pédale d'accélérateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-position-papillon

## Critères de Compatibilité

Pour commander le bon capteur de pédale d'accélérateur, vous devez connaître:

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

**Comment choisir Capteur de pédale d'accélérateur compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Capteur de pédale d'accélérateur ?**
En cas de accelerations irregulieres ou saccadees ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Capteur de pédale d'accélérateur sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
