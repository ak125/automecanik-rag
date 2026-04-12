---
category: transmission
slug: cardan
title: Cardan
pg_id: 13
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-03'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Transmet le couple moteur aux roues tout en permettant les mouvements de suspension
  must_be_true:
  - transmettre
  - entrainer
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
  - joint-arbre-longitudinal
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
  - ❌ "plus de puissance"
  cost_range:
    min: 100
    max: 350
    currency: EUR
    unit: cardan complet
    source: catalogue automecanik
  brands:
    premium:
    - SKF
    - GKN/Spidan
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Claquement braquant accelerant marche arriere
    severity: confort
  - id: S2
    label: Vibrations ressenties vitesse constante
    severity: confort
  - id: S3
    label: Graisse noire visible jante passage
    severity: confort
  - id: S4
    label: Soufflet de cardan dechire ou fendu visible
    severity: confort
  - id: S5
    label: Bruit roulement change selon angle
    severity: confort
  - id: S6
    label: Plus de 150 000 km sans verification des soufflets
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : claquement braquant accelerant marche arriere ?'
  - Vibrations ressenties vitesse constante ?
  - 'Observer : graisse noire visible jante passage ?'
  - 'Observer : soufflet de cardan dechire ou fendu visible ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Claquement braquant accelerant marche arriere
  - Vibrations ressenties vitesse constante
  - Graisse noire visible jante passage
  - Soufflet de cardan dechire ou fendu visible
  - Bruit roulement change selon angle
  - Plus de 150 000 km sans verification des soufflets
  good_practices:
  - Verifier le niveau d huile de boite selon preconisation constructeur
  - Controle des soufflets de protection (pas de fuite de graisse)
  - Remplacement de la bague d etancheite en cas de fuite
  - Inspection des cardans et croisillons a chaque revision
