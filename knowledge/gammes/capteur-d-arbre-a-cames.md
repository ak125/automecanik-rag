---
category: moteur
slug: capteur-d-arbre-a-cames
title: Capteur d'arbre a cames
pg_id: 3946
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
  role: Informer le calculateur de la position des arbres a cames pour l'injection sequentielle et le calage variable
  must_be_true:
  - position des cames
  - injection sequentielle
  - signal au calculateur
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: capteur-vilebrequin
    difference: Le capteur arbre a cames mesure la position des cames (haut moteur), le capteur vilebrequin mesure la rotation
      du vilebrequin (bas moteur)
  related_parts:
  - capteur-vilebrequin
  - chaine-de-distribution
  - poulie-d-arbre-a-came
  - arbre-a-came
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Position (admission ou echappement si double arbre)
  - Type de capteur (inductif ou a effet Hall)
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
    label: Demarrage long ou laborieux
    severity: confort
  - id: S2
    label: Voyant moteur allume (codes P0340, P0341, P0345)
    severity: confort
  - id: S3
    label: Rates d'allumage ou surconsommation
    severity: confort
  - id: S4
    label: Calage moteur aleatoire
    severity: securite
  - id: S5
    label: Perte de puissance
    severity: confort
  causes:
  - entrefer trop grand entre capteur et cible sur arbre a cames
  - connecteur oxyde ou fil endommage
  - usure du capteur magnetique par la chaleur
  quick_checks:
  - 'Observer : demarrage long ou laborieux ?'
  - Voyant moteur allume (codes P0340, P0341, P0345) ?
  - 'Comparer la consommation : rates d''allumage ou surconsommation ?'
  - 'Observer : calage moteur aleatoire ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Pas de periodicite. Verifier en cas de voyant moteur ou demarrage difficile.
  wear_signs:
  - Demarrage long ou laborieux
  - Voyant moteur allume (codes P0340, P0341, P0345)
  - Rates d'allumage ou surconsommation
  - Calage moteur aleatoire
  - Perte de puissance
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '3946'
  faq:
  - question: Comment tester le capteur d'arbre a cames ?
    answer: Scanner OBD pour codes P0340/P0341/P0345. Mesurer resistance et signal avec multimetre/oscilloscope.
  - question: Capteur arbre a cames OE ou adaptable ?
    answer: Privilegier OE ou OES. Le signal doit etre precis pour le calage injection sequentielle.
  - question: Peut-on rouler sans capteur arbre a cames ?
    answer: Le moteur peut tourner en mode degrade (injection simultanee) mais avec perte de puissance et surconsommation.
  - question: Attention admission ou echappement ?
    answer: Sur les moteurs double arbre a cames, il y a un capteur par arbre. Verifier la position avant commande.
  - question: Quelle erreur eviter ?
    answer: Ne pas confondre capteur admission et echappement. Verifier le joint torique du capteur pour eviter les fuites
      d'huile.
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
doc_id: 7ba29d01-3878-52a5-9ecf-f6cf60ecff68
content_hash: sha256:5cbe760fb0eaa3e7
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

# Capteur d'arbre a cames - Guide Diagnostic

## Fonction et Role

Informer le calculateur de la position des arbres a cames pour l'injection sequentielle.

## Symptomes de Defaillance

- Demarrage long ou laborieux
- Voyant moteur (P0340, P0341, P0345)
- Rates d'allumage ou surconsommation
- Calage moteur aleatoire
- Perte de puissance

## Pieces Associees

- capteur-vilebrequin
- chaine-de-distribution
- poulie-d-arbre-a-came
- arbre-a-came

## FAQ

**Comment tester le capteur d'arbre a cames ?**
Scanner OBD pour codes P0340/P0341/P0345. Mesurer resistance et signal avec multimetre/oscilloscope.

**Capteur arbre a cames OE ou adaptable ?**
Privilegier OE ou OES. Le signal doit etre precis pour le calage injection sequentielle.

**Peut-on rouler sans capteur arbre a cames ?**
Le moteur peut tourner en mode degrade (injection simultanee) mais avec perte de puissance et surconsommation.

**Attention admission ou echappement ?**
Sur les moteurs double arbre a cames, il y a un capteur par arbre. Verifier la position avant commande.

**Quelle erreur eviter ?**
Ne pas confondre capteur admission et echappement. Verifier le joint torique du capteur pour eviter les fuites d'huile.

## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Pas de periodicite. Verifier en cas de voyant moteur ou demarrage difficile.
