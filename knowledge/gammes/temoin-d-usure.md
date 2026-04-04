---
category: freinage
slug: temoin-d-usure
title: Témoin d'usure
pg_id: 407
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
  role: Signale l'usure des plaquettes de frein
  must_be_true:
  - signaler
  - alerter
  - indiquer
  must_not_contain:
  - injection
  - climatisation
  - embrayage
  - distribution
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
  - term: piece-de-freinage-voisine
    difference: 'Verifier la reference exacte : les pieces de freinage se ressemblent mais ne sont pas interchangeables entre
      essieux ou types de montage.'
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
  - ❌ "améliore le freinage"
  cost_range:
    min: 6
    max: 17
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  brands:
    premium:
    - Brembo
    - ATE (Continental)
    - TRW
    standard:
    - Textar
    - Bosch
    - Jurid
    budget:
    - A.B.S.
    - NK
    - Delphi
  quality_tiers:
  - tier: Origine constructeur
    description: Temoins d usure identiques a la premiere monte, avec connecteur et longueur de cable calibres pour le vehicule.
  - tier: Equipementier qualite OE
    description: Temoins fabriques selon les specifications constructeur avec connecteur et resistance electrique conformes.
  - tier: Adaptable qualite reconnue
    description: Temoins compatibles avec verification du type de connecteur et de la longueur de cable avant montage.
diagnostic:
  symptoms:
  - id: S1
    label: Voyant usure frein allume au tableau de bord
    severity: securite
  - id: S2
    label: Sifflement metallique freinage temoin acoustique
    severity: securite
  - id: S3
    label: Voyant allume en permanence meme plaquettes neuves
    severity: confort
  - id: S4
    label: Connecteur du temoin debranche ou coupe
    severity: confort
  - id: S5
    label: Fil du temoin fondu par frottement sur disque
    severity: confort
  - id: S6
    label: Freinage degrade malgre absence de voyant
    severity: securite
  - id: S7
    label: Odeur de brule si frottement du fil
    severity: confort
  - id: S8
    label: Plus de 30 000 km avec temoin non verifie
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  quick_checks:
  - Voyant usure frein allume au tableau de bord ?
  - 'Observer : sifflement metallique freinage temoin acoustique ?'
  - Voyant allume en permanence meme plaquettes neuves ?
  - 'Observer : connecteur du temoin debranche ou coupe ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant usure frein allume au tableau de bord
  - Sifflement metallique freinage temoin acoustique
  - Voyant allume en permanence meme plaquettes neuves
  - Connecteur du temoin debranche ou coupe
  - Fil du temoin fondu par frottement sur disque
  - Freinage degrade malgre absence de voyant
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '407'
  intro_title: A quoi sert Témoin d'usure ?
  risk_title: Pourquoi remplacer Témoin d'usure a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Témoin d'usure électrique ou acoustique ?
    answer: 'Électrique : voyant au tableau de bord. Acoustique : languette métallique qui siffle. Les deux indiquent qu''il
      faut changer les plaquettes.'
  - question: Comment savoir si mon témoin d'usure est HS ?
    answer: Voyant frein allumé en permanence même avec plaquettes neuves, ou au contraire pas de voyant alors que les plaquettes
      sont usées.
  - question: Faut-il changer le témoin à chaque changement de plaquettes ?
    answer: Oui pour les témoins électriques (usage unique). Le témoin acoustique est intégré à la plaquette et change avec
      elle.
  - question: Peut-on rouler avec le voyant d'usure allumé ?
    answer: Sur quelques centaines de km maximum. Le voyant s'allume quand il reste environ 2-3mm de garniture. Ne pas tarder
      à changer.
  - question: Quelle erreur éviter avec les témoins d'usure ?
    answer: Ne pas oublier de brancher le connecteur après changement de plaquettes. Vérifier que le câble ne frotte pas sur
      le disque.
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
doc_id: cbe549bc-c709-519a-bf1d-c82b5481c776
content_hash: sha256:d3e9ad5da5be961f
lang: fr
variants:
- name: Piece standard
  aliases:
  - standard
  - OE equivalent
  functional_differences:
  - Qualite equivalente a la monte d origine
  - Compatible avec la majorite des vehicules
