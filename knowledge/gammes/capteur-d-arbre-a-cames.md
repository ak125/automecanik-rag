---
category: moteur
slug: capteur-d-arbre-a-cames
title: Capteur d'arbre a cames
pg_id: 3946
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
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
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
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'Hall'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_0_5_mm: '0,5 mm'
    val_1_4_v: '1,4 V'
    val_10_mm: '10 mm'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Informer le calculateur de la position des arbres a cames pour l''injection sequentielle et le calage variable. Pièces
    liées : vérifier les composants adjacents lors du remplacement.'
  S2: 'Intervalle : selon constructeur. Symptômes de défaillance : - Demarrage long ou laborieux- Voyant moteur allume (codes
    P0340, P0341, P0345)- Rates d''allumage ou surconsommation- Calage moteur aleatoire- Perte de puissance'
  S3: 'Pour choisir le bon capteur d''arbre a cames pour votre véhicule : - Marque de votre vehicule- Modele de votre vehicule-
    Motorisation de votre vehicule- Annee de votre vehicule- Position (admission ou echappement si double arbre)- Type de
    capteur (inductif ou a effet Hall)- Marques : Bosch, Valeo, Denso (premium), Hella, NGK, Delphi (standard), Ridex, Topran
    (budget)- Budget : variable selon véhicule'
  S4_DEPOSE: 1. Débrancher la batterie. 2. Localiser la pièce selon la documentation constructeur. 3. Déconnecter les connecteurs
    électriques et raccords. 4. Dévisser les fixations de la pièce. 5. Déposer la pièce en notant l'orientation et la position
    de montage. 6. Nettoyer le logement et vérifier l'état des pièces adjacentes.
  S5: 'Erreurs fréquentes avec le capteur d''arbre a cames : - Ne pas vérifier la référence exacte avant commande — une pièce
    de mauvaise référence ne fonctionne pas correctement même si elle se monte physiquement- Oublier de débrancher la batterie
    avant intervention — risque de court-circuit sur les composants électroniques- Ne pas confondre capteur admission et echappement.
    Verifier le joint torique du capteur pour eviter les fuites d''huile.- Ne pas respecter le couple de serrage constructeur
    au remontage- Ignorer les symptômes d''usure en espérant que ça passe — une défaillance progressive s''aggrave toujours-
    Ne pas effacer les codes défaut après remplacement — le calculateur peut rester en mode dégradé'
  S6: 'Après le remplacement du capteur d''arbre a cames : - Controle de la tension et du courant avec un multimetre- Verifier
    les connexions electriques (oxydation, jeu)- Remplacement preventif si signes de faiblesse avant l hiver- Ne pas laisser
    le vehicule immobilise longtemps sans protection- Effacer les codes défaut éventuels avec l''outil OBD- Effectuer un essai
    route pour confirmer la disparition des symptômes'
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


## References supplementaires

<!-- materialized-from-db manual/64b8528a671a 2026-04-03 -->
### Données techniques OEM — Capteur d'arbre a cames

# Données techniques OEM — Capteur d'arbre a cames
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- Hall
- électrique

## Valeurs techniques de référence
- 0,5 mm
- 10 mm
