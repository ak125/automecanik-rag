---
category: electrique
slug: alternateur
title: Alternateur
pg_id: 4
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
  role: Recharger la batterie et alimenter les equipements electriques du vehicule moteur tournant
  must_be_true:
  - recharger
  - alimenter
  - fournir du courant
  must_not_contain:
  - demarrage
  - demarreur
  - lancer le moteur
  - rotation initiale
  - neiman
  - universel
  - tous modèles
  - adaptable tous
  confusion_with:
  - term: batterie
    difference: Alternateur recharge la batterie, si batterie HS l'alternateur ne peut compenser
  - term: demarreur
    difference: Alternateur = recharge batterie (moteur tournant), Démarreur = lance le moteur (au démarrage)
  related_parts:
  - batterie
  - demarreur
  - bougie-d-allumage
  - bobine-d-allumage
  - poulie-d-alternateur
selection:
  criteria:
  - Marque de votre véhicule
  - Modele de votre véhicule
  - Motorisation de votre véhicule
  - Annee de votre véhicule
  anti_mistakes:
  - ❌ "zéro panne électrique"
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  cost_range:
    min: 61
    max: 441
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  brands:
    premium:
    - Bosch
    - Valeo
    - Denso
    standard:
    - Hella
    - NGK
    - Delphi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Voyant batterie allume moteur tournant
    severity: confort
  - id: S2
    label: Batterie qui se decharge malgre les trajets
    severity: confort
  - id: S3
    label: Phares qui faiblissent ou clignotent
    severity: confort
  - id: S4
    label: Sifflement de la courroie d accessoire
    severity: confort
  - id: S5
    label: Odeur de courroie brulee ou d electrique
    severity: confort
  - id: S6
    label: Plus de 150 000 km ou tension de charge basse
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - remplacement preventif recommande
  depose_steps: []
  quick_checks:
  - Voyant batterie allume moteur tournant ?
  - 'Observer : batterie qui se decharge malgre les trajets ?'
  - 'Observer : phares qui faiblissent ou clignotent ?'
  - 'Observer : sifflement de la courroie d accessoire ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant batterie allume moteur tournant
  - Batterie qui se decharge malgre les trajets
  - Phares qui faiblissent ou clignotent
  - Sifflement de la courroie d accessoire
  - Odeur de courroie brulee ou d electrique
  - Plus de 150 000 km ou tension de charge basse
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '4'
  intro_title: A quoi sert Alternateur ?
  risk_title: Pourquoi remplacer Alternateur a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  - ❌ "zéro panne électrique"
  - ❌ "homologué CT"
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
  - question: Alternateur OE, OES ou échange standard ?
    answer: 'Les alternateurs OES (Bosch, Valeo, Denso) sont de qualité première monte. L''échange standard est économique
      : alternateur reconditionné avec garantie équivalente.'
  - question: Comment savoir si mon alternateur est HS ?
    answer: Voyant batterie allumé moteur tournant, batterie qui se décharge en roulant, phares qui faiblissent, équipements
      électriques défaillants.
  - question: Tous les combien changer l'alternateur ?
    answer: Pas de périodicité fixe. Durée de vie 150 000 à 300 000 km. Vérifier la charge régulièrement avec un multimètre
      (13,5 à 14,5V moteur tournant).
  - question: Peut-on changer l'alternateur soi-même ?
    answer: Oui si accessible. Débrancher batterie, détendre courroie, dévisser fixations, débrancher connecteurs. Compter
      1h à 3h selon véhicule.
  - question: Quelle erreur éviter avec l'alternateur ?
    answer: Ne pas inverser les polarités. Vérifier la tension de la courroie neuve. Contrôler aussi la poulie d'alternateur
      (débrayable sur certains modèles).
  quality:
    score: 76
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - adaptable tous
  requires_vehicle: true
doc_id: 5be21667-6567-5e22-96be-c8b3431c1e69
content_hash: sha256:be6aff0b83925e88
lang: fr
variants:
- name: Piece neuve OE/OES
  aliases:
  - neuf
  - OE
  - OES
  functional_differences:
  - Garantie constructeur ou equipementier
  - Calibration d usine