- name: Piece performance/sport
  aliases:
  - sport
  - haute performance
  functional_differences:
  - Materiaux haute temperature
  - Pour usage intensif ou sportif
location_on_vehicle:
  area: Au niveau des roues (avant et/ou arriere)
  access: Demontage de la roue necessaire (cric + chandelle)
  adjacent_parts:
  - disque
  - plaquette
  - etrier
  - flexible
installation:
  difficulty: moyen
  time: 30min a 1h par essieu
  tools:
  - cle a douille
  - cle Allen
  - pied a coulisse
  - cle dynamometrique
  prerequisite: Vehicule sur chandelles, roue demontee
phase5_enrichment:
  _source: ate-freinage.fr + bremboparts.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 9
  _has_tech_data: true
  technical_notes:
    val_3_mm: '3 mm'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le témoin d'usure est un capteur incorporédans la plaquette de frein du
    voiture. Son rôle est d'envoyer un signal sonore ou lumineuxsur le tableau
    de bord pour avertir le conducteur lorsqu'il détecte la limited'usure des
    plaquettes de frein. Lorsque les plaquettes de frein sont usées lecontact
    ferme un circuit électrique ce qui va allumer le témoin d'usure sur
    letableau de bord. Dés que le témoin d'usure s'allume nous vous conseillons
    decontrôlez l'état des plaquettes de frein et de les remplacées si
    nécessairepour éviter tous risques d'usure d'autres composants dans le
    système defreinage (disques de frein, étriers de frein). En savoir plus :
    témoin d'usure — définition et rôle mécanique 🚨 Bruit Témoin d'usure :
    causes et diagnostic
  S2: >-
    Ne pas attendre la panne complete pour intervenir. Symptômes d'usure : -
    Voyant usure frein allume au tableau de bord - Sifflement metallique
    freinage temoin acoustique - Voyant allume en permanence meme plaquettes
    neuves - Connecteur du temoin debranche ou coupe - Fil du temoin fondu par
    frottement sur disque - Freinage degrade malgre absence de voyant - Odeur de
    brule si frottement du fil - Plus de 30 000 km avec temoin non verifie -
    Comment fonctionne le témoin d'usure des plaquettes - Fonctionnement d'une
    auto - Contrôle technique - Savoir trouver une panne - Voiture électrique -
    1) Témoin sonore (ancien procédé) - 2) Capteur d'usure électrique - ## 1)
    Témoin sonore (ancien procédé) Les témoins d'usure qui existaient avant les
    versions électroniques sont de petites strates intégrées dans les plaquettes
    de frein, situées tout en amont de la... - ## 2) Capteur d'usure électrique
    Un petit capteur électrique est intégré à la plaquette de frein . Il est
    composé de deux fils électriques conducteurs qui sont séparés par une couche
    isolante. Lorsque...
  S3: >-
    Pour choisir les bons temoin d usure pour votre véhicule : - Marque de votre
    véhicule - Modele de votre véhicule - Annee de votre véhicule - Vérifier :
    voyant usure frein allume au tableau de bord - Vérifier : sifflement
    metallique freinage temoin acoustique - Vérifier : voyant allume en
    permanence meme plaquettes neuves - Vérifier : connecteur du temoin
    debranche ou coupe - Vérifier : fil du temoin fondu par frottement sur
    disque - Vérifier : freinage degrade malgre absence de voyant - Vérifier :
    odeur de brule si frottement du fil - Vérifier : plus de 30 000 km avec
    temoin non verifie - Vérifier : Voyant usure frein allume au tableau de bord
    - Vérifier : Sifflement metallique freinage temoin acoustique - Vérifier :
    Freinage degrade malgre absence de voyantPour aller plus loin : consultez
    notre guide d'achat témoin d'usure — comparatif marques, critères de choix
    et prix.
  S4_DEPOSE: >-
    1. Lever le vehicule et deposer la roue. 2. Localiser le connecteur du
    temoin d'usure sur l'etrier de frein ou derriere le moyeu. 3. Debrancher le
    connecteur electrique du temoin (clip ou languette). 4. Retirer le temoin de
    son logement dans la plaquette de frein — il est enfiche ou clipse dans la
    garniture. 5. Verifier que le nouveau temoin correspond (longueur du fil,
    type de connecteur, essieu avant ou arriere). 6. Enficher le temoin neuf
    dans le logement de la plaquette neuve AVANT de monter la plaquette sur
    l'etrier. 7. Rebrancher le connecteur et verifier que le voyant s'eteint au
    tableau de bord contact mis.
  S4_REPOSE: >-
    La repose du témoin d'usure est une opération rapide mais dont deux erreurs
    classiques génèrent des appels de garantie : oublier de brancher le
    connecteur après remontage des plaquettes, et laisser le câble frotter
    contre le disque de frein . Ces deux erreurs produisent un voyant d'usure
    allumé ou une odeur de brûlé alors que les plaquettes sont neuves. -
    Vérifiez que le témoin d'usure neuf est identique à celui démonté : type
    électrique (connecteur) ou acoustique (languette intégrée à la plaquette),
    nombre de broches, référence. - Changez systématiquement les plaquettes de
    frein lors du remplacement du témoin électrique — le témoin est à usage
    unique et ne doit pas être réutilisé avec les anciennes plaquettes même si
    elles semblent encore valables. - Contrôlez l'état du disque de frein
    associé : un disque en dessous de l'épaisseur minimale (gravée sur la
    tranche) doit être remplacé simultanément pour garantir l'efficacité du
    nouveau jeu de plaquettes. - Contrôlez le fonctionnement de l'étrier de
    frein : un piston coincé ou un coulisseau grippé empêche le recul correct de
    la plaquette et use le témoin neuf en quelques semaines. - Passez le câble
    du témoin d'usure dans son cheminement d'origine en maintenant une distance
    d'au moins 10 mm entre le câble et la surface du disque en rotation —
    vérifiez le cheminement avec l'étrier en position finale avant de remonter
    la roue. - Enfichez le connecteur électrique du témoin sur son support
    jusqu'au déclic de verrouillage. Tirez légèrement sur le câble pour
    confirmer la solidité du branchement. - Remontez les plaquettes de frein
    neuves avec leur ressort de rappel et les clips anti-bruit correctement
    positionnés — un ressort oublié génère des crissements après quelques
    frenages. - Refoulez le piston de l'étrier à l'aide d'un repousse-piston en
    ouvrant légèrement le purgeur pour éviter de refouler du vieux liquide vers
    le maître-cylindre. Vérifiez le niveau de liquide dans le réservoir. -
    Remontez la roue et effectuez 10 à 15 freinages progressifs depuis 50 km/h
    pour roder les plaquettes neuves et vérifier l'extinction du voyant d'usure
    au tableau de bord. - Vérifiez à nouveau le cheminement du câble du témoin
    après le premier roulage pour confirmer l'absence de frottement contre le
    disque ou la roue.
  S5: >-
    Erreurs frequentes avec le temoin d'usure de plaquettes : - Ne pas remplacer
    le temoin en meme temps que les plaquettes — le temoin a usage unique se
    declenche une seule fois, le reutiliser laisse le voyant allume ou ne
    detecte plus l'usure- Confondre temoin d'usure mecanique (languette
    metallique) et electrique (fil avec connecteur) — les deux systemes ne sont
    pas interchangeables- Oublier de rebrancher le connecteur du temoin apres
    remplacement des plaquettes — le voyant reste allume au tableau de bord sans
    raison- Couper le fil du temoin au lieu de le remplacer pour eteindre le
    voyant — masque l'usure reelle des plaquettes, dangereux- Confondre le
    voyant de temoin d'usure avec le voyant de niveau de liquide de frein — les
    deux allument le meme temoin sur certains vehicules
  S6: >-
    Après le remplacement d'un témoin d'usure de frein, plusieurs contrôles
    s'imposent avant de reprendre une utilisation normale du véhicule. Le témoin
    est un composant de sécurité : sa mise en service doit être validée
    rigoureusement. - Extinction du voyant tableau de bord : mettre le contact
    et vérifier que le voyant d'usure frein s'éteint normalement après
    l'autotest initial (3 à 5 secondes). S'il reste allumé en permanence, le
    connecteur du témoin est peut-être mal enfiché ou le fil de contact touche
    encore le disque. - Contrôle de la position du fil témoin : vérifier
    visuellement que le fil du témoin neuf est correctement logé dans son clip
    de maintien sur la plaquette et ne frotte pas sur la jante ou sur le disque
    de frein à froid — un frottement prématuré activerait le voyant à tort. -
    Vérification du connecteur électrique : tirer légèrement sur le connecteur
    pour s'assurer qu'il est verrouillé et non simplement posé. Un connecteur
    lâche provoque un voyant intermittent qui peut disparaître et réapparaître
    selon les vibrations. - Test de non-déclenchement à froid : effectuer 3 à 4
    freinages progressifs depuis 30 km/h jusqu'à l'arrêt complet — le voyant ne
    doit pas s'allumer pendant ces phases de freinage à froid. - Test après 5 à
    10 km de conduite normale : rouler en conditions normales et vérifier à
    l'arrêt que le voyant reste éteint. La chaleur générée par le freinage ne
    doit pas provoquer une fausse alerte par dilatation des composants. -
    Contrôle de l'épaisseur résiduelle des plaquettes : profiter du remplacement
    du témoin pour mesurer visuellement l'épaisseur des plaquettes de frein
    associées — si elles affichent moins de 3 mm de matière, le remplacement
    simultané est incontournable pour ne pas reposer un témoin sur des
    plaquettes en fin de vie. - Vérification de l'absence d'odeur de brûlé :
    après les premiers freinages, aucune odeur de plastique ou de caoutchouc
    chaud ne doit être perceptible au niveau des roues, signe que le fil du
    témoin ne frotte pas sur une surface chaude.
  S_GARAGE: >-
    Nous vous recommandons de confier cette intervention à un professionnel : -
    Plusieurs causes possibles de défaillance (3 identifiées) nécessitent un
    diagnostic professionnel Un garagiste qualifié dispose de l'outillage et de
    l'expérience nécessaires pour effectuer cette opération en toute sécurité.
  S7: >-
    Quel est le prix d'un témoin d'usure ?Le prix varie selon le véhicule et la
    marque. Utilisez notre sélecteur pour trouver le témoin d'usure compatible
    avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon témoin d'usure est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un témoin d'usure défaillant ?Cela dépend
    de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité
    du véhicule. Consultez la section symptômes pour évaluer l'urgence du
    remplacement.- cable de frein a main - capteur abs - disque de frein -
    etrier de frein - interrupteur des feux de freins - plaquette de frein -
    servo frein
  S8: >-
    Témoin d'usure électrique ou acoustique ?Électrique : voyant au tableau de
    bord. Acoustique : languette métallique qui siffle. Les deux indiquent qu'il
    faut changer les plaquettes. Comment savoir si mon témoin d'usure est HS
    ?Voyant frein allumé en permanence même avec plaquettes neuves, ou au
    contraire pas de voyant alors que les plaquettes sont usées. Faut-il changer
    le témoin à chaque changement de plaquettes ?Oui pour les témoins
    électriques (usage unique). Le témoin acoustique est intégré à la plaquette
    et change avec elle. Peut-on rouler avec le voyant d'usure allumé ?Sur
    quelques centaines de km maximum. Le voyant s'allume quand il reste environ
    2-3mm de garniture. Ne pas tarder à changer. Quelle erreur éviter avec les
    témoins d'usure ?Ne pas oublier de brancher le connecteur après changement
    de plaquettes. Vérifier que le câble ne frotte pas sur le disque.
  META: >-
    {"meta_title":"Témoin d'usure frein : voyant allumé, que faire ? |
    AutoMecanik","meta_description":"Voyant usure frein allumé ou sifflement
    métallique au freinage ? Le témoin d'usure doit être contrôlé sans tarder.
    Guide pour diagnostiquer et remplacer la pièce adaptée.","og_title":"Témoin
    d'usure freins : diagnostic et remplacement","og_description":"Voyant usure
    frein allumé ou sifflement métallique au freinage ? Le témoin d'usure doit
    être contrôlé sans tarder. Guide pour diagnostiquer et remplacer la pièce ad
    aptée.","schema_type":"Article","primary_intent":"diagnostic","gate_report":
    "PASS","char_count_title":55,"char_count_desc":186}
