---
category: capteurs
slug: capteur-abs
title: Capteur ABS
pg_id: 412
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
  role: Mesurer la vitesse de rotation de chaque roue et transmettre l'information au calculateur ABS
  must_be_true:
  - mesurer
  - detecter
  - transmettre
  must_not_contain:
  - electrovanne
  - modulateur
  - pompe abs
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
    min: 28
    max: 115
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Constructeur (OE)
    description: 'Capteur d''origine : connecteur, longueur de câble et sensibilité calibrés pour le calculateur d''origine.'
  - tier: Équivalent OE (OES)
    description: 'Capteurs produits par des équipementiers reconnus dans ce segment : Bosch, Hella, NTK, Delphi. Qualité et
      sensibilité conformes aux spécifications constructeur.'
  - tier: Adaptable
    description: Capteurs compatibles d'entrée de gamme. Vérifier impérativement le nombre de broches, la longueur de câble
      et le type de fixation.
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
    label: Voyant abs allume au tableau de bord
    severity: securite
  - id: S2
    label: Code defaut specifique a une roue
    severity: confort
  - id: S3
    label: Capteur visible endommage ou couvert de crasse
    severity: confort
  - id: S4
    label: Cable du capteur coupe ou denude
    severity: confort
  - id: S5
    label: Abs qui se declenche a basse vitesse sans raison
    severity: securite
  - id: S6
    label: Bruit anormal lors du fonctionnement abs
    severity: securite
  - id: S7
    label: Freinage desequilibre avec abs actif
    severity: securite
  - id: S8
    label: Plus de 150 000 km sans verification capteurs
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  quick_checks:
  - Voyant abs allume au tableau de bord ?
  - 'Observer : code defaut specifique a une roue ?'
  - 'Observer : capteur visible endommage ou couvert de crasse ?'
  - 'Observer : cable du capteur coupe ou denude ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant abs allume au tableau de bord
  - Code defaut specifique a une roue
  - Capteur visible endommage ou couvert de crasse
  - Cable du capteur coupe ou denude
  - Abs qui se declenche a basse vitesse sans raison
  - Bruit anormal lors du fonctionnement abs
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '412'
  intro_title: A quoi sert Capteur ABS ?
  risk_title: Pourquoi remplacer Capteur ABS a temps ?
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
  - question: Capteur ABS OE ou adaptable ?
    answer: Les capteurs adaptables de qualité fonctionnent très bien. Vérifiez la longueur du câble et le type de connecteur
      (2 ou 3 broches).
  - question: Comment savoir si mon capteur ABS est HS ?
    answer: Voyant ABS allumé, code défaut capteur spécifique à une roue, capteur visible endommagé ou câble coupé.
  - question: Tous les combien changer les capteurs ABS ?
    answer: Pas de périodicité. C'est une pièce durable. Remplacez uniquement en cas de défaillance confirmée par diagnostic.
  - question: Peut-on changer un capteur ABS soi-même ?
    answer: Oui, opération simple. Débrancher le connecteur, dévisser le capteur, nettoyer le logement, monter le neuf. Effacer
      le défaut après.
  - question: Quelle erreur éviter avec les capteurs ABS ?
    answer: Ne pas forcer si le capteur est grippé (risque de casse). Nettoyer la cible (roue dentée). Respecter l'entrefer
      si réglable.
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
doc_id: 21095e0f-9c43-57af-807b-0e85822fd63e
content_hash: sha256:ae70918984b4f522
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
  _source: delphiautoparts.com + hella.com + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 15
  _has_tech_data: true
  types_variants:
  - type: Hall
    source_ref: corpus RAG web OEM
  - type: composite
    source_ref: corpus RAG web OEM
  - type: inductif
    source_ref: corpus RAG web OEM
  - type: perforé
    source_ref: corpus RAG web OEM
  - type: ventilé
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_ece_r90: ECE R90
    val_0_1_km: 0,1 km
    val_100_a: 100 a
    val_21_a: 21 a
    val_347_a: 347 a
    val_5_a: 5 a
    val_7_a: 7 a
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le capteur ABS nommé aussi capteur devitesse de roue est placé au dessus de la roue d''impulsion qui est reliée aumoyeu
    de roue ou à l''arbre de transmission. Son rôle est de déterminer lavitesse de la roue. La rotation du disque cible monté
    sur les moyeux de roueentraîne des variations du champ magnétique, ce phénomène va déclencher des signauxqui seront transmis
    au calculateur puis analysés. Le calculateur ABS déterminela vitesse des roues ainsi le glissement et il utilise ces paramètres
    pourpermettre d''obtenir un freinage optimale sans bloquer les roues lors d''unfreinage d''urgence. Les capteurs ABS transmettent
    également les données qu''ils collectent à d''autres systèmesavancés au sein du véhicule suivant le niveau d''équipement
    de chaque voiture : - Le stabilisateur électronique detrajectoire ESP. - Le système anti-patinage ASR. - Le régulateur
    de vitesse. - Le système de navigation intégré. Il existe deux types de capteur ABS : - Capteur actif : il estactivé par
    l''application d''une alimentation en tension et génère alors unsignal de sortie. - Capteur passif : iltravaille sans
    alimentation en tension supplémentaire. En savoir plus : capteur abs — définition et rôle mécanique 🚨 Bruit Capteur ABS
    : causes et diagnostic Capteur ABS et capteur ESP : la même pièce ? Le capteur ESP (Electronic Stability Program) utilise
    les mêmes capteurs de vitesse de roue que le système ABS. En pratique, le capteur ABS et le capteur ESP sont une seule
    et même pièce physique. Lorsque le capteur de roue tombe en panne, les voyants ABS et ESP s''allument souvent simultanément
    au tableau de bord. Le système ESP utilise cependant des capteurs supplémentaires dédiés : le capteur de lacet (gyroscope
    mesurant la rotation du véhicule) et le capteur d''angle de braquage, qui sont des pièces distinctes.'
  S2: 'Ne pas attendre la panne complete pour intervenir. Symptômes d''usure : - Voyant abs allume au tableau de bord - Code
    defaut specifique a une roue - Capteur visible endommage ou couvert de crasse - Cable du capteur coupe ou denude - Abs
    qui se declenche a basse vitesse sans raison - Bruit anormal lors du fonctionnement abs - Freinage desequilibre avec abs
    actif - Plus de 150 000 km sans verification capteurs Symptômes détaillés et vérifications — ABS et ESP Un capteur ABS
    défaillant peut également déclencher des alertes liées au système ESP. Voici l''ensemble des signaux à surveiller, du
    simple voyant à la perte de contrôle active : - Voyant ABS allumé au tableau de bord : signe le plus fréquent — le calculateur
    a détecté un signal anormal sur au moins un capteur de roue. - Code défaut spécifique à une roue : un diagnostic OBD2
    permet d''identifier précisément le capteur en cause (avant gauche, arrière droit, etc.). - Capteur visible endommagé
    ou couvert de crasse : un capteur magnétique obstrué par de la boue ou un dépôt métallique peut générer des lectures erratiques
    sans être physiquement cassé. - Câble du capteur coupé ou dénudé : le câble longe le train roulant et est exposé aux projections
    — une rupture partielle produit des défauts intermittents difficiles à reproduire. - ABS qui se déclenche à basse vitesse
    sans raison : une roue qui envoie un signal de vitesse nul ou incohérent fait réagir le système de manière intempestive,
    ce qui allonge les distances de freinage. - Bruit anormal lors du fonctionnement ABS : un claquement ou un battement de
    la pédale de frein hors situation de freinage d''urgence peut indiquer une lecture erronée d''un capteur. - Freinage déséquilibré
    avec ABS actif : si une roue reçoit un signal erroné, le modulateur de pression peut sous- freiner ou sur-freiner sélectivement.
    - Voyant ESP allumé (capteur ESP défaillant) : le système ESP utilise les mêmes capteurs de vitesse de roue que l''ABS
    — un capteur ABS HS éteint également l''ESP, augmentant le risque de perte de contrôle en virage. - Perte de stabilité
    en virage ou sur sol glissant : sans données fiables de vitesse roue, le calculateur ESP ne peut pas moduler le freinage
    sélectif pour corriger une dérive. - Plus de 150 000 km sans vérification des capteurs : une inspection préventive est
    recommandée, notamment pour les véhicules exposés à la corrosion ou circulant souvent sur des pistes. Hypothèses à explorer
    Ces symptômes peuvent indiquer : un capteur physiquement endommagé, un encrassement de la cible magnétique ou de la roue
    phonique, une rupture du câble dans un gant de protection fissuré, ou une corrosion du connecteur. Un simple nettoyage
    suffit parfois si le capteur est intact. Vérifications non-invasives (à faire soi-même) - Brancher un outil de diagnostic
    OBD2 : les codes P0500–P0509 et C-ABS permettent d''identifier immédiatement la roue concernée sans démontage. - Inspecter
    visuellement chaque capteur accessible derrière la jante : présence de crasse, de déformation mécanique (choc de carrosserie)
    ou de corrosion sur le connecteur. - Tester un freinage progressif sur sol sec à basse vitesse (zone sécurisée) : un déclenchement
    ABS prématuré avant 10 km/h confirme un signal aberrant sur un capteur. - Vérifier l''état de la roue phonique (couronne
    dentée solidaire du moyeu ou de la transmission) : une dent cassée ou encrassée peut simuler une vitesse nulle sur la
    roue. Pour un diagnostic personnalisé adapté à votre véhicule, utilisez notre outil de diagnostic gratuit.'
  S2_DIAG: 'SymptômeCause probableActionVoyant abs allume au tableau de bordlocaliser source et verifier usure mecaniqueVoyant
    abs allume au tableau de bord ?Code defaut specifique a une rouelecture codes defaut obd et diagnostic electroniqueObserver
    : code defaut specifique a une roue ?Capteur visible endommage ou couvert de crasseremplacement preventif recommandeObserver
    : capteur visible endommage ou couvert de crasse ?Cable du capteur coupe ou denudelocaliser source et verifier usure mecaniqueObserver
    : cable du capteur coupe ou denude ?Abs qui se declenche a basse vitesse sans raisonlocaliser source et verifier usure
    mecaniqueVoyant abs allume au tableau de bord ?Bruit anormal lors du fonctionnement abslocaliser source et verifier usure
    mecaniqueVoyant abs allume au tableau de bord ?'
  S3: 'Critères essentiels pour choisir le bon capteur ABS : 1. Type de capteur : - Capteur passif (inductif) — génère un
    signal alternatif proportionnel à la vitesse. 2 fils, pas d''alimentation. Courant sur véhicules avant 2005. - Capteur
    actif (magnétorésistif / effet Hall) — signal carré numérique, plus précis à basse vitesse. 3 fils (alimentation + signal
    + masse). Standard sur véhicules récents. ⚠️ Les deux types ne sont pas interchangeables. Vérifiez le nombre de broches
    du connecteur. 2. Longueur du câble : - Elle varie entre l''avant et l''arrière, et parfois entre gauche et droite. Un
    câble trop court ne rejoindra pas le connecteur du faisceau. 3. Entrefer (gap) : - Sur les capteurs passifs, l''entrefer
    entre le capteur et la roue dentée (cible) est critique : typiquement 0.3 à 1.0 mm. Un entrefer trop grand = signal faible
    = code défaut. - Les capteurs actifs sont généralement auto-calibrés à l''entrefer. 4. OE vs aftermarket : - Les capteurs
    adaptables de qualité (Bosch, ATE, Delphi) fonctionnent très bien et coûtent 30 à 50 % de moins que l''OE. - Vérifiez
    la référence OE de votre capteur d''origine pour garantir la compatibilité. 5. Compatibilité véhicule : - Renseignez votre
    marque, modèle, année et motorisation pour filtrer les références compatibles. Pour aller plus loin : consultez notre
    guide d''achat capteur ABS — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 'Procédure de diagnostic d''un capteur ABS : 1. Lecture du code défaut (OBD) : Branchez une valise ou un lecteur
    OBD2. Les codes C0035-C0050 désignent un capteur spécifique (avant gauche, avant droit, arrière gauche, arrière droit).
    Notez la roue concernée. 2. Inspection visuelle du capteur : - Vérifier l''état du câble du capteur — coupure, dénudage,
    traces de frottement sur les flexibles de frein. - Vérifier le connecteur — oxydation, broches tordues, clips cassés.
    - Vérifier que le capteur n''est pas couvert de limaille ou de boue (faux signal). 3. Contrôle de l''entrefer : L''espace
    entre le capteur et la roue dentée (cible) doit être régulier. Un entrefer trop grand (capteur reculé) ou irrégulier (cible
    voilée) provoque un signal erratique. 4. Test de résistance (multimètre) : Débrancher le capteur et mesurer la résistance
    aux bornes : typiquement 800 Ω à 2 000 Ω pour un capteur inductif. Hors plage = capteur HS. 5. Contrôle de la roue dentée
    (cible) : Vérifier l''absence de dents cassées ou d''encrassement magnétique. Sur certains véhicules, la cible est intégrée
    au roulement de roue.'
  S4_REPOSE: 'Le remontage d''un capteur ABS est une opération accessible, mais plusieurs points de contrôle conditionnent
    l''efficacité du système après installation. L''entrefer entre le capteur et la cible (couronne dentée ou roulement encodeur)
    est particulièrement critique sur les capteurs actifs à effet Hall : un jeu hors tolérance génère des signaux erronés
    et déclenche le voyant ABS dès le premier roulage. - Vérifiez que le capteur ABS neuf est identique à celui déposé : type
    inductif ou effet Hall, nombre de broches du connecteur (2 ou 3), longueur du câble et diamètre du corps. Une confusion
    entre les positions avant et arrière, ou gauche et droite, est la première source d''erreur. - Nettoyez soigneusement
    le logement du capteur dans le moyeu ou la platine de freinage : éliminez la rouille, la crasse et les résidus de l''ancien
    capteur à l''aide d''un chiffon non pelucheux et si nécessaire d''un dégrippant. - Contrôlez l''état de la cible (couronne
    dentée) : les dents doivent être intactes, sans déformation ni encrassement. Si la cible est intégrée au roulement de
    roue , vérifiez l''état du roulement. - Insérez le capteur ABS dans son logement sans forcer. S''il ne rentre pas, vérifiez
    l''absence de corps étranger dans l''alésage — ne jamais frapper sur le corps du capteur. - Serrez la vis ou bride de
    fixation au couple constructeur (généralement 7 à 10 Nm). Un sous-serrage laisse le capteur vibrer et génère des faux
    signaux ; un sur-serrage fissure le corps du capteur. - Si le capteur est réglable en entrefer, vérifiez la distance capteur/cible
    avec un calibre à lame selon la valeur constructeur (typiquement 0,2 à 1,5 mm). Ajustez avec la cale d''épaisseur fournie
    si nécessaire. - Guidez le câble du capteur dans son chemin de câblage d''origine. Clipez chaque attache-câble et vérifiez
    qu''il n''y a pas de contact avec les pièces mobiles (roue, bras de suspension , disque de frein ). - Reconnectez le connecteur
    électrique jusqu''au clic de verrouillage. Vérifiez la continuité visuelle du câble sur toute sa longueur. - Remontez
    la roue et serrez les boulons de roue au couple constructeur (généralement 100 à 120 Nm). Abaissez le véhicule. - Rebranchez
    la batterie, puis effacez les codes défaut ABS avec la valise de diagnostic. Roulez à plus de 20 km/h pour que le calculateur
    recalibré valide le signal du nouveau capteur — le voyant ABS doit s''éteindre définitivement.'
  S5: 'Erreurs fréquentes avec les capteurs ABS : - ❌ Forcer pour extraire un capteur grippé — le corps du capteur est fragile
    (céramique ou plastique). Appliquer du dégrippant, chauffer légèrement le logement, puis tourner doucement. - ❌ Oublier
    de nettoyer la cible (roue dentée) — la limaille s''accumule sur les capteurs magnétiques. Nettoyer au chiffon non abrasif.
    - ❌ Ne pas effacer le code défaut après remplacement — le voyant ABS restera allumé tant que le défaut n''est pas effacé
    à la valise OBD. - ❌ Ignorer l''entrefer — sur les capteurs réglables, un entrefer trop grand donne un signal faible.
    Respecter la cote constructeur (généralement 0,5 à 1,5 mm). - ❌ Confondre capteur inductif et capteur actif — les capteurs
    actifs (Hall) ont 3 broches et ne sont pas interchangeables avec les inductifs (2 broches).'
  S6: 'Contrôles statiques - Vérifier le bon encliquetage du connecteur électrique - Contrôler que le câble est fixé dans
    tous ses clips et ne touche aucun élément mobile - Avec une valise OBD : effacer les codes défaut, vérifier que le capteur
    envoie un signal (vitesse de roue affichée) - Démarrer le moteur : le voyant ABS doit s''allumer puis s''éteindre après
    quelques secondes Essai routier - Rouler à 20-30 km/h : le voyant ABS doit rester éteint - Freiner progressivement puis
    fermement : l''ABS doit s''activer normalement sur surface glissante (pulsation dans la pédale) - Effectuer des virages
    à basse vitesse : vérifier l''absence de voyant ESP/ABS intempestif ⚠️ Consulter un atelier si : le voyant ABS reste allumé
    après effacement du code, le code défaut réapparaît immédiatement, pulsation anormale de la pédale en ligne droite. 🚨
    Bruit Capteur ABS : causes et diagnostic'
  S_GARAGE: 'Quand confier le remplacement d''un capteur ABS à un professionnel : - Capteur grippé ou cassé dans son logement
    — l''extraction d''un capteur corrodé demande un outillage spécifique (extracteur, chalumeau) pour ne pas endommager le
    moyeu ou le porte-fusée. - Code défaut persistant après remplacement — un capteur neuf qui déclenche encore le voyant
    ABS nécessite un diagnostic OBD approfondi : le problème peut venir du bloc ABS (agrégat), du câblage ou du calculateur.
    - Codage ou calibrage requis — sur certains véhicules (VAG, BMW), le nouveau capteur doit être appairé au calculateur
    ABS avec un outil de diagnostic constructeur. - Capteur arrière intégré au roulement — sur de nombreux véhicules récents,
    la cible magnétique est intégrée au roulement de roue. Le remplacement du capteur seul ne suffira pas si le roulement
    est en cause. Un garagiste qualifié dispose de l''outillage OBD, des extracteurs et de l''expérience nécessaires pour
    un diagnostic fiable et un montage sûr.'
  S7: 'Combien de capteurs ABS possède une voiture ? La plupart des véhicules modernes possèdent 4 capteurs ABS, un par roue.
    Certains véhicules plus anciens n''en ont que 3 (un par roue avant + un sur le différentiel arrière). Le code défaut OBD
    identifie précisément le capteur en cause. Peut-on nettoyer un capteur ABS au lieu de le remplacer ? Oui, si le capteur
    est simplement encrassé (limaille, boue). Nettoyez avec un nettoyant frein et une brosse douce. Si le voyant persiste
    après nettoyage et effacement du code défaut, le capteur est défaillant et doit être remplacé. Quel est le prix d''un
    capteur ABS ? Un capteur ABS coûte entre 15 € et 80 € selon le véhicule et la marque (Bosch, ATE, Febi). La main-d''œuvre
    varie de 30 à 90 minutes selon l''accessibilité — les capteurs arrière sont souvent plus longs à extraire (risque de grippage).
    Peut-on rouler avec un capteur ABS défaillant ? Oui, le freinage classique reste fonctionnel. En revanche, l''ABS sera
    désactivé : en cas de freinage d''urgence sur route mouillée, les roues peuvent bloquer. Le contrôle technique sanctionne
    un voyant ABS allumé en défaut majeur. Pièces associées au capteur ABS : - agregat de freinage - cable de frein a main
    - disque de frein - etrier de frein - kit de freins arriere - machoires de frein - plaquette de frein - roulement de roue'
  S8: Capteur ABS OE ou adaptable ?Les capteurs adaptables de qualité fonctionnent très bien. Vérifiez la longueur du câble
    et le type de connecteur (2 ou 3 broches). Comment savoir si mon capteur ABS est HS ?Voyant ABS allumé, code défaut capteur
    spécifique à une roue, capteur visible endommagé ou câble coupé. Tous les combien changer les capteurs ABS ?Pas de périodicité.
    C'est une pièce durable. Remplacez uniquement en cas de défaillance confirmée par diagnostic. Peut-on changer un capteur
    ABS soi-même ?Oui, opération simple. Débrancher le connecteur, dévisser le capteur, nettoyer le logement, monter le neuf.
    Effacer le défaut après. Quelle erreur éviter avec les capteurs ABS ?Ne pas forcer si le capteur est grippé (risque de
    casse). Nettoyer la cible (roue dentée). Respecter l'entrefer si réglable. Capteur ABS et capteur ESP, est-ce la même
    pièce ?Oui, le capteur de vitesse de roue est partagé entre le système ABS et le système ESP. Une seule pièce physique
    alimente les deux systèmes. Si le capteur tombe en panne, les voyants ABS et ESP s'allument ensemble. Pourquoi les voyants
    ABS et ESP s'allument en même temps ?Parce qu'ils utilisent le même capteur de roue. Un capteur défaillant coupe l'information
    aux deux systèmes simultanément. Un diagnostic OBD confirmera quel capteur est en cause.
  META: '{"og_title": "Capteur ABS défaillant : diagnostic voyant et remplacement", "meta_title": "Capteur ABS défaillant
    : voyant, diagnostic OBD et changement | AutoMecanik", "gate_report": "PASS", "schema_type": "Article", "og_description":
    "Voyant ABS allumé ? Capteur de roue défaillant. Guide entrefer, code défaut, compatibilité et remplacement étape par
    étape.", "primary_intent": "diagnostic", "char_count_desc": 153, "char_count_title": 55, "meta_description": "Voyant ABS
    allumé ? Capteur de roue défaillant probable. Vérifiez l''entrefer, lisez le code défaut et remplacez la bonne référence
    selon votre véhicule."}'
