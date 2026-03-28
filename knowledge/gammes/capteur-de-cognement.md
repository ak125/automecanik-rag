---
category: capteurs
slug: capteur-de-cognement
title: Capteur de cognement
pg_id: 3921
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
  role: Detecter les vibrations anormales du moteur liees au cliquetis et informer le calculateur pour ajuster l'avance
  must_be_true:
  - detecter
  - mesurer
  - transmettre
  must_not_contain:
  - allumage
  - bougie
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
    min: 30
    max: 100
    currency: EUR
    unit: capteur
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: 'Capteur certifié constructeur : sensibilité piézoélectrique, fréquence de résonance et connecteur conformes
      à la cartographie moteur d''origine. Pas d''apprentissage nécessaire.'
  - tier: Qualité équivalente OE
    description: Capteur d'un équipementier électronique de rang 1. Sensibilité et connecteur conformes. Fiabilité de signal
      compatible avec le calculateur d'injection d'origine.
  - tier: Adaptable compatible
    description: Capteur compatible avec plusieurs références proches. Vérifier le couple de montage (généralement entre 15
      et 25 Nm), le type de connecteur et la position sur le bloc moteur.
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
    label: Voyant moteur allume avec code p0325 ou p0327
    severity: confort
  - id: S2
    label: Cliquetis metallique a l acceleration detonation
    severity: confort
  - id: S3
    label: Perte de puissance notable allumage retarde
    severity: confort
  - id: S4
    label: Surconsommation de carburant anormale
    severity: confort
  - id: S5
    label: Fumee noire a l echappement
    severity: confort
  - id: S6
    label: Moteur qui chauffe plus que d habitude
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'Usure ou defaillance causant : voyant moteur allume avec code p0325 ou p0327'
  quick_checks:
  - Voyant moteur allume avec code p0325 ou p0327 ?
  - 'Observer : cliquetis metallique a l acceleration detonation ?'
  - 'Observer : perte de puissance notable allumage retarde ?'
  - 'Comparer la consommation : surconsommation de carburant anormale ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant moteur allume avec code p0325 ou p0327
  - Cliquetis metallique a l acceleration detonation
  - Perte de puissance notable allumage retarde
  - Surconsommation de carburant anormale
  - Fumee noire a l echappement
  - Moteur qui chauffe plus que d habitude
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '3921'
  intro_title: A quoi sert Capteur de cognement ?
  risk_title: Pourquoi remplacer Capteur de cognement a temps ?
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
  - question: Capteur de cognement OE ou adaptable ?
    answer: Les capteurs OES (Bosch, Hella, Denso) garantissent une sensibilité calibrée. Les adaptables peuvent générer des
      faux positifs ou manquer des détonations réelles.
  - question: Comment savoir si mon capteur de cognement est HS ?
    answer: Voyant moteur allumé, code P0325/P0327, perte de puissance, consommation excessive, cliquetis audible que le calculateur
      ne corrige plus.
  - question: Tous les combien changer le capteur de cognement ?
    answer: Pas de périodicité. Pièce électronique qui dure généralement toute la vie du moteur sauf défaillance ou choc.
  - question: Peut-on changer le capteur de cognement soi-même ?
    answer: Oui, opération simple. Débrancher la batterie, dévisser le capteur (souvent une vis), rebrancher. Respecter le
      couple de serrage (20-25 Nm).
  - question: Quelle erreur éviter avec le capteur de cognement ?
    answer: Ne pas serrer trop fort (fausse les mesures). Ne pas utiliser de joint non prévu. Vérifier l'absence de fissure
      sur le bloc moteur.
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
doc_id: d997aa30-7070-5ef5-be4b-cf237b845b61
content_hash: sha256:26693014f512ead3
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

# Capteur de cognement - Guide Diagnostic Complet

## Fonction et Rôle

Detecter les vibrations anormales du moteur liees au cliquetis et informer le calculateur pour ajuster l'avance

**Actions principales:** detecter, mesurer, transmettre, analyser

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant moteur allume avec code p0325 ou p0327
- cliquetis metallique a l acceleration detonation
- perte de puissance notable allumage retarde
- surconsommation de carburant anormale
- fumee noire a l echappement
- moteur qui chauffe plus que d habitude

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur de cognement:

1. **Inspection visuelle** - Examiner l'état du capteur de cognement
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

- capteur-impulsion
- corps-papillon
- debitmetre-d-air
- injecteur

## Critères de Compatibilité

Pour commander le bon capteur de cognement, vous devez connaître:

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

**Capteur de cognement OE ou adaptable ?**
Les capteurs OES (Bosch, Hella, Denso) garantissent une sensibilité calibrée. Les adaptables peuvent générer des faux positifs ou manquer des détonations réelles.

**Comment savoir si mon capteur de cognement est HS ?**
Voyant moteur allumé, code P0325/P0327, perte de puissance, consommation excessive, cliquetis audible que le calculateur ne corrige plus.

**Tous les combien changer le capteur de cognement ?**
Pas de périodicité. Pièce électronique qui dure généralement toute la vie du moteur sauf défaillance ou choc.

**Peut-on changer le capteur de cognement soi-même ?**
Oui, opération simple. Débrancher la batterie, dévisser le capteur (souvent une vis), rebrancher. Respecter le couple de serrage (20-25 Nm).

**Quelle erreur éviter avec le capteur de cognement ?**
Ne pas serrer trop fort (fausse les mesures). Ne pas utiliser de joint non prévu. Vérifier l'absence de fissure sur le bloc moteur.