rendering:
  pgId: '13'
  intro_title: A quoi sert Cardan ?
  risk_title: Pourquoi remplacer Cardan a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
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
  - question: Cardan OE, OES ou échange standard ?
    answer: Les cardans OES (SKF, GKN, Lobro) sont de qualité équivalente à l'OE. L'échange standard est 30-50% moins cher
      avec une qualité similaire.
  - question: Comment savoir si mon cardan est usé ?
    answer: Claquement en braquant et accélérant (manœuvres), vibrations à vitesse constante, graisse visible sur la jante
      ou sous le passage de roue.
  - question: Tous les combien changer le cardan ?
    answer: Pas de périodicité fixe. Un cardan avec soufflets intacts peut durer 200 000+ km. À remplacer dès qu'un joint
      claque ou vibre.
  - question: Peut-on changer un cardan soi-même ?
    answer: Oui mais technique. Dépose roue, étrier, moyeu. Attention à la vis de moyeu (très serrée, souvent à usage unique).
      Prévoir 2h par côté.
  - question: Quelle erreur éviter avec le cardan ?
    answer: Ne pas réutiliser l'écrou de moyeu usagé. Vérifier les soufflets avant de changer le cardan complet. Ne pas forcer
      sur le joint.
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
doc_id: bc2e108d-c21a-5f6c-b590-75411650de5a
content_hash: sha256:718a4b1bdda0e76f
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
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: Hall
    source_ref: corpus RAG web OEM
  - type: hall
    source_ref: corpus RAG web OEM
  technical_notes:
    val_10_v: 10 v
    val_1990__v: 1990, V
    val_2286441_v: 2286441 v
    val_25_a: 25 a
    val_36_a: 36 a
    val_70_a: 70 a
    val_75_a: 75 a
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Dansun véhicule les cardans ont pour rôle de transmettre l''effortde rotation du moteur à la motricité des roues du
    véhicule, en permettant enmême temps une légère flexibilité et le braquage des roues avant. En savoir plus : cardan —
    définition et rôle mécanique 🚨 Fuite de cardan : que vérifier'
  S2: '- Levez et calez levéhicule. - Braquez la roue ducoté concernée à fond. - Examiner l''état dusoufflet de cardan sur
    toute la périphérie en tournant la roue lentement : - Si vous constatezla présence de graisse, c''est que le soufflet
    de cardan n''est plus étanche. - Le soufflet decardan ne doit présenter aucune fissure. Sinon il faudra le remplacer.
    - Vérifiez l''état dela bague d''étanchéité de cardan côté boîte de vitesses (fuite d''huile). - Si vous constatezun jeu
    entre l''arbre et la tête de cardan (bruit de claquement), le cardan estdéfaillant Diagnostic complet : identifier une
    panne de cardan'
  S2_DIAG: SymptômeCause probableActionUn bruit anormal au niveau du cardan peut se manifester lors de la phase "acceleration"Pour
    identifier ce probleme de bruit du cardan:Verification visuelle du cardanDes vibrations provenant du cardan sont souvent
    perceptibles a haute vitessePour identifier ce probleme de vibration du cardan:Verification visuelle du cardan
  S3: 'Le cardan (arbre de transmission) transmet le couple moteur de la boîte de vitesses aux roues. C''est une pièce critique
    dont les dimensions doivent correspondre exactement au véhicule.Vérifications indispensables- Nombre de cannelures : côté
    boîte (21, 22, 25, 28 cannelures selon modèle) et côté moyeu (26, 28, 30, 36 cannelures)- Longueur totale : mesurer le
    cardan déposé de bout en bout (tolérance ± 5 mm)- Type de joint : tripode côté boîte + homocinétique côté roue, ou double
    homocinétique — la combinaison doit être identique- Côté du véhicule : cardan gauche souvent plus long que le droit (présence
    d''un arbre intermédiaire)- Présence d''ABS : certains cardans intègrent une bague ABS magnétique ou dentéeMéthode de
    vérificationComparer la référence OE. Compter les cannelures des deux côtés. Mesurer la longueur et vérifier la présence
    ou non de la bague ABS sur l''ancien cardan.Pour aller plus loin : consultez notre guide d''achat cardan — comparatif
    marques, critères de choix et prix.'
  S4_DEPOSE: '📖 Avant de démonter, consultez la fiche technique Cardan pour connaître les spécifications. - Levez et calez
    le véhicule. - Démontez la roue. - Vidanger la boîte de vitesses. - Dévissez l''écrou ou lavis centrale qui maintien le
    cardan dans le moyeu de roue. - Dans le cas d''un écroufrein à goupille il faut démontez la goupille puis l''écrou. -
    Démontez le cardancôté roue. - Si le cardan est vissécôté boîte de vitesses, desserrez les vis de fixation du cardan côté
    boîte devitesses. - Retirer le cardan. - Dans le cas où lecardan n''est pas vissé à la boîte de vitesse ou au différentiel
    : - Désaccoupler le bras desuspension, si nécessaire. - Écarter la fusée d''essieu. - Désaccoupler la tête decardan du
    moyeu. - Retirez le cardan en désaccouplant l''autreextrémité côté boîte de vitesse ou différentiel. - Il existe des modèles
    oùle cardan est soutenu par un pallier à roulement, situé au milieu et fixé aubloc moteur il faut le démontez afin de
    sortir le cardan.'
  S4_REPOSE: '- Contrôler le cardanneuf avec celui démonté (longueur, le nombre de dents et la présence de lacouronne ABS
    si le véhicule équipé). - Remplacez la bagued''étanchéité de cardan côté boîte de vitesses. - Refaire le niveaud''huile
    de la boîte de vitesses. - Graissez le cardanavant de le remontez. - Remontez le cardancôté boîte de vitesses et côté
    roue. - Resserrez les vis defixation et l''écrou du cardan. - Remettre la goupillede l''écrou du cardan. - Remontez la
    roue. - Redescendre le véhicule. - Resserrer la roue. - Faire un essai routier pour contrôler le bonfonctionnement du
    cardan. ✅ Après remontage, vérifiez les spécifications dans la fiche technique Cardan.'
  S5: '- Inverser le cardan gauche et droit — les longueurs sont souvent différentes et les cannelures peuvent ne pas correspondre
    → vérifier le côté (L/R) marqué sur l''emballage et comparer la longueur avec le cardan déposé- Forcer l''insertion dans
    la boîte de vitesses — le joint spy de boîte sera endommagé et l''huile fuira → aligner les cannelures, pousser à la main
    jusqu''au clip de retenue (clic audible)- Oublier la bague ABS — le voyant ABS restera allumé et le système de freinage
    d''urgence sera inopérant → vérifier la présence et l''orientation de la bague ABS avant montage- Ne pas remplacer l''écrou
    de moyeu — l''ancien écrou a perdu sa capacité de freinage, risque de desserrage → utiliser un écrou neuf et le serrer
    au couple constructeur (175-280 Nm)- Oublier de vidanger partiellement la boîte — l''huile de boîte coule au retrait du
    cardan et se perd → prévoir un bac de récupération et faire l''appoint d''huile après remontage- Laisser tomber le cardan
    neuf — un choc sur le joint homocinétique peut créer un méplat invisible qui provoquera des vibrations → manipuler avec
    précaution, ne jamais poser sur le joint- Monter un cardan sans graisse suffisante — les joints neufs sont pré-graissés
    mais vérifier que la graisse n''a pas été expulsée du soufflet → s''assurer que les soufflets sont gonflés normalement-
    Ne pas contrôler le joint spy de boîte — un joint spy usé fuira dès la réinsertion du cardan → inspecter et remplacer
    le joint spy s''il est dur, craquelé ou fuyant'
  S6: 'Contrôles statiques (véhicule au sol)- Vérifier le serrage de l''écrou de moyeu au couple constructeur (175-280 Nm
    selon modèle)- Contrôler que le cardan est correctement clipsé dans la boîte (tirer fermement : il ne doit pas sortir)-
    Inspecter l''absence de fuite d''huile de boîte côté joint spy- Vérifier le niveau d''huile de boîte de vitesses et faire
    l''appoint si nécessaire- Contrôler que le voyant ABS est éteint après démarrage (si bague ABS présente)Test routier progressif-
    Rouler à 20 km/h en braquant à fond : aucun claquement (signe de joint homocinétique défectueux)- Accélérer franchement
    en 1ère et 2nde : pas d''à-coup ni de vibration dans le plancher- Rouler à 90 km/h en ligne droite : absence de vibration
    périodique (cardan mal équilibré ou cannelures mal engagées)- Freiner fermement : vérifier que l''ABS fonctionne correctement⚠️
    Important : Tout claquement en virage après montage indique un problème de joint. Si le cardan est neuf, vérifier l''insertion
    côté boîte. Si le bruit persiste, le cardan peut être défectueux (rare mais possible sur pièce remanufacturée).'
  S7: Lors du remplacement d'un cardan, inspectez systématiquement ces pièces connexes :- Soufflet de cardan — sur un cardan
    neuf les soufflets sont inclus, mais sur un cardan échange standard vérifier leur état- Roulement de roue — un roulement
    usé crée du jeu qui accélère l'usure du cardan, vérifier l'absence de jeu radial- Écrou de moyeu — toujours remplacer
    par un écrou neuf (auto-freiné ou à créneaux avec goupille)- Joint spy de boîte de vitesses — remplacer s'il fuit ou s'il
    est dur au toucher, coût faible et accès facile cardan déposé- Huile de boîte de vitesses — prévoir un appoint (0,3-0,5
    L) car l'huile s'écoule au retrait du cardan- Rotule de suspension — souvent accessible lors de la dépose du cardan, vérifier
    le jeu- Capteur ABS — si le voyant ABS reste allumé après montage, vérifier le capteur et la bague magnétique
  S8: Comment savoir si mon cardan est usé ?Le symptôme le plus courant est un claquement métallique en tournant le volant,
    surtout en accélérant dans un virage serré (manœuvre de parking). Une vibration à vitesse constante (80-100 km/h) peut
    indiquer un cardan déséquilibré. De la graisse noire projetée sur le passage de roue signale un soufflet déchiré.Cardan
    neuf ou cardan échange standard ?Un cardan neuf offre la meilleure garantie de qualité et de durée de vie (garantie 2-5
    ans). Un cardan échange standard (reconditionné) coûte 30-50 % moins cher mais sa durée de vie est variable. Pour un véhicule
    récent ou à fort kilométrage annuel, privilégiez le neuf.Faut-il changer les deux cardans en même temps ?Non, sauf si
    les deux présentent des symptômes. Le cardan est une pièce robuste (150 000-250 000 km). Remplacer un seul côté est courant
    et ne pose aucun problème d'équilibre, contrairement aux amortisseurs ou aux plaquettes de frein.Peut- on rouler avec
    un cardan qui claque ?C'est dangereux. Un cardan usé peut se bloquer ou se désolidariser, entraînant une perte totale
    de motricité et un danger immédiat. Dès les premiers claquements, faites diagnostiquer et remplacer la pièce sans tarder.Le
    remplacement du cardan nécessite-t-il un passage au contrôle technique ?Non, mais le contrôle technique vérifie l'état
    des soufflets et des joints de cardan. Un soufflet déchiré est un motif de contre-visite. Après remplacement, votre véhicule
    sera conforme sur ce point.
  META: '- Changer Cardan de la Renault Clio II 1.2 16V.'
