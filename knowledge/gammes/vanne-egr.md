---
category: alimentation
slug: vanne-egr
title: Vanne EGR
pg_id: 1145
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
  role: Recycler une partie des gaz d'echappement vers l'admission pour reduire les emissions de NOx
  must_be_true:
  - recycler
  - ouvrir
  - fermer
  must_not_contain:
  - carburant
  - injection
  - injecteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - catalyseur
  - fap
  - silencieux
  - sonde-lambda
  - tube-d-echappement
  - collecteur-d-echappement
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
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
  - ❌ "nettoie le moteur"
  cost_range:
    min: 63
    max: 469
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Vanne identique au premier montage constructeur. Débit, course du clapet et connectique conformes aux paramètres
      du calculateur moteur.
  - tier: Équivalent OE (OES)
    description: Fabricants comme Valeo, Pierburg ou Delphi fournissent les vannes EGR aux constructeurs en première monte.
      Même qualité, même débit, même connectique.
  - tier: Adaptable (aftermarket)
    description: Vannes aftermarket compatibles. Vérifier le type (pneumatique ou électrique), le connecteur et le nombre
      de broches avant commande.
  brands:
    premium:
    - Walker
    - Bosal
    standard:
    - Valeo
    - Febi
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Perte de puissance a bas et moyen regime
    severity: confort
  - id: S2
    label: Fumee noire a l acceleration
    severity: confort
  - id: S3
    label: Ralenti irregulier ou moteur qui broute
    severity: confort
  - id: S4
    label: Voyant moteur allume codes p0400-p0409
    severity: confort
  - id: S5
    label: A-coups a bas regime
    severity: confort
  - id: S6
    label: Plus de 80 000 km sans nettoyage diesel
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - 'Observer : perte de puissance a bas et moyen regime ?'
  - 'Observer : fumee noire a l acceleration ?'
  - 'Observer : ralenti irregulier ou moteur qui broute ?'
  - Voyant moteur allume codes p0400-p0409 ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Perte de puissance a bas et moyen regime
  - Fumee noire a l acceleration
  - Ralenti irregulier ou moteur qui broute
  - Voyant moteur allume codes p0400-p0409
  - A-coups a bas regime
  - Plus de 80 000 km sans nettoyage diesel
  good_practices:
  - Controle visuel sous le vehicule a chaque revision
  - Verifier les fixations et silent-blocs de suspension d echappement
  - Remplacement si perforation, rouille traversante ou bruit anormal
  - Ne pas conduire avec un echappement defectueux (gaz toxiques)
rendering:
  pgId: '1145'
  intro_title: A quoi sert Vanne EGR ?
  risk_title: Pourquoi remplacer Vanne EGR a temps ?
  risk_explanation: '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  risk_consequences:
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
  - question: Vanne EGR OE ou adaptable ?
    answer: Les vannes OES (Valeo, Pierburg, Delphi) sont recommandées. Une vanne de qualité inférieure s'encrassera plus
      vite et pourra avoir un débit incorrect.
  - question: Comment savoir si ma vanne EGR est HS ?
    answer: Perte de puissance, fumée noire, voyant moteur allumé, ralenti irrégulier, à-coups à bas régime, mode dégradé
      possible.
  - question: Tous les combien nettoyer la vanne EGR ?
    answer: 'Nettoyage recommandé tous les 60 000 km sur diesel. Plus souvent si petits trajets urbains. Essence : moins critique.'
  - question: Peut-on nettoyer la vanne EGR soi-même ?
    answer: Oui, avec un nettoyant spécifique EGR. Démonter la vanne, tremper ou pulvériser, nettoyer les conduits. Compter
      1 à 2 heures.
  - question: Quelle erreur éviter avec la vanne EGR ?
    answer: Ne pas supprimer l'EGR (illégal et risque de surconsommation). Ne pas oublier de nettoyer aussi le collecteur
      d'admission encrassé.
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
doc_id: b44d8e1b-e7b2-5300-94af-6058ba627a6e
content_hash: sha256:5c21b0da84984d7d
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
  area: Sous le vehicule, du collecteur moteur au silencieux arriere
  access: Par le dessous (pont elevateur)
  adjacent_parts:
  - collecteur
  - catalyseur
  - tubes
  - silencieux
installation:
  difficulty: moyen
  time: 1h a 2h
  tools:
  - cle a douille
  - degripant
  - chandelles
  prerequisite: Pont elevateur, fixations souvent grippees par la rouille
