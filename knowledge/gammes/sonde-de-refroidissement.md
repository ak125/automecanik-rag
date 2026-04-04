---
category: capteurs
slug: sonde-de-refroidissement
title: Sonde de refroidissement
pg_id: 830
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
  role: Mesurer la temperature du liquide de refroidissement et informer le calculateur pour le pilotage moteur
  must_be_true:
  - mesurer
  - detecter
  - transmettre
  must_not_contain:
  - calorstat
  - thermostat
  - pompe a eau
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
  - ❌ "corrige la surchauffe"
  cost_range:
    min: 6
    max: 31
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  brands:
    premium:
    - Bosch
    - Hella
    - Continental VDO
    standard:
    - NTK (NGK)
    - FAE
    - Meat & Doria
    budget:
    - Febi Bilstein
    - Topran
    - Calorstat by Vernet
  quality_tiers:
  - tier: Origine (OE)
    description: Sondes fabriquees par l'equipementier d'origine. Courbe de resistance (CTN) et connecteur identiques a la
      piece constructeur.
  - tier: Qualite equivalente OE (OES)
    description: Equipementiers reconnus en capteurs moteur. Memes specifications electriques, fiabilite comparable.
  - tier: Adaptable de qualite
    description: Marques fiables en entree de gamme. Bien verifier le nombre de broches (2 ou 4) et la forme du connecteur
      avant commande.
diagnostic:
  symptoms:
  - id: S1
    label: Indicateur temperature bloque froid maximum
    severity: immobilisation
  - id: S2
    label: Ventilateur qui tourne en permanence ou jamais
    severity: confort
  - id: S3
    label: Bruit de ventilateur qui s emballe au demarrage
    severity: confort
  - id: S4
    label: Surconsommation et demarrage difficile a froid
    severity: confort
  - id: S5
    label: Odeur de liquide de refroidissement surchauffe
    severity: confort
  - id: S6
    label: Plus de 200 000 km sans controle du circuit
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  depose_steps: []
  quick_checks:
  - 'Observer : indicateur temperature bloque froid maximum ?'
  - 'Observer : ventilateur qui tourne en permanence ou jamais ?'
  - Bruit de ventilateur qui s emballe au demarrage ?
  - 'Comparer la consommation : surconsommation et demarrage difficile a froid ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Indicateur temperature bloque froid maximum
  - Ventilateur qui tourne en permanence ou jamais
  - Bruit de ventilateur qui s emballe au demarrage
  - Surconsommation et demarrage difficile a froid
  - Odeur de liquide de refroidissement surchauffe
  - Plus de 200 000 km sans controle du circuit
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '830'
  intro_title: A quoi sert Sonde de refroidissement ?
  risk_title: Pourquoi remplacer Sonde de refroidissement a temps ?
  risk_explanation: '**Pièce HS** - Le sonde de refroidissement peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le sonde de refroidissement peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Sonde de température OE ou adaptable ?
    answer: Les adaptables (Febi, FAE, NTK) fonctionnent bien. Vérifiez la courbe de résistance (CTN) et le nombre de broches
      (2 ou 4).
  - question: Comment savoir si ma sonde de température est HS ?
    answer: Indicateur bloqué à froid ou à chaud, ventilateur qui tourne en permanence, surconsommation, difficultés de démarrage
      à froid.
  - question: Tous les combien changer la sonde de température ?
    answer: Pas de périodicité. Pièce simple qui dure généralement 200 000+ km. À remplacer si valeurs incohérentes.
  - question: Peut-on changer la sonde de température soi-même ?
    answer: Oui, mais attention à la perte de liquide de refroidissement. Prévoir de compléter et purger le circuit après.
  - question: Quelle erreur éviter avec la sonde de température ?
    answer: Ne pas confondre sonde calculateur et sonde indicateur. Identifier laquelle est défaillante (diagnostic OBD).
      Purger le circuit après.
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
doc_id: 88def317-322d-56bf-96dd-63594c701dd0
content_hash: sha256:89476c9aed24f8f9
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
  area: Face avant du vehicule (radiateur) et bloc moteur
  access: Par le dessus (capot) ou face avant
  adjacent_parts:
  - radiateur
  - durites
  - pompe a eau
  - thermostat
