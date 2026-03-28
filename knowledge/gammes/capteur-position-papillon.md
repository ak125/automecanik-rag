---
category: moteur
slug: capteur-position-papillon
title: Capteur position papillon
pg_id: 3940
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
  role: Mesurer l'angle d'ouverture du papillon des gaz pour informer le calculateur moteur de la demande du conducteur
  must_be_true:
  - mesurer l'angle
  - ouverture du papillon
  - signal au calculateur
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: corps-papillon
    difference: Le capteur mesure l'angle, le corps papillon est l'ensemble mecanique complet incluant le volet et le moteur
      pas-a-pas
  - term: capteur-de-pedale-d-accelerateur
    difference: Le capteur pedale mesure l'enfoncement de la pedale, le capteur papillon mesure l'ouverture reelle du volet
  related_parts:
  - corps-papillon
  - capteur-de-pedale-d-accelerateur
  - debitmetre-d-air
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Type de capteur (potentiometre ou sans contact)
  - Nombre de broches
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
    label: Ralenti instable ou irregulier
    severity: confort
  - id: S2
    label: A-coups a l'acceleration
    severity: confort
  - id: S3
    label: Perte de puissance ou reponse lente a l'accelerateur
    severity: confort
  - id: S4
    label: Voyant moteur allume (codes P0120, P0121, P0122, P0123)
    severity: confort
  - id: S5
    label: Moteur qui cale au ralenti
    severity: securite
  causes:
  - usure de la piste resistive du potentiometre
  - connecteur oxyde ou fil endommage
  - encrassement du papillon affectant le signal
  quick_checks:
  - 'Observer : ralenti instable ou irregulier ?'
  - 'Observer : a-coups a l''acceleration ?'
  - 'Observer : perte de puissance ou reponse lente a l''accelerateur ?'
  - Voyant moteur allume (codes P0120, P0121, P0122, P0123) ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Pas de periodicite. Nettoyer le corps papillon regulierement peut prolonger la duree de vie du capteur.
  wear_signs:
  - Ralenti instable ou irregulier
  - A-coups a l'acceleration
  - Perte de puissance ou reponse lente a l'accelerateur
  - Voyant moteur allume (codes P0120, P0121, P0122, P0123)
  - Moteur qui cale au ralenti
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '3940'
  faq:
  - question: Comment tester le capteur position papillon ?
    answer: Scanner OBD pour codes P0120-P0123. Verifier la tension (0.5V ferme, 4.5V ouvert). Le signal doit varier lineairement
      sans sauts.
  - question: Capteur papillon OE ou adaptable ?
    answer: Privilegier OE car la precision du signal est critique pour la gestion moteur. Les generiques peuvent avoir des
      zones mortes.
  - question: Peut-on rouler avec un capteur papillon defaillant ?
    answer: Le moteur passe en mode degrade (puissance limitee). Rouler prudemment et faire remplacer rapidement.
  - question: Capteur integre ou separe du corps papillon ?
    answer: Sur les vehicules recents, le capteur est souvent integre au corps papillon (remplacement en bloc). Sur les anciens,
      il est separable.
  - question: Quelle erreur eviter ?
    answer: Ne pas forcer le capteur sur l'axe du papillon. Certains capteurs necessitent un apprentissage (reset adaptation)
      apres remplacement.
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
doc_id: 5576fd1b-a082-5bfb-88f2-12ba5db1dc93
content_hash: sha256:352269eb3a14b81e
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

# Capteur position papillon - Guide Diagnostic

## Fonction et Role

Mesurer l'angle d'ouverture du papillon des gaz pour le calculateur moteur.

## Symptomes de Defaillance

- Ralenti instable
- A-coups a l'acceleration
- Perte de puissance
- Voyant moteur (P0120-P0123)
- Moteur qui cale au ralenti

## Pieces Associees

- corps-papillon
- capteur-de-pedale-d-accelerateur
- debitmetre-d-air

## FAQ

**Comment tester le capteur position papillon ?**
Scanner OBD pour codes P0120-P0123. Verifier la tension (0.5V ferme, 4.5V ouvert). Le signal doit varier lineairement sans sauts.

**Capteur papillon OE ou adaptable ?**
Privilegier OE car la precision du signal est critique pour la gestion moteur. Les generiques peuvent avoir des zones mortes.

**Peut-on rouler avec un capteur papillon defaillant ?**
Le moteur passe en mode degrade (puissance limitee). Rouler prudemment et faire remplacer rapidement.

**Capteur integre ou separe du corps papillon ?**
Sur les vehicules recents, le capteur est souvent integre au corps papillon (remplacement en bloc). Sur les anciens, il est separable.

**Quelle erreur eviter ?**
Ne pas forcer le capteur sur l'axe du papillon. Certains capteurs necessitent un apprentissage (reset adaptation) apres remplacement.

## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Pas de periodicite. Nettoyer le corps papillon regulierement peut prolonger la duree de vie du capteur.
