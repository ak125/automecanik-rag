---
category: refroidissement
slug: vase-d-expansion
title: Vase d'expansion
pg_id: 397
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
  role: Compenser les variations de volume du liquide de refroidissement
  must_be_true:
  - compenser
  - stocker
  - indiquer
  must_not_contain:
  - radiateur
  - pompe
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - radiateur-de-refroidissement
  - pompe-a-eau
  - thermostat
  - durite-de-refroidissement
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
    min: 1500
    max: 4000
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Vase identique au premier montage constructeur. Plastique technique haute résistance, forme et raccords conformes
      aux cotes d'usine.
  - tier: Équivalent OE (OES)
    description: Fabricants comme Hella, Behr/Mahle ou Valeo fournissent les constructeurs en première monte. Même plastique
      technique et mêmes cotes.
  - tier: Adaptable (aftermarket)
    description: Vases aftermarket compatibles. Vérifier la forme, l'emplacement des raccords et la compatibilité du bouchon
      de pression avant commande.
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
    label: Fuite
    severity: confort
  - id: S2
    label: Fissure
    severity: confort
  - id: S3
    label: Niveau bas
    severity: confort
  causes:
  - identifier origine fuite et verifier joints
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  - 'Usure ou defaillance causant : fuite'
  quick_checks:
  - 'Observer : niveau bas ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Niveau bas
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '397'
  intro_title: A quoi sert Vase d'expansion ?
  risk_title: Pourquoi remplacer Vase d'expansion a temps ?
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
  - question: Comment choisir Vase d'expansion compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Vase d'expansion ?
    answer: En cas de fuite ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Vase d'expansion sans verification atelier ?
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
doc_id: 1604ceb5-92c4-59b5-918c-34732a1a82ae
content_hash: sha256:3ef6cb291fb6efcb
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
  _source: hella.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  technical_notes:
    val_1_5_bars: '1,5 bars'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le vase d'expansion est un réservoir en plastique semi-transparent relié au
    circuit de refroidissement du moteur. Son rôle est de compenser les
    variations de volume du liquide de refroidissement lorsque la température du
    moteur monte et descend au fil des cycles de fonctionnement. Lorsque le
    moteur chauffe, le liquide de refroidissement se dilate — son volume
    augmente d'environ 5 à 10 % entre 20°C et 100°C. Sans vase d'expansion,
    cette dilatation pressurise le circuit au-delà des tolérances des durites et
    des joints d'étanchéité. Le vase compense cette surpression en stockant le
    surplus de liquide pendant la montée en température, puis en le restituant
    dans le circuit lors du refroidissement. Le vase d'expansion joue également
    le rôle d'indicateur de niveau : deux repères (MIN et MAX) marqués sur la
    paroi permettent de vérifier la quantité de liquide de refroidissement sans
    ouvrir les durites ni toucher au radiateur. Le niveau doit toujours être lu
    moteur froid : à chaud, le liquide est dilaté et le niveau apparaît plus
    élevé qu'il ne l'est réellement. Sur les véhicules récents, le vase
    d'expansion intègre un capteur de niveau qui allume le voyant de température
    sur le tableau de bord dès que le niveau descend sous le minimum. Ce signal
    d'alerte ne doit jamais être ignoré : un circuit sous-rempli permet
    l'apparition de poches d'air, ce qui provoque des surchauffes localisées
    pouvant fissurer la culasse. Le vase d'expansion est fabriqué en
    polypropylène résistant à la chaleur. Avec l'âge et les cycles thermiques
    répétés, le plastique se fragilise et peut fissurer — notamment au niveau
    des raccords et des points de fixation. Une fissure, même fine, entraîne une
    fuite progressive de liquide, un niveau bas récurrent et un risque de
    surchauffe. Le remplacement est alors inévitable. Les pièces associées à
    vérifier sont le bouchon de vase (dont la valve de pression conditionne
    l'étanchéité du circuit) et les durites de refroidissement. En savoir plus :
    vase d'expansion — définition et rôle mécanique 🚨 Fuite circuit de
    refroidissement : causes et diagnostic
  S2: >-
    Un vased'expansion défectueux présente plusieurs symptômes : - Fuite au
    niveau du vase d'expansion. - Déformation du vase d'expansion en cas de choc
    frontal s'il est situé àproximité du radiateur moteur. - Lors d'un contrôle
    visuel vous remarquez que vous ne pouvez plus regarder le niveau duliquide
    de refroidissement. Un vase d'expansion HS etqu'il n'est pas remplacé à
    temps dans ce cas il va avoir un manque de liquidede refroidissement à cause
    des fuites ce qui va amener à la surchauffe dumoteur et à la casse de ce
    dernier Diagnostic complet : identifier une panne de vase d'expansion
  S3: >-
    Le vase d'expansion maintient la pression du circuit de refroidissement
    entre 1,2 et 1,4 bar en absorbant les variations de volume du liquide
    lorsqu'il monte en température (de 20 °C à 110 °C, le volume augmente de 4 à
    6 %). Un vase fissuré ou dont le bouchon est défaillant provoque une perte
    de pression progressive, une aération du circuit et, à terme, une surchauffe
    moteur. La sélection doit valider la géométrie et la capacité exactes. -
    Capacité en litres et référence OEM — La capacité du vase (exprimée en
    litres, généralement de 0,5 à 2 L) est calculée pour le volume total du
    circuit. Un vase trop petit ne peut pas absorber l'expansion thermique
    complète ; un vase trop grand modifie la pression de service. Utilisez la
    référence OEM ou le numéro de pièce constructeur. - Pression d'ouverture du
    bouchon — Le bouchon de vase (souvent vendu séparément) s'ouvre à une
    pression précise : 1,0 bar, 1,2 bar ou 1,4 bar selon le constructeur. Cette
    valeur est gravée sur le bouchon. Bouchon et vase doivent correspondre ; un
    bouchon de pression supérieure sollicite le vase au-delà de ses limites. -
    Emplacement et géométrie des tubulures — Le vase comporte une ou deux
    tubulures de raccordement dont la position (haut, côté, bas) et le diamètre
    (16 mm, 19 mm, 22 mm sont courants) doivent être identiques à l'original.
    Une mauvaise orientation de tubulure génère une contrainte mécanique sur le
    tuyau en caoutchouc. - Matériau et résistance aux glycols — Le vase est
    fabriqué en polyamide (PA6, PA66) ou en polypropylène. Vérifiez la
    compatibilité avec le liquide de refroidissement utilisé : certains antigels
    G12+ ou G13 à base de silicate attaquent les résines non homologuées. -
    Présence d'un flotteur de niveau intégré — Certains vases intègrent un
    capteur de niveau (flotteur + contact électrique) qui alimente le voyant
    tableau de bord. Si votre vase d'origine en est équipé, commandez une
    version avec le même connecteur pour ne pas perdre l'alerte niveau bas. -
    Vase avec ou sans prise de température — Sur certaines Renault (Laguna,
    Scénic) et Peugeot (407, 508), le vase comporte une prise pour sonde de
    température. Remplacer cette version par un vase sans prise laisse un
    circuit ouvert et déclenche un code défaut de temperature circuit. Pour
    aller plus loin : consultez notre guide d'achat vase d'expansion —
    comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Vase d'expansion pour
    connaître les spécifications. - Arrêtez le moteur et le laissez refroidir. -
    Débranchez la batterie. - Localisez l'emplacement du vase d'expansion. -
    Videz le circuit de refroidissement. - Débranchez le connecteur du capteur
    de niveau de liquide derefroidissement si équipé. - Désaccouplez les durites
    de refroidissement du vase d'expansion. - Desserrez les fixations du vase
    d'expansion. - Démontez le vase d'expansion.
  S4_REPOSE: >-
    Remontage du vase d'expansion — procédure et contrôle d'étanchéité Le
    remplacement du vase d'expansion est une intervention accessible, mais son
    remontage exige de respecter l'ordre des étapes pour éviter une introduction
    d'air dans le circuit de refroidissement, ce qui provoquerait une surchauffe
    moteur. - Vérification du vase neuf — Comparer le vase neuf avec l'ancien :
    capacité (volume en litres), position des raccords, présence ou absence d'un
    capteur de niveau intégré, filetage du bouchon. Un vase de capacité
    différente peut provoquer un manque de compensation ou un débordement de
    liquide. - Inspection des pièces associées — Avant le remontage, vérifier
    l'état du radiateur de refroidissement (absence de fuite de liquide au
    niveau des soudures), de la pompe à eau (absence de fuite d'axe, bruit
    d'usure de roulement) et des durites de refroidissement (absence de fissure
    ou de durcissement excessif). Un vase fissuré est souvent le symptôme d'une
    pression excessive du circuit — vérifier le bouchon de vase (valve de
    pression défaillante). - Mise en place du vase neuf — Placer le vase dans
    son support, aligner les points de fixation. Serrer les vis de fixation
    (généralement M6, couple 5-8 Nm). Sur-serrer les fixations d'un vase
    plastique les fragilise. - Connexion des durites — Raccorder la durite
    principale d'alimentation-retour du circuit sur le raccord inférieur ou
    latéral du vase. S'assurer que les colliers de durite sont serrés (8-10 Nm
    pour les colliers à vis, serrage à la main pour les colliers à ressort). Une
    durite mal raccordée est la cause numéro un de fuite après remplacement. -
    Reconnexion du capteur de niveau — Si le vase est équipé d'un capteur de
    niveau de liquide, reconnecter son connecteur électrique (clip verrouillage
    du connecteur vers le haut). Un capteur débranché allumera immédiatement le
    voyant de température tableau de bord. - Remplissage du circuit de
    refroidissement — Remplir le vase avec le liquide de refroidissement neuf
    préconisé par le constructeur (ne jamais mélanger des liquides de couleurs
    différentes sauf produit universel compatible). Remplir jusqu'au niveau MAX
    marqué sur le vase. Ne pas dépasser le niveau MAX — une surpression de
    liquide en température peut faire sauter le bouchon. - Purge du circuit —
    Sur la plupart des véhicules modernes, la purge se fait en laissant tourner
    le moteur avec le bouchon ouvert jusqu'à ce que le thermostat s'ouvre (le
    ventilateur se déclenche) et que toutes les bulles d'air s'échappent.
    Refermer le bouchon une fois la température de fonctionnement atteinte
    (environ 85-95°C). - Contrôle d'étanchéité après démarrage — Inspecter
    visuellement le vase, ses raccords et les durites pendant 5 minutes moteur à
    la température de fonctionnement. Toute fuite de liquide, même minime, doit
    être corrigée immédiatement. Vérifier le niveau après refroidissement
    complet (moteur froid) : le niveau doit se situer entre MIN et MAX. ✅ Après
    remontage, vérifiez les spécifications dans la fiche technique Vase
    d'expansion.
  S5: >-
    - ❌ "homologué CT - ❌ "sécurité garantie - ❌ "zéro panne - ❌ "garanti à vie
    - ❌ "evite la casse moteur
  S6: >-
    Le remplacement du vase d'expansion nécessite de vérifier l'intégrité du
    circuit de refroidissement dans son ensemble, car le vase travaille sous
    pression et tout défaut d'étanchéité peut provoquer une perte de liquide
    progressive et une surchauffe différée. - Contrôle de l'étanchéité du
    bouchon neuf : vérifier que le bouchon du vase d'expansion est correctement
    vissé et que le joint d'étanchéité est positionné. Sur la plupart des
    véhicules, la pression de tarage du bouchon est indiquée en bar sur celui-ci
    (généralement 1,2 à 1,4 bar) — un bouchon d'une valeur différente de celle
    du constructeur peut provoquer des pertes de liquide par la soupape. -
    Contrôle du niveau de liquide à froid : après le remplacement, remplir le
    vase jusqu'au repère MAX à froid et vérifier que le niveau est stable 10
    minutes après la mise en place, sans baisse visible signe d'une fuite au
    niveau du raccordement ou du fond du vase neuf. - Test de montée en pression
    : démarrer le moteur et laisser monter en température jusqu'à la
    stabilisation de l'aiguille. Pendant ce premier cycle, aucune bulle de
    vapeur ne doit s'échapper du vase, et le bouchon ne doit pas laisser passer
    de vapeur — signe que le circuit monte correctement en pression et que le
    bouchon est étanche. - Vérification du niveau à chaud et à froid (cycle
    complet) : noter le niveau à chaud moteur stabilisé, puis le contrôler à
    nouveau le lendemain matin moteur froid. Le niveau froid doit correspondre
    au repère MIN-MAX et non avoir baissé, confirmant l'absence de fuite lente
    sur le circuit. - Inspection des raccords du vase : vérifier le serrage et
    l'absence de suintement sur les deux durites raccordées au vase neuf (durite
    haute radiateur et durite de dégazage). Un collier de serrage insuffisant
    peut provoquer une fuite à chaud sous pression. - Contrôle de l'absence de
    lait de mayonnaise sous le bouchon : lors de la vérification du niveau,
    enlever brièvement le bouchon moteur FROID et inspecter la paroi interne du
    vase — toute émulsion blanchâtre (mélange huile/eau) signalerait un joint de
    culasse défaillant, problème préexistant à investiguer indépendamment du
    vase.
  S7: >-
    Le vase d'expansion est au cœur du circuit de refroidissement : il
    communique avec le radiateur, la pompe à eau et les tuyaux haute et basse
    pression. Lors de son remplacement, ou lorsqu'une fuite est détectée dans
    cette zone, plusieurs pièces doivent être inspectées ou remplacées
    conjointement pour éviter une nouvelle intervention à court terme. - Bouchon
    de vase d'expansion : C'est la pièce la plus souvent négligée et pourtant
    décisive. Le bouchon intègre une valve de surpression (s'ouvre à 1,2-1,4 bar
    selon les constructeurs) et une valve anti-retour (empêche le reflux d'air).
    Un bouchon qui ne tient plus la pression provoque une ébullition du liquide
    à température normale, des pertes de liquide répétées et des à-coups
    thermiques. Remplacer systématiquement le bouchon lors du changement du
    vase. - Thermostat : Si la surchauffe a été la cause de la fissuration du
    vase, le thermostat a probablement subi un choc thermique. Un thermostat
    collé en position fermée empêche la circulation du liquide dans le radiateur
    et génère des pics de température. Un thermostat collé en position ouverte
    allonge le temps de chauffe et augmente la consommation. Contrôler le
    thermostat si le moteur a chauffé de manière anormale avant la défaillance
    du vase. - Tuyaux de raccordement du vase : Les durites reliant le vase au
    radiateur et au moteur sont soumises à des cycles de pression et de
    température répétés. Si le vase est fissuré ou a fui, inspecter les
    jonctions et les colliers de serrage. Un tuyau ramolli, gonflé ou craquelé à
    proximité du vase doit être remplacé en même temps. - Liquide de
    refroidissement : Tout remplacement du vase impose une vidange et un
    remplissage avec du liquide neuf conforme aux spécifications constructeur
    (G11, G12, G13 selon le type de moteur). Ne jamais mélanger des liquides de
    composition différente — cela provoque un dépôt gélatineux qui bouche la
    pompe et le radiateur. Vérifier la concentration antigel (protège jusqu'à
    -25 °C minimum pour un usage européen). - Capteur de niveau de liquide de
    refroidissement : Intégré dans le vase d'expansion sur de nombreux modèles,
    ce capteur déclenche le voyant de niveau bas au tableau de bord. Si le
    voyant reste allumé après le remplacement du vase, vérifier la connectique
    du capteur ou prévoir son remplacement si le capteur est fourni séparément
    du vase.
  S8: >-
    Comment choisir Vase d'expansion compatible avec mon vehicule ?Renseignez
    marque, modele, type moteur et annee, puis verifiez la reference Quand
    remplacer Vase d'expansion ?En cas de fuite ou de degradation mesurable, il
    faut controler rapidement Puis-je monter Vase d'expansion sans verification
    atelier ?Le montage peut exiger controles de couple, alignement et
    references.
  META: >-
    {"meta_title":"Vase d'expansion : fissure, fuite, remplacement |
    AutoMecanik","meta_description":"Vase d'expansion fissuré, niveau de liquide
    de refroidissement bas ou fuite visible ? Diagnostic et remplacement selon
    votre véhicule.","og_title":"Vase d'expansion : quand et comment le
    remplacer | AutoMecanik","og_description":"Fissure, fuite ou niveau bas du
    liquide de refroidissement : guide complet pour diagnostiquer et remplacer
    le vase d'expansion.","schema_type":"HowTo","canonical_hint":"/pieces/vase-
    d-expansion"}
---

# Vase d'expansion - Guide Diagnostic Complet

## Fonction et Rôle

Compenser les variations de volume du liquide de refroidissement

**Actions principales:** compenser, stocker, indiquer, reguler la pression

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- fuite
- fissure
- niveau bas

## Procédure de Diagnostic

Pour diagnostiquer un problème de vase d'expansion:

1. **Inspection visuelle** - Examiner l'état du vase d'expansion
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

- bouchon-vase-d-expansion

## Critères de Compatibilité

Pour commander le bon vase d'expansion, vous devez connaître:

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

**Comment choisir Vase d'expansion compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Vase d'expansion ?**
En cas de fuite ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Vase d'expansion sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
