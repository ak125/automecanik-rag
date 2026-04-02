---
category: moteur
slug: capteur-vilebrequin
title: Capteur vilebrequin
pg_id: 833
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
  last_enriched_by: skill:phase5-hella-ngk
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Mesurer la vitesse de rotation et la position du vilebrequin pour le calculateur moteur
  must_be_true:
  - mesurer la position
  - vitesse de rotation
  - signal au calculateur
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: capteur-d-arbre-a-cames
    difference: Le capteur vilebrequin mesure la rotation du vilebrequin (bas moteur), le capteur arbre a cames mesure la
      position des cames (haut moteur)
  - term: capteur-impulsion
    difference: Le capteur d'impulsion est un terme generique, le capteur vilebrequin est specifique a la position du vilebrequin
  related_parts:
  - capteur-d-arbre-a-cames
  - bobine-d-allumage
  - courroie-de-distribution
  - volant-moteur
selection:
  criteria:
  - Marque de votre vehicule
  - Modele de votre vehicule
  - Motorisation de votre vehicule
  - Annee de votre vehicule
  - Type de capteur (inductif ou a effet Hall)
  - Nombre de broches du connecteur
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
    label: Moteur ne demarre pas (pas de signal de rotation)
    severity: securite
  - id: S2
    label: Calages aleatoires en roulant
    severity: securite
  - id: S3
    label: Perte de puissance intermittente
    severity: confort
  - id: S4
    label: Voyant moteur allume (codes P0335, P0336, P0337)
    severity: confort
  - id: S5
    label: Rates d'allumage ou tremblements moteur
    severity: confort
  - id: S6
    label: Demarrage long ou difficile a chaud
    severity: confort
  causes:
  - entrefer trop grand entre capteur et couronne dentee du volant moteur
  - fil de signal coupe ou connecteur oxyde
  - aimant du capteur desaimante par la chaleur
  quick_checks:
  - 'Observer : moteur ne demarre pas (pas de signal de rotation) ?'
  - 'Observer : calages aleatoires en roulant ?'
  - 'Observer : perte de puissance intermittente ?'
  - Voyant moteur allume (codes P0335, P0336, P0337) ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Pas de periodicite fixe. Remplacer en cas de codes defaut P0335/P0336 confirmes.
  wear_signs:
  - Moteur ne demarre pas (pas de signal de rotation)
  - Calages aleatoires en roulant
  - Perte de puissance intermittente
  - Voyant moteur allume (codes P0335, P0336, P0337)
  - Rates d'allumage ou tremblements moteur
  - Demarrage long ou difficile a chaud
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '833'
  faq:
  - question: Comment tester le capteur vilebrequin ?
    answer: Mesurer la resistance (200-1000 ohms pour inductif). Scanner OBD pour codes P0335/P0336. Verifier le signal avec
      un oscilloscope si disponible.
  - question: Capteur vilebrequin OE ou adaptable ?
    answer: Privilegier OE ou OES (Bosch, Hella, Continental). Les generiques peuvent avoir un signal trop faible.
  - question: Peut-on rouler sans capteur vilebrequin ?
    answer: Non, le calculateur ne peut pas gerer injection ni allumage sans ce signal. Le moteur cale ou ne demarre pas.
  - question: Tous les combien changer le capteur vilebrequin ?
    answer: Pas de periodicite fixe. Duree de vie generalement superieure a 200000 km sauf defaut electrique.
  - question: Quelle erreur eviter ?
    answer: Ne pas forcer le capteur dans son logement. Respecter l'entrefer. Ne pas confondre avec le capteur d'arbre a cames.
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
doc_id: 39efa841-a6c8-5725-8f8d-16b93552f839
content_hash: sha256:193aec1b4907e18b
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
  _source: HELLA TechWorld + NGK/NTK
  _validation_status: oem_verified
  _enriched_at: '2026-03-29'
  types_variants:
  - type: Capteur inductif (2 broches)
    description: Signal sinusoidal, pas d'alimentation externe, resistance 200-1000 ohms
    era: standard
  - type: Capteur a effet Hall (3 broches)
    description: Signal rectangulaire, necessite alimentation 5V du calculateur
    era: vehicules recents
  technical_notes:
    resistance_inductif: '200 - 1000 ohms'
    isolement_masse: '> 30 Mohms (infini attendu)'
    signal_inductif: 'sinusoidal, amplitude proportionnelle au regime'
    signal_hall: 'rectangulaire, amplitude constante'
  glossary:
  - terme: PMH
    definition: Point Mort Haut — position du piston au sommet de sa course, reference pour le calage allumage/injection
  - terme: roue dentee relucteur
    definition: Couronne a dents sur le vilebrequin/volant moteur, avec 1 ou 2 dents manquantes pour le repere PMH
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le capteurde vilebrequin possède un double rôle dans le moteur, il permet
    deconnaitre la position du vilebrequin ainsi que sa vitesse. Ces
    informationssont envoyées au calculateur moteur pour qu'il puisse savoir
    combien et quandil injecte du carburant. Le capteurde vilebrequin est une
    sorte d'une bobine qui intègre un noyau magnétique (aimant). Labobine est
    reliée à ces deux extrémités par 2 fils électriques qui sont reliésau
    calculateur. Le capteur est fixé sur le volant moteur qui possède 60
    dentsmoins 2 manquantes consécutives. Le capteur de vilebrequin étant
    sensible au magnétisme, il détecte les espacesdes dents manquantes ce qui
    correspondentau point mort haut du 1er cylindres et du 4éme cylindre. Il
    existe 2 types de capteur de vilebrequin : - Capteur de vilebrequin actif
    avec effet hall : il est le plusutilisé parce qu'il plus précis que l'ancien
    capteur inductif. Il doit êtrealimenté électriquement et il envoie un signal
    de 5 volts au calculateur moteurà chaque contact avec une des dents du
    volant moteur. Il est équipé d'unepetite carte électronique qui s'occupe de
    la communication avec le calculateur. - Capteur de vilebrequin passif avec
    effet inductif : il est moinsutilisé et il est remplacé par le capteur à
    effet hall. Il n'a pas besoind'être alimenter par du courant le mouvement du
    volant moteur à proximité ducapteur va induire du courant alternatif. Le
    contrôle du capteur inductif cefait sans l'outil diagnostic.
  S2: >-
    Un capteur de vilebrequindéfaillant présente plusieurs symptômes : - Des
    ratés du moteur. - Démarrage difficile dumoteur. - Le moteur ne démarre pas.
    - Lors d'un test diagnosticvous constatez l'enregistrement d'un code de
    défaut dans le calculateur moteur.
  S3: >-
    Le capteur de position vilebrequin (CKP sensor) est une pièce dont la
    compatibilité exacte conditionne le bon fonctionnement de la gestion moteur.
    Voici les critères déterminants pour faire le bon choix. - Type de
    technologie : vérifiez si votre moteur attend un capteur inductif (passif)
    ou un capteur à effet Hall (actif). Ces deux technologies ne sont pas
    interchangeables. Un capteur inductif génère sa propre tension alternative,
    un capteur à effet Hall nécessite une alimentation et délivre un signal
    numérique carré. La confusion entraîne une absence de signal au calculateur.
    - Référence OEM ou équivalence certifiée : recherchez la référence
    constructeur inscrite sur le capteur d'origine. Une équivalence aftermarket
    est acceptable à condition que le fabricant fournisse une table de
    correspondance avec la référence OEM (Bosch, Delphi, Vemo, Hella). - Nombre
    de fils du connecteur : 2 fils pour un capteur inductif, 3 fils pour un
    capteur à effet Hall. Le connecteur doit correspondre exactement à la prise
    du faisceau existant. Un adaptateur n'est jamais acceptable sur un circuit
    capteur moteur. - Longueur du câble et orientation du connecteur : vérifiez
    la longueur du câble et le sens de sortie du connecteur (vers le haut, à
    90°) pour éviter toute tension sur le faisceau après montage dans l'espace
    contraint du bloc moteur. - Entrefer (air gap) requis : certains capteurs
    inductifs nécessitent un réglage précis de l'entrefer entre la tête du
    capteur et la cible dentée, généralement entre 0,5 et 1,5 mm selon les
    données constructeur. Vérifiez si la pièce intègre une cale calibrée ou si
    le réglage est manuel. - Résistance thermique du boîtier : le capteur est
    exposé aux températures élevées du bloc moteur. Exigez un indice
    d'étanchéité IP67 minimum et un boîtier en polyamide haute température ou en
    métal pour résister aux projections d'huile et aux fluides. - Certification
    et rang d'équipementier : pour un véhicule sous garantie, choisissez une
    pièce d'origine ou un équipementier de rang 1. Pour les véhicules anciens,
    un fabricant aftermarket reconnu au catalogue Autodoc, TecDoc ou Febi-
    Bilstein offre un niveau de fiabilité suffisant.
  S4_DEPOSE: >-
    - Débranchez la batterie. - Localisez l'emplacement du capteur vilebrequin.
    - Démontez si nécessaire des pièces pour faciliter l'accès au capteur
    vilebrequin (par exemple jauge d'huile). - Débranchez le connecteur du
    capteur vilebrequin. - Desserrez la vis de fixation du capteur vilebrequin.
    - Démontez le capteur vilebrequin.
  S4_REPOSE: >-
    - Vérifiez que le capteur vilebrequin neuf est identique à celui démonté. -
    Contrôlez l'état de fonctionnement des injecteurs. - Contrôlez l'état de
    fonctionnement de la pompe injection. - Nettoyez le logement du capteur
    vilebrequin. - Mettre en place le capteur vilebrequin. - Serrez la vis de
    fixation du capteur vilebrequin. - Branchez le connecteur du capteur
    vilebrequin. - Remontez les pièces démontées pour faciliter l'accès au
    capteur vilebrequin. - Rebranchez la batterie. - Branchez l'outil
    diagnostic. - Démarrez le moteur pour contrôler l'état de fonctionnement du
    capteur vilebrequin.
  S5: >-
    Le remplacement d'un capteur vilebrequin est une opération en apparence
    simple, mais plusieurs erreurs fréquentes conduisent à des pannes
    récurrentes ou à un non-démarrage après intervention. Voici les cinq pièges
    les plus courants à écarter. - Confondre capteur inductif et capteur à effet
    Hall : brancher un capteur inductif à la place d'un capteur à effet Hall (ou
    inversement) génère immédiatement un code défaut P0335 et un non-démarrage.
    Identifiez toujours la technologie d'origine avant commande : 2 fils =
    inductif, 3 fils = effet Hall avec alimentation 5 V ou 12 V. - Ne pas
    nettoyer le logement avant la pose : de la rouille, des résidus de joint ou
    des débris métalliques dans le logement du capteur faussent l'entrefer et
    perturbent la lecture du signal. Nettoyez systématiquement le logement au
    chiffon non pelucheux et vérifiez l'absence de dépôt sur la roue phonique
    (cible dentée). - Serrer le capteur à la main sans vérifier le couple : le
    couple de serrage du capteur vilebrequin est spécifié par le constructeur,
    généralement entre 5 et 10 N.m. Un sous-serrage provoque des vibrations et
    un signal instable ; un sur-serrage fissure le boîtier plastique. Utilisez
    une clé dynamométrique. - Ne pas effacer les codes défauts après
    remplacement : même avec le nouveau capteur correctement installé, le
    calculateur conserve en mémoire les codes P0335 à P0339 et peut maintenir le
    voyant moteur allumé. Effacez systématiquement la mémoire du calculateur
    avec un scanner OBD2 après la pose. - Tirer ou plier le câble pour le
    connecter : le câble du capteur est court et passe souvent près de pièces
    chaudes. Forcer la connexion en tirant sur le faisceau existant endommage
    les cosses du connecteur ou crée un point de rupture futur. Suivez le chemin
    de câblage d'origine et fixez le câble avec les colliers de maintien prévus
    à cet effet.
  S6: >-
    Une fois le capteur vilebrequin posé, une séquence de vérifications
    structurée permet de confirmer le bon fonctionnement avant de rendre le
    véhicule à la circulation. - Effacement de la mémoire défauts : branchez un
    scanner OBD2, effacez tous les codes défauts (notamment P0335, P0336, P0337,
    P0338, P0339) et vérifiez qu'aucun code ne revient après le démarrage. -
    Démarrage à froid et observation du régime : démarrez le moteur à froid et
    observez la stabilité du régime au ralenti (normalement 650 à 850 tr/min
    selon le moteur). Un régime instable, des ratés ou un calage immédiat
    indiquent un problème de signal résiduel. - Lecture en temps réel du signal
    RPM : avec le scanner OBD2 en mode données live, vérifiez que la valeur RPM
    du calculateur est cohérente avec le régime réel du moteur et qu'elle monte
    de façon progressive sans à-coups lors des accélérations. - Test de montée
    en régime : accélérez progressivement jusqu'à 3 000 tr/min en mode statique.
    Le régime doit monter et descendre sans coupures, sans à-coups ni trous de
    puissance. Tout comportement erratique nécessite un nouveau contrôle de
    l'entrefer ou du faisceau. - Vérification visuelle du câblage et des
    fixations : contrôlez visuellement que le câble du capteur n'est pas coincé
    par un autre organe, qu'il n'est pas en contact avec le collecteur
    d'échappement, et que les colliers de fixation sont en place. - Contrôle de
    l'étanchéité du logement : inspectez le joint d'étanchéité du capteur (joint
    torique ou joint papier) pour s'assurer qu'il n'y a pas de fuite d'huile au
    niveau du logement dans le bloc moteur. Une fuite à cet endroit endommagera
    le connecteur à terme. - Essai routier de 10 à 15 km : réalisez un essai
    incluant phases urbaines et accélérations soutenues. À l'issue du trajet,
    reconnectez le scanner pour confirmer l'absence de nouveaux codes défauts en
    mémoire.
  S7: >-
    - Capteur d'arbre à cames — Le capteur vilebrequin et le capteur d'arbre à
    cames travaillent en tandem pour synchroniser l'injection et l'allumage. Un
    défaut sur l'un provoque souvent une panne diagnostique similaire sur
    l'autre (codes P0340/P0335) ; tester les deux avant de conclure à un
    remplacement unique. - Poulie vilebrequin / roue phonique — Le capteur lit
    les dents de la roue phonique montée sur la poulie vilebrequin. Une dent
    arrachée ou une roue phonique oxydée génère des signaux parasites identiques
    à un capteur défaillant. Inspecter la roue phonique à chaque remplacement du
    capteur. - Volant moteur — Certaines architectures positionnent la roue
    phonique sur le volant moteur. Des dents abîmées sur le volant rendent le
    remplacement du capteur seul inefficace ; vérifier l'état du volant lors du
    diagnostic par lecture OBD. - Capteur de cognement — Monté à proximité sur
    le bloc moteur, le capteur de cognement partage le câblage moteur et peut
    être confondu lors du diagnostic. Un code P0325 associé à un P0335 oriente
    vers une vérification simultanée des deux capteurs. - Joint spy vilebrequin
    — L'accès au capteur vilebrequin nécessite souvent de déposer des pièces
    proches du joint d'étanchéité avant du vilebrequin. Profiter de
    l'intervention pour contrôler l'état du joint spy et le remplacer
    préventivement s'il suinte.
  S8: >-
    Quels sont les symptômes d'un capteur vilebrequin défaillant ? Les symptômes
    les plus courants sont : un moteur qui cale sans raison au ralenti ou en
    roulant, des ratés d'allumage ressentis comme des à-coups, un voyant moteur
    allumé avec les codes défauts P0335 à P0339, un démarrage difficile ou un
    non-démarrage total, et une consommation de carburant anormalement élevée.
    Ces signes peuvent apparaître de façon intermittente au début, notamment par
    temps chaud lorsque le capteur est en limite de fonctionnement thermique.
    Peut-on rouler avec un capteur vilebrequin défaillant ? Non. Un capteur
    vilebrequin en panne prive le calculateur de l'information de position du
    vilebrequin, ce qui désactive complètement l'injection et l'allumage par
    sécurité. Dans le meilleur des cas, le moteur tourne de façon très instable
    ; dans la majorité des cas, il refuse de démarrer ou cale brutalement en
    roulant, ce qui représente un danger de sécurité routière sérieux. Dès
    l'apparition des premiers symptômes, faites diagnostiquer le véhicule sans
    délai. Comment tester un capteur vilebrequin inductif avec un multimètre ?
    Débranchez le connecteur du capteur et mesurez la résistance entre les deux
    bornes avec un multimètre en mode ohmmètre. Une résistance comprise entre
    800 et 1 200 ohms (selon le constructeur) indique un bobinage intact. Une
    résistance nulle (court-circuit) ou infinie (circuit ouvert) confirme un
    capteur défectueux. Pour un capteur à effet Hall (3 fils), le test à
    l'ohmmètre ne suffit pas : il faut mesurer la tension de sortie à
    l'oscilloscope ou avec un scanner OBD2 en données live. Faut-il remplacer la
    roue phonique en même temps que le capteur ? Pas systématiquement. La roue
    phonique (cible dentée solidaire du vilebrequin) est une pièce mécanique
    robuste qui ne se remplace que si elle présente des dents cassées, déformées
    ou fortement corrodées. Avant de changer le capteur, inspectez la roue
    phonique avec une lampe à travers le logement : si les dents sont uniformes
    et sans dépôt ferreux excessif, la roue est réutilisable. Une roue phonique
    endommagée génère un signal irrégulier que même un capteur neuf ne peut pas
    corriger. Le remplacement du capteur vilebrequin nécessite-t-il une
    reprogrammation du calculateur ? Non, dans la grande majorité des cas. Le
    capteur vilebrequin est une pièce de mesure dont le remplacement à
    l'identique ne requiert aucune procédure d'apprentissage ou de codage. Il
    suffit d'effacer les codes défauts après la pose. Certains véhicules récents
    (notamment BMW, Volkswagen Group) demandent une procédure d'adaptation du
    calage par outil constructeur après remplacement de composants du système de
    distribution, mais cela concerne le calage moteur global, pas le capteur CKP
    seul.
