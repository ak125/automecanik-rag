---
category: climatisation
slug: detendeur-de-climatisation
title: Détendeur de climatisation
pg_id: 183
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
  role: Détend le fluide frigorigène avant l'évaporateur
  must_be_true:
  - detendre
  - reguler
  - abaisser la pression
  must_not_contain:
  - injection
  - freinage
  - allumage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - compresseur-de-climatisation
  - condenseur-de-climatisation
  - evaporateur-de-climatisation
  - filtre-d-habitacle
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
  - ❌ "refroidit le moteur"
  cost_range:
    min: 50
    max: 150
    currency: EUR
    unit: détendeur
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: Pièce identique à celle montée en usine, avec la même plage de régulation et les mêmes raccords. Recommandé
      pour les véhicules récents ou les climatisations sous garantie.
  - tier: Équivalent OE (équipementiers climatisation)
    description: Produit de fabricants spécialisés en composants de climatisation automobile. Tolérances identiques, compatible
      avec les fluides R134a et R1234yf selon modèle.
  - tier: Pièce adaptable
    description: Peut convenir sur des véhicules plus anciens. La compatibilité avec le type de fluide, la position de montage
      et le débit nominal doit être vérifiée avant commande.
  brands:
    premium:
    - Denso
    - Valeo
    standard:
    - NRF
    - Delphi
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Evaporateur qui givre anormalement
    severity: confort
  - id: S2
    label: Refroidissement irregulier chaud puis froid
    severity: confort
  - id: S3
    label: Sifflement ou bruit de detente audible
    severity: confort
  - id: S4
    label: Compresseur qui cycle en permanence
    severity: confort
  - id: S5
    label: Odeur de gaz refrigerant dans l habitacle
    severity: confort
  - id: S6
    label: Clim qui fonctionne puis s arrete brusquement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : evaporateur qui givre anormalement'
  quick_checks:
  - 'Observer : evaporateur qui givre anormalement ?'
  - 'Observer : refroidissement irregulier chaud puis froid ?'
  - 'Observer : sifflement ou bruit de detente audible ?'
  - 'Observer : compresseur qui cycle en permanence ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Evaporateur qui givre anormalement
  - Refroidissement irregulier chaud puis froid
  - Sifflement ou bruit de detente audible
  - Compresseur qui cycle en permanence
  - Odeur de gaz refrigerant dans l habitacle
  - Clim qui fonctionne puis s arrete brusquement
  good_practices:
  - Faire tourner la climatisation 10 min par semaine meme en hiver
  - Remplacement du filtre d habitacle chaque annee
  - Recharge de gaz par un professionnel equipe (circuit sous pression)
  - Controle d etancheite si baisse de performance
rendering:
  pgId: '183'
  intro_title: A quoi sert Détendeur de climatisation ?
  risk_title: Pourquoi remplacer Détendeur de climatisation a temps ?
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
  - question: Détendeur clim OE ou adaptable ?
    answer: Les détendeurs OES (Valeo, Denso) garantissent un débit calibré. Un détendeur mal calibré peut provoquer un givrage
      de l'évaporateur.
  - question: Comment savoir si le détendeur est HS ?
    answer: Clim qui givre puis s'arrête, refroidissement irrégulier (chaud/froid), sifflement au niveau du détendeur, évaporateur
      partiellement givré.
  - question: Tous les combien changer le détendeur ?
    answer: Pas de périodicité. Pièce rarement en panne sauf obstruction par impuretés. Changez-le si diagnostic confirmé.
  - question: Peut-on changer le détendeur soi-même ?
    answer: Possible mais nécessite la récupération du gaz et une recharge. L'accès est souvent difficile (boîtier de ventilation).
  - question: Quelle erreur éviter avec le détendeur ?
    answer: Ne pas confondre un détendeur bouché avec un manque de gaz. Vérifier la pression HP et BP avant remplacement.
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
doc_id: ec1fed8c-3160-574f-af9d-559487c84df9
content_hash: sha256:81fad23642f8f8fa
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
  area: Face avant (condenseur), habitacle (evaporateur), moteur (compresseur)
  access: Variable selon composant (capot, tableau de bord, face avant)
  adjacent_parts:
  - compresseur
  - condenseur
  - detendeur
  - evaporateur
