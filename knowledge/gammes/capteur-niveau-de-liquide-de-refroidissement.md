---
category: refroidissement
slug: capteur-niveau-de-liquide-de-refroidissement
title: Capteur niveau de liquide de refroidissement
pg_id: 1288
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-21'
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
  role: Detecter le niveau de liquide de refroidissement et alerter le conducteur en cas de niveau bas
  must_be_true:
  - detecter le niveau
  - liquide de refroidissement
  - alerter le conducteur
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: sonde-de-refroidissement
    difference: La sonde mesure la temperature du liquide, le capteur de niveau detecte si le niveau est suffisant
  - term: bouchon-vase-expansion
    difference: Le bouchon assure la pression du circuit, le capteur mesure le niveau dans le vase
  related_parts:
  - vase-d-expansion
  - bouchon-vase-expansion
  - durite-de-refroidissement
  - sonde-de-refroidissement
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Type de capteur (flotteur magnetique, thermistance, ultrason)
  anti_mistakes:
  - universel
  - tous modeles
  - adaptable tous
  brands:
    premium:
    - Behr/Mahle
    - Gates
    standard:
    - Valeo
    - NRF
    - Febi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Voyant niveau liquide de refroidissement allume alors que le niveau est correct
    severity: confort
  - id: S2
    label: Pas d'alerte malgre un niveau bas reel
    severity: securite
  - id: S3
    label: Alerte intermittente en virage ou sur route bosselee
    severity: confort
  - id: S4
    label: Surchauffe moteur non detectee a temps
    severity: securite
  causes:
  - flotteur bloque par des depots de tartre ou de rouille
  - connecteur oxyde ou fil coupe
  - capteur thermistance defaillant (court-circuit ou circuit ouvert)
  depose_steps:
  - Laisser refroidir le moteur et ouvrir le bouchon du vase d'expansion pour depressuriser
  - Localiser le capteur de niveau sur le vase d'expansion (connecteur electrique visible)
  - Debrancher le connecteur electrique du capteur (languette de verrouillage)
  - Deposer le capteur par rotation (quart de tour) ou devisser selon le modele
  - Installer le nouveau capteur avec son joint neuf, reconnecter le connecteur
  - Completer le niveau de liquide de refroidissement si necessaire, purger le circuit
  quick_checks:
  - Voyant niveau liquide de refroidissement allume alors que le niveau est correct ?
  - 'Observer : pas d''alerte malgre un niveau bas reel ?'
  - 'Observer : alerte intermittente en virage ou sur route bosselee ?'
  - 'Observer : surchauffe moteur non detectee a temps ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Verifier le bon fonctionnement du voyant a chaque vidange de liquide de refroidissement.
  wear_signs:
  - Voyant niveau liquide de refroidissement allume alors que le niveau est correct
  - Pas d'alerte malgre un niveau bas reel
  - Alerte intermittente en virage ou sur route bosselee
  - Surchauffe moteur non detectee a temps
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '1288'
  faq:
  - question: Comment tester le capteur niveau LDR ?
    answer: Debrancher le connecteur, le voyant doit s'allumer (alerte niveau bas). Si non, verifier le faisceau et le capteur.
  - question: Capteur OE ou adaptable ?
    answer: Privilegier OE pour la fiabilite. Le capteur de niveau est une piece de securite.
  - question: Peut-on rouler avec un capteur defaillant ?
    answer: Oui mais sans alerte en cas de fuite, risque de surchauffe moteur non detectee. Verifier le niveau manuellement.
  - question: Tous les combien changer ?
    answer: Pas de periodicite. Remplacer si le voyant reste allume malgre un niveau correct ou si pas d'alerte malgre niveau
      bas.
  - question: Quelle erreur eviter ?
    answer: Ne pas oublier de purger le circuit de refroidissement apres intervention sur le vase d'expansion.
  quality:
    score: 60
    source: manual:claude-r3-kp
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modeles
  - adaptable tous
  requires_vehicle: true
doc_id: 58c757e2-3740-5935-976f-3eb4b9219f1e
content_hash: sha256:4f1849d5ca7ecc25
lang: fr
variants:
- name: Version OE (origine)
  aliases:
  - OE
  - constructeur
  functional_differences:
  - Reference constructeur exacte
  - Garantie et compatibilite maximales
- name: Version equivalente OES
  aliases:
  - OES
  - equipementier
  functional_differences:
  - Qualite equivalente, prix aftermarket
  - Equipementier de premier monte
location_on_vehicle:
  area: Face avant du vehicule (radiateur) et bloc moteur
  access: Par le dessus (capot) ou face avant
  adjacent_parts:
  - radiateur
  - durites
  - pompe a eau
  - thermostat
installation:
  difficulty: moyen
  time: 30min a 2h
  tools:
  - tournevis
  - pince de serrage
  - bac de recuperation
  prerequisite: Moteur froid, circuit vidange avant depose
---

# Capteur niveau de liquide de refroidissement - Guide Diagnostic

## Fonction et Role

Detecter le niveau de liquide de refroidissement et alerter en cas de niveau bas.

## Symptomes de Defaillance

- Voyant allume malgre niveau correct
- Pas d'alerte malgre niveau bas reel
- Alerte intermittente en virage
- Surchauffe non detectee

## Pieces Associees

- vase-d-expansion
- bouchon-vase-expansion
- durite-de-refroidissement
- sonde-de-refroidissement

## FAQ

**Comment tester le capteur niveau LDR ?**
Debrancher le connecteur, le voyant doit s'allumer (alerte niveau bas). Si non, verifier le faisceau et le capteur.

**Capteur OE ou adaptable ?**
Privilegier OE pour la fiabilite. Le capteur de niveau est une piece de securite.

**Peut-on rouler avec un capteur defaillant ?**
Oui mais sans alerte en cas de fuite, risque de surchauffe moteur non detectee. Verifier le niveau manuellement.

**Tous les combien changer ?**
Pas de periodicite. Remplacer si le voyant reste allume malgre un niveau correct ou si pas d'alerte malgre niveau bas.

**Quelle erreur eviter ?**
Ne pas oublier de purger le circuit de refroidissement apres intervention sur le vase d'expansion.

## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Verifier le bon fonctionnement du voyant a chaque vidange de liquide de refroidissement.