---

# Capteur vilebrequin - Guide Diagnostic

## Fonction et Role

Mesurer la vitesse de rotation et la position du vilebrequin pour le calculateur moteur.

## Symptomes de Defaillance

- Moteur ne demarre pas
- Calages aleatoires en roulant
- Perte de puissance intermittente
- Voyant moteur allume (P0335, P0336)
- Rates d'allumage
- Demarrage long a chaud

## Pieces Associees

- capteur-d-arbre-a-cames
- bobine-d-allumage
- courroie-de-distribution
- volant-moteur

## FAQ

**Comment tester le capteur vilebrequin ?**
Mesurer la resistance (200-1000 ohms pour inductif). Scanner OBD pour codes P0335/P0336. Verifier le signal avec un oscilloscope si disponible.

**Capteur vilebrequin OE ou adaptable ?**
Privilegier OE ou OES (Bosch, Hella, Continental). Les generiques peuvent avoir un signal trop faible.

**Peut-on rouler sans capteur vilebrequin ?**
Non, le calculateur ne peut pas gerer injection ni allumage sans ce signal. Le moteur cale ou ne demarre pas.

**Tous les combien changer le capteur vilebrequin ?**
Pas de periodicite fixe. Duree de vie generalement superieure a 200000 km sauf defaut electrique.

**Quelle erreur eviter ?**
Ne pas forcer le capteur dans son logement. Respecter l'entrefer. Ne pas confondre avec le capteur d'arbre a cames.

## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Pas de periodicite fixe. Remplacer en cas de codes defaut P0335/P0336 confirmes.
