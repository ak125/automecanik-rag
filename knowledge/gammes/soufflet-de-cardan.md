---
category: transmission
slug: soufflet-de-cardan
title: Soufflet de Cardan
pg_id: 193
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
  role: Protege le joint de cardan et retient la graisse de lubrification
  must_be_true:
  - proteger
  - etancher
  - contenir
  must_not_contain:
  - injection
  - freinage
  - climatisation
  - allumage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - cardan
  - roulement-de-roue
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
  - ❌ "transmission parfaite"
  cost_range:
    min: 15
    max: 50
    currency: EUR
    unit: soufflet
    source: catalogue automecanik
  brands:
    premium:
    - GKN (Loebro)
    - SKF
    - NTN-SNR
    standard:
    - Spidan
    - Febi Bilstein
    - Meyle
    budget:
    - Sasic
    - Topran
    - Maxgear
  quality_tiers:
  - tier: Origine (OE)
    description: Soufflets fabriques par l'equipementier d'origine. Caoutchouc haute resistance, diametre et longueur identiques
      a la piece constructeur. Graisse specifique incluse.
  - tier: Qualite equivalente OE (OES)
    description: Equipementiers reconnus en transmission. Soufflets en caoutchouc ou thermoplastique de qualite equivalente,
      kit avec colliers et graisse.
  - tier: Adaptable de qualite
    description: Marques fiables en entree de gamme. Verifier le diametre exact et le type (cote roue ou cote boite). Kit
      complet avec colliers et graisse recommande.
diagnostic:
  symptoms:
  - id: S1
    label: Graisse noire visible sur la jante interieure
    severity: confort
  - id: S2
    label: Soufflet fendu dechire ou decolle visible
    severity: confort
  - id: S3
    label: Claquement en braquant joint deja endommage
    severity: confort
  - id: S4
    label: Odeur de graisse brulee pres de la roue
    severity: confort
  - id: S5
    label: Vibrations au volant a vitesse constante
    severity: confort
  - id: S6
    label: Plus controle visuel soufflets
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'vibrations anormales : verifier equilibrage et fixations'
  quick_checks:
  - 'Observer : graisse noire visible sur la jante interieure ?'
  - 'Observer : soufflet fendu dechire ou decolle visible ?'
  - 'Observer : claquement en braquant joint deja endommage ?'
  - Odeur de graisse brulee pres de la roue ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Graisse noire visible sur la jante interieure
  - Soufflet fendu dechire ou decolle visible
  - Claquement en braquant joint deja endommage
  - Odeur de graisse brulee pres de la roue
  - Vibrations au volant a vitesse constante
  - Plus controle visuel soufflets
  good_practices:
  - Verifier le niveau d huile de boite selon preconisation constructeur
  - Controle des soufflets de protection (pas de fuite de graisse)
  - Remplacement de la bague d etancheite en cas de fuite
  - Inspection des cardans et croisillons a chaque revision
rendering:
  pgId: '193'
  intro_title: A quoi sert Soufflet de Cardan ?
  risk_title: Pourquoi remplacer Soufflet de Cardan a temps ?
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
  - question: Soufflet de cardan OE ou adaptable ?
    answer: 'Les soufflets OES (GKN, SKF) ou adaptables (Spidan, Febi) sont fiables. Vérifiez le diamètre exact et le type
      : côté roue ou côté boîte.'
  - question: Comment savoir si mon soufflet est percé ?
    answer: Graisse noire sur la jante ou le passage de roue, soufflet visiblement fendu ou déchiré, fuite de graisse sous
      le véhicule.
  - question: Tous les combien vérifier les soufflets ?
    answer: Contrôle visuel à chaque révision ou passage au contrôle technique. Un soufflet peut se fendre sans prévenir suite
      à un choc.
  - question: Peut-on changer un soufflet de cardan seul ?
    answer: 'Oui si le joint n''est pas usé. Opération technique : dépose du cardan, nettoyage du joint, regraissage, montage
      du soufflet neuf.'
  - question: Quelle erreur éviter avec le soufflet ?
    answer: Ne pas attendre si le soufflet est percé. Utiliser la graisse spécifique fournie. Vérifier les deux soufflets
      (côté roue et côté boîte).
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
doc_id: 50d7977f-f03f-5a93-89f5-2fd2270058a3
content_hash: sha256:63493ca7589a6996
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
  area: Sous le vehicule, relie la boite aux roues
  access: Par le dessous (pont elevateur)
  adjacent_parts:
  - cardan
  - soufflet
  - roulement de roue
  - boite
