---
category: capteurs
slug: capteur-pression-du-tuyau-d-admission
title: Capteur pression du tuyau d'admission
pg_id: 3947
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
  role: Mesurer la pression dans le collecteur d'admission
  must_be_true:
  - mesurer
  - detecter
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
    min: 15
    max: 200
    currency: EUR
    unit: l'unite
    source: estimation categorie
  quality_tiers:
  - tier: Constructeur (OE)
    description: Capteur calibré pour les plages de mesure (kPa/bar) du calculateur d'origine. Référence de compatibilité
      absolue.
  - tier: Équivalent OE (OES)
    description: 'Équipementiers reconnus dans ce segment : Bosch, Hella, NTK, Pierburg. Capteurs avec plages de mesure conformes
      à l''OE et résistance aux vapeurs d''huile.'
  - tier: Adaptable
    description: Capteurs génériques dont la plage de mesure peut différer légèrement. Peut provoquer un mélange riche ou
      pauvre persistent.
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
    label: Perte de puissance a l acceleration
    severity: confort
  - id: S3
    label: Sifflement au niveau du collecteur d admission
    severity: confort
  - id: S4
    label: Voyant moteur avec codes p0105-p0109
    severity: confort
  - id: S5
    label: Odeur de carburant melange mal dose
    severity: confort
  - id: S6
    label: Plus de 150 000 km sans nettoyage
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : ralenti instable ou irregulier ?'
  - 'Observer : perte de puissance a l acceleration ?'
  - 'Observer : sifflement au niveau du collecteur d admission ?'
  - Voyant moteur avec codes p0105-p0109 ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Ralenti instable ou irregulier
  - Perte de puissance a l acceleration
  - Sifflement au niveau du collecteur d admission
  - Voyant moteur avec codes p0105-p0109
  - Odeur de carburant melange mal dose
  - Plus de 150 000 km sans nettoyage
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '3947'
  intro_title: A quoi sert Capteur pression du tuyau d'admission ?
  risk_title: Pourquoi remplacer Capteur pression du tuyau d'admission a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Capteur MAP OE ou adaptable ?
    answer: Les adaptables de qualité (Bosch, Hella, NTK) fonctionnent bien. Vérifiez que la plage de mesure correspond à
      votre moteur (atmosphérique ou turbo).
  - question: Comment savoir si mon capteur MAP est HS ?
    answer: Ralenti instable, perte de puissance, surconsommation, voyant moteur avec codes P0105 à P0109, fumée noire.
  - question: Tous les combien changer le capteur MAP ?
    answer: 'Pas de périodicité fixe. Durée de vie 150 000+ km. Peut s''encrasser : un nettoyage suffit parfois.'
  - question: Peut-on changer le capteur MAP soi-même ?
    answer: Oui, très accessible. Généralement sur le collecteur d'admission, une ou deux vis, un connecteur. 15 minutes maximum.
  - question: Quelle erreur éviter avec le capteur MAP ?
    answer: Vérifier l'étanchéité du tuyau de dépression si présent. Ne pas confondre avec le débitmètre. Nettoyer avant de
      remplacer.
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
doc_id: 769bdc9b-9ddb-5f28-b62c-caf42f320f55
content_hash: sha256:bbecb6e6ac6a7326
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
  S1: 'Mesurer la pression dans le collecteur d''admission. Pièces liées : vérifier les composants adjacents lors du remplacement.'
  S2: 'Intervalle : selon constructeur. Symptômes de défaillance : - Ralenti instable ou irregulier- Perte de puissance a
    l acceleration- Sifflement au niveau du collecteur d admission- Voyant moteur avec codes p0105-p0109- Odeur de carburant
    melange mal dose- Plus de 150 000 km sans nettoyage'
  S3: 'Pour choisir le bon capteur pression du tuyau d''admission pour votre véhicule : - Marque de votre véhicule- Modele
    de votre véhicule- Annee de votre véhicule- Marques : Bosch, Valeo, Denso (premium), Hella, NGK, Delphi (standard), Ridex,
    Topran (budget)- Budget : 15 à 200 EUR'
  S4_DEPOSE: 1. Débrancher la batterie. 2. Localiser la pièce selon la documentation constructeur. 3. Déconnecter les connecteurs
    électriques et raccords. 4. Dévisser les fixations de la pièce. 5. Déposer la pièce en notant l'orientation et la position
    de montage. 6. Nettoyer le logement et vérifier l'état des pièces adjacentes.
  S5: 'Erreurs fréquentes avec le capteur pression du tuyau d''admission : - Ne pas vérifier la référence exacte avant commande
    — une pièce de mauvaise référence ne fonctionne pas correctement même si elle se monte physiquement- Oublier de débrancher
    la batterie avant intervention — risque de court- circuit sur les composants électroniques- Vérifier l''étanchéité du
    tuyau de dépression si présent. Ne pas confondre avec le débitmètre. Nettoyer avant de remplacer.- Ne pas respecter le
    couple de serrage constructeur au remontage- Ignorer les symptômes d''usure en espérant que ça passe — une défaillance
    progressive s''aggrave toujours- Ne pas effacer les codes défaut après remplacement — le calculateur peut rester en mode
    dégradé'
  S6: 'Après le remplacement du capteur pression du tuyau d''admission : - Controle de la tension et du courant avec un multimetre-
    Verifier les connexions electriques (oxydation, jeu)- Remplacement preventif si signes de faiblesse avant l hiver- Ne
    pas laisser le vehicule immobilise longtemps sans protection- Effacer les codes défaut éventuels avec l''outil OBD- Effectuer
    un essai route pour confirmer la disparition des symptômes'
---

# Capteur pression du tuyau d'admission - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la pression dans le collecteur d'admission

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- ralenti instable ou irregulier
- perte de puissance a l acceleration
- sifflement au niveau du collecteur d admission
- voyant moteur avec codes p0105-p0109
- odeur de carburant melange mal dose
- plus de 150 000 km sans nettoyage

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur pression du tuyau d'admission:

1. **Inspection visuelle** - Examiner l'état du capteur pression du tuyau d'admission
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-temperature-d-air-admission
- corps-papillon
- debitmetre-d-air
- filtre-a-air

## Critères de Compatibilité

Pour commander le bon capteur pression du tuyau d'admission, vous devez connaître:

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

**Capteur MAP OE ou adaptable ?**
Les adaptables de qualité (Bosch, Hella, NTK) fonctionnent bien. Vérifiez que la plage de mesure correspond à votre moteur (atmosphérique ou turbo).

**Comment savoir si mon capteur MAP est HS ?**
Ralenti instable, perte de puissance, surconsommation, voyant moteur avec codes P0105 à P0109, fumée noire.

**Tous les combien changer le capteur MAP ?**
Pas de périodicité fixe. Durée de vie 150 000+ km. Peut s'encrasser : un nettoyage suffit parfois.

**Peut-on changer le capteur MAP soi-même ?**
Oui, très accessible. Généralement sur le collecteur d'admission, une ou deux vis, un connecteur. 15 minutes maximum.

**Quelle erreur éviter avec le capteur MAP ?**
Vérifier l'étanchéité du tuyau de dépression si présent. Ne pas confondre avec le débitmètre. Nettoyer avant de remplacer.