phase5_enrichment:
  _source: ate-freinage.fr + denso-am.eu + ferodo.com + hella.com + mann-filter.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 16
  _has_tech_data: true
  types_variants:
  - type: 'Hall'
    source_ref: corpus RAG web OEM
  - type: 'Pneumatique'
    source_ref: corpus RAG web OEM
  - type: 'hall'
    source_ref: corpus RAG web OEM
  - type: 'inductif'
    source_ref: corpus RAG web OEM
  - type: 'pneumatique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_0_ohm: '0 ohm'
    val_0_035_mm: '0,035 mm'
    val_0_05_mm: '0,05 mm'
    val_0_1_km: '0,1 km'
    val_0_1_mm: '0,1 mm'
    val_0_15_v: '0,15 V'
    val_0_23_v: '0,23 V'
    val_1_1_bar: '1,1 bar'
    val_12_v: '12 V'
    val_14_v: '14 V'
    val_15_ohms: '15 ohms'
    val_16_v: '16 V'
    val_2_3_v: '2,3 V'
    val_20__: '20 %'
    val_3_bars: '3 bars'
  materials:
  - materiau: 'fonte grise'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Lavanne EGR est située entre le collecteur d''admission et le collecteurd''échappement, son rôle est de réduire les
    émissions de gaz polluantes Nox (Oxyde d''azote)des moteurs. La vanne EGR est constituée d''un clapet et d''un diaphragmefaisant
    recirculer les gaz d''échappement entrant dans le circuit d''admission.Le principe est de diminuer la proportion d''oxygène
    afin de ralentir la vitessede combustion, et donc l''émission d''oxyde d''azote responsable de la pollutionatmosphérique
    de l''ozone. La nouvelle génération de vanne EGR est utilisée surles nouveaux moteurs diesel dans le but de refroidir
    les gaz d''échappement enles brûlant une seconde fois dans le circuit d''admission. L''objectif est dediminuer les émissions
    NOx, dangereuse pour la santé. De par son principe derecirculation des gaz, la vanne EGR engendre des dépôts de particulesdans
    l''admission. Ces dépôts accumulés se transforment en une couche noire quipeut entraîner différentes pannes et problèmes
    de moteur. La quantité de gaz réinjecté varie de 5 à 35 %suivant le type de moteur. En savoir plus : vanne egr — définition
    et rôle mécanique 🚨 Bruit Vanne EGR : causes et diagnostic'
  S2: 'Ne pas attendre la panne complete pour intervenir. Symptômes d''usure : - Perte de puissance a bas et moyen regime
    - Fumee noire a l acceleration - Ralenti irregulier ou moteur qui broute - Voyant moteur allume codes p0400-p0409 - A-coups
    a bas regime - Plus de 80 000 km sans nettoyage diesel'
  S3: 'Pour choisir les bons vanne egr pour votre véhicule : - Marque de votre véhicule - Modele de votre véhicule - Annee
    de votre véhicule - Vérifier : perte de puissance a bas et moyen regime - Vérifier : fumee noire a l acceleration - Vérifier
    : ralenti irregulier ou moteur qui broute - Vérifier : voyant moteur allume codes p0400-p0409 - Vérifier : a-coups a bas
    regime - Vérifier : plus de 80 000 km sans nettoyage dieselPour aller plus loin : consultez notre guide d''achat vanne
    egr — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 1. Debrancher la batterie (intervention sur circuit electrique et electronique du moteur). 2. Localiser la vanne
    EGR entre le collecteur d'admission et le collecteur d'echappement — l'emplacement varie selon le vehicule. 3. Debrancher
    le connecteur electrique de la vanne EGR (clip ou vis). 4. Deconnecter les durites de depression ou le tuyau de recirculation
    des gaz selon le type de vanne (pneumatique ou electrique). 5. Devisser les vis de fixation de la vanne sur le collecteur
    (2 a 4 vis selon vehicule, souvent grippees par la calamine — utiliser du debloquant). 6. Deposer la vanne EGR delicatement
    sans forcer sur les collecteurs. 7. Nettoyer les plans de joint sur le collecteur d'admission et le collecteur d'echappement
    — retirer toute trace de calamine et d'ancien joint.
  S4_REPOSE: '- Vérifiez que la vanne EGRneuf soit identique à celle démonté. - Remontez la nouvelle vanneEGR. - Serrez les
    vis de fixationde la vanne EGR. - Rebranchez le connecteur dela vanne EGR. - Remontez la gaine du turbo. - Rebranchez
    la batterie. - A l''aide de l''outildiagnostic éteindre les témoins allumés sur le tableau de bord en effaçant lesdéfauts
    dans le calculateur moteur. - Effectuez une remise à zérodes adaptafis de fonctionnement de la vanne EGR à l''aide de
    l''outil diagnostic. ✅ Après remontage, vérifiez les spécifications dans la fiche technique Vanne EGR.'
  S5: 'Erreurs frequentes avec la vanne EGR : - Supprimer ou obturer la vanne EGR pour "gagner en puissance" — c''est illegal
    (non-conformite au controle technique) et provoque une augmentation des emissions de NOx- Ne pas nettoyer le conduit de
    recirculation lors du remplacement — la calamine accumulee colmate la vanne neuve en quelques milliers de km- Ignorer
    un voyant moteur allume avec perte de puissance — signe classique de vanne EGR bloquee ouverte ou fermee- Confondre vanne
    EGR pneumatique et electrique lors de l''achat — elles ne sont pas interchangeables et les references different- Ne pas
    verifier l''etat du refroidisseur EGR sur les vehicules qui en sont equipes — un refroidisseur percé fait entrer du liquide
    de refroidissement dans l''admission- Oublier de faire un reset des codes defaut apres remplacement — le calculateur moteur
    peut rester en mode degrade'
  S6: 'Après le remplacement d''une vanne EGR, les vérifications combinent un contrôle électronique via OBD et une validation
    du comportement moteur sur route. Sur moteur diesel, le premier cycle de conduite est déterminant pour confirmer la disparition
    des codes défaut et le retour aux performances nominales. - Effacement des codes défaut OBD : avant le premier démarrage
    après remplacement, effacer impérativement les codes mémorisés P0400 à P0409 avec un outil de diagnostic. Ces codes, liés
    à l''ancienne vanne défectueuse, ne doivent pas réapparaître après 1 à 2 cycles de conduite complets. Une réapparition
    immédiate signale un problème de câblage ou de compatibilité de la pièce. - Contrôle du ralenti au premier démarrage :
    moteur à température normale, le ralenti doit être stable entre 750 et 850 tr/min sur diesel sans à-coups ni bruit de
    broutement. Un ralenti irrégulier persistant peut indiquer que la vanne EGR neuve est déjà partiellement encrassée par
    des résidus présents dans le collecteur d''admission. - Test à bas régime sous charge : circuler en ville à allure modérée
    (2ème et 3ème rapport, 1 500 à 2 000 tr/min) — les à-coups caractéristiques et la perte de puissance à bas régime qui
    signalaient la vanne défectueuse doivent avoir disparu. - Inspection visuelle de l''étanchéité : moteur chaud, vérifier
    visuellement que le joint de montage entre la vanne EGR et le collecteur d''admission ne présente pas de fuite de gaz
    (trace noire carbonée ou sifflement). Un joint mal posé génère des faux airs qui perturbent la régulation et font réapparaître
    les codes P040x. - Vérification de l''absence de fumées noires : lors d''une accélération depuis 1 500 tr/min en 2ème
    rapport, observer l''échappement — l''absence de fumée noire dense confirme que le recyclage des gaz est opérationnel
    et que la combustion est correcte. - Test avec le circuit de refroidissement EGR (si applicable) : sur les vannes EGR
    à refroidissement eau, vérifier l''absence de fuite sur les raccords hydrauliques de la vanne et s''assurer que le niveau
    de liquide de refroidissement n''a pas baissé après le premier trajet chaud. - Conduite de validation après 80 km : effectuer
    un trajet d''au moins 80 km incluant 20 minutes d''autoroute à régime soutenu (2 500-3 000 tr/min) pour régénérer le circuit
    EGR et confirmer l''absence de tout code défaut récurrent.'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (4 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: Quel est le prix d'un vanne egr ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour trouver
    le vanne egr compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment savoir si mon
    vanne egr est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic ci-dessus. En
    cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un vanne egr défaillant ?Cela dépend
    de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section symptômes
    pour évaluer l'urgence du remplacement.- catalyseur - injecteur - turbo
  S8: 'Vanne EGR OE ou adaptable ?Les vannes OES (Valeo, Pierburg, Delphi) sont recommandées. Une vanne de qualité inférieure
    s''encrassera plus vite et pourra avoir un débit incorrect. Comment savoir si ma vanne EGR est HS ?Perte de puissance,
    fumée noire, voyant moteur allumé, ralenti irrégulier, à-coups à bas régime, mode dégradé possible. Tous les combien nettoyer
    la vanne EGR ?Nettoyage recommandé tous les 60 000 km sur diesel. Plus souvent si petits trajets urbains. Essence : moins
    critique. Peut-on nettoyer la vanne EGR soi-même ?Oui, avec un nettoyant spécifique EGR. Démonter la vanne, tremper ou
    pulvériser, nettoyer les conduits. Compter 1 à 2 heures. Quelle erreur éviter avec la vanne EGR ?Ne pas supprimer l''EGR
    (illégal et risque de surconsommation). Ne pas oublier de nettoyer aussi le collecteur d''admission encrassé.'
  META: '- Changer une vanne EGR Renault Scénic 2 1.9 DCI. - Vanne EGR Renault Clio 2 1.5 DCI.'