installation:
  difficulty: difficile (pro obligatoire)
  time: 1h a 4h
  tools:
  - station de recharge
  - detecteur de fuites
  - cle a douille
  prerequisite: Recuperation du gaz obligatoire par professionnel agree
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_1_v: '1 V'
    val_1__c: '1 °C'
    val_1_5__c: '1,5 °C'
    val_10__: '10 %'
    val_10_a: '10 a'
    val_100__: '100 %'
    val_100_kw: '100 kW'
    val_100_kg: '100 kg'
    val_100_km: '100 km'
    val_11_a: '11 a'
    val_12_kw: '12 kW'
    val_12__c: '12 °C'
    val_17_a: '17 a'
    val_18_a: '18 a'
    val_19__c: '19 °C'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le détendeur de climatisation est sous la forme d'un petitboîtier, il est
    situé sur l'évaporateur de climatisation. Le détendeur de climatisation va
    contrôlerl'entrée et la sortie du fluide frigorifique. Il va permettre de
    chuter lapression et la température du fluide frigorigène.Il permet aussi de
    réguler le débit de fluide qui entre dansl'évaporateur de climatisation. La
    régulation s'effectue à l'aide de la température du fluiderevenant de
    l'évaporateur de climatisation. Cette température va faire varier la
    pression dufluide se trouvant dans la tête thermostatique et ainsi ouvrir ou
    fermerlégèrement le détendeur de climatisation. Ce fonctionnement permet
    d'éviter d'envoyer trop defluide dans l'évaporateur de climatisation, ce qui
    aurait pour conséquence de voir arriver aucompresseur le fluide frigorigène
    sous mélange liquide/gaz et ainsi d'endommagervoire de gripper le
    compresseur de climatisation . En savoir plus : détendeur de climatisation —
    définition et rôle mécanique 🚨 Bruit Détendeur de climatisation : causes et
    diagnostic
  S2: >-
    Un détendeur de climatisation défectueuxprésente plusieurs symptômes : - Le
    compresseur de climatisation s'éteint périodiquement. - Instabilité dans le
    fonctionnement du système de refroidissement. - La pression de tête et celle
    d'aspiration sont inférieures à la norme. - La présence d'une importante
    quantité de réfrigérant qui rentre dansl'évaporateur de climatisation. -
    Lors d'un contrôle visuel vous remarquez que les conduites de
    climatisationet l'évaporateur de climatisation sont couverts de glace. -
    L'air froid souffle régulièrement dans l'habitacle. Diagnostic complet :
    identifier une panne de détendeur de climatisation
  S3: >-
    Le détendeur de climatisation régule le débit de fluide frigorigène entre la
    haute et la basse pression en aval du condenseur, juste avant l'évaporateur.
    Sa défaillance — blocage en position fermée ou ouverte — provoque soit un
    givrage de l'évaporateur (détendeur trop ouvert), soit une absence de froid
    total (détendeur bloqué fermé). Il existe deux technologies principales : le
    détendeur à tube orifice (calibré fixe) et le détendeur thermostatique (à
    aiguille réglable par thermostat intégré). Ces deux types ne sont pas
    interchangeables. Voici les critères à maîtriser avant commande. - Type de
    détendeur : tube orifice fixe ou détendeur thermostatique (TXV) — Le tube
    orifice est un calibre fixe sans pièce mobile, identifiable par son marquage
    coloré (couleur = débit calibré). Le détendeur thermostatique possède une
    aiguille pilotée par la température de sortie de l'évaporateur. Identifier
    le type présent sur le véhicule avant commande : les deux sont montés sur
    des circuits de conception différente. - Compatibilité fluide R134a ou
    R1234yf — Les détendeurs contiennent des joints et des éléments calibrés
    pour des plages de pression spécifiques à chaque fluide. Un détendeur R134a
    monté sur circuit R1234yf présente des risques de fuite et une calibration
    de débit incorrecte (pressions de service différentes de 15 à 25 %). - Débit
    nominal et calibre (pour tube orifice) — Le débit calibré est indiqué par la
    couleur du tube orifice (code couleur universel : beige, jaune, vert, orange
    selon débit croissant). Un tube de débit supérieur entraîne un sous-
    refroidissement de l'évaporateur et une surcharge du compresseur ; un débit
    insuffisant prive l'habitacle de froid. - Pression d'ouverture et surchauffe
    cible (pour détendeur TXV) — Le détendeur thermostatique est calibré pour
    une surchauffe (superheat) de sortie d'évaporateur, typiquement 5 à 10 °C.
    Cette valeur est gravée ou marquée sur le corps du détendeur. Un TXV avec
    une surchauffe mal calibrée provoque un givrage intermittent ou une
    compétition entre le détendeur et le pressostat. - Raccords et orientation
    de montage — Le détendeur s'interpose entre la ligne liquide et l'entrée de
    l'évaporateur. La position de la sonde de température (pour les TXV) doit
    être en contact direct avec la tubulure de sortie de l'évaporateur. Une
    mauvaise orientation empêche le régulateur de lire la bonne température. -
    Pièces à remplacer simultanément — Lors de l'ouverture du circuit pour
    remplacer le détendeur, la bouteille déshydratante doit être changée.
    Contrôler également l'évaporateur pour détecter d'éventuelles traces de
    corrosion ou de micro-fuites. Remettre sous vide le circuit pendant au
    minimum 45 minutes avant recharge en gaz. Pour aller plus loin : consultez
    notre guide d'achat détendeur de climatisation — comparatif marques,
    critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Détendeur de climatisation
    pour connaître les spécifications. Note : pour leremplacement de
    l'évaporateur de climatisation il doit être fait par un professionnel si non
    ilfaut se référé à la revue technique de vote voiture. - Débranchez la
    batterie. - Vidangez le liquide de climatisation. - Démontez le collecteur
    d'admission. - Démontez la vis de fixation de la platine de maintien des
    canalisations declimatisation. - Démontez les écrous de fixation des
    canalisations sur le détendeur declimatisation. - Démontez les canalisations
    du détendeur de climatisation et faire attention de ne pas lesdéformer. -
    Obturez les canalisations du liquide de climatisation. - Démontez la platine
    du détendeur de climatisation. - Démontez les joints des canalisations de
    climatisation sur le détendeur de climatisation. - Démontez la vis de
    fixation du détendeur de climatisation. - Mettre en place une tige filetée
    sur le détendeur de climatisation. - Démontez la deuxième vis de fixation du
    détendeur de climatisation. - Mettre en place une deuxième tige sur le
    détendeur de climatisation. - Démontez le détendeur de climatisation à
    l'aide des tiges de démontage. - Démontez le joint du détendeur de
    climatisation. Note : dans certain véhicule il faut démontezl'évaporateur de
    climatisation pour avoir accès au détendeur de climatisation.
  S4_REPOSE: >-
    Le remontage du détendeur de climatisation nécessite impérativement de
    remplacer tous les joints toriques et d'utiliser de l'huile PAG compatible
    avec le fluide frigorigène de votre circuit. Toute fuite sur les raccords
    impose une recharge complète du circuit, une opération réglementée qui ne
    peut être réalisée que par un technicien habilité avec un groupe de charge.
    - Vérifiez que le détendeur neuf est identique à celui déposé : mêmes cotes
    de raccordement, même type (tube d'orifice ou à pointeau thermostatique
    selon le véhicule). - Contrôlez l'état de l'évaporateur de climatisation et
    du compresseur avant de refermer le circuit : un évaporateur perforé ou un
    compresseur défaillant annulerait le travail de remplacement. - Enduisez les
    joints toriques neufs d'huile PAG adaptée au type de réfrigérant (R134a ou
    R1234yf selon le véhicule). Ne réutilisez jamais les anciens joints
    toriques. - Remontez le détendeur dans son logement. Orientez la sonde de
    température correctement si le détendeur est à capsule thermostatique
    (respectez le marquage constructeur). - Remontez la platine de maintien du
    détendeur et serrez ses vis de fixation sans excès pour ne pas écraser les
    joints. - Reconnectez les canalisations du circuit de climatisation sur le
    détendeur. Serrez les écrous de raccord au couple préconisé (généralement 15
    à 20 N·m selon le diamètre). - Remontez la vis de fixation de la platine de
    maintien des canalisations, puis les pièces de compartiment moteur déposées
    lors de l'accès. - Rebranchez la batterie (borne positive en premier). -
    Faites recharger le circuit de climatisation par un professionnel habilité
    avec le fluide frigorigène et l'huile préconisés pour votre véhicule.
    Contrôlez les pressions HP et BP pour vérifier le bon calibrage du
    détendeur. - Vérifiez l'absence de fuite réfrigérante avec un détecteur
    électronique et contrôlez l'efficacité de refroidissement de la
    climatisation en roulant. ✅ Après remontage, vérifiez les spécifications
    dans la fiche technique Détendeur de climatisation.
  S5: >-
    Erreurs frequentes avec le detendeur de climatisation : - Ne pas faire le
    vide du circuit avant recharge apres remplacement — l'air et l'humidite
    residuels provoquent des surpressions et degradent le compresseur- Oublier
    de remplacer les joints toriques du detendeur — les anciens joints durcis
    fuient immediatement avec le refrigerant sous pression- Ne pas verifier
    l'etat de l'evaporateur lors du remplacement du detendeur — un evaporateur
    bouche ou perce rend le nouveau detendeur inefficace- Confondre detendeur a
    orifice fixe et detendeur thermostatique — les deux types ne sont pas
    interchangeables et les references different selon le vehicule- Ignorer un
    compresseur qui s'enclenche et se decouple en boucle — signe classique de
    detendeur bloque ou de charge de refrigerant incorrecte- Ne pas respecter la
    quantite exacte de refrigerant specifiee par le constructeur — une surcharge
    endommage le compresseur, une sous-charge reduit le refroidissement
  S6: >-
    Le détendeur régule la pression du fluide frigorigène entre la haute
    pression (côté condenseur) et la basse pression (côté évaporateur). Après
    son remplacement, le circuit doit être mis sous vide et rechargé. Les
    contrôles suivants valident le bon fonctionnement de la détente dans les
    conditions réelles de conduite. - Vérifier l'étanchéité après recharge du
    circuit : utiliser un détecteur de fuite électronique ou un traceur
    fluorescent UV pour inspecter les raccords du détendeur, situés entre la
    sortie du condenseur (côté liquide) et l'entrée de l'évaporateur. Les joints
    toriques neufs doivent être légèrement enduits d'huile PAG avant montage. -
    Contrôler les pressions basse et haute en régime stabilisé : après 10
    minutes de fonctionnement à régime stabilisé, la pression basse côté
    évaporateur doit être comprise entre 1,5 et 2,5 bar, et la haute pression
    entre 14 et 20 bar à 20-25 °C ambiants. Une basse pression inférieure à 1
    bar indique un détendeur trop fermé (givrage évaporateur probable). -
    Contrôler l'absence de givrage sur l'évaporateur : un détendeur mal calibré
    ou coincé en position fermée provoque un givrage rapide de l'évaporateur. Si
    la soufflerie perd en débit d'air froid après 5 à 10 minutes de
    fonctionnement, inspecter l'évaporateur depuis l'habitacle : un bloc de
    glace signale un problème de détente. - Tester la stabilité de la pression
    basse pendant un cycle complet : la pression basse ne doit pas osciller de
    plus de ±0,5 bar en régime stabilisé. Des oscillations rapides (plus d'un
    cycle par seconde) indiquent un détendeur qui chasse et signalent un
    problème de calibration ou une pièce défectueuse. - Vérifier l'absence de
    sifflement audible : un léger bruit de détente à l'entrée de l'évaporateur
    est normal. Un sifflement aigu et persistant, notamment à l'enclenchement de
    la climatisation, signale un débit de fluide excessif dû à un détendeur trop
    ouvert. - Contrôler l'efficacité de refroidissement en cabine : fenêtres
    fermées avec le ventilateur à puissance maximale, la température de
    soufflage doit descendre sous 10 °C en 5 minutes à 20-25 °C ambiants. Un
    détendeur correctement posé restaure les performances d'origine du circuit.
  S7: >-
    Quel est le prix d'un détendeur de climatisation ?Le prix varie selon le
    véhicule et la marque. Utilisez notre sélecteur pour trouver le détendeur de
    climatisation compatible avec votre véhicule et comparer les tarifs des
    différents équipementiers.Comment savoir si mon détendeur de climatisation
    est à changer ?Les signes d'usure les plus courants sont détaillés dans la
    section diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par
    un professionnel.Peut-on rouler avec un détendeur de climatisation
    défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la
    pièce dans la sécurité du véhicule. Consultez la section symptômes pour
    évaluer l'urgence du remplacement.- detendre - reguler - abaisser la
    pression
  S8: >-
    Comment choisir Détendeur de climatisation compatible avec mon
    vehiculeRenseignez marque, modele, type moteur et annee, puis verifiez la
    reference Quand remplacer Détendeur de climatisation ?En cas de evaporateur
    qui givre anormalement ou de degradation mesurable, Puis-je monter Détendeur
    de climatisation sans verification atelierLe montage peut exiger controles
    de couple, alignement et references.
  META: >-
    {"meta_title":"Détendeur clim : givrage, quand changer |
    AutoMecanik","meta_description":"Évaporateur qui givre, refroidissement
    irrégulier ou compresseur qui cycle en permanence ? Apprenez à diagnostiquer
    un détendeur de climatisation défaillant et choisir la bonne
    pièce.","robots":"index,follow","og_type":"article","schema_type":"HowTo"}
---

# Détendeur de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Détend le fluide frigorigène avant l'évaporateur

**Actions principales:** detendre, reguler, abaisser la pression

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- evaporateur qui givre anormalement
- refroidissement irregulier chaud puis froid
- sifflement ou bruit de detente audible
- compresseur qui cycle en permanence
- odeur de gaz refrigerant dans l habitacle
- clim qui fonctionne puis s arrete brusquement

## Procédure de Diagnostic

Pour diagnostiquer un problème de détendeur de climatisation:

1. **Inspection visuelle** - Examiner l'état du détendeur de climatisation
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

- bouteille-deshydratante
- commande-de-ventilation
- compresseur-de-climatisation
- condenseur-de-climatisation
- evaporateur-de-climatisation
- filtre-d-habitacle

## Critères de Compatibilité

Pour commander le bon détendeur de climatisation, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit le moteur"

## FAQ

**Détendeur clim OE ou adaptable ?**
Les détendeurs OES (Valeo, Denso) garantissent un débit calibré. Un détendeur mal calibré peut provoquer un givrage de l'évaporateur.

**Comment savoir si le détendeur est HS ?**
Clim qui givre puis s'arrête, refroidissement irrégulier (chaud/froid), sifflement au niveau du détendeur, évaporateur partiellement givré.

**Tous les combien changer le détendeur ?**
Pas de périodicité. Pièce rarement en panne sauf obstruction par impuretés. Changez-le si diagnostic confirmé.

**Peut-on changer le détendeur soi-même ?**
Possible mais nécessite la récupération du gaz et une recharge. L'accès est souvent difficile (boîtier de ventilation).

**Quelle erreur éviter avec le détendeur ?**
Ne pas confondre un détendeur bouché avec un manque de gaz. Vérifier la pression HP et BP avant remplacement.
