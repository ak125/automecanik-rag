---
category: eclairage
slug: feu-clignotant
title: Feu clignotant
pg_id: 62
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
  role: Signale les changements de direction
  must_be_true:
  - signaler
  - indiquer
  - clignoter
  must_not_contain:
  - injection
  - freinage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - ampoule-feu-avant
  - ampoule-feu-arriere
  - feu-avant
  - feu-arriere
  - phares-antibrouillard
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
  - ❌ "meilleure visibilité"
  cost_range:
    min: 10
    max: 50
    currency: EUR
    unit: répétiteur
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Répétiteur identique à l'origine. Recommandé pour les véhicules récents avec répétiteurs intégrés dans les
      rétroviseurs.
  - tier: Équivalent OE (OES)
    description: Valeo et Hella proposent des répétiteurs OES sur les principaux modèles. Qualité équivalente à l'OE.
  - tier: Adaptable (aftermarket)
    description: Le marché aftermarket est bien développé pour les répétiteurs. Disponibles en version transparente, fumée
      ou LED. L'homologation E est obligatoire.
  brands:
    premium:
    - Osram
    - Philips
    standard:
    - Bosch
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Clignotant lateral qui ne s allume plus
    severity: confort
  - id: S2
    label: Clignotement rapide tableau bord ampoule
    severity: confort
  - id: S3
    label: Repetiteur casse ou fissure choc
    severity: confort
  - id: S4
    label: Eau ou buee visible dans le repetiteur
    severity: confort
  - id: S5
    label: Controle technique refuse signalisation defaillante
    severity: confort
  - id: S6
    label: Ampoule qui grille frequemment infiltration
    severity: confort
  - id: S7
    label: Clignotement plus rapide normale hyper
    severity: confort
  - id: S8
    label: Clignotant fonctionne intermittence maniere aleatoire
    severity: confort
  - id: S9
    label: Odeur plastique fondu court circuit
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : clignotant lateral qui ne s allume plus'
  quick_checks:
  - 'Observer : clignotant lateral qui ne s allume plus ?'
  - 'Observer : clignotement rapide tableau bord ampoule ?'
  - 'Observer : repetiteur casse ou fissure choc ?'
  - 'Observer : eau ou buee visible dans le repetiteur ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Clignotant lateral qui ne s allume plus
  - Clignotement rapide tableau bord ampoule
  - Repetiteur casse ou fissure choc
  - Eau ou buee visible dans le repetiteur
  - Controle technique refuse signalisation defaillante
  - Ampoule qui grille frequemment infiltration
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '62'
  intro_title: A quoi sert Feu clignotant ?
  risk_title: Pourquoi remplacer Feu clignotant a temps ?
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
  - question: Répétiteur clignotant OE ou adaptable ?
    answer: Les répétiteurs adaptables conviennent généralement. Vérifiez l'homologation E obligatoire. Les versions LED transparentes
      ou fumées sont populaires pour personnaliser.
  - question: Comment savoir si mon répétiteur est HS ?
    answer: Clignotant latéral qui ne s'allume plus, clignotement rapide (ampoule grillée), plastique cassé ou fissuré, eau
      à l'intérieur.
  - question: Tous les combien changer le répétiteur ?
    answer: Pas de périodicité. Remplacement si cassé ou si l'ampoule grille souvent (infiltration d'eau). Pièce qui peut
      durer toute la vie du véhicule.
  - question: Peut-on changer un répétiteur soi-même ?
    answer: Oui, très simple. Pousser le répétiteur vers l'avant ou l'arrière pour le déclipser, débrancher l'ampoule ou le
      connecteur, clipser le neuf. 5-10 min.
  - question: Quelle erreur éviter avec le répétiteur ?
    answer: Ne pas forcer pour déclipser (casser les pattes). Vérifier que le joint est en place. Tester le clignotement avant
      de tout remonter.
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
doc_id: 5b464c69-277d-5c5f-9872-23d7e41bc0dd
content_hash: sha256:9992177eb3eee225
lang: fr
variants:
- name: Ampoule halogene
  aliases:
  - halogene
  - H1
  - H4
  - H7
  functional_differences:
  - Standard, economique
  - Remplacement simple
