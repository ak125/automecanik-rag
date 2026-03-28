---
category: moteur
slug: capteur-vilebrequin
title: Capteur vilebrequin
pg_id: 833
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
  role: Mesurer la vitesse de rotation et la position du vilebrequin pour le calculateur moteur
  must_be_true:
  - mesurer la position
  - vitesse de rotation
  - signal au calculateur
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: capteur-d-arbre-a-cames
    difference: Le capteur vilebrequin mesure la rotation du vilebrequin (bas moteur), le capteur arbre a cames mesure la
      position des cames (haut moteur)
  - term: capteur-impulsion
    difference: Le capteur d'impulsion est un terme generique, le capteur vilebrequin est specifique a la position du vilebrequin
  related_parts:
  - capteur-d-arbre-a-cames
  - bobine-d-allumage
  - courroie-de-distribution
  - volant-moteur
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Type de capteur (inductif ou a effet Hall)
  - Nombre de broches du connecteur
  anti_mistakes:
  - universel
  - tous modeles
  - adaptable tous
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
    label: Moteur ne demarre pas (pas de signal de rotation)
    severity: securite
  - id: S2
    label: Calages aleatoires en roulant
    severity: securite
  - id: S3
    label: Perte de puissance intermittente
    severity: confort
  - id: S4
    label: Voyant moteur allume (codes P0335, P0336, P0337)
    severity: confort
  - id: S5
    label: Rates d'allumage ou tremblements moteur
    severity: confort
  - id: S6
    label: Demarrage long ou difficile a chaud
    severity: confort
  causes:
  - entrefer trop grand entre capteur et couronne dentee du volant moteur
  - fil de signal coupe ou connecteur oxyde
  - aimant du capteur desaimante par la chaleur
  quick_checks:
  - 'Observer : moteur ne demarre pas (pas de signal de rotation) ?'
  - 'Observer : calages aleatoires en roulant ?'
  - 'Observer : perte de puissance intermittente ?'
  - Voyant moteur allume (codes P0335, P0336, P0337) ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Pas de periodicite fixe. Remplacer en cas de codes defaut P0335/P0336 confirmes.
  wear_signs:
  - Moteur ne demarre pas (pas de signal de rotation)
  - Calages aleatoires en roulant
  - Perte de puissance intermittente
  - Voyant moteur allume (codes P0335, P0336, P0337)
  - Rates d'allumage ou tremblements moteur
  - Demarrage long ou difficile a chaud
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '833'
  faq:
  - question: Comment tester le capteur vilebrequin ?
    answer: Mesurer la resistance (200-1000 ohms pour inductif). Scanner OBD pour codes P0335/P0336. Verifier le signal avec
      un oscilloscope si disponible.
  - question: Capteur vilebrequin OE ou adaptable ?
    answer: Privilegier OE ou OES (Bosch, Hella, Continental). Les generiques peuvent avoir un signal trop faible.
  - question: Peut-on rouler sans capteur vilebrequin ?
    answer: Non, le calculateur ne peut pas gerer injection ni allumage sans ce signal. Le moteur cale ou ne demarre pas.
  - question: Tous les combien changer le capteur vilebrequin ?
    answer: Pas de periodicite fixe. Duree de vie generalement superieure a 200000 km sauf defaut electrique.
  - question: Quelle erreur eviter ?
    answer: Ne pas forcer le capteur dans son logement. Respecter l'entrefer. Ne pas confondre avec le capteur d'arbre a cames.
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
doc_id: 39efa841-a6c8-5725-8f8d-16b93552f839
content_hash: sha256:193aec1b4907e18b
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

# Capteur vilebrequin - Guide Diagnostic

## Fonction et Role

Mesurer la vitesse de rotation et la position du vilebrequin pour le calculateur moteur.

## Symptomes de Defaillance

- Moteur ne demarre pas
- Calages aleatoires en roulant
- Perte de puissance intermittente
- Voyant moteur allume (P0335, P0336)
- Rates d'allumage
- Demarrage long a chaud

## Pieces Associees

- capteur-d-arbre-a-cames
- bobine-d-allumage
- courroie-de-distribution
- volant-moteur

## FAQ

**Comment tester le capteur vilebrequin ?**
Mesurer la resistance (200-1000 ohms pour inductif). Scanner OBD pour codes P0335/P0336. Verifier le signal avec un oscilloscope si disponible.

**Capteur vilebrequin OE ou adaptable ?**
Privilegier OE ou OES (Bosch, Hella, Continental). Les generiques peuvent avoir un signal trop faible.

**Peut-on rouler sans capteur vilebrequin ?**
Non, le calculateur ne peut pas gerer injection ni allumage sans ce signal. Le moteur cale ou ne demarre pas.

**Tous les combien changer le capteur vilebrequin ?**
Pas de periodicite fixe. Duree de vie generalement superieure a 200000 km sauf defaut electrique.

**Quelle erreur eviter ?**
Ne pas forcer le capteur dans son logement. Respecter l'entrefer. Ne pas confondre avec le capteur d'arbre a cames.

## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Pas de periodicite fixe. Remplacer en cas de codes defaut P0335/P0336 confirmes.
