---
category: moteur
slug: palpeur-de-regime-gestion-moteur
title: Palpeur de regime gestion moteur
pg_id: 3896
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-21'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: low
lifecycle:
  stage: v4_converted
  last_enriched_by: script:rag-fill-remaining-gaps
  last_enriched_at: '2026-03-28'
domain:
  role: Mesurer le regime moteur pour transmettre l'information au calculateur de gestion moteur
  must_be_true:
  - mesurer le regime
  - transmettre au calculateur
  - signal de rotation
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: capteur-vilebrequin
    difference: Le palpeur de regime est souvent un synonyme du capteur vilebrequin, mais peut designer un capteur specifique
      sur certains moteurs anciens
  - term: capteur-impulsion
    difference: Le capteur d'impulsion mesure les impulsions de la couronne dentee, le palpeur de regime mesure la vitesse
      de rotation
  related_parts:
  - capteur-vilebrequin
  - bobine-d-allumage
  - calculateur-moteur
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
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Compte-tours inoperant ou instable
    severity: confort
  - id: S2
    label: Coupures moteur aleatoires
    severity: securite
  - id: S3
    label: Voyant moteur allume (codes P0335, P0336)
    severity: confort
  - id: S4
    label: Rates d'allumage ou moteur qui hesite
    severity: confort
  - id: S5
    label: Moteur ne demarre pas (pas de signal regime)
    severity: securite
  causes:
  - entrefer trop grand entre capteur et couronne dentee
  - fil de signal endommage ou connecteur oxyde
  - usure du capteur magnetique
  quick_checks:
  - 'Observer : compte-tours inoperant ou instable ?'
  - 'Observer : coupures moteur aleatoires ?'
  - Voyant moteur allume (codes P0335, P0336) ?
  - 'Observer : rates d''allumage ou moteur qui hesite ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Pas de periodicite fixe. Verifier en cas de voyant moteur ou instabilite du regime.
  wear_signs:
  - Compte-tours inoperant ou instable
  - Coupures moteur aleatoires
  - Voyant moteur allume (codes P0335, P0336)
  - Rates d'allumage ou moteur qui hesite
  - Moteur ne demarre pas (pas de signal regime)
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '3896'
  faq:
  - question: Comment tester le palpeur de regime ?
    answer: Verifier la resistance avec un multimetre (valeur constructeur, generalement 200 a 1000 ohms pour un inductif).
      Scanner OBD pour codes P0335/P0336.
  - question: Palpeur de regime et capteur vilebrequin, c'est la meme chose ?
    answer: Souvent oui, mais sur certains moteurs anciens le palpeur de regime est un capteur distinct monte sur le volant
      moteur.
  - question: Peut-on rouler sans palpeur de regime ?
    answer: Non, sans signal de regime le calculateur ne peut pas gerer l'injection ni l'allumage. Le moteur cale ou ne demarre
      pas.
  - question: Palpeur OE ou adaptable ?
    answer: Privilegier l'OE ou OES (Bosch, Hella). Les capteurs generiques peuvent avoir un signal trop faible ou un entrefer
      inadequat.
  - question: Quelle erreur eviter ?
    answer: Ne pas forcer le capteur dans son logement (risque de casser). Respecter l'entrefer specifie par le constructeur.
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
doc_id: ad2cb6be-a5a9-543a-818e-2ac4b1a69bff
content_hash: sha256:eb4ea7b423749fb4
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
  area: Sur le vehicule (position variable selon modele)
  access: Consulter la revue technique du vehicule
  adjacent_parts:
  - pieces adjacentes du meme systeme
installation:
  difficulty: variable
  time: consulter revue technique
  tools:
  - outillage standard
  prerequisite: Consulter la procedure constructeur
---

# Palpeur de regime gestion moteur - Guide Diagnostic

## Fonction et Role

Mesurer le regime moteur pour transmettre l'information au calculateur de gestion moteur.

## Symptomes de Defaillance

- Compte-tours inoperant ou instable
- Coupures moteur aleatoires
- Voyant moteur allume (codes P0335, P0336)
- Rates d'allumage
- Moteur ne demarre pas

## Pieces Associees

- capteur-vilebrequin
- bobine-d-allumage
- calculateur-moteur

## FAQ

**Comment tester le palpeur de regime ?**
Verifier la resistance avec un multimetre (valeur constructeur, generalement 200 a 1000 ohms pour un inductif). Scanner OBD pour codes P0335/P0336.

**Palpeur de regime et capteur vilebrequin, c'est la meme chose ?**
Souvent oui, mais sur certains moteurs anciens le palpeur de regime est un capteur distinct monte sur le volant moteur.

**Peut-on rouler sans palpeur de regime ?**
Non, sans signal de regime le calculateur ne peut pas gerer l'injection ni l'allumage. Le moteur cale ou ne demarre pas.

**Palpeur OE ou adaptable ?**
Privilegier l'OE ou OES (Bosch, Hella). Les capteurs generiques peuvent avoir un signal trop faible ou un entrefer inadequat.

**Quelle erreur eviter ?**
Ne pas forcer le capteur dans son logement (risque de casser). Respecter l'entrefer specifie par le constructeur.

## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Pas de periodicite fixe. Verifier en cas de voyant moteur ou instabilite du regime.
