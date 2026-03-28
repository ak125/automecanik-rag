---
category: freinage
slug: agregat-de-freinage
title: Agregat de freinage
pg_id: 415
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-25'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v4_converted
  last_enriched_by: script:rag-fill-remaining-gaps
  last_enriched_at: '2026-03-28'
domain:
  role: Module hydraulique de freinage avec ABS/ESP
  must_be_true:
  - moduler
  - réguler
  - distribuer
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
  - ❌ "meilleur freinage"
  cost_range:
    min: 200
    max: 600
    currency: EUR
    unit: l'unite
    source: estimation categorie
  quality_tiers:
  - tier: Piece d'origine (OE)
    description: Reference exacte du constructeur, codee par VIN. Garantit la compatibilite totale avec le calculateur ESP/ABS
      existant.
  - tier: Equipementier de rang 1
    description: Fabricants fournissant les constructeurs en premiere monte. Piece techniquement equivalente a l'OE pour la
      grande majorite des vehicules.
  - tier: Piece reconditionnee
    description: Module hydraulique remis en etat par un specialiste. Option envisageable sur vehicules anciens ou hors serie.
      Verifier la garantie et le processus de requalification.
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
    label: Voyant abs allume en permanence au tableau de bord
    severity: securite
  - id: S2
    label: Abs qui ne se declenche plus au freinage d urgence
    severity: securite
  - id: S3
    label: Bruit de pompe abs anormal ou continu
    severity: securite
  - id: S4
    label: Codes defaut abs stockes p ou c
    severity: securite
  - id: S5
    label: Pedale de frein qui pulse sans raison
    severity: securite
  - id: S6
    label: Esp ou controle de stabilite desactive
    severity: securite
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  quick_checks:
  - Voyant abs allume en permanence au tableau de bord ?
  - 'Observer : abs qui ne se declenche plus au freinage d urgence ?'
  - Bruit de pompe abs anormal ou continu ?
  - 'Observer : codes defaut abs stockes p ou c ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant abs allume en permanence au tableau de bord
  - Abs qui ne se declenche plus au freinage d urgence
  - Bruit de pompe abs anormal ou continu
  - Codes defaut abs stockes p ou c
  - Pedale de frein qui pulse sans raison
  - Esp ou controle de stabilite desactive
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '415'
  intro_title: A quoi sert Agregat de freinage ?
  risk_title: Pourquoi remplacer Agregat de freinage a temps ?
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
  - question: Bloc ABS neuf ou reconditionné ?
    answer: Le reconditionné est 50-70% moins cher. Choisissez un spécialiste reconnu avec garantie. Le neuf est parfois indisponible
      sur véhicules anciens.
  - question: Comment savoir si mon bloc ABS est défaillant ?
    answer: Voyant ABS allumé en permanence, ABS qui ne se déclenche plus au freinage d'urgence, codes défaut P ou C stockés,
      bruit de pompe anormal.
  - question: Tous les combien changer le bloc ABS ?
    answer: Pas de périodicité. C'est une pièce électronique durable. Les pannes sont souvent liées à des soudures ou composants
      électroniques fatigués.
  - question: Peut-on rouler avec le voyant ABS allumé ?
    answer: 'Oui, le freinage classique fonctionne. Mais l''ABS est désactivé : risque de blocage des roues sur sol glissant.
      À réparer rapidement.'
  - question: Quelle erreur éviter avec le bloc ABS ?
    answer: Ne pas débrancher le bloc moteur tournant. Éviter les courts-circuits lors du diagnostic. Faire une purge ABS
      après remplacement (outil requis).
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
doc_id: 60e3a7d3-7911-5579-ba5c-89bb5f9978d8
content_hash: sha256:6cfaa2ef8c7a869e
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
---

# Agregat de freinage - Guide Diagnostic Complet

## Fonction et Rôle

Module hydraulique de freinage avec ABS/ESP

**Actions principales:** moduler, réguler, distribuer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant abs allume en permanence au tableau de bord**
  voyant abs allume en permanence au tableau de bord
- **Abs qui ne se declenche plus au freinage d urgence**
  abs qui ne se declenche plus au freinage d urgence
- **Bruit de pompe abs anormal ou continu**
  bruit de pompe abs anormal ou continu
- **Codes defaut abs stockes p ou c**
  codes defaut abs stockes p ou c
- **Pedale de frein qui pulse sans raison**
  pedale de frein qui pulse sans raison
- **Esp ou controle de stabilite desactive**
  esp ou controle de stabilite desactive

## Procédure de Diagnostic

Pour diagnostiquer un problème de agregat de freinage:

1. **Inspection visuelle** - Examiner l'état du agregat de freinage
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- agregat-de-freinage
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere

## Critères de Compatibilité

Pour commander le bon agregat de freinage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur freinage"

## FAQ

**Bloc ABS neuf ou reconditionné ?**
Le reconditionné est 50-70% moins cher. Choisissez un spécialiste reconnu avec garantie. Le neuf est parfois indisponible sur véhicules anciens.

**Comment savoir si mon bloc ABS est défaillant ?**
Voyant ABS allumé en permanence, ABS qui ne se déclenche plus au freinage d'urgence, codes défaut P ou C stockés, bruit de pompe anormal.

**Tous les combien changer le bloc ABS ?**
Pas de périodicité. C'est une pièce électronique durable. Les pannes sont souvent liées à des soudures ou composants électroniques fatigués.

**Peut-on rouler avec le voyant ABS allumé ?**
Oui, le freinage classique fonctionne. Mais l'ABS est désactivé : risque de blocage des roues sur sol glissant. À réparer rapidement.

**Quelle erreur éviter avec le bloc ABS ?**
Ne pas débrancher le bloc moteur tournant. Éviter les courts-circuits lors du diagnostic. Faire une purge ABS après remplacement (outil requis).


## References supplementaires

<!-- materialized-from-db guides/freinage__purge.md 2026-03-03 -->
### Purge du circuit de freinage - procedure

## Procedure

1. verifier niveau de liquide et etat du bocal.
2. respecter l'ordre de purge constructeur.
3. purger roue par roue jusqu'a disparition des bulles.
4. maintenir le niveau de liquide pendant toute l'operation.
5. controler la fermete de pedale et l'absence de fuite.

## Controle final

- pedale ferme
- freinage stable
- aucun voyant defaut

## Symptomes supplementaires

<!-- materialized-from-db diagnostic/bosch-freinage-brochure-reparation-fad-2020-fr.md 2026-02-14 -->
### bosch freinage brochure reparation fad 2020 fr

[[PDF_PAGE:1]]
Frein à disque :
Conseils et informations pour
le diagnostic et les réparations freinage.

[[PDF_PAGE:3]]
Disque de frein
Conseils et informations pour le diagnostic
et les réparations freinage.
Les descriptions ci-dessous sont volontairement d'une portée générale et ne s'applique
pas à tous les véhicules ni à tous les types de frein à disque. En cas de doute merci de
vous référer à la notice du fabricant
1. Préparatifs
▶ Me surer l'efficacité de freinage sur un banc d'essai.
▶ Ef
fectuer éventuellement un essai sur route si la réclamation du client l'exige.
▶ V
érifier les roulements de roues, la suspension, les barres de force, les bras
de guidage, les essieux, la direction, les pneus et les jantes.
▶ T
out dommage sur la carrosserie peut avoir un impact négatif sur la réponse
de freinage.
fectuer les vérifications selon la check-list de freinage.
2. Dépose
▶ Éliminer le s grosses salissures avant la dépose.
▶ Déposer l'é
trier de frein et les plaquettes
3. Dépose
▶ A ccrocher l'étrier de frein de façon à ce que le flexible de frein ne soit
pas étiré.
ESI[tronic]
ESI[tronic] contient des instructions
complémentaires pour le dépannage,
qui sont plus détaillées et spécifiques
aux véhicules, avec des informations
concernant la position de montage,
la dépose, la pose, les réglages et
les couples de serrage. Il comporte
également des tests, des valeurs de
réglage et des solutions à d'autres
problèmes.
Important !
Ne pas intervenir sur la pédale de frein ni sur le frein de parking durant
la réparation du système de freinage. Assurez-vous qu’il n’y ait pas de dépôt
de graisse ou d’huile sur les surfaces en friction avant de remonter les roues.
Acier moulé –
sûr, parfait, adéquat
L’augmentation de la puissance des
moteurs et du poids des véhicules met
le système de freinage à rude épreuve,
seuls les disques de frein en acier de
qualité supérieure moulés et de structure
homogène respectent les spécifications
des constructeurs automobile.
3

