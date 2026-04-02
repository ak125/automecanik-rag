---
category: freinage
slug: flexible-de-frein
title: Flexible de frein
pg_id: 83
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
  role: Transmettre la pression hydraulique entre les elements mobiles
  must_be_true:
  - transmettre la pression
  - acheminer le liquide
  - resister a la pression
  must_not_contain:
  - friction
  - thermique
  - electronique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - disque-de-frein
  - plaquette-de-frein
  - etrier-de-frein
  - maitre-cylindre-de-frein
  - liquide-de-frein
  - tambour-de-frein
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
  - ❌ "freinage ameliore"
  cost_range:
    min: 12
    max: 20
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Flexible identique à l'origine. Pression de rupture et résistance chimique certifiées. Recommandé pour les
      véhicules récents et les usages sportifs.
  - tier: Équivalent OE (OES)
    description: Équipementiers spécialisés freinage produisent des flexibles avec des matériaux conformes aux normes en vigueur
      et testés aux fluides DOT 3, 4, 4LV et 5.1.
  - tier: Renforcé (aviation / tressé inox)
    description: Flexibles à armature inox tressée. Sensation de pédale améliorée et durabilité accrue. Plutôt destinés aux
      usages sportifs ou piste.
  brands:
    premium:
    - Brembo
    - ATE
    - TRW
    standard:
    - Bosch
    - Ferodo
    - Textar
    budget:
    - Ridex
    - Valeo
diagnostic:
  symptoms:
  - id: S1
    label: Craquelures ou fissures visibles sur le flexible
    severity: confort
  - id: S2
    label: Gonflement flexible lors appui pedale
    severity: confort
  - id: S3
    label: Fuite de liquide de frein au niveau du flexible
    severity: securite
  - id: S4
    label: Pedale de frein spongieuse ou molle
    severity: securite
  - id: S5
    label: Freinage qui tire d un cote flexible bouche
    severity: securite
  - id: S6
    label: Sifflement bruit niveau flexible sous
    severity: confort
  - id: S7
    label: Odeur de liquide de frein fuite
    severity: securite
  - id: S8
    label: Plus depuis dernier changement flexibles
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  depose_steps: []
  quick_checks:
  - 'Observer : craquelures ou fissures visibles sur le flexible ?'
  - 'Observer : gonflement flexible lors appui pedale ?'
  - Fuite de liquide de frein au niveau du flexible ?
  - 'Observer : pedale de frein spongieuse ou molle ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Craquelures ou fissures visibles sur le flexible
  - Gonflement flexible lors appui pedale
  - Fuite de liquide de frein au niveau du flexible
  - Pedale de frein spongieuse ou molle
  - Freinage qui tire d un cote flexible bouche
  - Sifflement bruit niveau flexible sous
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '83'
  intro_title: A quoi sert Flexible de frein ?
  risk_title: Pourquoi remplacer Flexible de frein a temps ?
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
  - question: 'Flexible OE ou renforcé : que choisir ?'
    answer: Les flexibles OE suffisent pour un usage normal. Les flexibles renforcés (aviation/tressés) offrent une meilleure
      sensation de pédale pour une conduite sportive.
  - question: Comment savoir si mon flexible de frein est HS ?
    answer: Craquelures visibles sur le caoutchouc, gonflement du flexible au freinage, fuite de liquide, pédale de frein
      spongieuse.
  - question: Tous les combien changer les flexibles de frein ?
    answer: Tous les 10 ans ou 150 000 km recommandé. Le caoutchouc vieillit même sans rouler. Contrôle visuel à chaque révision.
  - question: Peut-on changer un flexible de frein soi-même ?
    answer: Oui, mais nécessite de purger le circuit après. Attention à ne pas vriller le flexible au montage. Utilisez une
      clé à tuyauter.
  - question: Quelle erreur éviter avec les flexibles ?
    answer: Ne jamais plier ou tordre un flexible. Ne pas utiliser de pince étau pour le pincer. Vérifier que le flexible
      ne frotte pas sur la roue en braquant.
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
doc_id: eeb3f3ee-169f-5520-8162-8563441d99dc
content_hash: sha256:c028593c9f5c23ee
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
-_fabriqués_selon_la_norme_interne_d’ate: 'FMVSS 106.

