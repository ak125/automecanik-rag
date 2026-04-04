---
category: distribution
slug: poulie-d-alternateur
title: Poulie d'alternateur
pg_id: 1108
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
  role: Transmet le mouvement à l'alternateur
  must_be_true:
  - entrainer
  - transmettre
  must_not_contain:
  - freinage
  - climatisation
  - turbo
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - courroie-de-distribution
  - kit-de-distribution
  - galet-tendeur-de-courroie-de-distribution
  - galet-enrouleur-de-courroie-de-distribution
  - pompe-a-eau
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
  - ❌ "meilleure charge"
  cost_range:
    min: 47
    max: 56
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE (OES)
  - tier: Adaptable qualite
  - tier: Reconditionne
  - tier: Echange standard
  brands:
    premium:
    - Gates
    - Continental/Contitech
    standard:
    - Dayco
    - SKF
    - INA
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Sifflement aigu au demarrage a froid
    severity: confort
  - id: S2
    label: Courroie d accessoire qui saute ou patine
    severity: confort
  - id: S3
    label: Vibrations moteur au ralenti
    severity: confort
  - id: S4
    label: Bruit de roulement au niveau de l alternateur
    severity: confort
  - id: S5
    label: Alternateur qui charge mal par intermittence
    severity: confort
  - id: S6
    label: Plus de 120 000 km sans remplacement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - remplacement preventif recommande
  depose_steps:
  - Detendre la courroie d'accessoire via le galet tendeur automatique ou la vis de reglage
  - Retirer la courroie d'accessoire de la poulie d'alternateur
  - Bloquer l'alternateur et devisser la vis centrale de la poulie (souvent pas inverse, cle de 24)
  - Extraire l'ancienne poulie (un outil extracteur peut etre necessaire si poulie debrayable)
  - Monter la nouvelle poulie en respectant le sens, serrer au couple (50-80 Nm)
  - Remettre la courroie et verifier la tension et l'alignement
  quick_checks:
  - 'Observer : sifflement aigu au demarrage a froid ?'
  - 'Observer : courroie d accessoire qui saute ou patine ?'
  - Vibrations moteur au ralenti ?
  - Bruit de roulement au niveau de l alternateur ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Sifflement aigu au demarrage a froid
  - Courroie d accessoire qui saute ou patine
  - Vibrations moteur au ralenti
  - Bruit de roulement au niveau de l alternateur
  - Alternateur qui charge mal par intermittence
  - Plus de 120 000 km sans remplacement
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '1108'
  intro_title: A quoi sert Poulie d'alternateur ?
  risk_title: Pourquoi remplacer Poulie d'alternateur a temps ?
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
  - question: Poulie d'alternateur OE ou adaptable ?
    answer: 'Les poulies OES (INA, SKF, Gates) sont fiables. Vérifiez le type : fixe, débrayable ou roue libre selon votre
      véhicule.'
  - question: Comment savoir si ma poulie d'alternateur est HS ?
    answer: Sifflement aigu au démarrage, courroie qui saute, vibrations moteur au ralenti, bruit de roulement usé.
  - question: Tous les combien changer la poulie d'alternateur ?
    answer: Entre 100 000 et 150 000 km. Les poulies débrayables s'usent plus vite. À vérifier à chaque changement de courroie.
  - question: Peut-on changer la poulie d'alternateur soi-même ?
    answer: Oui mais nécessite souvent un outil spécial pour bloquer la poulie. Attention au sens de vissage (parfois inversé).
  - question: Quelle erreur éviter avec la poulie d'alternateur ?
    answer: Ne pas serrer au couple. Vérifier le type exact (fixe vs débrayable). Remplacer la courroie en même temps si usée.
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
doc_id: df3f1ad3-e6bb-52bf-9f8d-2de8816b901b
content_hash: sha256:48c8dedf193fb4b8
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
  area: Face laterale du moteur, derriere le carter de distribution
  access: Depose courroie accessoire + carter distribution
  adjacent_parts:
  - courroie
  - galets
  - pompe a eau
  - poulie
installation:
  difficulty: difficile (pro recommande)
  time: 3h a 6h
  tools:
  - kit calage distribution
  - cle dynamometrique
  - extracteur poulie
  prerequisite: Moteur cale au PMH, ne pas tourner le moteur sans courroie