---

# Cardan - Guide Diagnostic Complet

## Fonction et Rôle

Transmet le couple moteur aux roues tout en permettant les mouvements de suspension

**Actions principales:** transmettre, entrainer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement braquant accelerant marche arriere**
  claquement braquant accelerant marche arriere

### 🟢 Autres Symptômes

- vibrations ressenties vitesse constante
- graisse noire visible jante passage
- soufflet de cardan dechire ou fendu visible
- bruit roulement change selon angle
- plus de 150 000 km sans verification des soufflets

## Procédure de Diagnostic

Pour diagnostiquer un problème de cardan:

1. **Inspection visuelle** - Examiner l'état du cardan
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- bague-d-etancheite-cardan
- soufflet-de-cardan

## Critères de Compatibilité

Pour commander le bon cardan, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"

## FAQ

**Cardan OE, OES ou échange standard ?**
Les cardans OES (SKF, GKN, Lobro) sont de qualité équivalente à l'OE. L'échange standard est 30-50% moins cher avec une qualité similaire.

**Comment savoir si mon cardan est usé ?**
Claquement en braquant et accélérant (manœuvres), vibrations à vitesse constante, graisse visible sur la jante ou sous le passage de roue.

**Tous les combien changer le cardan ?**
Pas de périodicité fixe. Un cardan avec soufflets intacts peut durer 200 000+ km. À remplacer dès qu'un joint claque ou vibre.