- name: Ampoule LED
  aliases:
  - LED
  functional_differences:
  - Duree de vie superieure
  - Consommation reduite
  - Verifier homologation
location_on_vehicle:
  area: Face avant, arriere et laterale du vehicule
  access: Par le compartiment moteur (avant) ou coffre (arriere)
  adjacent_parts:
  - optique
  - ampoule
  - connecteur
  - reflecteur
installation:
  difficulty: facile
  time: 5 a 15 min
  tools:
  - tournevis
  - gants (ne pas toucher ampoule halogene)
  prerequisite: Moteur eteint, acces par compartiment moteur ou coffre
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'Plein'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_1_0_hz: '1,0 Hz'
    val_2_hz: '2 Hz'
    val_2_a: '2 a'
    val_28_a: '28 a'
    val_5_hz: '5 Hz'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Les feux de clignotant sontsitués à l''avant et à l''arrière du véhicule (au niveau des feux avant et desfeux arrière).
    Dans les feux de clignotant avant peuvent être solidaire ouséparé des feux avant mai les clignotants arrière font toujours
    part des feuxarrière. Sur une voiture on peut avoir d''autres feux clignotant supplémentairessuivant le niveau d''équipement
    de la voiture par exemple dans lesrétroviseurs extérieur, dans le pare-choc avant, dans les ailes avant de lavoiture?.
    Les feux de clignotant sontreprésentés sur le tableau de bord par deux flèches vertes pointant une àdroite et l''autre
    à gauche, ils vont permettre au conducteur d''avertir lesautres usagers de la route qu''il va se déporter ou tourner vers
    la droite ouvers la gauche, ou de vous garez et il servent aussi de feu de détresse. Le feude clignotant est un outil
    de signalisation extrêmement important dans le véhicule. La couleur réglementaire des feux de clignotant estl''orange.Les
    feux de clignotantsont actionnés par une manette située dans la commande d''éclairage monté dans la colonne de direction
    sous le volant de direction. En savoir plus : feu clignotant — définition et rôle mécanique 🚨 Bruit Feu clignotant : causes
    et diagnostic'
  S2: 'Un feu de clignotant défectueuxprésente plusieurs symptômes : - Avertissement sonore et visuel sur le témoin du tableau
    de bord. - Lors d''un contrôle visuel vous remarquez que le feu de clignotant estfissuré. - Problème dans le circuit du
    feu de clignotant par exemple un court-circuit. Un feu de clignotantHS et qu''il n''est pas remplacé à temps peut causer
    des risques d''accidents lorsde l''utilisation de la route et le refus de votre véhicule lors du contrôletechnique. Diagnostic
    complet : identifier une panne de feu clignotant'
  S3: 'Le feu clignotant (répétiteur de clignotant) est une pièce de signalisation réglementée : sa couleur (orange ambre),
    son angle de visibilité minimum de 80° et sa fréquence de clignotement (entre 60 et 120 éclairs par minute) sont imposés
    par le Code de la route. Un répétiteur non conforme entraîne un refus au contrôle technique et une responsabilité engagée
    en cas d''accident. Vérifiez les critères suivants avant de sélectionner la pièce. - Position et référence constructeur
    (avant gauche, avant droit, latéral, arrière) — Les clignotants se déclinent en plusieurs emplacements : répétiteur latéral
    dans l''aile, clignotant intégré au phare avant, clignotant dans le feu arrière. Chaque emplacement a une référence spécifique.
    Notez la référence OEM inscrite sur la pièce d''origine ou consultez l''éclaté constructeur pour éviter toute erreur de
    côté ou d''emplacement. - Marque, modèle, version et année de fabrication — Un même modèle peut avoir plusieurs emplacements
    de répétiteur selon l''année et la version d''équipement. L''année de fabrication exacte (mois/année) est indispensable
    car les facelifts modifient fréquemment la forme des clignotants sans que le nom commercial du modèle ne change. - Type
    d''ampoule compatible ou technologie LED — Les répétiteurs classiques utilisent des ampoules PY21W (21W, culot BAU15s)
    ou W21W. Les versions LED nécessitent une résistance de charge (load resistor) si le clignoteur d''origine est analogique,
    sous peine de clignotement hypercadencé (hyperflash) indiquant une défaillance au tableau de bord. Vérifiez la compatibilité
    électronique avec le clignoteur de votre véhicule. - Transparence de la lentille : orange ou translucide — Certains véhicules
    utilisent des répétiteurs à lentille translucide (blanche) associés à une ampoule orange PY21W. D''autres ont une lentille
    orange avec une ampoule blanche. Ces combinaisons ne sont pas interchangeables : une lentille blanche avec une ampoule
    blanche produit un clignotant blanc, illégal sur voie publique. - Résistance à la pénétration d''eau — La buée visible
    dans le répétiteur ou une ampoule qui grille fréquemment signalent une infiltration. Choisissez une pièce avec joint d''étanchéité
    intégré et indice IP65 minimum. Les répétiteurs latéraux montés dans l''aile sont particulièrement exposés aux projections.
    - Matériau du boîtier et résistance aux UV — Un répétiteur fissuré ou jauni perd son homologation. Les boîtiers en polycarbonate
    traité anti-UV conservent leur transparence et leur intégrité mécanique sur 8 à 10 ans. Évitez les pièces présentant un
    polycarbonate non traité qui jaunit dès la première saison. - Certification E-Mark obligatoire — Seules les pièces portant
    le marquage E sont homologuées pour la circulation en Europe. Tout répétiteur vendu comme "universel", "adaptable" ou
    "compatible tous modèles" ne garantit pas les cotes de montage ni l''homologation réglementaire. Pour aller plus loin
    : consultez notre guide d''achat feu clignotant — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Feu clignotant pour connaître les spécifications. - Débranchez
    la batterie. - Localisez l'emplacement du feu de clignotant que vous voulez démonter. - Démontez la glace du rétroviseur
    extérieur si nécessaire. - Démontez le cache du rétroviseur. - Dégrafez le feu de clignotant du rétroviseur extérieur.
    - Débranchez le connecteur du feu de clignotant. - Démontez le feu de clignotant.
  S4_REPOSE: 'Le remontage du feu clignotant (répétiteur latéral ou bloc optique intégré au rétroviseur) demande d''agir dans
    le bon ordre pour ne pas casser les pattes de clippage et garantir l''étanchéité contre les infiltrations d''eau. La vérification
    électrique avant fermeture du rétroviseur est indispensable. - Contrôlez que le feu clignotant neuf est de référence identique
    à celui déposé : vérifiez la couleur de la lentille (transparente, orange ou fumée), le type de douille et la polarité
    du connecteur. - Si les ampoules de feu clignotant sont séparables du bloc, insérez la nouvelle ampoule à baïonnette en
    l''alignant sur les plots de guidage, puis tournez d''un quart de tour dans le sens horaire jusqu''au blocage. - Vérifiez
    que le joint d''étanchéité périphérique du répétiteur est propre et bien positionné dans sa gorge. Un joint absent ou
    déplacé provoque une infiltration d''eau et des grillages fréquents d''ampoule. - Branchez le connecteur électrique du
    feu clignotant avant d''engager le boîtier dans son logement. Assurez-vous d''entendre le déclic de verrouillage du connecteur.
    - Positionnez le feu clignotant sur le rétroviseur extérieur en engageant d''abord le bord avant dans son guide, puis
    appuyez fermement sur le bord arrière jusqu''au clic des pattes de clippage. Ne forcez pas avec un tournevis. - Remontez
    le cache du rétroviseur en clipçant les agrafes dans l''ordre inverse du démontage (généralement de l''arrière vers l''avant).
    - Remontez la glace du rétroviseur si elle avait été déposée, en l''engageant par le bas puis en appuyant sur le dessus
    jusqu''au verrouillage. - Rebranchez la batterie : borne positive (+) en premier, borne négative (-) ensuite. - Activez
    les clignotants droit et gauche séparément pour vérifier le rythme de clignotement au tableau de bord. Un clignotement
    deux fois plus rapide qu''à l''ordinaire (hyper-flash) indique une ampoule de mauvaise puissance ou un connecteur mal
    serti. - Contrôlez visuellement l''absence de jeu ou de vibration du répétiteur en actionnant les retroviseurs électriques
    de bas en haut et en appuyant légèrement sur la coque du rétroviseur. ✅ Après remontage, vérifiez les spécifications dans
    la fiche technique Feu clignotant.'
  S5: 'Erreurs frequentes avec les feux clignotants : - Ne pas verifier le cote (gauche/droite) et la position (avant/lateral/retroviseur)
    avant achat — les references different selon l''emplacement- Confondre un clignotement rapide avec un defaut du feu —
    un clignotement accelere signale generalement une ampoule grillee, pas un feu defectueux- Forcer le demontage du connecteur
    electrique — les clips plastique sont fragiles, tirer droit sans forcer lateralement- Ne pas verifier l''etancheite du
    joint apres montage — l''humidite provoque de la buee et corrode les contacts- Ignorer un feu clignotant casse ou opaque
    — c''est un motif de contre-visite au controle technique- Remplacer par une ampoule LED sans adaptateur — la resistance
    differente perturbe la centrale clignotante et provoque un clignotement rapide'
  S6: 'Après le remplacement d''un feu clignotant ou répétiteur latéral, les vérifications portent sur la fréquence de clignotement,
    l''étanchéité du boîtier et l''absence de dysfonctionnement électrique déclenché par la nouvelle pièce.- Fréquence de
    clignotement normale — 60 à 120 cycles par minute — Actionnez le levier clignotant et comptez les flashs pendant 10 secondes.
    La fréquence normale se situe entre 60 et 120 cycles/min. Un clignotement trop rapide (hyperflashing) révèle une ampoule
    de résistance incorrecte ou un connecteur mal serti qui augmente la résistance de ligne.- Aucun signal d''ampoule grillée
    au tableau de bord — Sur les véhicules avec surveillance des feux, aucune alerte ne doit s''allumer. Si le tableau de
    bord signale une ampoule grillée malgré un clignotant qui fonctionne, vérifiez la continuité du fil de retour de masse
    (résistance doit être inférieure à 0,3 ohm).- Synchronisation avec le clignotant opposé — En cas de clignotants de détresse
    (warning), les quatre clignotants doivent flasher à la même fréquence et en phase. Un décalage visible indique un problème
    de relais clignotant ou une asymétrie de résistance entre les deux circuits.- Étanchéité du répétiteur latéral — Examinez
    le joint périphérique du boîtier : il doit être correctement positionné dans sa gorge sans pli ni compression excessive.
    Après une pluie, vérifiez l''absence d''eau à l''intérieur du répétiteur en observant le fond de la lentille.- Solidité
    de la fixation dans son logement — Le répétiteur ne doit pas bouger latéralement ni vibrer. Un jeu de plus de 1 mm dans
    le logement provoque des claquements en roulage et peut fracturer le clip de retenue par fatigue en quelques semaines.-
    Absence d''odeur de plastique fondu — Après 10 minutes de fonctionnement avec les warnings activés, aucune odeur de plastique
    brûlé ne doit être perceptible. Une odeur signale un court-circuit dans le connecteur ou une ampoule de puissance trop
    élevée pour le boîtier.- Contrôle de compatibilité LED si applicable — Si la nouvelle pièce est à technologie LED, vérifiez
    que le véhicule dispose bien d''une résistance de charge ou d''un relais clignotant adapté LED. Sans adaptation, le clignotement
    sera deux à trois fois trop rapide.'
  S7: Quel est le prix d'un feu clignotant ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour trouver
    le feu clignotant compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment savoir si
    mon feu clignotant est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic ci-dessus.
    En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un feu clignotant défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section symptômes
    pour évaluer l'urgence du remplacement.- signaler - indiquer - clignoter
  S8: Comment choisir Feu clignotant compatible avec mon vehicule ?Renseignez marque, modele, type moteur et annee, puis verifiez
    la reference Quand remplacer Feu clignotant ?En cas de clignotant lateral qui ne s allume plus ou de degradation mesurable,
    Puis-je monter Feu clignotant sans verification atelier ?Le montage peut exiger controles de couple, alignement et references.
  META: '{"meta_title":"Feu clignotant : quand le changer ? | AutoMecanik","meta_description":"Répétiteur cassé, clignotement
    rapide ou refus contrôle technique ? Feu clignotant défaillant. Guide symptômes, diagnostic et compatibilité par véhicule."}'