- Fabriqués selon la norme interne d’ATE'
    val_1_a: '1 a'
    val_100__: '100 %'
    val_100_a: '100 a'
    val_2264_a: '2264 a'
    val_7_a: '7 a'
    val_72_a: '72 a'
  materials:
  - materiau: 'EPDM'
    source_ref: corpus RAG web OEM
-_fabriqués_selon_la_norme_interne_d’ate: 'FMVSS 106.

- Fabriqués selon la norme interne d’ATE'
    val_1_a: '1 a'
    val_100__: '100 %'
    val_100_a: '100 a'
    val_7_a: '7 a'
    val_72_a: '72 a'
  materials:
  - materiau: 'EPDM'
    source_ref: corpus RAG web OEM
-_fabriqués_selon_la_norme_interne_d’ate: 'FMVSS 106.

- Fabriqués selon la norme interne d’ATE'
    val_100__: '100 %'
    val_100_a: '100 a'
    val_7_a: '7 a'
    val_72_a: '72 a'
  materials:
  - materiau: 'EPDM'
    source_ref: corpus RAG web OEM
-_fabriqués_selon_la_norme_interne_d’ate: 'FMVSS 106.

- Fabriqués selon la norme interne d’ATE'
    val_100__: '100 %'
    val_100_a: '100 a'
    val_7_a: '7 a'
    val_72_a: '72 a'
  materials:
  - materiau: 'EPDM'
    source_ref: corpus RAG web OEM
phase5_enrichment:
  _source: ate-freinage.fr + delphiautoparts.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 6
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_fmvss_106.

-_fabriqués_selon_la_norme_interne_d’ate: 'FMVSS 106.

