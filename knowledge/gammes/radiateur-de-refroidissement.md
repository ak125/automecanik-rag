---
category: refroidissement
slug: radiateur-de-refroidissement
title: Radiateur de refroidissement
pg_id: 470
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
  role: Dissiper la chaleur du liquide de refroidissement vers l'air exterieur
  must_be_true:
  - dissiper
  - echanger
  - refroidir
  must_not_contain:
  - chauffage
  - habitacle
  - huile
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - pompe-a-eau
  - thermostat
  - durite-de-refroidissement
  - vase-d-expansion
  - ventilateur-de-refroidissement
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
    min: 62
    max: 218
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE (OES)
  - tier: Adaptable qualite
  - tier: Reconditionne
  - tier: Echange standard
  brands:
    premium:
    - Behr/Mahle
    - Gates
    standard:
    - Valeo
    - NRF
    - Febi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Flaque de liquide colore sous l avant
    severity: confort
  - id: S2
    label: Traces de corrosion sur les tubes du radiateur
    severity: confort
  - id: S3
    label: Sifflement d air ou de vapeur a l avant
    severity: confort
  - id: S4
    label: Surchauffe au ralenti ou en embouteillage
    severity: confort
  - id: S5
    label: Odeur de liquide de refroidissement chaud
    severity: confort
  - id: S6
    label: Radiateur visiblement deforme ou perce
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  depose_steps: []
  quick_checks:
  - 'Observer : flaque de liquide colore sous l avant ?'
  - 'Observer : traces de corrosion sur les tubes du radiateur ?'
  - 'Observer : sifflement d air ou de vapeur a l avant ?'
  - 'Observer : surchauffe au ralenti ou en embouteillage ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Flaque de liquide colore sous l avant
  - Traces de corrosion sur les tubes du radiateur
  - Sifflement d air ou de vapeur a l avant
  - Surchauffe au ralenti ou en embouteillage
  - Odeur de liquide de refroidissement chaud
  - Radiateur visiblement deforme ou perce
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '470'
  intro_title: A quoi sert Radiateur de refroidissement ?
  risk_title: Pourquoi remplacer Radiateur de refroidissement a temps ?
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
  - question: Radiateur OE ou adaptable ?
    answer: Les radiateurs OES (Valeo, Behr/Mahle, Nissens) garantissent un refroidissement optimal. Les adaptables moins
      chers peuvent avoir un rendement inférieur.
  - question: Comment savoir si mon radiateur fuit ?
    answer: Flaque de liquide sous l'avant du véhicule, niveau qui baisse, traces vertes/roses sur le radiateur, surchauffe
      au ralenti prolongé.
  - question: Tous les combien changer le radiateur ?
    answer: Pas de périodicité. À remplacer si fuite, si bouché (surchauffe) ou si endommagé par un choc.
  - question: Peut-on réparer un radiateur percé ?
    answer: Une réparation provisoire (résine, soudure) est possible mais temporaire. Le remplacement reste la solution fiable.
  - question: Quelle erreur éviter avec le radiateur ?
    answer: Ne pas monter un radiateur sans remplacer le liquide de refroidissement. Vérifier l'état des supports et des durites
      adjacentes.
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
doc_id: 6992b1dd-582f-5d32-86f7-fb08e7ea8f3a
content_hash: sha256:ad6ca200cdbb9f3a
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
  _source: denso-am.eu + fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 2
  _has_tech_data: true
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_0_5_bar: '0,5 bar'
    val_1_bar: '1 bar'
    val_100__c: '100 °C'
    val_110__c: '110 °C'
    val_20__c: '20 °C'
    val_30__c: '30 °C'
    val_480__c: '480 °C'
    val_500__c: '500 °C'
    val_560__c: '560 °C'
    val_60__c: '60 °C'
    val_80__c: '80 °C'
    val_90__c: '90 °C'
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le radiateur de refroidissement refroidis le liquide derefroidissement en
    dissipant la chaleur du liquide en provenance du moteur afinde réguler la
    température de ce dernier. Le liquide de refroidissement est pompé en
    continu par lapompe à eau , à travers le circuit de refroidissement et le
    radiateur moteur secharge de maintenir la température du moteur dans une
    moyenne de 90°C. Pour assurer le refroidissement du moteur, le ventilateur
    de refroidissement électrique se déclenche automatiquement par le contacteur
    de la sonde de température de refroidissement dés que la température initial
    est dépassée, même quand le véhicule est à l'arrêt et que le moteur tourne
    au ralentie. En savoir plus : radiateur de refroidissement — définition et
    rôle mécanique 🚨 Bruit Radiateur de refroidissement : causes et diagnostic
  S2: >-
    Le radiateur de refroidissement doit être contrôlé et remplacé sinécessaire
    dès que vous constatez les symptômes suivants : - Surchauffedu moteur. -
    Fuites de liquide de refroidissement au niveau du radiateur. - En cas de
    déformation du radiateur suite à un accident (choc frontal). - Leradiateur
    est froid d'un côté et chaud de l'autre côté. Si le radiateur
    derefroidissement défaillant n'est pas remplacée, le refroidissement du
    moteurne sera plus assurée ce qui va produire une surchauffe du moteur
    (joint deculasse à long terme casse moteur). Diagnostic complet : identifier
    une panne de radiateur de refroidissement
  S3: >-
    Le radiateur de refroidissement dissipe vers l'air extérieur la chaleur
    absorbée par le liquide de refroidissement au contact du bloc moteur. Sa
    capacité d'échange thermique doit être calibrée pour le moteur spécifique du
    véhicule : un radiateur sous-dimensionné provoque une surchauffe chronique
    en embouteillage ou en côte, tandis qu'un radiateur surdimensionné peut
    retarder la montée en température et pénaliser les émissions en phase de
    démarrage à froid. - Dimensions hors-tout et superficie d'échange — La
    largeur, la hauteur et l'épaisseur du radiateur (généralement 30 à 60 mm)
    sont déterminées par l'espace disponible dans la baie moteur. Mesurer
    l'encombrement de l'original avant toute commande, car des différences de 10
    mm sur la hauteur modifient le positionnement des fixations. - Nombre de
    rangées et type de cœur — Les radiateurs à 1 ou 2 rangées de tubes aluminium
    conviennent aux motorisations standards. Les moteurs diesel à forte
    cylindrée ou suralimentés nécessitent des radiateurs à 2 ou 3 rangées pour
    dissiper un flux thermique supérieur. Ne pas monter un radiateur mono-rangée
    à la place d'un birangée d'origine. - Diamètre et positionnement des
    raccords de durites — Les raccords sont de diamètre 28, 32, 36 ou 40 mm
    selon le moteur. Leur position (haut droit, bas gauche, ou configuration
    spécifique) doit correspondre au circuit existant sans modifier la longueur
    des durites. Vérifier la position de la sortie du vase d'expansion. -
    Présence et emplacement des prises de refroidissement boîte auto — Les
    véhicules équipés d'une boîte automatique disposent de raccords
    supplémentaires sur le bas du radiateur pour le refroidissement du liquide
    de transmission. Ces raccords sont absents sur les radiateurs destinés aux
    boîtes manuelles : commander impérativement la version adaptée à la
    transmission. - Type de fixation et pattes de montage — Les pattes de
    fixation en aluminium ou plastique renforcé doivent correspondre aux plots
    de caoutchouc anti-vibration du châssis. Un radiateur avec pattes décalées
    de 5 mm impose des alésages supplémentaires dans le tablier. - Matériau du
    cœur et compatibilité avec le liquide de refroidissement — Les radiateurs
    tout-aluminium sont compatibles avec les liquides OAT (Organic Acid
    Technology, rosâtre ou orangé) et HOAT. Les anciens radiateurs cuivre-laiton
    exigent des liquides IAT (vert). Vérifier la nature du liquide de
    refroidissement en circulation pour éviter les réactions électrolytiques. -
    Contrôle simultané du thermostat et des durites — Un radiateur neuf sur un
    circuit avec thermostat collé ouvert ou fermé ne résoudra pas la surchauffe.
    Contrôler le thermostat (température d'ouverture 82 °C à 92 °C selon le
    moteur) et l'état des durites (rigidité, fissures) lors de tout remplacement
    de radiateur. Pour aller plus loin : consultez notre guide d'achat radiateur
    de refroidissement — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Radiateur de
    refroidissement pour connaître les spécifications. - Arrêtez le moteur et
    lelaisser refroidir. - Ouvrez le bouchon du vase d'expansion . - Levez et
    calez le véhicule. - Vidangez le liquide de refroidissement. - Démontez les
    différentescanalisations du radiateur moteur. - Démontez la sonde de
    température si équipé. - Dégager l'accès au radiateur moteur si dans
    ledémontage vous auriez besoin de démonter autre pièce (pare-choc,
    traversesetc.). - Démontez les différentes fixations du radiateur
    derefroidissement. - Démontez le radiateur de refroidissement.
  S4_REPOSE: >-
    Note :Généralement les purgeurs ou les vis de purge sont situés : - sur le
    radiateur moteur. - sur une durite haute. - sur le thermostat . - Ouvrez la
    vis de purges. - Remplissez le circuit derefroidissement par la quantité du
    liquide préconisé par le constructeur (cetteinformation vous pouvez la
    trouver dans la notice d'utilisation de votrevéhicule). - Laissez le liquide
    derefroidissement s'écouler jusqu'à qu'il sort sans bulle d'air. - Fermez la
    vis de purge. - Démarrez le moteur. - Laissez le moteur tournerau ralenti et
    contrôlez l'évacuation des bulles d'air du circuit derefroidissement. -
    Contrôlez le niveau duliquide de refroidissement et le corrigez si
    nécessaire. - Laissez tourner le moteur jusqu'à enclenchement duventilateur
    de refroidissement. - Ouvrir le bouchon du vased'expansion après l'arrêt du
    ventilateur de refroidissement pour laisser échapper la pression. -
    Contrôlez le niveau du liquide derefroidissement et le corrigez si
    nécessaire. - Arrêtez le moteur et lelaissez refroidir. - Contrôlez le
    niveau deliquide de refroidissement. ✅ Après remontage, vérifiez les
    spécifications dans la fiche technique Radiateur de refroidissement.
  S5: >-
    Erreurs frequentes avec le radiateur de refroidissement : - Ne pas verifier
    l'etat du thermostat lors du remplacement du radiateur — un thermostat
    bloque ferme provoque une surchauffe meme avec un radiateur neuf- Oublier de
    remplacer les durites fragiles lors du demontage — une durite craquelée fuit
    sous pression apres le remontage- Ne pas purger correctement le circuit
    apres remplacement — une bulle d'air bloque la circulation et provoque des
    points chauds- Confondre radiateur de refroidissement moteur et radiateur de
    chauffage — ce sont deux pieces distinctes avec des emplacements differents-
    Ne pas verifier les fixations et silent-blocs du radiateur — un radiateur
    mal fixe vibre et les raccords finissent par fuir- Ignorer une legere tache
    de liquide vert/rose sous le vehicule — signe de micro-fuite au radiateur,
    la surchauffe est a venir
  S6: >-
    Le radiateur de refroidissement est le composant central du circuit
    thermique moteur. Son remplacement impose une purge soignée et une série de
    contrôles sur les deux premières heures de fonctionnement, car une
    défaillance post-montage peut conduire rapidement à une surchauffe moteur
    irréversible. - Purge complète du circuit de refroidissement : remplir le
    circuit avec un mélange eau déminéralisée / antigel à 50 % (protection
    jusqu'à -35 °C), ouvrir les vis de purge, et laisser tourner le moteur
    jusqu'à la mise en route du ventilateur électrique (environ 95-100 °C).
    Répéter le niveau deux fois à froid pour éliminer toutes les bulles d'air
    résiduelles. - Absence de fuite au niveau des connections latérales :
    inspecter les deux renforts latéraux du radiateur (boîtes à eau en
    plastique) aux points de raccordement des durites haute et basse. Une trace
    blanche calcaire ou une buée persistante signale une micro-fuite à traiter
    immédiatement avant de circuler. - Contrôle de l'absence de surchauffe au
    ralenti et en embouteillage : après 20 minutes de fonctionnement, la jauge
    de température du tableau de bord doit se stabiliser à mi-cadran (environ 90
    °C). Toute tendance à monter vers les 3/4 de cadran ou au-delà indique que
    le ventilateur de refroidissement ne s'enclenche pas ou que la purge est
    incomplète. - Vérification du bouchon de radiateur : si le bouchon de
    radiateur n'a pas été remplacé simultanément, tester sa pression d'ouverture
    : la valve doit s'ouvrir entre 0,9 et 1,3 bar selon le type. Un bouchon
    défaillant empêche la montée en pression du circuit et favorise les
    ébullitions locales. - Contrôle des ailerons du radiateur : après remontage,
    s'assurer qu'aucun aileron n'a été plié lors de la manipulation (entre le
    radiateur et le condenseur de climatisation notamment). Des ailerons aplatis
    sur plus de 20 % de la surface réduisent significativement l'efficacité de
    refroidissement. - Absence de traces de corrosion sur les tubes : inspecter
    visuellement les tubes verticaux ou horizontaux du radiateur. Aucune trace
    de vert-de-gris ni de calcaire incrusté ne doit être visible sur les
    brasures. Si des dépôts sont présents sur la nouvelle pièce dès
    l'installation, le circuit d'eau est fortement calcaire — envisager un
    rinçage du circuit avant de remettre en service.
  S7: >-
    Quel est le prix d'un radiateur de refroidissement ?Le prix varie selon le
    véhicule et la marque. Utilisez notre sélecteur pour trouver le radiateur de
    refroidissement compatible avec votre véhicule et comparer les tarifs des
    différents équipementiers.Comment savoir si mon radiateur de refroidissement
    est à changer ?Les signes d'usure les plus courants sont détaillés dans la
    section diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par
    un professionnel.Peut-on rouler avec un radiateur de refroidissement
    défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la
    pièce dans la sécurité du véhicule. Consultez la section symptômes pour
    évaluer l'urgence du remplacement.- dissiper - echanger - refroidir
  S8: >-
    Comment choisir Radiateur de refroidissement compatible avec mon
    vehiculeRenseignez marque, modele, type moteur et annee, puis verifiez la
    reference Quand remplacer Radiateur de refroidissement ?En cas de flaque de
    liquide colore sous l avant ou de degradation mesurable, Puis-je monter
    Radiateur de refroidissement sans verification atelierLe montage peut exiger
    controles de couple, alignement et references.
  META: >-
    Changer le radiateur de refroidissement de la Peugeot 206 1.4 HDI.
---

# Radiateur de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Dissiper la chaleur du liquide de refroidissement vers l'air exterieur

**Actions principales:** dissiper, echanger, refroidir, evacuer la chaleur

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- flaque de liquide colore sous l avant
- traces de corrosion sur les tubes du radiateur
- sifflement d air ou de vapeur a l avant
- surchauffe au ralenti ou en embouteillage
- odeur de liquide de refroidissement chaud
- radiateur visiblement deforme ou perce

## Procédure de Diagnostic

Pour diagnostiquer un problème de radiateur de refroidissement:

1. **Inspection visuelle** - Examiner l'état du radiateur de refroidissement
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

- bouchon-de-radiateur
- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-chauffage
- sonde-de-refroidissement
- thermostat
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon radiateur de refroidissement, vous devez connaître:

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

**Radiateur OE ou adaptable ?**
Les radiateurs OES (Valeo, Behr/Mahle, Nissens) garantissent un refroidissement optimal. Les adaptables moins chers peuvent avoir un rendement inférieur.

**Comment savoir si mon radiateur fuit ?**
Flaque de liquide sous l'avant du véhicule, niveau qui baisse, traces vertes/roses sur le radiateur, surchauffe au ralenti prolongé.

**Tous les combien changer le radiateur ?**
Pas de périodicité. À remplacer si fuite, si bouché (surchauffe) ou si endommagé par un choc.

**Peut-on réparer un radiateur percé ?**
Une réparation provisoire (résine, soudure) est possible mais temporaire. Le remplacement reste la solution fiable.

**Quelle erreur éviter avec le radiateur ?**
Ne pas monter un radiateur sans remplacer le liquide de refroidissement. Vérifier l'état des supports et des durites adjacentes.
