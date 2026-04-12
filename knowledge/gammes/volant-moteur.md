---
category: embrayage
slug: volant-moteur
title: Volant moteur
pg_id: 577
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
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Lisser les vibrations du moteur, supporter le disque d'embrayage et transmettre l'inertie
  must_be_true:
  - lisser
  - supporter
  - transmettre l'inertie
  must_not_contain:
  - butée
  - pédale
  - commande
  - differentiel
  - cardan
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - kit-d-embrayage
  - butee-d-embrayage
  - emetteur-d-embrayage
  - recepteur-d-embrayage
  - cable-d-embrayage
  confusion_with:
  - term: piece-d-embrayage-voisine
    difference: Le systeme d embrayage comporte plusieurs pieces (disque, mecanisme, butee, emetteur, recepteur). Verifier
      laquelle est defectueuse.
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
  - ❌ "embraye mieux"
  cost_range:
    min: 273
    max: 756
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  brands:
    premium:
    - Sachs (ZF)
    - LuK (Schaeffler)
    - Valeo
    standard:
    - Aisin
    - Blue Print
    - Japanparts
    budget:
    - Valeo (kit 4P)
    - Sachs (kit conversion)
  quality_tiers:
  - tier: Origine (OE/OES)
    description: Volants moteur fabriqués par les équipementiers d'origine. Masse d'inertie, nombre de dents de couronne et
      surface de friction identiques à la pièce d'usine.
  - tier: Équivalent OE
    description: Fabricants aftermarket de confiance. Conformes aux spécifications constructeur, y compris pour les volants
      bimasse.
  - tier: Adaptable / Kit de conversion rigide
    description: Kits de conversion bimasse vers rigide. Moins cher et plus durable, mais génère davantage de vibrations et
      de bruit diesel. Vérifier la compatibilité boîte de vitesses.
diagnostic:
  symptoms:
  - id: S1
    label: Bruit de claquement ou cognement au ralenti
    severity: confort
  - id: S2
    label: Vibrations anormales transmises a l habitacle
    severity: confort
  - id: S3
    label: Craquement au demarrage ou a l arret du moteur
    severity: confort
  - id: S4
    label: Angulaire perceptible main volant depose
    severity: confort
  - id: S5
    label: Embrayage qui vibre ou accroche au demarrage
    severity: confort
  - id: S6
    label: Changement d embrayage prevu verifier le volant
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'vibrations anormales : verifier equilibrage et fixations'
  quick_checks:
  - Bruit de claquement ou cognement au ralenti ?
  - Vibrations anormales transmises a l habitacle ?
  - 'Observer : craquement au demarrage ou a l arret du moteur ?'
  - 'Observer : angulaire perceptible main volant depose ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Bruit de claquement ou cognement au ralenti
  - Vibrations anormales transmises a l habitacle
  - Craquement au demarrage ou a l arret du moteur
  - Angulaire perceptible main volant depose
  - Embrayage qui vibre ou accroche au demarrage
  - Changement d embrayage prevu verifier le volant
  good_practices:
  - Eviter de laisser le pied sur la pedale d embrayage au point mort
  - Remplacement du kit complet (disque + mecanisme + butee)
  - Purge du circuit hydraulique si recepteur/emetteur concerne
  - Verifier le volant moteur lors du remplacement d embrayage
rendering:
  pgId: '577'
  intro_title: A quoi sert Volant moteur ?
  risk_title: Pourquoi remplacer Volant moteur a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: 'Volant moteur OE ou OES : que choisir ?'
    answer: Les volants OES (Sachs, LuK, Valeo) sont de qualité équivalente. Pour un bimasse, privilégiez l'OE ou OES premium.
      Un volant rigide de conversion est une option économique.
  - question: Comment savoir si mon volant moteur est HS ?
    answer: Bruit de claquement au ralenti ou à l'accélération, vibrations transmises à l'habitacle, jeu angulaire excessif
      (test à la main), craquement au démarrage.
  - question: Faut-il changer le volant moteur avec l'embrayage ?
    answer: Pas systématiquement. Vérifier le jeu angulaire du bimasse (max 3-5° selon modèle). Si usé, le changer en même
      temps pour éviter une 2e intervention.
  - question: Peut-on remplacer un volant bimasse par un rigide ?
    answer: 'Oui, des kits de conversion existent. Avantages : moins cher, incassable. Inconvénients : plus de vibrations,
      bruit diesel accentué. Vérifier la compatibilité.'
  - question: Quelle erreur éviter avec le volant moteur ?
    answer: Ne pas réutiliser les vis de fixation (écrous autobloquants). Respecter le couple de serrage. Ne pas usiner un
      volant bimasse. Vérifier le joint spi vilebrequin.
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
doc_id: 2e13d929-bac9-55c6-b098-913f6db40e9a
content_hash: sha256:053dd07f22a644b3
lang: fr
variants:
- name: Kit embrayage complet
  aliases:
  - kit complet
  - 3 pieces
  functional_differences:
  - Disque + mecanisme + butee
  - Remplacement recommande en bloc
