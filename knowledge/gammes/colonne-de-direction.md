---
category: direction
slug: colonne-de-direction
title: Colonne de direction
pg_id: 1211
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
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Relier le volant a la cremailliere - Transmet la rotation du conducteur au systeme de direction
  must_be_true:
  - relier
  - transmettre
  - connecter
  must_not_contain:
  - suspension
  - amortissement
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - cremailliere-de-direction
  - rotule-de-direction
  - pompe-de-direction-assistee
  - barre-de-direction
  - soufflet-de-direction
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
  - ❌ "securite garantie"
  cost_range:
    min: 200
    max: 500
    currency: EUR
    unit: colonne
    source: catalogue automecanik
  quality_tiers:
  - tier: Equipement d origine (OE)
  - tier: Equivalent OE
  - tier: Piece reconditionnee
  brands:
    premium:
    - Lemforder
    - TRW
    standard:
    - Febi
    - Meyle
    - MOOG
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Jeu important du volant vertical ou lateral
    severity: confort
  - id: S2
    label: Craquements ou bruits secs en tournant le volant
    severity: confort
  - id: S3
    label: Volant qui ne revient pas seul apres un virage
    severity: confort
  - id: S4
    label: Bruits de frottement dans la colonne
    severity: confort
  - id: S5
    label: Voyant direction assistee allume
    severity: securite
  - id: S6
    label: Sensation de points durs en tournant
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  quick_checks:
  - 'Observer : jeu important du volant vertical ou lateral ?'
  - 'Observer : craquements ou bruits secs en tournant le volant ?'
  - 'Observer : volant qui ne revient pas seul apres un virage ?'
  - Bruits de frottement dans la colonne ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Jeu important du volant vertical ou lateral
  - Craquements ou bruits secs en tournant le volant
  - Volant qui ne revient pas seul apres un virage
  - Bruits de frottement dans la colonne
  - Voyant direction assistee allume
  - Sensation de points durs en tournant
  good_practices:
  - Controle du jeu de direction a chaque revision
  - Verifier les soufflets de protection (pas de fuite de graisse)
  - Faire verifier la geometrie apres remplacement
  - Inspecter les biellettes et rotules associees
rendering:
  pgId: '1211'
  intro_title: A quoi sert Colonne de direction ?
  risk_title: Pourquoi remplacer Colonne de direction a temps ?
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
  - question: Colonne de direction OE ou adaptable ?
    answer: Privilégiez l'OE ou l'échange standard. C'est une pièce de sécurité critique. Les copies peuvent avoir des jeux
      importants.
  - question: Comment savoir si ma colonne de direction est usée ?
    answer: Jeu vertical ou latéral du volant, craquements en tournant, bruits de frottement, direction assistée qui grogne.
  - question: Tous les combien changer la colonne de direction ?
    answer: Pas de périodicité fixe. Durée de vie très longue (200 000+ km). Remplacement uniquement en cas de défaut avéré.
  - question: Peut-on changer la colonne de direction soi-même ?
    answer: Déconseillé. Opération complexe impliquant l'airbag et l'électronique. Nécessite calibrage sur véhicules récents.
  - question: Quelle erreur éviter avec la colonne de direction ?
    answer: Ne pas toucher au système sans débrancher la batterie (airbag). Faire recalibrer l'angle volant après intervention.
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
doc_id: 3ffea5f8-858f-52f2-8570-2fc58fd3d122
content_hash: sha256:2a160b7856e7456e
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
  area: Sous le vehicule, relie le volant aux roues
  access: Par le dessous (pont elevateur recommande)
  adjacent_parts:
  - cremailliere
  - biellette
  - rotule
  - soufflet