---

# Vanne EGR - Guide Diagnostic Complet

## Fonction et Rôle

Recycler une partie des gaz d'echappement vers l'admission pour reduire les emissions de NOx

**Actions principales:** recycler, ouvrir, fermer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- perte de puissance a bas et moyen regime
- fumee noire a l acceleration
- ralenti irregulier ou moteur qui broute
- voyant moteur allume codes p0400-p0409
- a-coups a bas regime
- plus de 80 000 km sans nettoyage diesel

## Procédure de Diagnostic

Pour diagnostiquer un problème de vanne egr:

1. **Inspection visuelle** - Examiner l'état du vanne egr
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- catalyseur
- fap
- injecteur
- turbo

## Critères de Compatibilité

Pour commander le bon vanne egr, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "nettoie le moteur"

## FAQ

**Vanne EGR OE ou adaptable ?**
Les vannes OES (Valeo, Pierburg, Delphi) sont recommandées. Une vanne de qualité inférieure s'encrassera plus vite et pourra avoir un débit incorrect.

**Comment savoir si ma vanne EGR est HS ?**
Perte de puissance, fumée noire, voyant moteur allumé, ralenti irrégulier, à-coups à bas régime, mode dégradé possible.

**Tous les combien nettoyer la vanne EGR ?**
Nettoyage recommandé tous les 60 000 km sur diesel. Plus souvent si petits trajets urbains. Essence : moins critique.

