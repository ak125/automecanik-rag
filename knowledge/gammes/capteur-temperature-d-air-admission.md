---
category: capteurs
slug: capteur-temperature-d-air-admission
title: Capteur température d'air admission
pg_id: 3939
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
  role: Mesurer la temperature de l'air entrant dans le moteur pour optimiser le melange air-carburant
  must_be_true:
  - mesurer
  - detecter
  - transmettre
  must_not_contain:
  - echappement
  - refroidissement
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
    min: 15
    max: 50
    currency: EUR
    unit: capteur
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
    label: Surconsommation de carburant anormale
    severity: confort
  - id: S2
    label: Ralenti instable surtout a froid
    severity: confort
  - id: S3
    label: Sifflement anormal a l admission
    severity: confort
  - id: S4
    label: Fumee noire a l echappement
    severity: confort
  - id: S5
    label: Odeur de carburant non brule
    severity: confort
  - id: S6
    label: Plus de 150 000 km sans verification
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - remplacement preventif recommande
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - 'Comparer la consommation : surconsommation de carburant anormale ?'
  - 'Observer : ralenti instable surtout a froid ?'
  - 'Observer : sifflement anormal a l admission ?'
  - 'Observer : fumee noire a l echappement ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Surconsommation de carburant anormale
  - Ralenti instable surtout a froid
  - Sifflement anormal a l admission
  - Fumee noire a l echappement
  - Odeur de carburant non brule
  - Plus de 150 000 km sans verification
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '3939'
  intro_title: A quoi sert Capteur température d'air admission ?
  risk_title: Pourquoi remplacer Capteur température d'air admission a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Capteur IAT OE ou adaptable ?
    answer: Les adaptables (Febi, FAE, NTK) fonctionnent bien pour cette pièce simple. Vérifiez le type de connecteur et la
      plage de mesure.
  - question: Comment savoir si mon capteur IAT est HS ?
    answer: Surconsommation, ralenti instable à froid, voyant moteur avec codes P0110 à P0114, démarrage difficile par temps
      froid.
  - question: Tous les combien changer le capteur IAT ?
    answer: Pas de périodicité. Pièce simple qui dure généralement toute la vie du véhicule. À remplacer uniquement si défaillant.
  - question: Peut-on changer le capteur IAT soi-même ?
    answer: Oui, très facile si séparé. Sur le conduit d'admission, un connecteur, parfois une vis. 10 minutes maximum.
  - question: Quelle erreur éviter avec le capteur IAT ?
    answer: Ne pas confondre avec la sonde de température moteur. Vérifier s'il est intégré au débitmètre avant de commander
      séparément.
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
doc_id: 5469890a-5828-5b98-a9cb-54a8155cc07b
content_hash: sha256:29e0688743083d58
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
  S1: 'Mesurer la temperature de l''air entrant dans le moteur pour optimiser le melange air-carburant. Pièces liées : vérifier
    les composants adjacents lors du remplacement.'
  S2: 'Intervalle : selon constructeur. Symptômes de défaillance : - Surconsommation de carburant anormale- Ralenti instable
    surtout a froid- Sifflement anormal a l admission- Fumee noire a l echappement- Odeur de carburant non brule- Plus de
    150 000 km sans verification'
  S3: 'Pour choisir le bon capteur température d''air admission pour votre véhicule : - Marque de votre véhicule- Modele de
    votre véhicule- Annee de votre véhicule- Marques : Bosch, Valeo, Denso (premium), Hella, NGK, Delphi (standard), Ridex,
    Topran (budget)- Budget : 15 à 50 EUR'
  S4_DEPOSE: 1. Débrancher la batterie. 2. Localiser la pièce selon la documentation constructeur. 3. Déconnecter les connecteurs
    électriques et raccords. 4. Dévisser les fixations de la pièce. 5. Déposer la pièce en notant l'orientation et la position
    de montage. 6. Nettoyer le logement et vérifier l'état des pièces adjacentes.
  S5: 'Erreurs fréquentes avec le capteur température d''air admission : - Ne pas vérifier la référence exacte avant commande
    — une pièce de mauvaise référence ne fonctionne pas correctement même si elle se monte physiquement- Oublier de débrancher
    la batterie avant intervention — risque de court- circuit sur les composants électroniques- Ne pas confondre avec la sonde
    de température moteur. Vérifier s''il est intégré au débitmètre avant de commander séparément.- Ne pas respecter le couple
    de serrage constructeur au remontage- Ignorer les symptômes d''usure en espérant que ça passe — une défaillance progressive
    s''aggrave toujours- Ne pas effacer les codes défaut après remplacement — le calculateur peut rester en mode dégradé'
  S6: 'Après le remplacement du capteur température d''air admission : - Controle de la tension et du courant avec un multimetre-
    Verifier les connexions electriques (oxydation, jeu)- Remplacement preventif si signes de faiblesse avant l hiver- Ne
    pas laisser le vehicule immobilise longtemps sans protection- Effacer les codes défaut éventuels avec l''outil OBD- Effectuer
    un essai route pour confirmer la disparition des symptômes'
---

# Capteur température d'air admission - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la temperature de l'air entrant dans le moteur pour optimiser le melange air-carburant

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- surconsommation de carburant anormale
- ralenti instable surtout a froid
- sifflement anormal a l admission
- fumee noire a l echappement
- odeur de carburant non brule
- plus de 150 000 km sans verification

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur température d'air admission:

1. **Inspection visuelle** - Examiner l'état du capteur température d'air admission
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- catalyseur
- corps-papillon
- debitmetre-d-air
- fap
- filtre-a-air

## Critères de Compatibilité

Pour commander le bon capteur température d'air admission, vous devez connaître:

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

**Capteur IAT OE ou adaptable ?**
Les adaptables (Febi, FAE, NTK) fonctionnent bien pour cette pièce simple. Vérifiez le type de connecteur et la plage de mesure.

**Comment savoir si mon capteur IAT est HS ?**
Surconsommation, ralenti instable à froid, voyant moteur avec codes P0110 à P0114, démarrage difficile par temps froid.

**Tous les combien changer le capteur IAT ?**
Pas de périodicité. Pièce simple qui dure généralement toute la vie du véhicule. À remplacer uniquement si défaillant.

**Peut-on changer le capteur IAT soi-même ?**
Oui, très facile si séparé. Sur le conduit d'admission, un connecteur, parfois une vis. 10 minutes maximum.

**Quelle erreur éviter avec le capteur IAT ?**
Ne pas confondre avec la sonde de température moteur. Vérifier s'il est intégré au débitmètre avant de commander séparément.