**Peut-on changer un cardan soi-même ?**
Oui mais technique. Dépose roue, étrier, moyeu. Attention à la vis de moyeu (très serrée, souvent à usage unique). Prévoir 2h par côté.

**Quelle erreur éviter avec le cardan ?**
Ne pas réutiliser l'écrou de moyeu usagé. Vérifier les soufflets avant de changer le cardan complet. Ne pas forcer sur le joint.
## Boîte manuelle

### Craquement au passage de vitesse
- **Synchroniseurs usés** : Craquement surtout sur un rapport précis (souvent 2ème ou 3ème). Pire à froid, s'améliore à chaud.
- **Huile de boîte inadaptée ou usée** : Vidange de boîte à effectuer (75W-80 ou 75W-90 selon constructeur).
- **Câble ou timonerie de commande usé** : Passage imprécis, sensation de flou dans le levier.

### Vitesse qui saute
- **Fourchette de sélection usée** : La vitesse se désengage spontanément sous charge.
- **Ressort de verrouillage cassé** : Le rapport ne tient plus en position.

### Bruit de roulement en boîte
- **Roulement d'arbre primaire usé** : Sifflement continu qui disparaît quand on appuie sur l'embrayage.
- **Roulement de sortie** : Bruit proportionnel à la vitesse du véhicule.

## Boîte automatique

### À-coups ou patinage
- **Niveau d'huile ATF incorrect** : Vérifier le niveau à chaud, moteur tournant au point mort.
- **Huile ATF usée** : Couleur marron foncé au lieu de rouge. Vidange recommandée.
- **Convertisseur de couple usé** : Patinage au démarrage, surchauffe de l'huile.

### Passage de rapports brutal
- **Calculateur de boîte** : Réinitialisation des adaptations parfois nécessaire.
- **Électrovannes de commande** : Corps de vannes encrassé ou électrovanne bloquée.

## Cardans et transmission

### Claquement en virage
- **Soufflet de cardan déchiré** : Graisse projetée visible sur la roue intérieure. Le cardan tourne sans lubrification.
- **Croisillon de cardan usé** : Claquement sec en accélération ou décélération dans les virages.

### Vibration à l'accélération
- **Cardan voilé** : Vibration proportionnelle à la vitesse.
- **Silent-bloc de transmission usé** : Vibrations transmises dans l'habitacle.

## Quand consulter un professionnel

- Boîte automatique en mode dégradé (bloquée sur un rapport)
- Fuite d'huile de boîte importante
- Craquement systématique sur tous les rapports
- Cardan cassé (roue qui ne tourne plus)