---

# Feu clignotant - Guide Diagnostic Complet

## Fonction et Rôle

Signale les changements de direction

**Actions principales:** signaler, indiquer, clignoter

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Repetiteur casse ou fissure choc**
  repetiteur casse ou fissure choc

### 🟢 Autres Symptômes

- clignotant lateral qui ne s allume plus
- clignotement rapide tableau bord ampoule
- eau ou buee visible dans le repetiteur
- controle technique refuse signalisation defaillante
- ampoule qui grille frequemment infiltration
- clignotement plus rapide normale hyper

## Procédure de Diagnostic

Pour diagnostiquer un problème de feu clignotant:

1. **Inspection visuelle** - Examiner l'état du feu clignotant
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

- ampoule-feu-clignotant
- commande-d-eclairage
- feu-arriere
- feu-avant

## Critères de Compatibilité

Pour commander le bon feu clignotant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure visibilité"

## FAQ

**Répétiteur clignotant OE ou adaptable ?**
Les répétiteurs adaptables conviennent généralement. Vérifiez l'homologation E obligatoire. Les versions LED transparentes ou fumées sont populaires pour personnaliser.

**Comment savoir si mon répétiteur est HS ?**
Clignotant latéral qui ne s'allume plus, clignotement rapide (ampoule grillée), plastique cassé ou fissuré, eau à l'intérieur.