- Fabriqués selon la norme interne d’ATE'
    val_100__: '100 %'
    val_100_a: '100 a'
    val_7_a: '7 a'
    val_72_a: '72 a'
  materials:
  - materiau: 'EPDM'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Unflexible de frein est un tuyau en caoutchouc souples renforcé par des
    fibres synthétique et une couche plastiquepour s'adapter au mouvementdu
    véhicule, il assure la circulation du liquide de frein du maître-cylindre de
    frein jusqu'aux étriers de frein avant ou arrière pour pousser les
    plaquettes de frein contre lesdisques de frein ou vers les cylindres de
    roues de la voiture pour écarter les mâchoires defrein contre les tambours
    de frein afin de ralentir ou arrêter le véhicule. Sur chaque véhicule on
    peut compter de 4 à 8 flexible defrein selon le niveau d'équipementde chaque
    voiture. En savoir plus : flexible de frein — définition et rôle mécanique 🚨
    Bruit Flexible de frein : causes et diagnostic
  S2: >-
    Ne pas attendre la panne complete pour intervenir. Symptômes d'usure : -
    Craquelures ou fissures visibles sur le flexible - Gonflement flexible lors
    appui pedale - Fuite de liquide de frein au niveau du flexible - Pedale de
    frein spongieuse ou molle - Freinage qui tire d un cote flexible bouche -
    Sifflement bruit niveau flexible sous - Odeur de liquide de frein fuite -
    Plus depuis dernier changement flexibles - # Flexibles de frein - Accueil
    Pièces Freinage Freinage Flexibles de frein Flexibles de frein Assurant la
    transmission de la pression hydraulique vers les étriers de frein ou les
    cylindres de roue,...
  S3: >-
    Pour choisir les bons flexible de frein pour votre véhicule : - Marque de
    votre véhicule - Modele de votre véhicule - Annee de votre véhicule -
    Vérifier : craquelures ou fissures visibles sur le flexible - Vérifier :
    gonflement flexible lors appui pedale - Vérifier : fuite de liquide de frein
    au niveau du flexible - Vérifier : pedale de frein spongieuse ou molle -
    Vérifier : freinage qui tire d un cote flexible bouche - Vérifier : odeur de
    liquide de frein fuitePour aller plus loin : consultez notre guide d'achat
    flexible de frein — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    1. Lever le vehicule, deposer la roue, securiser sur chandelles. 2. Placer
    un bac de recuperation sous le flexible — le liquide de frein coule a la
    deconnexion. 3. Devisser le raccord du flexible cote canalisation rigide
    (cle a tuyauter pour ne pas arrondir l'ecrou) — obturer la canalisation
    immediatement. 4. Devisser le raccord cote etrier de frein (cle plate ou cle
    a tuyauter selon vehicule). 5. Retirer le clip de maintien du flexible sur
    son support de carrosserie ou de suspension. 6. Deposer le flexible complet.
    7. Comparer le flexible neuf avec l'ancien : longueur, type de raccords,
    position du clip de fixation.
  S4_REPOSE: >-
    La repose d'un flexible de frein est une opération critique qui touche au
    circuit hydraulique de freinage. Chaque étape doit être réalisée sans forcer
    sur les raccords filetés et la purge du circuit est obligatoire avant tout
    test au roulage. Travaillez toujours sur véhicule calé, roue déposée. -
    Comparez le flexible de frein neuf avec celui déposé : longueur, diamètre
    des raccords (10 mm ou 12 mm), type de fixation côté caisse (agrafe ou écrou
    de bridage). Toute différence de longueur interdit le montage. - Contrôlez
    l'état de l'étrier de frein et du cylindre de roue : traces de fuite,
    corrosion sur les raccords. Remplacez-les si des suintements sont visibles,
    pour ne pas refaire la purge dans quelques semaines. - Enduisez légèrement
    les filetages des raccords de flexible de frein avec un produit anti-
    grippage adapté aux circuits hydrauliques (jamais de graisse polyvalente qui
    dégrade le caoutchouc). - Vissez à la main le raccord côté étrier ou
    cylindre de roue pour amorcer le filet sans forcer. Serrez ensuite à la clé
    à tuyauter au couple prescrit par le constructeur (généralement 14 à 17
    N·m). Ne serrez jamais avec une pince étau. - Fixez le flexible de frein
    côté caisse en engageant l'agrafe de maintien ou en serrant l'écrou de
    bridage. Vérifiez que le flexible n'est pas vrillé sur son axe longitudinal
    (un trait de repère tracé lors de la dépose aide à retrouver l'orientation).
    - Contrôlez le positionnement du flexible en braquant la direction en butée
    gauche puis droite et en comprimant la suspension : le flexible ne doit
    jamais frotter sur la roue, le ressort hélicoïdal ou la carrosserie dans
    aucune position. - Remplissez le réservoir de liquide de frein jusqu'au
    repère MAX avec le liquide préconisé par le constructeur (DOT 4 ou DOT 5.1
    selon spécification). Ne mélangez jamais deux indices DOT différents. -
    Purgez le circuit de freinage au niveau du flexible remplacé en ouvrant la
    vis de purge de l'étrier et en poussant du liquide neuf depuis le réservoir
    jusqu'à ce que la sortie soit exempte de bulles d'air. - Remontez la roue et
    serrez les écrous ou boulons de jante au couple constructeur (généralement
    100 à 120 N·m selon le véhicule). - Avant de démarrer, appuyez plusieurs
    fois sur la pédale de frein depuis l'habitacle jusqu'à ce qu'elle devienne
    ferme et résistante. Une pédale molle après plusieurs appuis indique une
    purge incomplète — recommencez la purge avant tout déplacement. ✅ Après
    remontage, vérifiez les spécifications dans la fiche technique Flexible de
    frein.
  S5: >-
    - ❌ "homologué CT" - ❌ "sécurité garantie" - ❌ "zéro panne" - ❌ "garanti à
    vie" - ❌ "freinage ameliore" - ## La normalité ? Trop peu pour . En terme de
    la qualité, refuse les compromis. Nos flexibles de frein vont donc au-delà
    des normes en vigueur. Répondant aux critères extrêmement élevés de la
    norme...
  S6: >-
    Contrôles statiques - Vérifier l'absence de fuite aux deux raccords du
    flexible (côté canalisation et côté étrier/cylindre) - Contrôler que le
    flexible ne touche pas la roue ou le disque en braquage complet gauche et
    droite - Vérifier le niveau de liquide de frein dans le bocal - Pomper la
    pédale : elle doit devenir dure après 3 à 5 appuis Essai routier progressif
    - Freinage doux à 10 km/h, vérifier que le véhicule freine droit - Augmenter
    à 30, 50 puis 70 km/h avec des freinages normaux - Effectuer des braquages
    complets à basse vitesse pour vérifier l'absence de frottement - Après 5 km,
    s'arrêter et inspecter visuellement les raccords (aucune goutte) ⚠️ Arrêter
    immédiatement si : pédale molle, fuite visible, tirage au freinage,
    gonflement du flexible (poche sous pression), bruit de frottement en
    braquant. 🚨 Bruit Flexible de frein : causes et diagnostic
  S_GARAGE: >-
    Nous vous recommandons de confier cette intervention à un professionnel : -
    Plusieurs causes possibles de défaillance (4 identifiées) nécessitent un
    diagnostic professionnel Un garagiste qualifié dispose de l'outillage et de
    l'expérience nécessaires pour effectuer cette opération en toute sécurité.
  S7: >-
    Quel est le prix d'un flexible de frein ?Le prix varie selon le véhicule et
    la marque. Utilisez notre sélecteur pour trouver le flexible de frein
    compatible avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon flexible de frein est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un flexible de frein défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la
    sécurité du véhicule. Consultez la section symptômes pour évaluer l'urgence
    du remplacement.- capteur abs - cylindre de roue - disque de frein - etrier
    de frein - interrupteur des feux de freins - kit de freins arriere -
    machoires de frein - maitre cylindre de frein
  S8: >-
    Flexible OE ou renforcé : que choisir ?Les flexibles OE suffisent pour un
    usage normal. Les flexibles renforcés (aviation/tressés) offrent une
    meilleure sensation de pédale pour une conduite sportive. Comment savoir si
    mon flexible de frein est HS ?Craquelures visibles sur le caoutchouc,
    gonflement du flexible au freinage, fuite de liquide, pédale de frein
    spongieuse. Tous les combien changer les flexibles de frein ?Tous les 10 ans
    ou 150 000 km recommandé. Le caoutchouc vieillit même sans rouler. Contrôle
    visuel à chaque révision. Peut-on changer un flexible de frein soi-même
    ?Oui, mais nécessite de purger le circuit après. Attention à ne pas vriller
    le flexible au montage. Utilisez une clé à tuyauter. Quelle erreur éviter
    avec les flexibles ?Ne jamais plier ou tordre un flexible. Ne pas utiliser
    de pince étau pour le pincer. Vérifier que le flexible ne frotte pas sur la
    roue en braquant.
  META: >-
    Guide complet pour remplacer vos flexibles de frein : compatibilité des
    raccords, purge du circuit, erreurs à éviter et FAQ pour un freinage sûr.
---

# Flexible de frein - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre la pression hydraulique entre les elements mobiles

**Actions principales:** transmettre la pression, acheminer le liquide, resister a la pression, conduire le fluide, relier

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Fuite de liquide de frein au niveau du flexible**
  fuite de liquide de frein au niveau du flexible
- **Pedale de frein spongieuse ou molle**
  pedale de frein spongieuse ou molle
- **Freinage qui tire d un cote flexible bouche**
  freinage qui tire d un cote flexible bouche
- **Odeur de liquide de frein fuite**
  odeur de liquide de frein fuite

### 🟢 Autres Symptômes

- craquelures ou fissures visibles sur le flexible
- gonflement flexible lors appui pedale
- sifflement bruit niveau flexible sous
- plus depuis dernier changement flexibles

## Procédure de Diagnostic

Pour diagnostiquer un problème de flexible de frein:

1. **Inspection visuelle** - Examiner l'état du flexible de frein
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
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

- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere
- machoires-de-frein
- maitre-cylindre-de-frein

## Critères de Compatibilité

Pour commander le bon flexible de frein, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage ameliore"

## FAQ

**Flexible OE ou renforcé : que choisir ?**
Les flexibles OE suffisent pour un usage normal. Les flexibles renforcés (aviation/tressés) offrent une meilleure sensation de pédale pour une conduite sportive.

**Comment savoir si mon flexible de frein est HS ?**
Craquelures visibles sur le caoutchouc, gonflement du flexible au freinage, fuite de liquide, pédale de frein spongieuse.

**Tous les combien changer les flexibles de frein ?**
Tous les 10 ans ou 150 000 km recommandé. Le caoutchouc vieillit même sans rouler. Contrôle visuel à chaque révision.

**Peut-on changer un flexible de frein soi-même ?**
Oui, mais nécessite de purger le circuit après. Attention à ne pas vriller le flexible au montage. Utilisez une clé à tuyauter.

**Quelle erreur éviter avec les flexibles ?**
Ne jamais plier ou tordre un flexible. Ne pas utiliser de pince étau pour le pincer. Vérifier que le flexible ne frotte pas sur la roue en braquant.


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
