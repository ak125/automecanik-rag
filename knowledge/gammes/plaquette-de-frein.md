---
category: freinage
slug: plaquette-de-frein
title: Plaquette de frein
pg_id: 402
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-04-02'
verification_status: draft
intent_targets:
- diagnostic
- achat
- reference
- entretien
business_priority: high
priority_signals:
  avg_basket: 120
  monthly_searches: 8000
  margin_tier: high
lifecycle:
  stage: auto_generated
  last_enriched_by: script:rag-enrich-from-web-corpus
  last_enriched_at: '2026-04-02'
  v5_migrated_at: '2026-03-29'
_sources:
  ece-r90:
    type: norm
    doc: null
    note: Norme europeenne performances freinage remplacement
  experience-atelier:
    type: field-expertise
    note: Retours atelier partenaire, donnees constructeurs
domain:
  role: La plaquette de frein est la garniture de friction pressee contre le disque par l'etrier hydraulique pour ralentir
    le vehicule de maniere progressive et repetable
  must_be_true:
  - friction
  - etrier
  - disque
  - garniture
  - paire
  must_not_contain:
  - tambour de frein
  - frein a main
  confusion_with:
  - term: disque de frein
    difference: Le disque est le plateau metallique fixe au moyeu; la plaquette est la garniture qui frotte contre le disque
  - term: machoire de frein
    difference: La machoire est utilisee dans un systeme a tambour; la plaquette est specifique au systeme a disque
  related_parts:
  - Disques de frein (a controler systematiquement au changement de plaquettes)
  - Etrier de frein (presse les plaquettes contre le disque)
  - Flexible de frein (transmet la pression hydraulique a l'etrier)
  - Capteur d'usure (alerte quand la garniture atteint l'epaisseur minimale)
  - Liquide de frein (a purger si le circuit a ete ouvert)
  norms:
  - ECE R90 — performances de freinage proches de l'equipement d'origine
  cross_gammes:
  - slug: disque-de-frein
    relation: always_together
    context: Des plaquettes neuves sur des disques uses ne freinent pas correctement. Remplacer conjointement.
  - slug: etrier-de-frein
    relation: check_on_replace
    context: Controler l'etat de l'etrier et des guidages au demontage des plaquettes
  - slug: flexible-de-frein
    relation: check_on_replace
    context: Verifier l'etat du flexible si le circuit hydraulique est ouvert
  - slug: liquide-de-frein
    relation: check_on_replace
    context: Purger le liquide de frein si le circuit hydraulique a ete ouvert