**Tous les combien changer le répétiteur ?**
Pas de périodicité. Remplacement si cassé ou si l'ampoule grille souvent (infiltration d'eau). Pièce qui peut durer toute la vie du véhicule.

**Peut-on changer un répétiteur soi-même ?**
Oui, très simple. Pousser le répétiteur vers l'avant ou l'arrière pour le déclipser, débrancher l'ampoule ou le connecteur, clipser le neuf. 5-10 min.

**Quelle erreur éviter avec le répétiteur ?**
Ne pas forcer pour déclipser (casser les pattes). Vérifier que le joint est en place. Tester le clignotement avant de tout remonter.
## Phares et feux

### Phares faibles
- **Ampoules vieillissantes** : Les ampoules halogènes perdent 20-30% de luminosité après 2-3 ans. Remplacement par paire recommandé.
- **Optiques ternies** : Le polycarbonate des phares jaunit et devient opaque avec le temps. Kit de rénovation ou polissage.
- **Réglage incorrect** : Phares trop bas après un chargement ou un remplacement. Réglage avec les vis dédiées.

### Ampoules grillées fréquemment
- **Surtension** : Régulateur d'alternateur défaillant (tension > 14.8V). Mesurer la tension de charge.
- **Vibrations excessives** : Ampoule mal fixée dans son support, vibrations transmises au filament.
- **Mauvaise qualité** : Préférer des ampoules de marque (Philips, Osram, Bosch).