- name: Kit avec volant moteur
  aliases:
  - kit 4 pieces
  - kit + volant
  functional_differences:
  - Inclut le volant moteur bimasse
  - Pour vehicules diesel modernes
location_on_vehicle:
  area: Entre le moteur et la boite de vitesses
  access: Depose de la boite de vitesses necessaire (pont elevateur)
  adjacent_parts:
  - volant moteur
  - boite de vitesses
  - arbre primaire
installation:
  difficulty: difficile (pro recommande)
  time: 4h a 8h
  tools:
  - pont elevateur
  - cric de boite
  - centreur d embrayage
  - cle dynamometrique
  prerequisite: Depose complete de la boite de vitesses
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-04'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_133_kw: '133 kW'
    val_2_v: '2 v'
    val_6_kw: '6 kW'
    val_60_kw: '60 kW'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le volant moteur est lié au démarreur et à l'embrayage pour amortirles
    chocs, les vibrations et les bruits du moteur. Le volant moteur bi-
    masseéquipe la plupart des nouveaux modèlesdes véhicules,il comprend deux
    masses pour réduire les vibrations (la premièrefonctionne avec le
    vilebrequin et la deuxième avec la transmission) reliéesentre elles par un
    ressort, des taquets et un roulement à billes. En savoir plus : volant
    moteur — définition et rôle mécanique 🚨 Vibration volant moteur : identifier
    la cause
  S2: >-
    Unvolant moteur défaillant présente plusieurs symptômes : - Passagedifficile
    des vitesses. - Vibration lorsdu changement des rapports de vitesses. - A
    coups detransmission. - Claquements dumoteur. Un volant moteur défectueux et
    qu'il n'est pasremplacé à temps peut causer plusieurs problèmes : - Usure du
    kit d'embrayage . - Usure dudémarreur . - Usure duvilebrequin. - Usure de
    laboîte de vitesses. Diagnostic complet : identifier une panne de volant
    moteur
  S2_DIAG: >-
    SymptômeCause probableActionUn bruit anormal au niveau du volant moteur peut
    se manifester lors de la phase "acceleration"Pour identifier ce probleme de
    bruit du volant moteur:Verification visuelle du volant moteurDes vibrations
    provenant du volant moteur sont souvent perceptibles a haute vitessePour
    identifier ce probleme de vibration du volant moteur:Verification visuelle
    du volant moteur
  S3: >-
    Le volant moteur (ou volant bimasse sur les véhicules modernes) stocke
    l'énergie cinétique entre les impulsions de combustion et lisse les
    vibrations torsionnelles transmises à la boîte de vitesses. Sur les
    motorisations diesel post-2000, le volant bimasse remplace le volant
    monobloc traditionnel en intégrant des amortisseurs à ressorts hélicoïdaux —
    deux technologies radicalement différentes que l'on ne peut pas confondre
    lors du remplacement. - Volant monobloc ou bimasse — Le volant monobloc
    (fonte ou acier) est une pièce rigide adaptée aux moteurs essence et aux
    diesels jusqu'à fin des années 1990. Le volant bimasse (DMF — Dual Mass
    Flywheel) comporte deux masses reliées par des ressorts et est obligatoire
    sur les moteurs diesel à fort couple (à partir de 200 Nm). Ces deux versions
    ne sont pas interchangeables. - Diamètre extérieur et diamètre de centrage —
    Le diamètre de la couronne de démarrage (en contact avec le pignon du
    démarreur) et le diamètre d'appui du disque d'embrayage doivent correspondre
    à la millimètre. Un diamètre différent rend le démarrage impossible ou abîme
    le disque d'embrayage neuf. - Nombre de dents de la couronne de démarrage —
    La couronne de démarrage (souvent soudée sur le volant) comporte un nombre
    de dents précis (exemple : 124, 128 ou 132 dents) dimensionné pour le
    rapport de réduction du démarreur. Un nombre de dents erroné provoque un
    bruit de toc lors du démarrage et use le pignon de démarreur. - Référence
    bimasse et contrôle du jeu angulaire — Avant de commander un volant bimasse
    neuf, mesurez le jeu angulaire entre les deux masses sur l'ancien volant :
    un jeu supérieur à 25-30 mm (mesuré en périphérie) confirme la fin de vie.
    En dessous de ce seuil, un nettoyage peut suffire sur certaines
    configurations. - Kit complet volant + embrayage — Le volant bimasse se
    remplace systématiquement avec le kit embrayage complet (disque + mécanisme
    + butée). Les surfaces d'appui du mécanisme d'embrayage sont usinées pour le
    volant d'origine ; un nouveau mécanisme sur un vieux volant marqué peut
    provoquer une vibration résiduelle. - Couple de serrage des vis de fixation
    — Les vis de fixation du volant au vilebrequin sont serrées à un couple
    précis (généralement 60 à 100 Nm selon le moteur) avec une séquence
    angulaire spécifique. Utilisez des vis neuves à chaque montage ; certains
    constructeurs imposent des vis à usage unique pour ce point de serrage
    critique. Pour aller plus loin : consultez notre guide d'achat volant moteur
    — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Volant moteur pour
    connaître les spécifications. - Débranchez la batterie. - Levez et calez le
    véhicule. - Vidangez la boîte de vitesses. - Démontez la tringle de
    vitesses. - Démontez la commande d'embrayage. Note : la commande peut être
    mécanique par câble d'embrayage ou hydraulique suivant le niveau
    d'équipement du véhicule. Dans le montage hydraulique seulement le récepteur
    d'embrayage doit être démontez. - Démontez le démarreur . - Démontez les
    cardans. - Débranchez les capteurs de boîte de vitesse (capteur de feu de
    recule, capteur de vitesses, capteur point mort haut...). - Soutenez le
    moteur avec crique ou un palan ou une chèvre ou barre de fer et un crochet
    avant de démontez les supports de la boîte de vitesses. - Démontez les
    supports de la boîte de vitesse. - Démontez les fixations de la boîte de
    vitesses. - Immobilisez le volant moteur à l'aide d'un outil approprié. -
    Démontez les vis de fixation du kit d'embrayage sur le volant moteur. -
    Démontez le mécanisme d'embrayage et le disque d'embrayage. - Démontez
    l'outil de fixation du volant moteur. - Démontez le volant moteur.
  S4_REPOSE: >-
    Le remontage du volant moteur conditionne directement le comportement de
    l'embrayage et l'absence de vibrations en fonctionnement. Deux points
    critiques doivent être observés sans compromis : l'utilisation de vis de
    fixation neuves (les écrous ou vis autobloquants existants ne doivent jamais
    être réutilisés) et la vérification préalable du joint spi de vilebrequin,
    dont le remplacement est fortement conseillé dès lors que le volant est
    déposé. - Vérifiez que le volant moteur neuf est strictement identique à
    celui déposé : type (rigide ou bimasse), nombre de dents de la couronne de
    démarrage, position du marquage PMH (Point Mort Haut) et géométrie des trous
    de fixation. - Inspectez et remplacez si nécessaire le joint spi de
    vilebrequin arrière (côté volant) : c'est la seule occasion de le faire sans
    déposer à nouveau la boîte de vitesses. Un spi qui commence à suinter
    détruira l'embrayage par contamination d'huile. - Vérifiez l'état du kit
    d'embrayage (disque, mécanisme, butée) et remplacez-le systématiquement si
    son kilométrage est supérieur à 100 000 km. Combiner un volant neuf avec un
    embrayage usé oblige une deuxième intervention coûteuse à court terme. -
    Nettoyez le flasque de vilebrequin avec un solvant approprié. La surface de
    contact doit être parfaitement propre, sans trace d'huile, de griffe ou de
    corrosion. - Positionnez le volant moteur sur le vilebrequin en alignant les
    repères de calage (trou de détrompeur ou marquage PMH) avec les repères
    correspondants sur le flasque. Sur un volant bimasse, vérifiez que
    l'amortisseur rotatif n'est pas bloqué avant la mise en place. - Engagez les
    vis de fixation neuves à la main sans les serrer. Toutes les vis doivent
    entrer sans résistance : forcer une vis sur un filetage endommagé causera un
    desserrage en fonctionnement et une destruction du volant. - Immobilisez le
    volant avec l'outil de blocage approprié (outil de calage vilebrequin ou
    pige de blocage en denture). Serrez les vis dans un ordre en étoile au
    couple final prescrit par la revue technique (généralement 60 à 90 Nm selon
    le moteur, avec parfois un angle complémentaire de 30 à 60°). - Centrez le
    disque d'embrayage à l'aide d'un centreur d'embrayage avant de poser le
    mécanisme. Un disque mal centré rend impossible la rentrée de la boîte de
    vitesses et endommage les cannelures de l'arbre primaire. - Serrez les vis
    du mécanisme d'embrayage progressivement et dans l'ordre diagonal prescrit,
    jusqu'au couple final (typiquement 18 à 25 Nm). Retirez le centreur
    d'embrayage uniquement après le serrage complet. - Remontez la boîte de
    vitesses en la guidant sur l'arbre primaire sans forcer. Ne pas utiliser les
    vis de fixation pour tirer la boîte vers le moteur : l'arbre primaire doit
    entrer librement dans le disque d'embrayage. - Remontez dans l'ordre : les
    fixations de la boîte au moteur au couple prescrit, les supports de boîte,
    les cardans, le démarreur, la commande d'embrayage (câble ou récepteur
    hydraulique). - Faites l'appoint d'huile de boîte de vitesses avec le grade
    préconisé. Si le circuit d'embrayage est hydraulique, purgez-le jusqu'à
    obtenir une pédale ferme et sans jeu mort excessif. - Rebranchez la
    batterie, démarrez le moteur. Contrôlez le passage des rapports à froid puis
    à température de fonctionnement. Vérifiez l'absence de vibration au ralenti
    et à l'accélération, caractéristique d'un défaut de centrage ou d'un balourd
    de volant.
  S5: >-
    - ❌ "homologué CT - ❌ "sécurité garantie - ❌ "zéro panne - ❌ "garanti à vie
    - ❌ "embraye mieux
  S6: >-
    Le remplacement d'un volant moteur (bi-masse ou monobloc) est une opération
    majeure qui intervient souvent en même temps que le kit d'embrayage. Les
    vérifications post-montage visent à confirmer la disparition des bruits,
    l'absence de vibrations résiduelles et le correct accouplement entre le
    volant et le disque d'embrayage. - Contrôle du couple de serrage des vis de
    fixation du volant : les vis fixant le volant moteur au vilebrequin ont des
    couples précis (typiquement 60 à 100 Nm selon le moteur, parfois avec
    angulaire supplémentaire de +45° à +90°). Vérifier que toutes les vis ont
    été serrées en étoile en au moins 2 passes et que le frein-filet
    constructeur a été appliqué si requis. - Test de silence au ralenti moteur
    chaud : le bruit de claquement ou cognement au ralenti qui caractérisait le
    volant bi-masse usé doit avoir complètement disparu. Moteur à température
    normale (aiguille stabilisée) et ralenti entre 750 et 850 tr/min, écouter
    attentivement en conditions statiques fenêtres ouvertes. - Test de
    vibrations au volant de direction : conduire à 50 et 80 km/h en terrain plat
    — les vibrations anormales transmises au volant de direction qui signalaient
    un déséquilibre du volant moteur doivent avoir disparu. Une vibration
    résiduelle peut indiquer que le nouveau volant n'a pas été rebalancé avec
    son kit d'embrayage. - Contrôle de la douceur d'embrayage : effectuer une
    dizaine de démarrages en côte légère. La prise d'embrayage doit être
    progressive et sans accrochage ni vibration, confirmant que le disque
    d'embrayage s'engage correctement sur les tétons du volant neuf. - Absence
    de craquement au démarrage ou à l'arrêt du moteur : écouter attentivement
    lors de la coupure moteur — un volant bi-masse neuf ne doit produire aucun
    craquement sec lors de la décélération du vilebrequin jusqu'à l'arrêt
    complet. Un craquement persistant révèle un mauvais positionnement ou un
    montage du disque d'embrayage à l'envers. - Vérification de l'absence de
    fuite d'huile vilebrequin : après le premier trajet de 30 km, inspecter le
    carter embrayage par dessous. Toute trace d'huile neuve signale que le joint
    spi de vilebrequin (côté boîte) a été endommagé lors de la dépose du volant
    et doit être remplacé avant que l'huile ne contamine le disque d'embrayage
    neuf. - Test du capteur d'impulsion (PMH) : si le volant remplacé porte la
    couronne dentée utilisée par le capteur de position vilebrequin, connecter
    un outil OBD et vérifier l'absence de code P0335 (signal capteur PMH) qui
    indiquerait un jeu excessif ou un mauvais positionnement de la roue
    phonique.
  S7: >-
    Quel est le prix d'un volant moteur ?Le prix varie selon le véhicule et la
    marque. Utilisez notre sélecteur pour trouver le volant moteur compatible
    avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon volant moteur est à changer ?Les signes
    d'usure les plus courants sont détaillés dans la section diagnostic ci-
    dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un volant moteur défaillant ?Cela dépend
    de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité
    du véhicule. Consultez la section symptômes pour évaluer l'urgence du
    remplacement.- butee d embrayage - cable d embrayage - capteur impulsion -
    demarreur - emetteur d embrayage - kit d embrayage - recepteur d embrayage
  S8: >-
    Comment choisir Volant moteur compatible avec mon vehicule ?Renseignez
    marque, modele, type moteur et annee, puis verifiez la reference Quand
    remplacer Volant moteur ?En cas de bruit de claquement ou cognement au
    ralenti ou de degradation Puis-je monter Volant moteur sans verification
    atelier ?Le montage peut exiger controles de couple, alignement et
    references.
  META: >-
    Changer le volant moteur de la Citroën C4 I 1.6 HDI.