**Peut-on nettoyer la vanne EGR soi-même ?**
Oui, avec un nettoyant spécifique EGR. Démonter la vanne, tremper ou pulvériser, nettoyer les conduits. Compter 1 à 2 heures.

**Quelle erreur éviter avec la vanne EGR ?**
Ne pas supprimer l'EGR (illégal et risque de surconsommation). Ne pas oublier de nettoyer aussi le collecteur d'admission encrassé.
## Témoins critiques (ARRÊT IMMÉDIAT)

### Témoin huile moteur (rouge)
- **Signification** : Pression d'huile insuffisante
- **Action** : ARRÊT IMMÉDIAT du véhicule
- **Causes** : Niveau bas, pompe à huile, fuite
- **Risque** : Casse moteur
- **Vérification** : Niveau d'huile à la jauge

### Témoin température moteur (rouge)
- **Signification** : Surchauffe moteur
- **Action** : ARRÊT IMMÉDIAT, laisser refroidir
- **Causes** : Liquide refroidissement, thermostat, ventilateur
- **Risque** : Joint de culasse, casse moteur

### Témoin frein (rouge)
- **Signification** : Niveau liquide frein bas ou frein à main
- **Action** : Vérifier frein à main, puis niveau liquide
- **Causes** : Fuite, usure plaquettes extrême
- **Risque** : Perte de freinage

### Témoin batterie (rouge)
- **Signification** : Charge batterie insuffisante
- **Action** : Rejoindre un garage rapidement
- **Causes** : Alternateur, courroie, batterie HS
- **Risque** : Panne complète

## Témoins importants (attention requise)

### Témoin ABS (orange)
- **Signification** : Système ABS désactivé
- **Action** : Contrôle recommandé
- **Causes** : Capteur ABS, bloc hydraulique
- **Impact** : Freinage normal mais sans assistance ABS
- **Pièces** : Capteur ABS, bloc ABS

### Témoin ESP/ASR (orange)
- **Signification** : Antipatinage/stabilité désactivé
- **Action** : Conduire prudemment
- **Causes** : Capteur, calculateur

### Témoin airbag (orange)
- **Signification** : Système airbag défaillant
- **Action** : Contrôle obligatoire
- **Risque** : Non-déclenchement en cas d'accident
- **Pièces** : Contacteur tournant, capteur airbag

### Témoin moteur (orange - check engine)
- **Signification** : Anomalie gestion moteur
- **Action** : Diagnostic OBD recommandé
- **Causes multiples** : Capteur O2, catalyseur, allumage
- **Impact** : Surconsommation, pollution

### Témoin FAP/DPF (orange - diesel)
- **Signification** : Filtre à particules saturé
- **Action** : Rouler 20min sur autoroute (régénération)
- **Causes** : Trajets courts répétés
- **Pièces** : FAP, nettoyage, additif

## Témoins d'information

### Témoin préchauffage (diesel)
- **Signification** : Préchauffage des bougies en cours
- **Action** : Attendre extinction avant démarrage
- **Normal** : S'éteint après quelques secondes

### Témoin clignotant
- **Signification** : Clignotant actif
- **Anomalie si** : Clignote rapidement = ampoule grillée

### Témoin feux de route
- **Signification** : Pleins phares activés

### Témoin antibrouillard
- **Signification** : Feux de brouillard actifs

## Codes couleur

| Couleur | Signification | Action |
|---------|---------------|--------|
| **Rouge** | Danger immédiat | Arrêt véhicule |
| **Orange** | Attention | Contrôle rapide |
| **Vert/Bleu** | Information | Aucune |
## Bruits d'échappement

### Bruit métallique sous la voiture
- **Catalyseur décollé** : Le substrat céramique interne s'est fragmenté et vibre dans le boîtier. Bruit de ferraille au ralenti.
- **Silencieux percé** : Corrosion ayant percé le pot d'échappement. Bruit de souffle ou grondement.
- **Flexible d'échappement fissuré** : Joint de raccord entre le collecteur et la ligne d'échappement. Bruit de fuite.
- **Collier ou bride desserré** : Claquement rythmique, plus audible au ralenti.

### Sifflement
- **Fuite au collecteur** : Joint de collecteur d'échappement brûlé. Sifflement aigu surtout à froid, qui peut s'atténuer à chaud.
- **Fissure sur le tube** : Soudure fatiguée ou corrosion localisée.

