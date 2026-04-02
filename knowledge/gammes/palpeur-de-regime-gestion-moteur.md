---
category: moteur
slug: palpeur-de-regime-gestion-moteur
title: Palpeur de regime gestion moteur
pg_id: 3896
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
business_priority: low
lifecycle:
  stage: v5_ssot
  last_enriched_by: skill:phase5-vague6
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Mesurer le regime moteur pour transmettre l'information au calculateur de gestion moteur
  must_be_true:
  - mesurer le regime
  - transmettre au calculateur
  - signal de rotation
  must_not_contain:
  - universel
  - tous modeles
  - adaptable tous
  confusion_with:
  - term: capteur-vilebrequin
    difference: Le palpeur de regime est souvent un synonyme du capteur vilebrequin, mais peut designer un capteur specifique
      sur certains moteurs anciens
  - term: capteur-impulsion
    difference: Le capteur d'impulsion mesure les impulsions de la couronne dentee, le palpeur de regime mesure la vitesse
      de rotation
  related_parts:
  - capteur-vilebrequin
  - bobine-d-allumage
  - calculateur-moteur
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
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Compte-tours inoperant ou instable
    severity: confort
  - id: S2
    label: Coupures moteur aleatoires
    severity: securite
  - id: S3
    label: Voyant moteur allume (codes P0335, P0336)
    severity: confort
  - id: S4
    label: Rates d'allumage ou moteur qui hesite
    severity: confort
  - id: S5
    label: Moteur ne demarre pas (pas de signal regime)
    severity: securite
  causes:
  - entrefer trop grand entre capteur et couronne dentee
  - fil de signal endommage ou connecteur oxyde
  - usure du capteur magnetique
  quick_checks:
  - 'Observer : compte-tours inoperant ou instable ?'
  - 'Observer : coupures moteur aleatoires ?'
  - Voyant moteur allume (codes P0335, P0336) ?
  - 'Observer : rates d''allumage ou moteur qui hesite ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Pas de periodicite fixe. Verifier en cas de voyant moteur ou instabilite du regime.
  wear_signs:
  - Compte-tours inoperant ou instable
  - Coupures moteur aleatoires
  - Voyant moteur allume (codes P0335, P0336)
  - Rates d'allumage ou moteur qui hesite
  - Moteur ne demarre pas (pas de signal regime)
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '3896'
  faq:
  - question: Comment tester le palpeur de regime ?
    answer: Verifier la resistance avec un multimetre (valeur constructeur, generalement 200 a 1000 ohms pour un inductif).
      Scanner OBD pour codes P0335/P0336.
  - question: Palpeur de regime et capteur vilebrequin, c'est la meme chose ?
    answer: Souvent oui, mais sur certains moteurs anciens le palpeur de regime est un capteur distinct monte sur le volant
      moteur.
  - question: Peut-on rouler sans palpeur de regime ?
    answer: Non, sans signal de regime le calculateur ne peut pas gerer l'injection ni l'allumage. Le moteur cale ou ne demarre
      pas.
  - question: Palpeur OE ou adaptable ?
    answer: Privilegier l'OE ou OES (Bosch, Hella). Les capteurs generiques peuvent avoir un signal trop faible ou un entrefer
      inadequat.
  - question: Quelle erreur eviter ?
    answer: Ne pas forcer le capteur dans son logement (risque de casser). Respecter l'entrefer specifie par le constructeur.
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
doc_id: ad2cb6be-a5a9-543a-818e-2ac4b1a69bff
content_hash: sha256:eb4ea7b423749fb4
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
    role: 'mesure le regime moteur pour le calculateur (equivalent capteur vilebrequin ancienne generation)'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le capteur derégime est un des nombreux capteurs qui sont utilisés dans un
    véhicule pour transmettreles informations utiles pour assurer le
    fonctionnement du moteur. Il est situéà coté du volant moteur, il va mesurer
    le régime moteur (nombrede tours/minute). Ces informations seront transmises
    au calculateur moteur pourassurer une synchronisation optimal dans le cycle
    de combustion du moteur.
  S2: >-
    Un capteur de régimedéfaillant présente plusieurs signes de défaillance : -
    Comportement de l'aiguille du compte-tours vous constatez que le régime
    n'est pas stable. - Vous constatez que le moteur s'étouffe. - Des ratés du
    moteur. - Vous sentez des odeurs de carburant. - L'allumage du témoin de
    défaillance ou de gestion moteur sur le tableaude bord. Un capteur de régime
    défectueux va envoyer des informations erronées au calculateur moteurce qui
    va créer plusieurs problèmes pendant le cycle de combustion : - Usure des
    injecteurs. - Usure des soupapes. - Usure des pistons.
  S3: >-
    Le palpeur de régime (capteur RPM dédié à la gestion moteur) fournit au
    calculateur ECU les informations de vitesse de rotation nécessaires au
    calcul des temps d'injection et d'allumage. Son choix doit être rigoureux
    pour garantir la compatibilité électrique et mécanique avec le système de
    gestion du moteur. - Compatibilité exacte avec le calculateur moteur : le
    palpeur de régime dédiée à la gestion moteur est étroitement lié à la
    cartographie du calculateur ECU. Vérifiez impérativement la référence
    constructeur et ne vous fiez pas uniquement aux cotes mécaniques. Deux
    palpeurs de dimensions identiques peuvent délivrer des signaux de nature
    différente (analogique, numérique, fréquence variable). - Type de signal de
    sortie : identifiez si le calculateur attend un signal sinusoïdal (capteur
    inductif) ou un signal carré (capteur à effet Hall ou magnétorésistif).
    Cette information figure dans la documentation technique du véhicule ou dans
    les données du scanner OBD2 sous la rubrique type de signal capteur régime.
    - Tension d'alimentation (capteurs actifs) : pour les palpeurs à effet Hall
    ou magnétorésistifs, vérifiez la tension d'alimentation requise — 5 V ou 12
    V selon les constructeurs. Alimenter un palpeur 5 V avec 12 V le détruit
    immédiatement et peut endommager le calculateur ECU. - Référence TecDoc ou
    catalogue constructeur : utilisez impérativement un catalogue de référence
    (TecDoc, AutoData, ETKA pour Volkswagen Group, EPC Renault) pour croiser la
    référence OEM avec la pièce de remplacement. Ne commandez jamais sur la
    seule base d'une description textuelle. - Longueur du câble et type de
    connecteur : le palpeur de régime est souvent positionné dans un endroit
    difficile d'accès. Contrôlez la longueur de câble fournie et le type de
    connecteur (Sumitomo, AMP, Bosch Junior Timer) pour éviter toute adaptation
    de faisceau qui fragilise le circuit. - Équipementier de référence : pour ce
    type de capteur critique à la gestion moteur, privilégiez des marques
    disposant d'une validation OEM documentée : Bosch, Continental, Delphi,
    Febi-Bilstein, Vemo ou Hella selon la marque du véhicule. Évitez les
    références sans marque identifiée sur les circuits de gestion moteur.
  S4_DEPOSE: >-
    - Débranchez la batterie. - Levez et calez le véhicule. - Démontez la
    protection sous moteur si nécessaire. - Localisez l'emplacement du capteur
    de régime. - Débranchez le connecteur du capteur de régime. - Desserrez la
    vis de fixation du capteur régime. - Démontez le capteur le régime.
  S4_REPOSE: >-
    Remontage du palpeur de régime — procédure et validation du signal Le
    palpeur de régime (capteur de vilebrequin ou capteur de régime moteur)
    transmet les impulsions générées par la roue phonique au calculateur pour
    mesurer le régime moteur (RPM) et la position angulaire du vilebrequin. Son
    remontage impropre est souvent la cause d'un défaut récurrent après
    remplacement. - Vérification du capteur neuf — Comparer la référence
    constructeur, la longueur du nez de capteur, le type de capteur (inductif ou
    à effet Hall), le nombre de broches du connecteur. Un capteur inductif (2
    fils) et un capteur Hall (3 fils) ne sont pas interchangeables même si la
    fixation est identique. - Nettoyage du logement — Essuyer le logement du
    capteur dans le carter moteur avec un chiffon propre. Éliminer les copeaux
    ferreux qui s'accumulent sur les capteurs inductifs à aimant permanent (ils
    y adhèrent magnétiquement). Ces copeaux perturbent le signal si laissés en
    place. - Inspection de la roue phonique — Avant d'insérer le capteur neuf,
    regarder la roue phonique visible depuis le logement (ou depuis l'inspection
    de carter). Compter visuellement si possible les dents présentes : une dent
    manquante génère un signal haché que le calculateur interprète comme un
    capteur défaillant (code P0335). Nettoyer les dépôts gras sur les dents à la
    brosse métallique fine. - Contrôle de l'entrefer — L'entrefer (distance
    entre le nez du capteur et les dents de la roue phonique) est critique :
    trop grand = signal faible, ratés à froid ; trop petit = risque de contact
    mécanique à la dilatation thermique. Pour les capteurs inductifs, l'entrefer
    est généralement de 0,5 à 1,5 mm selon le constructeur. Les capteurs Hall
    ont généralement un entrefer plus tolérant (jusqu'à 2 mm). - Insertion et
    serrage du capteur — Engager le capteur dans son logement, vissez la vis de
    fixation (M6, couple 8-10 Nm). Sur les capteurs avec joint torique,
    s'assurer que le joint est bien dans sa gorge avant insertion. - Reconnexion
    du connecteur et cheminement du câble — Connecter le faisceau jusqu'au clic.
    Vérifier que le câble est guidé dans ses clips de maintien et qu'il ne frôle
    pas les poulies, courroies ou surfaces chaudes de l'échappement. Un câble de
    capteur de régime frottant sur une courroie d'accessoire s'abîme en quelques
    semaines. - Validation par outil diagnostic — Rebrancher la batterie.
    Brancher un lecteur OBD, démarrer le moteur. Vérifier la valeur de régime en
    temps réel : elle doit être stable au ralenti (700-900 tr/min selon moteur),
    sans sauts ni valeur nulle. Accélérer progressivement et vérifier la
    cohérence RPM. Effacer les codes mémorisés P0335/P0336/P0338 et effectuer un
    essai sur route avant de conclure. ✅ Après remontage, vérifiez les
    spécifications dans la fiche technique Palpeur de régime.
  S5: >-
    Le palpeur de régime gestion moteur est un capteur critique dont une pose
    incorrecte peut conduire à des dysfonctionnements du calculateur ECU ou à
    des pannes difficiles à diagnostiquer. Ces cinq erreurs récurrentes sont à
    éviter absolument. - Monter un palpeur de type différent sans vérification
    du signal : remplacer un palpeur inductif par un palpeur à effet Hall (ou
    l'inverse) parce que les cotes mécaniques sont identiques est une erreur
    fréquente et coûteuse. Le calculateur reçoit alors un signal incompatible
    avec sa cartographie, ce qui provoque des codes défauts RPM persistants, des
    ratés d'injection et dans certains cas un endommagement de l'étage d'entrée
    du calculateur ECU. - Ne pas nettoyer la surface de contact et le logement :
    des résidus de rouille, de calamine ou d'huile dans le logement du palpeur
    créent un entrefer non conforme ou contamine le connecteur. Nettoyez
    systématiquement le logement avec un chiffon non pelucheux avant la pose du
    palpeur neuf. - Serrer le palpeur sans respecter le couple constructeur : le
    couple de serrage est généralement spécifié entre 6 et 12 N.m selon le
    constructeur. Un serrage trop fort fissure le corps du capteur ; un serrage
    insuffisant laisse le palpeur vibrer et génère un signal bruité ou
    intermittent. Utilisez toujours une clé dynamométrique. - Inverser les fils
    du connecteur lors d'une repose : sur les palpeurs à trois fils
    (alimentation, masse, signal), inverser les fils d'alimentation et de signal
    court-circuite l'alimentation du capteur et peut endommager la sortie du
    calculateur. Photographiez systématiquement le câblage avant de débrancher
    le connecteur d'origine. - Omettre l'effacement de la mémoire défauts après
    la pose : le calculateur ECU mémorise les défauts de signal RPM et peut
    conserver un mode dégradé ou allumer le voyant moteur même après une pose
    correcte. Connectez un scanner OBD2, effacez les codes défauts et vérifiez
    leur absence après 5 minutes de fonctionnement moteur.
  S6: >-
    Après la pose du palpeur de régime, une vérification méthodique confirme que
    le calculateur ECU reçoit un signal correct et que le moteur fonctionne dans
    les paramètres attendus. - Effacement des codes défauts OBD2 : connectez un
    scanner OBD2 et effacez tous les codes présents avant le démarrage. Les
    codes liés au régime moteur (P0725, P0726, P0727, P0728 pour le capteur de
    vitesse turbine ou régime boîte, ou codes RPM spécifiques constructeur)
    doivent disparaître définitivement. - Contrôle du signal RPM en données live
    : dans le menu données en temps réel du scanner, vérifiez que la valeur RPM
    transmise au calculateur correspond au régime réel du moteur. Au ralenti
    stabilisé, la valeur doit être stable et cohérente (650 à 900 tr/min selon
    le moteur), sans sauts brusques. - Vérification du démarrage à froid :
    démarrez le moteur à froid et observez le comportement au ralenti pendant
    les 2 premières minutes. Un palpeur correctement posé permet un démarrage
    franc et une montée en température progressive sans irrégularités de régime.
    - Test de montée en régime : accélérez le moteur à vide de façon progressive
    jusqu'à 3 000 tr/min. Le régime doit monter et descendre de façon linéaire.
    Des à-coups, des trous ou un régime qui oscille signalent un signal instable
    à investiguer (entrefer incorrect, connecteur mal encliqueté). - Inspection
    visuelle du câblage : vérifiez que le câble du palpeur n'est pas positionné
    à proximité de surfaces chaudes (collecteur, turbo), qu'il n'est pas pincé
    par un autre organe, et que les clips de maintien du faisceau sont en place.
    - Contrôle de l'étanchéité au niveau du logement : inspectez la zone
    d'implantation du palpeur pour détecter toute trace de fuite d'huile. Le
    joint d'étanchéité du capteur doit être correctement en place. Une micro-
    fuite à cet endroit contamine le connecteur en quelques semaines et génère
    des pannes intermittentes.
  S7: >-
    - Capteur vilebrequin — Sur de nombreux moteurs, le palpeur de régime et le
    capteur vilebrequin désignent le même composant physique (lecture des dents
    de la roue phonique du vilebrequin). Vérifier la référence constructeur :
    sur certaines architectures les deux termes sont synonymes et une seule
    pièce couvre les deux fonctions. Sur d'autres moteurs, le palpeur de régime
    est distinct et complémentaire au capteur vilebrequin. - Capteur d'arbre à
    cames — Le calculateur croise le signal de régime du palpeur (position
    vilebrequin) avec le signal de phase du capteur d'arbre à cames pour
    séquencer l'injection cylindre par cylindre. Un défaut de synchronisation
    entre les deux génère un code de corrélation (P0016/P0017) et des ratés
    d'allumage. Diagnostiquer les deux capteurs simultanément si les ratés
    persistent après remplacement du palpeur. - Roue phonique / poulie
    vilebrequin — Le palpeur lit les impulsions générées par les dents de la
    roue phonique solidaire du vilebrequin. Une dent manquante, un dépôt de
    graisse ou une roue encrassée produit un signal haché interprété comme une
    panne du capteur. Inspecter la roue phonique depuis le logement du capteur
    avant de conclure au remplacement du palpeur. - Faisceau moteur / câblage du
    palpeur — Le câble du palpeur chemine le long du bloc moteur, exposé à la
    chaleur et aux vibrations. Une gaine craquelée, un connecteur corrodé ou un
    fil pincé dans le support de fixation génère des ratés intermittents à
    chaud. Contrôler la continuité du câble au multimètre (résistance < 1 Ω)
    avant de remplacer le capteur. - Bobine d'allumage — Des ratés d'allumage
    associés à un signal de régime erratique peuvent signaler une bobine
    défaillante plutôt que le palpeur. Un code défaut moteur précisant le
    cylindre fautif (P0301, P0302...) oriente vers la bobine ; un code P0335
    sans cylindre identifié oriente vers le palpeur. La lecture OBD distingue
    les deux avant toute intervention.
  S8: >-
    Quelle est la différence entre le palpeur de régime gestion moteur et le
    capteur de position vilebrequin ? Les deux capteurs mesurent la rotation du
    vilebrequin, mais ils n'ont pas le même rôle fonctionnel dans l'architecture
    électronique. Le capteur de position vilebrequin (CKP) fournit la position
    angulaire précise du vilebrequin pour synchroniser l'injection et
    l'allumage. Le palpeur de régime gestion moteur est un capteur dédié au
    calcul du régime en tours par minute (tr/min), utilisé principalement par le
    calculateur ECU pour les stratégies de gestion des régimes limites, du
    contrôle des émissions et de la modulation de la pression de suralimentation
    sur les moteurs turbo. Sur certains véhicules, un seul capteur remplit les
    deux fonctions ; sur d'autres (architectures plus complexes), ce sont deux
    capteurs distincts. Le voyant moteur s'allume après le remplacement du
    palpeur de régime. Que faire ? Un voyant moteur allumé après remplacement
    est normal si les codes défauts n'ont pas été effacés. Connectez un scanner
    OBD2 et effacez la mémoire. Si le voyant revient immédiatement après
    l'effacement, cela indique soit un problème de compatibilité du palpeur
    monté (technologie ou référence incorrecte), soit un connecteur mal
    encliqueté, soit un défaut du câblage entre le palpeur et le calculateur.
    Lisez les codes actifs avec le scanner pour identifier la nature exacte du
    défaut avant d'intervenir à nouveau. Comment localiser le palpeur de régime
    gestion moteur sur le moteur ? La position du palpeur de régime varie selon
    le constructeur et l'architecture moteur. Il est généralement implanté sur
    le bloc moteur, à proximité du volant moteur ou de la couronne dentée du
    vilebrequin, ou parfois sur le carter de distribution. Sur les moteurs à
    distribution par chaîne, il peut également se trouver côté distribution. La
    documentation technique du véhicule (manuel de réparation Haynes, ETAI, ou
    données AllData) et les schémas électriques du constructeur indiquent sa
    position exacte avec les couleurs de fils du connecteur. Peut-on tester le
    palpeur de régime sans le déposer du moteur ? Oui, dans une large mesure.
    Avec un scanner OBD2 disposant du mode données live, observez la valeur RPM
    transmise au calculateur au démarrage et en fonctionnement. Si la valeur est
    absente, incohérente ou présente des sauts anormaux, le capteur ou son
    câblage est suspect. Pour les capteurs inductifs, un oscilloscope branché
    sur les bornes du connecteur permet de visualiser la forme du signal
    sinusoïdal. Pour les capteurs à effet Hall, une mesure de tension de sortie
    (0 V / 5 V en commutation) suffit à confirmer le fonctionnement sans dépose.
    Le remplacement du palpeur de régime nécessite-t-il un effacement de la
    mémoire adaptative du calculateur ? Un simple effacement des codes défauts
    suffit dans la grande majorité des cas. La mémoire adaptative du calculateur
    (gestion du ralenti, coefficients de correction long terme) se recalibrera
    automatiquement après quelques cycles de conduite. Certains calculateurs
    diesel récents (PSA, Renault, BMW) demandent une procédure d'initialisation
    via l'outil constructeur après remplacement de capteurs liés à la gestion
    des émissions. Consultez la documentation spécifique au véhicule en cas de
    doute.
---

# Palpeur de regime gestion moteur - Guide Diagnostic

## Fonction et Role

Mesurer le regime moteur pour transmettre l'information au calculateur de gestion moteur.

## Symptomes de Defaillance

- Compte-tours inoperant ou instable
- Coupures moteur aleatoires
- Voyant moteur allume (codes P0335, P0336)
- Rates d'allumage
- Moteur ne demarre pas

## Pieces Associees

- capteur-vilebrequin
- bobine-d-allumage
- calculateur-moteur

## FAQ

**Comment tester le palpeur de regime ?**
Verifier la resistance avec un multimetre (valeur constructeur, generalement 200 a 1000 ohms pour un inductif). Scanner OBD pour codes P0335/P0336.

**Palpeur de regime et capteur vilebrequin, c'est la meme chose ?**
Souvent oui, mais sur certains moteurs anciens le palpeur de regime est un capteur distinct monte sur le volant moteur.

**Peut-on rouler sans palpeur de regime ?**
Non, sans signal de regime le calculateur ne peut pas gerer l'injection ni l'allumage. Le moteur cale ou ne demarre pas.

**Palpeur OE ou adaptable ?**
Privilegier l'OE ou OES (Bosch, Hella). Les capteurs generiques peuvent avoir un signal trop faible ou un entrefer inadequat.

**Quelle erreur eviter ?**
Ne pas forcer le capteur dans son logement (risque de casser). Respecter l'entrefer specifie par le constructeur.

## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Pas de periodicite fixe. Verifier en cas de voyant moteur ou instabilite du regime.
