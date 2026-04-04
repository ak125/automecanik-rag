---
category: moteur
slug: capteur-position-papillon
title: Capteur position papillon
pg_id: 3940
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-03'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
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
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: Hall
    source_ref: corpus RAG web OEM
  - type: inductif
    source_ref: corpus RAG web OEM
  - type: pneumatique
    source_ref: corpus RAG web OEM
  - type: électrique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_0_v: 0 V
    val_0_1__: 0,1 %
    val_1_5__: 1,5 %
    val_14__: 14 %
    val_4_5__: 4,5 %
    val_400__c: 400 °C
    val_5_v: 5 V
  materials:
  - materiau: aluminium
    source_ref: corpus RAG web OEM
  - materiau: platine
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Mesurer l''angle d''ouverture du papillon des gaz pour informer le calculateur moteur de la demande du conducteur.
    Pièces liées : vérifier les composants adjacents lors du remplacement.'
  S2: 'Intervalle : selon constructeur. Symptômes de défaillance : - Ralenti instable ou irregulier- A-coups a l''acceleration-
    Perte de puissance ou reponse lente a l''accelerateur- Voyant moteur allume (codes P0120, P0121, P0122, P0123)- Moteur
    qui cale au ralenti'
  S3: 'Pour choisir le bon capteur position papillon pour votre véhicule : - Marque de votre vehicule- Modele de votre vehicule-
    Motorisation de votre vehicule- Annee de votre vehicule- Type de capteur (potentiometre ou sans contact)- Nombre de broches-
    Marques : Bosch, Valeo, Denso (premium), Hella, NGK, Delphi (standard), Ridex, Topran (budget)- Budget : variable selon
    véhicule'
  S4_DEPOSE: 1. Débrancher la batterie. 2. Localiser la pièce selon la documentation constructeur. 3. Déconnecter les connecteurs
    électriques et raccords. 4. Dévisser les fixations de la pièce. 5. Déposer la pièce en notant l'orientation et la position
    de montage. 6. Nettoyer le logement et vérifier l'état des pièces adjacentes.
  S5: 'Erreurs fréquentes avec le capteur position papillon : - Ne pas vérifier la référence exacte avant commande — une pièce
    de mauvaise référence ne fonctionne pas correctement même si elle se monte physiquement- Oublier de débrancher la batterie
    avant intervention — risque de court-circuit sur les composants électroniques- Ne pas forcer le capteur sur l''axe du
    papillon. Certains capteurs necessitent un apprentissage (reset adaptation) apres remplacement.- Ne pas respecter le couple
    de serrage constructeur au remontage- Ignorer les symptômes d''usure en espérant que ça passe — une défaillance progressive
    s''aggrave toujours- Ne pas effacer les codes défaut après remplacement — le calculateur peut rester en mode dégradé'
  S6: 'Après le remplacement du capteur position papillon : - Controle de la tension et du courant avec un multimetre- Verifier
    les connexions electriques (oxydation, jeu)- Remplacement preventif si signes de faiblesse avant l hiver- Ne pas laisser
    le vehicule immobilise longtemps sans protection- Effacer les codes défaut éventuels avec l''outil OBD- Effectuer un essai
    route pour confirmer la disparition des symptômes'
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


## References supplementaires

<!-- materialized-from-db manual/3cc575a345fc 2026-04-03 -->
### Données techniques OEM — Capteur position papillon

# Données techniques OEM — Capteur position papillon
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- Hall
- inductif
- pneumatique
- électrique

## Matériaux
- aluminium
- platine

## Valeurs techniques de référence
- 0,1 %
- 1,5 %
- 14 %
- 4,5 %
- 400 °C