## Fumées anormales

### Fumée blanche épaisse
- **Joint de culasse défaillant** : Liquide de refroidissement entre dans la chambre de combustion. Fumée blanche sucrée, persistante même moteur chaud. Vérifier le niveau de liquide de refroidissement.

### Fumée noire
- **Mélange trop riche** : Injecteurs qui fuient, capteur MAP/MAF défaillant, filtre à air colmaté.
- **Turbo défaillant** : Fuite d'huile dans l'admission via les joints du turbo.

### Fumée bleue
- **Consommation d'huile** : Segments usés, guides de soupapes usés, ou joint de queue de soupape. L'huile brûle dans la chambre de combustion.

## Catalyseur et FAP

- **Catalyseur colmaté** : Perte de puissance, moteur qui étouffe à l'accélération, voyant moteur allumé (codes P0420/P0430).
- **Filtre à particules bouché** : Voyant FAP allumé, régénérations trop fréquentes, perte de puissance. Fréquent sur les trajets courts en ville.
- **Sonde lambda défaillante** : Consommation en hausse, voyant moteur, mélange air/carburant mal régulé.

## Quand consulter un professionnel

- Fumée blanche persistante moteur chaud (risque joint de culasse)
- Voyant moteur + perte de puissance (catalyseur/FAP)
- Odeur d'œuf pourri (catalyseur en surchauffe)
- Bruit d'échappement fort + odeur de gaz dans l'habitacle
## Témoins critiques (ARRÊT IMMÉDIAT)

### Témoin huile moteur (rouge)
- **Signification** : Pression d'huile insuffisante
- **Action** : ARRÊT IMMÉDIAT du véhicule
- **Causes** : Niveau bas, pompe à huile, fuite
- **Risque** : Casse moteur
- **Vérification** : Niveau d'huile à la jauge

### Témoin température moteur (rouge)
- **Signification** : Surchauffe moteur
- **Action** : ARRÊT IMMÉDIAT, laisser refroidir
- **Causes** : Liquide refroidissement, thermostat, ventilateur
- **Risque** : Joint de culasse, casse moteur

### Témoin frein (rouge)
- **Signification** : Niveau liquide frein bas ou frein à main
- **Action** : Vérifier frein à main, puis niveau liquide
- **Causes** : Fuite, usure plaquettes extrême
- **Risque** : Perte de freinage

### Témoin batterie (rouge)
- **Signification** : Charge batterie insuffisante
- **Action** : Rejoindre un garage rapidement
- **Causes** : Alternateur, courroie, batterie HS
- **Risque** : Panne complète

## Témoins importants (attention requise)

### Témoin ABS (orange)
- **Signification** : Système ABS désactivé
- **Action** : Contrôle recommandé
- **Causes** : Capteur ABS, bloc hydraulique
- **Impact** : Freinage normal mais sans assistance ABS
- **Pièces** : Capteur ABS, bloc ABS

### Témoin ESP/ASR (orange)
- **Signification** : Antipatinage/stabilité désactivé
- **Action** : Conduire prudemment
- **Causes** : Capteur, calculateur

### Témoin airbag (orange)
- **Signification** : Système airbag défaillant
- **Action** : Contrôle obligatoire
- **Risque** : Non-déclenchement en cas d'accident
- **Pièces** : Contacteur tournant, capteur airbag

### Témoin moteur (orange - check engine)
- **Signification** : Anomalie gestion moteur
- **Action** : Diagnostic OBD recommandé
- **Causes multiples** : Capteur O2, catalyseur, allumage
- **Impact** : Surconsommation, pollution

### Témoin FAP/DPF (orange - diesel)
- **Signification** : Filtre à particules saturé
- **Action** : Rouler 20min sur autoroute (régénération)
- **Causes** : Trajets courts répétés
- **Pièces** : FAP, nettoyage, additif

## Témoins d'information

### Témoin préchauffage (diesel)
- **Signification** : Préchauffage des bougies en cours
- **Action** : Attendre extinction avant démarrage
- **Normal** : S'éteint après quelques secondes

### Témoin clignotant
- **Signification** : Clignotant actif
- **Anomalie si** : Clignote rapidement = ampoule grillée

### Témoin feux de route
- **Signification** : Pleins phares activés

### Témoin antibrouillard
- **Signification** : Feux de brouillard actifs

## Codes couleur

| Couleur | Signification | Action |
|---------|---------------|--------|
| **Rouge** | Danger immédiat | Arrêt véhicule |
| **Orange** | Attention | Contrôle rapide |
| **Vert/Bleu** | Information | Aucune |
## Bruits d'échappement

### Bruit métallique sous la voiture
- **Catalyseur décollé** : Le substrat céramique interne s'est fragmenté et vibre dans le boîtier. Bruit de ferraille au ralenti.
- **Silencieux percé** : Corrosion ayant percé le pot d'échappement. Bruit de souffle ou grondement.
- **Flexible d'échappement fissuré** : Joint de raccord entre le collecteur et la ligne d'échappement. Bruit de fuite.
- **Collier ou bride desserré** : Claquement rythmique, plus audible au ralenti.

