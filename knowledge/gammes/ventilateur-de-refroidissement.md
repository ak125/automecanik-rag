---
category: refroidissement
slug: ventilateur-de-refroidissement
title: Ventilateur de refroidissement
pg_id: 508
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
  role: Forcer le passage de l'air a travers le radiateur quand le vehicule est a l'arret ou a faible vitesse
  must_be_true:
  - forcer
  - ventiler
  - refroidir
  must_not_contain:
  - pulseur
  - habitacle
  - chauffage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - radiateur-de-refroidissement
  - pompe-a-eau
  - thermostat
  - durite-de-refroidissement
  - vase-d-expansion
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
  - ❌ "evite la casse moteur"
  cost_range:
    min: 287
    max: 343
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  brands:
    premium:
    - Valeo
    - Behr/Hella
    - Gates
    - Nissens
    - Denso
    standard:
    - NRF
    - Van Wezel
    - Frigair
    - Thermotec
    - Kale
    budget:
    - Prasco
    - Polcar
    - Diederichs
  quality_tiers:
  - tier: Origine (OE/OES)
    description: Ventilateurs fabriqués par les équipementiers d'origine ou leurs filiales. Débit d'air, durabilité et connectique
      identiques à la pièce montée en usine.
  - tier: Équivalent OE
    description: Fabricants aftermarket reconnus, conformes aux spécifications constructeur. Bon rapport qualité/prix pour
      un remplacement fiable.
  - tier: Adaptable
    description: Ventilateurs économiques. Vérifier le débit d'air (m³/h), le diamètre des pales et la connectique avant commande.