---

# Volant moteur - Guide Diagnostic Complet

## Fonction et Rôle

Lisser les vibrations du moteur, supporter le disque d'embrayage et transmettre l'inertie

**Actions principales:** lisser, supporter, transmettre l'inertie, amortir les à-coups, stocker l'énergie

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement ou cognement au ralenti**
  bruit de claquement ou cognement au ralenti

### 🟢 Autres Symptômes

- vibrations anormales transmises a l habitacle
- craquement au demarrage ou a l arret du moteur
- angulaire perceptible main volant depose
- embrayage qui vibre ou accroche au demarrage
- changement d embrayage prevu verifier le volant

## Procédure de Diagnostic

Pour diagnostiquer un problème de volant moteur:

1. **Inspection visuelle** - Examiner l'état du volant moteur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- butee-d-embrayage
- cable-d-embrayage
- capteur-impulsion
- demarreur
- emetteur-d-embrayage
- kit-d-embrayage
- recepteur-d-embrayage

## Critères de Compatibilité

Pour commander le bon volant moteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "embraye mieux"

## FAQ

**Volant moteur OE ou OES : que choisir ?**
Les volants OES (Sachs, LuK, Valeo) sont de qualité équivalente. Pour un bimasse, privilégiez l'OE ou OES premium. Un volant rigide de conversion est une option économique.

**Comment savoir si mon volant moteur est HS ?**
Bruit de claquement au ralenti ou à l'accélération, vibrations transmises à l'habitacle, jeu angulaire excessif (test à la main), craquement au démarrage.

**Faut-il changer le volant moteur avec l'embrayage ?**
Pas systématiquement. Vérifier le jeu angulaire du bimasse (max 3-5° selon modèle). Si usé, le changer en même temps pour éviter une 2e intervention.

**Peut-on remplacer un volant bimasse par un rigide ?**
Oui, des kits de conversion existent. Avantages : moins cher, incassable. Inconvénients : plus de vibrations, bruit diesel accentué. Vérifier la compatibilité.

**Quelle erreur éviter avec le volant moteur ?**
Ne pas réutiliser les vis de fixation (écrous autobloquants). Respecter le couple de serrage. Ne pas usiner un volant bimasse. Vérifier le joint spi vilebrequin.