---

# Capteur ABS - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la vitesse de rotation de chaque roue et transmettre l'information au calculateur ABS

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant abs allume au tableau de bord**
  voyant abs allume au tableau de bord
- **Abs qui se declenche a basse vitesse sans raison**
  abs qui se declenche a basse vitesse sans raison
- **Bruit anormal lors du fonctionnement abs**
  bruit anormal lors du fonctionnement abs
- **Freinage desequilibre avec abs actif**
  freinage desequilibre avec abs actif

### 🟢 Autres Symptômes

- code defaut specifique a une roue
- capteur visible endommage ou couvert de crasse
- cable du capteur coupe ou denude
- plus de 150 000 km sans verification capteurs

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur abs:

1. **Inspection visuelle** - Examiner l'état du capteur abs
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

- agregat-de-freinage
- cable-de-frein-a-main
- disque-de-frein
- etrier-de-frein
- kit-de-freins-arriere
- machoires-de-frein
- plaquette-de-frein
- roulement-de-roue

## Critères de Compatibilité

Pour commander le bon capteur abs, vous devez connaître:

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

**Capteur ABS OE ou adaptable ?**
Les capteurs adaptables de qualité fonctionnent très bien. Vérifiez la longueur du câble et le type de connecteur (2 ou 3 broches).

