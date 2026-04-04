---
category: alimentation
slug: pompe-a-air
title: Pompe à air
pg_id: 903
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
  role: Injecter de l'air frais dans l'echappement pour accelerer le rechauffement du catalyseur
  must_be_true:
  - insuffler
  - injecter
  - alimenter
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
  - insuffler
  - injecter
  - alimenter
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Pompe à air.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Comparer les dimensions et le type de montage avec la piece d origine
  - Choisir un equipementier reconnu pour garantir qualite et compatibilite
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
  - tier: Equivalent OE homologue
  - tier: Adaptable generique
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
    label: Voyant moteur au demarrage a froid
    severity: confort
  - id: S2
    label: Bruit de soufflerie anormal au demarrage
    severity: confort
  - id: S3
    label: Code defaut systeme air secondaire
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - 'Usure ou defaillance causant : voyant moteur au demarrage a froid'
  quick_checks:
  - Voyant moteur au demarrage a froid ?
  - Bruit de soufflerie anormal au demarrage ?
  - 'Observer : code defaut systeme air secondaire ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant moteur au demarrage a froid
  - Bruit de soufflerie anormal au demarrage
  - Code defaut systeme air secondaire
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '903'
  intro_title: A quoi sert Pompe à air ?
  risk_title: Pourquoi remplacer Pompe à air a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Comment choisir Pompe à air compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Pompe à air ?
    answer: En cas de voyant moteur au demarrage a froid ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Pompe à air sans verification atelier ?
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
doc_id: 463dbe16-d048-5dee-9d93-50104fe6a17e
content_hash: sha256:30a8f1b19ce329bf
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
    La pompe à air secondaire, également appelée pompe à air d'injection
    secondaire, est un composant du système de dépollution des gaz
    d'échappement. Son rôle est d'insuffler et d'injecter de l'air frais
    directement dans le collecteur d'échappement, immédiatement en aval des
    soupapes d'échappement, lors des premières minutes suivant le démarrage à
    froid.Ce système permet d'alimenter la réaction d'oxydation dans le
    catalyseur pendant la phase de montée en température. Le catalyseur ne
    devient pleinement efficace qu'à partir d'environ 250 à 300°C (température
    de light-off). En injectant de l'air chaud dans les gaz d'échappement encore
    riches en hydrocarbures imbrûlés, la pompe crée une post-combustion qui
    dégage de la chaleur supplémentaire et accélère la montée en température du
    catalyseur, réduisant ainsi les émissions polluantes en phase de démarrage à
    froid.La pompe à air est entraînée électriquement par un moteur DC commandé
    par le calculateur moteur (ECU) pendant une durée déterminée (généralement
    60 à 120 secondes après le démarrage). Elle est associée à une soupape d'air
    secondaire (soupape d'aspiration) qui contrôle le flux d'air, et à
    l'intercooler du circuit d'air secondaire. Ce système est présent sur de
    nombreux moteurs essence des années 1990 aux années 2010.
  S2: >-
    La défaillance de la pompe à air secondaire se traduit par des symptômes
    distincts, souvent détectables dès les premières secondes après le démarrage
    à froid. Ces signes ne doivent pas être ignorés car ils entraînent un échec
    au contrôle antipollution.- Voyant moteur allumé au démarrage à froid :
    C'est le signe le plus fréquent. Le calculateur détecte une absence de
    signal ou une valeur hors plage dans le circuit d'air secondaire et stocke
    un ou plusieurs codes défaut (P0410, P0412, P0418 selon le constructeur).-
    Bruit de soufflerie anormal au démarrage : Un bruit de frottement, de
    grincement ou de cliquetis dans la zone moteur dans les 60 premières
    secondes après le démarrage à froid indique une usure mécanique interne de
    la pompe (roulements, balais de moteur électrique).- Code défaut système
    d'air secondaire : La lecture des codes défaut OBD avec un scanner révèle
    des codes spécifiques au circuit d'air secondaire. Ces codes peuvent
    indiquer un débit insuffisant, un court-circuit dans le circuit
    d'alimentation ou une absence de réponse de la pompe.- Absence de bruit de
    pompe au démarrage à froid : Sur un véhicule dont la pompe fonctionnait
    normalement, son silence soudain au démarrage à froid signifie qu'elle ne
    s'enclenche plus, soit par défaillance électrique, soit par blocage
    mécanique.- Échec au test antipollution : Des émissions d'hydrocarbures (HC)
    anormalement élevées lors d'un test antipollution peuvent résulter d'un
    catalyseur qui ne monte pas correctement en température, causé par une pompe
    à air défaillante.- Consommation légèrement accrue à froid : Une combustion
    incomplète en phase de démarrage peut se traduire par une consommation
    légèrement plus élevée sur les premiers kilomètres.
  S3: >-
    Le choix d'une pompe à air secondaire de remplacement exige une
    correspondance précise avec les spécifications d'origine du véhicule. Ce
    composant électromécanique ne tolère pas les approximations de référence.-
    Marque, modèle, année et motorisation : La pompe à air est spécifique à
    chaque motorisation. Le débit d'air requis, la tension d'alimentation et les
    dimensions varient selon le moteur. Renseigner impérativement la cylindrée,
    le type d'injection et la puissance.- Référence OEM depuis le code défaut :
    Si un scanner OBD a été utilisé, les codes défaut permettent d'identifier
    précisément quel composant du circuit est en cause (pompe, relais, soupape
    de commutation). Croiser la référence OEM avec les catalogues
    équipementiers.- Vérifier d'abord le relais et la soupape : Avant de
    commander une pompe neuve, vérifier le relais de commande de la pompe et la
    soupape d'air secondaire. Ces composants tombent plus souvent en panne que
    la pompe elle-même et coûtent beaucoup moins cher. Un relais défaillant
    simule une pompe en panne.- Comparer avec la pompe déposée : Vérifier que la
    pompe de remplacement présente le même type de connexion électrique (nombre
    de broches, forme du connecteur), les mêmes points de fixation et la même
    orientation de la sortie d'air.- Préférer une pompe d'équipementier original
    : Les pompes à air de qualité inférieure présentent des durées de vie
    réduites sur ce poste soumis à des cycles thermiques importants. Privilégier
    les équipementiers Pierburg, Bosch, Delphi ou Hella selon la marque du
    véhicule.- Vérifier l'état des durites de raccordement : Le remplacement de
    la pompe est l'occasion d'inspecter et de remplacer les durites souples du
    circuit d'air secondaire, souvent craquelées ou durcies après plusieurs
    années.Pour aller plus loin : consultez notre guide d'achat pompe à air —
    comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement d'une pompe à air secondaire est une opération de difficulté
    intermédiaire, accessible à un mécanicien expérimenté. L'accès à la pompe
    varie fortement selon le véhicule. Prévoir 1 à 3 heures d'intervention.-
    Confirmer le diagnostic avant dépose : Lire les codes défaut avec un scanner
    OBD et vérifier le relais de la pompe (le substituer par un relais de même
    référence pour valider). Localiser la pompe sur le moteur (souvent en
    position basse sur le côté du bloc, proche du collecteur).- Déposer la
    batterie ou débrancher la borne négative : Toute intervention sur un
    composant électrique doit être précédée du débranchement de l'alimentation
    pour éviter les courts-circuits et protéger le calculateur moteur.- Accéder
    à la pompe : Selon le véhicule, l'accès peut nécessiter de retirer un cache
    moteur plastique, un boîtier de filtre à air, ou de travailler depuis le
    dessous du véhicule. S'équiper d'une lampe d'atelier pour bien visualiser
    les points de fixation.- Débrancher le connecteur électrique : Identifier le
    connecteur d'alimentation de la pompe (généralement 2 fils), déverrouiller
    le clip de retenue et tirer perpendiculairement pour débrancher.-
    Déconnecter les durites d'air : Desserrer les colliers de serrage des
    durites de raccordement (entrée air et sortie vers la soupape d'air
    secondaire). Bouchonner les extrémités pour éviter la chute de corps
    étrangers dans le circuit.- Déposer les fixations de la pompe : Dévisser les
    boulons de fixation (généralement M8 ou M10). La pompe peut être lourde (1 à
    2 kg). La maintenir pendant le retrait de la dernière fixation pour éviter
    une chute.- Monter la pompe neuve : Positionner la nouvelle pompe, visser
    les fixations au couple préconisé par le constructeur. Reconnecter les
    durites en vérifiant l'absence de vrillage, puis le connecteur électrique
    jusqu'au clic.- Effacer les codes défaut et tester : Reconnecter la
    batterie, effacer les codes défaut mémorisés avec le scanner OBD, démarrer à
    froid et vérifier l'activation de la pompe (bruit de soufflerie normal
    pendant 60-90 secondes) et l'absence de retour de code défaut.
  S4_REPOSE: >-
    Après remplacement de la pompe à air secondaire, le remontage doit être
    réalisé avec soin pour éviter les entrées d'air parasite, qui
    déclencheraient immédiatement de nouveaux codes défaut P0410 ou similaires.
    Procédez dans l'ordre suivant. - Vérification des durites et flexibles avant
    repose — Avant de positionner la nouvelle pompe, inspectez toutes les
    durites d'air et les raccords associés. Un flexible fissuré ou un collier
    desserré annulerait l'effet du remplacement en créant une fuite d'air. -
    Positionnement de la pompe dans son support — Installez la pompe à air dans
    son support antivibration en caoutchouc. Ces silentblocs doivent être en bon
    état pour isoler les vibrations de la pompe du reste de la carrosserie.
    Remplacez-les si durcis ou fissurés. - Fixation des vis de support — Serrez
    les vis de fixation du support de pompe au couple prescrit (généralement 10
    à 20 Nm selon le bloc moteur). Vérifiez que la pompe ne touche aucun élément
    mobile ou chaud de l'habitacle moteur. - Reconnexion des durites d'air —
    Raccordez la durite d'entrée d'air frais sur le filtre à air ou la prise
    atmosphérique dédiée. Raccordez la durite de sortie vers la soupape de
    commutation (soupape d'air secondaire). Serrez les colliers sans écraser le
    caoutchouc. - Reconnexion du connecteur électrique — Branchez le connecteur
    d'alimentation de la pompe jusqu'au déclic. Vérifiez que le câblage n'est
    pas en contact avec des pièces en mouvement ou des surfaces chaudes. -
    Remontage du cache moteur si déposé — Replacez le cache plastique supérieur
    du moteur en vérifiant l'absence d'outil oublié dans le compartiment. - Test
    au démarrage à froid — Démarrez le moteur froid. La pompe à air s'active
    automatiquement durant les premières secondes. Écoutez le bruit de
    soufflerie (normal et discret). L'absence de son ou un bruit anormalement
    fort indique un problème de montage ou de pièce. - Effacement des codes
    défaut — Après vérification du bon fonctionnement, effacez les codes défaut
    mémorisés via outil OBD. Le voyant moteur doit s'éteindre après un ou deux
    cycles de conduite complets. Attention : ne pas tester la pompe à air en la
    branchant directement sur batterie. Elle fonctionne sous la commande de
    l'ECU moteur à des moments précis. Un test hors véhicule n'est pas
    représentatif du fonctionnement en condition réelle.
  S5: >-
    Le diagnostic et le remplacement de la pompe à air secondaire font l'objet
    de plusieurs erreurs fréquentes qui conduisent à des remplacements inutiles
    ou à des pannes récidivantes.- Remplacer la pompe sans vérifier le relais :
    Un relais de commande défaillant coupe l'alimentation de la pompe et produit
    exactement les mêmes symptômes qu'une pompe HS. Le relais coûte moins de 20
    euros contre plusieurs centaines pour la pompe. Tester le relais en premier
    systématiquement.- Ignorer la soupape d'air secondaire : Si la soupape d'air
    secondaire est collée fermée, la pompe fonctionne mais aucun air n'est
    injecté. Ce cas génère les mêmes codes défaut qu'une pompe défaillante.
    Inspecter la soupape avant de conclure à la pompe.- Ne pas effacer les codes
    défaut après remplacement : Si les codes défaut ne sont pas effacés après
    l'intervention, le voyant moteur reste allumé même si la pompe est neuve.
    Effacer les codes et réaliser un cycle de démarrage à froid pour confirmer
    la réparation.- Omettre d'inspecter les durites : Des durites craquelées
    créent des fuites d'air qui diminuent le débit injecté et peuvent déclencher
    à nouveau des codes défaut en quelques semaines. Remplacer les durites
    détériorées lors de l'intervention sur la pompe.- Commander une pompe
    générique sans vérifier la référence : Les pompes à air de basse qualité
    présentent des débits et des tensions d'alimentation non conformes, ce qui
    génère des codes défaut persistants même après montage. Utiliser une
    référence compatible vérifiée pour le véhicule.
  S6: >-
    Après le montage de la pompe à air secondaire, les contrôles suivants
    permettent de valider la réparation avant de rendre le véhicule.- Test de
    démarrage à froid : Laisser le moteur refroidir complètement (plusieurs
    heures) avant le test. Au démarrage à froid, écouter le bruit
    caractéristique de soufflerie de la pompe pendant les 60 à 120 premières
    secondes. L'activation de la pompe doit être audible mais non gênante.-
    Lecture des codes défaut après 2 cycles de démarrage : Utiliser un scanner
    OBD pour vérifier l'absence de retour des codes défaut liés au système d'air
    secondaire après au moins deux démarrages à froid complets.- Vérification de
    l'absence de fuite sur les durites : Inspecter visuellement les raccords de
    durites sous le capot moteur chaud pour détecter toute fuite d'air (un
    sifflement ou une trace de calamine peut révéler un collier mal serré).-
    Contrôle de la fixation de la pompe : Après une dizaine de kilomètres,
    vérifier le serrage des boulons de fixation de la pompe, qui peuvent se
    détendre légèrement sous les vibrations et les cycles thermiques.-
    Vérification de l'absence de voyant au tableau de bord : Confirmer que le
    voyant moteur ne se rallume pas après plusieurs démarrages à froid
    successifs, signe que le système d'air secondaire est pleinement
    opérationnel.
  S7: >-
    La pompe à air secondaire s'intègre dans un sous-système complet de post-
    traitement des gaz. La défaillance d'un composant adjacent peut entraîner
    les mêmes symptômes qu'une pompe défaillante. Vérifiez ces éléments avant de
    conclure à un remplacement de pompe. - Soupape d'air secondaire — Cette
    soupape commandée électriquement régule l'admission de l'air injecté par la
    pompe dans le collecteur d'échappement. Une soupape bloquée fermée provoque
    les mêmes codes défaut qu'une pompe HS. Vérifier son état avant remplacement
    de la pompe. - Soupape d'aspiration d'air secondaire — Assure l'alimentation
    en air frais de la pompe. Une soupape d'aspiration défaillante prive la
    pompe d'air frais et accélère son usure par surchauffe interne. -
    Intercooler — Sur moteurs turbocompressés, l'intercooler conditionne la
    température de l'air d'admission. Bien que distinct du circuit d'air
    secondaire, il peut être inspecté simultanément si l'intervention nécessite
    le démontage du circuit d'air avant. - Durites et flexibles du circuit d'air
    secondaire — Les durites en caoutchouc vieillissent et se fissurent. Une
    fuite sur ce circuit génère un défaut de débit détecté par la sonde Lambda
    aval et déclenchera un code P0410 ou équivalent. - Relais de pompe à air —
    Le relais commande l'alimentation électrique de la pompe. Un relais
    défaillant empêche la pompe de démarrer. Vérifiez-le avant toute dépose si
    la pompe ne se déclenche pas au démarrage à froid. La référence exacte de la
    pompe à air dépend du moteur (cylindrée, code moteur) et non seulement de la
    carrosserie. Fournissez le code moteur inscrit sur le bloc ou la carte grise
    lors de votre commande.
  S8: >-
    le rôle de la pompe à air secondaire et pourquoi est-elle différente d'un
    compresseur d'air ?La pompe à air secondaire n'a rien à voir avec un
    compresseur ou une pompe à carburant. C'est un petit moteur électrique qui
    souffle de l'air frais dans le collecteur d'échappement pendant les 60 à 120
    premières secondes après un démarrage à froid. Son unique fonction est
    d'accélérer la montée en température du catalyseur pour réduire les
    émissions polluantes lors de la phase froide. Ce système est absent sur les
    véhicules diesel et sur certains moteurs essence récents équipés de
    catalyseurs chauffants.Le code défaut P0410 signifie-t-il forcément que la
    pompe est défaillante ?Non. Le code P0410 indique une défaillance du système
    d'injection d'air secondaire, pas nécessairement de la pompe elle-même. Ce
    code peut être causé par un relais de commande défaillant, une soupape d'air
    secondaire bloquée, une durite percée ou déconnectée, ou un problème de
    câblage. Tester ces éléments dans cet ordre avant de conclure à une pompe
    défaillante.Peut-on rouler avec une pompe à air secondaire en panne ?Oui
    techniquement, la pompe à air secondaire n'affecte pas le fonctionnement
    mécanique du moteur ni la sécurité du véhicule. Cependant, le voyant moteur
    allumé masque d'autres pannes potentielles et le véhicule échouera aux tests
    antipollution. Le contrôle technique peut refuser le véhicule en cas de
    voyant moteur présent. L'intervention reste nécessaire pour maintenir la
    conformité réglementaire.Peut-on supprimer la pompe à air secondaire sur un
    véhicule ancien ?La suppression de la pompe à air secondaire est illégale
    sur un véhicule homologué avec ce système, car elle modifie les dispositifs
    de dépollution. Un véhicule sans ce système provoque des codes défaut
    permanents et échoue au contrôle technique. Cette suppression n'est pas
    recommandée et peut entraîner un refus de contrôle technique en France.
---

# Pompe à air - Guide Diagnostic Complet

## Fonction et Rôle

Injecter de l'air frais dans l'echappement pour accelerer le rechauffement du catalyseur

**Actions principales:** insuffler, injecter, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant moteur au demarrage a froid
- bruit de soufflerie anormal au demarrage
- code defaut systeme air secondaire

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à air:

1. **Inspection visuelle** - Examiner l'état du pompe à air
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- intercooler
- soupape-d-air-secondaire
- soupape-d-aspiration-d-air-secondaire

## Critères de Compatibilité

Pour commander le bon pompe à air, vous devez connaître:

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

**Comment choisir Pompe à air compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Pompe à air ?**
En cas de voyant moteur au demarrage a froid ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Pompe à air sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