installation:
  difficulty: difficile
  time: 1h a 3h
  tools:
  - cle a douille
  - arrache-rotule
  - cle dynamometrique
  prerequisite: Pont elevateur, geometrie a refaire apres
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_2_2_v: '2.2 V'
    val_40_km: '40 km'
    val_50_a: '50 A'
    val_60_km: '60 km'
    val_7_a: '7 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'La colonne de direction est située entre le volant et lacrémaillère de direction son rôle et de transmettre le mouvement
    de rotationappliquée par le conducteur à la crémaillère qui va permettre l''actionnementdes barres de direction en translation
    droite ou gauche pour le braquage desroues. La colonne de direction est constituée d''un axe guidé àl''intérieur d''un
    fourreau, solidaire du volant. A l''extrémité inférieure lacolonne de direction est liée à un cardan pour autoriser le
    renvoi d''angle àl''entrée de la crémaillère de direction. La colonne dedirection possède plusieurs autres fonctions dans
    un véhicule : - Support des commandes au volant (commande d''éclairage et commandes d''essuie-glace). - Support pour les
    habillages de protection. - Elle intègre le neiman et le dispositif de réglage enhauteur et en longueur du volant. - Sur
    les nouvelles voitures aussi la colonne de direction comporte aussi le capteurde couple et le capteur d''angle pour l''assistance
    dedirection. - Pour les véhicules à système de direction assistée électriques le moteurélectrique est souvent monté sur
    la colonne de direction. En savoir plus : colonne de direction — définition et rôle mécanique 🚨 Bruit Colonne de direction
    : causes et diagnostic'
  S2: 'Une colonne de direction défectueuse présente plusieurs symptômes : Symptômes mécaniques : - Jeu vertical ou latéral
    du volant — le volant bouge sans que les roues répondent. Testez en secouant le volant moteur arrêté. - Craquements ou
    bruits secs en tournant le volant, surtout à basse vitesse ou en manœuvre. - Volant qui ne revient pas seul après un virage
    — le rappel est mou ou inexistant. - Points durs — sensation de crantage en tournant, typique d''un cardan de colonne
    usé. - Bruits de frottement dans la colonne, aggravés sur route dégradée. Symptômes électriques (direction assistée électrique)
    : - Voyant direction assistée allumé — défaut du moteur électrique ou du calculateur intégré à la colonne. - Direction
    qui se coupe brusquement lors d''un braquage à fond ou sur une bosse. - Direction qui reste dure malgré plusieurs redémarrages.
    Pièces impactées par une colonne HS : - Crémaillère de direction — contraintes anormales si jeu dans la colonne. - Rotule
    de direction — usure accélérée. - Pompe de direction assistée — surcharge si résistance dans la colonne. ⚠️ Sécurité :
    toute perte de contrôle directionnelle est un risque immédiat. Faites diagnostiquer sans attendre. Diagnostic complet
    : identifier une panne de colonne de direction Tests à réaliser : - Test du jeu radial — moteur arrêté, secouez le volant
    haut/bas et gauche/droite. Plus de 2 cm de jeu sans mouvement des roues = colonne à remplacer. - Test en roulage — sur
    route droite, le volant doit rester stable. S''il vibre ou dévie sans raison, la colonne ou le cardan intermédiaire est
    en cause. - Test du rappel — après un virage à 90°, lâchez le volant : il doit revenir seul et progressivement. Un retour
    lent ou absent indique un problème dans la colonne ou la crémaillère. - Contrôle visuel — inspectez les soufflets du cardan
    intermédiaire sous le tableau de bord. Toute déchirure ou trace de graisse = cardan HS.'
  S3: 'La colonne de direction transmet mécaniquement ou électromécaniquement la rotation du volant vers la crémaillière.
    C''est une pièce de sécurité active : un jeu excessif du volant ou un grippage de la colonne impacte directement la précision
    de braquage, notamment aux vitesses autoroutières. La sélection doit prendre en compte le type de direction (mécanique,
    assistée hydraulique, assistée électrique EPAS) car ces trois technologies ont des colonnes structurellement différentes.
    - Identifier le type de direction assistée avant toute commande : direction mécanique (sans assistance), direction hydraulique
    (pompe hydraulique entraînée par courroie), ou direction électrique (moteur électrique intégré dans la colonne ou sur
    la crémaillière). Ces trois types utilisent des colonnes incompatibles — une colonne EPAS comporte un moteur électrique
    et un capteur de couple intégré absents d''une colonne mécanique. - Colonne simple ou à réglage (inclinable/télescopique)
    : les véhicules équipés d''un réglage de volant (inclinaison, profondeur) utilisent une colonne articulée avec des mécanismes
    de blocage par came ou à crémaillière. Remplacer une colonne articulée par une colonne fixe supprime les réglages d''ergonomie
    et peut nécessiter une adaptation des fixations. - Cardan de direction intermédiaire : angle et longueur : la colonne
    est reliée à la crémaillière par un cardan (joint de cardan à croisillon ou à roulement sphérique). Cet élément doit être
    remplacé si le jeu ou le grincement provient de cette zone. L''angle de travail du cardan (généralement entre 5° et 25°)
    détermine le type de joint compatible. - Capteur de couple et d''angle intégré (colonnes EPAS) : sur les véhicules à direction
    assistée électrique, la colonne intègre un ou deux capteurs (angle absolu et couple de braquage) connectés à l''unité
    de commande de direction. Ces capteurs doivent être compatibles avec le protocole CAN bus du véhicule. Après remplacement,
    une calibration du capteur d''angle est systématiquement requise avec un outil de diagnostic. - Coussinet de palier de
    colonne et bague anti-bruit : les bruits de frottement en tournant le volant proviennent fréquemment d''un coussinet de
    palier plastique usé plutôt que d''une colonne entière défaillante. Vérifier si le coussinet est disponible séparément
    — remplacer ce seul élément peut résoudre 70 % des cas de bruits à moindre coût. - Compatibilité airbag et commodos de
    colonne : la colonne de direction supporte la bague de contact tournante (relais spiralé) de l''airbag conducteur et les
    connecteurs des commodos (clignotants, klaxon, régulateur de vitesse). Une colonne de remplacement doit impérativement
    avoir les mêmes points d''ancrage pour ces équipements — vérifier la liste des options du véhicule (airbag, régulateur,
    radio au volant). - Couple de serrage des raccords universels (cardans) : le boulon de serrage du cardan sur la crémaillière
    (M10 typiquement, couple de 24 à 30 Nm) doit être neuf à chaque démontage — c''est généralement un boulon auto-freiné
    à usage unique. Vérifier si le kit de remplacement inclut cette visserie ou si elle est à commander séparément. Pour aller
    plus loin : consultez notre guide d''achat colonne de direction — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Colonne de direction pour connaître les spécifications. - Débranchez
    la batterie. - Démontez l'airbag conducteur si équipé. - Débranchez les connecteurs électriques auniveau du volant de
    direction. - Démontez le volant de direction. - Démontez l'ensemble de commande sous levolant (manette de clignotant et
    d'essuie- glace ). - Si le véhicule est équipé d'une clé decontact il faut débranchez le connecteur du contacteur, dégagez
    le faisceauélectrique de la colonne et démontez le neiman. - Si le véhicule est équipé d'une cartedébranchez le connecteur
    de la colonne de direction, démontez la vis defixation du verrou électrique de la colonne puis démontez le verrou. - Démontez
    l'écrou du cardan de la colonnede direction en dessous du tapis en bas de la colonne de direction. - Démontez le tableau
    de bord si nécessaire. - Démontez les écrous de fixation supérieurede la colonne de direction. - Démontez la colonne de
    direction de latraverse du tableau de bord. - Retirez avec précaution la colonnedirection vers soit.
  S4_REPOSE: '- Vérifier que la nouvelle colonne dedirection est identique à celle démontée. - Contrôlez le bon fonctionnement
    de lapompe de direction assistée. - Contrôlez le bon fonctionnement de lacrémaillère de direction. - Remontez la colonnede
    direction. - Remontez les écrous de lacolonne de direction. - Remontez le cardaninférieur de la colonne de direction.
    - Remontez le neiman ou leverrou électrique. - Rebranchez tous lesconnecteurs débranchez. - Remontez la commande sousle
    volant. - Remontez le volant dedirection. - Remontez l''airbagconducteur. - Rebranchez la batterie. - Contrôlez le bonfonctionnement
    de la direction. ✅ Après remontage, vérifiez les spécifications dans la fiche technique Colonne de direction.'
  S5: 'Erreurs fréquentes lors du remplacement d''une colonne de direction : - ❌ Ne pas débrancher la batterie avant intervention
    — l''airbag est intégré à la colonne. Risque de déclenchement accidentel. Attendre 10 min après débranchement. - ❌ Oublier
    le recalibrage de l''angle volant — sur les véhicules récents (ESP, aide au stationnement), le capteur d''angle doit être
    réinitialisé à la valise après repose. - ❌ Forcer sur les vis de serrage — les cannelures du cardan de colonne sont fragiles.
    Couple de serrage constructeur obligatoire. - ❌ Confondre colonne et crémaillère — un jeu au volant peut venir de la crémaillère,
    des rotules ou des biellettes. Diagnostiquer avant de commander. - ❌ Monter une colonne sans direction assistée sur un
    véhicule assisté (et inversement) — vérifier le type exact : mécanique, hydraulique ou électrique. - ❌ Ignorer les bruits
    après montage — un claquement résiduel signale souvent un cardan mal engagé ou un silent- bloc manquant.'
  S6: 'Après le remplacement de votre colonne de direction, effectuez ces vérifications dans l''ordre. - Vérifiez le serrage
    de l''accouplement cannelé entre la colonne et la crémaillière au couple préconisé : aucun jeu axial ou angulaire ne doit
    être perceptible à la main. - Contrôlez le centrage du volant : les rayons doivent être symétriques en ligne droite avant
    de rouler — ajustez si nécessaire en déposant le volant et repositionnant l''airbag. - Vérifiez le branchement du connecteur
    de l''ensemble commodo-contacteur tournant (airbag) : verrouillage en place, aucun code airbag au tableau de bord. - Démarrez
    le moteur et faites tourner le volant de butée à butée lentement : aucun craquement, point dur ni frottement dans la colonne.
    - Contrôlez que le voyant direction assistée s''éteint bien après démarrage et ne réapparaît pas lors des manoeuvres.
    - Effectuez un essai routier à faible allure en virage : le volant doit revenir spontanément en position droite après
    un virage à vitesse stabilisée. Consultez également la page références colonne de direction pour identifier la pièce compatible
    avec votre véhicule.'
  S7: 'Combien coûte le changement d''une colonne de direction ? La pièce seule coûte entre 150 € et 600 € selon le véhicule
    (mécanique ou électrique). La main-d''œuvre représente 2 à 4 heures, soit 150 à 400 € en garage. Au total, comptez 300
    à 1 000 € selon la complexité (colonne avec direction assistée électrique = plus cher). Quelle est la différence entre
    colonne de direction mécanique et électrique ? La colonne mécanique transmet directement la rotation du volant à la crémaillère
    via un cardan. La colonne électrique (EPS) intègre un moteur d''assistance et un capteur de couple — elle est plus légère
    et supprime le circuit hydraulique, mais son remplacement est plus coûteux et nécessite souvent une calibration électronique.
    Peut-on passer le contrôle technique avec une colonne de direction usée ? Un jeu excessif au volant ou un voyant direction
    allumé est un défaut majeur au contrôle technique. La colonne de direction est un organe de sécurité critique : tout jeu
    anormal, craquement ou point dur entraîne un refus ou une contre-visite obligatoire. Quels sont les premiers signes d''usure
    d''une colonne de direction ? Les signes avant-coureurs sont : jeu vertical ou latéral au volant, craquements en tournant,
    volant qui ne revient pas seul après un virage, sensation de points durs. Sur les colonnes électriques, le voyant EPS
    s''allume en cas de défaillance du capteur de couple ou du moteur. - Crémaillère de direction — si jeu dans la colonne,
    les efforts anormaux usent la crémaillère prématurément. Vérifiez l''absence de fuite d''huile de DA. - Pompe de direction
    assistée — une colonne grippée surcharge la pompe. Contrôlez le niveau et la couleur du fluide hydraulique. - Rotule de
    direction — un jeu dans la colonne masque souvent un jeu en rotule. Vérifiez en soulevant la roue et en testant le jeu
    latéral. - Cardan de colonne de direction — les craquements en tournant proviennent souvent du cardan intermédiaire. Pièce
    à contrôler systématiquement lors du diagnostic. 📖 Fiche technique Colonne de direction — intervalles et spécifications
    d''entretien.'
  S8: 'Colonne de direction OE ou adaptable ?Privilégiez l''OE ou l''échange standard. C''est une pièce de sécurité critique.
    Les copies peuvent avoir des jeux importants dès le montage. Marques fiables : TRW, Lemförder, Febi Bilstein. Comment
    savoir si ma colonne de direction est usée ?Jeu vertical ou latéral du volant moteur arrêté, craquements en tournant à
    basse vitesse, volant qui ne revient pas seul après un virage, voyant direction assistée allumé. Tous les combien changer
    la colonne de direction ?Pas de périodicité fixe. Durée de vie très longue (200 000+ km). Remplacement uniquement en cas
    de jeu avéré, bruit ou voyant. Certaines colonnes électriques ont un moteur d''usure. Peut-on changer la colonne de direction
    soi-même ?Déconseillé. L''airbag est logé dans la colonne — il faut débrancher la batterie et attendre 10 min. Sur les
    véhicules récents, un recalibrage du capteur d''angle volant est nécessaire à la valise. Quel est le prix moyen d''une
    colonne de direction ?Entre 120 € et 1 200 € selon le modèle. Les colonnes avec direction assistée électrique intégrée
    sont les plus chères. Comptez 1 à 3h de main-d''œuvre en atelier.'
  META: '{"og_title": "Colonne de direction : 3 tests pour diagnostiquer un jeu au volant", "meta_title": "Colonne de direction
    : symptômes, changement et prix | AutoMecanik", "gate_report": "PASS", "schema_type": "HowTo", "og_description": "Jeu
    au volant ou craquements ? 3 tests simples pour diagnostiquer une colonne de direction HS. Causes, coût et pièces compatibles.",
    "primary_intent": "diagnostic", "char_count_desc": 148, "char_count_title": 59, "meta_description": "Jeu au volant, craquements
    en tournant ? Diagnostiquez votre colonne de direction en 3 tests. Causes d''usure, coût moyen et pièces compatibles."}'