phase5_enrichment:
  _source: automotive.hutchinson.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: false
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Dés la mise en marche dumoteur la courroie d'accessoires du véhicule va
    faire tourner la poulie d'alternateur quiva-t-elle même faire fonctionner
    l'alternateur. L'alternateur de l'automobile va fournir lecourant nécessaire
    au réseau électrique du véhicule à travers la batterie de la voiture. Il
    existe plusieurs types depoulie d'alternateur selon le type de la courroie
    d'accessoires : - Poulie à profil poly-V : ce type est le plus utilisé à
    cause de lasurface de contact importante avec la courroie et il a remplacé
    la poulie àprofil trapézoïdale. - Poulie à profil trapézoïdale. - Poulie à
    roue libre nommé aussi pouliedébrayable : elle lisseles à-coups de
    transmission entre le vilebrequin et l'alternateur. En savoir plus : poulie
    d'alternateur — définition et rôle mécanique 🚨 Bruit Poulie d'alternateur :
    causes et diagnostic
  S2: >-
    Ne pas attendre la panne complete pour intervenir. Symptômes d'usure : -
    Sifflement aigu au demarrage a froid - Courroie d accessoire qui saute ou
    patine - Vibrations moteur au ralenti - Bruit de roulement au niveau de l
    alternateur - Alternateur qui charge mal par intermittence - Plus de 120 000
    km sans remplacement
  S3: >-
    Pour choisir les bons poulie d alternateur pour votre véhicule : - Marque de
    votre véhicule - Modele de votre véhicule - Annee de votre véhicule -
    Vérifier : sifflement aigu au demarrage a froid - Vérifier : courroie d
    accessoire qui saute ou patine - Vérifier : vibrations moteur au ralenti -
    Vérifier : bruit de roulement au niveau de l alternateur - Vérifier :
    alternateur qui charge mal par intermittence - Vérifier : plus de 120 000 km
    sans remplacement
  S4_DEPOSE: >-
    1. Detendre la courroie d'accessoire via le galet tendeur automatique ou la
    vis de reglage 2. Retirer la courroie d'accessoire de la poulie
    d'alternateur 3. Bloquer l'alternateur et devisser la vis centrale de la
    poulie (souvent pas inverse, cle de 24) 4. Extraire l'ancienne poulie (un
    outil extracteur peut etre necessaire si poulie debrayable) 5. Monter la
    nouvelle poulie en respectant le sens, serrer au couple (50-80 Nm) 6.
    Remettre la courroie et verifier la tension et l'alignement
  S4_REPOSE: >-
    - Vérifiez que la poulie d'alternateur neuve est identique à celle démontée.
    - Changez la courroie d'accessoires et le galet tendeur d'accessoires si
    nécessaire. - Remontez la poulie d'alternateur. - Serrez la fixation de la
    poulie d'alternateur. - Remontez la courroie d'accessoires. - Rebranchez la
    batterie. - Contrôlez le bon fonctionnement de l'alternateur. ✅ Après
    remontage, vérifiez les spécifications dans la fiche technique Poulie
    d'alternateur.
  S5: >-
    - ❌ "homologué CT" - ❌ "sécurité garantie" - ❌ "zéro panne" - ❌ "garanti à
    vie" - ❌ "meilleure charge"
  S6: >-
    La poulie d'alternateur (poulie à roue libre ou poulie débrayante) transmet
    le mouvement de la courroie d'accessoire à l'alternateur tout en absorbant
    les irrégularités de rotation du moteur. Après remplacement, les contrôles
    portent sur le silence de fonctionnement, la tension de courroie et la
    charge de l'alternateur. - Absence de sifflement au démarrage à froid : au
    premier démarrage, écouter spécifiquement la zone courroie d'accessoire
    pendant les 2 à 3 premières minutes. Un sifflement aigu qui disparaît avec
    la chauffe peut indiquer une courroie ancienne et détendue — la remplacer si
    elle a plus de 60 000 km. Un sifflement permanent signale une tension de
    courroie incorrecte ou un mauvais montage de la poulie. - Sens de rotation
    du mécanisme libre vérifié : avant remontage de la courroie, faire tourner
    la poulie à la main dans le sens de rotation du moteur — elle doit tourner
    librement. Dans le sens inverse, elle doit se bloquer (comportement de la
    roue libre). Si la poulie tourne librement dans les deux sens ou ne tourne
    pas du tout, la pièce est défectueuse ou mal montée. - Couple de serrage de
    l'écrou central respecté : la poulie d'alternateur s'assemble avec un outil
    spécial (douille à ergots) et un contre-appui. Le couple de serrage est
    généralement compris entre 50 et 80 N·m selon le modèle d'alternateur. Un
    serrage insuffisant provoque un desserrage en usage et une destruction
    rapide de l'alternateur. - Tension de la courroie d'accessoire après pose :
    si la courroie a été déposée lors de l'intervention, contrôler sa tension à
    l'aide d'un tensiomètre vibratoire (fréquence cible : 100 à 150 Hz selon
    véhicule) ou par la méthode de la déflexion au doigt (5 à 8 mm de jeu au
    milieu du brin libre). Une courroie trop tendue détruit le roulement de
    l'alternateur. - Charge de l'alternateur vérifiée au multimètre : avec le
    moteur en marche à 2 000 tr/min et les consommateurs allumés (feux,
    chauffage, lunette thermique), mesurer la tension aux bornes de la batterie.
    Une valeur entre 13,8 V et 14,4 V confirme que l'alternateur charge
    correctement via la nouvelle poulie. En dessous de 13,5 V, la poulie ne
    transmet pas correctement le couple. - Absence de vibrations au ralenti : au
    ralenti stable (750 à 850 tr/min selon moteur), ne pas percevoir de
    vibration anormale du moteur liée à un déséquilibre de la poulie. Des
    vibrations rythmiques au ralenti qui disparaissent à 1 500 tr/min signalent
    un déséquilibre de la poulie neuve ou un montage légèrement excentré.
  S_GARAGE: >-
    Nous vous recommandons de confier cette intervention à un professionnel : -
    Plusieurs causes possibles de défaillance (3 identifiées) nécessitent un
    diagnostic professionnel Un garagiste qualifié dispose de l'outillage et de
    l'expérience nécessaires pour effectuer cette opération en toute sécurité.
  S7: >-
    - alternateur - courroie d accessoire - galet enrouleur de courroie d
    accessoire - galet tendeur de courroie d accessoire - poulie vilebrequin
  S8: >-
    Poulie d'alternateur OE ou adaptable ?Les poulies OES (INA, SKF, Gates) sont
    fiables. Vérifiez le type : fixe, débrayable ou roue libre selon votre
    véhicule. Comment savoir si ma poulie d'alternateur est HS ?Sifflement aigu
    au démarrage, courroie qui saute, vibrations moteur au ralenti, bruit de
    roulement usé. Tous les combien changer la poulie d'alternateur ?Entre 100
    000 et 150 000 km. Les poulies débrayables s'usent plus vite. À vérifier à
    chaque changement de courroie. Peut-on changer la poulie d'alternateur soi-
    même ?Oui mais nécessite souvent un outil spécial pour bloquer la poulie.
    Attention au sens de vissage (parfois inversé). Quelle erreur éviter avec la
    poulie d'alternateur ?Ne pas serrer au couple. Vérifier le type exact (fixe
    vs débrayable). Remplacer la courroie en même temps si usée.
  META: >-
    {"meta_title":"Poulie d'alternateur : sifflement, usure et remplacement |
    AutoMecanik","meta_description":"Sifflement aigu au démarrage à froid ou
    courroie qui patine ? La poulie d'alternateur est peut-être usée. Guide pour
    identifier le bon type (fixe ou débrayable) et le
    remplacer.","og_title":"Poulie d'alternateur : guide diagnostic et
    choix","og_description":"Sifflement aigu au démarrage à froid ou courroie
    qui patine ? La poulie d'alternateur est peut-être usée. Guide pour
    identifier le bon type (fixe ou débrayable) et le remplacer.","schema_type":
    "Article","primary_intent":"diagnostic","gate_report":"PASS","char_count_tit
    le":56,"char_count_desc":196}
---

# Poulie d'alternateur - Guide Diagnostic Complet

## Fonction et Rôle

Transmet le mouvement à l'alternateur

**Actions principales:** entrainer, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- sifflement aigu au demarrage a froid
- courroie d accessoire qui saute ou patine
- vibrations moteur au ralenti
- bruit de roulement au niveau de l alternateur
- alternateur qui charge mal par intermittence
- plus de 120 000 km sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de poulie d'alternateur:

1. **Inspection visuelle** - Examiner l'état du poulie d'alternateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon poulie d'alternateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure charge"

## FAQ

**Poulie d'alternateur OE ou adaptable ?**
Les poulies OES (INA, SKF, Gates) sont fiables. Vérifiez le type : fixe, débrayable ou roue libre selon votre véhicule.

**Comment savoir si ma poulie d'alternateur est HS ?**
Sifflement aigu au démarrage, courroie qui saute, vibrations moteur au ralenti, bruit de roulement usé.

**Tous les combien changer la poulie d'alternateur ?**
Entre 100 000 et 150 000 km. Les poulies débrayables s'usent plus vite. À vérifier à chaque changement de courroie.

**Peut-on changer la poulie d'alternateur soi-même ?**
Oui mais nécessite souvent un outil spécial pour bloquer la poulie. Attention au sens de vissage (parfois inversé).

**Quelle erreur éviter avec la poulie d'alternateur ?**
Ne pas serrer au couple. Vérifier le type exact (fixe vs débrayable). Remplacer la courroie en même temps si usée.


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