[[PDF_PAGE:4]]
Disque de frein – Conseils et informations pour le diagnostic et
les réparations freinage
4. Vérification du disque de frein (degré d'usure)
▶ Sécuriser le disque de frein à l'aide d'entretoises et des boulons de
roue
▶ Mesurer le degré d'usure du disque de frein avec un pied à co ulisse
5. Vérification du disque de frein (voilage latéral)
▶ Utiliser un comparateur monter sur support magné tique articulé
▶ Ajuster le support magnétique de façon que le palpeu r du comparateur
soit en contact avec la surface de friction, à env iron 10 à 15 mm du bord
extérieur, et soit légèrement en appui
▶ Faire to urner doucement le disque de frein et mesurer le voilage latéral
6. Vérification du disque de frein (voilage latéral)
▶ En cas de disques ventilés, mesurer également le voilage latéral sur la face
intérieure du disque de frein
7. Vérification du disque de frein (écart d'épaisseur)
▶ A l'aide d'un micromèt re extérieur, mesurer l'épaisseur du disque de frein
sur au moins 8 points et relever les valeurs mesurées.
▶ La dif
férence entre la valeur maximale et la valeur minimale mesurée
correspond à l'écart d'épaisseur
Nous vous recommandons de répéter ces mesure s après le montage du
nouveau
4

[[PDF_PAGE:5]]
Causes Conséquences Les conseils de
Bosch
▶ Poussières ou particules
mé
talliques en contact
avec la plaquette ou
le disque de frein.
▶ Bruit au freinage.
▶
Fr
ottement lors du
freinage.
▶ Mauv
aise efficacité du
▶ Lorsq ue vous changez
les disques de frein,
changez toujours
les plaquettes de
frein en même temps
▶
F
onctionnement
anormal de l'étier de
frein.
▶
Voile du disq
ue de frein.
aise et/ou inégale
efficacité au freinage.
▶ Vibr
ations dans le volant.
ation dans la pédale
de frein.
▶ Vér
ifier l'étrier de frein
et le moyeu de roue lors
du remplacement des
disques de frein.
▶
Surc
hauffe due à des
plaquettes de frein
bloquées.
▶
Le v
éhicule a roulé avec
le frein à main.
▶ Le
s pistons de l'étrier
de frein sont coincés.
▶ Surchauffe.
ifier la totalité du
système de freinage
▶ S'as
surer que l'étrier
de frein fonctionne
correctement
▶
ais nettoyage de
la surface de contact.
▶ Domma
ges liés à des
corps étrangers.
▶ Défor
mation du moyeu
de la roue.
▶ Au
gmentation du voile
du disque de frein.
ottements lors du
▶ Ne
ttoyer la surface de
contact entre le disque
de frein et le moyeu de
roue avant de monter
un nouveau disque.
▶
Ne pa
s utiliser de pâte
lubrifiante (pâte de cuivre).
▶ Cont
act avec des
substances corrosives
(sel sur la route, agents
nettoyants...).
▶
ge lié à l'eau
ou à une trop faible
utilisation des freins.
▶ Bruit lors du freinage.
▶
Per
formances de
freinage irrégulières.
▶ Remplac
er les disques
et les plaquettes de
▶ Pré
venir le consommateur
qu'il peut occasionnellement
solliciter les freins en
augmentant la pression
sur la pédale de frein.
Disque de frein – Identifier et résoudre les problèmes les plus courants
Corrosion de
la zone de friction
Marquages et rainures
sur la surface de
friction
Usure inégale
Une décoloration
bleutée à la surface
du disque
Marques sur
5

[[PDF_PAGE:6]]
8. Vérification des pièces voisines
▶ Démonter, nettoyer et vérifier les composants tels qu e le plateau de frein
▶ Contrôler également les pièces voisines, telles que les f lexibles de frein
9. Préparation du moyeu de roue
▶ Avant de poser le nouveau disque, nettoyer et vé rifier la portée du moyeu de
▶ Nettoyer la portée du moyeu de roue avec une brosse de polissage spéciale
10. Vérification du moyeu (oscillation)
▶ Ajuster le support magnétique de façon que le pal peur du manomètre soit
en contact avec la portée du moyeu, à environ 2 à 4 mm d u bord extérieur,
et soit légèrement en appui
▶ Le palpeur ne doit pas pouvoir tomber dans les trous de f ixation des
boulons de roue
▶ Faire tourner doucement le moyeu et mesurer l'osci llation
11. Pose d'un nouveau disque de frein
▶ Ne pas appliquer de lubrifiants ni de vernis sur la portée nettoyée et
brillante du moyeu de roue
▶ Fixer le nouveau disque de frein à l'aide d'entretoises et de s boulons
de roue
▶ Mesurer le voilage latéral
12. Pose de la chape d'étrier
▶ Avant de poser la chape, lubrifier les emplacements accueillant les
oreilles des plaquettes e t (selon la conception de l'étrier de frein) les
colonnettes de l'étrier à l'aide du Bosch Superfit réf. 5 000 000 150
ou 5 000 000 376
▶ Installer les vis de la chape avec du frein filet et serrer (au couple
spécifique)
intérieur
e du disque de frein
· Ne jamais utiliser de lubrifiant contenant du cuivre
·
Pour certains véhicules, des vis neuves devront être utilisées
· Les vis récupérées doivent être nettoyées avant toute réutilisation
Ne pas procéder à un surfaçage
6

[[PDF_PAGE:7]]
13. Repousse du piston (étrier sans anti-retour)
▶ A l'aide d'un repousse piston, repousser complètement le piston de l'étrier
de frein sans anti-retour
▶ Dans le cas d'un étrier fixe, vérifier ensuite la position du piston et la

corriger si nécessaire
▶ Vérifier la position du joint cache poussière du piston
14. Repousse du piston (étrier avec anti-retour)
▶ Faire rentrer le piston de l'étrier de frein avec anti-retour à l'aide d'un
repousse piston, en le poussant à fond avec un mouvement de rotation
▶ Le dévisser ensuite sur environ 1/4 à 1/2 tour jusqu’à ce que les marquages
à l'intérieur du piston soient alignés par rapport à ceux du logement de
l'étrier.
· Le dos des plaquettes de frein autocollantes ne doit jamais être lubrifié
· Le frein à main doit être totalement desserré lors de la repousse du piston et le
levier doit être en butée
· Pour les véhicules équipés d'un frein à main électromécanique, le système doit
être en mode service. Ceci nécessite l'utilisation d'un appareil de la gamme KTS
7

[[PDF_PAGE:8]]
15. Montage des plaquettes
▶ Placer les plaques de guidage des plaquettes sur l a
chape si besoin
▶ Lubrifier les oreilles des plaquettes à l'aide du
Bosch Superfit réf. 5 000 000 150 ou 5 000 000 376
16. Montage des plaquettes
▶ Installer les plaquettes sur la chape
▶ S'assurer que la position de montage est correcte, notamment pour
les plaquettes directionnelles, celles-ci présentant un sens
17. Montage des plaquettes
▶ Retirer la protection de la couche adhésive au dos de la plaquette
juste avant le montage
Ne jamais appliquer de lubrifiant sur la couche adhésive
Astuce d'atelier
Une réparation avec de la graisse contenant
du cuivre peut entraîner des vibrations en
résonance et/ou empêcher les plaquettes
de frein de revenir souplement en position
desserrée. Cela peut donc entraîner des
crissements.
En appliquant la graisse de frein Superfit
de Bosch sur les oreilles des plaquettes
de frein, il est possible d'éviter ces bruits et
d'améliorer les propriétés de glissement des
plaquettes dans leur logement.
8

[[PDF_PAGE:9]]
Causes Conséquences Les conseils de Bosch
▶ Les étriers et/ou
s pistons sont bloqués.
▶ Le guide d'é
trier de
frein ne fonctionne
pas correctement.
▶
Le v éhicule dévie d'un
coté lors du freinage.
▶ Une usur
e plus rapide
et/ou inégale des
▶
Vér ifier les étriers
er les plaquettes
▶ Usure de
s joints et/ou
des ressorts des étriers
▶
Un jeu e
xcessif des
étriers.
e prématurée
des plaquettes de frein.
▶ Bruits lors du freinage.
ifier les étriers de
frein et les remplacer
si nécessaire.
▶
▶ Pous
sières ou particules
métalliques en contact
▶
Éraf
lures à la surface
▶ Bruit lors du fr
einage.
ations lors du
aise efficacité au
ifier les disques de
▶
▶ Tr
ès forte température
due au contact permanent
entre les plaquettes et
le disque.
▶
Une lé
gère courbure du
support de la plaquette.
s étriers de frein et/
ou les pistons sont
bloqués.
▶
éhicule dévie d'un
▶ Surchauffe du disque.
▶
Usure iné
gale de
la garniture de freinage.
Plaquettes de frein – Identifier et résoudre les problèmes les plus
courants
Usure sur une
seule face
Usure conique :
verticale ou horizontale
Rainures et marques
sur le matériel de
Fissures ou cassures
dans le matériel de
9

[[PDF_PAGE:10]]
Après la réparation proprement dite,
il reste à effectuer des tâches et des
contrôles finaux, par exemple des tests
ou des essais sur route.
18. Montage de l'étrier, train avant
▶ Monter l'étrier sur la chape et s'assurer qu'il est correctement
positionné
▶ Visser les colonnettes de l'étrier de frein
▶ Installer et serrer les boulons de l'étrier (au co uple spécifique)
▶ Remplacer les pièces accessoires telles que ressor ts, agrafes, etc
▶ Après le montage, pomper plusieurs fois avec la pédale de frein
19. Montage de l'étrier, train arrière
▶ Monter l'étrier sur la chape et s'assurer qu'il est correctement positionné.
L'ergot présent sur le dos de la plaquette doit se trouver dans l'encoche du
piston
▶ Visser les colonnettes de l'étrier de frein, remplacer les pièces accessoires
telles que ressorts, agrafes, etc.
▶ Après le montage, pomper plusieurs fois avec la pédale de frein. Les câbles
du frein à main ne devront être attachés qu'à ce stade. Effectuer ensuite le
réglage du frein de parking
10

[[PDF_PAGE:11]]
Checklist de freinage
20 points de sécurité
Les tests et vérifications ci-dessous comprennent des contrôles visuels, fonctionnels et
d'étanchéité. Ils sont complétés par des contrôles internes et tests d'efficacité. Une dépose
et repose peut s'avérer nécessaire. Pour la description des procédures de pose/dépose et
pour toute autre information, se reporter à ESI[tronic].
Test OK not OK
~ p
1. Test d’efficacité sur banc de freinage
Force de freinage / écart de freinage / détermination du coefficient de freinage / contrôle des valeurs spécifiées.
Pour plus d'informations, se reporter à ESI[tronic]
2. Essai sur route
Bruit / vibration de la pédale de frein / vibrations dans le volant / volant non centré / la voiture tire à
gauche ou à droite
3. Roulements de roue
Etat, bruit de roulement / jeu latéral / jeu axial / étanchéité
4. Suspension des roues
Joints d'appui et de guidage / moyeu / système de fixation de la roue
5. Essieux, suspension, direction
Jambe de force / amortisseur / ressorts / axe de guidage / supports en caoutchouc / direction
6. Pneus / jantes
Profondeur de profil / usure / pression / équilibrage / adéquation avec le véhicule / détériorations
7. Actionnement du frein de service
Caoutchouc de la pédale / course à vide / jeu dans la tringlerie / facilité de mouvement de l'axe de
la pédale / contacteur de feu stop
8. Actionnement du frein à main
Course du levier / bouton poussoir / facilité de mouvement / voyant / système de commande en cas
d'AFU électromécanique
9. Servofrein, clapet de retenue
Détériorations externes / fixations / clapet de retenue / flexibles et tuyaux / fonctionnement et étanchéité
du servofrein. Pour plus d'informations, se reporter à ESI[tronic]
10. Réservoir de liquide hydraulique
Bouchon / réservoir / fixation / contacteur de niveau
11. Liquide de frein
Niveau / aspect / altération du liquide de frein / teneur en eau / point d'ébullition
12. Maître-cylindre
Dommages externes / fixation appropriée / raccordements / étanchéité
13. ABS/TCS/ESP®/SBC – Bloc hydraulique
Dommages externes / fixation appropriée / raccordements / protections / fonctionnement / étanchéité
Important ! Il peut s'avérer nécessaire d'effectuer un essai hydraulique et électrique
14. Tuyaux de frein, flexibles de frein
D
ommage externes / fixation appropriée / raccordements / corrosion / pose sans torsion / vétusté / étanchéité
15. Régulateur de freinage, limiteur de freinage
Dommages externes / fixation appropriée / raccordements / tige de commande, levier / butée / fonctionnement
16. Étrier de frein
Dommages externes / fixation appropriée / vis de purge / soufflets / étanchéité / supports de plaquette /
guides / mouvement aisé du piston / garniture anti-poussière / réglage de base
17. Plaquette de frein
Épaisseur (*) de la plaquette de frein / dommages / fissures / polissage / position de montage / colonnettes
plaquettes / plaques coulissantes
Important ! (*) Limite d'usure de 4 mm d'épaisseur, mesurée sans le plateau de frein
18. Disque de frein
Degré d'usure / dommages / formations de fissures / corrosion / voilage latéral / tolérance d'épaisseur /
voilage radial
19. Frein à tambour
Plateau de frein / cylindre de frein / levier de frein à main / système de rattrapage / sabot de frein /
mâchoire de frein / ressorts de rappel / réglage initial
20. Câbles de frein, liaisons de freinage
Dommages externes / fixations / installation correcte / ruptures
11

[[PDF_PAGE:12]]
Pour en savoir plus : www.bosch.fr
What drives you,
drives us*
Bosch : votre partenaire pour
un avenir prometteur du garage
boschaftermarket.com
Les technologies de Bosch sont présentes sur presque tous les véhicules
du monde. Notre priorité ? Nos clients, et garant

[...]