---

# Colonne de direction - Guide Diagnostic Complet

## Fonction et Rôle

Relier le volant a la cremailliere - Transmet la rotation du conducteur au systeme de direction

**Actions principales:** relier, transmettre, connecter, vehiculer la rotation

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant direction assistee allume**
  voyant direction assistee allume

### 🟢 Autres Symptômes

- jeu important du volant vertical ou lateral
- craquements ou bruits secs en tournant le volant
- volant qui ne revient pas seul apres un virage
- bruits de frottement dans la colonne
- sensation de points durs en tournant

## Procédure de Diagnostic

Pour diagnostiquer un problème de colonne de direction:

1. **Inspection visuelle** - Examiner l'état du colonne de direction
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

- cremailliere-de-direction
- pompe-de-direction-assistee
- rotule-de-direction

## Critères de Compatibilité

Pour commander le bon colonne de direction, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"

## FAQ

**Colonne de direction OE ou adaptable ?**
Privilégiez l'OE ou l'échange standard. C'est une pièce de sécurité critique. Les copies peuvent avoir des jeux importants.

**Comment savoir si ma colonne de direction est usée ?**
Jeu vertical ou latéral du volant, craquements en tournant, bruits de frottement, direction assistée qui grogne.

**Tous les combien changer la colonne de direction ?**
Pas de périodicité fixe. Durée de vie très longue (200 000+ km). Remplacement uniquement en cas de défaut avéré.

