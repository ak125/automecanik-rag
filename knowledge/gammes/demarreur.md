---
category: electrique
slug: demarreur
title: Démarreur
pg_id: 2
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
  role: Appliquer une rotation initiale au moteur pour declencher le demarrage
  must_be_true:
  - lancer le moteur
  - entrainer
  - demarrer
  must_not_contain:
  - charge
  - recharge
  - alimentation electrique
  - alternateur
  - universel
  - tous modèles
  - adaptable tous
  confusion_with:
  - term: alternateur
    difference: Démarreur = lance le moteur (au démarrage), Alternateur = recharge batterie (moteur tournant)
  - term: batterie
    difference: Batterie faible peut simuler un démarreur HS - toujours tester la batterie d'abord
  related_parts:
  - alternateur
  - batterie
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
  - ❌ "démarrage garanti"
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  cost_range:
    min: 85
    max: 334
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
    label: Claquement contact demarrage solenoide
    severity: confort
  - id: S2
    label: Demarreur tourne mais moteur lance
    severity: confort
  - id: S3
    label: Aucune reaction au contact moteur electrique hs
    severity: immobilisation
  - id: S4
    label: Grincement ou bruit anormal au demarrage
    severity: confort
  - id: S5
    label: Odeur de brule electrique au demarrage
    severity: confort
  - id: S6
    label: Plus demarrages difficiles recurrents
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - 'vehicule immobilise ou symptome critique : verification urgente piece et alimentation'
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  quick_checks:
  - 'Observer : claquement contact demarrage solenoide ?'
  - 'Observer : demarreur tourne mais moteur lance ?'
  - 'Observer : aucune reaction au contact moteur electrique hs ?'
  - 'Observer : grincement ou bruit anormal au demarrage ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Claquement contact demarrage solenoide
  - Demarreur tourne mais moteur lance
  - Aucune reaction au contact moteur electrique hs
  - Grincement ou bruit anormal au demarrage
  - Odeur de brule electrique au demarrage
  - Plus demarrages difficiles recurrents
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '2'
  intro_title: A quoi sert Démarreur ?
  risk_title: Pourquoi remplacer Démarreur a temps ?
  risk_explanation: '**Pièce HS** - Le démarreur peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le démarreur peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  - ❌ "démarrage garanti"
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
  - question: Démarreur OE, OES ou échange standard ?
    answer: 'Les démarreurs OES (Bosch, Valeo, Denso) sont de qualité première monte. L''échange standard est économique et
      fiable : pièce reconditionnée avec garantie.'
  - question: Comment savoir si mon démarreur est HS ?
    answer: Claquement sans démarrage (solénoïde), démarreur qui tourne dans le vide (lanceur usé), pas de réaction au contact
      (moteur électrique grillé).
  - question: Tous les combien changer le démarreur ?
    answer: Pas de périodicité fixe. Durée de vie 150 000 à 250 000 km selon utilisation. Les démarrages fréquents (ville)
      usent plus vite.
  - question: Peut-on changer le démarreur soi-même ?
    answer: Oui, opération accessible. Débrancher la batterie, dévisser les 2-3 vis de fixation, débrancher les fils. Compter
      1h à 2h selon l'accès.
  - question: Quelle erreur éviter avec le démarreur ?
    answer: Ne pas insister si le démarreur ne répond pas (risque de griller le solénoïde). Vérifier la batterie et les câbles
      avant de changer le démarreur.
  quality:
    score: 60
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - adaptable tous
  requires_vehicle: true
