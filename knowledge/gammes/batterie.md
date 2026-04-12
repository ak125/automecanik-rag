---
category: electrique
slug: batterie
title: Batterie
pg_id: 1
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
business_priority: high
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Stocker et fournir l'energie electrique pour demarrer le moteur et alimenter les equipements du vehicule
  must_be_true:
  - stocker l'energie
  - fournir du courant
  - demarrer le moteur
  - alimenter les equipements
  must_not_contain:
  - recharger (role de l'alternateur)
  - produire de l'electricite
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: alternateur
    difference: La batterie stocke l'energie, l'alternateur la produit et recharge la batterie moteur tournant
  - term: demarreur
    difference: La batterie fournit le courant, le demarreur convertit ce courant en rotation mecanique pour lancer le moteur
  related_parts:
  - alternateur
  - demarreur
  - cosses-de-batterie
  - cables-de-batterie
  - coupe-circuit-batterie
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Tension nominale (12V pour vehicules legers, 24V pour poids lourds)
  - Capacite en Ah (amperes-heures) adaptee a la motorisation
  - Courant de demarrage a froid CCA (Cold Cranking Amps)
  - Technologie (SLI standard, EFB pour Start-Stop basique, AGM pour Start-Stop avance)
  - Dimensions et polarite (borne positive a droite ou a gauche)
  anti_mistakes:
  - universel
  - tous modeles
  - adaptable tous
  - pas cher
  - premier prix
  cost_range:
    min: 60
    max: 350
    currency: EUR
    unit: l'unite
    source: Bosch aftermarket 2026
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
    label: Demarrage lent ou laborieux surtout a froid
    severity: securite
  - id: S2
    label: Voyant batterie allume sur le tableau de bord
    severity: securite
  - id: S3
    label: Perte de memoire autoradio et horloge apres arret prolonge
    severity: confort
  - id: S4
    label: Phares et eclairage interieur faibles moteur eteint
    severity: confort
  - id: S5
    label: Batterie gonflée ou deformee (surcharge ou gel)
    severity: securite
  - id: S6
    label: Odeur de soufre ou d'oeuf pourri pres de la batterie
    severity: securite
  causes:
  - usure naturelle des plaques de plomb (4-5 ans en moyenne)
  - decharges profondes repetees (courts trajets, oubli phares)
  - alternateur defaillant ne rechargeant plus correctement
  - temperatures extremes (gel hivernal, canicule estivale)
  depose_steps:
  - Couper le contact et retirer la cle
  - Debrancher la borne negative (-) en premier
  - Debrancher la borne positive (+)
  - Retirer la fixation de maintien de la batterie
  - Extraire la batterie (attention au poids 15-25 kg)
  - Nettoyer le bac et les cosses si necessaire
  - Poser la batterie neuve, fixer le maintien
  - Rebrancher la borne positive (+) en premier puis la negative (-)
  quick_checks:
  - 'Observer : demarrage lent ou laborieux surtout a froid ?'
  - Voyant batterie allume sur le tableau de bord ?
  - 'Observer : perte de memoire autoradio et horloge apres arret prolonge ?'
  - 'Observer : phares et eclairage interieur faibles moteur eteint ?'
maintenance:
  interval:
    value: 4 a 5 ans
    unit: duree
    note: Verifier la tension avant chaque hiver (12.6V minimum au repos). Les batteries EFB/AGM peuvent durer 6-7 ans.
    source: Bosch aftermarket
  good_practices:
  - Verifier la tension au repos avec un multimetre (12.4V minimum)
  - Nettoyer les cosses si presence d'oxydation (sulfate blanc)
  - Eviter les decharges profondes repetees
  - Recharger avec un chargeur intelligent si vehicule immobilise plus de 3 semaines
  - Controler le bon serrage des cosses
  wear_signs:
  - Demarrage lent ou laborieux surtout a froid
  - Voyant batterie allume sur le tableau de bord
  - Perte de memoire autoradio et horloge apres arret prolonge
  - Phares et eclairage interieur faibles moteur eteint
  - Batterie gonflée ou deformee (surcharge ou gel)
  - Odeur de soufre ou d'oeuf pourri pres de la batterie
rendering:
  pgId: '1'
  intro_title: A quoi sert la batterie auto ?
  risk_title: Pourquoi remplacer la batterie a temps ?
  risk_explanation: '**Panne de demarrage** - Une batterie faible peut vous immobiliser sans prevenir'
  risk_consequences:
  - '**Panne de demarrage** - Immobilisation soudaine, surtout par temps froid'
  - '**Decharge profonde** - Endommage definitivement les plaques internes'
  - '**Surcharge** - Batterie gonflee = risque de fuite acide'
  risk_conclusion: Un controle preventif avant l'hiver evite la panne au pire moment.
  arguments:
  - content: Selection guidee par vehicule, Ah, CCA et technologie.
    icon: check-circle
    title: Compatibilite verifiee
  - content: Un remplacement preventif evite l'immobilisation.
    icon: shield-check
    title: Priorite securite
  - content: Le guide aide a choisir entre SLI, EFB et AGM.
    icon: clock
    title: Decision rapide
  - content: Verifier cosses et fixation reduit les retours.
    icon: list-check
    title: Montage maitrise
  faq:
  - question: Batterie OE ou adaptable, comment choisir ?
    answer: Privilegier une batterie de marque reconnue (Bosch, Varta, Exide) avec les memes Ah et CCA que l'origine. Les
      batteries AGM sont obligatoires pour les vehicules Start-Stop avances.
  - question: Comment savoir si ma batterie est HS ?
    answer: Tension au repos inferieure a 12.4V, demarrage lent, voyant batterie allume, perte des memoires electroniques
      apres une nuit. Un test de charge chez un professionnel confirme le diagnostic.
  - question: Tous les combien changer la batterie ?
    answer: En moyenne 4 a 5 ans pour une batterie SLI, 5 a 7 ans pour EFB/AGM. Verifier la tension avant chaque hiver et
      apres une periode d'immobilisation.
  - question: Peut-on changer la batterie soi-meme ?
    answer: 'Oui, operation simple (15-30 min). Toujours debrancher le negatif en premier et rebrancher le positif en premier.
      Attention : sur certains vehicules recents, un recalibrage calculateur est necessaire apres remplacement.'
  - question: Quelle erreur eviter avec la batterie ?
    answer: Ne jamais inverser les polarites (risque de court-circuit et destruction du calculateur). Ne pas monter une batterie
      SLI sur un vehicule Start-Stop (exige EFB ou AGM). Eviter les batteries sans marque ou sous-dimensionnees en CCA.
  quality:
    score: 76
    source: manual:claude-r3-kp
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modeles
  - adaptable tous
  requires_vehicle: true
doc_id: 5572827b-068e-5f80-bb39-6d7a4d2515ad
content_hash: sha256:5e8b7e6664e2584e
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
  _source: automotive.hutchinson.com + boschaftermarket.com + bremboparts.com + denso-am.eu + fr.wikipedia.org + hella.com + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 14
  _has_tech_data: true
  types_variants:
  - type: 'hall'
    source_ref: corpus RAG web OEM
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'Électrique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_0_1_mm: '0,1 mm'
    val_0_9_mm: '0,9 mm'
    val_000_v: '000 V'
    val_000__c: '000 °C'
    val_1_1_bar: '1,1 bar'
    val_1__v: '1. V'
    val_10_nm: '10 Nm'
    val_10_a: '10 a'
    val_10_5_v: '10,5 V'
    val_100_kw: '100 kW'
    val_11_93_v: '11,93 V'
    val_115_nm: '115 Nm'
    val_12_v: '12 V'
    val_12_a: '12 a'
    val_12_v: '12 v'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'La batterie fournie au démarreur l''énergie nécessaire, lors dudémarrage du véhicule. Après le démarrage du moteur
    et la mise en route duvéhicule, c''est l''alternateur qui fournit l''énergie électrique et rechargela batterie. La batterie
    stock l''énergie électrique nécessaire pour le véhicule (pour ledémarrage et pour les équipements électriques).La recharge
    de la batterie se fait de façon continue dès le démarrage duvéhicule. L''alternateur et la batterie sont des éléments
    dépendants l''une de l''autre ettrès essentiel pour le véhicule. Si l''alternateur ne fonctionne pas la batterieva se
    décharger rapidement. En savoir plus : batterie — définition et rôle mécanique 🚨 Bruit Batterie : causes et diagnostic'
  S2: 'Une batterie défaillante présente plusieurs symptômes : - Témoin de la batterie s''allume sur le tableau de bord. -
    Le véhicule prend du temps pour démarrer. - Manque de luminosité à l''intérieur ou à l''extérieur duvéhicule. Diagnostic
    complet : identifier une panne de batterie'
  S3: 'Choisir une batterie adaptée à votre véhicule exige de respecter plusieurs paramètres techniques précis. Une capacité
    ou un courant de démarrage inadapté peut provoquer des pannes de démarrage dès les premières semaines. - Type de technologie
    : batterie plomb-acide standard pour les véhicules sans système Stop&Start, batterie AGM (Absorbent Glass Mat) obligatoire
    pour les véhicules équipés de Stop&Start intensif — durée de vie 5 à 7 ans contre 4 à 5 ans pour une standard. La batterie
    EFB (Enhanced Flooded Battery) convient aux Stop&Start d''entrée de gamme. - Capacité en Ah : ne jamais descendre sous
    la valeur d''origine. Repères indicatifs : 40-50 Ah pour une citadine essence, 50-60 Ah pour une compacte essence, 60-70
    Ah pour un diesel standard, 70-95 Ah pour un diesel puissant ou avec nombreux équipements. - Courant de démarrage CCA
    (A) : mesuré à -18°C selon norme EN. La valeur CCA doit être au minimum égale à celle préconisée par le constructeur —
    ne jamais utiliser une valeur inférieure. - Dimensions exactes : longueur, largeur et hauteur au millimètre près. Un boîtier
    trop grand ne rentrera pas ; trop petit, la batterie se déplacera et les cosses vibrent jusqu''à rupture. - Position des
    bornes : vérifier la polarité gauche ou droite (borne + à gauche ou à droite selon le sens de câblage du compartiment
    moteur). Une inversion impose des modifications de câblage coûteuses. - Référence OEM ou équivalent homologué : comparer
    la référence d''origine constructeur avec l''EAN du produit. Les batteries dites « universelles » ou « tous modèles »
    sont à proscrire. - Marque et certification : privilégier des fabricants avec certification ISO, standards EN 50342 pour
    batteries de démarrage. Les marques Varta, Bosch, Exide sont des références OEM européennes reconnues.'
  S4_DEPOSE: '📖 Avant de démonter, consultez la fiche technique Batterie pour connaître les spécifications. Attention : la
    couleur rouge est pour la borne positive et la couleur noir pour la bornenégative. - Débranchez la borne négative de labatterie.
    - Débranchez la borne positive de labatterie. - Déposez la batterie.'
  S4_REPOSE: '- Mettre en place la batterie. - Rebranchez la borne positive de labatterie puis la borne négative. Attention
    :Faites attention à ne pas inverser les cosses de la batterie. - Remettez les composants électriques à zéro (radio,indicateur
    de maintenance, horloge ..). - Faire un test diagnostic pour tous les composants duvéhicule. ✅ Après remontage, vérifiez
    les spécifications dans la fiche technique Batterie.'
  S5: 'Plusieurs erreurs fréquentes lors du remplacement d''une batterie peuvent endommager l''électronique du véhicule, court-circuiter
    le réseau de bord ou accélérer la dégradation de la nouvelle pièce. - Inverser les polarités à la pose : connecter la
    borne négative avant la borne positive crée un arc électrique qui peut griller les fusibles principaux, détériorer le
    calculateur moteur ou endommager l''alternateur en quelques secondes. - Déconnecter la batterie sans sauvegarder les mémoires
    : sur les véhicules modernes, retirer la batterie efface les paramètres d''adaptation du moteur (valeurs de ralenti, corrections
    injecteurs), les codes radio et les réglages de vitres électriques. Utiliser un alimentateur de maintien 12 V avant la
    dépose. - Monter une batterie sous-dimensionnée en CCA : un courant de démarrage insuffisant ne détruit pas immédiatement
    la batterie, mais le démarreur compense en tirant plus d''intensité, ce qui chauffe ses bobinages et réduit sa durée de
    vie de 30 à 50 %. - Poser une batterie standard sur un véhicule Stop&Start : les cycles répétés de charge/décharge d''un
    Stop&Start (jusqu''à 500 000 microcycles sur la durée de vie) détruisent une batterie plomb-acide classique en moins de
    18 mois. - Ne pas nettoyer les cosses avant la repose : les dépôts blancs ou bleus (sulfate de plomb, oxyde de cuivre)
    sur les bornes créent une résistance parasite. Une résistance de 0,05 Ω suffit à faire chuter la tension de démarrage
    de 0,6 V, ce qui peut empêcher le démarrage par grand froid. - Recycler l''ancienne batterie dans les ordures ménagères
    : les batteries au plomb-acide contiennent du plomb et de l''acide sulfurique. Le dépôt en déchetterie agréée est obligatoire
    en France sous peine d''amende.'
  S6: 'Après la pose d''une batterie neuve, plusieurs contrôles techniques permettent de confirmer que l''installation est
    correcte et que le système de charge fonctionne normalement. - Tension au repos : mesurer avec un multimètre entre les
    deux bornes, moteur coupé depuis 30 minutes. La valeur doit être comprise entre 12,4 V et 12,8 V. En dessous de 12,2 V,
    la batterie est partiellement déchargée ou défectueuse. - Tension en charge (moteur tournant) : mesurer entre les bornes,
    moteur au ralenti. La tension doit se situer entre 13,5 V et 14,5 V, confirmant que l''alternateur charge correctement.
    Une valeur inférieure à 13 V indique une défaillance de l''alternateur ou de son régulateur. - Serrage des cosses : vérifier
    que les cosses sont bien serrées à la main, sans jeu possible. Un couple de serrage de 4 à 6 N·m est généralement préconisé
    selon le type de borne. Une cosse mal serrée provoque des chutes de tension intermittentes difficiles à diagnostiquer.
    - Absence de codes défaut OBD : brancher un outil de diagnostic et vérifier l''absence de DTC (Diagnostic Trouble Codes)
    liés au réseau de bord, au calculateur moteur ou à l''alternateur. Le remplacement de batterie peut déclencher un P0620
    ou P0563 sur certains véhicules. - Réinitialisation du gestionnaire d''énergie : sur les véhicules BMW, Audi, Mercedes
    ou Renault récents, coder la nouvelle batterie via l''outil de diagnostic constructeur pour que le gestionnaire d''énergie
    adapte ses seuils de charge au cycle de vie réel de la batterie neuve. - Test de charge sous charge : activer phares,
    ventilation plein régime, et lunette arrière dégivrante simultanément. La tension ne doit pas descendre sous 13,2 V, confirmant
    la capacité de l''alternateur à compenser les consommateurs. - Contrôle visuel des connexions : vérifier l''absence de
    câbles en contact avec des pièces chaudes (collecteur, turbo), de pincements ou de frottements sur l''arête de la tôle
    du compartiment moteur.'
  S7: 'La batterie ne fonctionne pas de façon isolée : elle alimente et est rechargée par un ensemble de composants électriques
    interdépendants. Remplacer uniquement la batterie sans contrôler ces pièces conduit souvent à une panne répétée à court
    terme. - Alternateur — La batterie et l''alternateur forment un système de charge solidaire. Un alternateur défaillant
    délivre moins de 13,8 V à régime stabilisé et épuise prématurément toute batterie neuve en quelques semaines. Mesurer
    la tension aux bornes moteur tournant : entre 13,8 V et 14,5 V confirme un alternateur sain. Une valeur inférieure à 13,5
    V ou supérieure à 15 V impose le remplacement de l''alternateur avant ou simultanément à la batterie. - Démarreur — Un
    démarreur en fin de vie tire des pointes de courant anormalement élevées (jusqu''à 300 A sur certains moteurs) qui abîment
    les plaques de la batterie à chaque démarrage. Si les démarrages sont lents, laborieux ou accompagnés d''un bruit de cliquetis
    du démarreur, faire tester la consommation de courant du démarreur (starter test) avant de conclure à une batterie seule.
    - Courroie d''accessoire — La courroie d''accessoire entraîne l''alternateur. Une courroie glissante, trop lâche ou en
    fin de vie réduit la tension de charge transmise à l''alternateur et génère les mêmes symptômes qu''une batterie faible.
    Contrôler la tension et l''état de la courroie (craquelures, effilochage) à chaque intervention sur le circuit de charge.
    - Boîtier de fusibles et relais principaux — Un mauvais contact sur le fusible principal ou le relais de batterie provoque
    des chutes de tension identiques à une batterie défaillante. Inspecter les cosses de batterie (oxydation, sulfatation),
    les câbles de masse du moteur et de carrosserie, et les fusibles de puissance lors de chaque remplacement de batterie.
    Un câble de masse corrodé peut faire chuter la tension de 0,5 V et suffire à empêcher un démarrage. - Capteur de température
    moteur — Sur les véhicules équipés du système Start-Stop, le calculateur de gestion de batterie pilote la charge en fonction
    de la température moteur. Un capteur défectueux induit une gestion incorrecte : la batterie est sollicitée à chaque cycle
    de coupure moteur sans être rechargée au niveau optimal. Ce scénario réduit la durée de vie d''une batterie AGM à moins
    de 2 ans. - Capteur de gestion de batterie (BSM/IBS) — Sur de nombreux véhicules récents, un capteur de gestion de batterie
    (Battery Management Sensor) est fixé sur la borne négative. Ce capteur mesure en temps réel la tension, le courant et
    la température de la batterie pour informer le calculateur. Lors d''un remplacement de batterie, ce capteur doit être
    initialisé via un outil de diagnostic constructeur : sans cette étape, le système de charge reste calé sur les paramètres
    de l''ancienne batterie. Vérifier également que les bornes de la batterie neuve sont serrées au couple recommandé (généralement
    4 à 6 Nm) et que les couvercles protecteurs sont remis en place. Une borne desserrée provoque des arcs électriques qui
    brûlent les fils et peuvent endommager le calculateur moteur.'
  S8: 'Quelle est la durée de vie d''une batterie auto ? Une batterie plomb-acide standard dure en moyenne 4 à 5 ans. Une
    batterie AGM (pour véhicules Stop&Start) tient 5 à 7 ans. La durée réelle varie selon le climat (le froid accélère la
    décharge), la fréquence des trajets courts qui ne permettent pas une recharge complète, et la qualité des connexions.
    Une batterie qui ne démarre plus de façon fiable après 4 ans doit être testée avec un testeur de charge avant de conclure
    à son remplacement. Comment savoir si c''est la batterie ou l''alternateur qui est défaillant ? La distinction se fait
    au multimètre. Moteur coupé, la tension aux bornes inférieure à 12,2 V pointe vers une batterie déchargée ou usée. Moteur
    tournant, une tension inférieure à 13,5 V indique que l''alternateur ne charge pas. Si la batterie se décharge sans raison
    apparente malgré un alternateur sain, une fuite de courant (consommateur parasite) est probable : mesurer le courant de
    repos doit donner moins de 50 mA, portes et capot fermés pendant 15 minutes. Peut-on remplacer soi-même sa batterie de
    voiture ? Le remplacement est accessible sur la plupart des véhicules. Les conditions sont : disposer d''un alimentateur
    de maintien 12 V pour préserver les mémoires électroniques, respecter l''ordre de déconnexion (masse en premier à la dépose,
    masse en dernier à la pose), et vérifier la compatibilité dimensionnelle et technique exacte. Sur les véhicules récents
    avec gestion d''énergie intelligente (BMW, Audi, Mercedes, Renault Megane IV+), un codage via outil de diagnostic constructeur
    est nécessaire après la pose. Pourquoi ma batterie neuve se décharge rapidement ? Trois causes principales : une fuite
    de courant (consommateur parasite non coupé à l''arrêt du moteur), un alternateur défaillant qui ne recharge pas, ou des
    trajets trop courts et trop fréquents (moins de 10 km) qui ne permettent pas de recharger complètement la batterie. En
    hiver, une batterie de 55 Ah correcte peut nécessiter 45 minutes de roulage à régime stabilisé pour se recharger après
    un démarrage à froid. Quelle différence entre CCA, CA et RC sur une batterie ? Le CCA (Cold Cranking Amperes) mesure le
    courant disponible pendant 30 secondes à -18°C — c''est le critère de démarrage par grand froid. Le CA (Cranking Amperes)
    est mesuré à 0°C et donne une valeur plus élevée que le CCA. Le RC (Reserve Capacity) mesure en minutes la durée pendant
    laquelle une batterie chargée peut alimenter les équipements essentiels si l''alternateur tombe en panne. Pour le choix
    d''une batterie de remplacement, le CCA et la capacité en Ah sont les critères prioritaires.'
---

# Batterie - Guide Diagnostic Complet

## Fonction et Role

Stocker et fournir l'energie electrique pour demarrer le moteur et alimenter les equipements du vehicule a l'arret et au demarrage.

**Actions principales:** stocker l'energie, fournir du courant, demarrer le moteur, alimenter les equipements, maintenir la tension

## Symptomes de Defaillance

### 🔴 Symptomes Securite

- Demarrage lent ou laborieux surtout a froid
- Voyant batterie allume sur le tableau de bord
- Batterie gonflee ou deformee (surcharge ou gel)
- Odeur de soufre ou d'oeuf pourri pres de la batterie

### 🟢 Autres Symptomes

- Perte de memoire autoradio et horloge apres arret prolonge
- Phares et eclairage interieur faibles moteur eteint

## Procedure de Diagnostic

Pour diagnostiquer un probleme de batterie:

1. **Mesure de tension au repos** - Multimetre sur les bornes, moteur eteint (12.6V = 100%, 12.4V = 75%, 12.2V = 50%)
2. **Test de charge** - Tension moteur tournant entre 13.5V et 14.5V (alternateur OK)
3. **Inspection visuelle** - Verifier gonflement, fissures, oxydation cosses, niveau electrolyte si accessible
4. **Test de demarrage** - Tension ne doit pas descendre sous 10V au demarrage


## Entretien et Intervalles

- **Intervalle** : 4 a 5 ans
- Verifier la tension avant chaque hiver (12.6V minimum au repos). Les batteries EFB/AGM peuvent durer 6-7 ans.

## Causes Probables

- **Usure naturelle** - Degradation des plaques de plomb apres 4-5 ans
- **Decharges profondes** - Courts trajets repetes, oubli phares ou equipements
- **Alternateur defaillant** - Ne recharge plus correctement la batterie
- **Temperatures extremes** - Gel hivernal ou canicule estivale accelerent le vieillissement

## Pieces Associees

Lors du remplacement, verifier egalement:

- alternateur
- demarreur
- cosses-de-batterie
- cables-de-batterie
- coupe-circuit-batterie

## Ne Pas Confondre Avec

### alternateur
**Distinction:** La batterie stocke l'energie electrique, l'alternateur la produit et recharge la batterie moteur tournant

### demarreur
**Distinction:** La batterie fournit le courant electrique, le demarreur le convertit en rotation mecanique pour lancer le moteur

## Criteres de Compatibilite

Pour commander la bonne batterie, vous devez connaitre:

- **Marque** de votre vehicule
- **Modele** de votre vehicule
- **Motorisation** de votre vehicule
- **Annee** de votre vehicule
- **Tension** nominale (12V ou 24V)
- **Capacite** en Ah (amperes-heures)
- **CCA** courant de demarrage a froid
- **Technologie** SLI, EFB ou AGM selon equipement Start-Stop
- **Dimensions et polarite** de la borne positive

## Attention aux Fausses Promesses

Mefiez-vous des vendeurs qui utilisent ces termes interdits:

- "universel"
- "tous modeles"
- "adaptable tous"
- "pas cher"
- "premier prix"

## FAQ

**Batterie OE ou adaptable, comment choisir ?**
Privilegier une batterie de marque reconnue (Bosch, Varta, Exide) avec les memes Ah et CCA que l'origine. Les batteries AGM sont obligatoires pour les vehicules Start-Stop avances.

**Comment savoir si ma batterie est HS ?**
Tension au repos inferieure a 12.4V, demarrage lent, voyant batterie allume, perte des memoires electroniques apres une nuit. Un test de charge chez un professionnel confirme le diagnostic.

**Tous les combien changer la batterie ?**
En moyenne 4 a 5 ans pour une batterie SLI, 5 a 7 ans pour EFB/AGM. Verifier la tension avant chaque hiver et apres une periode d'immobilisation.

**Peut-on changer la batterie soi-meme ?**
Oui, operation simple (15-30 min). Toujours debrancher le negatif en premier et rebrancher le positif en premier. Attention : sur certains vehicules recents, un recalibrage calculateur est necessaire apres remplacement.

**Quelle erreur eviter avec la batterie ?**
Ne jamais inverser les polarites (risque de court-circuit et destruction du calculateur). Ne pas monter une batterie SLI sur un vehicule Start-Stop (exige EFB ou AGM). Eviter les batteries sans marque ou sous-dimensionnees en CCA.