diagnostic:
  symptoms:
  - id: S1
    label: Surchauffe uniquement au ralenti ou en ville
    severity: confort
  - id: S2
    label: Ventilateur qui ne demarre jamais silence
    severity: confort
  - id: S3
    label: Bruit de roulement ou grincement au demarrage
    severity: confort
  - id: S4
    label: Pales de ventilateur fissurees ou cassees
    severity: confort
  - id: S5
    label: Odeur de plastique chaud pres du radiateur
    severity: confort
  - id: S6
    label: Clim moins efficace ventilateur partage
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : surchauffe uniquement au ralenti ou en ville'
  quick_checks:
  - 'Observer : surchauffe uniquement au ralenti ou en ville ?'
  - 'Observer : ventilateur qui ne demarre jamais silence ?'
  - Bruit de roulement ou grincement au demarrage ?
  - 'Observer : pales de ventilateur fissurees ou cassees ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Surchauffe uniquement au ralenti ou en ville
  - Ventilateur qui ne demarre jamais silence
  - Bruit de roulement ou grincement au demarrage
  - Pales de ventilateur fissurees ou cassees
  - Odeur de plastique chaud pres du radiateur
  - Clim moins efficace ventilateur partage
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '508'
  intro_title: A quoi sert Ventilateur de refroidissement ?
  risk_title: Pourquoi remplacer Ventilateur de refroidissement a temps ?
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
  - question: Ventilateur OE ou adaptable ?
    answer: Les ventilateurs OES (Valeo, Behr, Gates) offrent un débit d'air et une durabilité optimaux. Les adaptables peuvent
      être plus bruyants ou moins puissants.
  - question: Comment savoir si mon ventilateur est HS ?
    answer: Surchauffe au ralenti ou en embouteillage, ventilateur qui ne démarre pas moteur chaud, bruit de roulement, pales
      fissurées.
  - question: Tous les combien changer le ventilateur ?
    answer: Pas de périodicité. Le moteur électrique peut durer 200 000+ km. À remplacer si défaillant ou si le roulement
      grogne.
  - question: Peut-on tester le ventilateur facilement ?
    answer: Oui, pontez le relais ou branchez directement sur la batterie. S'il tourne, le problème est électrique (relais,
      sonde, câblage).
  - question: Quelle erreur éviter avec le ventilateur ?
    answer: Ne pas rouler sans ventilateur fonctionnel en ville. Vérifier que les pales ne touchent pas le carénage après
      montage.
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
doc_id: 3177b096-ba94-51a2-b27d-ae15de402eba
content_hash: sha256:cc5430f0d00d50e9
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
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  types_variants:
  - type: Ventilateur electrique
    description: Moteur electrique + helice, declenche par la sonde ou le calculateur
    era: standard
  - type: Ventilateur a viscocoupleur
    description: Entraine par courroie, embrayage visqueux module la vitesse selon temperature
    era: utilitaires, anciens vehicules
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le ventilateur de refroidissement est situé derrière leradiateur de
    refroidissement , il participe avec ce dernier au refroidissement dumoteur.
    Il achemine le flux d'air qui passe à travers ces lamelles. Il dissipeaussi
    la chaleur du radiateurmoteur lorsque le moteur tourne et le véhicule est à
    l'arrêt. Le ventilateurde refroidissement est constitué d'un petit moteur
    électrique qui assure larotation des pales, il produit le courant d'air qui
    va diminuer la températuredu liquide de refroidissement. Le fonctionnement
    du ventilateur de refroidissent estactionné par l'interrupteur de
    refroidissement. En savoir plus : ventilateur de refroidissement —
    définition et rôle mécanique 🚨 Bruit Ventilateur de refroidissement : causes
    et diagnostic
  S2: >-
    Pour savoir si le moteur duventilateur de refroidissement est en panne il
    faut contrôler son état de fonctionnement,en vérifiant son alimentation
    électrique : - Débranchez le fil d'alimentation du moteur de ventilateur. -
    Mettre une ampoule témoin entre le fil d'alimentation et la masse. - Si la
    lampe s'allume, cela signifie que l'alimentation du moteur estbonne mais que
    celui-ci est grillé. - Si l'ampoule reste éteinte, dans ce cas il faut
    contrôler le câblage ducircuit électrique peut être il est endommagé. -
    Contrôlez aussi l'état des fusibles. Diagnostic complet : identifier une
    panne de ventilateur de refroidissement
  S3: >-
    Le ventilateur de refroidissement force le passage de l'air à travers le
    radiateur lorsque le véhicule est à l'arrêt ou roule à faible vitesse (en
    dessous de 40-50 km/h, le flux d'air naturel est insuffisant). Un
    ventilateur défaillant provoque une surchauffe systématique en circulation
    urbaine ou en embouteillage, sans symptôme sur autoroute — ce qui retarde
    souvent le diagnostic. La sélection doit impérativement valider la puissance
    électrique, les dimensions et le sens de rotation. - Tension et puissance
    électrique du moteur — Les ventilateurs de refroidissement fonctionnent en
    12 V DC avec des puissances variant de 80 W à 400 W selon la taille du
    radiateur. Un moteur sous-puissant ne brassera pas assez d'air ; un moteur
    sur-puissant surchargera le relais ou le fusible haute intensité. Relevez la
    puissance en watts ou l'intensité en ampères sur l'étiquette du moteur
    original. - Nombre de pales et diamètre du rotor — Le diamètre du
    ventilateur (de 280 mm à 500 mm selon les véhicules) et le nombre de pales
    (5, 7 ou 9 pales selon l'optimisation acoustique) déterminent le débit
    d'air. Ces dimensions doivent correspondre exactement pour que le module
    rentre dans son logement. - Sens de rotation — Les ventilateurs fonctionnent
    soit en aspiration (air tiré depuis l'avant vers le radiateur), soit en
    soufflage (air poussé depuis le moteur vers le radiateur). Le sens de
    rotation est inversé entre les deux configurations et n'est pas corrigible
    par simple inversion de polarité sur les versions tripales. - Version moteur
    seul ou module complet avec motoventilateur — Sur les véhicules modernes
    (post-2000), le ventilateur est souvent livré en module complet avec son
    support, son shroud et parfois son relais intégré. Commander seulement le
    moteur électrique sans le support entraîne un problème de fixation. -
    Vitesse de rotation : une vitesse ou deux vitesses — Certains systèmes
    utilisent un ventilateur à deux vitesses (petite vitesse pour le moteur,
    grande vitesse pour la climatisation). Cette configuration utilise un
    branchement spécifique à 3 fils (+ commun, vitesse 1, vitesse 2). Un
    ventilateur à 2 fils ne peut pas reproduire cette fonction. - Compatibilité
    avec le circuit de climatisation — Sur les véhicules équipés de la clim, le
    même ventilateur refroidit simultanément le radiateur moteur et le
    condenseur de climatisation. Un débit insuffisant dégrade l'efficacité de la
    clim même si le moteur reste à température normale. Pour aller plus loin :
    consultez notre guide d'achat ventilateur de refroidissement — comparatif
    marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Ventilateur de
    refroidissement pour connaître les spécifications. - Arrêtez le moteur et le
    laissez refroidir. - Débranchez la batterie. - Localisez l'emplacement du
    ventilateur de refroidissement. - Démontez le connecteur du moteur de
    ventilateur. - Débranchez le connecteur de la sonde de refroidissement. -
    Desserrez les fixations du support ventilateur de refroidissement. - Retirez
    vers le haut le ventilateur de refroidissement complet (avec lemoteur
    électrique et le support).
  S4_REPOSE: >-
    La repose du ventilateur de refroidissement doit s'accompagner d'une
    vérification du circuit électrique de commande. Un ventilateur neuf qui ne
    se déclenche pas faute d'un relais défaillant ou d'une sonde de température
    hors service conduira à une surchauffe moteur malgré l'intervention. Testez
    toujours le déclenchement avant de refermer le compartiment moteur. -
    Vérifiez que le ventilateur de refroidissement neuf est identique à celui
    déposé : dimensions du support, nombre de pales, tension nominale du moteur
    électrique (12 V) et sens de rotation indiqué par la flèche sur le carénage.
    - Contrôlez le moteur électrique du ventilateur si vous avez opté pour un
    remplacement du groupe ventilateur complet. Si seul le moteur est remplacé,
    vérifiez la fixation des pales sur le moyeu et l'état des pattes de support.
    - Inspectez l'état de la sonde de refroidissement (sonde de déclenchement
    ventilateur, généralement verte ou bleue selon les marques) : une sonde à
    seuil décalé peut provoquer un déclenchement tardif du ventilateur et une
    surchauffe au ralenti, symptôme identique à un ventilateur défaillant. -
    Vérifiez l'état du relais de ventilateur dans le boîtier de fusibles : un
    relais qui accroche ou qui ne commute plus est la panne électrique la plus
    fréquente sur les groupes ventilateurs. Testez-le en pontant temporairement
    les bornes 30 et 87 du relais. - Positionnez le groupe ventilateur dans son
    logement en vérifiant l'orientation : le flux d'air doit être dirigé vers le
    radiateur (aspiration côté radiateur, soufflage côté moteur en configuration
    classique). - Serrez les fixations du support ventilateur uniformément.
    Vérifiez que les pattes de support ne sont pas fissurées : une patte cassée
    génère des vibrations qui détruisent le roulement du moteur électrique en
    quelques milliers de kilomètres. - Vérifiez le jeu entre les pales et le
    carénage sur tout le pourtour : le jeu doit être uniforme, sans aucun
    contact. Un frottement intermittent crée un bruit de roulement identique à
    un roulement défaillant et peut casser des pales à haute vitesse de
    rotation. - Reconnectez le connecteur du moteur électrique et le connecteur
    de la sonde de refroidissement jusqu'au déclic. Vérifiez que les fils ne
    sont pas coincés par le carénage ou les pattes de fixation. - Rebranchez la
    batterie. Sans démarrer le moteur, testez le ventilateur en pontant
    directement le relais ou en utilisant un outil de diagnostic pour activer le
    ventilateur par commande forcée. Il doit démarrer immédiatement et tourner
    sans bruit parasite. - Démarrez le moteur et laissez-le monter en
    température jusqu'au déclenchement automatique du ventilateur (généralement
    entre 90 °C et 100 °C selon les véhicules). Vérifiez que la température
    moteur reste stable sous la barre rouge après déclenchement.
  S5: >-
    Erreurs frequentes avec le ventilateur de refroidissement : - Ne pas
    verifier le relais et le fusible du ventilateur avant remplacement — ce sont
    les causes de panne les plus frequentes et les moins couteuses- Confondre un
    probleme de sonde de temperature avec un defaut de ventilateur — si la sonde
    ne transmet pas la bonne temperature, le ventilateur ne se declenche pas-
    Ignorer un ventilateur qui tourne en permanence moteur froid — signe de
    relais colle ou de sonde en court-circuit, surconsommation electrique et
    usure prematuree du moteur de ventilateur- Ne pas verifier l'etat du
    thermostat — un thermostat bloque ferme provoque une surchauffe meme avec un
    ventilateur fonctionnel- Oublier de rebrancher le connecteur de la sonde
    apres intervention sur le circuit de refroidissement — le ventilateur se met
    en securite et tourne en permanence
  S6: >-
    Après le remplacement d'un ventilateur de refroidissement, les vérifications
    portent sur le déclenchement électrique, la rotation libre du
    motoventilateur et l'efficacité du refroidissement en conditions statiques
    (ralenti et embouteillage). C'est dans ces conditions que la panne se
    manifestait, et c'est là que la réparation doit être confirmée. - Test de
    démarrage à froid du ventilateur : connecter le moteur du ventilateur
    directement à la batterie (12V) hors véhicule avant le montage pour
    confirmer qu'il tourne librement, sans bruit de roulement ni vibration. Un
    bruit métallique à vide signale un problème de fabrication à traiter avant
    montage. - Vérification du sens de rotation : s'assurer avant le montage que
    les pales brassent l'air en direction du radiateur (aspiration côté moteur)
    et non à l'inverse. Un ventilateur monté à l'envers souffle l'air dans le
    mauvais sens et aggrave la surchauffe en conditions statiques. - Test de
    déclenchement électrique : après montage, mettre le contact et attendre que
    le moteur monte en température jusqu'à 90-95°C. Le ventilateur doit se
    déclencher automatiquement via le manocontact ou la sonde de température
    dédiée. S'il ne se déclenche pas, vérifier le fusible de puissance du
    ventilateur (généralement 20 à 40A) et le relais associé. - Contrôle de
    l'absence de bruit de rotation : ventilateur tournant sous le capot, aucun
    bruit de frottement des pales sur le carter de protection ni grincement de
    roulement ne doit être perceptible. Un bruit en rotation indique un jeu
    excessif dû à un mauvais positionnement du motoventilateur dans son support.
    - Test d'efficacité en conditions réelles : effectuer un trajet en
    circulation urbaine dense (arrêts fréquents, ralenti prolongé) et surveiller
    l'aiguille de température. Celle-ci doit rester stable dans la zone normale,
    confirmant que le ventilateur assure correctement le refroidissement sans
    apport de vitesse du véhicule. - Vérification de la climatisation couplée :
    si le véhicule est équipé de la climatisation et que le ventilateur assure
    aussi le refroidissement du condenseur, activer la clim et vérifier qu'elle
    reste efficace — un ventilateur sous-dimensionné ou monté dans le mauvais
    sens dégraderait les performances de la climatisation. - Inspection des
    fixations et connecteur électrique : après les premiers cycles chaud/froid,
    contrôler que les vis de fixation du support du motoventilateur n'ont pas
    vibré et que le connecteur électrique est bien verrouillé dans son clip de
    maintien sur le faisceau.
  S7: >-
    Quel est le prix d'un ventilateur de refroidissement ?Le prix varie selon le
    véhicule et la marque. Utilisez notre sélecteur pour trouver le ventilateur
    de refroidissement compatible avec votre véhicule et comparer les tarifs des
    différents équipementiers.Comment savoir si mon ventilateur de
    refroidissement est à changer ?Les signes d'usure les plus courants sont
    détaillés dans la section diagnostic ci-dessus. En cas de doute, faites
    contrôler la pièce par un professionnel.Peut-on rouler avec un ventilateur
    de refroidissement défaillant ?Cela dépend de la gravité du
    dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l'urgence du remplacement.-
    Moteur électrique de ventilateur . - Sonde de refroidissement. 📖 Fiche
    technique Ventilateur de refroidissement — intervalles et spécifications
    d’entretien.
  S8: >-
    Comment choisir Ventilateur de refroidissement compatible avec mon
    vehiculeRenseignez marque, modele, type moteur et annee, puis verifiez la
    reference Quand remplacer Ventilateur de refroidissement ?En cas de
    surchauffe uniquement au ralenti ou en ville ou de degradation Puis-je
    monter Ventilateur de refroidissement sans verification atelierLe montage
    peut exiger controles de couple, alignement et references.
  META: >-
    {"meta_title":"Ventilateur refroidissement : quand changer ? |
    AutoMecanik","meta_description":"Surchauffe au ralenti, ventilateur
    silencieux ou pales fissurées ? Motoventilateur défaillant. Guide symptômes,
    diagnostic et compatibilité par véhicule."}
---

# Ventilateur de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Forcer le passage de l'air a travers le radiateur quand le vehicule est a l'arret ou a faible vitesse

**Actions principales:** forcer, ventiler, refroidir, brasser l'air

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de roulement ou grincement au demarrage**
  bruit de roulement ou grincement au demarrage
- **Pales de ventilateur fissurees ou cassees**
  pales de ventilateur fissurees ou cassees

### 🟢 Autres Symptômes

- surchauffe uniquement au ralenti ou en ville
- ventilateur qui ne demarre jamais silence
- odeur de plastique chaud pres du radiateur
- clim moins efficace ventilateur partage

## Procédure de Diagnostic

Pour diagnostiquer un problème de ventilateur de refroidissement:

1. **Inspection visuelle** - Examiner l'état du ventilateur de refroidissement
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

- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- vase-d-expansion
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon ventilateur de refroidissement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "evite la casse moteur"

## FAQ

**Ventilateur OE ou adaptable ?**
Les ventilateurs OES (Valeo, Behr, Gates) offrent un débit d'air et une durabilité optimaux. Les adaptables peuvent être plus bruyants ou moins puissants.

**Comment savoir si mon ventilateur est HS ?**
Surchauffe au ralenti ou en embouteillage, ventilateur qui ne démarre pas moteur chaud, bruit de roulement, pales fissurées.

**Tous les combien changer le ventilateur ?**
Pas de périodicité. Le moteur électrique peut durer 200 000+ km. À remplacer si défaillant ou si le roulement grogne.

**Peut-on tester le ventilateur facilement ?**
Oui, pontez le relais ou branchez directement sur la batterie. S'il tourne, le problème est électrique (relais, sonde, câblage).

**Quelle erreur éviter avec le ventilateur ?**
Ne pas rouler sans ventilateur fonctionnel en ville. Vérifier que les pales ne touchent pas le carénage après montage.


## Symptomes supplementaires

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