### Sifflement
- **Fuite au collecteur** : Joint de collecteur d'échappement brûlé. Sifflement aigu surtout à froid, qui peut s'atténuer à chaud.
- **Fissure sur le tube** : Soudure fatiguée ou corrosion localisée.

## Fumées anormales

### Fumée blanche épaisse
- **Joint de culasse défaillant** : Liquide de refroidissement entre dans la chambre de combustion. Fumée blanche sucrée, persistante même moteur chaud. Vérifier le niveau de liquide de refroidissement.

### Fumée noire
- **Mélange trop riche** : Injecteurs qui fuient, capteur MAP/MAF défaillant, filtre à air colmaté.
- **Turbo défaillant** : Fuite d'huile dans l'admission via les joints du turbo.

### Fumée bleue
- **Consommation d'huile** : Segments usés, guides de soupapes usés, ou joint de queue de soupape. L'huile brûle dans la chambre de combustion.

## Catalyseur et FAP

- **Catalyseur colmaté** : Perte de puissance, moteur qui étouffe à l'accélération, voyant moteur allumé (codes P0420/P0430).
- **Filtre à particules bouché** : Voyant FAP allumé, régénérations trop fréquentes, perte de puissance. Fréquent sur les trajets courts en ville.
- **Sonde lambda défaillante** : Consommation en hausse, voyant moteur, mélange air/carburant mal régulé.
## Variantes et types
- hall

## Matériaux
- fonte grise

## Valeurs techniques de référence
- 0,035 mm
- 0,05 mm
- 0,1 mm
- 550 °C
- 650 °C
## Témoins critiques (ARRÊT IMMÉDIAT)

### Témoin huile moteur (rouge)
- **Signification** : Pression d'huile insuffisante
- **Action** : ARRÊT IMMÉDIAT du véhicule
- **Causes** : Niveau bas, pompe à huile, fuite
- **Risque** : Casse moteur
- **Vérification** : Niveau d'huile à la jauge

### Témoin température moteur (rouge)
- **Signification** : Surchauffe moteur
- **Action** : ARRÊT IMMÉDIAT, laisser refroidir
- **Causes** : Liquide refroidissement, thermostat, ventilateur
- **Risque** : Joint de culasse, casse moteur

### Témoin frein (rouge)
- **Signification** : Niveau liquide frein bas ou frein à main
- **Action** : Vérifier frein à main, puis niveau liquide
- **Causes** : Fuite, usure plaquettes extrême
- **Risque** : Perte de freinage

### Témoin batterie (rouge)
- **Signification** : Charge batterie insuffisante
- **Action** : Rejoindre un garage rapidement
- **Causes** : Alternateur, courroie, batterie HS
- **Risque** : Panne complète

## Témoins importants (attention requise)

### Témoin ABS (orange)
- **Signification** : Système ABS désactivé
- **Action** : Contrôle recommandé
- **Causes** : Capteur ABS, bloc hydraulique
- **Impact** : Freinage normal mais sans assistance ABS
- **Pièces** : Capteur ABS, bloc ABS

### Témoin ESP/ASR (orange)
- **Signification** : Antipatinage/stabilité désactivé
- **Action** : Conduire prudemment
- **Causes** : Capteur, calculateur

### Témoin airbag (orange)
- **Signification** : Système airbag défaillant
- **Action** : Contrôle obligatoire
- **Risque** : Non-déclenchement en cas d'accident
- **Pièces** : Contacteur tournant, capteur airbag

### Témoin moteur (orange - check engine)
- **Signification** : Anomalie gestion moteur
- **Action** : Diagnostic OBD recommandé
- **Causes multiples** : Capteur O2, catalyseur, allumage
- **Impact** : Surconsommation, pollution

### Témoin FAP/DPF (orange - diesel)
- **Signification** : Filtre à particules saturé
- **Action** : Rouler 20min sur autoroute (régénération)
- **Causes** : Trajets courts répétés
- **Pièces** : FAP, nettoyage, additif

## Témoins d'information

### Témoin préchauffage (diesel)
- **Signification** : Préchauffage des bougies en cours
- **Action** : Attendre extinction avant démarrage
- **Normal** : S'éteint après quelques secondes

### Témoin clignotant
- **Signification** : Clignotant actif
- **Anomalie si** : Clignote rapidement = ampoule grillée

### Témoin feux de route
- **Signification** : Pleins phares activés

### Témoin antibrouillard
- **Signification** : Feux de brouillard actifs

## Codes couleur

| Couleur | Signification | Action |
|---------|---------------|--------|
| **Rouge** | Danger immédiat | Arrêt véhicule |
| **Orange** | Attention | Contrôle rapide |
| **Vert/Bleu** | Information | Aucune |
## Bruits d'échappement

