---
category: accessoires
slug: bouchon-reservoir-de-carburant
title: Bouchon réservoir de carburant
pg_id: 602
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
  role: Ferme hermétiquement le réservoir de carburant
  must_be_true:
  - fermer
  - etancheifier
  - proteger
  must_not_contain:
  - pompe
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - disque-de-frein
  - plaquette-de-frein
  - etrier-de-frein
  - flexible-de-frein
  - maitre-cylindre-de-frein
  - liquide-de-frein
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Bouchon réservoir de carburant.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Respecter les dimensions et le type de montage (ventile, plein, perfore)
  - Choisir un equipementier reconnu (ATE, TRW, Brembo, Bosch) pour la securite
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "economie carburant"
  cost_range:
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Bouchon de réservoir fourni par l'équipementier d'origine du véhicule. Verrouillage, joint et valve d'évent
      conformes aux spécifications constructeur.
  - tier: Équivalent OE — spécialistes accessoires carrosserie
    description: Fabricants reconnus en bouchons de réservoir et accessoires de carburant. Joint d'étanchéité intégré testé
      en résistance aux vapeurs d'hydrocarbures.
  - tier: Adaptables
    description: Bouchons génériques couvrant plusieurs véhicules. Vérifier le diamètre de col de remplissage, le type de
      fermeture et la compatibilité système EVAP avant commande.
  brands:
    premium:
    - Stabilus
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Odeur de carburant persistante
    severity: confort
  - id: S2
    label: Voyant defaut evaporation allume
    severity: confort
  - id: S3
    label: Difficultes a refermer le bouchon
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - 'Usure ou defaillance causant : odeur de carburant persistante'
  - 'Usure ou defaillance causant : voyant defaut evaporation allume'
  quick_checks:
  - Odeur de carburant persistante ?
  - Voyant defaut evaporation allume ?
  - 'Observer : difficultes a refermer le bouchon ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Odeur de carburant persistante
  - Voyant defaut evaporation allume
  - Difficultes a refermer le bouchon
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '602'
  intro_title: A quoi sert Bouchon réservoir de carburant ?
  risk_title: Pourquoi remplacer Bouchon réservoir de carburant a temps ?
  risk_explanation: '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  risk_consequences:
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
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
  - question: Comment choisir Bouchon réservoir de carburant compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Bouchon réservoir de carburant ?
    answer: En cas de odeur de carburant persistante ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Bouchon réservoir de carburant sans verification atelier ?
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
doc_id: 12cf9984-b2e7-5546-92bd-5f3e5f7fee98
content_hash: sha256:0022abc599c6f6bd
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
  area: Sur la carrosserie (capot, coffre, portes)
  access: Accessible directement sans outil special
  adjacent_parts:
  - charniere
  - serrure
  - cable
  - joint
