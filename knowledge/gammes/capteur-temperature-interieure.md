---
schema_version: '5.0'
category: climatisation
slug: capteur-temperature-interieure
title: Capteur température intérieure
pg_id: 832
source_type: gamme
doc_family: catalog
truth_level: L2
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
domain:
  role: Le capteur de temperature interieure mesure la temperature de l''air dans l''habitacle pour reguler automatiquement
    la climatisation. Il est implante derriere le retroviseur interieur, dans la planche de bord ou dans le plafonnier.
  must_be_true: []
  must_not_contain: []
  related_parts: []
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
  S1: Il est implanté dans une coque derrière le rétroviseur intérieur, dissimulé dans la planche de bord ou encore dans le
    plafonnier (suivant le niveau d'équipement du véhicule). Certains capteurs comportent un micromoteur avec hélice de ventilation
    pour un brassage de l'air assurant une meilleure mesure.
  S2: Le capteur de température d'habitacle n'a pas de période de remplacement. Un capteur de température intérieure défaillant
    peut se signaler par un affichage au tableau de bord bloqué, ou manifestement non conforme à la réalité. Si le véhicule
    est équipé d'une climatisation automatique, la défaillance du capteur se traduit également par un fonctionnement inapproprié
    de celle-ci (trop chaud ou trop froid).Lors du remplacement du capteur il faut bien localiser la position de la pièce.
  S3: 'Le capteur de température intérieure (sonde habitacle) mesure la température de l''air dans l''habitacle et transmet
    cette valeur au calculateur de climatisation automatique pour ajuster le soufflage. Un capteur incompatible fausse toute
    la régulation thermique, quelle que soit la qualité du reste du système. Les critères de sélection sont les suivants :
    - Compatibilité stricte par référence véhicule : renseigner marque, modèle, motorisation et année de mise en circulation.
    Chaque constructeur définit une courbe de résistance NTC (coefficient de température négatif) propre à son architecture
    de calculateur climatisation. Un capteur générique peut afficher des écarts de 5 à 15°C entre la valeur transmise et la
    température réelle, ce qui empêche la climatisation automatique de maintenir la consigne. - Type de boîtier et système
    de fixation : la forme du boîtier (carré, rond, allongé) et le système de maintien (rotation d''un quart de tour, clips
    latéraux, vis) sont spécifiques à l''emplacement prévu dans le tableau de bord. Vérifier les dimensions hors-tout et le
    type de fixation avant de commander. - Nombre de broches du connecteur : 2 broches pour les capteurs passifs (résistance
    pure), 3 broches pour les capteurs avec micro- ventilateur intégré. Toujours identifier le brochage du faisceau d''origine
    pour ne pas commander une variante incompatible. - Présence d''un micro- ventilateur aspirant : sur les véhicules haut
    de gamme et certains compacts modernes (post-2005), le capteur habitacle intègre un petit ventilateur qui aspire l''air
    ambiant pour améliorer la réactivité de la mesure. Si votre application d''origine dispose de ce ventilateur, remplacer
    par un modèle sans ventilateur dégrade significativement la précision de régulation, notamment lors des journées très
    chaudes ou très froides. - Équipementiers recommandés : Valeo, Hella, Vemo, Behr proposent des références certifiées ISO
    conformes aux courbes constructeur. Les capteurs de marques inconnues présentent souvent des courbes NTC approximatives
    qui génèrent des erreurs de régulation permanentes sans code défaut détectable. - Ne pas confondre avec le capteur de
    température extérieure : les deux pièces sont parfois de forme similaire mais implantées à des endroits radicalement différents.
    Le capteur intérieur est toujours dans l''habitacle (tableau de bord, console, plafond). Le capteur extérieur est derrière
    la calandre ou dans le rétroviseur gauche. Identifier l''emplacement avant de commander.'
  S4_DEPOSE: 'L''accès au capteur de température intérieure s''effectue entièrement depuis l''habitacle, sans intervention
    sur le circuit frigorifique. L''opération dure généralement 20 à 45 minutes selon le modèle. Un démonte-garniture plastique
    est indispensable pour préserver le tableau de bord. - Couper le contact et attendre 30 secondes : mettre le véhicule
    hors tension avant toute manipulation du faisceau électrique. Sur les véhicules récents avec gestion électronique active,
    attendre que les calculateurs se mettent en veille. - Localiser précisément le capteur : sur la majorité des véhicules,
    le capteur est intégré dans la façade centrale du tableau de bord, derrière une petite grille d''aération reconnaissable
    à ses lamelles horizontales. Sur certains modèles, il est implanté dans la console centrale ou en plafond (véhicules haut
    de gamme bi-zone). Consulter le manuel d''utilisation ou le schéma d''implantation propre au modèle si l''emplacement
    n''est pas évident. - Déposer la grille de protection si présente : glisser un démonte-garniture plastique entre la grille
    et le tableau de bord, sans forcer. Certaines grilles sont retenues par deux clips latéraux — les comprimer simultanément
    pour les dégager sans casser les pattes. - Dégager le capteur de son logement : selon le système, soit une rotation d''un
    quart de tour dans le sens antihoraire, soit une pression sur deux clips latéraux tout en tirant doucement vers soi. Ne
    jamais tirer sur le câble — tenir fermement le boîtier du capteur. - Débrancher le connecteur électrique : appuyer sur
    la languette de déverrouillage et tirer délicatement le connecteur en tenant le boîtier plastique, pas les fils. Sur les
    connecteurs vieillis, un léger mouvement de rotation d''un côté puis de l''autre facilite l''extraction. - Inspecter le
    logement et le faisceau : vérifier l''absence de condensation ou de traces d''humidité dans le logement, qui pourrait
    indiquer une infiltration à traiter. Contrôler l''état des broches du connecteur (oxydation, écrasement). - Brancher le
    nouveau capteur avant de l''encastrer : connecter d''abord le connecteur électrique (le déclic confirme le verrouillage),
    puis emboîter le capteur dans son logement jusqu''au clic final. Cette séquence évite de travailler dans un espace contraint
    avec le connecteur déjà en position. - Remettre le contact et tester : activer la climatisation automatique et vérifier
    que la température affichée est cohérente avec la température ressentie dans l''habitacle. Sur les systèmes bi-zone, tester
    les deux côtés indépendamment.'
  S5: '- Commander sans vérifier la courbe NTC : deux capteurs d''aspect extérieur identique peuvent avoir des courbes de
    résistance thermique radicalement différentes selon le constructeur. Un capteur avec une courbe décalée transmet une valeur
    erronée en permanence — la climatisation compensera excessivement sans afficher de code défaut. Le seul moyen de le détecter
    est de mesurer la résistance du capteur à température connue et de la comparer aux valeurs du tableau constructeur. -
    Forcer le déclipsage avec un tournevis : les clips de retenue des boîtiers de tableau de bord sont en polypropylène fragile.
    Un outil métallique appliqué sans précaution casse les pattes de fixation et oblige à remplacer la garniture complète
    du tableau de bord — une intervention autrement plus coûteuse. Utiliser exclusivement des démonte-garnitures plastiques
    à lame fine. - Remplacer par un modèle sans micro-ventilateur quand l''original en est équipé : le micro- ventilateur
    aspirant garantit que l''air mesuré est bien représentatif de l''habitacle et non de la cavité stagnante du tableau de
    bord. Sans ventilateur, le capteur réagit avec un décalage de plusieurs minutes, rendant la régulation automatique erratique
    et inconfortable par temps chaud ou froid. - Laisser le connecteur partiellement engagé : un connecteur non clipsé génère
    une résistance de contact variable. La valeur transmise au calculateur oscille aléatoirement, produisant des variations
    de soufflage inexpliquées et difficiles à diagnostiquer. Vérifier systématiquement le déclic de verrouillage après branchement.
    - Remettre le contact immédiatement après intervention sur le tableau de bord : les calculateurs modernes peuvent réagir
    à une micro-déconnexion électrique par une procédure d''initialisation. Remettre l''alimentation avant que tous les connecteurs
    soient en place risque d''enregistrer un code défaut transitoire qui persistera au tableau de bord. Toujours finir le
    montage mécanique et électrique avant de remettre le contact.'
  S6: '- Contrôle de cohérence de la valeur mesurée : mettre le contact et activer la climatisation automatique. Relever la
    température affichée sur le panneau de commande et la comparer à la température ambiante réelle de l''habitacle mesurée
    avec un thermomètre indépendant. L''écart acceptable est de ±2°C. Un écart supérieur à 5°C indique un capteur avec une
    courbe NTC inadaptée ou une connexion défectueuse. - Test de réactivité du soufflage : modifier la consigne de plusieurs
    degrés (augmenter de 5°C puis diminuer de 5°C) et observer la réponse du soufflage. La ventilation doit s''adapter en
    moins de 30 secondes. Une réponse absente ou très lente suggère que le calculateur ne reçoit pas la valeur correctement.
    - Validation bi-zone sur les véhicules concernés : si le véhicule dispose d''une climatisation bi-zone (consignes conducteur
    et passager indépendantes), vérifier que les deux capteurs (si deux sont présents) fonctionnent indépendamment en modifiant
    les consignes de chaque côté. - Cycle thermique complet chaud/froid : réaliser un trajet de 20 à 30 minutes avec alternance
    de phases de chauffe (28-30°C de consigne) et de refroidissement (18-20°C) pour valider la régulation sur toute la plage
    opérationnelle et confirmer l''absence d''oscillations de la valeur mesurée.'
  S7: 'Lors du diagnostic ou du remplacement du capteur de température intérieure, les pièces du circuit de climatisation
    suivantes doivent être contrôlées pour identifier si le problème de régulation est bien limité au capteur : - Compresseur
    de climatisation — principal organe actif du circuit frigorifique. Si le compresseur présente un cycle d''enclenchement/déclenchement
    anormal (court-cycling), la température de soufflage varie indépendamment du capteur habitacle. À contrôler si le problème
    de régulation persiste après remplacement du capteur. - Pressostat de climatisation — protège le compresseur en mesurant
    la pression du réfrigérant. Un pressostat défaillant déclenche et coupe le compresseur de façon intempestive, créant des
    à-coups de température que le capteur habitacle tente vainement de compenser. - Bouteille déshydratante — filtre le réfrigérant
    et absorbe l''humidité résiduelle. Un filtre saturé réduit l''efficacité de refroidissement et perturbe la régulation
    automatique. À remplacer systématiquement lors de toute ouverture du circuit. - Évaporateur de climatisation — échangeur
    thermique situé dans le boîtier de chauffage. Si des odeurs de moisi persistent après remplacement du capteur, l''évaporateur
    est encrassé et doit être nettoyé ou remplacé. - Capteur de température extérieure — souvent confondu avec le capteur
    intérieur lors du diagnostic. Le calculateur de climatisation utilise les deux valeurs conjointement pour piloter le soufflage.
    Un capteur extérieur défaillant peut mimer les symptômes d''un capteur intérieur défaillant.'
  S8: 'La climatisation automatique chauffe ou refroidit trop : est-ce le capteur intérieur ? Un capteur habitacle défaillant
    transmet une valeur erronée au calculateur de climatisation, qui sur-compense ou sous-compense pour tenter d''atteindre
    la consigne. Tester rapidement : passer en mode manuel (forcer le débit d''air sans automatisme) et observer si le problème
    disparaît. Si oui, le capteur est suspect. Pour confirmer, brancher un scanner OBD capable de lire les données de climatisation
    (PID température habitacle) et comparer la valeur transmise à la température réelle mesurée par un thermomètre dans l''habitacle.
    Un écart supérieur à 5°C confirme la défaillance du capteur. Où se trouve exactement le capteur de température intérieure
    ? L''emplacement varie selon les constructeurs et les générations de modèles. Le plus fréquent est la façade centrale
    du tableau de bord, reconnaissable à une petite grille de ventilation intégrée. Sur les véhicules avec climatisation bi-zone
    haut de gamme (BMW, Mercedes, Audi post-2005), le capteur peut être implanté dans le plafond ou dans la console centrale.
    Sur les compacts plus anciens (années 1990-2005), il est parfois derrière la grille du tableau de bord côté passager.
    Le manuel d''utilisation ou un schéma d''implantation téléchargeable via le portail constructeur indique l''emplacement
    précis pour chaque modèle. Le remplacement du capteur nécessite-t-il une recharge de climatisation ? Non. Le capteur de
    température intérieure est un composant purement électronique implanté dans l''habitacle. Son remplacement ne touche en
    aucun cas le circuit frigorifique sous pression (compresseur, condenseur, détendeur, évaporateur). Aucune manipulation
    du gaz réfrigérant, aucune recharge et aucune habilitation spécifique ne sont requises. L''opération se réalise entièrement
    à l''intérieur du véhicule avec des outils de base. Peut- on remplacer le capteur de température intérieure soi-même ?
    Dans la grande majorité des cas, oui. La difficulté principale est de localiser le capteur et de décliper le boîtier sans
    abîmer les garnitures du tableau de bord. Prévoir un jeu de démonte-garnitures plastiques (3 à 5 EUR) pour protéger les
    surfaces. La dépose prend 20 à 45 minutes selon le modèle. La repose est symétrique à la dépose. La seule précaution électronique
    est de couper le contact avant d''intervenir et d''attendre que les calculateurs soient en veille. Pourquoi le capteur
    habitacle a-t-il un micro-ventilateur ? Le micro-ventilateur aspirant (visible par les lamelles de la grille de protection)
    sert à forcer la circulation de l''air habitacle devant l''élément sensible du capteur. Sans ce ventilateur, l''air dans
    la cavité du tableau de bord reste statique et sa température peut différer de plusieurs degrés de l''air ambiant de l''habitacle,
    surtout en cas de fort ensoleillement sur le tableau de bord. Le ventilateur garantit que la valeur mesurée correspond
    réellement à l''air que les occupants respirent, rendant la régulation automatique précise et confortable. Un code défaut
    OBD apparaît après remplacement : que faire ? Sur certains véhicules, la déconnexion temporaire du capteur (ou le remplacement
    par une pièce au brochage légèrement différent) génère un code défaut mémorisé dans le calculateur de climatisation ou
    le calculateur confort. Utiliser un scanner OBD compatible avec le constructeur concerné pour effacer les codes défauts
    après avoir vérifié que le nouveau capteur fonctionne correctement. Sur les véhicules BMW, Mercedes ou VAG, un outil de
    diagnostic constructeur ou multimarque (VCDS, ISTA, STAR) est parfois nécessaire pour accéder aux données de climatisation
    et effacer les codes spécifiques à ce système.'
---

# Capteur température intérieure

<!-- A enrichir : Phase 5 -->


## References supplementaires

<!-- materialized-from-db manual/6ef523b42185 2026-04-03 -->
### Données techniques OEM — Capteur température intérieure

# Données techniques OEM — Capteur température intérieure
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- Hall
- inductif
- pneumatique
- électrique

## Matériaux
- aluminium
- platine

## Valeurs techniques de référence
- 0,1 %
- 1,5 %
- 14 %
- 4,5 %
- 400 °C