### Bruit métallique sous la voiture
- **Catalyseur décollé** : Le substrat céramique interne s'est fragmenté et vibre dans le boîtier. Bruit de ferraille au ralenti.
- **Silencieux percé** : Corrosion ayant percé le pot d'échappement. Bruit de souffle ou grondement.
- **Flexible d'échappement fissuré** : Joint de raccord entre le collecteur et la ligne d'échappement. Bruit de fuite.
- **Collier ou bride desserré** : Claquement rythmique, plus audible au ralenti.

### Sifflement
- **Fuite au collecteur** : Joint de collecteur d'échappement brûlé. Sifflement aigu surtout à froid, qui peut s'atténuer à chaud.
- **Fissure sur le tube** : Soudure fatiguée ou corrosion localisée.

## Fumées anormales

### Fumée blanche épaisse
- **Joint de culasse défaillant** : Liquide de refroidissement entre dans la chambre de combustion. Fumée blanche sucrée, persistante même moteur chaud. Vérifier le niveau de liquide de refroidissement.

### Fumée noire
- **Mélange trop riche** : Injecteurs qui fuient, capteur MAP/MAF défaillant, filtre à air colmaté.
- **Turbo défaillant** : Fuite d'huile dans l'admission via les joints du turbo.

### Fumée bleue
- **Consommation d'huile** : Segments usés, guides de soupapes usés, ou joint de queue de soupape. L'huile brûle dans la chambre de combustion.

## Catalyseur et FAP

- **Catalyseur colmaté** : Perte de puissance, moteur qui étouffe à l'accélération, voyant moteur allumé (codes P0420/P0430).
- **Filtre à particules bouché** : Voyant FAP allumé, régénérations trop fréquentes, perte de puissance. Fréquent sur les trajets courts en ville.
- **Sonde lambda défaillante** : Consommation en hausse, voyant moteur, mélange air/carburant mal régulé.

## Quand consulter un professionnel

- Fumée blanche persistante moteur chaud (risque joint de culasse)
- Voyant moteur + perte de puissance (catalyseur/FAP)
- Odeur d'œuf pourri (catalyseur en surchauffe)
- Bruit d'échappement fort + odeur de gaz dans l'habitacle


## References supplementaires

<!-- materialized-from-db manual/02f258d16d9c 2026-03-28 -->
### Conduit de recirculation des gaz d'échappement (EGR)

Dépollution
Conduit de recirculation des gaz d'échappement (EGR)

Notre conduit transfère les gaz d'échappement après le turbocompresseur vers l'admission d'air avant le turbocompresseur.

Principaux bénéfices
Résistance chimique et thermique
Mélange de caoutchouc réalisé en interne
Caractéristiques techniques
Description

Assemblage de tuyaux en caoutchouc avec ou sans renforts annulaires, avant et après le refroidisseur EGR.

Informations fonctionnelles
Résistance à 230 °C
Résistance chimique aux gaz d'échappement
Technologies
Technologie enveloppée
Tuyaux ondulés
Bénéfices
Amélioration des performances
Résistance aux fortes pressions
Fiabilité

<!-- materialized-from-db manual/38af23bf7c77 2026-04-03 -->
### Données techniques OEM — Vanne EGR