- name: Piece echange standard
  aliases:
  - echange standard
  - reconditionne
  functional_differences:
  - Moins cher
  - Piece d origine reconditionnee
location_on_vehicle:
  area: Compartiment moteur (alternateur, demarreur) ou peripherie
  access: Par le dessus (capot) ou par le dessous selon modele
  adjacent_parts:
  - faisceau electrique
  - batterie
  - fusibles
installation:
  difficulty: facile a moyen
  time: 15min a 1h
  tools:
  - cle a douille
  - multimetre
  - tournevis
  prerequisite: Debrancher la batterie avant intervention
phase5_enrichment:
  _source: automotive.hutchinson.com + boschaftermarket.com + denso-am.eu + fr.wikipedia.org + gpa26.com + profauto.fr + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 12
  _has_tech_data: true
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'inductif'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_iso_9981: 'ISO 9981'
    val_000_km: '000 km'
    val_10_a: '10 a'
    val_12_v: '12 V'
    val_135__c: '135 °C'
    val_14_v: '14 V'
    val_24_v: '24 V'
    val_28_v: '28 V'
    val_30_a: '30 a'
    val_4_a: '4 a'
    val_45_a: '45 A'
    val_50_hz: '50 Hz'
    val_503_a: '503 a'
    val_59_a: '59 a'
    val_6_a: '6 a'
    val_70_a: '70 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'L''alternateur est entraîné par la courroie accessoire à partir de la poulie de vilebrequin, il ne fonctionne que quand
    le moteur tourne. L''alternateur produit un courant alternatif (ampères) qui alimente les différents organes en courant
    continu (volts). Le courant est donc d''abord redressé, puis régulé pour ne pas dépasser une certaine valeur. Car une
    tension au-delà de cette valeur serait préjudiciable à l''électronique embarqué (qui peut endommager les composants électrique)
    et à la batterie (qui bout et finit par se mettre en court-circuit). En savoir plus : alternateur — définition et rôle
    mécanique 🚨 Bruit de alternateur : que faire ?'
  S2: 'Ne pas attendre la panne complete pour intervenir. Symptômes d''usure : - Voyant batterie allume moteur tournant -
    Batterie qui se decharge malgre les trajets - Phares qui faiblissent ou clignotent - Sifflement de la courroie d accessoire
    - Odeur de courroie brulee ou d electrique - Plus de 150 000 km ou tension de charge basse'
  S2_DIAG: 'SymptômeCause probableActionVoyant batterie allume moteur tournantlocaliser source et verifier usure mecaniqueVoyant
    batterie allume moteur tournant ?Batterie qui se decharge malgre les trajetslecture codes defaut obd et diagnostic electroniqueObserver
    : batterie qui se decharge malgre les trajets ?Phares qui faiblissent ou clignotentremplacement preventif recommandeObserver
    : phares qui faiblissent ou clignotent ?Sifflement de la courroie d accessoirelocaliser source et verifier usure mecaniqueObserver
    : sifflement de la courroie d accessoire ?Odeur de courroie brulee ou d electriquelocaliser source et verifier usure mecaniqueVoyant
    batterie allume moteur tournant ?Plus de 150 000 km ou tension de charge basselocaliser source et verifier usure mecaniqueVoyant
    batterie allume moteur tournant ?'
  S3: 'Pour choisir le bon alternateur pour votre vehicule : - Amperage : verifier l''amperage d''origine (ex: 90A, 120A,
    150A) — un alternateur sous-dimensionne ne supporte pas les equipements electriques du vehicule- Voltage : 12V pour vehicules
    particuliers, 24V pour utilitaires — ne pas interchanger- Type de fixation : verifier le nombre de points de fixation
    et la position des pattes par rapport au bloc moteur- Poulie : poulie libre (overrunning alternator pulley) ou poulie
    fixe — les vehicules recents utilisent des poulies libres pour reduire les vibrations- Connectique : verifier le type
    de branchement (nombre de bornes, presence du connecteur regulateur)'
  S4_DEPOSE: 1. Débranchez la batterie (borne négative en premier). 2. Repérez le cheminement de la courroie d'accessoires
    et desserrez le galet tendeur. 3. Retirez la courroie d'accessoires. 4. Débranchez les connecteurs électriques de l'alternateur
    (fil d'excitation + borne B+). 5. Dévissez les vis de fixation de l'alternateur (généralement 2 ou 3 vis). 6. Retirez
    l'alternateur par le haut ou par le bas selon l'accessibilité.
  S4_REPOSE: '- Contrôler le nouveau alternateur avec celui monté sur le véhicule s''assurer que le voltage et l''ampérage
    soient identique. - Contrôlez l''état de tousles éléments entraînés par la courroie d''accessoires (compresseur de climatisation
    , pompe de direction assistée ). - Contrôlez l''état de la courroied''accessoires, du galet tendeur et lesremplacées si
    nécessaire. - Remontez l''alternateur. - Serrez les vis de fixationde l''alternateur. - Branchez le connecteur del''alternateur.
    - Remontez la courroie d''accessoires. - Rebranchez la batterie. - Contrôlez le bonfonctionnement de l''alternateur et
    tous les composants électriques. ✅ Après remontage, vérifiez les spécifications dans la fiche technique Alternateur.'
  S5: 'Erreurs frequentes avec l''alternateur : - Ne pas tester la batterie avant de remplacer l''alternateur — une batterie
    en fin de vie mime les symptomes d''un alternateur defaillant (voyant batterie, demarrage lent)- Oublier de verifier la
    tension de la courroie d''accessoire — une courroie detendue fait patiner l''alternateur et reduit la charge- Inverser
    les bornes lors du branchement — destruction immediate du pont de diodes de l''alternateur- Ne pas debrancher la batterie
    avant intervention — risque de court-circuit sur la borne B+ sous tension permanente- Remonter un alternateur avec un
    amperage inferieur a l''origine — le vehicule equipe de nombreux accessoires electriques decharge la batterie progressivement-
    Ignorer un bruit de roulement cote alternateur — signe de roulement interne use, la panne complete est imminente'
  S6: 'Verifications apres remplacement de l''alternateur : - Tension batterie moteur tournant : mesurer au multimetre — doit
    etre entre 13,5 V et 14,5 V. En dessous = alternateur ne charge pas, au-dessus = regulateur defaillant- Tension batterie
    moteur arrete : doit etre a 12,6 V minimum. En dessous = batterie defaillante, pas l''alternateur- Courroie d''accessoire
    : verifier la tension et l''alignement — une courroie mal tendue fait siffler et reduit la charge- Voyant batterie : doit
    s''eteindre moteur tournant. S''il reste allume = verifier le cablage du connecteur regulateur- Test en charge : allumer
    phares + ventilation + lunette arriere — la tension ne doit pas descendre sous 13,2 V'
  S_GARAGE: 'Nous vous recommandons de confier cette intervention à un professionnel : - Plusieurs causes possibles de défaillance
    (3 identifiées) nécessitent un diagnostic professionnel Un garagiste qualifié dispose de l''outillage et de l''expérience
    nécessaires pour effectuer cette opération en toute sécurité.'
  S7: '- courroie d accessoire - demarreur - galet enrouleur de courroie d accessoire - galet tendeur de courroie d accessoire
    - poulie d alternateur - poulie vilebrequin'
  S8: 'Alternateur OE, OES ou échange standard ?Les alternateurs OES (Bosch, Valeo, Denso) sont de qualité première monte.
    L''échange standard est économique : alternateur reconditionné avec garantie équivalente. Comment savoir si mon alternateur
    est HS ?Voyant batterie allumé moteur tournant, batterie qui se décharge en roulant, phares qui faiblissent, équipements
    électriques défaillants. Tous les combien changer l''alternateur ?Pas de périodicité fixe. Durée de vie 150 000 à 300
    000 km. Vérifier la charge régulièrement avec un multimètre (13,5 à 14,5V moteur tournant). Peut-on changer l''alternateur
    soi-même ?Oui si accessible. Débrancher batterie, détendre courroie, dévisser fixations, débrancher connecteurs. Compter
    1h à 3h selon véhicule. Quelle erreur éviter avec l''alternateur ?Ne pas inverser les polarités. Vérifier la tension de
    la courroie neuve. Contrôler aussi la poulie d''alternateur (débrayable sur certains modèles).'
  META: '{"meta_title":"Alternateur : Guide Remplacement et Conseils | AutoMecanik","meta_description":"Voyant batterie allumé
    ou batterie qui se décharge ? Découvrez quand changer l''alternateur, comment le remplacer et choisir la pièce compatible
    sur AutoMecanik."}'
---

# Alternateur - Guide Diagnostic Complet

## Fonction et Rôle

Recharger la batterie et alimenter les equipements electriques du vehicule moteur tournant

**Actions principales:** recharger, alimenter, fournir du courant, maintenir la charge, produire de lelectricite

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant batterie allume moteur tournant
- batterie qui se decharge malgre les trajets
- phares qui faiblissent ou clignotent
- sifflement de la courroie d accessoire
- odeur de courroie brulee ou d electrique
- plus de 150 000 km ou tension de charge basse

## Procédure de Diagnostic

Pour diagnostiquer un problème de alternateur:

1. **Inspection visuelle** - Examiner l'état du alternateur
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé
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

- courroie-d-accessoire
- demarreur
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- poulie-d-alternateur
- poulie-vilebrequin

## ⚠️ Ne Pas Confondre Avec

### demarreur
**Distinction:** Alternateur = recharge batterie (moteur tournant), Démarreur = lance le moteur (au démarrage)

### batterie
**Distinction:** Alternateur recharge la batterie, si batterie HS l'alternateur ne peut compenser

## Critères de Compatibilité

Pour commander le bon alternateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "zéro panne électrique"
- ❌ "homologué CT"
- ❌ "sécurité garantie"

## FAQ

**Alternateur OE, OES ou échange standard ?**
Les alternateurs OES (Bosch, Valeo, Denso) sont de qualité première monte. L'échange standard est économique : alternateur reconditionné avec garantie équivalente.

**Comment savoir si mon alternateur est HS ?**
Voyant batterie allumé moteur tournant, batterie qui se décharge en roulant, phares qui faiblissent, équipements électriques défaillants.

**Tous les combien changer l'alternateur ?**
Pas de périodicité fixe. Durée de vie 150 000 à 300 000 km. Vérifier la charge régulièrement avec un multimètre (13,5 à 14,5V moteur tournant).

**Peut-on changer l'alternateur soi-même ?**
Oui si accessible. Débrancher batterie, détendre courroie, dévisser fixations, débrancher connecteurs. Compter 1h à 3h selon véhicule.

**Quelle erreur éviter avec l'alternateur ?**
Ne pas inverser les polarités. Vérifier la tension de la courroie neuve. Contrôler aussi la poulie d'alternateur (débrayable sur certains modèles).


## References supplementaires

<!-- materialized-from-db web-catalog/a86e664db2c1 2026-03-28 -->
### Produits d’entretien – Textar Brake Technology - Formula XT

### Formula XT

Le nettoyant freins de Textar est un produit efficace pour enlever les tâches d’huile, de graisse et la saleté, sans laisser de traces.

LE NETTOYANT FREINS DE TEXTAR NETTOIE TOUT :

- Freins, embrayage et engrenages

- Démarreurs et alternateurs

- Carburateurs, pompes à injection et éléments du moteur

- Surfaces en verre ou métal avant collage

Les atouts du nettoyant freins Textar :

- N’attaque pas le polystyrène

- Sans solvant chloré

- Homologué par le ministère fédéral allemand de l’Environnement

Formula XT est disponible en :

Bombe aérosol de 500 ml . Référence Numéro: 96000100 Unité de vente (lot): 12 bombes aérosols

UTILISATION:

Pulvérisez généreusement le produit sur les parties à nettoyer. Laissez le dissolvant s’éliminer par écoulement ou évaporation. Répétez le processus sur les parties encrassées.

- Gérer les options

- Gérer les services

- Gérer {vendor_count} fournisseurs

- En savoir plus sur ces finalités

- {title}

- {title}

- {title}

- Gérer les options

- Gérer les services

- Gérer {vendor_count} fournisseurs

- En savoir plus sur ces finalités

- {title}

- {title}

- {title}

## Symptomes supplementaires

<!-- materialized-from-db diagnostic/alternateur-diagnostic-mahle.md 2026-03-28 -->
### schadensbroschuere generatoren 2020 fr final low

[[PDF_PAGE:1]]
Alternateurs
Dommages
Causes, remèdes et préventionMAHLE Aftermarket GmbH
Pragstraße 26 – 46
70376 Stuttgart, Allemagne
Téléphone : +49 711 501-0
www.mahle-aftermarket.com
www.mpulse.mahle.com
mahled-089/04.2020/FR

[[PDF_PAGE:2]]
02
03
Structure et fonctionnement
d’un alternateur 04

1 Pénétration de liquide
1.1 Pénétration de liquide dans l’alternateur 06
2 Défaut de montage
2.1 Poulie I 08
2.2 Poulie II 10
2.3 Régulateur 12
2.4 Raccordement électrique 14
3 Encrassement
3.1 Concentration d’impuretés dans l’alternateur 16

4 Mécanique
4.1 Dommages mécaniques sur l’alternateur 18
5 Fonctionnement
5.1 L’alternateur ne fonctionne pas
(diodes d’excitation défectueuses) 20
5.2 L’alternateur ne fonctionne pas
(diodes de redressement défectueuses) 22
5.3 L’alternateur ne fonctionne pas
avec raccordement pour capteur de batterie 24
5.4 L’alternateur ne fonctionne pas
au bout d’un certain kilométrage 26
6 Performance électrique
6.1 L’alternateur n’est pas performant,
le rotor émet des bruits de frottement 28
6.2 L’alternateur n’est pas performant,
le voyant de charge ne s’éteint pas 30
Glossaire 32
Notre catalogue de produits 34
Nos services d’info 35
Sommaire
MAHLE est l’un des plus importants partenaires
de développement et équipementiers de l’indus-
trie automobile. Le groupe est spécialisé dans la
fabrication de pièces et systèmes moteur.
Les ingénieurs MAHLE développent des produits
d’excellente qualité en étroite collaboration avec
les motoristes et les constructeurs automobiles
du monde entier.
Les pièces de rechange destinées au marché de l’après-vente
répondent aux mêmes exigences de qualité.
Des contrôles multiples pendant et après la fabrication garan-
tissent le niveau de qualité élevé des produits MAHLE. Si le véhi-
cule tombe malgré tout en panne, la faute est le plus souvent liée
aux pièces périphériques du moteur. Défaut de montage, erreur
d’utilisation ou emploi d’équipements inappropriés peuvent tou-
tefois également être à l’origine d’une panne.
Cette brochure décrit les dommages typiques. Elle en décrit les
causes afin d’en faciliter la recherche, et fournit des conseils
pour qu’ils ne se reproduisent pas. Cette brochure contribue à
la fiabilité et à la longévité de nos produits et, par conséquent,
à prolonger la durée de vie du moteur.
Nos experts sont néanmoins confrontés à des scénarios de
pannes complexes, dont la description dépasserait le cadre de
cette brochure. Si vous avez des doutes sur l’origine de dom-
mages affectant nos produits, nous vous proposons d’examiner
ces derniers dans nos ateliers et d’établir un rapport d’expertise.
Adressez-vous dans ce cas à notre partenaire commercial le
plus proche.
Introduction

Plus d’infos sur

[[PDF_PAGE:3]]
04
05
De très nombreuses fonctions d’un véhicule ont besoin de
courant électrique. Celui-ci est produit par l’alternateur lorsque
le moteur à combustion interne tourne ; la batterie du véhicule
stocke l’énergie et sert de tampon.
L’alternateur doit être conçu de telle sorte que tous les consom-
mateurs d’électricité du véhicule sollicités sur une longue durée
soient suffisamment alimentés. Le régime habituel du moteur
joue également un rôle.
Dans la plupart des cas, le moteur du véhicule entraîne l’alterna-
teur par le biais d’une courroie. La rotation du rotor à l’intérieur du
stator fixe crée inductivement un courant électrique. La plupart
des alternateurs sont triphasés.
Un pont de diodes ou redresseur permet de transformer le cou-
rant alternatif en courant continu. En fonction du besoin actuel en
électricité du véhicule, le régulateur fournit à la bobine d’excita-
tion du rotor le courant nécessaire. L’alimentation du rotor par le
régulateur se fait au moyen de balais de charbon montés sur les
bagues collectrices du rotor.
À cause des pertes électromagnétiques et des résistances
électriques de ses composants, l’alternateur génère également
de la chaleur en plus du courant électrique. Selon les modèles,
un ou deux ventilateurs sont montés sur l’arbre du rotor pour
assurer l’évacuation de la chaleur produite.
d’un alternateur
Exemple de schéma de raccordement Courbes caractéristiques d’un alternateur
Palier arrière
Rotor
Stator
Palier avant
9
10
11
Poulie
Rondelle entretoise
Arbre
Ventilateur
Carter
Capot de protection
1
5
2
6
3
4
12
1 2 3
4 5 4 6 7
12 11 10 9 8
Régulateur
7 Redresseur/diodes d’excitation
Régulateur/balais de charbon/
bagues collectrices
8
1000 2000 3000 4000 5000 6000 7000 8000
0
14 V 120 A
14 V 95 A
14 V 85 A
14 V 80 A
14 V 70 A
20
30
40
50
60
70
80
90
100
110
120
(A)
n/tr/min
U = const. = 13 V
Tamb. = 23 °C ± 5 °C

[[PDF_PAGE:4]]
Dépôt d’huile sur le régulateur avec abrasion gluante des charbonsÉpais dépôt d’huile sur l’alternateur
Épais dépôt d’huile sur les bagues collectrices
Épais dépôt d’huile sur l’alternateur
Dépôt d’huile sur le régulateur
Huile dans l’alternateur
06
07
1.1 Pénétration de liquide
Dans l’alternateur
Mécanique Encrassement Défaut de montage Pénétration de liquideFonctionnementPerformance électrique
-
Diagnostic :
n Dépôt d’huile autour de l’alternateur
(huiles moteur/hydraulique ou diesel)
n L’alternateur fournit peu ou pas
d’énergie
n Usure importante des balais
n Usure importante des bagues
collectrices
n Abrasion des balais sous forme
de pâte au niveau du régulateur
n Porte-balais calciné
Cause(s) :
n Pénétration de liquide dans l’alter-
nateur (huiles moteur/hydraulique
ou diesel)
n Défaut d’étanchéité sur le moteur, le
système hydraulique ou à carburant
n Contamination de l’alternateur lors
du remplacement des filtres
n Contamination lors du remplissage
d’huile dans le moteur
n Surcharge thermique de l’alternateur,
écoulement d’huile par les paliers
Remèdes/prévention :
n Remplacer l’alternateur
n Rechercher et éliminer l’origine du
défaut d’étanchéité sur le circuit
d’huile, hydraulique ou à carburant

n En cas de dépôt important de
poussière et d’impuretés, nettoyer
régulièrement l’arrivée d’air, le venti-
lateur et l’alternateur

n Les consommateurs électriques
reliés à l’alternateur doivent être
adaptés à sa performance élec-
trique. En cas de branchement
d’autres accessoires électriques,
opter éventuellement pour un
alternateur similaire plus puissant
Attention !
En cas de fuite d’huile dans le compartiment moteur, ne pas utiliser
de liquide inflammable pour nettoyer l’alternateur : risque d’incendie !

[[PDF_PAGE:5]]
Résidus de l’arbre arraché dans l’écrou Arbre de l’alternateur arraché suite à un couple de serrage trop élevé
(clé à chocs)
Filetage de l’arbre de l’alternateur fortement endommagé
Ne jamais utiliser une clé à chocs pour serrer l’écrou de la poulie.
La clé à chocs ne peut être utilisée que pour dévisser l’écrou.
Vérifier au préalable le sens de rotation !
08
09
2.1 Défaut de montage
Poulie I
-
-
n Filetage de l’arbre endommagé/
arraché

n Écrou de la poulie vissé à un couple
de serrage trop élevé (arbre trop
sollicité au niveau du filetage)
n Écrou de la poulie serré à l’aveugle
avec une clé à chocs
n Fixer l’arbre avec une clé Allen ou
à denture multiple

n Serrer l’écrou de la poulie au couple
de serrage spécifié :
M16 × 1,5 : 95 Nm +/- 5 Nm,
M27 × 1,5 : 152 Nm +/- 17,5 Nm

[[PDF_PAGE:6]]
2.2 Défaut de montage
Poulie II
Usure évidente de l’arbre au niveau du roulement à billes (l’écrou était
desserré). Le jeu étant plus important, le rotor a frotté sur le stator.
Poulie à roue libre montée sans rondelle entretoise Alternateur avec poulie à roue libre montée par le client
Usure évidente de l’arbre au niveau du palier (l’écrou était desserré)
Extrémité de l’arbre fortement usée par la poulie (l’écrou était desserré) Arbre fortement usé au niveau du roulement avant (l’écrou était desserré)
Extrémité de l’arbre fortement usée par la poulie (l’écrou était desserré)Traces de frottement du rotor sur le stator en raison de l’usure de l’arbre
-
-
n L’alternateur ne fournit plus d’énergie
au bout d’un certain kilométrage
n Bruits dans l’alternateur
n Voyant de charge allumé
n Poulie desserrée
n Traces d’usure sur la poulie
n Filetage de l’arbre fortement usé/limé
n Jeu radial évident du rotor sur le côté
de la poulie
n Arbre fortement usé au niveau du
roulement avant
n Le rotor a touché le stator
n Traces de frottement sur le rotor
n Les tôles du stator sont en partie
décalées dans le sens circonférentiel,
ce qui a provoqué un court-circuit
dans les spires
n L’écrou n’était pas assez serré sur
l’arbre. Par conséquent, la courroie
n’était pas tendue et s’est enroulée
sur l’arbre
n Le mécanicien a vissé la poulie à
roue libre sur l’arbre sans installer les
rondelles entretoises nécessaires.
De ce fait, la bague intérieure du palier
à roulement n’était pas suffisamment
fixée sur l’arbre. L’arbre a tourné dans
la bague de roulement intérieure,
ce qui l’a usé. Le jeu entre la bague
de roulement et l’arbre ayant ainsi
augmenté, le rotor n’a pas été guidé
correctement et a frotté contre le
stator. Les tôles du stator se sont
décalées l’une vers l’autre, provo-
quant des courts-circuits dans les
spires
n Lors du montage d’une poulie,
installer des rondelles entretoises
adaptées
n Visser l’écrou de la poulie au couple

[[PDF_PAGE:7]]
13
2.3 Défaut de montage
Bagues collectrices endommagées par des charbons cassés
Rupture des charbons lors du démontage/montage du régulateurRupture des charbons lors du démontage/montage du régulateur
-
-
n Directement ou peu après le montage
d’un régulateur neuf : le voyant de
charge s’allume (pas d’énergie)
n Directement après le montage d’un
régulateur neuf : l’alternateur fournit
peu d’énergie
n Structure de rupture grossière d’un
balai (fracture nette), éventuellement lé-
gères traces de frottement de la bague
collectrice au milieu du balai cassé
n Stries et traces de brûlure sur une
bague collectrice
n Au cours du montage ou démontage
du régulateur : balai coincé et cassé
n Le balai cassé ne transmet qu’un faible
courant d’excitation : l’alternateur
produit peu ou pas d’énergie
n La surface de contact du balai cassé
est trop réduite et la force d’appui
trop faible : davantage d’étincelles
sur la bague collectrice concernée

n Lors du démontage ou montage du
régulateur, pousser les charbons
contre les ressorts pour éviter qu’ils
ne se coincent
n Si les charbons se coincent, ne pas
forcer

[[PDF_PAGE:8]]
14
15
2.4 Défaut de montage
Raccordement électrique
Écrou de la borne B+ mal serré
Borne B+ brûlée
Cosse avec traces de brûlureTraces de brûlure sur les rondelles et l’écrou
-
-
n La batterie du véhicule n’est pas
suffisamment chargée
n Écrou de la borne B+ desserré
n Boulon de raccordement B+
décoloré par la chaleur
partiellement brûlé
n Écrou et rondelles présentent des
traces de brûlure et de fusion
n Écrou de la borne B+ insuffisamment
serré
n Câble de raccordement fixé de
manière non conforme aux consignes
du fabricant. Un câble qui bouge libre-
ment peut provoquer le desserrage
de l’écrou

n Un serrage incorrect ou insuffisant
de l’écrou entraîne un échauffement
des pièces suite aux résistances de
contact et la formation d’arcs élec-
triques suite aux courants de charge
n Vérifier si le câble de raccordement
et la cosse sont endommagés et
les remplacer si nécessaire
n Fixer le câble de raccordement
conformément aux consignes du
fabricant afin d’éviter tout mouve-
ment libre
n Visser l’écrou au couple de serrage
spécifié :
M5 : 3,3 Nm +/- 0,6 Nm
M6 : 5,1 Nm +/- 0,9 Nm
M8 : 11 Nm +/- 2 Nm
M10 : 11,8 Nm +/- 2,3 Nm
(agrandie)

[[PDF_PAGE:9]]
16
17
3.1 Encrassement
Concentration d’impuretés dans l’alternateur
Alternateur fortement encrassé Saleté sur les spires du stator
Redresseur et diodes d’excitation fortement encrassés Décoloration et stries dues à la saleté sur les bagues collectrices de
l’alternateur
Fort encrassement du régulateur. Charbons surchauffés et bloqués dans guidage fondu.
-
-
n L’alternateur fait du bruit
n Le roulement à billes est rugueux
n L’isolant des bobinages en cuivre
et des tuyaux de l’alternateur est
n Les balais de charbon et les bagues
collectrices sont très usés par rapport
au kilométrage

n L’extérieur de l’alternateur est
fortement encrassé
n L’intérieur de l’alternateur est
également fortement encrassé
et encroûté
n Les diodes sont endommagées
n Épaisse couche de poussière et d’im-
puretés provenant de l’environnement
n Encrassement de l’alternateur par des
liquides (huiles, carburant, liquide de
refroidissement, fuite de graisse des
paliers), ce qui a favorisé l’agglutina-
tion de poussière
n L’agglutination de poussière et de
saleté a empêché une évacuation
complète de la chaleur, d’où la sur-
charge thermique et la détérioration
des composants de l’alternateur
n Surcharge thermique du roulement
à billes : réduction de la capacité
de charge du film lubrifiant. La fuite
de graisse entraîne la détériora-
tion des chemins de roulement

n En cas de fort encrassement au cours
du fonctionnement, nettoyer soigneu-
sement l’alternateur et le comparti-
ment moteur à brefs intervalles
n En cas de contamination par des
liquides, rechercher l’origine et
remédier aux défauts d’étanchéité

[[PDF_PAGE:10]]
18
19
4.1 Mécanique
Dommages mécaniques sur l’alternateur
Capot du carter de l’alternateur cassé Dommage mécanique sur la diode de puissance et platine plastique
Lamelles en tôle décalées à l’intérieur du stator Déformation (défaut) du stator (suite à une chute de l’alternateur par ex.) Carter de régulateur déformé et fendu
(surcharge mécanique)
Borne cassée du condensateur (suite à une chute
de l’alternateur par ex.)
Carter fendu suite à surcharge mécanique
-
-
n L’alternateur ne fonctionne pas
n Capot plastique endommagé
n Raccordements électriques déformés
n Raccordements électriques arrachés
n Composants défectueux à l’intérieur
du capot plastique endommagé
d’énergie ou de tension
n Carter de régulateur cassé
n Bruits de frottement lorsqu’on
tourne la poulie manuellement
n L’alternateur est grip

[...]