---

# Témoin d'usure - Guide Diagnostic Complet

## Fonction et Rôle

Signale l'usure des plaquettes de frein

**Actions principales:** signaler, alerter, indiquer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant usure frein allume au tableau de bord**
  voyant usure frein allume au tableau de bord
- **Sifflement metallique freinage temoin acoustique**
  sifflement metallique freinage temoin acoustique
- **Freinage degrade malgre absence de voyant**
  freinage degrade malgre absence de voyant

### 🟢 Autres Symptômes

- voyant allume en permanence meme plaquettes neuves
- connecteur du temoin debranche ou coupe
- fil du temoin fondu par frottement sur disque
- odeur de brule si frottement du fil
- plus de 30 000 km avec temoin non verifie

## Procédure de Diagnostic

Pour diagnostiquer un problème de témoin d'usure:

1. **Inspection visuelle** - Examiner l'état du témoin d'usure
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins
- plaquette-de-frein
- servo-frein

## Critères de Compatibilité

Pour commander le bon témoin d'usure, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "améliore le freinage"

## FAQ

**Témoin d'usure électrique ou acoustique ?**
Électrique : voyant au tableau de bord. Acoustique : languette métallique qui siffle. Les deux indiquent qu'il faut changer les plaquettes.

**Comment savoir si mon témoin d'usure est HS ?**
Voyant frein allumé en permanence même avec plaquettes neuves, ou au contraire pas de voyant alors que les plaquettes sont usées.

