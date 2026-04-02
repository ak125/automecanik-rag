---
category: moteur
slug: joint-de-collecteur
title: Joint de collecteur
pg_id: 40
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
  role: Assurer l'etancheite entre le collecteur et la culasse
  must_be_true:
  - assurer l'etancheite
  - empecher les fuites
  - separer les fluides
  must_not_contain:
  - boite de vitesses
  - electronique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - assurer l'etancheite
  - empecher les fuites
  - separer les fluides
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
    min: 20
    max: 80
    currency: EUR
    unit: joint
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d'origine (OE)
    description: 'Joint avec les mêmes spécifications matériau que la première monte. Pour l''échappement : feuille multicouches
      ou graphite expansé. Pour l''admission : élastomère basse porosité.'
  - tier: Equivalent OE (OES)
    description: Fabricants spécialisés en joints haute temperature. Corpus RAG cite Elring et Victor Reinz pour cette gamme.
      Matériaux validés pour les cycles thermiques.
  - tier: Adaptable générique
    description: Joints de forme standard pour applications communes. Convient aux moteurs atmosphériques en usage normal.
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
    label: Sifflement ou souffle a l echappement
    severity: confort
  - id: S2
    label: Bruit de claquement a froid qui disparait a chaud
    severity: confort
  - id: S3
    label: Ralenti instable prise d air admission
    severity: confort
  - id: S4
    label: Suie noire visible autour du joint d echappement
    severity: confort
  - id: S5
    label: Voyant moteur allume melange perturbe
    severity: confort
  - id: S6
    label: Odeur d echappement dans l habitacle
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  quick_checks:
  - 'Observer : sifflement ou souffle a l echappement ?'
  - Bruit de claquement a froid qui disparait a chaud ?
  - 'Observer : ralenti instable prise d air admission ?'
  - 'Observer : suie noire visible autour du joint d echappement ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Sifflement ou souffle a l echappement
  - Bruit de claquement a froid qui disparait a chaud
  - Ralenti instable prise d air admission
  - Suie noire visible autour du joint d echappement
  - Voyant moteur allume melange perturbe
  - Odeur d echappement dans l habitacle
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '40'
  intro_title: A quoi sert Joint de collecteur ?
  risk_title: Pourquoi remplacer Joint de collecteur a temps ?
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
  - question: Joint de collecteur OE ou adaptable ?
    answer: Les joints OES (Elring, Victor Reinz) sont recommandés, surtout pour l'échappement. Un joint de mauvaise qualité
      ne tiendra pas aux hautes températures.
  - question: Comment savoir si le joint de collecteur fuit ?
    answer: 'Échappement : sifflement ou bruit de souffle. Admission : ralenti instable, prise d''air, voyant moteur. Suie
      visible autour du joint.'
  - question: Tous les combien changer le joint de collecteur ?
    answer: Pas de périodicité fixe. À remplacer si bruit anormal ou fuite détectée. Le joint d'échappement s'use plus vite
      que celui d'admission.
  - question: Peut-on changer le joint de collecteur soi-même ?
    answer: Possible mais accès souvent difficile. Les goujons peuvent être grippés. Utiliser un dégrippant et travailler
      à froid.
  - question: Quelle erreur éviter avec le joint de collecteur ?
    answer: Ne pas forcer sur les goujons grippés (risque de casse). Nettoyer parfaitement les surfaces. Respecter le couple
      de serrage.
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
doc_id: 3e353235-ef96-5044-b74f-343057abe501
content_hash: sha256:26a72fb45bd6e0a3
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
  materials:
  - composant: joint echappement
    materiau: acier inox multi-couches + graphite (resistant 900°C+)
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le rôle du jointde collecteur est d'établir l'étanchéité entre le moteur et
    le collecteurd'admission ou d'échappement. - Joint de collecteur d'admission
    : il empêche la pénétration ou lafuite de l'air dans le moteur lors de la
    combustion. Une prise d'air altère la qualité de combustion. - Joint de
    collecteurd'échappement : il empêche la fuite des gaz d'échappement qui vont
    êtrerecueillis dans le collecteur et canaliser ensuite vers la ligne
    d'échappement. Le joint de collecteur doit posséder 3 qualités : - Le joint
    doit bien tenir la température dans ce cas il estconstitué de matériaux qui
    résistent à la température des gaz d'échappement. - Le joint doit bien tenir
    la pression parce qu'à la sortie deschambres de combustion la pression des
    gaz est entre 2et 3 bars, associée à la température et à la vitesse de
    sortie des gaz cela esttrès agressive pour le joint. - Le joint doit être
    bien étanche pour assurer l'étanchéité du collecteurd'admission et du
    collecteur d'échappement . Il existe 2 types de jointde collecteur : - Joint
    mono-pièce : un seul joint commun,inséré entre la culasse et le collecteur.
    - Jeu dejoints : chaque cylindre est équipé d'un joint indépendant. En
    savoir plus : joint de collecteur — définition et rôle mécanique 🚨 Bruit
    Joint de collecteur : causes et diagnostic
  S2: >-
    Un joint de collecteurdéfaillant présente plusieurs symptômes : - Odeur des
    gaz d'échappement dans l'habitacle. - Surconsommation du carburant. - Trace
    de suie côté collecteur d'échappement . - Bruit d'échappement lors de
    l'accélération. Un joint de collecteurdéfectueux et qu'il n'est pas remplacé
    à temps ne va plus assurer l'étanchéitéentre la culasse et le collecteur ce
    qui peut causer plusieurs problèmes : - Usure de la culasse. - Usure des
    pistons. Diagnostic complet : identifier une panne de joint de collecteur
  S3: >-
    Le joint de collecteur assure l'étanchéité entre le collecteur d'admission
    ou d'échappement et la culasse du moteur. Une défaillance de ce joint génère
    des fuites de gaz brûlés pouvant perturber le mélange air-carburant, altérer
    les mesures de la sonde lambda et provoquer une surconsommation
    significative. Sur le collecteur d'échappement, les gaz chauds qui
    s'échappent peuvent endommagent les câbles et durites environnants. Le choix
    du joint adapté est critique pour l'étanchéité durable et la performance
    moteur. - Collecteur d'admission vs collecteur d'échappement — Ces deux
    types de joints n'ont pas les mêmes contraintes thermiques. Un joint de
    collecteur d'admission opère entre 40 et 80 °C, souvent en matériau
    composite papier-métal. Un joint de collecteur d'échappement supporte des
    températures de 600 à 900 °C et doit être en acier inoxydable multicouche
    (MLS) ou graphite expansé. - Nombre de cylindres et configuration — Un
    moteur 4 cylindres en ligne utilise un joint de collecteur unitaire couvrant
    les 4 ports. Un V6 ou V8 dispose de deux collecteurs latéraux avec leurs
    joints propres. Identifier précisément la configuration avant de commander.
    - Matériau : graphite, acier MLS ou composite — Le graphite expansé offre
    une excellente résistance aux chocs thermiques et se déforme pour compenser
    les irrégularités de surface. L'acier MLS (Multi-Layer Steel) est plus
    rigide et adapté aux moteurs turbocompressés où les pressions de gaz sont
    élevées. - Épaisseur et portée du joint — L'épaisseur du joint conditionne
    la hauteur de serrage entre collecteur et culasse. Un joint trop fin sous-
    comprimé laisse passer les gaz ; un joint trop épais crée des contraintes
    mécaniques sur les goujons de fixation. Vérifier l'épaisseur nominale dans
    la documentation constructeur. - Compatibilité avec les goujons existants —
    Les goujons de fixation du collecteur doivent être en bon état (filetage
    propre, pas de corrosion). Si les goujons sont cassés ou détériorés, les
    remplacer avant de monter le nouveau joint, sinon le serrage sera inégal et
    le joint percera rapidement. - Version turbo ou atmosphérique — Sur les
    moteurs turbocompressés, le collecteur d'échappement est souvent intégré à
    la culasse de turbo. Le joint correspondant doit être conçu pour supporter
    la pression des gaz en amont du turbo (jusqu'à 2 bar en pic). Ne pas monter
    un joint atmosphérique sur une application turbo. - Marque, modèle, année et
    code moteur — Le code moteur (visible sur le bloc ou en rubrique P.5 de la
    carte grise) est déterminant pour sélectionner le bon joint : un même
    véhicule peut avoir reçu plusieurs versions de culasse au fil des années de
    production. Pour aller plus loin : consultez notre guide d'achat joint de
    collecteur — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Joint de collecteur pour
    connaître les spécifications. - Arrêtez le moteur et le laissé refroidir. -
    Débranchez la batterie. - Localisez le collecteur que vous allez lui démonté
    son joint. Note : pour cette opération il faut se référé à la revue
    technique de votre voiture pour savoir les démarches des opérations. Parce
    qu'il y'aura plusieurs composants qu'il faut démontez : filtre à air ,
    débitmètre d'air ... - Desserrez les fixations du collecteur à démonter. -
    Démontez le collecteur d'admission ou le collecteur d'échappement . -
    Retirez le joint du collecteur.
  S4_REPOSE: >-
    La repose du joint de collecteur d'admission ou d'échappement requiert un
    nettoyage minutieux des plans de joint et le respect strict des couples de
    serrage. Sur un collecteur d'échappement, les goujons grippés sont le piège
    numéro un : ils doivent être traités avant toute tentative de serrage pour
    éviter leur casse dans la culasse. - Vérifiez que le joint de collecteur
    neuf correspond exactement à la position (admission ou échappement), au
    nombre de cylindres et à la disposition des orifices du joint d'origine. Un
    joint d'admission ne s'utilise jamais sur l'échappement — les matériaux ne
    résistent pas aux températures. - Nettoyez soigneusement le plan de joint
    côté culasse avec un grattoir plastique et un chiffon imbibé de décapant
    joints. Éliminez toute trace de calamine, de résidu de l'ancien joint et
    d'huile. Terminez par un passage à l'air comprimé pour ne pas laisser de
    débris dans les conduits. - Nettoyez de même le plan de joint du collecteur
    lui-même. Contrôlez la planéité avec une règle rectifiée : une déformation
    supérieure à 0,3 mm impose le surfaçage du collecteur pour garantir
    l'étanchéité. - Sur collecteur d'échappement, appliquez un dégrippant
    pénétrant sur les filets des goujons et laissez agir 15 à 30 minutes. Si un
    goujon présente de la corrosion profonde, chauffez-le légèrement à la lampe
    à souder avant de visser l'écrou — la dilatation facilite le dévissage et
    évite la casse. - Positionnez le joint de collecteur côté culasse en
    alignant tous les orifices sur leurs guides. Sur les joints multi-couches,
    respectez impérativement le sens indiqué par la flèche gravée ou le marquage
    "TOP" ou "HAUT". - Présentez le collecteur en engageant simultanément tous
    les goujons dans leurs écrous pour ne pas déplacer le joint. Ne serrez aucun
    écrou avant que tous soient engagés à la main. - Serrez les écrous ou vis du
    collecteur en commençant par les points centraux puis en progressant vers
    les extrémités, en deux passes : une première passe à la moitié du couple
    final, puis une deuxième au couple prescrit par la revue technique
    (généralement 20-25 N·m à l'admission, 25-35 N·m à l'échappement). -
    Remontez les pièces périphériques déposées lors de l'accès : durites
    d'admission, brides de raccordement turbo ou catalyseur, support moteur,
    protections thermiques. Vérifiez que les durites sont bien orientées et que
    les colliers sont positionnés à 15 mm minimum du bord des embouts. -
    Rebranchez la batterie, démarrez le moteur à froid et laissez-le monter
    progressivement en température. Écoutez attentivement les sifflements ou
    bruits de souffle qui trahiraient une fuite de gaz autour du nouveau joint.
    - Contrôlez le serrage après le premier cycle thermique (moteur refroidi
    après fonctionnement) : un joint d'échappement se tasse légèrement à la
    première chauffe et peut nécessiter un appoint de serrage de 2 à 3 N·m pour
    maintenir l'étanchéité durable. Vérifiez également l'absence de voyant
    moteur (code P0420 ou déséquilibre de mélange). ✅ Après remontage, vérifiez
    les spécifications dans la fiche technique Joint de collecteur.
  S5: >-
    Erreurs fréquentes avec le joint de collecteur : - ❌ Réutiliser l'ancien
    joint — un joint de collecteur est à usage unique. Même s'il semble intact,
    la compression a déformé la matière. Toujours monter un joint neuf. - ❌ Ne
    pas surfacer le plan de joint — des résidus d'ancien joint ou des rayures
    sur la culasse empêchent l'étanchéité. Gratter au racloir plastique (jamais
    métallique sur l'alu). - ❌ Serrer trop fort — le joint de collecteur se
    serre en étoile, au couple constructeur (généralement 20-25 Nm). Un serrage
    excessif déforme le collecteur. - ❌ Confondre collecteur admission et
    échappement — les joints sont différents (matière, épaisseur, forme).
    Vérifier le côté du moteur. - ❌ Ignorer les goujons grippés — sur les
    collecteurs d'échappement, les goujons rouillent et cassent. Appliquer du
    dégrippant 24h avant et chauffer si nécessaire. - ❌ Oublier de vérifier le
    collecteur lui-même — un collecteur voilé ou fissuré fuira même avec un
    joint neuf. Contrôler la planéité à la règle.
  S6: >-
    Le joint de collecteur (admission ou échappement) assure l'étanchéité entre
    le collecteur et la culasse. Un joint mal posé provoque des fuites de gaz
    d'échappement chauds, altère la mesure du mélange air/carburant par la sonde
    lambda et peut déclencher un voyant moteur. Les contrôles suivants doivent
    être effectués dès la remise en route. - Contrôle du couple de serrage des
    écrous du collecteur : serrer les écrous du collecteur d'échappement en
    croix, progressivement, au couple constructeur (généralement 15 à 25 N·m
    selon le diamètre des goujons). Les goujons d'échappement travaillent à
    haute température et nécessitent un serrage rigoureux pour éviter tout
    relâchement thermique. - Vérification de l'état des goujons et des écrous :
    à l'issue du montage, s'assurer qu'aucun goujon n'est filetté, allongé ou
    cassé. Un goujon endommagé ne peut pas exercer la force de serrage
    nécessaire — le remplacer avant de valider le montage. - Premier démarrage à
    froid — écoute des fuites de gaz : démarrer le moteur froid et approcher
    l'oreille (prudemment, sans contact) de la zone collecteur. Tout sifflement
    ou souffle rythmé au régime moteur indique une fuite de gaz entre collecteur
    et culasse (symptôme RAG confirmé). Arrêter et resserrer. - Contrôle du
    bruit de claquement à froid : écouter spécifiquement le bruit de claquement
    qui apparaît à froid et disparaît à chaud, caractéristique d'un joint de
    collecteur qui fuit (symptôme RAG prioritaire). Si ce bruit a disparu après
    remplacement, le joint est correctement posé. - Resserrage après la première
    montée en température : après 15 minutes de fonctionnement et
    refroidissement complet, resserrer les écrous du collecteur au couple
    constructeur. La dilatation thermique lors du premier chauffage peut
    légèrement détendre certains écrous. - Contrôle de l'absence de suie : après
    30 minutes de fonctionnement, inspecter visuellement les bords du joint et
    la face du collecteur. L'absence totale de trace de suie noire confirme
    l'étanchéité. Des traces noires fraîches localisées indiquent un point de
    fuite résiduel. - Contrôle du voyant moteur : après 50 km de conduite
    incluant des phases à régime variable, vérifier l'absence de voyant moteur.
    Une fuite de gaz d'échappement perturbe la sonde lambda et génère un code
    défaut P0420 ou P0171/P0174 (mélange pauvre) — brancher un OBD2 si le voyant
    s'allume.
  S7: >-
    Quel est le prix d'un joint de collecteur ?Le prix varie selon le véhicule
    et la marque. Utilisez notre sélecteur pour trouver le joint de collecteur
    compatible avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon joint de collecteur est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un joint de collecteur défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la
    sécurité du véhicule. Consultez la section symptômes pour évaluer l'urgence
    du remplacement.- bagues d etancheite moteur - joint de cache culbuteurs -
    joint de culasse - soupape d admission - soupape d echappement - vis de
    culasse
  S8: >-
    Joint de collecteur admission ou échappement — quelle différence ?Le joint
    d'admission est en papier, caoutchouc ou composite (résistant aux
    hydrocarbures). Le joint d'échappement est en métal ou amiante-métal
    (résistant aux hautes températures, 600°C+). Ils ne sont pas
    interchangeables. Comment savoir si mon joint de collecteur fuit
    ?Échappement : sifflement ou souffle audible près du moteur, suie noire
    autour du joint, bruit de claquement à froid qui disparaît à chaud.
    Admission : ralenti instable, voyant moteur allumé (prise d'air),
    surconsommation. Peut-on changer un joint de collecteur soi-même ?Oui pour
    le collecteur d'admission (accès facile, boulons). Le collecteur
    d'échappement est plus difficile : goujons grippés, espace réduit, risque de
    casse. Prévoir du dégrippant et un extracteur de goujon. Quel est le prix
    d'un joint de collecteur ?Le joint seul coûte 5 à 40 €. La main-d'œuvre
    varie : 1h pour l'admission, 2-4h pour l'échappement (goujons,
    accessibilité). Budget total : 80-400 € selon la complexité. Faut-il changer
    les goujons en même temps que le joint ?Si les goujons sont rouillés,
    corrodés ou déformés : oui. Les goujons d'échappement sont les plus exposés.
    Prévoir un jeu de goujons neufs + écrous cuivrés pour éviter le grippage
    futur.
  META: >-
    {"meta_title":"Joint de collecteur : quand le changer ? |
    AutoMecanik","meta_description":"Sifflement à l'échappement, suie noire ou
    ralenti instable ? Joint de collecteur qui fuit. Guide diagnostic, symptômes
    et choix selon votre motorisation."}
---

# Joint de collecteur - Guide Diagnostic Complet

## Fonction et Rôle

Assurer l'etancheite entre le collecteur et la culasse

**Actions principales:** assurer l'etancheite, empecher les fuites, separer les fluides

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement a froid qui disparait a chaud**
  bruit de claquement a froid qui disparait a chaud

### 🟢 Autres Symptômes

- sifflement ou souffle a l echappement
- ralenti instable prise d air admission
- suie noire visible autour du joint d echappement
- voyant moteur allume melange perturbe
- odeur d echappement dans l habitacle

## Procédure de Diagnostic

Pour diagnostiquer un problème de joint de collecteur:

1. **Inspection visuelle** - Examiner l'état du joint de collecteur
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- bagues-d-etancheite-moteur
- joint-de-cache-culbuteurs
- joint-de-culasse
- soupape-d-admission
- soupape-d-echappement
- vis-de-culasse

## Critères de Compatibilité

Pour commander le bon joint de collecteur, vous devez connaître:

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

**Joint de collecteur OE ou adaptable ?**
Les joints OES (Elring, Victor Reinz) sont recommandés, surtout pour l'échappement. Un joint de mauvaise qualité ne tiendra pas aux hautes températures.

**Comment savoir si le joint de collecteur fuit ?**
Échappement : sifflement ou bruit de souffle. Admission : ralenti instable, prise d'air, voyant moteur. Suie visible autour du joint.

**Tous les combien changer le joint de collecteur ?**
Pas de périodicité fixe. À remplacer si bruit anormal ou fuite détectée. Le joint d'échappement s'use plus vite que celui d'admission.

**Peut-on changer le joint de collecteur soi-même ?**
Possible mais accès souvent difficile. Les goujons peuvent être grippés. Utiliser un dégrippant et travailler à froid.

**Quelle erreur éviter avec le joint de collecteur ?**
Ne pas forcer sur les goujons grippés (risque de casse). Nettoyer parfaitement les surfaces. Respecter le couple de serrage.