doc_id: 49ecb965-df48-5669-a85d-22d90aaec1c3
content_hash: sha256:8da30191f5b1f212
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
  _source: delphiautoparts.com + mann-filter.com + textar.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 8
  types_variants:
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_2_a: '2 a'
    val_31_a: '31 a'
    val_59_a: '59 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    - Niveau de difficulté : facile à intermédiaire (accessibilité variable
    selon véhicule). - Temps estimé : 30 min à 2 h. - Outils : clés à
    œil/douilles 10-13 mm, rallonge + cliquet, lampe. - Précaution : débranchez
    impérativement la borne négative de la batterie — le câble B+ du démarreur
    est sous tension permanente. - Accès : par le dessus (véhicules compacts) ou
    par le dessous (cric + chandelles nécessaires).
  S2: >-
    Ne pas attendre la panne complete pour intervenir. Symptômes d'usure : -
    Claquement contact demarrage solenoide - Demarreur tourne mais moteur lance
    - Aucune reaction au contact moteur electrique hs - Grincement ou bruit
    anormal au demarrage - Odeur de brule electrique au demarrage - Plus
    demarrages difficiles recurrents
  S2_DIAG: >-
    SymptômeCause probableActionClaquement contact demarrage
    solenoideverification urgente piece et alimentationObserver : claquement
    contact demarrage solenoide ?Demarreur tourne mais moteur lancelocaliser
    source et verifier usure mecaniqueObserver : demarreur tourne mais moteur
    lance ?Aucune reaction au contact moteur electrique hsvehicule immobilise ou
    symptome critique : verification urgente piece et alimentationObserver :
    aucune reaction au contact moteur electrique hs ?Grincement ou bruit anormal
    au demarragebruit anormal detecte : localiser source et verifier usure
    mecaniqueObserver : grincement ou bruit anormal au demarrage ?Odeur de brule
    electrique au demarrageverification urgente piece et alimentationObserver :
    claquement contact demarrage solenoide ?Plus demarrages difficiles
    recurrentsverification urgente piece et alimentationObserver : claquement
    contact demarrage solenoide ?
  S3: >-
    Pour choisir le bon demarreur pour votre vehicule : - Puissance (kW) : doit
    correspondre a la cylindree et au type de moteur — un demarreur sous-
    puissant ne lancera pas le moteur, surtout a froid- Nombre de dents du
    pignon lanceur : doit correspondre exactement a la couronne du volant moteur
    (9, 10, 11 ou 13 dents selon vehicule)- Sens de rotation : horaire ou anti-
    horaire selon le moteur — un demarreur inversé tourne dans le vide- Fixation
    : verifier le nombre de vis (2 ou 3), le diametre et l'entraxe —
    l'accessibilite varie fortement d'un vehicule a l'autre- Connectique : borne
    B+ (gros cable batterie) et connecteur du solenoide doivent correspondre au
    faisceau existant
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Démarreur pour connaître
    les spécifications. - Démonterun démarreur. - Débranchez la batterie. -
    Levez et calez le véhiculesi nécessaire. - Identifiez la position du
    démarreur. - Repérez les branchements etles positions des connexions du
    démarreur. - Débranchez les connexionsdu démarreur. - Analyser les points de
    fixation. - Identifier les différentesfixations du démarreur. Note : le
    démarreur peut être fixé soit à : - la boîte de vitesse. - la boîte de
    vitesse et l'arrièredu démarreur au moteur. - la boîte de vitesse par
    desdifférentes vis, et ces derniers servent à maintenir en place le
    groupemotopropulseur par exemple Volkswagen,Audi, Seat et Skoda. Dans ce
    type de fixations il faut placer un cric sous le moteur afinpour le
    soutenir. - la boîte de vitesse, dansde nombreux autres cas ces mêmes vis
    sont reliées à des organes (supportde filtre à air, support de canalisation
    etc.). - Déposer votre démarreur. - Après la dépose du démarreur,Il faut
    récupérer le guide qui sert pour le centrer sur la boite de vitessepuisqu'il
    peut rester accroché sur la tête du démarreur. - Récupérez le support
    defixation à l'arrière du démarreur car il ne sera pas livré sur lanouvelle
    pièce.
  S4_REPOSE: >-
    - Comparer le nouveau démarreur avec celui monté sur le véhicule avant de le
    remonté, s'assurez que les pointsde fixations et le nombre de dents soient
    identiques. - Mettre en place le supportde fixation arrière du démarreur. -
    Remontez le démarreuret vérifiez qu'il soit bien positionné sur son guide. -
    Serrer les différentesfixations du démarreur. - Nettoyez à l'aide
    d'unebrosse métallique les cosses qui pourraient être oxydées. - Rebranchez
    les connexionsdu démarreur. - Rebranchez la bornenégative de la batterie. -
    Vérifiez le bonfonctionnement du démarreur. ✅ Après remontage, vérifiez les
    spécifications dans la fiche technique Démarreur.
  S5: >-
    Erreurs frequentes lors du remplacement d'un demarreur : - Oublier de
    debrancher la batterie — le cable B+ du demarreur est sous tension
    permanente, risque de court-circuit et d'etincelle- Ne pas verifier la
    couronne du volant moteur — des dents cassees empechent le lanceur
    d'engrener correctement et usent le demarreur neuf prematurement- Inverser
    les connexions electriques — le cable B+ (gros cable batterie) et le fil de
    commande du solenoide ne sont pas interchangeables- Forcer les vis de
    fixation si le demarreur ne s'aligne pas — signe que la reference est
    incorrecte ou qu'un element gene le positionnement- Ne pas tester le circuit
    electrique avant de remplacer le demarreur — une batterie faible, un cable
    oxyde ou un contacteur defaillant peuvent mimer une panne de demarreur-
    Oublier de verifier le serrage de la borne B+ apres montage — un mauvais
    contact provoque des chutes de tension et un demarrage lent
  S6: >-
    Verifications apres remplacement du demarreur : - Test de demarrage : le
    moteur doit demarrer sans bruit anormal — un claquement metallique indique
    un mauvais engrainement du lanceur sur la couronne- Tension batterie :
    mesurer avec un multimetre (12,6 V moteur arret, 13,5-14,5 V moteur
    tournant) — une tension basse apres demarrage signale un probleme
    d'alternateur, pas du demarreur- Connexions electriques : verifier que la
    borne B+ est bien serree et sans oxydation — un mauvais contact provoque un
    demarrage lent qui mime un demarreur defaillant- Couple de serrage :
    verifier les vis de fixation du demarreur sur la cloche de boite — un
    demarreur mal fixe vibre et use le pignon lanceur- Absence de fumee ou
    d'odeur : une odeur de brule apres demarrage indique un probleme de cablage
    ou un demarreur bloque en position engrenee
  S_GARAGE: >-
    Nous vous recommandons de confier cette intervention à un professionnel : -
    Plusieurs causes possibles de défaillance (4 identifiées) nécessitent un
    diagnostic professionnel Un garagiste qualifié dispose de l'outillage et de
    l'expérience nécessaires pour effectuer cette opération en toute sécurité.
  S7: >-
    - neiman - contacteur demarreur
  S8: >-
    Démarreur OE, OES ou échange standard ?Les démarreurs OES (Bosch, Valeo,
    Denso) sont de qualité première monte. L'échange standard est économique et
    fiable : pièce reconditionnée avec garantie. Comment savoir si mon démarreur
    est HS ?Claquement sans démarrage (solénoïde), démarreur qui tourne dans le
    vide (lanceur usé), pas de réaction au contact (moteur électrique grillé).
    Tous les combien changer le démarreur ?Pas de périodicité fixe. Durée de vie
    150 000 à 250 000 km selon utilisation. Les démarrages fréquents (ville)
    usent plus vite. Peut-on changer le démarreur soi-même ?Oui, opération
    accessible. Débrancher la batterie, dévisser les 2-3 vis de fixation,
    débrancher les fils. Compter 1h à 2h selon l'accès. Quelle erreur éviter
    avec le démarreur ?Ne pas insister si le démarreur ne répond pas (risque de
    griller le solénoïde). Vérifier la batterie et les câbles avant de changer
    le démarreur.
  META: >-
    {"meta_title":"Démarreur : Guide Remplacement et Diagnostic |
    AutoMecanik","meta_description":"Claquement au démarrage, moteur qui ne se
    lance pas ? Découvrez quand changer le démarreur, comment le remplacer et
    choisir la pièce compatible sur AutoMecanik."}
---

# Démarreur - Guide Diagnostic Complet

## Fonction et Rôle

Appliquer une rotation initiale au moteur pour declencher le demarrage

**Actions principales:** lancer le moteur, entrainer, demarrer, mettre en rotation, entrainer le vilebrequin

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Aucune reaction au contact moteur electrique hs**
  aucune reaction au contact moteur electrique hs

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement contact demarrage solenoide**
  claquement contact demarrage solenoide
- **Grincement ou bruit anormal au demarrage**
  grincement ou bruit anormal au demarrage

### 🟢 Autres Symptômes

- demarreur tourne mais moteur lance
- odeur de brule electrique au demarrage
- plus demarrages difficiles recurrents

## Procédure de Diagnostic

Pour diagnostiquer un problème de démarreur:

1. **Inspection visuelle** - Examiner l'état du démarreur
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le démarreur peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- neiman
- contacteur-demarreur

## ⚠️ Ne Pas Confondre Avec

### alternateur
**Distinction:** Démarreur = lance le moteur (au démarrage), Alternateur = recharge batterie (moteur tournant)

### batterie
**Distinction:** Batterie faible peut simuler un démarreur HS - toujours tester la batterie d'abord

## Critères de Compatibilité

Pour commander le bon démarreur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "démarrage garanti"
- ❌ "homologué CT"
- ❌ "sécurité garantie"

## FAQ

**Démarreur OE, OES ou échange standard ?**
Les démarreurs OES (Bosch, Valeo, Denso) sont de qualité première monte. L'échange standard est économique et fiable : pièce reconditionnée avec garantie.

**Comment savoir si mon démarreur est HS ?**
Claquement sans démarrage (solénoïde), démarreur qui tourne dans le vide (lanceur usé), pas de réaction au contact (moteur électrique grillé).

**Tous les combien changer le démarreur ?**
Pas de périodicité fixe. Durée de vie 150 000 à 250 000 km selon utilisation. Les démarrages fréquents (ville) usent plus vite.

**Peut-on changer le démarreur soi-même ?**
Oui, opération accessible. Débrancher la batterie, dévisser les 2-3 vis de fixation, débrancher les fils. Compter 1h à 2h selon l'accès.

**Quelle erreur éviter avec le démarreur ?**
Ne pas insister si le démarreur ne répond pas (risque de griller le solénoïde). Vérifier la batterie et les câbles avant de changer le démarreur.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/alternateur-diagnostic-mahle.md 2026-02-22 -->
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
n L’alternateur est grippé
n L’alternateur est bloqué
n L’alternateur a été endommagé
pendant le transport
n L’alternateur est tombé sur le
sol lors du montage
n L’alternateur a heurté d’autres
pièces du compartiment moteur
n Ne pas jeter ou laisser tomber
n Vérifier absolument l’état de l’em-
ballage et de l’alternateur avant le
montage

n Faire tourner manuellement l’arbre
de l’alternateur pour vérifier s’il
fait du bruit ou s’il est grippé
n En cas d’endommagement, ne pas
démonter l’alternateur pour éviter
des frais supplémentaires
n Lors du montage de l’alternateur,
éviter de le heurter contre d’autres
le fixer d’abord avec au moins
une vis pour éviter qu’il ne
tombe pendant l’opération

[[PDF_PAGE:11]]
21
5.1 Fonctionnement
L’alternateur ne fonctionne pas (diodes d’excitation défectueuses)
Symptômes de court-circuit sur la borne de masse et le carter du régulateur
Diode d’excitation brûlée (court-circuit)Traces d’arc électrique sur le carter de l’alternateur
Traces de brûlure par court-circuit sur le carter de l’alternateur Le câble conducteur provoque un court-circuit sur le régulateur
-
-
n L’alternateur ne fournit pas d’énergie
n Diodes d’ex

[...]