**Faut-il changer le témoin à chaque changement de plaquettes ?**
Oui pour les témoins électriques (usage unique). Le témoin acoustique est intégré à la plaquette et change avec elle.

**Peut-on rouler avec le voyant d'usure allumé ?**
Sur quelques centaines de km maximum. Le voyant s'allume quand il reste environ 2-3mm de garniture. Ne pas tarder à changer.

**Quelle erreur éviter avec les témoins d'usure ?**
Ne pas oublier de brancher le connecteur après changement de plaquettes. Vérifier que le câble ne frotte pas sur le disque.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/freinage/vibration-au-freinage.md 2026-01-01 -->
### Diagnostic - Vibrations véhicule

# Vibrations véhicule - Diagnostic complet

## Types de vibrations

### Vibrations au volant
- **À basse vitesse (< 50 km/h)** : Problème de pneus ou jantes
- **À haute vitesse (> 80 km/h)** : Équilibrage ou géométrie
- **Au freinage** : Disques voilés

### Vibrations dans l'habitacle
- **Moteur au ralenti** : Supports moteur
- **En accélération** : Transmission, cardans
- **À vitesse constante** : Pneus, roulements

### Vibrations dans la pédale de frein
- **Au freinage** : Disques voilés, plaquettes usées

## Causes et solutions