**Comment savoir si mon capteur ABS est HS ?**
Voyant ABS allumé, code défaut capteur spécifique à une roue, capteur visible endommagé ou câble coupé.

**Tous les combien changer les capteurs ABS ?**
Pas de périodicité. C'est une pièce durable. Remplacez uniquement en cas de défaillance confirmée par diagnostic.

**Peut-on changer un capteur ABS soi-même ?**
Oui, opération simple. Débrancher le connecteur, dévisser le capteur, nettoyer le logement, monter le neuf. Effacer le défaut après.

**Quelle erreur éviter avec les capteurs ABS ?**
Ne pas forcer si le capteur est grippé (risque de casse). Nettoyer la cible (roue dentée). Respecter l'entrefer si réglable.
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
## Variantes et types
- composite
- perforé
- ventilé

## Normes applicables

[...]
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
## Variantes et types
- Hall
- composite
- inductif
- perforé
- venti

[...]
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


## Conseils supplementaires

<!-- materialized-from-db web/624cbc1f42da 2026-03-28 -->
### Instructions pour remplacer... - Montage auto - section-1

# Instructions pour remplacer... - Montage auto

- Skip to main content Skip to menu Skip to footer Partager sur Instructions pour remplacer les freins à tambour Nous vous conseillons de lire et de suivre attentivement les instructions fournies. Vous trouverez les mêmes instructions dans l’emballage des freins à tambour. N’oubliez pas de les conserver pendant toute la durée de vie du produit. En cas de passage de propriété, elles devront être remises au nouveau propriétaire du véhicule. Ces instructions de montage sont un guide générique sur les réparations, qui peuvent varier d’un système de freinage à l’autre. Les instructions spécifiques émises par le constructeur du véhicule ou du système de freinage doivent impérativement être respectées. Avant de commencer la procédure de remplacement, s’assurer que la pièce de rechange utilisée pour le remplacement est adaptée à la marque et au modèle du véhicule. Procédure de remplacement La procédure décrite concerne une roue, elle doit être répétée sur l’autre roue de l’essieu. 1. Démonter les roues. 2. Le frein à main doit être complètement relâché. 3. Mettre complètement 4. Démonter le tambour du frein. AVERTISSEMENT ! N’appliquer aucune force pour éviter d’endommager les moyeux et les roulements des roues, les capteurs et les bagues dentées. AVERTISSEMENT! Utiliser les outils spéciaux prévus. 5. Dans le cas de tambours de freins avec roulements des roues et bagues dentées intégrées, démonter ces pièces pour leur réutilisation postérieure (uniquement si les pièces ne présentent de dommages ou de défauts). Avant de passer aux autres phases de remplacement, nous vous conseillons de suivre ces étapes pour le nettoyage et le contrôle du Produit qui favorisent un meilleur montage. Nettoyage/contrôle/montage préalable 1. Nettoyer la surface de la bride/rehausse de centrage dans le moyeu de la roue. Celui-ci doit être parfaitement propre, exempt de toute trace de rouille et d’ébarbure, lisse. Surface de la bride brillante (ne pas utiliser de ponceuses d’angle !). 2. Dans le cas de tambours de freins avec roulements des roues intégrés, monter les pièces neuves ou démontées ne présentant pas de dommages ou de défauts, en suivant les prescriptions. Appliquer le lubrifiant prescrit. 3. Monter les nouveaux éléments d’étanchéité pour les roulements des roues. 4. Si présente, monter la bague dentée (neuve ou sans dommages ni défauts). ​​​​​​ DANGER! Tous les composants du frein à tambour, comme cylindres de la roue, mâchoires de frein, ressorts, leviers, supports, languettes, etc. doivent être contrôlés avant leur réutilisation pour vérifier leur parfait état et fonctionnement ou bien procéder au remplacement des pièces. 5. Sauf indication contraire, éliminer complètement le traitement anticorrosion du nouveau tambour de frein uniquement au niveau de la surface de la bride et de la surface de travail. Vérifier que la surface de la bride est propre, sans ébarbure et intacte. Procédure de montage 1. En cas d’utilisation de nouvelles mâchoires de frein, mettre complètement à zéro leur réglage. 2. Dans le cas d’un moyeu de la roue séparé, appliquer uniformément une très fine couche d’huile anticorrosion (pas en pâte) sur la bride. 3. Centrer le tambour de frein. En fonction du type de construction, fixer avec la vis ou avec le dispositif de sécurité et/ou avec la roue. 4. Serrer uniformément en croix ou (procéder dans le sens des aiguilles d'une montre) en deux phases en utilisant le moment de torsion prescrit. 5. Sur les tambours de frein avec moyeu de la roue intégré, centrer le tambour de frein, régler/fixer le roulement de la roue selon les prescriptions, fermer avec une calotte neuve ou ne présentant pas de dommages ni défauts. 6. Régler selon les prescriptions le jeu des mâchoires du frein de service/frein à main. 7. Dans le cas d’un moyeu de la roue séparé, appliquer uniformément une très fine couche d’huile anticorrosion (pas en pâte) sur la bride. 8. Si le système hydraulique avait été ouvert, remplir/purger le système de freinage avec le liquide prescrit. Contrôle du fonctionnement ATTENTION! Contrôler que les parties en caoutchouc ne sont pas endommagées. Si nécessaire, les remplacer. 1. Actionner la pédale pour rapprocher les mâchoires du tambour. Répéter l’opération jusqu’à ce que la course de la pédale soit correcte. 2. Contrôler le niveau du liquide de frein dans le réservoir et faire l’appoint, si nécessaire. 3. Effectuer l'équilibrage de la roue. 4. Remonter la roue et serrer les vis de roue de la façon indiquée par le constructeur du véhicule ou dans le catalogue Brembo. Essai et rodage Effectuer un essai sur route. Durant cet essai, éviter de freiner brusquement et pendant plus de 3 secondes. L’essai sert à vérifier l’absence de bruits et de vibrations provenant des freins. Le rodage à conseiller à l’utilisateur final consiste à parcourir 200 km, en effectuant des freinages doux et courts, sans faire intervenir l’ABS. DANGER! Un mauvais rodage risque de compromettre l’efficacité du système de freinage . Informations générales et de sécurité Le produit Brembo a été conçu pour respecter les meilleurs standards de sécurité . Les Produits ne doivent pas être destinés à une utilisation différente de celle pour laquelle ils ont été conçus et fabriqués. L’ utilisation à d’autres fins , la modification ou la manipulation du produit risquent d’altérer son fonctionnement et de compromettre sa sécurité. Toute modification éventuelle ou toute utilisation impropre rendent nulles les Limitations de garantie et peuvent rendre la personne utilisant le Produit dans ces conditions responsable quant aux dommages physiques ou matériels éventuellement causés à des tiers. Dans ces instructions, lorsqu’il est indiqué « DANGER! », cela signifie que le non-respect de la procédure indiquée a de fortes probabilités de provoquer de graves dommages physiques ou même la mort. La mention « ATTENTION! » indique une procédure dont le non-respect peut provoquer des dommages physiques , alors que la mention « AVERTISSEMENT! » indique une procédure dont le non-respect peut provoquer des dommages au véhicule . DANGER! Avant de commencer la procédure de remplacement, s’assurer que la pièce de rechange est adaptée à la marque et au modèle du véhicule . Le Produit revêt une importance fondamentale pour la sécurité du véhicule sur lequel il est installé et il doit, donc, être installé par du personnel qualifié ayant reçu une formation adéquate ou possédant suffisamment d’expérience dans l’installation et dans l’utilisation prévue du Produit. L’installateur doit avoir à sa disposition l’outillage adéquat à l’installation et posséder des connaissances et une expérience appropriées pour s’occuper de l’entretien du véhicule. Une installation inadéquate ou erronée, due au non-respect de ces instructions ou autres, rendra nulles les Limitations de garantie et pourrait rendre l’installateur responsable quant aux dommages physiques ou matériels éventuellement provoqués. Brembo décline toute responsabilité en cas de dommage matériel ou physique provoqué à ou par une personne conduisant un véhicule sur lequel le produit aurait été installé de façon inappropriée. ATTENTION! Les pièces remplacées doivent être éliminées selon les dispositions prescrites par la loi. Il est important d’éviter de frapper violemment ou d’endommager le Produit et ses composants, parce que cela risquerait de réduire son efficacité et de provoquer des dysfonctionnements. Si nécessaire, remplacer les composants endommagés. Pour éviter tout dommage physique, nous conseillons de: Toujours porter des gants lors des opérations de démontage et de remontage des composants présentant des arêtes coupantes.

![Démonter les roues.   2. Le frein à main doit être complètement relâché.   3. Mettre complètement](_raw/web-images/b5c921aa115db50a.jpg)

![Azzera completamente la regolazione automatica o manuale dei ceppi dei freni.](_raw/web-images/b5c921aa115db50a.jpg)

![Dans le cas d’un moyeu de la roue séparé, appliquer uniformément une très fine couche d’huile anticorrosion (pas en pâte) sur la bride.](_raw/web-images/715ee9e5ec242126.jpg)

![Azzera completamente la regolazione automatica o manuale dei ceppi dei freni.](_raw/web-images/b5c921aa115db50a.jpg)

![Montare le ruote e serrare come al punto 13.](_raw/web-images/6d065a220e4ccac2.jpg)

- Éviter le contact direct de la peau avec le matériau de friction des plaquettes et mâchoires parce que cela risque de provoquer des abrasions.

- Utiliser des moyens appropriés pour éviter d’inhaler les poussières soulevées pendant le nettoyage des pièces.

- Protéger les composants électriques démontés contre l’humidité.

- Éviter le contact de graisse et autres lubrifiants avec les surfaces de freinage du disque et de la plaquette parce que cela risque de rendre le système de freinage inefficace et de provoquer de graves dommages physiques.

- Toujours remplacer les tambours de frein sur tout l'essieu , en utilisant les deux tambours présents dans l’emballage. À chaque remplacement des tambours, il est recommandé de remplacer également les mâchoires.

- Ne pas soumettre les composants électriques à des charges électrostatiques et à des chocs susceptibles d’endommager les pièces en plastique.

- S’assurer que tous les contacts électriques sont branchés correctement, en vérifiant que les témoins de signalisation s’allument. Si ce n'est pas le cas, le dysfonctionnement des témoins de signalisation peut provoquer une efficacité réduite du système de freinage ou le dysfonctionnement des indicateurs de freinage.

<!-- materialized-from-db web/bd63f4a06831 2026-03-28 -->
### Capteurs ABS – Textar Brake Technology - section-1

# Capteurs ABS – Textar Brake Technology

- Capteurs ABS – Textar Brake Technology CAPTEURS ABS Premium LA QUALITÉ TEXTAR Les capteurs ABS sont un élément important des systèmes de stabilité dynamique, tels que l’ABS, l’ASR et l’ESP. Ils surveillent en permanence la vitesse des roues et transmettent les signaux à l’unité de commande. Avec plus de 430 capteurs ABS actifs et passifs, la gamme de Textar propose le produit adéquat pour presque tous les véhicules. PLUS DE 1 REFERENCES MANAGE COOKIE CONSENT NOUS ACCORDONS UNE IMPORTANCE AU RESPECT DE VOTRE VIE PRIVÉE. NOUS UTILISONS LES COOKIES SUR CE SITE INTERNET POUR AMÉLIORER VOTRE EXPERIENCE ET ANALYSER NOTRE TRAFIC. POUR ACCEPTER TOUS LES COOKIES, CLIQUEZ SUR « J'ACCEPTE LES COOKIES ». Functional Functional Toujours activé The technical storage or access is strictly necessary for the legitimate purpose of enabling the use of a specific service explicitly requested by the subscriber or user, or for the sole purpose of carrying out the transmission of a communication over an electronic communications network. Preferences Preferences The technical storage or access is necessary for the legitimate purpose of storing preferences that are not requested by the subscriber or user. Statistics Statistics The technical storage or access that is used exclusively for statistical purposes. The technical storage or access that is used exclusively for anonymous statistical purposes. Without a subpoena, voluntary compliance on the part of your Internet Service Provider, or additional records from a third party, information stored or retrieved for this purpose alone cannot usually be used to identify you. Marketing Marketing The technical storage or access is required to create user profiles to send advertising, or to track the user on a website or across several websites for similar marketing purposes. Gérer les options

- Gérer les services

- Gérer {vendor_count} fournisseurs

- En savoir plus sur ces finalités

- {title}

- {title}

- {title}

- Gérer les options

- Gérer les services

- Gérer {vendor_count} fournisseurs

- En savoir plus sur ces finalités

- {title}

- {title}

- {title}

## References supplementaires

<!-- materialized-from-db manual/e5b55c545755 2026-04-02 -->
### Données techniques OEM — Capteur ABS

# Données techniques OEM — Montage maitrise
Source : delphiautoparts.com + textar.com (14 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- composite
- perforé
- ventilé

## Normes applicables

[...]

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