installation:
  difficulty: facile
  time: 10 a 30 min
  tools:
  - tournevis
  - cle plate
  - clip de fixation
  prerequisite: Aucun prerequis special
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'plein'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_20_litres: '20 litres'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le bouchon de réservoir de carburant est un composant très essentiel dans le
    véhicule malgré sa petite dimension. Il a pour fonction d'obturer la
    goulotte de remplissage du réservoir et d'en assurer l'étanchéité, pour
    éviter toute fuite ou déversement de carburant. Il est composé de matériaux
    thermoplastique très résistant (suivant le niveau d'équipement du véhicule).
    Il est hermétique si le réservoir est ventilé par une prise d'air au niveau
    du goulotte de remplissage si non c'est le bouchon lui-m&ecirc;me qui est
    équipé d'une prise d'air. Le plus plupart des bouchons est à l'abri d'une
    trappe et il est doté ou non d'une serrure de sécurité. L'ouverture du
    bouchon ce fait après l'ouverture de la trappe du réservoir et par la clé de
    contact ou sans la clé.
  S2: >-
    Le bouchon de réservoir de carburant n'a pas une période de remplacement
    parce que ce n'est pas une pièce d'usure. On peut constater qu'il est
    défectueux si on constate un problème au niveau du joint, ou du mécanisme
    antiblocage, ou de la serrure et en cas de perte du bouchon. Toute trace de
    fuite de carburant impose son remplacement.
  S3: >-
    - Référence constructeur exacte : Le bouchon de réservoir est une pièce
    dimensionnée au millimètre près. Relevez la référence OEM inscrite sur le
    bouchon d'origine ou dans la documentation technique du véhicule avant de
    commander. - Diamètre du filetage et pas de vis : Un bouchon à filetage
    légèrement différent peut sembler se visser mais ne garantit pas
    l'étanchéité. Vérifiez le diamètre (généralement entre 38 et 60 mm) et le
    sens de vissage (droit ou gauche selon les constructeurs). - Système de
    fermeture : Distinguez les bouchons à vis simple, à déclic (avec limiteur de
    couple intégré) et les bouchons verrouillables anti-vol. Le type d'origine
    doit être conservé pour maintenir la compatibilité avec la trappe de
    carburant. - Présence ou absence d'évent : Certains bouchons intègrent une
    soupape d'évent calibrée qui régule la pression du circuit d'évaporation
    (EVAP). Remplacer un bouchon à évent par un bouchon simple peut déclencher
    un code défaut P0457 ou P0442. - Matériau de la gorge d'étanchéité : Le
    joint torique intégré doit résister aux hydrocarbures (NBR ou FKM). Évitez
    les bouchons génériques dont le joint se dégrade rapidement au contact de
    l'essence sans plomb ou du diesel. - Compatibilité avec le véhicule
    homologué E10 : Si votre véhicule utilise du carburant E10 (superéthanol),
    vérifiez que le joint du bouchon est compatible avec les mélanges éthanol-
    essence pour éviter le gonflement. - Marque, modèle et année du véhicule :
    Ces trois informations sont obligatoires pour filtrer les références
    compatibles. Une même gamme de véhicule peut avoir reçu plusieurs
    générations de réservoirs avec des bouchons différents. Pour aller plus loin
    : consultez notre guide d'achat bouchon réservoir de carburant — comparatif
    marques, critères de choix et prix.
  S4_DEPOSE: >-
    - Sécuriser le véhicule à froid : Laissez le moteur refroidir au moins 30
    minutes. Le réservoir peut être sous légère pression résiduelle après un
    trajet. Ne travaillez jamais près d'une flamme nue ou d'une source
    d'étincelles. - Localiser la trappe de réservoir : Ouvrez la trappe depuis
    l'habitacle (levier ou bouton selon le modèle) puis accédez à l'extérieur du
    véhicule côté réservoir. - Dévisser le bouchon d'origine : Tournez le
    bouchon dans le sens antihoraire (sens horaire pour les modèles à filetage
    inversé, consulter la documentation constructeur). Si un système de
    déverrouillage à déclic est présent, appuyez sur le bouton central avant de
    dévisser. - Inspecter le goulot : Examinez l'état du filetage sur le goulot
    du réservoir. Tout filetage endommagé doit être signalé — le remplacement du
    goulot seul est parfois possible, sinon le réservoir complet est concerné. -
    Contrôler le joint torique du goulot : Si un joint d'étanchéité est présent
    sur le goulot (distinct du joint intégré au bouchon), vérifiez son état et
    remplacez-le si nécessaire. - Installer le nouveau bouchon : Engagez le
    nouveau bouchon dans le filetage en veillant à l'aligner correctement.
    Vissez à la main jusqu'à sentir la résistance, puis serrez jusqu'au clic de
    confirmation (bouchons à limiteur de couple) ou jusqu'à butée ferme
    (bouchons simples). Ne forcez pas. - Vérifier l'étanchéité : Démarrez le
    moteur et laissez-le tourner 2 minutes. Inspectez visuellement le pourtour
    du bouchon et la trappe pour détecter toute fuite ou suintement de
    carburant. - Effacer les codes défaut éventuels : Si le voyant de contrôle
    du circuit EVAP était allumé avant l'intervention, connectez un outil OBD-II
    pour lire puis effacer les codes défaut (P0455, P0457, P0442). Le voyant
    doit s'éteindre après quelques cycles moteur.
  S4_REPOSE: >-
    La repose du bouchon de réservoir de carburant est une opération simple mais
    qui doit être effectuée avec soin pour garantir l'étanchéité du circuit
    d'évaporation (EVAP) et éviter tout risque lié aux vapeurs de carburant. Une
    mauvaise repose peut maintenir le voyant de contrôle allumé ou générer une
    odeur persistante dans l'habitacle. - S'assurer que le goulot est propre et
    intact : avant de visser le nouveau bouchon, inspecter le goulot du
    réservoir. Le filetage doit être propre, sans résidu de carburant séché ni
    trace d'oxydation. Essuyer avec un chiffon propre. Tout filetage endommagé
    ou goulot fissuré doit être traité avant la repose du bouchon. - Vérifier
    que le joint torique du nouveau bouchon est en place : le bouchon neuf est
    livré avec son joint intégré ou séparé. S'assurer que le joint est
    correctement positionné dans sa gorge avant toute tentative de vissage. Un
    joint absent ou mal placé génèrera immédiatement une fuite de vapeurs de
    carburant. - Contrôler l'état du joint de goulot (si présent) : certains
    véhicules disposent d'un joint supplémentaire sur le goulot lui-même,
    indépendant du joint du bouchon. Inspecter cet élément et le remplacer si
    nécessaire. Ce joint assure l'étanchéité entre le goulot et la carrosserie
    de la trappe. - Engager le bouchon dans le filetage à la main : positionner
    le bouchon dans le goulot et le visser manuellement dans le sens horaire
    (antihoraire pour les modèles à filetage inversé, se référer à la
    documentation constructeur). Le filetage doit s'engager sans résistance sur
    les premières spires. Toute résistance prématurée signale un filetage croisé
    : dévisser et recommencer. - Serrer jusqu'au clic de confirmation ou à butée
    ferme : les bouchons modernes sont équipés d'un limiteur de couple qui
    produit un déclic lorsque le serrage optimal est atteint. Continuer à
    tourner jusqu'à entendre ce clic (3 à 5 clics consécutifs selon le modèle).
    Pour les bouchons sans limiteur de couple, serrer jusqu'à contact ferme sans
    forcer au-delà. - Refermer la trappe de réservoir : rabattre la trappe
    jusqu'au clic d'encliquetage. Vérifier depuis l'intérieur que le loquet de
    trappe s'est bien engagé et que la trappe affleure correctement la
    carrosserie. - Démarrer et laisser tourner le moteur 2-3 minutes : une fois
    le moteur en marche, le circuit EVAP se met en pression. Inspecter
    visuellement la trappe et le pourtour du bouchon pour détecter tout
    suintement ou odeur de carburant. En l'absence de fuite, la repose est
    correcte. - Effacer les codes défaut avec un outil OBD-II si nécessaire : si
    un voyant EVAP (codes P0455, P0457, P0442) était présent avant
    l'intervention en raison d'un bouchon défaillant, effacer les codes après la
    repose. Le calculateur doit valider l'étanchéité du circuit lors des
    prochains cycles de conduite avant d'éteindre le voyant définitivement.
  S5: >-
    - Monter un bouchon générique sans correspondance de référence : Un bouchon
    dont le filetage ne correspond pas exactement au goulot peut sembler tenir
    mais laisse filtrer des vapeurs de carburant. Ces fuites déclenchent le
    voyant de défaut du circuit EVAP et peuvent faire échouer le contrôle
    technique à la mesure des émissions. - Serrer excessivement le bouchon : Les
    bouchons modernes sont conçus avec un limiteur de couple intégré qui clique
    à la bonne valeur. Forcer au-delà abîme irrémédiablement le filetage du
    goulot — une réparation nettement plus coûteuse que le bouchon lui-même. -
    Remplacer un bouchon à évent par un bouchon hermétique simple : Le circuit
    d'évaporation (EVAP) de votre véhicule nécessite un évent calibré. Un
    bouchon hermétique crée une dépression dans le réservoir qui peut aspirer le
    carburant, perturber l'alimentation et générer des codes OBD persistants. -
    Ignorer l'odeur de carburant après remplacement : Si une odeur persiste
    après l'installation du nouveau bouchon, ne concluez pas à un défaut du
    bouchon sans vérifier l'état du joint du goulot. Un joint fissuré ou écrasé
    maintient une fuite même avec un bouchon neuf correct. - Commander sans
    vérifier la compatibilité avec l'année de production : Sur plusieurs modèles
    de véhicules, le même constructeur a changé le design du goulot en cours de
    fabrication. L'année exact (et parfois le mois) de mise en circulation
    conditionne la référence correcte.
  S6: >-
    - Contrôle visuel immédiat : Après installation, inspectez le pourtour du
    bouchon sur le goulot — aucun espace visible, le joint doit être plaqué
    uniformément sur toute la circonférence. - Test olfactif moteur chaud :
    Démarrez le véhicule et laissez tourner 3 à 5 minutes. Aucune odeur de
    carburant ne doit être détectable au niveau de la trappe de réservoir ou
    dans l'habitacle. - Lecture OBD après 2 cycles de conduite : Si le voyant
    défaut circuit EVAP était présent avant l'intervention, branchez un scanner
    OBD-II après 2 cycles de roulage complets (démarrage à froid jusqu'à
    température normale). Le moniteur EVAP doit repasser à "prêt" et les codes
    P0455, P0457 ou P0442 ne doivent plus revenir. - Vérification de la trappe
    d'accès : Assurez-vous que la trappe de carburant se referme correctement et
    que le bouchon ne gêne pas sa fermeture (test de fermeture à la main puis à
    distance si trappe électrique). - Contrôle à 500 km : Après une semaine
    d'utilisation normale, réinspectez le bouchon et la trappe pour vérifier
    l'absence de suintement ou de dépôts blanchâtres autour du goulot.
  S7: >-
    Le bouchon de réservoir de carburant est un composant d'étanchéité qui
    s'intègre dans le système de contrôle des émissions par évaporation (EVAP).
    Sa défaillance peut déclencher des voyants moteur et des codes OBD liés à
    l'ensemble de ce circuit. Lors du remplacement du bouchon, vérifier l'état
    des éléments suivants. - Goulot de réservoir de carburant : le bouchon visse
    directement sur le goulot. Si le filetage du goulot est endommagé ou si le
    goulot est fissuré, le nouveau bouchon ne pourra pas assurer l'étanchéité.
    Un goulot défaillant peut nécessiter un remplacement partiel (goulot seul
    sur certains modèles) ou complet du réservoir. - Trappe de réservoir de
    carburant : la trappe protège mécaniquement le bouchon des intrusions
    extérieures. Un loquet de trappe défaillant ou une trappe déformée peut
    exposer le bouchon à des contraintes anormales. Vérifier le bon
    fonctionnement de l'ouverture de trappe depuis l'habitacle. - Purge de boîte
    à charbon actif (canister) : dans le circuit EVAP, le canister absorbe les
    vapeurs de carburant quand le moteur est à l'arrêt. Une purge canister
    bouchée ou un canister saturé génère des codes P0440-P0461 similaires à ceux
    d'un bouchon de réservoir défaillant. En cas de voyant EVAP persistant après
    remplacement du bouchon, le canister est à inspecter. - Vanne de purge EVAP
    : cette vanne commande le transfert des vapeurs du canister vers l'admission
    moteur. Sa défaillance (collée ouverte ou fermée) perturbe le circuit EVAP
    et peut générer des fuites de vapeur ou des codes défaut résiduels. À
    contrôler si des codes P0446 ou P0443 sont présents. - Joint de goulot :
    distinct du joint intégré au bouchon, ce joint assure l'étanchéité entre le
    goulot et la carrosserie de la trappe. Son vieillissement ou son écrasement
    peut provoquer une légère odeur de carburant même avec un bouchon neuf. À
    remplacer si l'odeur persiste après installation du nouveau bouchon.
  S8: >-
    Un bouchon de réservoir cassé peut-il faire allumer un voyant ? Oui. Un
    bouchon mal fermé ou dont le joint est défaillant laisse s'échapper des
    vapeurs de carburant dans l'atmosphère. Le calculateur moteur détecte cette
    fuite via le capteur de pression du circuit EVAP et allume le témoin de
    défaut moteur (MIL). Les codes défaut associés sont généralement P0455
    (grande fuite), P0457 (bouchon desserré) ou P0442 (petite fuite). Le
    remplacement du bouchon suffit souvent à résoudre ces codes, à condition que
    le reste du circuit EVAP soit intact. Comment savoir si mon bouchon est à
    évent ou hermétique ? La quasi-totalité des véhicules fabriqués après 1996
    est équipée de bouchons à évent intégré (conformes à la norme OBD-II). Un
    bouchon à évent présente généralement un petit clapet ou une membrane
    visible sur sa face intérieure. Si vous retirez votre bouchon et constatez
    qu'il est parfaitement plan et plein à l'intérieur, il est possible qu'il
    soit hermétique — mais vérifiez la fiche technique de votre véhicule avant
    de conclure, car certains modèles ont l'évent déporté sur le goulot lui-
    même. Peut-on faire le plein avec un bouchon abîmé en attendant le
    remplacement ? Techniquement possible pour un trajet court, mais
    déconseillé. Un bouchon endommagé ne garantit plus l'étanchéité du réservoir
    : projection de carburant en virage serré, aspiration de poussières ou d'eau
    dans le réservoir, et risque d'inflammation des vapeurs sont à prendre au
    sérieux. Si vous devez rouler temporairement, évitez de remplir le réservoir
    à plus de 75 % de sa capacité pour limiter les risques de débordement. Le
    bouchon de réservoir fait-il partie du contrôle technique ? Oui, depuis le
    renforcement du CT en 2019, le contrôle des émissions de polluants inclut la
    vérification de l'étanchéité du circuit de dépollution. Un bouchon
    défaillant générant des fuites de vapeurs peut entraîner une contre-visite.
    Le point de contrôle est listé sous "système de contrôle des émissions par
    évaporation" dans le rapport de contrôle technique.
---

# Bouchon réservoir de carburant - Guide Diagnostic Complet

## Fonction et Rôle

Ferme hermétiquement le réservoir de carburant

**Actions principales:** fermer, etancheifier, proteger

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- odeur de carburant persistante
- voyant defaut evaporation allume
- difficultes a refermer le bouchon

## Procédure de Diagnostic

Pour diagnostiquer un problème de bouchon réservoir de carburant:

1. **Inspection visuelle** - Examiner l'état du bouchon réservoir de carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- reservoir
- trappe

## Critères de Compatibilité

Pour commander le bon bouchon réservoir de carburant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "economie carburant"

## FAQ

**Comment choisir Bouchon réservoir de carburant compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Bouchon réservoir de carburant ?**
En cas de odeur de carburant persistante ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Bouchon réservoir de carburant sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