**Peut-on changer la colonne de direction soi-même ?**
Déconseillé. Opération complexe impliquant l'airbag et l'électronique. Nécessite calibrage sur véhicules récents.

**Quelle erreur éviter avec la colonne de direction ?**
Ne pas toucher au système sans débrancher la batterie (airbag). Faire recalibrer l'angle volant après intervention.
## Symptômes au volant

### Volant dur
- **Direction assistée défaillante** : Pompe DA qui siffle ou ne fournit plus assez de pression. Vérifier le niveau de liquide DA et l'état de la courroie.
- **Crémaillère grippée** : Corrosion interne ou manque de lubrification. Le volant est dur dans les deux sens, surtout à froid.
- **Colonne de direction usée** : Cardan de direction grippé, surtout après un long stationnement.

### Jeu dans le volant
- **Rotules de direction usées** : Jeu perceptible en tournant le volant sans que les roues bougent. Contrôler visuellement le jeu en secouant la roue.
- **Biellettes de direction desserrées** : Claquement en manœuvrant, jeu latéral au volant.
- **Crémaillère avec jeu interne** : Usure des pignons ou des bagues de guidage.

### Bruits en braquant
- **Craquement dans les virages** : Soufflet de cardan déchiré, graisse partie, croisillon usé.
- **Grincement à basse vitesse** : Roulements de butée d'amortisseur ou coupelles supérieures usées.
- **Sifflement continu** : Pompe de direction assistée en fin de vie ou niveau de liquide bas.

## Fuites de direction

### Fuite de liquide DA
- **Au niveau du bocal** : Joint de bouchon ou bocal fissuré.
- **Sur les raccords** : Durites de pression ou retour qui fuient aux colliers.
- **Sur la crémaillère** : Joints spy de crémaillère usés, fuite visible aux soufflets.

## Vérifications simples

- Contrôler le niveau de liquide de direction assistée (bocal sous le capot)
- Inspecter les soufflets de crémaillère (pas de déchirure, pas de fuite)
- Secouer la roue à 9h-15h pour détecter le jeu dans les rotules
- Tourner le volant moteur allumé : le mouvement doit être fluide et silencieux

## Quand consulter un professionnel

- Volant qui vibre ou tire d'un côté en ligne droite
- Bruit métallique constant dans la direction
- Fuite importante de liquide DA (risque de blocage)
- Jeu excessif au volant détecté au contrôle technique