### 1. Pneus déséquilibrés
- **Symptôme** : Vibration volant à partir de 80-100 km/h
- **Vérification** : Visuel sur les masses d'équilibrage
- **Solution** : Équilibrage des 4 pneus
- **Coût** : 40-60€
- **Urgence** : Moyenne

### 2. Pneus usés irrégulièrement
- **Symptôme** : Vibration + bruit de roulement
- **Vérification** : Usure en "dents de scie"
- **Solution** : Remplacement pneus + géométrie
- **Urgence** : Haute

### 3. Roulement de roue défaillant
- **Symptôme** : Grondement augmentant avec la vitesse
- **Vérification** : Jeu dans la roue, bruit en virage
- **Solution** : Remplacement roulement
- **Pièces** : Kit roulement de roue
- **Urgence** : Haute - Sécurité

### 4. Cardans usés
- **Symptôme** : Claquement en braquant, vibration en accélération
- **Vérification** : Soufflets déchirés, jeu
- **Solution** : Remplacement cardan
- **Pièces** : Cardan complet ou transmission
- **Urgence** : Haute

### 5. Disques de frein voilés
- **Symptôme** : Vibration pédale au freinage
- **Vérification** : Mesure au comparateur
- **Solution** : Rectification ou remplacement
- **Pièces** : Disques de frein
- **Urgence** : Moyenne