### Feux qui ne fonctionnent pas
- **Fusible grillé** : Vérifier le fusible correspondant dans la boîte à fusibles.
- **Connecteur oxydé** : Humidité dans le porte-ampoule, nettoyage et graisse contact.
- **Problème de masse** : Fil de masse corrodé au niveau du feu. Fréquent sur les feux arrière.

## Contrôle technique - Points éclairage

- Tous les feux doivent fonctionner : croisement, route, position, stop, recul, clignotants, antibrouillard arrière
- Hauteur de faisceau correcte (réglage)
- Pas de fissure laissant entrer l'eau dans les optiques
- Couleur conforme : blanc devant, rouge derrière, orange pour les clignotants

## LED vs Halogène vs Xénon

- **Halogène (H7, H4, H1)** : Standard, remplacement facile, coût faible
- **Xénon (D1S, D2S, D3S)** : Puissant, durée de vie longue, remplacement coûteux, nécessite un ballast
- **LED** : Très longue durée de vie, faible consommation, remplacement du bloc optique entier en cas de panne

## Quand consulter un professionnel

- Phare xénon qui clignote ou change de couleur (ballast ou ampoule)
- Feux LED intégrés défaillants (remplacement du bloc complet)
- Court-circuit récurrent (fusible qui saute à chaque remplacement)
- Défaut de réglage persistant malgré les ajustements


