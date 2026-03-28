---
category: freinage
slug: accumulateur-de-pression
title: Accumulateur de pression
pg_id: 1064
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
  role: Stocker la pression hydraulique pour assister le freinage et maintenir la pression dans le circuit
  must_be_true:
  - stocker la pression
  - assister le freinage
  - maintenir la pression hydraulique
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: accumulateur-de-pression-de-carburant
    difference: L'accumulateur de pression freinage stocke la pression hydraulique du circuit de frein, celui de carburant
      maintient la pression dans la rampe d'injection
  - term: maitre-cylindre-de-frein
    difference: Le maitre-cylindre genere la pression, l'accumulateur la stocke
  related_parts:
  - pompe-hydraulique-systeme-de-freinage
  - maitre-cylindre-de-frein
  - agregat-de-freinage
  - flexible-de-frein
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Type de systeme de freinage (hydraulique assiste, Citroen hydractive, etc.)
  - Pression de service
  anti_mistakes:
  - universel
  - tous modeles
  - adaptable tous
  brands:
    premium:
    - Brembo
    - ATE
    - TRW
    standard:
    - Bosch
    - Ferodo
    - Textar
    budget:
    - Ridex
    - Valeo
diagnostic:
  symptoms:
  - id: S1
    label: Pedale de frein dure et difficile a enfoncer
    severity: securite
  - id: S2
    label: Pompe hydraulique qui tourne en continu ou trop souvent
    severity: securite
  - id: S3
    label: Freinage assiste defaillant apres quelques coups de frein
    severity: securite
  - id: S4
    label: Voyant de frein allume au tableau de bord
    severity: securite
  - id: S5
    label: Bruit de claquement dans le circuit de freinage
    severity: confort
  causes:
  - membrane interne de l'accumulateur percee
  - perte de pression d'azote dans la sphere
  - usure naturelle apres 100000 km ou 8-10 ans
  quick_checks:
  - 'Observer : pedale de frein dure et difficile a enfoncer ?'
  - 'Observer : pompe hydraulique qui tourne en continu ou trop souvent ?'
  - 'Observer : freinage assiste defaillant apres quelques coups de frein ?'
  - Voyant de frein allume au tableau de bord ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Verifier si la pedale devient dure apres 3-4 freinages moteur eteint. Duree de vie 80000 a 150000 km.
  wear_signs:
  - Pedale de frein dure et difficile a enfoncer
  - Pompe hydraulique qui tourne en continu ou trop souvent
  - Freinage assiste defaillant apres quelques coups de frein
  - Voyant de frein allume au tableau de bord
  - Bruit de claquement dans le circuit de freinage
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '1064'
  faq:
  - question: Comment tester l'accumulateur de pression ?
    answer: Moteur eteint, appuyer 10 fois sur la pedale de frein. Si elle devient dure des le 3eme appui, l'accumulateur
      est HS.
  - question: Peut-on rouler avec un accumulateur defaillant ?
    answer: Oui mais le freinage sera moins assiste. Intervention a prevoir rapidement pour la securite.
  - question: Accumulateur OE ou adaptable ?
    answer: Privilegier l'OE car la pression de service doit correspondre exactement aux specifications constructeur.
  - question: Combien coute un accumulateur de pression ?
    answer: Entre 80 et 400 EUR selon le vehicule. Les systemes Citroen hydractive sont plus couteux.
  - question: Quelle erreur eviter ?
    answer: Ne jamais ouvrir un accumulateur (gaz sous pression). Toujours purger le circuit de frein apres remplacement.
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
doc_id: 3069ccff-bc79-55a0-8519-4c12a236cd2d
content_hash: sha256:d02c488259e517ac
lang: fr
variants:
- name: Piece standard
  aliases:
  - standard
  - OE equivalent
  functional_differences:
  - Qualite equivalente a la monte d origine
  - Compatible avec la majorite des vehicules
- name: Piece performance/sport
  aliases:
  - sport
  - haute performance
  functional_differences:
  - Materiaux haute temperature
  - Pour usage intensif ou sportif
location_on_vehicle:
  area: Au niveau des roues (avant et/ou arriere)
  access: Demontage de la roue necessaire (cric + chandelle)
  adjacent_parts:
  - disque
  - plaquette
  - etrier
  - flexible
installation:
  difficulty: moyen
  time: 30min a 1h par essieu
  tools:
  - cle a douille
  - cle Allen
  - pied a coulisse
  - cle dynamometrique
  prerequisite: Vehicule sur chandelles, roue demontee
---

# Accumulateur de pression - Guide Diagnostic

## Fonction et Role

Stocker la pression hydraulique pour assister le freinage et maintenir la pression dans le circuit.

## Symptomes de Defaillance

- Pedale de frein dure et difficile a enfoncer
- Pompe hydraulique qui tourne en continu
- Freinage assiste defaillant apres quelques coups de frein
- Voyant de frein allume
- Bruit de claquement dans le circuit

## Pieces Associees

- pompe-hydraulique-systeme-de-freinage
- maitre-cylindre-de-frein
- agregat-de-freinage
- flexible-de-frein

## FAQ

**Comment tester l'accumulateur de pression ?**
Moteur eteint, appuyer 10 fois sur la pedale de frein. Si elle devient dure des le 3eme appui, l'accumulateur est HS.

**Peut-on rouler avec un accumulateur defaillant ?**
Oui mais le freinage sera moins assiste. Intervention a prevoir rapidement pour la securite.

**Accumulateur OE ou adaptable ?**
Privilegier l'OE car la pression de service doit correspondre exactement aux specifications constructeur.

**Combien coute un accumulateur de pression ?**
Entre 80 et 400 EUR selon le vehicule. Les systemes Citroen hydractive sont plus couteux.

**Quelle erreur eviter ?**
Ne jamais ouvrir un accumulateur (gaz sous pression). Toujours purger le circuit de frein apres remplacement.

## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Verifier si la pedale devient dure apres 3-4 freinages moteur eteint. Duree de vie 80000 a 150000 km.