### 6. Supports moteur fatigués
- **Symptôme** : Vibration au ralenti dans l'habitacle
- **Vérification** : Visuel sur silent-blocs
- **Solution** : Remplacement supports
- **Pièces** : Support moteur, silent-bloc
- **Urgence** : Basse

## Arbre de décision

```
Vibration ?
├── Au volant ?
│   ├── À haute vitesse → Équilibrage / Géométrie
│   ├── Au freinage → Disques voilés
│   └── En virage → Roulement / Cardan
├── Dans l'habitacle ?
│   ├── Au ralenti → Supports moteur
│   ├── En accélération → Cardan / Transmission
│   └── Constant → Pneus / Roulements
└── Pédale de frein ?
    └── Au freinage → Disques voilés
```

<!-- materialized-from-db diagnostic/bruits-freinage.md 2026-01-01 -->
### Diagnostic - Bruits de freinage

# Bruits de freinage - Diagnostic complet

## Symptômes courants

### Grincement aigu au freinage
- **Quand** : Au moment du freinage léger ou modéré
- **Caractéristique** : Son métallique aigu, type "crissement"

### Sifflement continu
- **Quand** : Pendant tout le freinage
- **Caractéristique** : Son aigu constant

### Bruit sourd / grondement
- **Quand** : Freinage appuyé
- **Caractéristique** : Vibration ressentie dans la pédale

### Claquement
- **Quand** : Début ou fin de freinage
- **Caractéristique** : Bruit sec, ponctuel

## Causes possibles et solutions

### 1. Plaquettes de frein usées
- **Probabilité** : 70%
- **Vérification** : Témoin usure allumé, épaisseur < 3mm
- **Solution** : Remplacement des plaquettes
- **Pièces** : Plaquettes de frein avant/arrière
- **Urgence** : Haute - Sécurité

### 2. Disques de frein voilés
- **Probabilité** : 15%
- **Vérification** : Vibration pédale, usure inégale visible
- **Solution** : Rectification ou remplacement des disques
- **Pièces** : Disques de frein
- **Urgence** : Moyenne

### 3. Étrier grippé
- **Probabilité** : 10%
- **Vérification** : Usure asymétrique des plaquettes
- **Solution** : Nettoyage/graissage ou remplacement étrier
- **Pièces** : Kit réparation étrier, étrier complet
- **Urgence** : Haute

### 4. Absence de graisse sur glissières
- **Probabilité** : 5%
- **Vérification** : Plaquettes difficiles à bouger
- **Solution** : Nettoyage et graissage
- **Pièces** : Graisse haute température
- **Urgence** : Basse

## Questions complémentaires pour affiner le diagnostic

1. Le bruit apparaît-il à froid ou à chaud ?
2. Le bruit est-il présent sur les 4 roues ou localisé ?
3. Y a-t-il une vibration dans le volant ?
4. Quand avez-vous changé vos plaquettes pour la dernière fois ?
5. Avez-vous un témoin d'usure allumé au tableau de bord ?

## Recommandations

- **Contrôle visuel** : Vérifier l'épaisseur des plaquettes (minimum 3mm)
- **Kilométrage** : Remplacement préventif tous les 30 000 - 50 000 km
- **Qualité** : Privilégier les marques équipementier (Bosch, Brembo, TRW)