installation:
  difficulty: difficile
  time: 1h a 3h
  tools:
  - pont elevateur
  - cle a douille
  - arrache-cardan
  prerequisite: Vidange huile de boite si cardan depose
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-04'
  _web_files_count: 1
  _has_tech_data: false
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le soufflet de cardan joue lerôle d'un joint et d'un récipient de graisse
    pour le bon fonctionnement ducardan. Il retient la graisse utilisée pour le
    graissage des articulations situéesà chaque extrémité du cardan. Dans
    certain véhicule le cardan intérieur côté gaucheest lubrifié par l'huile de
    boîte de vitesses dans ce cas le soufflet de cardanretient l'huile et non
    pas la graisse. Le soufflet de cardan est fabriqué encaoutchouc souple pour
    qu'il s'adapte à toute forme de distorsion, en luipermettant de rester
    étanche dans toutes les situations. En savoir plus : soufflet de cardan —
    définition et rôle mécanique 🚨 Bruit Soufflet de Cardan : causes et
    diagnostic
  S2: >-
    Le seul moyen poursavoir l'état d'usure du soufflet cardan est de faire un
    contrôle visuel enlevant le véhicule dans ce cas vous allez remarquer
    plusieurs symptômes : - Fissure ou craquelure au niveau du soufflet de
    cardan. - Des traces de graisse côté roue dans ce cas le soufflet de cardan
    estpercé. Si un soufflet de cardan est HS,dans ce cas le cardan ne sera plus
    graissé qui peut amener à l'usure d'autrespièces : - Usure de la boîte de
    vitesses coté gauche à cause de fuite d'huile. - Usure du moyeu de roue.
    Diagnostic complet : identifier une panne de soufflet de cardan
  S3: >-
    Le soufflet de cardan protège le joint homocinétique de la saleté et retient
    la graisse. Un soufflet incompatible laissera entrer l'eau et la poussière,
    détruisant le cardan en quelques milliers de kilomètres.Vérifications
    indispensables- Côté du cardan : soufflet côté roue (plus grand) ou côté
    boîte (plus petit) — les deux ne sont pas interchangeables- Diamètre
    intérieur petit bout : correspond à l'arbre de transmission (25-35 mm selon
    modèle)- Diamètre intérieur grand bout : correspond au bol du joint (70-110
    mm selon côté)- Matériau : caoutchouc (souple, durée standard) ou
    thermoplastique (plus rigide, durée supérieure)Méthode de
    vérificationIdentifier côté roue ou côté boîte. Mesurer les diamètres des
    deux extrémités sur le soufflet déposé. Comparer la référence OE avec la
    fiche produit.Pour aller plus loin : consultez notre guide d'achat soufflet
    de cardan — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Soufflet de Cardan pour
    connaître les spécifications. - Levez et calez le véhicule. - Démontez les
    roues. - Démontez le cardan. - Démontez les colliers deserrage du soufflet
    de cardan. - Démontez le soufflet decardan.
  S4_REPOSE: >-
    - Vérifiez que le soufflet de cardan neuf est identique à celui démonté.-
    Contrôlez l'état d'usure des cardans et les remplacés si nécessaire. -
    Nettoyez et graissez les articulations du cardan avant le remontage. -
    Mettre en place les soufflets de cardan. - Serrez les colliers de serrage
    des soufflets de cardan. - Bougez l'articulation du cardan pour répartir la
    graisse. - Remontez le cardan. - Remontez les roues. ✅ Après remontage,
    vérifiez les spécifications dans la fiche technique Soufflet de Cardan.
  S5: >-
    - Confondre soufflet côté roue et côté boîte — les diamètres sont
    différents, le montage sera impossible ou le soufflet se déchirera →
    toujours identifier le côté avant commande- Ne pas nettoyer le joint
    homocinétique — la graisse contaminée par l'eau et le sable reste dans le
    joint et l'use prématurément → dégraisser complètement le joint au nettoyant
    frein et sécher avant remontage- Réutiliser la graisse d'origine — la
    graisse contaminée a perdu ses propriétés lubrifiantes → remplacer
    intégralement par de la graisse neuve spéciale cardan (graisse au bisulfure
    de molybdène)- Sous-doser la graisse — un joint sous-graissé chauffe et
    s'use en quelques milliers de km → utiliser la quantité préconisée (80-120 g
    côté roue, 40-60 g côté boîte)- Pincer le soufflet lors du serrage des
    colliers — fuite de graisse garantie et entrée d'eau → vérifier que le
    soufflet n'est ni vrillé ni pincé avant de sertir les colliers- Utiliser des
    colliers inadaptés — un collier trop large ou mal serti ne garantit pas
    l'étanchéité → utiliser des colliers de sertissage spécifiques, pas des
    colliers à vis- Oublier de purger l'air du soufflet — le soufflet gonflé
    comme un ballon se détériore rapidement en rotation → percer légèrement avec
    une aiguille ou soulever le bord pour évacuer l'air, puis refermer- Monter
    un soufflet fendu sur un cardan encore bon — rouler même quelques kilomètres
    avec un soufflet déchiré contamine le joint → remplacer le soufflet dès la
    première fissure visible
  S6: >-
    Contrôles statiques (véhicule au sol)- Vérifier que les deux colliers de
    soufflet sont correctement sertis (pas de jeu au toucher)- Contrôler
    l'absence de fuite de graisse autour des colliers et sur le soufflet-
    Inspecter que le soufflet n'est ni vrillé, ni pincé, ni gonflé- Vérifier le
    serrage de l'écrou de moyeu au couple constructeur (175-280 Nm selon
    modèle)Test routier progressif- Rouler à 20 km/h en braquant à fond à droite
    puis à gauche : aucun claquement ne doit être audible- Accélérer franchement
    en ligne droite : pas de vibration ni de à-coup dans la transmission- Rouler
    à 80 km/h : absence de vibration périodique (signe de joint mal regraissé ou
    endommagé)- Après 50 km, inspecter visuellement le soufflet : pas de
    projection de graisse sur la jante ou le passage de roue⚠️ Important : Si
    des claquements apparaissent en virage après remplacement du soufflet, le
    joint homocinétique est probablement déjà endommagé. Dans ce cas, le cardan
    complet doit être remplacé.
  S7: >-
    Quel est le prix d'un soufflet de cardan ?Le prix varie selon le véhicule et
    la marque. Utilisez notre sélecteur pour trouver le soufflet de cardan
    compatible avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon soufflet de cardan est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un soufflet de cardan défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la
    sécurité du véhicule. Consultez la section symptômes pour évaluer l'urgence
    du remplacement.Cardan. 📖 Fiche technique Soufflet de Cardan — intervalles
    et spécifications d’entretien.
  S8: >-
    Comment savoir si mon soufflet de cardan est percé ? Le signe le plus
    visible est de la graisse noire projetée sur la jante intérieure, sur le
    passage de roue ou sur la jupe de carrosserie adjacente. La graisse xénon de
    cardan (noire et collante) est caractéristique : contrairement à la graisse
    mécanique ordinaire, elle s'étale en fine couche sur les surfaces
    environnantes. Un soufflet visiblement fendu, déchiré ou décollé de son
    collier est une défaillance confirmée à l'inspection visuelle. L'absence de
    signes extérieurs ne suffit pas : un soufflet peut présenter une micro-
    fissure invisible qui laisse échapper la graisse progressivement. Peut-on
    rouler avec un soufflet de cardan percé ? Quelques centaines de kilomètres
    au maximum, et à vitesse réduite. Un soufflet percé laisse entrer eau et
    sable dans le joint homocinétique : sans graisse protectrice et avec des
    abrasifs, les billes de cardan s'usent en quelques semaines seulement. Le
    premier signe d'un joint endommagé est un claquement sec en braquant à fond
    et en accélérant. Une fois ce stade atteint, le cardan entier doit être
    remplacé, ce qui représente un coût nettement supérieur au simple
    remplacement d'un soufflet. Peut-on remplacer uniquement le soufflet sans
    changer le cardan ? Oui, à condition que le joint homocinétique soit encore
    en bon état (pas de jeu perceptible, pas de claquement en virage, graisse
    non contaminée par l'eau ou le sable). Si le soufflet vient de se fissurer
    et que la détérioration est récente (moins de quelques semaines), un
    remplacement de soufflet seul avec regraissage complet est justifié. Si le
    claquement est déjà présent, le joint est usé et le cardan complet doit être
    remplacé. Certains mécaniciens proposent des kits soufflet + graisse qui
    permettent de tout refaire proprement sans dépose complète du cardan. Faut-
    il changer les deux soufflets en même temps ? Pas obligatoirement, mais il
    est conseillé de vérifier les quatre soufflets (deux par cardan : côté roue
    et côté boîte) en même temps. Le soufflet côté roue est exposé aux
    projections et aux variations d'angle plus importantes lors du braquage ; il
    s'use donc plus vite. Le soufflet côté boîte subit moins d'amplitude
    angulaire mais peut se fissurer par vieillissement. Si un soufflet est à
    remplacer sur un cardan, vérifier l'autre soufflet du même cardan et l'état
    du cardan opposé pour éviter deux interventions rapprochées. Quelle graisse
    utiliser pour le soufflet de cardan ? La graisse de cardan est spécifique :
    c'est une graisse à base de savon de lithium ou de molybdène, formulée pour
    résister aux températures élevées et aux fortes contraintes d'angle du joint
    homocinétique. Ne pas utiliser de graisse à roue ou de graisse ordinaire :
    ces graisses ne sont pas conçues pour les joints homocinétiques et peuvent
    provoquer une usure prématurée. Utiliser impérativement la graisse fournie
    avec le kit soufflet, ou une graisse spécifiée par le constructeur du cardan
    (GKN, SKF, Spidan précisent la référence dans leurs notices de montage).
    Combien de temps prend le remplacement d'un soufflet de cardan ? Entre 1h et
    2h30 selon l'accès et l'état du cardan. Les étapes comprennent la dépose du
    cardan (démontage de l'écrou de moyeu, dépose de la rotule inférieure de
    bras de suspension ou débranchement de la boîte selon le type de montage),
    la découpe du soufflet défaillant, le nettoyage complet du joint
    homocinétique, le contrôle de l'état des billes et du logement, le
    regraissage au bon dosage (quantité de graisse indiquée dans la notice kit),
    la pose et le serrage des colliers neuf, puis la repose du cardan avec un
    écrou de moyeu neuf serré au couple constructeur (souvent entre 180 et 280
    Nm selon les véhicules).
  META: >-
    Guide remplacement soufflet de cardan : choisir le bon côté, erreurs de
    montage à éviter, graisse adaptée et vérifications. Conseils pratiques.
---

# Soufflet de Cardan - Guide Diagnostic Complet

## Fonction et Rôle

Protege le joint de cardan et retient la graisse de lubrification

**Actions principales:** proteger, etancher, contenir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement en braquant joint deja endommage**
  claquement en braquant joint deja endommage

### 🟢 Autres Symptômes

- graisse noire visible sur la jante interieure
- soufflet fendu dechire ou decolle visible
- odeur de graisse brulee pres de la roue
- vibrations au volant a vitesse constante
- plus controle visuel soufflets

## Procédure de Diagnostic

Pour diagnostiquer un problème de soufflet de cardan:

1. **Inspection visuelle** - Examiner l'état du soufflet de cardan
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- cardan

## Critères de Compatibilité

Pour commander le bon soufflet de cardan, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "transmission parfaite"

## FAQ

**Soufflet de cardan OE ou adaptable ?**
Les soufflets OES (GKN, SKF) ou adaptables (Spidan, Febi) sont fiables. Vérifiez le diamètre exact et le type : côté roue ou côté boîte.

**Comment savoir si mon soufflet est percé ?**
Graisse noire sur la jante ou le passage de roue, soufflet visiblement fendu ou déchiré, fuite de graisse sous le véhicule.

**Tous les combien vérifier les soufflets ?**
Contrôle visuel à chaque révision ou passage au contrôle technique. Un soufflet peut se fendre sans prévenir suite à un choc.

**Peut-on changer un soufflet de cardan seul ?**
Oui si le joint n'est pas usé. Opération technique : dépose du cardan, nettoyage du joint, regraissage, montage du soufflet neuf.

**Quelle erreur éviter avec le soufflet ?**
Ne pas attendre si le soufflet est percé. Utiliser la graisse spécifique fournie. Vérifier les deux soufflets (côté roue et côté boîte).