## References supplementaires

<!-- materialized-from-db manual/35e91d83bc4e 2026-04-03 -->
### Données techniques OEM — Feu clignotant

# Données techniques OEM — Feu clignotant
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- Plein
- électrique

## Symptomes supplementaires

<!-- materialized-from-db diagnostic/eclairage-voyants.md 2026-02-15 -->
### Diagnostic - Éclairage et signalisation

# Éclairage et signalisation - Diagnostic complet

## Phares et feux

### Phares faibles
- **Ampoules vieillissantes** : Les ampoules halogènes perdent 20-30% de luminosité après 2-3 ans. Remplacement par paire recommandé.
- **Optiques ternies** : Le polycarbonate des phares jaunit et devient opaque avec le temps. Kit de rénovation ou polissage.
- **Réglage incorrect** : Phares trop bas après un chargement ou un remplacement. Réglage avec les vis dédiées.

### Ampoules grillées fréquemment
- **Surtension** : Régulateur d'alternateur défaillant (tension > 14.8V). Mesurer la tension de charge.
- **Vibrations excessives** : Ampoule mal fixée dans son support, vibrations transmises au filament.
- **Mauvaise qualité** : Préférer des ampoules de marque (Philips, Osram, Bosch).

### Feux qui ne fonctionnent pas
- **Fusible grillé** : Vérifier le fusible correspondant dans la boîte à fusibles.
- **Connecteur oxydé** : Humidité dans le porte-ampoule, nettoyage et graisse contact.
- **Problème de masse** : Fil de masse corrodé au niveau du feu. Fréquent sur les feux arrière.

## Contrôle technique - Points éclairage

- Tous les feux doivent fonctionner : croisement, route, position, stop, recul, clignotants, antibrouillard arrière
- Hauteur de faisceau correcte (réglage)
- Pas de fissure laissant entrer l'eau dans les optiques
- Couleur conforme : blanc devant, rouge derrière, orange pour les clignotants

## LED vs Halogène vs Xénon

- **Halogène (H7, H4, H1)** : Standard, remplacement facile, coût faible
- **Xénon (D1S, D2S, D3S)** : Puissant, durée de vie longue, remplacement coûteux, nécessite un ballast
- **LED** : Très longue durée de vie, faible consommation, remplacement du bloc optique entier en cas de panne

## Quand consulter un professionnel

- Phare xénon qui clignote ou change de couleur (ballast ou ampoule)
- Feux LED intégrés défaillants (remplacement du bloc complet)
- Court-circuit récurrent (fusible qui saute à chaque remplacement)
- Défaut de réglage persistant malgré les ajustements
