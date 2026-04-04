---
category: alimentation
slug: pompe-d-amorcage
title: Pompe d'amorcage
pg_id: 862
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
  role: Amorcer le circuit carburant lors du demarrage a froid
  must_be_true:
  - amorcer
  - aspirer
  - preparer
  must_not_contain:
  - freinage
  - climatisation
  - distribution
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - amorcer
  - aspirer
  - preparer
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
  - ❌ "repare l'injection"
  cost_range:
    min: 200
    max: 800
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE
  - tier: Adaptable
  brands:
    premium:
    - Bosch
    - Delphi
    - Denso
    standard:
    - Pierburg
    - VDO
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Demarrage difficile apres coupure moteur
    severity: confort
  - id: S2
    label: Poire molle sans resistance
    severity: confort
  - id: S3
    label: Bulles d air dans le circuit
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : demarrage difficile apres coupure moteur'
  quick_checks:
  - 'Observer : demarrage difficile apres coupure moteur ?'
  - 'Observer : poire molle sans resistance ?'
  - 'Observer : bulles d air dans le circuit ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Demarrage difficile apres coupure moteur
  - Poire molle sans resistance
  - Bulles d air dans le circuit
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '862'
  intro_title: A quoi sert Pompe d'amorcage ?
  risk_title: Pourquoi remplacer Pompe d'amorcage a temps ?
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
  - question: Comment choisir Pompe d'amorcage compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Pompe d'amorcage ?
    answer: En cas de demarrage difficile apres coupure moteur ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Pompe d'amorcage sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
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
doc_id: af4accc2-a048-50f2-901a-2de489e1ed13
content_hash: sha256:5eb27dfec1aaac21
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
  _has_tech_data: false
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La pompe d'amorçage (ou pompe d'amorce) est un composant du circuit
    d'alimentation en carburant, utilisé principalement sur les moteurs diesel
    et certains moteurs essence à injection indirecte. Son rôle est d'amorcer le
    circuit carburant en chassant l'air présent dans les conduites et en pré-
    remplissant le filtre à carburant avant le démarrage.Lors d'un arrêt moteur
    prolongé, d'une intervention de maintenance (remplacement du filtre à
    carburant) ou d'une panne à sec, des bulles d'air s'introduisent dans le
    circuit carburant basse pression. Ces bulles d'air empêchent la pompe
    d'injection de monter en pression, rendant le démarrage difficile ou
    impossible. La pompe d'amorçage permet à l'opérateur d'aspirer manuellement
    le carburant depuis le réservoir et de préparer le circuit pour la mise en
    route, sans avoir à actionner le démarreur à répétition.Dans sa forme la
    plus courante, la pompe d'amorçage se présente sous la forme d'une poire
    souple en caoutchouc ou silicone, montée en ligne sur le circuit de retour
    carburant, généralement à proximité du filtre à carburant. L'utilisateur
    pompe manuellement en pressant et relâchant la poire jusqu'à ce qu'elle
    offre une résistance ferme, signe que le circuit est plein de carburant et
    exempt d'air. Les pièces associées comprennent l'accumulateur de pression,
    le régulateur de pression carburant et la soupape de rampe commune.
  S2: >-
    Une pompe d'amorçage défaillante se manifeste principalement par des
    difficultés de démarrage caractéristiques. Identifier ces signes permet
    d'intervenir avant d'endommager la pompe d'injection principale.- Démarrage
    difficile après coupure moteur : Après chaque arrêt, le moteur nécessite
    plusieurs secondes de démarreur avant de s'allumer. Ce symptôme est
    particulièrement net après un stationnement prolongé (une nuit ou plus), ce
    qui distingue un problème d'amorçage d'autres pannes de démarrage.- Poire
    molle sans résistance : La poire de la pompe d'amorçage ne développe plus de
    résistance lorsqu'on la comprime, même après de nombreuses pressions. Ce
    symptôme indique que la poire a perdu son élasticité ou que les clapets
    anti-retour internes ne s'étanchéifient plus correctement.- Bulles d'air
    visibles dans le circuit : Sur les circuits équipés de raccords transparents
    ou de voyants de contrôle, la présence de bulles d'air dans la conduite
    carburant après une période de stationnement confirme une perte d'étanchéité
    dans le circuit, souvent imputable à la pompe d'amorçage elle-même.- Odeur
    de carburant sous le capot : Une fuite au niveau de la pompe d'amorçage ou
    de ses raccords crée une odeur de carburant persistante. La pompe en
    caoutchouc peut se fissurer avec l'âge, surtout sous l'effet de la chaleur
    moteur.- Démarrage impossible après remplacement du filtre : Si le moteur ne
    démarre pas après une opération de maintenance ayant nécessité d'ouvrir le
    circuit carburant, vérifier en premier la pompe d'amorçage et la procédure
    d'amorçage.- Résistance anormale à la compression de la poire : Au contraire
    d'une poire molle, une poire trop dure indique un clapet anti-retour collé
    en position fermée, bloquant le flux de carburant.
  S3: >-
    Le choix d'une pompe d'amorçage adaptée dépend des caractéristiques
    mécaniques du circuit carburant et des spécifications constructeur. Ce
    composant en contact direct avec le carburant doit être résistant aux
    hydrocarbures et compatible avec les températures du compartiment moteur.-
    Marque, modèle et année du véhicule : Les pompes d'amorçage sont souvent
    spécifiques à une gamme ou à un moteur. Renseigner ces données permet
    d'identifier si une poire universelle convient ou si une référence
    spécifique est requise.- Diamètre intérieur des durites de raccordement : Le
    diamètre interne des raccords de la pompe doit correspondre exactement au
    diamètre des durites du circuit (généralement 6, 8 ou 10 mm). Un mauvais
    diamètre rend le montage impossible ou crée des fuites.- Vérifier la
    compatibilité avec le type de carburant : Les matériaux de la pompe
    (caoutchouc, joints) doivent être compatibles avec le carburant utilisé
    (gazole standard, gazole B7, gazole B10, ou gazole de synthèse HVO).
    Certaines pompes anciennes ne résistent pas aux biocarburants à teneur
    élevée en FAME.- Vérifier les durites et les raccords associés : Lors du
    remplacement de la pompe d'amorçage, inspecter les durites de raccordement.
    Des durites craquelées ou durcies sont la cause principale des entrées d'air
    dans le circuit. Les remplacer si elles présentent des signes de
    vieillissement.- Distinguer la pompe d'amorçage manuelle de la pompe
    électrique d'amorçage : Certains véhicules disposent d'une pompe d'amorçage
    électrique commandée lors de la mise du contact. Ces deux types ont des
    références et des procédures de remplacement différentes.- Choisir une pièce
    avec clapet anti-retour intégré : Une poire d'amorçage sans clapet ne
    retient pas le carburant entre deux actionnements. Vérifier que la pièce de
    remplacement intègre des clapets anti-retour efficaces aux deux
    extrémités.Pour aller plus loin : consultez notre guide d'achat pompe
    d'amorcage — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement d'une pompe d'amorçage à poire manuelle est une opération
    accessible, rapide (15 à 30 minutes) et ne nécessitant pas d'outillage
    spécialisé. Travailler dans un endroit aéré, à l'écart de toute source de
    chaleur ou d'étincelle.- Identifier et localiser la pompe d'amorçage : La
    pompe est généralement montée en ligne sur la conduite de carburant basse
    pression, entre le réservoir et le filtre à carburant, ou en aval du filtre.
    Repérer son emplacement précis depuis la documentation technique du
    véhicule.- Préparer les matériaux absorbants : Placer un chiffon absorbant
    ou un bac de récupération sous la pompe avant toute dépose. Une faible
    quantité de carburant s'écoulera lors de la dépose des durites.- Dégrafer ou
    desserrer les colliers de durites : La pompe est raccordée aux durites par
    des colliers à vis ou des colliers à ressort. Utiliser une pince à colliers
    ou un tournevis pour desserrer les deux colliers et dégager la pompe.-
    Repérer le sens de montage : Avant de déposer la pompe, noter le sens du
    flux carburant (indiqué par une flèche ou une marque sur la pompe). Une
    pompe remontée dans le mauvais sens ne fonctionne pas.- Déposer la pompe
    défectueuse : Faire glisser les durites hors des embouts de la pompe en les
    faisant légèrement pivoter. Si les durites sont collées, les chauffer
    légèrement avec un sèche-cheveux pour les assouplir sans brûler le
    caoutchouc.- Monter la pompe neuve : Positionner la nouvelle pompe dans le
    bon sens (flèche dans le sens du flux), emboîter les durites sur les embouts
    en les enfonçant jusqu'à butée. Repositionner les colliers à au moins 5 mm
    des extrémités des embouts.- Amorcer le circuit : Comprimer et relâcher la
    poire manuellement une vingtaine de fois jusqu'à sentir une résistance
    ferme, signe que le circuit est rempli de carburant.- Démarrer et vérifier :
    Tenter le démarrage. Le moteur doit démarrer plus facilement qu'avant.
    Inspecter visuellement les raccords de durites pour confirmer l'absence de
    fuite.
  S4_REPOSE: >-
    Une fois la nouvelle pompe d'amorcage disponible et sa compatibilité
    vérifiée (référence, diamètre des raccords, type de connexion), procédez au
    remontage dans l'ordre inverse de la dépose. L'objectif principal est de
    rétablir un circuit carburant étanche, sans air résiduel. - Inspection des
    durites avant connexion — Examinez les durites amont et aval de la pompe.
    Toute fissure ou durcissement du caoutchouc justifie un remplacement
    simultané. Une durite défaillante en aval de la pompe neuve recréera
    immédiatement les bulles d'air qui ont conduit au diagnostic initial. -
    Positionnement de la pompe — Installez la pompe en respectant le sens
    d'écoulement du carburant indiqué par la flèche gravée ou la position des
    raccords. Une pompe montée à l'envers ne débite pas et peut forcer en sens
    inverse. - Connexion des durites — Glissez les durites sur les raccords de
    la pompe sur au moins 2 cm. Serrez les colliers en vis (Serflex) ou replacez
    les colliers d'origine (pinces). Tirez sur chaque durite pour vérifier
    qu'elle ne se désolidarise pas sous traction. - Fixation mécanique de la
    pompe — Si la pompe est fixée sur un support (bloc moteur ou cadre), serrez
    les vis de support au couple prescrit. Une pompe insuffisamment fixée vibre
    et fragilise les raccords. - Reconnexion électrique — Sur les pompes à
    commande électrique, branchez le connecteur jusqu'au déclic. Sur les pompes
    manuelles à membrane (poire), vérifiez simplement l'absence de fissure sur
    la poire avant de refermer. - Purge manuelle du circuit — Actionnez la poire
    d'amorçage à la main jusqu'à ressentir une résistance franche, signe que le
    circuit est plein. Si la pompe est électrique, effectuez plusieurs courtes
    mises en contact sans démarrer pour remplir le circuit. - Contrôle
    d'étanchéité — Après démarrage, vérifiez visuellement chaque raccord de la
    pompe pendant 2 à 3 minutes de ralenti. Toute trace humide de carburant
    indique une fuite à corriger immédiatement avant de conduire. Point de
    vigilance : sur les circuits diesel, la présence d'air résiduel se traduit
    par un démarrage difficile les premières tentatives puis un fonctionnement
    normal une fois la pompe en pression. Si le démarrage difficile persiste,
    purgez à nouveau le circuit ou vérifiez les joints de raccords.
  S5: >-
    Malgré la simplicité apparente de ce composant, plusieurs erreurs fréquentes
    compromettent l'efficacité du remplacement ou créent des problèmes
    persistants après l'intervention.- Monter la pompe dans le mauvais sens : La
    pompe d'amorçage est directionnelle. Les clapets anti-retour intégrés ne
    fonctionnent que si le flux carburant circule dans le bon sens, indiqué par
    une flèche ou un marquage sur la poire. Une pompe inversée empêche
    complètement le démarrage du moteur.- Ne pas remplacer les durites dégradées
    : Remplacer la poire sans changer les durites craquelées ou poreuses revient
    à réparer à moitié. Les durites continuent à aspirer de l'air, produisant
    exactement les mêmes symptômes qu'avant l'intervention. Inspecter
    systématiquement les durites lors du remplacement de la pompe.- Serrer les
    colliers de durites trop près des extrémités : Un collier positionné au ras
    de l'extrémité de la durite ne serre pas correctement le caoutchouc contre
    l'embout et peut causer une fuite. Positionner le collier à au moins 5 à 10
    mm de l'extrémité de la durite.- Ne pas amorcer suffisamment avant le
    démarrage : Visser les raccords et tenter de démarrer sans avoir
    préalablement amorcé le circuit manuellement fait travailler le démarreur à
    vide et peut fatiguer le moteur de démarrage. Pomper manuellement jusqu'à
    résistance ferme avant toute tentative de démarrage.- Confondre la pompe
    d'amorçage avec la pompe de gavage : Sur certains moteurs diesel, la pompe
    de gavage intégrée à la pompe d'injection est un composant distinct, plus
    complexe et coûteux. Vérifier que la panne provient bien de la pompe
    d'amorçage externe avant d'engager un remplacement de la pompe de gavage.
  S6: >-
    Une fois la pompe d'amorçage remplacée et le circuit amorcé, les contrôles
    suivants permettent de confirmer l'étanchéité et l'efficacité de
    l'intervention.- Test de résistance de la poire après amorçage : Comprimer
    la poire après une dizaine de pompes manuelles. Elle doit offrir une
    résistance ferme et élastique, signe que le circuit est plein et que les
    clapets fonctionnent. Une poire qui reste molle indique une fuite
    persistante dans le circuit.- Démarrage franc au premier tour de démarreur :
    Sur un moteur diesel en bon état, le remplacement d'une pompe d'amorçage
    fonctionnelle doit se traduire par un démarrage net et franc, sans longues
    tentatives au démarreur.- Inspection visuelle des raccords sous pression :
    Après le premier démarrage, inspecter les raccords de durites autour de la
    pompe pour détecter toute trace d'humidité ou d'odeur de carburant indiquant
    une micro-fuite.- Test après un stationnement prolongé (12-24 heures) :
    Laisser le véhicule immobile une nuit et vérifier que le démarrage reste
    facile le lendemain matin. Si le démarrage redevient difficile, l'étanchéité
    du circuit est encore insuffisante et il faut poursuivre la recherche de
    fuite.- Vérification de l'absence de bulles d'air dans le circuit : Sur les
    circuits avec raccord transparent ou voyant de contrôle, vérifier après
    quelques minutes de fonctionnement moteur qu'aucune bulle d'air n'est
    visible dans la conduite de retour.
  S7: >-
    La pompe d'amorçage travaille en liaison avec plusieurs composants du
    circuit carburant. Une défaillance sur l'un d'eux peut recréer les mêmes
    symptômes après remplacement de la pompe. Vérifiez ces éléments lors de
    l'intervention. - Accumulateur de pression carburant — Maintient une
    pression résiduelle dans le circuit après extinction du moteur, facilitant
    le redémarrage. Un accumulateur défaillant nécessite plusieurs cycles de
    pompe avant le démarrage. Souvent confondu avec une pompe d'amorçage
    défaillante. - Régulateur de pression carburant — Maintient la pression dans
    le circuit à un niveau constant. Un régulateur percé laisse le carburant
    refluer vers le réservoir, provoquant les mêmes difficultés de démarrage
    après une coupure moteur. - Soupape de rampe commune — Sur les moteurs
    Common Rail, contrôle la pression en entrée de rampe. En cas de défaillance,
    la pression monte difficilement après une longue coupure, surtout à froid. -
    Filtre à carburant — Un filtre colmaté augmente la résistance à l'aspiration
    de la pompe d'amorçage et peut simuler une défaillance de pompe. À vérifier
    et remplacer si le kilométrage depuis le dernier remplacement est élevé. -
    Durites d'alimentation carburant — Les durites de la ligne basse pression se
    fissurent avec l'âge. Une microfissure laisse entrer de l'air dans le
    circuit, créant des bulles qui perturbent le démarrage. La pompe d'amorçage
    est particulièrement répandue sur les moteurs diesel avec filtre séparateur.
    Vérifiez le type de connexion (raccords rapides ou colliers) et la position
    sur le circuit (entre réservoir et filtre ou entre filtre et pompe haute
    pression) avant de commander.
  S8: >-
    Comment savoir si le problème de démarrage difficile vient de la pompe
    d'amorçage ou d'une autre pièce ?Le signe distinctif d'une pompe d'amorçage
    défaillante est que la difficulté de démarrage survient systématiquement
    après un stationnement prolongé et s'améliore si on pompe manuellement avant
    de tenter le démarrage. Si comprimer la poire manuellement une vingtaine de
    fois améliore le démarrage, la pompe d'amorçage est en cause (ou une durite
    associée laisse entrer de l'air). Si le démarrage reste difficile même après
    amorçage manuel, la panne est ailleurs (pompe de transfert, pompe
    d'injection, problème mécanique).Quelle est la durée de vie d'une pompe
    d'amorçage ?Une pompe d'amorçage en caoutchouc dure généralement entre 8 et
    15 ans selon l'exposition à la chaleur et au type de carburant utilisé. Les
    moteurs situés dans des compartiments très chauds ou fonctionnant au
    biodiesel dégradent le caoutchouc plus rapidement. Un remplacement préventif
    lors des grandes révisions (tous les 100 000 à 150 000 km) est une bonne
    pratique sur les moteurs diesel.Peut-on fabriquer une pompe d'amorçage ou
    utiliser une poire universelle ?Des poires d'amorçage universelles
    compatibles avec la majorité des circuits carburant diesel sont disponibles
    dans les rayons accessoires automobiles. Elles conviennent dans la grande
    majorité des cas, à condition de choisir le bon diamètre intérieur (6, 8 ou
    10 mm selon le véhicule) et de s'assurer que le matériau est homologué pour
    le carburant diesel. Vérifier la présence de clapets anti-retour intégrés
    avant l'achat.Faut-il amorcer le circuit carburant après le remplacement
    d'un simple filtre à carburant ?Oui. Toute ouverture du circuit carburant, y
    compris pour remplacer le filtre, introduit de l'air dans les conduites.
    Après la fermeture du circuit, pomper manuellement la poire d'amorçage
    jusqu'à résistance ferme, puis tenter le démarrage. Si le démarrage reste
    long malgré l'amorçage, faire tourner le moteur quelques secondes, couper le
    contact, re-pomper et recommencer jusqu'au démarrage complet.
---

# Pompe d'amorcage - Guide Diagnostic Complet

## Fonction et Rôle

Amorcer le circuit carburant lors du demarrage a froid

**Actions principales:** amorcer, aspirer, preparer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage difficile apres coupure moteur
- poire molle sans resistance
- bulles d air dans le circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe d'amorcage:

1. **Inspection visuelle** - Examiner l'état du pompe d'amorcage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- accumulateur-de-pression-de-carburant
- regulateur-de-pression-carburant
- soupape-de-rampe-commune-d-injection

## Critères de Compatibilité

Pour commander le bon pompe d'amorcage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"

## FAQ

**Comment choisir Pompe d'amorcage compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Pompe d'amorcage ?**
En cas de demarrage difficile apres coupure moteur ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Pompe d'amorcage sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
