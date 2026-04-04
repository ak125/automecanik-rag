---
category: eclairage
slug: commande-d-eclairage
title: Commande d'éclairage
pg_id: 809
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
  role: Commande les différents feux du véhicule
  must_be_true:
  - commander
  - activer
  - regler
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
  - ❌ "meilleur éclairage"
  cost_range:
    min: 40
    max: 200
    currency: EUR
    unit: commodo
    source: catalogue automecanik
  quality_tiers:
  - tier: Constructeur (OE)
    description: 'Commodo d''origine : connecteurs, fonctions (veille, croisement, route, antibrouillard, correcteur) et codage
      calculateur conformes au véhicule.'
  - tier: Équivalent OE (OES)
    description: 'Équipementiers reconnus dans ce segment : Valeo, Hella, TRW. Commodos avec connecteurs conformes et fonctions
      vérifiées par correspondance de référence.'
  - tier: Adaptable
    description: Commodos génériques avec risque de fonctions manquantes ou de connecteurs légèrement différents. Peut nécessiter
      adaptation.
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
    label: Feux croisement route allument plus
    severity: confort
  - id: S2
    label: Commodo bloque ou difficile a tourner
    severity: immobilisation
  - id: S3
    label: Fonctions aleatoires s allument puis s eteignent
    severity: confort
  - id: S4
    label: Clignotants fonctionnent plus depuis commodo
    severity: confort
  - id: S5
    label: Bruit de craquement en actionnant l interrupteur
    severity: confort
  - id: S6
    label: Fusibles ok mais feux inoperants
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - 'vehicule immobilise ou symptome critique : verification urgente piece et alimentation'
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  quick_checks:
  - 'Observer : feux croisement route allument plus ?'
  - 'Observer : commodo bloque ou difficile a tourner ?'
  - 'Observer : fonctions aleatoires s allument puis s eteignent ?'
  - 'Observer : clignotants fonctionnent plus depuis commodo ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Feux croisement route allument plus
  - Commodo bloque ou difficile a tourner
  - Fonctions aleatoires s allument puis s eteignent
  - Clignotants fonctionnent plus depuis commodo
  - Bruit de craquement en actionnant l interrupteur
  - Fusibles ok mais feux inoperants
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '809'
  intro_title: A quoi sert Commande d'éclairage ?
  risk_title: Pourquoi remplacer Commande d'éclairage a temps ?
  risk_explanation: '**Pièce HS** - Le commande d''éclairage peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le commande d''éclairage peut être hors service et nécessiter un remplacement'
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Commande d'éclairage OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (Valeo, Hella). Le commodo doit être parfaitement compatible avec votre véhicule (connecteurs,
      fonctions). Les adaptables peuvent avoir des incompatibilités.
  - question: Comment savoir si ma commande d'éclairage est HS ?
    answer: Feux qui ne s'allument plus ou par intermittence, commodo qui reste bloqué, fonctions aléatoires, bruit de craquement
      en tournant le commutateur.
  - question: Tous les combien changer la commande d'éclairage ?
    answer: Pas de périodicité fixe. Durée de vie variable selon usage. À remplacer si dysfonctionnement avéré après vérification
      des fusibles et ampoules.
  - question: Peut-on changer la commande d'éclairage soi-même ?
    answer: Oui, opération accessible. Débrancher la batterie, déposer le cache colonne de direction, débrancher les connecteurs,
      dévisser le commodo. 30 min à 1h.
  - question: Quelle erreur éviter avec la commande d'éclairage ?
    answer: Toujours vérifier les fusibles et ampoules avant de remplacer le commodo. Débrancher la batterie pour éviter les
      courts-circuits. Ne pas forcer sur les connecteurs.
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
doc_id: 271e3dbc-55df-5f6f-b12a-21d0223b3fb3
content_hash: sha256:50ece7f502310d3e
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
  - type: hall
    source_ref: corpus RAG web OEM
  - type: électrique
    source_ref: corpus RAG web OEM
  technical_notes:
    norme_din_5035: DIN 5035
    val_020__c: 020 °C
    val_100__: 100 %
    val_11_a: 11 a
    val_11_9__: 11,9 %
    val_12__: 12 %
    val_12_5__: 12,5 %
    val_15_a: 15 a
    val_15_8__: 15,8 %
    val_17_a: 17 a
    val_2_5__: 2,5 %
    val_20__: 20 %
    val_21_a: 21 a
    val_23__: 23 %
    val_25__: 25 %
    val_25_hz: 25 Hz
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le rôle de la commanded''éclairage est de piloter les différentes fonctions d''éclairage et designalisation : feux
    de position, feux de croisement, feux de route, feux clignotants, les appels de phares. L''emplacement de la commanded''éclairage
    change d''un véhicule à un autre : - Dans les anciens modèle de voiture la commande d''éclairage est situés surle tableau
    de bord par plusieurs boutons et chacun d''eux à sa propre fonctiondans le système d''éclairage. - Dans d''autre modèle
    de voiture par exemple chez Volkswagen la commanded''éclairage est partagée sur deux. La première partie est la commandeprincipale
    pour l''allumage des feux avant et arrière est sous forme d''un boutonrotatif situé à gauche du conducteur sur le tableau
    de bord. La deuxième partie est la manette située à portéede main gauche du conducteur sous le volant de direction pour
    actionner lesclignotants et les phares du véhicule. - Sur d''autres véhicules la commande d''éclairage est intégrée à
    un blocunique ou séparé (pièce indépendante). Il regroupe les deux manettes de commande d''éclairage et d''essuie-glaces
    (et autres fonctions selonl''équipement de la voiture). Il est installé à portée de main gauche sous levolant, fixé à
    la colonne de direction. Note : La commanded''éclairage peut intégrer les commandes des feux de brouillard et de détresse,ou
    l''avertisseur sonore (selon le niveau d''équipement de la voiture). Lacommande des feux clignotants est équipée d''un
    dispositif de rappel automatiquede la manette après usage. En savoir plus : commande d''éclairage — définition et rôle
    mécanique 🚨 Bruit Commande d''éclairage : causes et diagnostic'
  S2: 'Une commande d''éclairage défectueuse ne vaplus faire fonctionner les fonctions d''éclairage du véhicule dans ce cas
    sivous remarquez qu''une des fonctions d''éclairage ne fonctionne pas et que lesfeux de la voiture sont en bonne état
    de fonctionnement dans ce cas c''est lecomodo d''éclairage qu''il faut le contrôlez et le remplacé en cas de besoin. Diagnostic
    complet : identifier une panne de commande d''éclairage'
  S3: 'La commande d''éclairage (aussi appelée commodo de phares ou interrupteur de feux) est le module de commande depuis
    lequel le conducteur active les feux de position, de croisement, de route, les anti-brouillards et les clignotants. La
    moindre différence de brochage ou de configuration de fonctions entre un commodo d''origine et une pièce de remplacement
    peut rendre certains feux inopérants ou provoquer des courts-circuits sur le circuit d''éclairage. - Compatibilité stricte
    par référence constructeur (OEM) : les commandes d''éclairage sont très spécifiques à chaque véhicule. Deux modèles de
    la même marque dont les planche de bord sont visuellement identiques peuvent avoir des commodos différents selon les options
    (phares directionnels, correction d''assiette motorisée, feux diurnes LED). La référence OEM est le seul critère fiable.
    - Nombre de fonctions et configuration des feux : la commande doit correspondre exactement à l''équipement d''éclairage
    de votre véhicule. Si votre véhicule est équipé d''anti-brouillards arrière et d''une correction d''assiette électrique
    des phares, la commande de remplacement doit intégrer les positions et résistances correspondantes. Un commodo sans la
    bonne position anti- brouillard court-circuite ou ne pilote pas correctement ces fonctions. - Type de connecteur et nombre
    de voies : les commandes d''éclairage utilisent des connecteurs multiplex de 12 à 24 voies selon les véhicules. La forme
    du connecteur (mini-ISO, Tyco AMP, Molex) et l''affectation des broches sont propres à chaque constructeur. Vérifier le
    nombre de voies sur l''ancienne commande avant sélection. - Intégration de la commande de régulateur de vitesse / limiteur
    : sur de nombreux véhicules récents, le commodo de phares intègre également le régulateur de vitesse et le limiteur de
    vitesse sur la même molette ou les mêmes leviers. Un remplacement sans ces fonctions supprime le régulateur de vitesse
    du véhicule — vérifier les équipements de série ou en option au moment de l''achat d''origine. - Pièce neuve ou reconditionné
    : attention à l''usure des contacts : les commodes de phares usés présentent des contacts internes oxydés ou brûlés. Un
    reconditionné doit avoir subi un nettoyage des contacts à l''alcool isopropylique et un test de résistance de contact
    inférieur à 0,5 Ω par voie. Sans garantie de test électrique, préférer le neuf sur une commande d''éclairage. - Vérification
    des fusibles avant remplacement : un commodo qui ne commande plus les feux alors que les fusibles sont intacts est suspect
    de défaillance interne. Mais si les fusibles ont grillé plusieurs fois, cela indique un court-circuit dans le câblage
    ou les blocs optiques — remplacer le commodo sans traiter le court-circuit recréera la panne. Inspecter le câblage avant
    commande de la pièce. Pour aller plus loin : consultez notre guide d''achat commande d''éclairage — comparatif marques,
    critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Commande d'éclairage pour connaître les spécifications. - Débranchez
    la batterie. - Desserrez les vis de fixations des caches de protection de la colonne dedirection. - Démontez les caches
    supérieur et inférieure de la colonne de direction. - Débranchez les connecteurs de la commande d'éclairage. - Desserrez
    les fixations de la commande d'éclairage. - Démontez la commande d'éclairage.
  S4_REPOSE: '- Vérifiez que la commande d''éclairage neuve est identique à celledémontée. - Remontez la commande d''éclairage.
    - Serrez les fixations de la commande d''éclairage. - Rebranchez les connecteurs de la commande d''éclairage. - Remontez
    les caches supérieur et inférieure de la colonne de direction. - Serrez les vis de fixations des caches de protection
    de la colonne dedirection. - Rebranchez la batterie. - Vérifiez le bon fonctionnement de la commande d''éclairage. ✅ Après
    remontage, vérifiez les spécifications dans la fiche technique Commande d''éclairage.'
  S5: 'Erreurs frequentes avec la commande d''eclairage : - Ne pas verifier les fusibles et relais avant de remplacer la commande
    — un fusible grille ou un relais defaillant est moins couteux et plus frequent- Forcer le demontage du commodo sans connaitre
    le systeme de fixation — les clips et vis sont fragiles, consulter la procedure specifique au vehicule- Ne pas debrancher
    la batterie et attendre 10 minutes avant intervention — le circuit d''airbag passe souvent dans la colonne de direction,
    risque de declenchement accidentel- Confondre commande d''eclairage et commande d''essuie-glace — sur certains vehicules
    les deux commodos sont proches mais pas interchangeables- Oublier de tester toutes les fonctions apres montage (codes,
    phares, anti- brouillard, clignotants) — un mauvais encliquetage du connecteur laisse des fonctions inactives'
  S6: 'Après le remplacement de votre commande d''éclairage, effectuez ces vérifications dans l''ordre. - Testez chaque position
    du commodo dans l''ordre : feux de position, feux de croisement, feux de route — chaque fonction doit s''activer sans
    délai ni intermittence. - Vérifiez le fonctionnement des clignotants gauche et droit depuis la manette : cadence de clignotement
    normale, sans accélération qui indiquerait une ampoule grillée dans le circuit. - Contrôlez les feux arrière simultanément
    (stop, position, brouillard si présent) : un assistant actionne les pédales pendant l''inspection visuelle arrière. -
    Vérifiez l''absence de bruit de craquement lors de l''actionnement de la manette en position feux de route et clignotants.
    - Contrôlez visuellement le câblage du connecteur colonne de direction : aucun fil pincé par le boîtier de commodo, clips
    de verrouillage en place. - Vérifiez que les fusibles correspondants aux feux (boîte à fusibles) sont d''ampérage conforme
    et non fondus après la première utilisation. Consultez également la page références commande d''éclairage pour identifier
    la pièce compatible avec votre véhicule.'
  S7: Quel est le prix d'un commande d'éclairage ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour
    trouver le commande d'éclairage compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon commande d'éclairage est à changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un commande
    d'éclairage défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l'urgence du remplacement.- commande d essuie glace - feu arriere - feu avant
    - feu clignotant
  S8: Comment choisir Commande d'éclairage compatible avec mon vehicule ?Renseignez marque, modele, type moteur et annee,
    puis verifiez la reference Quand remplacer Commande d'éclairage ?En cas de feux croisement route allument plus ou de degradation
    mesurable, Puis-je monter Commande d'éclairage sans verification atelier ?Le montage peut exiger controles de couple,
    alignement et references.
  META: '{"meta_title":"Commande d''éclairage : symptômes et remplacement | AutoMecanik","meta_description":"Feux qui ne s''allument
    plus, commodo bloqué, clignotants défaillants ? Identifiez les signes d''une commande d''éclairage HS et trouvez la référence
    compatible avec votre véhicule.","source":"rag://gammes/commande-d-eclairage.md"}'