# Données techniques OEM — Vanne EGR
Source : ate-freinage.fr + denso-am.eu + ferodo.com + hella.com + mann-filter.com (16 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- Hall
- Pneumatique
- hall
- inductif
- pneumatique

## Matériaux
- fonte grise

## Valeurs techniques de référence
- 0,035 mm
- 0,05 mm
- 0,1 mm
- 1,1 bar
- 20 %
- 3 bars

<!-- materialized-from-db manual/96043d143a3b 2026-04-02 -->
### Données techniques OEM — Vanne EGR

# Données techniques OEM — Montage maitrise
Source : ate-freinage.fr + denso-am.eu + ferodo.com (3 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- hall

## Matériaux
- fonte grise

## Valeurs techniques de référence
- 0,035 mm
- 0,05 mm
- 0,1 mm
- 550 °C
- 650 °C

## Symptomes supplementaires

<!-- materialized-from-db diagnostic/temoins-tableau-bord.md 2026-01-01 -->
### Diagnostic - Témoins tableau de bord

# Témoins tableau de bord - Guide complet

## Témoins critiques (ARRÊT IMMÉDIAT)

### Témoin huile moteur (rouge)
- **Signification** : Pression d'huile insuffisante
- **Action** : ARRÊT IMMÉDIAT du véhicule
- **Causes** : Niveau bas, pompe à huile, fuite
- **Risque** : Casse moteur
- **Vérification** : Niveau d'huile à la jauge

### Témoin température moteur (rouge)
- **Signification** : Surchauffe moteur
- **Action** : ARRÊT IMMÉDIAT, laisser refroidir
- **Causes** : Liquide refroidissement, thermostat, ventilateur
- **Risque** : Joint de culasse, casse moteur

### Témoin frein (rouge)
- **Signification** : Niveau liquide frein bas ou frein à main
- **Action** : Vérifier frein à main, puis niveau liquide
- **Causes** : Fuite, usure plaquettes extrême
- **Risque** : Perte de freinage

### Témoin batterie (rouge)
- **Signification** : Charge batterie insuffisante
- **Action** : Rejoindre un garage rapidement
- **Causes** : Alternateur, courroie, batterie HS
- **Risque** : Panne complète

## Témoins importants (attention requise)

### Témoin ABS (orange)
- **Signification** : Système ABS désactivé
- **Action** : Contrôle recommandé
- **Causes** : Capteur ABS, bloc hydraulique
- **Impact** : Freinage normal mais sans assistance ABS
- **Pièces** : Capteur ABS, bloc ABS

### Témoin ESP/ASR (orange)
- **Signification** : Antipatinage/stabilité désactivé
- **Action** : Conduire prudemment
- **Causes** : Capteur, calculateur

### Témoin airbag (orange)
- **Signification** : Système airbag défaillant
- **Action** : Contrôle obligatoire
- **Risque** : Non-déclenchement en cas d'accident
- **Pièces** : Contacteur tournant, capteur airbag

### Témoin moteur (orange - check engine)
- **Signification** : Anomalie gestion moteur
- **Action** : Diagnostic OBD recommandé
- **Causes multiples** : Capteur O2, catalyseur, allumage
- **Impact** : Surconsommation, pollution

### Témoin FAP/DPF (orange - diesel)
- **Signification** : Filtre à particules saturé
- **Action** : Rouler 20min sur autoroute (régénération)
- **Causes** : Trajets courts répétés
- **Pièces** : FAP, nettoyage, additif

## Témoins d'information

### Témoin préchauffage (diesel)
- **Signification** : Préchauffage des bougies en cours
- **Action** : Attendre extinction avant démarrage
- **Normal** : S'éteint après quelques secondes

### Témoin clignotant
- **Signification** : Clignotant actif
- **Anomalie si** : Clignote rapidement = ampoule grillée

### Témoin feux de route
- **Signification** : Pleins phares activés

### Témoin antibrouillard
- **Signification** : Feux de brouillard actifs

## Codes couleur

| Couleur | Signification | Action |
|---------|---------------|--------|
| **Rouge** | Danger immédiat | Arrêt véhicule |
| **Orange** | Attention | Contrôle rapide |
| **Vert/Bleu** | Information | Aucune |

## Diagnostic OBD-II

Pour les témoins moteur, un diagnostic OBD permet de lire les codes défaut :
- **P0xxx** : Groupe motopropulseur
- **B0xxx** : Carrosserie
- **C0xxx** : Châssis
- **U0xxx** : Réseau/Communication

<!-- materialized-from-db diagnostic/echappement-catalyseur.md 2026-02-15 -->
### Diagnostic - Échappement et catalyseur

# Échappement et catalyseur - Diagnostic complet

## Bruits d'échappement

### Bruit métallique sous la voiture
- **Catalyseur décollé** : Le substrat céramique interne s'est fragmenté et vibre dans le boîtier. Bruit de ferraille au ralenti.
- **Silencieux percé** : Corrosion ayant percé le pot d'échappement. Bruit de souffle ou grondement.
- **Flexible d'échappement fissuré** : Joint de raccord entre le collecteur et la ligne d'échappement. Bruit de fuite.
- **Collier ou bride desserré** : Claquement rythmique, plus audible au ralenti.

### Sifflement
- **Fuite au collecteur** : Joint de collecteur d'échappement brûlé. Sifflement aigu surtout à froid, qui peut s'atténuer à chaud.
- **Fissure sur le tube** : Soudure fatiguée ou corrosion localisée.

## Fumées anormales

### Fumée blanche épaisse
- **Joint de culasse défaillant** : Liquide de refroidissement entre dans la chambre de combustion. Fumée blanche sucrée, persistante même moteur chaud. Vérifier le niveau de liquide de refroidissement.

### Fumée noire
- **Mélange trop riche** : Injecteurs qui fuient, capteur MAP/MAF défaillant, filtre à air colmaté.
- **Turbo défaillant** : Fuite d'huile dans l'admission via les joints du turbo.

### Fumée bleue
- **Consommation d'huile** : Segments usés, guides de soupapes usés, ou joint de queue de soupape. L'huile brûle dans la chambre de combustion.

## Catalyseur et FAP

- **Catalyseur colmaté** : Perte de puissance, moteur qui étouffe à l'accélération, voyant moteur allumé (codes P0420/P0430).
- **Filtre à particules bouché** : Voyant FAP allumé, régénérations trop fréquentes, perte de puissance. Fréquent sur les trajets courts en ville.
- **Sonde lambda défaillante** : Consommation en hausse, voyant moteur, mélange air/carburant mal régulé.

## Quand consulter un professionnel

- Fumée blanche persistante moteur chaud (risque joint de culasse)
- Voyant moteur + perte de puissance (catalyseur/FAP)
- Odeur d'œuf pourri (catalyseur en surchauffe)
- Bruit d'échappement fort + odeur de gaz dans l'habitacle