installation:
  difficulty: moyen
  time: 30min a 2h
  tools:
  - tournevis
  - pince de serrage
  - bac de recuperation
  prerequisite: Moteur froid, circuit vidange avant depose
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  technical_notes:
    val_195_8__c: '195,8 °C'
    val_23_a: '23 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Un moteur peut être équipé d'une sonde de refroidissement,d'un capteur de
    refroidissement et d'un interrupteur de refroidissement. Surcertain véhicule
    ces fonctions peuvent être regroupées dans une ou deux sondes - La sonde
    detempérature : elle mesure la température du moteur, informe leconducteur
    sur le tableau de bord et allume le voyant de surchauffe. - Le capteur
    detempérature : mesure la température du moteur et envoie lavaleur mesurée
    au calculateur pour qu'il gère le fonctionnement du moteur. -
    L'interrupteurde température : met en marche ou arrête le ventilateur
    moteuren fonction de la température du moteur. Généralement la sonde
    detempérature et le capteur de température sont situés sur la culasse et
    l'interrupteurde température se situe soit sur le radiateurmoteur, ou dans
    certains cas surune des durites de liquide de refroidissement accouplées à
    ce dernier. En savoir plus : sonde de refroidissement — définition et rôle
    mécanique 🚨 Bruit Sonde de refroidissement : causes et diagnostic
  S2: >-
    Il existe plusieurs symptômes de dysfonctionnement de sondede
    refroidissement suivant les différents types : - Une sonde de températureHS
    : mauvaise indication de température tableau de bord, le voyant desurchauffe
    du moteur s'allume directement après la mise en route du moteur (lemoteur
    est froid). - Un capteur de températureHS : perte de puissance, fumée
    d'échappement noire, moteur ne démarre pas. - Interrupteur de températureHS
    : voyant allumé sur le tableau de bord, le ventilateur moteur nefonctionne
    pas. Si une des sondes de refroidissement est défectueuse etqu'elle n'est
    pas remplacé à temps cela peut amener à la surchauffe du moteuret même à la
    casse de ce dernier. Diagnostic complet : identifier une panne de sonde de
    refroidissement
  S3: >-
    La sonde de refroidissement (aussi appelée capteur de température du liquide
    de refroidissement ou CTT) informe le calculateur moteur en temps réel pour
    piloter l'injection, l'allumage, le ventilateur électrique et le chauffage
    habitacle. Une sonde avec une caractéristique de résistance différente de
    l'original fausse l'ensemble de ces régulations, pouvant provoquer une
    surconsommation persistante ou une surchauffe non détectée. La sélection par
    référence constructeur est obligatoire. - Caractéristique NTC et valeurs de
    résistance à des températures clés — Les sondes NTC (Negative Temperature
    Coefficient) voient leur résistance diminuer quand la température monte. Les
    valeurs de référence à vérifier : résistance à 20 °C (typiquement 2,2 kΩ à
    3,5 kΩ), à 80 °C (200 à 350 Ω) et à 110 °C (80 à 120 Ω). Un écart de 10 %
    sur ces valeurs décale la cartographie injection de 5 à 8 °C, ce qui
    enrichit ou appauvrit le mélange. - Nombre de broches du connecteur et rôle
    de chaque signal — Les sondes 1 broche alimentent uniquement le voyant de
    température ou la jauge analogique. Les sondes 2 broches fournissent un
    signal au calculateur moteur (injection/allumage). Les sondes 3 broches
    combinent signal calculateur et affichage jauge. Une inversion de type prive
    le calculateur de données ou sature l'affichage. - Filetage et pas de vis —
    Les filetages les plus répandus sont M12x1,5 et M14x1,5. Certains
    constructeurs utilisent M10x1 (Volkswagen groupe) ou des connecteurs
    enfichables sans filetage. Un filetage trop grand force les pas de vis du
    bloc moteur ; trop petit, il fuit. - Longueur de plongée dans le circuit —
    La longueur active de la sonde (de 10 à 30 mm selon les modèles) détermine
    si l'élément thermosensible est bien immergé dans le flux de liquide. Une
    sonde trop courte mesure la température de la paroi du conduit, pas du
    liquide, ce qui génère des erreurs de lecture à chaud. - Position de montage
    sur le circuit : culasse ou collecteur — La plupart des véhicules utilisent
    2 sondes de température : une en sortie de culasse (haute température,
    signal calculateur) et une autre en entrée de radiateur ou sur le boîtier
    thermostat (plus froide, affichage tableau de bord). Ces deux sondes ont des
    caractéristiques et des emplacements différents. - Compatibilité avec les
    liquides de refroidissement — Les sondes en laiton nickelé résistent aux
    liquides IAT et HOAT. Sur les circuits utilisant des liquides OAT à base
    d'azoles (pH élevé), préférer des sondes avec corps en acier inoxydable ou
    avec revêtement compatible pour éviter la corrosion de la gaine. - Pièces à
    contrôler avant remplacement — Avant de conclure à une sonde défaillante,
    vérifier l'état du connecteur électrique (oxydation des broches), la
    continuité du câblage (résistance de ligne inférieure à 1 Ω) et l'absence de
    fuite de liquide au niveau du joint. Un mauvais contact électrique imite
    parfaitement une sonde défaillante. Pour aller plus loin : consultez notre
    guide d'achat sonde de refroidissement — comparatif marques, critères de
    choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Sonde de refroidissement
    pour connaître les spécifications. - Arrêtez le moteur et le laissé
    refroidir. - Débranchez la batterie. - Ouvrir le bouchon du vase d'expansion
    pour libérer la pression du circuitde refroidissement. - Refermez le bouchon
    du vase d'expansion. - Levez et calez le véhicule en cas de besoin. - Mettre
    un bac de récupération pour récupérer le liquide de refroidissementen cas
    d'écoulement de ce dernier. - Localisez l'emplacement de la sonde
    refroidissement à démonter. - Débranchez le connecteur électrique de la
    sonde de refroidissement. - Démontez la sonde de refroidissementselon le
    type de fixation (visser ou avec agrafe).
  S4_REPOSE: >-
    Le remontage de la sonde de refroidissement est une opération courte, mais
    deux points sont non-négociables : l'absence de fuite au raccord fileté et
    la purge complète du circuit. Un circuit mal purgé génère des poches d'air
    qui faussent immédiatement les mesures de température et font tourner le
    ventilateur en permanence. - Vérifiez que la sonde de refroidissement neuve
    est identique à celle démontée : résistance CTN (courbe négative), nombre de
    broches (2 ou 4), diamètre et pas de filetage. - Contrôlez l'état du
    ventilateur de refroidissement et son module de commande — profitez de
    l'intervention pour tester le fonctionnement électrique du motoventilateur
    avant la remise en service du circuit. - Inspectez les durites de
    refroidissement proches de l'emplacement de la sonde : toute durite avec des
    craquelures visibles ou des zones molles doit être remplacée pendant
    l'opération. - Enduisez le filetage de la sonde avec du téflon liquide ou un
    ruban PTFE adapté aux applications de refroidissement pour garantir
    l'étanchéité sans bloquer les contacts électriques. - Remontez la sonde de
    refroidissement en la vissant à la main jusqu'en butée, puis serrez au
    couple prescrit (typiquement 15 à 25 N·m) — ne pas serrer à l'excès pour
    éviter de fissurer le pas de vis dans le bloc ou le boîtier. - Rebranchez le
    connecteur électrique de la sonde jusqu'au clic de verrouillage — un
    connecteur mal enfiché provoque exactement les mêmes symptômes qu'une sonde
    défaillante (indicateur bloqué, ventilateur déréglé). - Remplissez le
    circuit de refroidissement avec un mélange liquide de refroidissement / eau
    déminéralisée à la concentration préconisée par le constructeur
    (généralement 50/50 jusqu'à -35 °C). - Purgez le circuit en ouvrant les
    purgeurs disponibles et en faisant tourner le moteur à froid jusqu'à
    ouverture du thermostat : les bulles remontent naturellement vers le vase
    d'expansion. Maintenez le niveau jusqu'à stabilisation. - Rebranchez la
    batterie, démarrez le moteur et surveillez l'indicateur de température sur
    les 10 premières minutes : l'aiguille doit monter progressivement jusqu'à la
    position normale (milieu de cadran) et s'y stabiliser. - Vérifiez l'absence
    de fuite au raccord de la sonde après le premier cycle de chauffe complet,
    puis vérifiez à nouveau le niveau dans le vase d'expansion à moteur froid le
    lendemain.
  S5: >-
    Erreurs frequentes avec la sonde de temperature de refroidissement : -
    Confondre sonde de temperature pour jauge (tableau de bord) et sonde pour
    calculateur moteur — ce sont deux pieces distinctes avec des connecteurs
    differents- Ne pas vidanger partiellement le circuit avant depose — le
    liquide de refroidissement coule a la depose de la sonde- Oublier de
    remplacer le joint cuivre ou le joint torique de la sonde — un joint
    reutilise provoque une fuite de liquide de refroidissement- Ignorer un
    ventilateur qui tourne en permanence — signe de sonde en court-circuit, le
    calculateur active le refroidissement par securite- Ne pas effacer les codes
    defaut apres remplacement — le calculateur peut rester en mode degrade tant
    que l'ancien defaut est memorise
  S6: >-
    La sonde de refroidissement (ou capteur de température liquide de
    refroidissement) est un capteur électronique miniature dont le remplacement
    prend moins de 30 minutes mais dont la validation post-montage est critique.
    Elle transmet en permanence la température du circuit au calculateur moteur
    — une mesure erronée perturbe directement la richesse du mélange air-
    carburant, les seuils d'allumage du ventilateur et l'activation des
    protections moteur. - Vérification de l'étanchéité du raccord : après
    serrage de la sonde au couple constructeur (généralement 15 à 20 Nm),
    démarrer le moteur et inspecter immédiatement la base du capteur. Aucun
    suintement de liquide de refroidissement ni de vapeur blanche ne doit
    apparaître. Utiliser du téflon ou un joint torique neuf si livré avec la
    pièce — ne jamais reutiliser un joint vieux. - Contrôle de l'indicateur de
    température au tableau de bord : surveiller la montée en température lors du
    premier démarrage. L'aiguille doit progresser régulièrement depuis la
    position froide (0 °C environ) jusqu'au point de stabilisation à mi-cadran
    (entre 80 et 95 °C selon le thermostat). Une aiguille qui reste bloquée en
    butée froide ou qui oscille signale un connecteur mal encliqueté ou une
    sonde défaillante. - Déclenchement correct du ventilateur de refroidissement
    : observer à quel moment le ventilateur électrique s'enclenche. Sur la
    plupart des motorisations, le premier palier de ventilation se déclenche
    entre 95 et 100 °C, le second palier entre 100 et 105 °C. Un ventilateur qui
    tourne en permanence dès le démarrage ou qui ne se déclenche jamais indique
    une sonde non calibrée sur le véhicule. - Absence de codes défaut liés à la
    sonde : brancher un outil de diagnostic OBD après 5 à 10 minutes de chauffe.
    Vérifier l'absence des codes P0115, P0116, P0117, P0118 (circuit de
    température du liquide de refroidissement) et effacer les codes mémorisés
    avant le remplacement si le voyant moteur était allumé. - Contrôle de la
    consommation de carburant : après 100 km de circulation normale, la
    consommation doit revenir dans les valeurs constructeur. Une surconsommation
    persistante indique que le calculateur reçoit toujours un signal de froid
    permanent depuis la sonde — souvent dû à une résistance de sonde hors plage.
    - Vérification du niveau de liquide de refroidissement : le remplacement de
    la sonde entraîne une légère perte de liquide. Contrôler le niveau dans le
    vase d'expansion après refroidissement complet (moteur froid pendant au
    moins 1 heure). Compléter avec le mélange antigel adapté si le niveau est
    sous le repère MIN.
  S7: >-
    Quel est le prix d'un sonde de refroidissement ?Le prix varie selon le
    véhicule et la marque. Utilisez notre sélecteur pour trouver le sonde de
    refroidissement compatible avec votre véhicule et comparer les tarifs des
    différents équipementiers.Comment savoir si mon sonde de refroidissement est
    à changer ?Les signes d'usure les plus courants sont détaillés dans la
    section diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par
    un professionnel.Peut-on rouler avec un sonde de refroidissement défaillant
    ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans
    la sécurité du véhicule. Consultez la section symptômes pour évaluer
    l'urgence du remplacement.- Thermostat. - Pompe à eau . 📖 Fiche technique
    Sonde de refroidissement — intervalles et spécifications d’entretien.
  S8: >-
    Comment choisir Sonde de refroidissement compatible avec mon
    vehiculeRenseignez marque, modele, type moteur et annee, puis verifiez la
    reference Quand remplacer Sonde de refroidissement ?En cas de indicateur
    temperature bloque froid maximum ou de degradation Puis-je monter Sonde de
    refroidissement sans verification atelier ?Le montage peut exiger controles
    de couple, alignement et references.
  META: >-
    {"meta_title":"Sonde de refroidissement : symptômes et remplacement |
    AutoMecanik","meta_description":"Indicateur température bloqué, ventilateur
    déréglé, surconsommation à froid ? Diagnostiquez votre sonde de
    refroidissement et trouvez la référence compatible avec votre
    véhicule.","source":"rag://gammes/sonde-de-refroidissement.md"}
---

# Sonde de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la temperature du liquide de refroidissement et informer le calculateur pour le pilotage moteur

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Indicateur temperature bloque froid maximum**
  indicateur temperature bloque froid maximum

### 🟢 Autres Symptômes

- ventilateur qui tourne en permanence ou jamais
- bruit de ventilateur qui s emballe au demarrage
- surconsommation et demarrage difficile a froid
- odeur de liquide de refroidissement surchauffe
- plus de 200 000 km sans controle du circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de sonde de refroidissement:

1. **Inspection visuelle** - Examiner l'état du sonde de refroidissement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le sonde de refroidissement peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-a-eau
- radiateur-de-refroidissement
- thermostat
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon sonde de refroidissement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la surchauffe"

## FAQ

**Sonde de température OE ou adaptable ?**
Les adaptables (Febi, FAE, NTK) fonctionnent bien. Vérifiez la courbe de résistance (CTN) et le nombre de broches (2 ou 4).

**Comment savoir si ma sonde de température est HS ?**
Indicateur bloqué à froid ou à chaud, ventilateur qui tourne en permanence, surconsommation, difficultés de démarrage à froid.

**Tous les combien changer la sonde de température ?**
Pas de périodicité. Pièce simple qui dure généralement 200 000+ km. À remplacer si valeurs incohérentes.

**Peut-on changer la sonde de température soi-même ?**
Oui, mais attention à la perte de liquide de refroidissement. Prévoir de compléter et purger le circuit après.

**Quelle erreur éviter avec la sonde de température ?**
Ne pas confondre sonde calculateur et sonde indicateur. Identifier laquelle est défaillante (diagnostic OBD). Purger le circuit après.


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

<!-- materialized-from-db diagnostic/refroidissement.md 2026-01-08 -->
### Diagnostic - Systeme de refroidissement

# Systeme de refroidissement - Diagnostic complet

## Symptomes surchauffe

### Temoin temperature allume
- **Quand** : En roulant ou a l'arret
- **Caracteristique** : Voyant rouge fixe ou clignotant
- **Urgence** : Critique - Arreter immediatement le moteur

### Temperature monte rapidement
- **Quand** : Apres quelques kilometres
- **Caracteristique** : Aiguille dans le rouge en moins de 10 min
- **Urgence** : Haute - Risque joint de culasse

### Chauffage habitacle faible
- **Quand** : Moteur chaud
- **Caracteristique** : Air tiede au lieu de chaud
- **Indication** : Niveau liquide bas ou thermostat bloque

### Fuite liquide de refroidissement
- **Quand** : Vehicule a l'arret
- **Caracteristique** : Flaque verte/orange sous le vehicule
- **Localisation** : Durites, radiateur, pompe a eau

## Symptomes thermostat

### Moteur long a chauffer
- **Quand** : Par temps froid
- **Caracteristique** : Temperature ne monte pas apres 10 km
- **Cause probable** : Thermostat bloque ouvert

### Temperature instable
- **Quand** : En roulant
- **Caracteristique** : Aiguille qui oscille
- **Cause probable** : Thermostat defaillant

## Causes et solutions - Surchauffe

### 1. Niveau liquide insuffisant
- **Probabilite** : 40%
- **Verification** : Niveau vase expansion (moteur froid)
- **Solution** : Completer et chercher la fuite
- **Pieces** : Liquide refroidissement G12/G13
- **Urgence** : Moyenne

### 2. Pompe a eau defaillante
- **Probabilite** : 25%
- **Verification** : Jeu sur axe, fuite par trou temoin
- **Solution** : Remplacement (souvent avec distribution)
- **Pieces** : Pompe a eau
- **Urgence** : Haute

### 3. Thermostat bloque ferme
- **Probabilite** : 20%
- **Verification** : Durite superieure radiateur froide moteur chaud
- **Solution** : Remplacement thermostat
- **Pieces** : Calorstat/thermostat
- **Urgence** : Haute

### 4. Ventilateur HS
- **Probabilite** : 10%
- **Verification** : Ne se declenche pas a 100°C
- **Solution** : Test motoventilateur, fusible, relais
- **Pieces** : Motoventilateur, relais
- **Urgence** : Moyenne

### 5. Radiateur bouche/fuyant
- **Probabilite** : 5%
- **Verification** : Zones froides sur radiateur, traces calcaire
- **Solution** : Rinçage ou remplacement
- **Pieces** : Radiateur
- **Urgence** : Moyenne

## Causes et solutions - Fuites

### 1. Durites percees/craquelees
- **Probabilite** : 35%
- **Verification** : Inspection visuelle, traces blanches
- **Solution** : Remplacement durite
- **Pieces** : Durites refroidissement
- **Urgence** : Moyenne

### 2. Joint de pompe a eau
- **Probabilite** : 25%
- **Verification** : Fuite par trou temoin pompe
- **Solution** : Remplacement pompe complete
- **Pieces** : Pompe a eau
- **Urgence** : Haute

### 3. Bouchon vase expansion
- **Probabilite** : 20%
- **Verification** : Pression circuit (tarage bouchon)
- **Solution** : Remplacement bouchon
- **Pieces** : Bouchon vase expansion
- **Urgence** : Basse

### 4. Joint de culasse
- **Probabilite** : 10%
- **Verification** : Mayonnaise sous bouchon huile, fumee blanche echappement
- **Solution** : Remplacement joint (intervention lourde)
- **Pieces** : Joint de culasse, kit vis
- **Urgence** : Critique

### 5. Radiateur de chauffage
- **Probabilite** : 10%
- **Verification** : Odeur sucree habitacle, buee pare-brise
- **Solution** : Remplacement radiateur chauffage
- **Pieces** : Radiateur de chauffage
- **Urgence** : Moyenne

## Diagnostics complementaires

### Test de pression circuit
- Outil : Pompe de mise en pression
- Pression : 1.2 à 1.5 bar selon vehicule
- But : Detecter fuites non visibles

### Test CO2 dans liquide
- Outil : Testeur de fuite joint culasse
- Indicateur : Changement couleur (bleu → jaune)
- But : Confirmer fuite joint de culasse

## Recommandations

- **Liquide** : Respecter specifications constructeur (G12, G13, type D)
- **Melange** : Ne jamais melanger differents types
- **Vidange** : Tous les 4-5 ans ou 100 000 km
- **Purge** : Obligatoire apres intervention (bulles d'air = surchauffe)
- **Marques** : Valeo, Gates, SKF (pompes), Behr (radiateurs)