---

# Commande d'éclairage - Guide Diagnostic Complet

## Fonction et Rôle

Commande les différents feux du véhicule

**Actions principales:** commander, activer, regler

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Commodo bloque ou difficile a tourner**
  commodo bloque ou difficile a tourner

### 🟢 Autres Symptômes

- feux croisement route allument plus
- fonctions aleatoires s allument puis s eteignent
- clignotants fonctionnent plus depuis commodo
- bruit de craquement en actionnant l interrupteur
- fusibles ok mais feux inoperants

## Procédure de Diagnostic

Pour diagnostiquer un problème de commande d'éclairage:

1. **Inspection visuelle** - Examiner l'état du commande d'éclairage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le commande d'éclairage peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-d-essuie-glace
- feu-arriere
- feu-avant
- feu-clignotant

## Critères de Compatibilité

Pour commander le bon commande d'éclairage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur éclairage"

## FAQ

**Commande d'éclairage OE ou adaptable ?**
Privilégiez l'OE ou OES (Valeo, Hella). Le commodo doit être parfaitement compatible avec votre véhicule (connecteurs, fonctions). Les adaptables peuvent avoir des incompatibilités.

**Comment savoir si ma commande d'éclairage est HS ?**
Feux qui ne s'allument plus ou par intermittence, commodo qui reste bloqué, fonctions aléatoires, bruit de craquement en tournant le commutateur.

**Tous les combien changer la commande d'éclairage ?**
Pas de périodicité fixe. Durée de vie variable selon usage. À remplacer si dysfonctionnement avéré après vérification des fusibles et ampoules.

**Peut-on changer la commande d'éclairage soi-même ?**
Oui, opération accessible. Débrancher la batterie, déposer le cache colonne de direction, débrancher les connecteurs, dévisser le commodo. 30 min à 1h.

**Quelle erreur éviter avec la commande d'éclairage ?**
Toujours vérifier les fusibles et ampoules avant de remplacer le commodo. Débrancher la batterie pour éviter les courts-circuits. Ne pas forcer sur les connecteurs.


## References supplementaires

<!-- materialized-from-db manual/a744e5d73ba5 2026-04-03 -->
### Données techniques OEM — Commande d'éclairage

# Données techniques OEM — Commande d'éclairage
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- hall
- électrique

## Normes applicables
- DIN 5035

## Valeurs techniques de référence
- 020 °C
- 100 %
- 11,9 %
- 12 %
- 12,5 %
- 15,8 %
- 2,5 %
- 20 %
- 23 %
- 25 %
