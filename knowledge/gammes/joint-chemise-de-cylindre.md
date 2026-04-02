---
category: moteur
slug: joint-chemise-de-cylindre
title: Joint chemise de cylindre
pg_id: 128
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-03-29'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: skill:phase5-vague6
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Assurer l'etancheite entre la chemise et le bloc moteur
  must_be_true:
  - assurer l'etancheite
  - isoler
  must_not_contain:
  - freinage
  - climatisation
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - assurer l'etancheite
  - isoler
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
  - ❌ "repare le moteur"
  cost_range:
    min: 5
    max: 200
    currency: EUR
    unit: l'unite
    source: estimation categorie
  brands:
    premium:
    - Elring
    - Victor Reinz
    standard:
    - Febi
    - Ajusa
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Melange eau-huile mayonnaise
    severity: confort
  - id: S2
    label: Surchauffe moteur sans fuite visible
    severity: confort
  - id: S3
    label: Perte de compression sur un cylindre
    severity: confort
  causes:
  - identifier origine fuite et verifier joints
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  - 'Usure ou defaillance causant : melange eau-huile mayonnaise'
  depose_steps: []
  quick_checks:
  - 'Observer : melange eau-huile mayonnaise ?'
  - 'Observer : surchauffe moteur sans fuite visible ?'
  - 'Observer : perte de compression sur un cylindre ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Melange eau-huile mayonnaise
  - Surchauffe moteur sans fuite visible
  - Perte de compression sur un cylindre
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '128'
  intro_title: A quoi sert Joint chemise de cylindre ?
  risk_title: Pourquoi remplacer Joint chemise de cylindre a temps ?
  risk_explanation: '**Défaillance progressive** - Usure normale due à l''utilisation'
  risk_consequences:
  - '**Défaillance progressive** - Usure normale due à l''utilisation'
  - '**Conditions d''utilisation** - Sollicitations excessives ou environnement défavorable'
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
  - question: Comment choisir Joint chemise de cylindre compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Joint chemise de cylindre ?
    answer: En cas de melange eau-huile mayonnaise ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Joint chemise de cylindre sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
  quality:
    score: 60
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: c01b0462-c91a-5f52-9b6b-410c606b8811
content_hash: sha256:273972354de0f9d4
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
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    depassement_chemise: '0,02 a 0,08 mm au-dessus du bloc (verifier au comparateur)'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le joint de chemise de cylindre est une pièce d'étanchéité annulaire qui
    assure l'étanchéité entre la chemise de cylindre et le bloc moteur. Il isole
    le circuit de refroidissement du carter d'huile et de la chambre de
    combustion, empêchant tout mélange entre les fluides moteur (huile, liquide
    de refroidissement, gaz de combustion). Dans les moteurs équipés de chemises
    de cylindres amovibles (c'est-à-dire des cylindres rapportés dans le bloc,
    par opposition aux cylindres usinés directement dans la masse), chaque
    chemise est scellée en bas par un ou plusieurs joints toriques ou joints
    plats. Ces joints travaillent dans un environnement extrême : températures
    allant de l'ambiante jusqu'à plus de 100°C pour le liquide de
    refroidissement qui circule autour des chemises, pression de combustion
    transmise à travers les parois, et vibrations mécaniques continues. La
    défaillance de ce joint se distingue du joint de culasse par sa localisation
    en bas de chemise plutôt qu'en tête. Elle provoque les mêmes symptômes
    catastrophiques : mélange eau-huile, surchauffe moteur, perte de compression
    — mais affecte spécifiquement l'interface chemise-bloc. Les pièces à
    contrôler systématiquement lors d'une intervention sont la chemise de
    cylindre elle-même (usure, ovalisations) et le joint de culasse.
  S2: >-
    Les symptômes d'un joint de chemise de cylindre défaillant sont parmi les
    plus sérieux de la mécanique moteur. Leur apparition doit déclencher un
    arrêt immédiat du diagnostic et de l'utilisation du véhicule : - Mélange
    eau-huile dit "mayonnaise" : la contamination croisée entre le circuit de
    refroidissement et le circuit d'huile produit une émulsion jaunâtre ou beige
    visible sous le bouchon de remplissage d'huile ou sur la jauge. C'est le
    signe le plus caractéristique et le plus grave d'une défaillance
    d'étanchéité. - Surchauffe moteur sans fuite visible externe : le liquide de
    refroidissement s'échappe dans le carter d'huile ou dans la chambre de
    combustion sans s'évacuer à l'extérieur du moteur. Le niveau de liquide
    baisse, la température monte — sans qu'aucune flaque ne soit visible sous le
    véhicule. - Perte de compression sur un cylindre : lors d'un test de
    compression, un cylindre affiche une valeur nettement inférieure aux autres
    (écart de plus de 10 %). Cela indique une fuite du circuit de
    refroidissement ou des gaz de combustion à travers le joint de chemise. -
    Fumée blanche persistante à l'échappement : la combustion de liquide de
    refroidissement produit une fumée blanche dense et continue (différente de
    la condensation matinale qui disparaît après quelques minutes). La fumée a
    souvent une odeur douceâtre caractéristique. - Bulles dans le vase
    d'expansion : des gaz de combustion s'infiltrent dans le circuit de
    refroidissement et forment des bulles visibles dans le vase d'expansion lors
    du fonctionnement moteur.
  S3: >-
    Le joint de chemise de cylindre est une pièce de précision dont les
    dimensions doivent correspondre au millimètre près à la chemise et au
    logement du bloc. Les critères de sélection sont stricts : - Marque, modèle
    et code moteur : identifier précisément le code moteur inscrit sur la
    plaquette constructeur ou dans le carnet d'entretien. Deux moteurs du même
    modèle commercial peuvent avoir des chemises de diamètres différents selon
    l'année de production. - Diamètre extérieur de la chemise : mesurer le
    diamètre de la chemise en place si possible, ou se référer aux cotes
    constructeur. Un joint sous-dimensionné ne scelle pas ; un joint sur-
    dimensionné ne rentre pas dans le logement. - Matériau du joint selon les
    contraintes thermiques : joints toriques en EPDM pour les basses
    températures (circuit de refroidissement), joints en silicone haute
    température pour les zones proches des gaz de combustion. Respecter
    impérativement les spécifications constructeur. - Nombre de joints par
    chemise : certains moteurs utilisent un joint en bas de chemise plus un
    joint en haut (interface chambre de combustion). Vérifier combien de joints
    sont requis par chemise selon la documentation technique. - Achat en kit :
    les équipementiers spécialisés en mécanique moteur (Goetze, Elring, NPR)
    proposent des jeux de joints complets pour toutes les chemises du moteur.
    Cette option garantit la cohérence des cotes et évite des remontages
    partiels. - Vérification de l'état de la chemise et du logement : avant de
    commander, faire mesurer le diamètre des chemises par un rectifieur pour
    détecter une ovalisation. Un logement rayé dans le bloc devra être traité
    avant montage.
  S4_DEPOSE: >-
    Le remplacement des joints de chemise de cylindre est une opération de
    rectification moteur qui nécessite la dépose complète du moteur ou à minima
    de la culasse et parfois du carter d'huile. C'est une intervention lourde
    réservée à des mécaniciens expérimentés : - Diagnostic préalable obligatoire
    : avant de démonter, confirmer le diagnostic par un test de compression, un
    test de combustion des gaz du circuit de refroidissement (kit de détection
    CO2) et une analyse d'huile. Éviter un démontage lourd sur un doute. -
    Dépose de la culasse : vider le liquide de refroidissement et l'huile
    moteur. Déposer la culasse selon la procédure constructeur (ordre de
    desserrage des vis de culasse, couple de dépose). Contrôler la planéité de
    la culasse à la règle — une culasse voilée doit être rectifiée. - Extraction
    des chemises : utiliser un extracteur de chemise adapté (poulies, étriers,
    extracteur à vis). Ne jamais frapper sur une chemise pour l'extraire — cela
    endommage le logement du bloc. Marquer la position et l'orientation de
    chaque chemise pour la reposer dans la même position si elles sont
    réutilisées. - Nettoyage des logements et mesures : nettoyer les logements
    de chemise dans le bloc avec du produit dégraissant. Mesurer les diamètres
    et la propreté des portées. Faire confirmer par un rectifieur si nécessaire.
    - Remplacement des joints : retirer les anciens joints toriques de leurs
    gorges. Installer les nouveaux joints secs (sans lubrifiant sauf indication
    contraire) dans leurs gorges respectives. Vérifier qu'ils sont bien emboîtés
    sur toute leur circonférence. - Réintroduction des chemises : introduire
    chaque chemise dans son logement en appliquant une légère pression uniforme,
    sans jamais frapper. La chemise doit coulisser librement jusqu'à sa butée.
    Contrôler la dépassée de chemise (hauteur hors bloc) avec un comparateur —
    valeur à respecter selon le constructeur. - Repose de la culasse et serrage
    au couple : monter un joint de culasse neuf. Serrer les vis de culasse dans
    l'ordre et selon les cycles de serrage angulaire constructeur (généralement
    3 à 4 phases). Remplir les fluides et procéder à la mise en route
    progressive.
  S4_REPOSE: >-
    Après rectification du bloc et contrôle de la dépassée de chemise, la repose
    des joints de chemise de cylindre suit un protocole de précision. Un écart
    de quelques centièmes de millimètre peut provoquer une fuite immédiate au
    premier démarrage. - Contrôle final de la dépassée de chemise : mesurer au
    comparateur la hauteur de chaque chemise hors bloc avant toute repose de
    joint. La valeur doit être comprise dans la plage spécifiée par le
    constructeur (généralement 0,04 à 0,10 mm). Si une chemise est en dessous du
    minimum, ne pas poser les joints. - Nettoyage des portées de joint :
    dégraisser soigneusement la gorge du bloc et la base de la chemise avec un
    solvant propre et chiffon non pelucheux. Toute trace d'huile, de coolant ou
    de colle de joint ancien compromet l'étanchéité. - Pose des joints neufs à
    sec : installer les joints annulaires neufs dans leurs gorges respectives —
    joints du bas en caoutchouc pour le circuit de refroidissement, joint cuivre
    ou acier en haut si applicable. Ne pas lubrifier les joints O-ring avec de
    la graisse silicone sauf indication constructeur explicite. - Mise en place
    des chemises : introduire chaque chemise verticalement dans son alésage sans
    forcer. Une légère rotation de quelques degrés peut être nécessaire pour
    engager les joints dans leurs gorges. Un maillet en plastique peut aider si
    la chemise résiste. - Contrôle de la dépassée après mise en place : re-
    mesurer la dépassée de chaque chemise avec les joints en place. La valeur
    doit être identique à celle mesurée sans joint — si elle a changé, un joint
    est mal positionné dans sa gorge. - Pose de la culasse : monter le joint de
    culasse neuf orienté correctement (repère "haut" ou "top" visible),
    descendre la culasse sans glissement latéral. Serrer les vis de culasse au
    couple prescrit en procédant en croix depuis le centre vers les extrémités,
    en plusieurs passes progressives. - Rebranchement du circuit de
    refroidissement : reconnecter les durites, remplir le circuit avec le
    liquide de refroidissement préconisé (G11, G12, G13 selon le constructeur),
    purger les bulles d'air via le(s) bouchon(s) de purge prévu(s). Point de
    contrôle avant démarrage : vérifier le niveau d'huile (remettre si elle a
    été vidangée), vérifier l'absence de corps étrangers oubliés, reconnectrer
    la batterie. Le premier démarrage doit se faire moteur chaud progressivement
    — voir section Vérification.
  S5: >-
    L'intervention sur les joints de chemise de cylindre est complexe. Les
    erreurs suivantes sont les plus fréquentes et les plus coûteuses : -
    Négliger la dépassée de chemise : la hauteur de chemise hors bloc doit
    respecter une cote précise (généralement 0,04 à 0,10 mm selon le
    constructeur). Une dépassée insuffisante ne comprime pas correctement le
    joint de culasse ; une dépassée excessive concentre les contraintes et
    provoque une casse rapide. Ne pas mesurer cette cote est une erreur grave. -
    Réutiliser les joints toriques après dépose : les joints toriques qui ont
    travaillé sous pression et à haute température ont subi une déformation
    permanente. Les réutiliser garantit une fuite à court terme. Toujours monter
    des joints neufs, même si les anciens semblent intacts. - Intervertir les
    chemises lors du remontage : sur un moteur rodé, chaque chemise a développé
    une géométrie légèrement adaptée à son alésage. Remettre une chemise dans un
    autre alésage crée un appariement incorrect. Marquer et respecter la
    position d'origine. - Omettre le diagnostic culasse : une défaillance de
    joint de chemise provoque souvent une surchauffe qui voile la culasse.
    Remonter une culasse voilée sans la faire rectifier reproduit la défaillance
    dans les 10 000 km suivants. - Ne pas confirmer le diagnostic avant
    démontage : démonter un moteur pour joints de chemise sans avoir confirmé le
    diagnostic par des tests objectifs (compression, gaz CO2) risque de
    découvrir en cours de démontage que la vraie cause est un joint de culasse —
    ou une fissure de bloc — bien plus grave.
  S6: >-
    Après remplacement des joints de chemise de cylindre et remontage du moteur,
    une procédure de mise en route rigoureuse est indispensable pour valider
    l'intervention : - Contrôle de la dépassée de chemise avant repose de
    culasse : mesurer au comparateur la hauteur de chaque chemise hors plan de
    joint du bloc. Toute valeur hors tolérance impose une correction avant de
    refermer le moteur. - Test de compression après remontage : avant le premier
    démarrage complet, effectuer un test de compression à froid (débrancher
    l'injection ou l'allumage pour éviter le démarrage). Les 4 cylindres doivent
    afficher des valeurs homogènes et conformes aux spécifications constructeur.
    - Montée en température progressive et surveillance : lors du premier
    démarrage, laisser monter le moteur en température lentement. Observer la
    température moteur, vérifier l'absence de fumée blanche à l'échappement et
    surveiller le vase d'expansion pour détecter la formation de bulles. -
    Contrôle des niveaux d'huile et de liquide de refroidissement après 10
    minutes : couper le moteur, attendre 5 minutes, vérifier le niveau d'huile
    et sa couleur (aucune contamination par l'eau). Vérifier le niveau de
    liquide de refroidissement et sa clarté. - Inspection sous le véhicule après
    le premier trajet de 20 km : examiner les joints, le dessous moteur,
    rechercher toute trace de fuite de liquide de refroidissement ou d'huile. Un
    suivi du niveau d'huile toutes les 500 km pendant les 2 000 premiers km est
    conseillé.
  S7: >-
    Le remplacement des joints de chemise de cylindre est une intervention
    moteur profonde. D'autres pièces doivent systématiquement être vérifiées et
    souvent remplacées dans le même temps pour éviter de démonter à nouveau le
    moteur à court terme. - Joint de culasse : la culasse est obligatoirement
    déposée pour accéder aux chemises. Le joint de culasse doit être remplacé
    systématiquement à chaque dépose — jamais réutilisé, même s'il semble
    intact. - Chemise de cylindre : si la chemise présente une rayure axiale,
    une ovalisation ou une corrosion par piqûres, elle doit être remplacée en
    même temps que le joint. Une chemise endommagée ne tiendra pas même avec un
    joint neuf. - Joints d'étanchéité moteur (kit complet) : lors d'une
    intervention à ce niveau, remplacer tous les joints de culasse, joints de
    soupapes et joints de cache culbuteurs par un kit moteur complet pour une
    remise à neuf totale. - Liquide de refroidissement : le circuit de
    refroidissement est vidangé lors de la dépose. Remettre du liquide neuf
    adapté à votre motorisation (G11, G12+ ou G13 selon constructeur). Ne jamais
    mélanger les types. - Vis de culasse : sur la plupart des motorisations
    modernes, les vis de culasse sont à usage unique (élastiques avec
    allongement permanent). Vérifier la préconisation constructeur — si usage
    unique, ne jamais réutiliser.
  S8: >-
    Quelle est la différence entre un joint de chemise et un joint de culasse ?
    Le joint de culasse assure l'étanchéité entre la culasse et le bloc moteur
    en haut des cylindres (interface chambre de combustion). Le joint de chemise
    de cylindre assure l'étanchéité entre la chemise amovible et son logement
    dans le bloc moteur — généralement en bas de la chemise, du côté du circuit
    de refroidissement et du carter d'huile. Les deux joints peuvent présenter
    des symptômes similaires (mélange eau-huile, surchauffe) mais à des
    localisations différentes dans le moteur. Tous les moteurs ont-ils des
    chemises de cylindres avec joints ? Non. Seuls les moteurs à chemises
    amovibles (dites "humides" ou "sèches") sont concernés. Les moteurs à
    cylindres usinés directement dans le bloc (bloc monolithique fonte ou
    aluminium) n'ont pas de joint de chemise au sens strict. Les moteurs diesel
    de forte cylindrée et les moteurs de poids lourds utilisent plus fréquemment
    des chemises humides que les moteurs essence de petite cylindrée. Peut-on
    conduire avec un joint de chemise défaillant ? Non. Une défaillance de joint
    de chemise provoque la contamination de l'huile par l'eau, ce qui détruit la
    lubrification en quelques dizaines de kilomètres. La surchauffe associée
    peut voiler la culasse ou fissurer le bloc moteur. Continuer à rouler avec
    ces symptômes transforme une réparation de quelques centaines d'euros en
    remplacement de moteur. Arrêt immédiat et diagnostic obligatoires. Combien
    coûte le remplacement des joints de chemise de cylindre ? Le coût de la
    main-d'oeuvre est élevé car l'opération nécessite la dépose de la culasse et
    l'extraction des chemises — soit 6 à 15 heures de travail selon le moteur. À
    cela s'ajoutent les joints, le joint de culasse neuf, la rectification
    éventuelle de la culasse et le remplissage des fluides. Prévoir un budget
    total entre 800 et 2 500 euros selon le moteur et l'atelier. Une fois les
    symptômes confirmés, l'intervention est incontournable.
  META: >-
    {"meta_title":"Joint chemise de cylindre : symptômes et
    remplacement","meta_description":"Mayonnaise sous le bouchon d'huile,
    surchauffe moteur ou perte de compression ? Repérez les signes d'un joint de
    chemise défaillant avant la casse moteur."}
---

# Joint chemise de cylindre - Guide Diagnostic Complet

## Fonction et Rôle

Assurer l'etancheite entre la chemise et le bloc moteur

**Actions principales:** assurer l'etancheite, isoler

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Surchauffe moteur sans fuite visible**
  surchauffe moteur sans fuite visible

### 🟢 Autres Symptômes

- melange eau-huile mayonnaise
- perte de compression sur un cylindre

## Procédure de Diagnostic

Pour diagnostiquer un problème de joint chemise de cylindre:

1. **Inspection visuelle** - Examiner l'état du joint chemise de cylindre
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- chemise-de-cylindre
- joint-de-culasse

## Critères de Compatibilité

Pour commander le bon joint chemise de cylindre, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"

## FAQ

**Comment choisir Joint chemise de cylindre compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Joint chemise de cylindre ?**
En cas de melange eau-huile mayonnaise ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Joint chemise de cylindre sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
