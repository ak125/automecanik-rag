---
category: capteurs
slug: capteur-impulsion
title: Capteur impulsion
pg_id: 4813
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
  role: Detecter les impulsions du vilebrequin ou de l'arbre a cames
  must_be_true:
  - detecter
  - compter
  - transmettre
  must_not_contain:
  - reparation
  - regeneration
  - nettoyage
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
  - ❌ "mesure parfaite"
  cost_range:
    min: 25
    max: 80
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
    label: Moteur qui ne demarre pas du tout
    severity: immobilisation
  - id: S2
    label: Calages repetes au ralenti ou en roulant
    severity: immobilisation
  - id: S3
    label: Claquement ou rate d allumage
    severity: confort
  - id: S4
    label: Voyant moteur avec codes p0335 p0336
    severity: confort
  - id: S5
    label: Odeur d essence injection non synchronisee
    severity: confort
  - id: S6
    label: Plus demarrages difficiles recurrents
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  quick_checks:
  - 'Observer : moteur qui ne demarre pas du tout ?'
  - 'Observer : calages repetes au ralenti ou en roulant ?'
  - 'Observer : claquement ou rate d allumage ?'
  - Voyant moteur avec codes p0335 p0336 ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Moteur qui ne demarre pas du tout
  - Calages repetes au ralenti ou en roulant
  - Claquement ou rate d allumage
  - Voyant moteur avec codes p0335 p0336
  - Odeur d essence injection non synchronisee
  - Plus demarrages difficiles recurrents
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '4813'
  intro_title: A quoi sert Capteur impulsion ?
  risk_title: Pourquoi remplacer Capteur impulsion a temps ?
  risk_explanation: '**Pièce HS** - Le capteur impulsion peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le capteur impulsion peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
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
  - question: Capteur PMH OE ou adaptable ?
    answer: Les capteurs OES (Bosch, Hella, Valeo) sont recommandés. Le signal doit être précis pour la synchronisation injection/allumage.
      Adaptables possibles si marque reconnue.
  - question: Comment savoir si mon capteur PMH est HS ?
    answer: Moteur qui ne démarre pas ou cale au ralenti, à-coups à l'accélération, voyant moteur avec codes P0335/P0336,
      démarrage difficile à chaud.
  - question: Tous les combien changer le capteur PMH ?
    answer: Pas de périodicité. Durée de vie 150 000+ km en général. À remplacer uniquement en cas de défaillance avérée.
  - question: Peut-on changer le capteur PMH soi-même ?
    answer: Oui, généralement accessible. Une vis de fixation, un connecteur. Attention à l'entrefer sur certains modèles
      (cale d'épaisseur).
  - question: Quelle erreur éviter avec le capteur PMH ?
    answer: Ne pas forcer le connecteur. Vérifier l'état de la cible (dents du volant moteur). Ne pas utiliser de capteur
      incompatible (inductif vs effet Hall).
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
doc_id: f8bccdfe-1503-5a26-b082-dd7932e45988
content_hash: sha256:505736dd17bd1754
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
  S1: 'Detecter les impulsions du vilebrequin ou de l''arbre a cames. Pièces liées : vérifier les composants adjacents lors
    du remplacement.'
  S2: 'Intervalle : selon constructeur. Symptômes de défaillance : - Moteur qui ne demarre pas du tout- Calages repetes au
    ralenti ou en roulant- Claquement ou rate d allumage- Voyant moteur avec codes p0335 p0336- Odeur d essence injection
    non synchronisee- Plus demarrages difficiles recurrents'
  S3: 'Pour choisir le bon capteur impulsion pour votre véhicule : - Marque de votre véhicule- Modele de votre véhicule- Annee
    de votre véhicule- Marques : Bosch, Valeo, Denso (premium), Hella, NGK, Delphi (standard), Ridex, Topran (budget)- Budget
    : 25 à 80 EUR'
  S4_DEPOSE: 1. Débrancher la batterie. 2. Localiser la pièce selon la documentation constructeur. 3. Déconnecter les connecteurs
    électriques et raccords. 4. Dévisser les fixations de la pièce. 5. Déposer la pièce en notant l'orientation et la position
    de montage. 6. Nettoyer le logement et vérifier l'état des pièces adjacentes.
  S5: 'Erreurs fréquentes avec le capteur impulsion : - Ne pas vérifier la référence exacte avant commande — une pièce de
    mauvaise référence ne fonctionne pas correctement même si elle se monte physiquement- Oublier de débrancher la batterie
    avant intervention — risque de court-circuit sur les composants électroniques- Ne pas forcer le connecteur. Vérifier l''état
    de la cible (dents du volant moteur). Ne pas utiliser de capteur incompatible (inductif vs effet Hall).- Ne pas respecter
    le couple de serrage constructeur au remontage- Ignorer les symptômes d''usure en espérant que ça passe — une défaillance
    progressive s''aggrave toujours- Ne pas effacer les codes défaut après remplacement — le calculateur peut rester en mode
    dégradé'
  S6: 'Après le remplacement du capteur impulsion : - Controle de la tension et du courant avec un multimetre- Verifier les
    connexions electriques (oxydation, jeu)- Remplacement preventif si signes de faiblesse avant l hiver- Ne pas laisser le
    vehicule immobilise longtemps sans protection- Effacer les codes défaut éventuels avec l''outil OBD- Effectuer un essai
    route pour confirmer la disparition des symptômes'
---

# Capteur impulsion - Guide Diagnostic Complet

## Fonction et Rôle

Detecter les impulsions du vilebrequin ou de l'arbre a cames

**Actions principales:** detecter, compter, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui ne demarre pas du tout**
  moteur qui ne demarre pas du tout
- **Calages repetes au ralenti ou en roulant**
  calages repetes au ralenti ou en roulant

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement ou rate d allumage**
  claquement ou rate d allumage

### 🟢 Autres Symptômes

- voyant moteur avec codes p0335 p0336
- odeur d essence injection non synchronisee
- plus demarrages difficiles recurrents

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur impulsion:

1. **Inspection visuelle** - Examiner l'état du capteur impulsion
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le capteur impulsion peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-de-cognement
- capteur-impulsion
- poulie-d-arbre-a-came
- poulie-vilebrequin
- volant-moteur

## Critères de Compatibilité

Pour commander le bon capteur impulsion, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "mesure parfaite"

## FAQ

**Capteur PMH OE ou adaptable ?**
Les capteurs OES (Bosch, Hella, Valeo) sont recommandés. Le signal doit être précis pour la synchronisation injection/allumage. Adaptables possibles si marque reconnue.

**Comment savoir si mon capteur PMH est HS ?**
Moteur qui ne démarre pas ou cale au ralenti, à-coups à l'accélération, voyant moteur avec codes P0335/P0336, démarrage difficile à chaud.

**Tous les combien changer le capteur PMH ?**
Pas de périodicité. Durée de vie 150 000+ km en général. À remplacer uniquement en cas de défaillance avérée.

**Peut-on changer le capteur PMH soi-même ?**
Oui, généralement accessible. Une vis de fixation, un connecteur. Attention à l'entrefer sur certains modèles (cale d'épaisseur).

**Quelle erreur éviter avec le capteur PMH ?**
Ne pas forcer le connecteur. Vérifier l'état de la cible (dents du volant moteur). Ne pas utiliser de capteur incompatible (inductif vs effet Hall).
