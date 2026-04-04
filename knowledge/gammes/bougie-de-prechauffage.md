---
category: allumage
slug: bougie-de-prechauffage
title: Bougie de préchauffage
pg_id: 243
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
  role: Chauffer la chambre de combustion a froid pour faciliter le demarrage diesel - N'agit qu'au demarrage
  must_be_true:
  - chauffer
  - prechauffer
  - rechauffer
  must_not_contain:
  - essence
  - etincelle
  - allumage
  - haute tension
  - bobine
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
  - ❌ "plus de puissance"
  cost_range:
    min: 15
    max: 23
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Bougie d'origine (OE)
    description: Reference constructeur, adaptee aux parametres du boitier de prechauffage du vehicule. Recommandee sur vehicules
      recents ou si le moteur a ete sensible aux pannes de demarrage.
  - tier: Equipementier specialise prechauffage diesel
    description: Fabricants specialises en systemes de prechauffage, proposant des equivalences documentees par motorisation
      diesel. Verifier la tension nominale (11V, 4.4V selon les technologies) et la longueur de ti
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
    label: Demarrage long ou difficile par temps froid
    severity: confort
  - id: S2
    label: Voyant prechauffage allume plus reste
    severity: confort
  - id: S3
    label: Fumee blanche au demarrage qui persiste
    severity: confort
  - id: S4
    label: Rates moteur a froid les premieres secondes
    severity: confort
  - id: S5
    label: Odeur de gazole non brule au demarrage
    severity: confort
  - id: S6
    label: Plus de 100 000 km sans remplacement diesel
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - 'Observer : demarrage long ou difficile par temps froid ?'
  - Voyant prechauffage allume plus reste ?
  - 'Observer : fumee blanche au demarrage qui persiste ?'
  - 'Observer : rates moteur a froid les premieres secondes ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Demarrage long ou difficile par temps froid
  - Voyant prechauffage allume plus reste
  - Fumee blanche au demarrage qui persiste
  - Rates moteur a froid les premieres secondes
  - Odeur de gazole non brule au demarrage
  - Plus de 100 000 km sans remplacement diesel
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '243'
  intro_title: A quoi sert Bougie de préchauffage ?
  risk_title: Pourquoi remplacer Bougie de préchauffage a temps ?
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
  - question: Bougie de préchauffage OE ou adaptable ?
    answer: 'Les bougies OES (Beru, Bosch, NGK) sont de qualité équivalente à l''OE. Vérifiez le type : crayon standard, céramique
      ou autorégulée selon votre moteur.'
  - question: Comment savoir si mes bougies de préchauffage sont HS ?
    answer: Démarrage difficile à froid, voyant préchauffage anormal, test à l'ohmmètre (résistance infinie = bougie HS),
      fumée blanche persistante.
  - question: Tous les combien changer les bougies de préchauffage ?
    answer: Entre 80 000 et 120 000 km selon type. Les bougies céramique durent plus longtemps. À vérifier tous les 60 000
      km sur diesel.
  - question: Peut-on changer les bougies de préchauffage soi-même ?
    answer: Oui mais attention au grippage. Démonter moteur chaud, utiliser un dégrippant, ne pas forcer. Risque de casse
      dans la culasse si grippée.
  - question: Quelle erreur éviter avec les bougies de préchauffage ?
    answer: Ne jamais forcer une bougie grippée. Utiliser le bon couple de serrage. Changer les 4 même si une seule est HS.
      Laisser refroidir avant test.
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
doc_id: 54fb51fb-5676-57b4-9355-8b8866e561e2
content_hash: sha256:a29b4ee751d0b776
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
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'céramique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_050__c: '050 °C'
    val_12_a: '12 a'
    val_30_a: '30 a'
  materials:
  - materiau: 'céramique'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'La bougie de préchauffage fonctionne comme une résistance, l''énergieélectrique est conduite par un filament qui s''échauffe
    et devient incandescentpuisqu''il peut dépasser les 1000° C. La fonction principale des bougies de préchauffage est dedélivrer
    une énergie supplémentaire pour le démarrage. Avant le démarrage du moteur, la bougie de préchauffage estmise sous tension
    et le crayon à incandescence de la bougie est porté à unetempérature supérieure à 800° C. Cette chaleur améliore de manière
    considérablela capacité de démarrage à froid du moteur. Le dégagement de chaleur de labougie de préchauffage optimise
    par ailleurs la combustion, réduisant lesfumées et autres émissions polluantes. En savoir plus : bougie de préchauffage
    — définition et rôle mécanique 🚨 Bruit Bougie de préchauffage : causes et diagnostic'
  S2: '- Démarrages difficiles dumoteur surtout à froid. - Le moteur tourne mais nedémarre pas. - Après le démarrage, fortdégagement
    de fumée. - Surconsommation decarburant. Diagnostic complet : identifier une panne de bougie de préchauffage'
  S3: 'La bougie de préchauffage chauffe la chambre de combustion du moteur diesel avant le démarrage à froid, permettant
    l''auto-inflammation du gazole sans apport d''étincelle. Sur les moteurs diesel modernes à injection directe, la température
    de préchauffage atteint 850 à 1 000°C en moins de 2 secondes (bougies à régulation rapide). Un choix incorrect de bougie
    génère soit un démarrage difficile à froid, soit une casse de bougie dans la culasse — réparation particulièrement coûteuse.
    - Type de bougie : céramique (SiN) ou métal (acier inox) — Les bougies céramique modernes (ex : Bosch Dura-Speed, NGK
    Y-Type) atteignent 1 000°C en 2 secondes contre 6 à 8 secondes pour les bougies métal. Elles sont indispensables sur les
    moteurs Euro 5 et Euro 6 à démarrage quasi-instantané. Ne pas substituer une bougie céramique par une bougie métal : le
    temps de chauffe du boîtier est configuré pour le type d''origine. - Tension nominale de fonctionnement : 11 V ou 5 V
    (bougies à basse tension) — Certains constructeurs récents (PSA, Renault 1.5 dCi) utilisent des bougies 5 V pour limiter
    la consommation électrique au démarrage. Ces bougies ne sont pas interchangeables avec les bougies 11 V standards : une
    bougie 11 V alimentée en 5 V ne chauffe pas suffisamment ; une bougie 5 V alimentée en 11 V se détruit immédiatement.
    - Diamètre et pas de filetage : M8 x 1 ou M10 x 1 — Le filetage M8x1 équipe la majorité des moteurs diesel modernes compacts
    (1.3 à 2.0 L). Le M10x1 se retrouve sur les anciens moteurs et sur certains utilitaires. Un mauvais filetage abîme la
    culasse ; sur un moteur diesel, le retaraudage d''un puits de bougie est une opération délicate et coûteuse. - Longueur
    hors-tout et longueur de filetage (reach) — La longueur de filetage varie de 8 à 26 mm selon la profondeur du préchambre.
    Une bougie trop courte ne précauffe pas la zone d''injection ; une bougie trop longue heurte le piston. Ces deux erreurs
    provoquent une casse de bougie ou une destruction du piston. - Résistance à froid (Ω) — vérification avant achat sur moteur
    à préchambre — Sur un moteur à chambre de précombustion, la résistance d''une bougie neuve est mesurable : entre 0,5 et
    1,5 Ω selon le type. Une mesure supérieure à 3 Ω indique une bougie ouverte (filament grillé). Cette vérification permet
    de s''assurer qu''une bougie de remplacement issue d''un lot est conforme. - Intervalle de remplacement : tous les 60
    000 à 100 000 km en préventif — La durée de vie recommandée est de 60 000 km pour les bougies métal standard, jusqu''à
    100 000 km pour les bougies céramique de qualité. Au-delà, le filament s''oxyde et la montée en température ralentit,
    ce qui soumet le boîtier de préchauffage à des cycles de chauffe prolongés qui l''usent prématurément. - Marque et homologation
    constructeur — vérifier la liste d''applications — NGK, Bosch, Denso et BERU sont les fabricants de référence avec des
    listes d''applications validées par les constructeurs automobiles. Les bougies génériques sans liste d''application constructeur
    présentent des risques de mauvais positionnement du filament dans la chambre. Pour aller plus loin : consultez notre guide
    d''achat bougie de préchauffage — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Bougie de préchauffage pour connaître les spécifications. -
    Débranchez la batterie. - Débranchez les connecteurs des bougies depréchauffage. - Mettre un anti-dégrippant si les bougiessont
    grippées (faire attention que le liquide ne coule pas dans la culasseaprès l'extraction des bougies). - Dévissez les bougies
    de préchauffage.
  S4_REPOSE: 'Le remontage des bougies de préchauffage sur un moteur diesel exige du soin : le filetage dans la culasse, souvent
    fragilisé par la chaleur et la corrosion, supporte mal les erreurs de serrage. Si le moteur était chaud lors du démontage,
    attendez qu''il soit redescendu à température ambiante — le métal dilaté rend le serrage imprecis. - Vérifiez que les
    bougies de préchauffage neuves sont identiques aux bougies déposées : type (crayon standard, céramique ou autorégulée),
    diamètre du filetage et longueur. Ne mélangez pas des types différents sur le même moteur. - Contrôlez l''état du boîtier
    de préchauffage et des fils d''alimentation électrique des bougies. Un boîtier défaillant grillera les nouvelles bougies
    rapidement. - Appliquez un léger film de graisse anti-grippage à haute température sur le filetage des bougies neuves
    (sans en mettre sur la tige chauffante ni sur la zone de contact électrique). - Vissez chaque bougie de préchauffage à
    la main jusqu''à la butée, sans forcer. Si vous sentez une résistance avant la butée, arrêtez — le filetage dans la culasse
    est peut-être endommagé. - Serrez les bougies au couple prescrit à l''aide d''une clé dynamométrique : en général entre
    8 et 15 Nm selon le type de bougie et le constructeur (valeur exacte dans la fiche technique). Un sur-serrage fissure
    la céramique ou endommage le filetage culasse ; un sous-serrage provoque des fuites de compression. - Rebranchez les connecteurs
    électriques de chaque bougie en vous assurant du bon verrouillage. Vérifiez que les fils ne sont pas sous tension mécanique.
    - Rebranchez la batterie. - Mettez le contact sans démarrer et observez le comportement du voyant de préchauffage : il
    doit s''allumer brièvement puis s''éteindre. S''il reste allumé ou clignote, vérifiez le connecteur ou le boîtier de préchauffage.
    - Démarrez le moteur et contrôlez l''absence de raté à froid, de fumée blanche persistante et d''odeur de gazole non brûlé.
    - Effacez les codes défaut OBD mémorisés avant l''intervention à l''aide d''un outil de diagnostic.'
  S5: 'Erreurs frequentes avec les bougies de prechauffage : - Forcer le devissage d''une bougie grippee — la bougie casse
    dans la culasse et l''extraction necessite un outillage specifique couteux. Utiliser du debloquant et un couple progressif-
    Ne pas remplacer les bougies par jeu complet — si une bougie est defaillante, les autres ont le meme age et vont lacher
    rapidement- Oublier de debrancher la batterie avant intervention — les bougies sont alimentees en 12V, risque de court-circuit-
    Confondre bougie de prechauffage et bougie d''allumage — les bougies de prechauffage sont exclusivement pour les moteurs
    diesel- Ignorer un demarrage difficile a froid avec fumee blanche — symptome classique de bougies de prechauffage usees,
    ne pas accuser le demarreur- Ne pas respecter le couple de serrage au remontage (10 a 15 Nm selon constructeur) — une
    bougie trop serree se deforme et casse'
  S6: 'Après le remplacement de vos bougies de préchauffage, effectuez ces vérifications dans l''ordre. - Vérifier le couple
    de serrage de chaque bougie selon la fiche technique constructeur : un serrage insuffisant provoque une fuite de compression,
    un serrage excessif casse le filetage dans la culasse - Contrôler que le voyant de préchauffage s''allume au démarrage
    puis s''éteint en moins de 15 secondes à température ambiante - Tester le démarrage à froid dès que la température descend
    sous 5°C : aucune fumée blanche persistant au-delà de 2 minutes n''est acceptable - S''assurer de l''absence d''odeur
    de gazole non brûlé à l''échappement moteur en température - Effectuer une lecture de codes à la valise OBD après 50 km
    : vérifier l''absence de tout code lié au préchauffage (P0380, P0381, P0670 à P0679) - Pour un remplacement à plus de
    100 000 km, contrôler simultanément le boîtier de préchauffage et les connecteurs des bougies Retrouvez les spécifications
    techniques sur la fiche référence bougie de préchauffage.'
  S7: Quel est le prix d'un bougie de préchauffage ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur
    pour trouver le bougie de préchauffage compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon bougie de préchauffage est à changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un bougie de
    préchauffage défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l'urgence du remplacement.- chauffer - prechauffer - rechauffer
  S8: Comment choisir Bougie de préchauffage compatible avec mon vehiculeRenseignez marque, modele, type moteur et annee,
    puis verifiez la reference Quand remplacer Bougie de préchauffage ?En cas de demarrage long ou difficile par temps froid
    ou de degradation Puis-je monter Bougie de préchauffage sans verification atelier ?Le montage peut exiger controles de
    couple, alignement et references.
  META: '{"meta_title":"Bougie de préchauffage : quand changer ? | AutoMecanik","meta_description":"Démarrage long à froid,
    fumée blanche, voyant allumé : identifiez une bougie de préchauffage HS et remplacez-la au bon moment sur votre diesel.","og_title":"Bougie
    de préchauffage diesel : symptômes et remplacement","og_description":"Démarrage difficile par temps froid ? 6 signes d''une
    bougie HS : voyant, fumée blanche, ratés à froid. Guide pour choisir la bonne pièce.","sources":[{"type":"rag","ref":"gammes/bougie-de-
    prechauffage.md","field":"diagnostic.symptoms,domain.role,rendering.faq"}]}'
---

# Bougie de préchauffage - Guide Diagnostic Complet

## Fonction et Rôle

Chauffer la chambre de combustion a froid pour faciliter le demarrage diesel - N'agit qu'au demarrage

**Actions principales:** chauffer, prechauffer, rechauffer, porter a temperature, faciliter le demarrage

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage long ou difficile par temps froid
- voyant prechauffage allume plus reste
- fumee blanche au demarrage qui persiste
- rates moteur a froid les premieres secondes
- odeur de gazole non brule au demarrage
- plus de 100 000 km sans remplacement diesel

## Procédure de Diagnostic

Pour diagnostiquer un problème de bougie de préchauffage:

1. **Inspection visuelle** - Examiner l'état du bougie de préchauffage
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

- alternateur
- boitier-de-prechauffage
- demarreur
- filtre-a-carburant

## Critères de Compatibilité

Pour commander le bon bougie de préchauffage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"

## FAQ

**Bougie de préchauffage OE ou adaptable ?**
Les bougies OES (Beru, Bosch, NGK) sont de qualité équivalente à l'OE. Vérifiez le type : crayon standard, céramique ou autorégulée selon votre moteur.

**Comment savoir si mes bougies de préchauffage sont HS ?**
Démarrage difficile à froid, voyant préchauffage anormal, test à l'ohmmètre (résistance infinie = bougie HS), fumée blanche persistante.

**Tous les combien changer les bougies de préchauffage ?**
Entre 80 000 et 120 000 km selon type. Les bougies céramique durent plus longtemps. À vérifier tous les 60 000 km sur diesel.

**Peut-on changer les bougies de préchauffage soi-même ?**
Oui mais attention au grippage. Démonter moteur chaud, utiliser un dégrippant, ne pas forcer. Risque de casse dans la culasse si grippée.

**Quelle erreur éviter avec les bougies de préchauffage ?**
Ne jamais forcer une bougie grippée. Utiliser le bon couple de serrage. Changer les 4 même si une seule est HS. Laisser refroidir avant test.


## Conseils supplementaires

<!-- materialized-from-db web/2d8006fe60a7 2026-03-03 -->
### La direction assistée - Sondage au hasard :

## Sondage au hasard :

Pour l'achat d'une auto vous optez pour :

Sur le même sujet

- Fonctionnement d'une voiture électrique

- Les différents types d'hybrides : Micro hybride MHEV, Full hybride (HEV) et PHEV

- Cycle Miller : une variante du cycle classique dit Otto

- Cycle Atkinson : une variante du cycle classique dit Otto

- Otto : le cycle classique d'un moteur à quatre temps

- Les principaux composants d'un moteur thermique

- Les masses mobiles d'un moteur

- Moteur 6 temps Porsche : bien comprendre le fonctionnement

- Les facteurs de pertes du moteur thermiques (rendement)

- Le cycle à 4 temps du moteur diesel en détails

- Le cycle à 4 temps du moteur essence en détails

- Cycle 4 temps : différences entre essence et diesel

- Fonctionnement d'un moteur

- Comment fonctionne la recharge par induction

- Taux de compression : définition, mesures et problèmes potentiels

- Le couvre-culasse : le couvercle de la culasse ?

- Les différentes courroies d'un moteur (distribution et accessoires)

- Recyclage des gaz d'échappement : les différents systèmes

- Les différents mécanismes qui corrigent le jeu aux soupapes

- Poussoirs hydrauliques : utilité et fonctionnement

- Les pastilles de compensation d'usure (soupapes)

- Fonctionnement et constituants du vilebrequin

- Fonctionnement du moteur rotatif (type Wankel)

- Différence entre une vanne EGR haute pression et basse pression

- Pompe à vide : fonctionnement, variantes et problèmes

- Pompe d'injection d'air secondaire : utilité et fonctionnement

- Fonctionnement des galets tendeurs

- Rôle des clapets / volets d'admission

- Les différents capteurs de vitesse

- Les différents types d'échangeurs d'un moteur

- Utilité et rôles de l'échangeur air / air pour un moteur

- Capteurs liés au turbo

- Gestion thermique / refroidissement d'une voiture électrique

- Compression d'un moteur : comment et pourquoi ?

- Principe du starter

- Le régulateur de ralenti / moteur pas à pas

- Fonctionnement de la distribution variable

- Fonctionnement du moteur à compression variable

- Les différents capteurs et sondes d'une voiture

- L'admission d'air

- La poulie damper : rôle et faiblesses

- Utilité et pannes de la sonde lambda

- Différences entre carter sec et humide

- Lubrification avec carter sec

- Le calorstat / Thermostat

- La segmentation d'un moteur

- Reniflard : fonctionnement et problèmes

- Le collecteur d'admission : utilité et fonctionnement

- Double arbre à cames en tête

- Soupapes

- Arbre à cames : rôle, types et emplacements

- Boîtier Papillon

- Fonctionnement de la distribution d'un moteur

- Fonctionnement du débitmètre

- Rôle du boitier BSI (boitier de servitude intelligent)

- Fonctionnement de la vanne EGR

- Fonctionnement d'un alternateur

- Refroidissement moteur

- Fonctionnement d'une bougie d'allumage

- Les types de bougies d'allumage

- L'allumage d'un moteur essence

- Utilité et avantages de la double injection : directe et indirecte

- Canister : fonctionnement et pannes

- Programmation des injecteurs : utilité et méthode

- La charge stratifiée : comment et pourquoi ?

- Circuit de carburant / injection

- Injection monopoint et multipoint

- Différence entre injection classique et rampe commune

- Différence entre injection directe et indirecte

- Fonctionnement de l'injection

- Turbo électrique : fonctionnement et utilité

- Fonctionnement Skyactiv-X

- La Dump Valve : principe

- Différences entre moteur atmosphérique et suralimenté par turbo

- Fonctionnement des moteurs bi-turbo

- Fonctionnement du diesel tri-turbo BMW 50d

- Fonctionnement de la wastegate

- Fonctionnement détaillé du turbo

- Différences entre volant moteur mono-masse et bi-masses

- Volant moteur : utilité et fonctionnement

- Fonctionnement de la transmission Xdrive BMW

- Avantages et inconvénients d'une transmission intégrale 4 roues motrices

- Torque Vectoring / Couple vectoriel : fonctionnement

- Les types de différentiels à glissement limité

- Différences entre Torsen et Haldex

- Différentiel Torsen : fonctionnement

- Fonctionnement de la transmission Haldex

- Fonctionnement du Quattro d'Audi

- Embrayage multidisque : fonctionnement détaillé

- Technique du double débrayage

- Fonctionnement boîte automatique (BVA)

- Démultiplication des rapports de boîte

- Différentiel autobloquant ou à glissement limité

- Fonctionnement de la commande hydraulique d'embrayage

- Fonctionnement d'une boîte double embrayage

- Fonctionnement du convertisseur de couple (BVA)

- Le différentiel ("ouvert" / classique) : fonctionnement

- Les différents types de boîtes automatiques

- Fonctionnement d'une boîte de vitesses

- Fonctionnement de l'embrayage

- Fonctionnement de l'Adblue / SCR

- Fonctionnement du FAP

- Fonctionnement du catalyseur

- Ligne d'échappement : les constituants

- La portance / appui aérodynamique d'une voiture

- Différences entre le Cx et le sCx

- La traînée aérodynamique d'une voiture

- L'effet de sol : comment est-il produit ?

- Lien entre puissance et vitesse de pointe

- Freinage par fil (IBS / By Wire) et sans lien physique

- L'aérodynamisme d'une voiture (Cx, sCx, trainée etc.)

- Calcul des distances de freinage

- Fonctionnement des freins à tambour

- Types de disques de frein

- Freinage : facteurs déterminants

- Fonctionnement des freins

- Comprendre la géométrie d'une voiture

- Les (nombreuses) variables liées à l'insonorisation d'une voiture

- Fonctionnement de la direction par fil "By Wire"

- Barre anti-roulis ACTIVE : utilité et fonctionnement

- Fonctionnement de la direction assistée hydraulique

- Fonctionnement de la direction électrique

- Rôle et fonctionnement du capteur d'angle volant

- Rôle et fonctionnement du capteur de couple volant

- Volant capacitif : avantages et fonctionnement

- Freinage : les facteurs déterminants

- E-Active Body Control

- Active / Magic Body Control

- Les facteurs / variables qui favorisent le confort de suspension

- Fonctionnement de la suspension

- Fonctionnement des amortisseurs

- Roues arrière directices : fonctionnement des dispositifs existants

- Amortissement Citroën Advanced Comfort

- Les types de châssis d'une voiture

- Amortissement piloté / suspension adaptative

- Suspension pneumatique : fonctionnement / architecture

- Bien choisir ses jantes : les conseils déterminants

- La direction assistée

- Les types de suspensions : Macpherson, Double triangle, Multibras etc.

- Suspension active et semi-active

- Tenue de route : les facteurs déterminants

- Roulement à bille

- Parallélisme : pincement et ouverture

- Angle de carrossage

- Différence entre amortisseur et ressort de suspension

- Rôle de la barre anti-roulis / stabilisatrice

- Capteur d'arbre à cames : principe et pannes

- Rôle du capteur PMH

- Fonctionnement d'une pompe à chaleur pour automobile

- Le chauffage : principe

- Fonctionnement de la climatisation

- Kit protoxyde d'azote Nitrous / N2O

- Pompe à essence : fonctionnement

- Pompe de gavage

- Correcteur / répartiteur de freinage

- Le boitier ABS

- Fonctionnement de l'ABS

- Fonctionnement de l'Hybrid+ de MG

- Fonctionnement du freinage régénératif

- Fonctionnement de l'hybride rechargeable PSA : HYbrid2 et HYbrid4

- Fonctionnement des hybrides TFSIe (E-Tron et GTE)

- Fonctionnement de l'hybride Toyota HSD

- Hybrid Assist de Renault

- Le bobinage en épingle à cheveux : principe et avantages

- Rôle et fonctionnement des relais

- Eclairage Led matriciel / Matrix Led

- Voiture à hydrogène : fonctionnement

- Fonctionnement des batteries lithium-ion

- Batterie de voiture au plomb : principe

- Le moteur électrique

- Vitres électriques : fonctionnement et pannes

- Phares automatiques

- Essuie-glace automatique

- Types d'éclairage : LED, Xénon, Laser etc ...

- Le démarreur

- Fonctionnement de l'AFU

- Fonctionnement de l'ESP

- Fonctionnement des phares au Xénon

- Fonctionnement du radar de recul

- Fonctionnement du ParkAssist (stationnement automatique)

- Fonctionnement Stop and Start

- Différences entre moteur électrique et moteur thermique

- Comment sont produits et extraits l'essence et le diesel ?

- Les différentes positions possibles d'un moteur

- Rapport entre cylindrée et puissance

- Moteur transversal et longitudinal

- Différence entre puissance et couple

- Différences entre ESSENCE et DIESEL

- Savoir lire une fiche technique

- Liste des aides à la conduite

- Les différents segments du marché

- Les différentes architectures moteur

- Moteur en ligne VS moteur en V

- Avantages et inconvénients de la propulsion

- Fonctionnement du rupteur

- Soft Limiter : Pourquoi certains moteurs refusent de hurler à l?arrêt ?

- Comment fonctionne une cartographie moteur ?

- Moteur à injection d'eau

- Système Pantone : principe et faisabilité

- Fonctionnement des hybrides BYD (EHS, DM-i et DM-o)

- Fonctionnement / caractéristiques de l'Hybride 4X4 de Dacia

- Moteur électrique à flux axial : fonctionnement, avantages et inconvénients

- Les types de déphaseurs

- Les types de vilebrequins

- Caractéristiques des carburants

- Comment fonctionne le témoin d'usure des plaquettes

- Circuit de freinage d'une auto

- Différences entre étriers fixes et flottants

- Tout sur le Multiplexage d'une voiture

- Technique du revêtement plasma par bore spray coating

- Suspension hydropneumatique

- Capteurs liés à l'admission d'air d'un moteur

- Fonctionnement des boîtes de transfert

- Largeur des voies : notions techniques et subtilités

- Fonctionnement du Launch Control

- Différence entre cliquetis et auto-allumage ?

- Utilité et fonctionnement du préchauffage

- Boîte CVT à variation continue

- Lubrification d'un moteur

- Comment fonctionne le frein moteur ?

- Pourquoi les voitures modernes ont moins de frein moteur ?

- Arbre d'équilibrage moteur : fonctionnement et pannes potentielles

- Coupure des cylindres ACT : fonctionnement

- Fonctionnement des cylindres à la demande (cylinder on demand)

Nouveautés auto

- Marché auto : 2026 commence en marche arrière (neuf et occasion réunis)

- Test d'autonomie de VE à -31°C : bonnes surprises et aberrations à dénoncer

- Classe S restylée : plus E que jamais ? Revue détaillée ...

- Tesla acte la fin des Model S et Model X, et ce n'est pas anodin

- Tesla revoit la monétisation de son Autopilot : plus rien de série, tout passe par la location

- La Chine envisage d'interdire les poignées escamotables à partir de 2027

- Des chiffres concrets sur la fin de la propriété automobile

- La pollution induite par les voitures électriques mise en évidence par des drones ?!

- Quand l'industrie auto commence à parler défense, c'est mauvais signe

- Fiat propose de brider les voitures pour tout un tas d'intérêts ...

- Immatriculations frauduleuses : quand l'État se fait pirater et envoie la facture aux garages

- Stellantis abandonne l'hybride rechargeable aux USA

Choisir une voiture

- Avis voitures

- Essais voitures

- Classement auto

- Consommation auto

- Fiabilité auto

- Témoignages fiabilité

- Pannes connues

- Rappels constructeurs

Fiabilité / Entretien

- Entretenir son auto

- Fonctionnement d'une auto

- Définitions voitures

- Les chiffres de l'auto

© CopyRights Fiches-auto.fr 2026. Tous droits de reproductions réservés. Nous contacter - Mentions légales Fiches-auto.fr participe et est conforme à l'ensemble des Spécifications et Politiques du Transparency & Consent Framework de l'IAB Europe. Il utilise la Consent Management Platform n°92. Vous pouvez modifier vos choix à tout moment en cliquant ici .

## References supplementaires

<!-- materialized-from-db manual/2eb504a5fe75 2026-04-03 -->
### Données techniques OEM — Bougie de préchauffage

# Données techniques OEM — Bougie de préchauffage
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- céramique
- électrique

## Matériaux
- céramique

## Valeurs techniques de référence
- 050 °C