selection:
  criteria:
  - 'Essieu : avant (supporte 70% de l''effort de freinage) ou arriere (stabilite)'
  - 'Materiau : semi-metallique (polyvalent), ceramique (silencieux, peu de poussiere), organique (souple, confort)'
  - Dimensions et reference OE (specifiques au vehicule et a l'etrier)
  - 'Usage : standard (urbain/mixte 20-50 EUR/jeu), haute capacite (montagne 50-80 EUR), sport (80-120 EUR)'
  checklist:
  - Verifier l'essieu concerne (avant ≠ arriere)
  - Commander par jeu de 4 plaquettes (1 essieu complet)
  - Controler l'etat des disques (les changer si uses)
  - Verifier la compatibilite avec le capteur d'usure si present
  - Choisir le materiau adapte a l'usage (urbain, montagne, sport)
  - Privilegier une marque reconnue (Bosch, TRW, Brembo, Ferodo)
  anti_mistakes:
  - Commander pour le mauvais essieu (avant ≠ arriere)
  - Melanger des garnitures de materiaux differents sur un meme essieu
  - Oublier de controler l'etat des disques au changement de plaquettes
  - Choisir uniquement sur le prix sans verifier marque et qualite
  - Ne pas respecter la periode de rodage (200 km de freinage progressif)
  cost_range:
    min: 20
    max: 120
    currency: EUR
    unit: le jeu (4 plaquettes, 1 essieu
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE (OES)
  - tier: Adaptable qualite
  - tier: Reconditionne
  - tier: Echange standard
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
    label: Grincement metallique au freinage
    severity: securite
  - id: S2
    label: Temoin d'usure allume au tableau de bord
    severity: securite
  - id: S3
    label: Distance de freinage allongee
    severity: securite
  causes:
  - Usure normale de la garniture (kilometrage)
  - Freinage intensif repete (conduite urbaine, descentes prolongees)
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - Inspection visuelle a travers la jante (epaisseur de garniture visible)
  - Ecouter un grincement metallique au freinage leger
  depose_steps: []
maintenance:
  interval:
    value: 30000-50000
    unit: km
    note: Variable selon style de conduite, type de garniture et conduite urbaine vs route
    source: null
  good_practices:
  - Controle visuel a chaque revision
  - Mesure d'epaisseur au pied a coulisse (minimum 3 mm)
  wear_signs:
  - Temoin d'usure qui touche le disque (grincement metallique)
  - Epaisseur de garniture inferieure a 3 mm
rendering:
  pgId: '402'
  intro_title: A quoi sert la plaquette de frein ?
  risk_title: Pourquoi remplacer les plaquettes de frein a temps ?
  risk_explanation: Des plaquettes usees reduisent l'efficacite de freinage et endommagent les disques.
  risk_consequences:
  - Distance de freinage allongee
  - Destruction des disques de frein
  - Grincement metallique permanent
  risk_conclusion: Un controle regulier et un remplacement par essieu complet sont indispensables.
  arguments:
  - title: Compatibilite verifiee
    icon: check-circle
    source_ref: null
  - title: Priorite securite
    icon: shield-check
    source_ref: null
  - title: Decision rapide
    icon: clock
    source_ref: null
  - title: Montage maitrise
    icon: list-check
    source_ref: null
  faq:
  - question: Faut-il changer les 4 plaquettes en meme temps ?
    answer: On remplace les plaquettes par essieu (les 4 d'un meme essieu). Il n'est pas necessaire de changer avant et arriere
      simultanement sauf si les deux sont uses.
  - question: Plaquettes ceramiques ou semi-metalliques ?
    answer: Les ceramiques sont plus silencieuses et generent moins de poussiere. Les semi-metalliques offrent un meilleur
      freinage a haute temperature. Pour un usage urbain standard, les deux conviennent.
  - question: Combien de temps durent les plaquettes ?
    answer: Entre 30 000 et 50 000 km en usage mixte. En conduite urbaine intensive, l'usure peut etre plus rapide.
  - question: Peut-on changer ses plaquettes soi-meme ?
    answer: Le remplacement est accessible a un bricoleur equipe, mais le freinage est un element de securite critique. En
      cas de doute, confiez le montage a un professionnel.
  quality:
    score: 76
    source: stub-manual
    version: GammeContentContract.v4
seo_cluster:
  source: keyword-dataset
  updated_at: '2026-02-23'
  schema_version: '1.0'
  primary_keyword:
    text: plaquettes de freins bosch
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
  keyword_variants:
  - keyword: disque et plaquette de frein clio 4
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: prix disque et plaquette de frein peugeot 308
    volume: 500
    traffic_range: 250-1250/mo
    intent: transactionnelle
    competition: moyenne
  - keyword: prix plaquette et disque de frein clio 4
    volume: 500
    traffic_range: 250-1250/mo
    intent: transactionnelle
    competition: moyenne
  - keyword: prix disque et plaquette de frein peugeot 3008
    volume: 500
    traffic_range: 250-1250/mo
    intent: transactionnelle
    competition: moyenne
  - keyword: plaquettes de frein bmw serie 1
    volume: 500
    traffic_range: 250-1250/mo
    intent: informationnelle
    competition: moyenne
  - keyword: prix disque et plaquette de frein peugeot 208
    volume: 500
    traffic_range: 250-1250/mo
    intent: transactionnelle
    competition: moyenne
  - keyword: disque et plaquette de frein 207 prix
    volume: 50
    traffic_range: 25-125/mo
    intent: transactionnelle
    competition: faible
  - keyword: disque et plaquette de frein citroën c3
    volume: 50
    traffic_range: 25-125/mo
    intent: informationnelle
    competition: faible
  - keyword: disque et plaquette de frein c4 picasso prix
    volume: 50
    traffic_range: 25-125/mo
    intent: transactionnelle
    competition: faible
  - keyword: prix disque et plaquette de frein c3
    volume: 50
    traffic_range: 25-125/mo
    intent: transactionnelle
    competition: faible
  paa_questions: []
  role_mapping:
    R1: prix disque et plaquette de frein peugeot 308
    R3_guide: plaquettes de freins bosch
    R3_conseils: quand changer plaquette de frein
    R4: plaquette de frein definition
    R5: symptome plaquette de frein use
doc_id: 06dbeae8-79b3-5241-9d4c-a1157becc7a5
content_hash: sha256:114f27b86d0c95b7
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
  _source: aftermarket.zf.com + ate-freinage.fr + bremboparts.com + delphiautoparts.com + ferodo.com + gpa26.com + profauto.fr + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 92
  _has_tech_data: true
  types_variants:
  - type: 'Composite'
    source_ref: corpus RAG web OEM
  - type: 'NAO'
    source_ref: corpus RAG web OEM
  - type: 'composite'
    source_ref: corpus RAG web OEM
  - type: 'céramique'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_dot5.1: 'DOT5.1'
    norme_ece_r90: 'ECE R90'
    norme_sae_j2521: 'SAE J2521'
    val_0_035_mm: '0,035 mm'
    val_0_05_mm: '0,05 mm'
    val_0_1_mm: '0,1 mm'
    val_0_10_mm: '0,10 mm'
    val_0_12_mm: '0,12 mm'
    val_0_15_mm: '0,15 mm'
    val_0_5__: '0,5 %'
    val_000_km: '000 km'
    val_1_5_mm: '1,5 mm'
    val_1__v: '1. V'
    val_10__m: '10 µm'
    val_10__v: '10. V'
    val_100__: '100 %'
    val_100_a: '100 a'
    val_110_nm: '110 Nm'
  materials:
  - materiau: 'EPDM'
    source_ref: corpus RAG web OEM
  - materiau: 'HNBR'
    source_ref: corpus RAG web OEM
  - materiau: 'acier inoxydable'
    source_ref: corpus RAG web OEM
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
  - materiau: 'céramique'
    source_ref: corpus RAG web OEM
  - materiau: 'fonte grise'
    source_ref: corpus RAG web OEM
  - materiau: 'graphite'
    source_ref: corpus RAG web OEM
  - materiau: 'silicone'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'La plaquette de frein est la garniture de friction pressee contre le disque par l''etrier hydraulique pour ralentir
    le vehicule de maniere progressive et repetable. Composition : un support metallique + une garniture de friction collee
    ou rivetee. L''epaisseur minimale de la garniture est de 2 mm — en dessous, le freinage est dangereux. Types de garnitures
    : - Organiques : souples, silencieuses, usure plus rapide — adaptees a la conduite urbaine- Semi-metalliques : bon compromis
    performance/duree — les plus repandues en premiere monte- Ceramiques : freinage stable a haute temperature, moins de poussiere
    — vehicules sportifs ou haut de gammeControle visuel : l''epaisseur de la garniture est visible a travers l''ouverture
    de l''etrier sans demontage. Si la garniture est au niveau du temoin d''usure ou en dessous de 2-3 mm, le remplacement
    est immediat. Pieces liees : Disques de frein (a controler systematiquement au changement de plaquettes), Etrier de frein
    (presse les plaquettes contre le disque), Flexible de frein (transmet la pression hydraulique a l''etrier), Capteur d''usure
    (alerte quand la garniture atteint l''epaisseur minimale), Liquide de frein (a purger si le circuit a ete ouvert).'
  S2: 'Les plaquette de frein sont à remplacer tous les 30 000 à 50 000 km environ. Variable selon style de conduite, type
    de garniture et conduite urbaine vs route Symptômes d''usure : - Grincement metallique au freinage - Temoin d''usure allume
    au tableau de bord - Distance de freinage allongee'
  S2_DIAG: SymptômeCause probableActionGrincement metallique au freinageUsure normale de la garniture (kilometrage)Inspection
    visuelle a travers la jante (epaisseur de garniture visible)Temoin d'usure allume au tableau de bordFreinage intensif
    repete (conduite urbaine, descentes prolongees)Ecouter un grincement metallique au freinage legerDistance de freinage
    allongeeUsure mecanique progressiveInspection visuelle a travers la jante (epaisseur de garniture visible)
  S3: 'Pour choisir les bons plaquette de frein pour votre véhicule : - Essieu : avant (supporte 70% de l''effort de freinage)
    ou arriere (stabilite) - Materiau : semi-metallique (polyvalent), ceramique (silencieux, peu de poussiere), organique
    (souple, confort) - Dimensions et reference OE (specifiques au vehicule et a l''etrier) - Usage : standard (urbain/mixte
    20-50 EUR/jeu), haute capacite (montagne 50-80 EUR), sport (80-120 EUR)Pour aller plus loin : consultez notre guide d''achat
    plaquette de frein — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 1. Desserrez les boulons de roue, levez et calez le véhicule sur chandelles. 2. Démontez la roue. 3. Retirez
    les vis ou clips de maintien des plaquettes. 4. Repoussez le piston de l'étrier à l'aide d'un repousse-piston (vérifiez
    le niveau de liquide de frein au fur et à mesure). 5. Déclipsez ou dévissez l'étrier et suspendez-le sans tendre le flexible
    de frein. 6. Retirez les anciennes plaquettes et nettoyez le support d'étrier au nettoyant frein.
  S4_REPOSE: 'Le remontage des plaquettes de frein conditionne directement la sécurité au freinage. Après avoir nettoyé l''étrier
    et repris les pistons, chaque étape de remise en place doit être effectuée avec soin : un mauvais sens de montage, un
    piston non remis en position ou une pédale non purgée peuvent conduire à une défaillance du freinage. Remplacer systématiquement
    par essieu complet — les 4 plaquettes d''un même essieu simultanément. - Contrôler l''état des disques avant remontage
    — Inspecter les disques de frein gauche et droit : présence de rainures profondes, de traces bleues thermiques ou d''épaisseur
    sous le seuil minimal gravé sur la tranche. Des plaquettes neuves montées sur des disques usés ne freinent pas correctement
    et s''usent prématurément. Remplacer les disques si nécessaire. - Vérifier l''état des étriers — Contrôler que les étriers
    de frein ne sont pas grippés et que les pistons se rétractent librement. Nettoyer les glissières de guidage des plaquettes
    à la brosse métallique. Un étrier grippé génère une usure dissymétrique et surchauffe la plaquette intérieure. - Nettoyer
    le système et repousser les pistons — Dépoussiérer l''ensemble du système de freinage avec un nettoyant frein dégraissant.
    Repousser le(s) piston(s) de l''étrier à l''aide d''un repousse-piston, après avoir ouvert légèrement le bocal de liquide
    de frein pour éviter le débordement. - Monter les nouvelles plaquettes — Insérer les plaquettes de frein neuves dans les
    glissières de l''étrier en respectant scrupuleusement le sens de montage (flèche ou marquage « R » côté rotation du disque).
    Vérifier que les ressorts anti- vibration et les cales anti-bruit sont correctement positionnés. - Remplacer les accessoires
    et témoins d''usure — Changer systématiquement les accessoires de plaquettes (ressorts, clips de retenue) et les témoins
    d''usure gauche et droit. Brancher les connecteurs des témoins d''usure avant de refermer l''étrier. - Graisser et remonter
    l''étrier — Appliquer de la graisse haute température sur les vis de colonette et les points de contact des glissières
    (jamais sur la piste du disque ni sur la garniture). Repositionner l''étrier de frein sur les plaquettes et serrer les
    boulons au couple prescrit (généralement 25 à 35 Nm selon modèle). - Remonter la roue — Remettre la roue en place et serrer
    les écrous à la croix au couple constructeur (généralement 110 à 130 Nm). Rebrancher la batterie si elle avait été déconnectée
    pour réinitialiser le témoin ABS. - Pomper la pédale et descendre le véhicule — Avant de descendre le véhicule, pomper
    plusieurs fois la pédale de frein jusqu''à ce qu''elle soit ferme et résistante. Les pistons de l''étrier reprennent leur
    position de travail au contact des nouvelles plaquettes. Descendre le véhicule et resserrer les écrous de roue au couple
    après remontage du véhicule au sol. - Rodage sur les 200 premiers kilomètres — Effectuer 5 à 6 freinages progressifs de
    80 km/h à 30 km/h en laissant les disques refroidir entre chaque décélération. Éviter tout freinage d''urgence pendant
    le rodage : la surface de contact entre la garniture et le disque doit se former progressivement. Contrôler le bon fonctionnement
    du système de freinage.'
  S5: '- Commander pour le mauvais essieu (avant ≠ arriere) - Melanger des garnitures de materiaux differents sur un meme
    essieu - Oublier de controler l''etat des disques au changement de plaquettes - Choisir uniquement sur le prix sans verifier
    marque et qualite - Ne pas respecter la periode de rodage (200 km de freinage progressif)'
  S6: Après avoir remplacé vos plaquettes de frein, ces vérifications techniques sont indispensables avant toute reprise de
    la route. Un contrôle rigoureux garantit l'efficacité du freinage et évite tout incident. - Pomper la pédale avant de
    démarrer — Appuyer et relâcher la pédale de frein 5 à 8 fois jusqu'à ce qu'elle soit ferme et ne descende plus. Si la
    pédale reste molle ou descend jusqu'au plancher, le circuit hydraulique est mal purgé ou il y a une fuite à inspecter
    immédiatement. - Contrôler le niveau du liquide de frein — Vérifier le niveau dans le bocal après avoir repoussé les pistons
    (le niveau remonte). S'il déborde, retirer l'excédent. Le niveau doit se situer entre MIN et MAX. - Vérifier l'absence
    de bruit au premier démarrage — Rouler doucement à 5 km/h et freiner légèrement. Aucun grincement métallique ne doit être
    audible. Un léger sifflement initial (1-2 frenages) est normal avec des plaquettes neuves. - Contrôler qu'aucune fuite
    hydraulique n'est présente — Inspecter visuellement les flexibles, l'étrier et les raccords après le premier trajet. Toute
    trace humide ou colorée signe une fuite à traiter avant de rouler. - Contrôle visuel des boulons d'étrier — Vérifier visuellement
    que les boulons de guidage de l'étrier sont bien en place et serrés. Un étrier mal fixé provoque des vibrations au freinage
    et peut se bloquer. - Respecter le rodage sur 200 km — Durant les 200 premiers kilomètres, éviter tout freinage d'urgence.
    La garniture neuve doit se "roder" progressivement contre le disque pour atteindre sa pleine capacité de friction. En
    cas de freinage trop violent avant rodage, les plaquettes peuvent se vitrifier. - Re-contrôler les couples de serrage
    après 50 km — Après le premier rodage, vérifier le serrage des boulons de roue à la clé dynamométrique au couple constructeur.
    - Vérifier l'absence de tirage latéral au freinage — Sur une route droite et dégagée, freiner progressivement. Le véhicule
    ne doit pas dévier d'un côté. Un tirage signale un étrier grippé ou des plaquettes déséquilibrées entre les deux côtés
    de l'essieu.
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (5 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: Quel est le prix d'un plaquette de frein ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour
    trouver le plaquette de frein compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon plaquette de frein est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un plaquette de frein défaillant
    ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section
    symptômes pour évaluer l'urgence du remplacement.- Disques de frein (a controler systematiquement au changement de plaquettes)
    - Etrier de frein (presse les plaquettes contre le disque) - Flexible de frein (transmet la pression hydraulique a l'etrier)
    - Capteur d'usure (alerte quand la garniture atteint l'epaisseur minimale) - Liquide de frein (a purger si le circuit
    a ete ouvert)
  S8: Faut-il changer les 4 plaquettes en meme temps ?On remplace les plaquettes par essieu (les 4 d'un meme essieu). Il n'est
    pas necessaire de changer avant et arriere simultanement sauf si les deux sont uses. Plaquettes ceramiques ou semi-metalliques
    ?Les ceramiques sont plus silencieuses et generent moins de poussiere. Les semi-metalliques offrent un meilleur freinage
    a haute temperature. Pour un usage urbain standard, les deux conviennent. Combien de temps durent les plaquettes ?Entre
    30 000 et 50 000 km en usage mixte. En conduite urbaine intensive, l'usure peut etre plus rapide. Peut-on changer ses
    plaquettes soi-meme ?Le remplacement est accessible a un bricoleur equipe, mais le freinage est un element de securite
    critique. En cas de doute, confiez le montage a un professionnel.
  META: '- Changer vos plaquettes de frein Golf 4 1.9 TDI.'
---

# Plaquette de frein

## FAQ

**Faut-il changer les 4 plaquettes en meme temps ?**
On remplace les plaquettes par essieu (les 4 d'un meme essieu). Il n'est pas necessaire de changer avant et arriere simultanement sauf si les deux sont uses.

**Plaquettes ceramiques ou semi-metalliques ?**
Les ceramiques sont plus silencieuses et generent moins de poussiere. Les semi-metalliques offrent un meilleur freinage a haute temperature. Pour un usage urbain standard, les deux conviennent.

**Combien de temps durent les plaquettes ?**
Entre 30 000 et 50 000 km en usage mixte. En conduite urbaine intensive, l'usure peut etre plus rapide.

**Peut-on changer ses plaquettes soi-meme ?**
Le remplacement est accessible a un bricoleur equipe, mais le freinage est un element de securite critique. En cas de doute, confiez le montage a un professionnel.

## Entretien et Intervalles

- **Intervalle** : 30000-50000
- Variable selon style de conduite, type de garniture et conduite urbaine vs route
## Definition

La norme ECE R90 encadre la conformite des pieces de freinage de remplacement (ex: plaquettes, disques) avec des exigences de performance proches de l'equipement d'origine.

## Pourquoi c'est important

- meilleure coherence de freinage
- reduction du risque de pieces non conformes
- reference utile pour le choix de pieces sur vehicule de tourisme
## Pourquoi identifier soi-meme sa panne ?

Un diagnostic precoce permet d'eviter une panne totale, de reduire le cout de reparation et d'arriver chez le garagiste avec une hypothese claire. 80% des pannes presentent des signes avant-coureurs pendant plusieurs semaines avant l'immobilisation.

## Les 3 methodes pour identifier une panne auto

### 1. Observer les symptomes sensoriels (sans outil)

Chaque organe du vehicule communique par un canal sensoriel distinct :

| Canal | Exemples | Zone probable |
|-------|----------|---------------|
| Auditif | Sifflement, claquement, grincement | Freinage, suspension, moteur |
| Visuel | Fumee, voyant, fuite | Moteur, circuit de refroidissement, freins |
| Tactile | Vibration, a-coup, pedale molle | Suspension, embrayage, freinage |
| Olfactif | Odeur de brule, de caoutchouc | Embrayage, freins, circuit electrique |

### 2. Lire les voyants du tableau de bord

Les voyants sont le premier niveau de diagnostic embarque. Leur couleur indique l'urgence :
- Rouge : arret immediat obligatoire (huile, temperature, frein)
- Orange : attention requise rapidement (moteur, ABS, FAP)
- Jaune/vert : information (entretien, assistance parking)

Un voyant orange moteur (check engine) indique une anomalie enregistree dans le calculateur. La lecture des codes OBD avec un scanner (protocole OBD2 depuis 2001) permet d'identifier le defaut exact.

### 3. Scanner le code OBD (P, C, B, U)

Les codes OBD se lisent avec un scanner OBD2 (disponibles a partir de 30 EUR) :
- P0xxx : moteur et transmission
- C0xxx : chassis (ABS, ESP)
- B0xxx : carrosserie (airbags, sieges)
- U0xxx : reseau de communication

## Les 10 signes avant-coureurs d'une panne

1. **Bruit inhabituel au freinage** — sifflement aigu = plaquettes usees, grincement = disques ou etrier
2. **Voyant moteur allume** — code OBD a lire dans les 48h
3. **Vibration au volant** — a vitesse constante : pneumatiques ; au freinage : disques voiles
4. **Demarrage difficile** — lent, bruyant ou manque = batterie, demarreur ou alternateur
5. **Surconsommation soudaine** — injecteurs, bougie, fuite circuit d'alimentation
6. **Fumee a l'echappement** — blanche = liquide de refroidissement ; noire = richesse essence ; bleue = huile
7. **Perte de puissance** — turbo, FAP obstrue, injecteurs defaillants
8. **Odeur de brule** — embrayage en patinage, frein grippe, court-circuit electrique
9. **Pedale de frein molle** — fuite liquide de frein, plaquettes usees extremes
10. **Voyant ABS ou ESP** — capteur de roue, bloc hydraulique

## Panne mecanique vs electrique : comment distinguer

| Critere | Mecanique | Electrique |
|---------|-----------|------------|
| Manifestation | Progressive, sonore, vibratoire | Soudaine, voyant allume |
| Temperature | Souvent liee a la montee en temperature | Independante |
| Diagnostic | Inspection visuelle, ecoute | Scanner OBD indispensable |
| Exemples | Usure plaquettes, joint HS, courroie | Capteur O2, calculateur, alternateur |

## Que faire en cas de panne sur autoroute ?

**Priorite absolue : securiser le vehicule et les occupants.**

1. Allumer les feux de detresse immediatement
2. Se garer sur la bande d'arret d'urgence (BAU), le plus a droite possible
3. Couper le moteur et serrer le frein a main
4. Sortir du vehicule par la droite et s'eloigner de la glissiere
5. Revetir le gilet de securite (obligatoire)
6. Poser le triangle de signalisation a 150m minimum (si possible sans danger)
7. Appeler le 3477 (societe d'autoroute) depuis une borne d'appel orange ou votre telephone

**Ne jamais tenter de reparer sur la BAU.** Appelez le prestataire agree de l'autoroute.
## Mots-clés et expressions SEO

### Intention informationnelle
- comment trouver pièce auto compatible avec mon véhicule
- comment être sûr de commander la bonne pièce auto
- comment savoir le type de motorisation de ma voiture
- c'est quoi F1 F2 F3 sur une carte grise
- quelle est la différence entre type mine et code moteur
- où trouver le numéro VIN de mon véhicule
- quelle est la différence entre pièce d'origine et pièce équipementier
- où trouver un logiciel de vue éclatée automobile gratuit
- comment trouver la référence d'une pièce auto
- mon véhicule a des variantes de montage : comment choisir la bonne pièce

### Intention commerciale
- sélecteur de véhicule pièces auto
- configurateur de pièces auto en ligne
- pièce auto avec carte grise
- numéro VIN 17 caractères pièces auto
- guide pratique choisir pièces auto
- sélection des pièces détachées par modèle de voiture
- information voiture avec plaque d'immatriculation gratuit

### Intention transactionnelle
- recherche pièces auto par plaque d'immatriculation
- trouver pièce auto avec numéro de châssis
- chercher pièce détachée par référence OEM
- trouver code moteur avec VIN gratuit
- trouver numéro OEM avec VIN gratuit

### Intention navigationnelle
- Automecanik sélecteur véhicule
- Automecanik recherche par immatriculation
- Automecanik recherche par VIN

## Les 4 méthodes d'identification

### 1. Par immatriculation (la plus rapide)

Saisissez votre numéro de plaque au format SIV (AA-123-BB) ou ancien format FNI. Le système identifie automatiquement votre véhicule en quelques secondes. C'est la recherche de pièces auto par plaque d'immatriculation la plus rapide pour les plaques françaises.

**Ce qu'il faut** : plaque française (SIV ou FNI)
**Fiabilité** : bonne (si la base est à jour)
**Limitation** : les plaques étrangères ne sont pas reconnues
**Recommandé si** : vous êtes sur le véhicule ou vous avez la plaque sous les yeux. Fonctionne aussi avec la carte grise (pièce auto par carte grise).

### 2. Par numéro VIN (la plus fiable)

Saisissez les 17 caractères du VIN (visible sur la carte grise au champ E ou sur le pare-brise côté conducteur). Cette méthode offre 99%+ de fiabilité et identifie la configuration exacte sortie d'usine, y compris pour les véhicules importés.

**Ce qu'il faut** : VIN de 17 caractères (carte grise champ E)
**Fiabilité** : excellente (99%+)
**Limitation** : le VIN n'est pas toujours sous la main
**Recommandé si** : pièces de sécurité (freins, suspension), véhicule importé, ou variantes de montage. Permet aussi de trouver le code moteur avec le VIN gratuitement.

### 3. Sélection manuelle — marque, modèle, motorisation (toujours disponible)

Sélectionnez successivement la marque (champ D.1 de la carte grise), le modèle/génération, l'année (champ B) et la motorisation (champ P.3). En cas de doute entre 2 motorisations proches, utilisez la recherche par VIN.

**Ce qu'il faut** : marque, modèle, année, motorisation
**Fiabilité** : bonne (si la motorisation exacte est sélectionnée)
**Limitation** : doute possible entre motorisations proches
**Recommandé si** : vous connaissez votre véhicule. Fonctionne sans carte grise. Sélection des pièces détachées par modèle de voiture.

### 4. Par référence OEM (la plus précise)

Saisissez le numéro OEM (Origine Équipementier) gravé sur la pièce d'origine pour trouver l'équivalent exact ou les alternatives compatibles chez d'autres fabricants. C'est la méthode pour chercher une pièce détachée par sa référence OEM avec 100% de précision.

**Ce qu'il faut** : numéro OE gravé sur la pièce usagée
**Fiabilité** : maximale (100%)
**Limitation** : nécessite d'avoir la pièce usagée sous les yeux
**Recommandé si** : vous avez le numéro OE de l'ancienne pièce. Permet un remplacement à l'identique garanti et de trouver les équivalences équipementiers.

## Tableau comparatif des méthodes

| Critère | Immatriculation | VIN | Manuelle | OEM |
|---------|-----------------|-----|----------|-----|
| **Fiabilité** | Bonne (si base à jour) | Excellente (99%+) | Bonne (si motorisation exacte) | Maximale (100%) |
| **Vitesse** | Quelques secondes | Quelques secondes | 1-2 minutes | Instantané |
| **Ce qu'il faut** | Plaque française (SIV/FNI) | 17 caractères (carte grise champ E) | Marque, modèle, année, motorisation | Numéro OE (gravé sur la pièce) |
| **Quand l'utiliser** | Commandes courantes | Pièces sécurité, variantes, import | Sans carte grise, véhicule connu | Remplacement à l'identique |
| **Limitation** | Plaques étrangères non reconnues | VIN pas toujours sous la main | Doute entre motorisations proches | Pièce usagée nécessaire |

## Carte grise — champs utiles pour identifier son véhicule

| Champ | Contenu | Utilité pour le sélecteur |
|-------|---------|---------------------------|
| **B** | Date de première immatriculation | Année du véhicule (étape 3 sélection manuelle) |
| **D.1** | Marque du véhicule | Étape 1 sélection manuelle |
| **D.2** | Type mine / variante / version | Identification précise de la version |
| **E** | Numéro VIN (17 caractères) | Méthode VIN — 99%+ de fiabilité |
| **P.3** | Type de carburant (essence, diesel, hybride, électrique, GPL) | Motorisation — étape 4 sélection manuelle |
| **F.1** | Masse en charge maximale techniquement admissible (PTAC) | Dimensionner freinage et suspension |
| **F.2** | PTAC de l'ensemble (véhicule + remorque) | Dimensionner freinage |
| **F.3** | Masse en charge maximale de l'ensemble en service (PTRA) | Dimensionner suspension (amortisseurs, ressorts) |

**Astuce** : prenez votre carte grise en photo avec votre téléphone. Vous aurez toutes les infos sous la main la prochaine fois, même loin du véhicule.

## Variantes de montage

Les constructeurs automobiles utilisent plusieurs fournisseurs pour une même pièce. En cours de production, ils peuvent changer de fournisseur, modifier des spécifications ou ajouter des options.

### Pourquoi les variantes existent

- **Multi-fournisseurs** : un même modèle peut être équipé en première monte par différents équipementiers selon la date et le lieu de fabrication.
- **Évolutions en série** : les constructeurs améliorent les pièces en continu. Un véhicule de début de série peut avoir des spécifications différentes d'un véhicule de fin de série.
- **Options d'usine** : les packs sport, suspensions pilotées ou systèmes Start & Stop modifient les pièces requises.

### Exemples courants de variantes (même véhicule)

| Catégorie | Variante |
|-----------|----------|
| **Freinage** | Diamètre disque 280 vs 288 vs 312 mm, ventilé vs plein |
| **Batterie** | Start & Stop → AGM/EFB obligatoire |
| **Filtration** | Cartouche vs vissé selon moteur |
| **Suspension** | Standard vs sport / pilotée |

### Comment éviter l'erreur

1. Vérifiez les critères clés sur la fiche produit (diamètre, capteur, type de fixation).
2. Privilégiez le VIN quand c'est disponible — 99% de compatibilité.
3. En cas de doute : comparez le numéro OE de l'ancienne pièce avec les références proposées. Le numéro OE = la meilleure confirmation.

## Dépannage

### Mon véhicule n'apparaît pas dans le sélecteur

**Cause probable** : véhicule importé, très récent, ou plaque étrangère non reconnue.
**Solution** : passez en recherche par VIN (champ E de la carte grise). Les véhicules importés depuis l'Allemagne ou la Belgique sont généralement reconnus par VIN même si la plaque ne fonctionne pas.

### J'hésite entre deux motorisations proches

**Cause probable** : le modèle existe avec plusieurs cylindrées ou puissances similaires (ex : 1.5 dCi 90ch vs 1

[...]


## Conseils supplementaires

<!-- materialized-from-db web/8e08445d2550 2026-03-28 -->
### Difference entre les plaquettes de frein standard et les Xtra . - section-1

# Difference entre les plaquettes de frein standard et les Xtra .

# Plaquettes de frein standard ou Xtra : lesquelles choisir?

![Montrer les plaquettes Xtra et les plaquettes de frein standard de Brembo](_raw/web-images/bd1f2134f6c780e6.jpg)

<!-- materialized-from-db web/aa1ee27642e9 2026-03-28 -->
### Comment faire si plaquettes et disque de frein grincent et sifflent - section-1

# Comment faire si plaquettes et disque de frein grincent et sifflent

- Skip to main content Skip to menu Skip to footer Partager sur Bruits et vibrations Quels sont les conseils de Brembo pour un remplacement dans les règles de l'art afin de prévenir tous bruits et vibrations ? Les sifflements du système de freinage, tout comme les vibrations, ne sont généralement pas dus au dysfonctionnement ou à la mauvaise qualité d'une pièce neuve. Plus souvent qu'on ne l'imagine, ces sifflements sont dus à l’usure d'autres pièces du système de freinage, qui font alors apparaître un dysfonctionnement des plaquettes ou des disques. Lors du remplacement des plaquettes et des disques, il est recommandé de ne pas se limiter à leur simple substitution, mais d'effectuer une vérification approfondie et un entretien complet de l'ensemble du système de freinage. Il est généralement conseillé d'exécuter les opérations suivantes : En cas de remplacement des plaquettes , vérifier l'état d'usure du disque.

- En cas de remplacement des disques , toujours remplacer les plaquettes.

- Nettoyer les surfaces d'accouplement du disque et du moyeu de roue (des saletés ou de la rouille)

- S’il y a des dépôts de matière ou de saleté (disque usagé), nettoyer également la surface de la bande de freinage.

- Contrôler l’oscillation du disque monté sur le moyeu de roue. Normalement, elle ne doit pas excéder 0,10 mm. En cas de problème, vérifier l'oscillation du moyeu de roue sans le disque, qui ne doit pas excéder 0,050 mm.

![Lubrifiant Brembo B-Quiet pour systèmes de freinage](_raw/web-images/057d50d39bbd8d69.jpg)

- Lorsque l'on remplace des plaquettes équipées d'une cale antibruit amovible (shim), attention à la remonter correctement. Ne pas réutiliser la cale antibruit usagée.

- Contrôler que les pistons, les joints, la coiffe de protection contre la poussière et les éléments coulissants de l'étrier ne sont pas détériorés ou corrodés, et qu'ils sont en mesure de coulisser. Utiliser de la graisse spéciale appropriée à chacune des pièces et n'attaquant pas les composants en caoutchouc. Remplacer toutes les pièces détériorées.

- Nettoyer et appliquer une graisse antibruit sur les surfaces de contact entre l'étrier et les plaquettes.

- Inspecter, nettoyer ou remplacer à neuf les ressorts de l'étrier s'ils s'ont vieux et usés.

- Vérifier le bon positionnement des ressorts .

- Contrôler le niveau du liquide de frein , qui doit se trouver entre les points min et max. Le liquide de frein doit être vidangé tous les deux ans ou selon les prescriptions du constructeur.

- Serrer les vis de la roue avec la séquence appropriée à l'aide d'une clé dynamométrique au couple de serrage prescrit .

- Effectuer un test sur route , en s'assurant du bon fonctionnement du système et de l'absence de vibrations et de bruits. Il s'avère fondamental de suggérer au conducteur de respecter un rodage de 300 km environ , au cours duquel les freinages brusques et une utilisation intensive des freins devront être évités, afin de permettre l'alignement optimal des disques et des plaquettes.

<!-- materialized-from-db web/3cb342907fc5 2026-03-28 -->
### Instructions pour remplacer... - Montage auto - section-1

# Instructions pour remplacer... - Montage auto

- Skip to main content Skip to menu Skip to footer Partager sur Instructions pour remplacer les maîtres-cylindres de frein ou les cylindres des maîtres-cylindres de frein Nous vous conseillons de lire et de suivre attentivement les instructions fournies. Vous trouverez les mêmes instructions dans l’emballage des maîtres-cylindres. N’oubliez pas de les conserver pendant toute la durée de vie du produit. En cas de passage de propriété, elles devront être remises au nouveau propriétaire du véhicule. Indications générales 1. Utiliser uniquement du liquide de frein DOT3 ou DOT4, à l’exception des véhicules qui requièrent du liquide de frein DOTS (à base de silicium). 2. Le liquide de frein doit être complètement remplacé après que le réservoir a été soigneusement lavé avec de l'alcool dénaturé. 3. À cause de la nature technique du produit, les maîtres-cylindres de frein doivent être remplacés par un technicien qualifié et, en cas de réclamation, il faudra le démontrer à l’aide d'une facture. Procédure de remplacement 1. Si le cylindre est équipé de vis de purge, brancher la vis de purge du cylindre à un tuyau en caoutchouc et placer l'extrémité libre du tuyau dans un récipient transparent. 2. Déposer les couvertures, supports, branchements électriques ou autres pièces éventuelles, qui gêneront la dépose du cylindre une fois desserré. 3. Desserrer légèrement les vis des tuyaux en retenant les tuyaux de sortie. 4. Déposer les vis ou les boulons qui retiennent le cylindre sur le servofrein ou sur le pare-feu. 5. Desserrer complètement les vis du tuyau de sortie et éloigner les tuyaux du cylindre, en faisant attention à ne pas les plier ni les déformer. Placer un chiffon sous le cylindre pour capturer la sortie de liquide et déposer le cylindre. 6. Si le liquide de frein se renverse sur la peinture, laver immédiatement avec de l'eau. Procédure de montage 1. Retirer les capuchons de protection du nouveau cylindre. 2. Contrôler que le joint de sortie de l’unité servo, si présente, est monté correctement et est en bon état. 3. Placer le cylindre (si possible, avec le réservoir déjà inséré) et contrôler attentivement que la tige de poussée du servo soit positionnée correctement ou que la tige de poussée reliée à la pédale de frein puisse se déplacer librement. 4. Remettre en place les boulons ou les vis de montage du cylindre, en les remplaçant s’ils sont endommagés. Le couple de serrage des boulons doit correspondre à celui recommandé par le constructeur du véhicule. 5. Brancher les connecteurs du tuyau de frein, en veillant à ce que le filetage sur les connecteurs du tuyau et le cylindre correspondent. Serrer les connecteurs selon les couples de serrage recommandé par le constructeur du véhicule. 6. Monter le réservoir et remplir avec le liquide de frein comme spécifié par le constructeur du véhicule. 7. Si le système ABS est installé, suivre scrupuleusement toutes les instructions du constructeur du véhicule. 8. Purger le système de freinage en suivant les instructions du constructeur du véhicule. 9. Vérifier la présence de fuites sur le système de freinage. 10. Contrôler le niveau du liquide de frein. 11. Effectuer un essai sur route. Informations générales et de sécurité Le produit Brembo a été conçu pour respecter les meilleurs standards de sécurité . Les Produits ne doivent pas être destinés à une utilisation différente de celle pour laquelle ils ont été conçus et fabriqués. L’ utilisation à d’autres fins , la modification ou la manipulation du produit risquent d’ altérer son fonctionnement et de compromettre sa sécurité . Toute modification éventuelle ou toute utilisation impropre rendent nulles les Limitations de garantie et peuvent rendre la personne utilisant le Produit dans ces conditions responsable quant aux dommages physiques ou matériels éventuellement causés à des tiers. Dans ces instructions, lorsqu’il est indiqué « DANGER! », cela signifie que le non-respect de la procédure indiquée a de fortes probabilités de provoquer de graves dommages physiques ou même la mort . La mention « ATTENTION! » indique une procédure dont le non-respect peut provoquer des dommages physiques, alors que la mention « AVERTISSEMENT! » indique une procédure dont le non-respect peut provoquer des dommages au véhicule. DANGER! Avant de commencer la procédure de remplacement, s’assurer que la pièce de rechange est adaptée à la marque et au modèle du véhicule. Le Produit revêt une importance fondamentale pour la sécurité du véhicule sur lequel il est installé et il doit, donc, être installé par du personnel qualifié ayant reçu une formation adéquate ou possédant suffisamment d’expérience dans l’installation et dans l’utilisation prévue du Produit. L’installateur doit avoir à sa disposition l’ outillage adéquat à l’installation et posséder des connaissances et une expérience appropriées pour s’occuper de l’entretien du véhicule. Une installation inadéquate ou erronée, due au non-respect de ces instructions ou autres, rendra nulles les Limitations de garantie et pourrait rendre l’installateur responsable quant aux dommages physiques ou matériels éventuellement provoqués. Il est fondamental de r emplacer les disques de frein pour chaque essieu , en les prélevant de leur emballage. À chaque remplacement des disques, remplacer aussi leurs plaquettes. Éviter le contact de graisse et autres lubrifiants avec les surfaces de freinage du disque et des plaquettes parce que cela risque de rendre le système de freinage inefficace. Brembo décline toute responsabilité en cas de dommage matériel ou physique provoqué à ou par une personne conduisant un véhicule sur lequel le produit aurait été installé de façon inappropriée. ATTENTION! Les pièces remplacées doivent être éliminées selon les dispositions prescrites par la loi. Il est important d’éviter de frapper violemment ou d’endommager le Produit et ses composants, parce que cela risquerait de réduire son efficacité et de provoquer des dysfonctionnements. Si nécessaire, remplacer les composants endommagés. Pour éviter tout dommage physique, nous conseillons de: Toujours porter des gants lors de l’opération de démontage et de remontage des composants présentant des arêtes coupantes.

![Approfondissements](_raw/web-images/2d2507a39e7ef6eb.jpg)

![Comment choisir le bon produit](_raw/web-images/554e6f769f52f78a.jpg)

![Montage auto](_raw/web-images/d8bc5a5c2c667779.jpg)

![Montage moto](_raw/web-images/8f8c2ca53665bfa9.jpg)

![Entretien](_raw/web-images/e936dadf5dced240.jpg)

- Éviter le contact direct de la peau avec le matériau de friction des plaquettes et mâchoires parce que cela risque de provoquer des abrasions.

![Service après-vente](_raw/web-images/c8ff08f5cb503a6a.jpg)

![Limites de garantie](_raw/web-images/3f780074f3f64f27.jpg)

![Contacter le support Brembo](_raw/web-images/1e8d4f4c405ed310.webp)

![WeChat](_raw/web-images/dec8ad591b7cebf6.jpg)

<!-- materialized-from-db web/e598f5f6d678 2026-03-28 -->
### Instructions pour remplacer le... - Montage auto - section-1

# Instructions pour remplacer le... - Montage auto

- Skip to main content Skip to menu Skip to footer Partager sur Instructions pour remplacer le cylindre émetteur d'embrayage et le maître-cylindre Nous vous conseillons de lire et de suivre attentivement les instructions fournies. Vous trouverez les mêmes instructions dans l’emballage des maîtres-cylindres. N’oubliez pas de les conserver pendant toute la durée de vie du produit. En cas de passage de propriété, elles devront être remises au nouveau propriétaire du véhicule. Indications générales 1. Utiliser le liquide de frein recommandé par le constructeur. 2. Le liquide de frein doit être complètement remplacé après que le réservoir a été soigneusement lavé avec de l'alcool isopropylique ou dénaturé. 3. À cause de la nature technique du produit, les cylindres émetteurs d'embrayage et le maître-cylindre doivent être remplacés par un technicien qualifié et, en cas de réclamation, il faudra le démontrer à l’aide d'une facture. 4. De nombreux véhicules plus récents sont équipés d’un cylindre esclave concentrique qui est monté à l'intérieur du logement de la cloche de boîte de vitesses. Afin de remplacer cette unité, la boîte de vitesses doit être déposée. 5. Certains de ces cylindres esclaves concentriques ont un tuyau d’alimentation et un tuyau de purge et purger ces systèmes est normalement simple. D’autres ont un seul tuyau d'alimentation avec des branchements de tuyaux extérieurs où le système est purgé. Ceux-ci peuvent être difficiles à purger, nous vous conseillons de suivre attentivement les procédures du fabricant. 6. Sur certains des nouveaux systèmes, le tuyau qui relie le cylindre émetteur d’embrayage au maître-cylindre est maintenu en place dans les cylindres à l’aide d’un clip et il est scellé avec un petit joint torique. Veiller à ce que ces tuyaux soient correctement montés pour éviter les fuites. 7. À présent, sur certains véhicules, les cylindres émetteurs d’embrayage sont montés à l’intérieur du véhicule et il est important de suivre les procédures correctes pour les déposer parce qu’il pourrait être nécessaire de déposer ou de desserrer des éléments critiques comme la colonne de direction. Procédure de remplacement 1. Soulever le véhicule et le soutenir en utilisant des supports spécifiques. 2. Déposer la moulure du compartiment de pieds en suivant les lignes directrices du constructeur du véhicule. 3. Débrancher le tuyau du cylindre, sceller le trou avec un bouchon en caoutchouc pour éviter que le fluide ne sorte. 4. Déposer le maître-cylindre ou le cylindre émetteur d'embrayage en suivant les lignes directrices du constructeur du véhicule. 5. Faire attention au diamètre/dimension du piston lors du remplacement du cylindre. Procédure de montage 1. Remplacer en même temps le cylindre émetteur d'embrayage et le maître-cylindre. 2. Installer les cylindres conformément aux instructions du constructeur du véhicule. 3. S’assurer que le maître-cylindre d’embrayage est parfaitement aligné et sûr pour empêcher de pousser la tige de poussée dans le cylindre coudé. 4. Brancher le tuyau. 5. Serrer les vis et les écrous à un couple approprié. 6. Vidanger le liquide de frein. 7. Purger l'embrayage. 8. Actionner plusieurs fois la pédale d'embrayage. 9. Vérifier le niveau du liquide de frein et si nécessaire, faire l’appoint, puis fermer le bouchon. 10. Vérifier s’il y a des fuites dans le système. 11. Contrôler la position de la pédale et la régler si nécessaire. 12. Assembler à nouveau la moulure du compartiment de pieds en suivant les lignes directrices du constructeur du véhicule. 13. Effectuer un essai sur route et contrôler la fonction de frein et d’embrayage. Informations générales et de sécurité Le produit Brembo a été conçu pour respecter les meilleurs standards de sécurité. Les Produits ne doivent pas être destinés à une utilisation différente de celle pour laquelle ils ont été conçus et fabriqués. L’utilisation à d’autres fins, la modification ou la manipulation du produit risquent d’altérer son fonctionnement et de compromettre sa sécurité. Toute modification éventuelle ou toute utilisation impropre rendent nulles les Limitations de garantie et peuvent rendre la personne utilisant le Produit dans ces conditions responsable quant aux dommages physiques ou matériels éventuellement causés à des tiers. Dans ces instructions, lorsqu’il est indiqué « DANGER! », cela signifie que le non-respect de la procédure indiquée a de fortes probabilités de provoquer de graves dommages physiques ou même la mort. La mention « ATTENTION! » indique une procédure dont le non-respect peut provoquer des dommages physiques , alors que la mention « AVERTISSEMENT! » indique une procédure dont le non-

[...]
