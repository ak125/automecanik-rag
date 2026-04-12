---
category: refroidissement
slug: durite-de-refroidissement
title: Durite de refroidissement
pg_id: 475
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
  role: Acheminer le liquide de refroidissement entre les elements du circuit
  must_be_true:
  - acheminer
  - conduire
  - relier
  must_not_contain:
  - huile
  - carburant
  - frein
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - radiateur-de-refroidissement
  - pompe-a-eau
  - thermostat
  - vase-d-expansion
  - ventilateur-de-refroidissement
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
  - ❌ "evite la casse moteur"
  cost_range:
    min: 15
    max: 80
    currency: EUR
    unit: durite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: 'Durite conforme aux spécifications constructeur : même matière, mêmes dimensions et mêmes raccords. Recommandé
      pour les véhicules récents ou à forte valeur.'
  - tier: Équipementier reconnu (refroidissement)
    description: Produit de fabricants spécialisés en circuit de refroidissement. Résistance thermique et pression de service
      équivalentes à la pièce d'origine.
  - tier: Durite silicone renforcée (aftermarket)
    description: Offre une résistance thermique et chimique supérieure à l'EPDM standard. Convient particulièrement pour les
      véhicules utilisés intensivement ou en conditions extrêmes. Vérifier la compatibilité des di
  brands:
    premium:
    - Behr/Mahle
    - Gates
    standard:
    - Valeo
    - NRF
    - Febi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Traces de liquide colore sous le vehicule
    severity: confort
  - id: S2
    label: Durite visiblement gonflee ou craquelee
    severity: confort
  - id: S3
    label: Sifflement ou gargouillement dans le circuit
    severity: confort
  - id: S4
    label: Niveau de liquide qui baisse regulierement
    severity: confort
  - id: S5
    label: Odeur sucree de liquide de refroidissement
    severity: confort
  - id: S6
    label: Plus de 100 000 km ou 8 ans sans remplacement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  quick_checks:
  - 'Observer : traces de liquide colore sous le vehicule ?'
  - 'Observer : durite visiblement gonflee ou craquelee ?'
  - 'Observer : sifflement ou gargouillement dans le circuit ?'
  - 'Observer : niveau de liquide qui baisse regulierement ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Traces de liquide colore sous le vehicule
  - Durite visiblement gonflee ou craquelee
  - Sifflement ou gargouillement dans le circuit
  - Niveau de liquide qui baisse regulierement
  - Odeur sucree de liquide de refroidissement
  - Plus de 100 000 km ou 8 ans sans remplacement
  good_practices:
  - Controle du niveau de liquide de refroidissement a froid chaque mois
  - Remplacement du liquide selon preconisation constructeur (2-5 ans)
  - Verification des durites et colliers a chaque revision
  - Purge du circuit apres toute intervention sur le refroidissement
rendering:
  pgId: '475'
  intro_title: A quoi sert Durite de refroidissement ?
  risk_title: Pourquoi remplacer Durite de refroidissement a temps ?
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
  - question: Durite OE ou adaptable ?
    answer: Les durites OES (Gates, Contitech) offrent une résistance optimale à la chaleur et à la pression. Les adaptables
      (Febi, Meyle) conviennent pour un usage courant.
  - question: Comment savoir si une durite est à changer ?
    answer: Durite gonflée, craquelée, suintement au niveau des colliers, traces blanches de calcaire séché, durite dure au
      toucher.
  - question: Tous les combien changer les durites ?
    answer: Contrôle visuel tous les 2 ans. Remplacement préventif à 100 000 km ou 8 ans. Plus tôt si traces de fissures.
  - question: Peut-on changer une durite soi-même ?
    answer: Oui, opération accessible. Vidanger le circuit, desserrer les colliers, remplacer par une durite identique. Purger
      le circuit après.
  - question: Quelle erreur éviter avec les durites ?
    answer: Ne pas réutiliser les vieux colliers. Utiliser des colliers neufs adaptés. Vérifier l'absence de pliure après
      montage.
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
doc_id: 1e5d946e-8a92-5fb5-83f2-c49719db56e5
content_hash: sha256:c672b28c18460299
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
  area: Face avant du vehicule (radiateur) et bloc moteur
  access: Par le dessus (capot) ou face avant
  adjacent_parts:
  - radiateur
  - durites
  - pompe a eau
  - thermostat
installation:
  difficulty: moyen
  time: 30min a 2h
  tools:
  - tournevis
  - pince de serrage
  - bac de recuperation
  prerequisite: Moteur froid, circuit vidange avant depose
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_120__c: '120 °C'
    val_95__c: '95 °C'
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Une durite de liquide de refroidissement est fabriquée encaoutchouc résistant à la chaleur du moteur afin d''assurer
    une circulation optimaldu liquide de refroidissement entre les différents éléments du moteur parexemple radiateur refroidissement
    et moteur. Dans un véhicule on peut avoir plusieurs duritesde liquide de refroidissement. En savoir plus : durite de refroidissement
    — définition et rôle mécanique 🚨 Bruit Durite de refroidissement : causes et diagnostic'
  S2: 'Une durite de liquide de refroidissement défectueuxprésente plusieurs symptômes : - Fuite au niveau de la durite. -
    Déchirure de la durite. - La durite est craquelée. - Les colliers de serrage ne tiennes plus dans ce cas usure des extrémitésdes
    durites. Une durite de liquide de refroidissement et qu''elle n''est pas remplacée à temps va amener à la pertedu liquide
    de refroidissement dans ce cas le moteur risque de surchauffer et deprovoquer des dégâts dans ce dernier (la casse du
    moteur). Diagnostic complet : identifier une panne de durite de refroidissement'
  S3: 'La durite de refroidissement achemine le liquide de refroidissement entre le moteur, le radiateur, le thermostat, le
    vase d''expansion et le chauffage habitacle. Sa rupture ou sa fissuration provoque une perte rapide de liquide, une surchauffe
    moteur et, si non détectée à temps, une casse de culasse (joint de culasse grillé, plaquage de culasse). Les durites en
    caoutchouc EPDM de première monte ont une durée de vie de 100 000 à 150 000 km, mais des conditions d''utilisation sévères
    (circuit vieilli, liquide acide) peuvent réduire cette durée. Voici les critères à vérifier avant commande. - Référence
    véhicule et position sur le circuit — Il existe plusieurs durites sur un même moteur (durite supérieure radiateur, durite
    inférieure, durite vase d''expansion, durite chauffage, etc.). Identifier précisément la durite défaillante par sa position
    (marquée sur les schémas du manuel d''atelier ou reconnaissable à ses diamètres interne et externe et sa longueur). Commandez
    avec la référence OE ou les cotes exactes. - Diamètre interne et externe — Le diamètre interne de la durite (exprimé en
    mm, courant entre 16 et 45 mm) doit correspondre exactement aux raccords du moteur et du radiateur. Une durite trop large
    glisse sur les raccords sous pression ; une durite trop étroite se déforme et restreint le débit de liquide. Ne jamais
    adapter avec des colliers surdimensionnés. - Matériau : EPDM renforcé vs silicone — Les durites EPDM d''origine sont adaptées
    aux liquides de refroidissement OAT, HOAT et NOAT utilisés par les constructeurs. Les durites silicone offrent une résistance
    thermique supérieure (jusqu''à 180 °C contre 120 °C pour l''EPDM standard) et conviennent aux moteurs turbo à températures
    élevées, mais ne pas les utiliser si le circuit contient des liquides à base d''amines (vérifier la fiche technique du
    liquide en place). - Forme pré-moulée ou durite universelle coupée — Les durites pré-moulées reproduisent exactement le
    tracé d''origine avec les coudes à l''angle exact, évitant toute tension ou pincement. Les durites universelles droites
    ou coudées à couper sont acceptables pour des trajets simples, mais inadaptées aux durites avec des coudes multiples ou
    des renforts internes anti-effondrement. - État des colliers de serrage — Lors du remplacement d''une durite, les colliers
    d''origine (souvent des colliers à oreille à usage unique) doivent être remplacés par des colliers à vis de qualité (inox
    de préférence) serrés au couple préconisé, généralement 3 à 5 N·m. Un serrage excessif coupe la durite ; un serrage insuffisant
    laisse fuir sous pression. - Contrôle du circuit avant remontage — Avant de remonter la durite neuve, purger le circuit
    de refroidissement et vérifier l''état du thermostat, de la pompe à eau et du vase d''expansion. Un thermostat grippé
    ouvert ou une pompe à eau dont le roulement bruite sont des défauts qui provoqueront une nouvelle surchauffe à court terme,
    indépendamment de la durite remplacée. Pour aller plus loin : consultez notre guide d''achat durite de refroidissement
    — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Durite de refroidissement pour connaître les spécifications.
    - Arrêtez le moteur et le laissez refroidir. - Localisez l'emplacement de la durite de liquide de refroidissement quevous
    voulez démonter. - Débranchez la batterie. - Libérez si nécessaire l'accès à la durite de liquide de refroidissementque
    vous voulez démonter. - Ouvrir le bouchon du vase d'expansion pour libérer la pression. - Videz le liquide de refroidissement
    dans récipient. - Démontez les colliers de serrage de la durite de liquide derefroidissement que vous voulez démonter.
    - Retirez la durite de liquide de refroidissement.
  S4_REPOSE: 'Le remontage d''une durite de refroidissement paraît simple, mais trois erreurs courantes génèrent des fuites
    après quelques kilomètres : réutilisation des anciens colliers, portée de raccord non nettoyée et durite montée avec un
    pli. Soignez ces points et la purge sera la seule difficulté réelle. - Comparez la durite neuve avec l''ancienne : longueur,
    diamètre intérieur, orientation des coudes. Un mauvais angle contraint la durite en service et provoque une fissure précoce.
    - Contrôlez l''état de la pompe à eau et du radiateur de refroidissement : remplacez-les si l''un présente une fuite ou
    des ailettes bouchées, pendant que le circuit est déjà vidangé. - Nettoyez les portées des raccords sur le moteur, le
    radiateur ou le boîtier de thermostat avec un chiffon non pelucheux. Retirez tout dépôt calcaire ou trace de l''ancien
    joint. - Positionnez la durite neuve sur ses raccords sans pli ni contrainte excessive. Elle doit s''engager facilement
    sur 20 à 30 mm selon le diamètre. - Montez des colliers de serrage neufs adaptés au diamètre. Positionnez-les à 10 mm
    du bout du raccord, pas sur le bourrelet. Serrez progressivement jusqu''à immobilisation sans écraser le caoutchouc. -
    Remontez les pièces déposées lors de l''accès (protection sous moteur, éléments de carrosserie) avant de remplir le circuit.
    - Remplissez le circuit avec le liquide de refroidissement préconisé (dilution 50/50 ou selon fiche constructeur). Ne
    jamais mélanger un liquide vert (silicate) et un liquide rouge (OAT). - Purgez le circuit en ouvrant le ou les bouchons
    de purge prévus (sur le boîtier de thermostat ou le radiateur). Laissez tourner le moteur jusqu''à montée en température
    et fermeture du thermostat. - Contrôlez le niveau une fois le moteur refroidi. Resserrez les colliers à froid si une légère
    suintance est visible. - Effectuez un essai routier et vérifiez l''absence de fuite et la stabilité du niveau sur 2 jours
    d''utilisation. ✅ Après remontage, vérifiez les spécifications dans la fiche technique Durite de refroidissement.'
  S5: 'Erreurs frequentes avec les durites de refroidissement : - Reutiliser les colliers de serrage d''origine — les colliers
    a ressort perdent leur tension et les colliers a vis se deforment, provoquer des fuites- Ne pas verifier l''etat de toutes
    les durites lors du remplacement d''une seule — si une durite est craquelée, les autres du meme age sont dans le meme
    etat- Oublier de purger le circuit apres remplacement — des bulles d''air provoquent des points chauds et un chauffage
    defaillant- Ignorer une durite gonflee ou molle au toucher — signe de degradation interne du caoutchouc, la rupture peut
    survenir sans prevenir- Forcer une durite rigide sur un raccord — le caoutchouc durci par l''age casse au lieu de se deformer.
    Chauffer legerement l''embout au decapeur thermique pour assouplir- Ne pas verifier le niveau de liquide de refroidissement
    dans les jours suivant le remplacement — une purge incomplete se revele par une baisse de niveau progressive'
  S6: 'Une durite de refroidissement remplacée incorrectement ou avec des colliers insuffisamment serrés peut provoquer une
    fuite rapide et une surchauffe moteur. Les contrôles post-montage doivent être effectués à froid avant le premier démarrage,
    puis à nouveau après la première montée en température. - Inspecter visuellement tous les colliers avant le démarrage
    : chaque extrémité de durite doit être positionnée à minimum 5 mm au-delà des jonctions du raccord, et le collier doit
    être centré sur la zone de sertissage. Un collier positionné sur le renfort métallique du raccord ne peut pas s''étancher
    correctement. - Vérifier le couple de serrage des colliers : pour les colliers à vis, le couple de serrage est généralement
    de 2 à 3 Nm. Un serrage excessif écrase la durite et crée des micro-fissures ; un serrage insuffisant laisse fuir sous
    pression. Utiliser un tournevis dynamométrique ou serrer jusqu''à résistance franche sans forcer. - Purger l''air du circuit
    de refroidissement : après la pose, ouvrir le bouchon de purge sur le thermostat ou le radiateur (selon le véhicule) et
    remplir lentement le circuit. Démarrer le moteur et laisser tourner avec le chauffage à fond et le capot ouvert jusqu''à
    disparition des bulles d''air dans le vase d''expansion. Un circuit mal purgé provoque des points chauds et une surchauffe
    localisée. - Contrôler le niveau de liquide de refroidissement après la première chauffe : à moteur chaud, le niveau dans
    le vase d''expansion doit se stabiliser entre les repères MIN et MAX. Une baisse de niveau de plus de 0,2 L indique une
    fuite résiduelle ou une prise d''air. - Inspecter chaque collier à chaud après 10 minutes de fonctionnement : les durites
    se dilatent à chaud et les colliers peuvent légèrement se relâcher. Resserrer d''un quart de tour si un suintement apparaît.
    Attention : ne jamais dévisser un bouchon de radiateur ou de vase d''expansion moteur chaud. - Vérifier l''absence de
    gargouillements dans le circuit : des gargouillements audibles après purge signalent une prise d''air résiduelle ou une
    durite partiellement obstruée. Effectuer un second cycle de purge à moteur chaud jusqu''à disparition complète des bruits.
    - Contrôler la température moteur sur les 50 premiers km : l''aiguille de température doit rester stable dans la zone
    normale (généralement à mi-course). Tout mouvement vers la zone rouge impose un arrêt immédiat pour inspection de l''étanchéité
    du circuit.'
  S7: Quel est le prix d'un durite de refroidissement ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur
    pour trouver le durite de refroidissement compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon durite de refroidissement est à changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un durite de
    refroidissement défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du
    véhicule. Consultez la section symptômes pour évaluer l'urgence du remplacement.- Thermostat. - Radiateur de refroidissement
    . - Pompe à eau . 📖 Fiche technique Durite de refroidissement — intervalles et spécifications d’entretien.
  S8: Comment choisir Durite de refroidissement compatible avec mon vehiculeRenseignez marque, modele, type moteur et annee,
    puis verifiez la reference Quand remplacer Durite de refroidissement ?En cas de traces de liquide colore sous le vehicule
    ou de degradation Puis-je monter Durite de refroidissement sans verification atelier ?Le montage peut exiger controles
    de couple, alignement et references.
  META: '{"meta_title":"Durite de refroidissement : Conseils remplacement | AutoMecanik","meta_description":"Durite de refroidissement
    gonflée, craquelée ou fuite de liquide coloré ? Sachez quand changer cette pièce (100 000 km / 8 ans) et comment la choisir."}'
---

# Durite de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Acheminer le liquide de refroidissement entre les elements du circuit

**Actions principales:** acheminer, conduire, relier, transporter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- traces de liquide colore sous le vehicule
- durite visiblement gonflee ou craquelee
- sifflement ou gargouillement dans le circuit
- niveau de liquide qui baisse regulierement
- odeur sucree de liquide de refroidissement
- plus de 100 000 km ou 8 ans sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de durite de refroidissement:

1. **Inspection visuelle** - Examiner l'état du durite de refroidissement
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

- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- thermostat
- vase-d-expansion
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon durite de refroidissement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "evite la casse moteur"

## FAQ

**Durite OE ou adaptable ?**
Les durites OES (Gates, Contitech) offrent une résistance optimale à la chaleur et à la pression. Les adaptables (Febi, Meyle) conviennent pour un usage courant.

**Comment savoir si une durite est à changer ?**
Durite gonflée, craquelée, suintement au niveau des colliers, traces blanches de calcaire séché, durite dure au toucher.

**Tous les combien changer les durites ?**
Contrôle visuel tous les 2 ans. Remplacement préventif à 100 000 km ou 8 ans. Plus tôt si traces de fissures.

**Peut-on changer une durite soi-même ?**
Oui, opération accessible. Vidanger le circuit, desserrer les colliers, remplacer par une durite identique. Purger le circuit après.

**Quelle erreur éviter avec les durites ?**
Ne pas réutiliser les vieux colliers. Utiliser des colliers neufs adaptés. Vérifier l'absence de pliure après montage.
## Symptomes surchauffe

### Temoin temperature allume
- **Quand** : En roulant ou a l'arret
- **Caracteristique** : Voyant rouge fixe ou clignotant
- **Urgence** : Critique - Arreter immediatement le moteur

### Temperature monte rapidement
- **Quand** : Apres quelques kilometres
- **Caracteristique** : Aiguille dans le rouge en moins de 10 min
- **Urgence** : Haute - Risque joint de culasse

### Chauffage habitacle faible
- **Quand** : Moteur chaud
- **Caracteristique** : Air tiede au lieu de chaud
- **Indication** : Niveau liquide bas ou thermostat bloque

### Fuite liquide de refroidissement
- **Quand** : Vehicule a l'arret
- **Caracteristique** : Flaque verte/orange sous le vehicule
- **Localisation** : Durites, radiateur, pompe a eau

## Symptomes thermostat

### Moteur long a chauffer
- **Quand** : Par temps froid
- **Caracteristique** : Temperature ne monte pas apres 10 km
- **Cause probable** : Thermostat bloque ouvert

### Temperature instable
- **Quand** : En roulant
- **Caracteristique** : Aiguille qui oscille
- **Cause probable** : Thermostat defaillant

## Causes et solutions - Surchauffe

### 1. Niveau liquide insuffisant
- **Probabilite** : 40%
- **Verification** : Niveau vase expansion (moteur froid)
- **Solution** : Completer et chercher la fuite
- **Pieces** : Liquide refroidissement G12/G13
- **Urgence** : Moyenne

### 2. Pompe a eau defaillante
- **Probabilite** : 25%
- **Verification** : Jeu sur axe, fuite par trou temoin
- **Solution** : Remplacement (souvent avec distribution)
- **Pieces** : Pompe a eau
- **Urgence** : Haute

### 3. Thermostat bloque ferme
- **Probabilite** : 20%
- **Verification** : Durite superieure radiateur froide moteur chaud
- **Solution** : Remplacement thermostat
- **Pieces** : Calorstat/thermostat
- **Urgence** : Haute

### 4. Ventilateur HS
- **Probabilite** : 10%
- **Verification** : Ne se declenche pas a 100°C
- **Solution** : Test motoventilateur, fusible, relais
- **Pieces** : Motoventilateur, relais
- **Urgence** : Moyenne

### 5. Radiateur bouche/fuyant
- **Probabilite** : 5%
- **Verification** : Zones froides sur radiateur, traces calcaire
- **Solution** : Rinçage ou remplacement
- **Pieces** : Radiateur
- **Urgence** : Moyenne

## Causes et solutions - Fuites

### 1. Durites percees/craquelees
- **Probabilite** : 35%
- **Verification** : Inspection visuelle, traces blanches
- **Solution** : Remplacement durite
- **Pieces** : Durites refroidissement
- **Urgence** : Moyenne

### 2. Joint de pompe a eau
- **Probabilite** : 25%
- **Verification** : Fuite par trou temoin pompe
- **Solution** : Remplacement pompe complete
- **Pieces** : Pompe a eau
- **Urgence** : Haute

### 3. Bouchon vase expansion
- **Probabilite** : 20%
- **Verification** : Pression circuit (tarage bouchon)
- **Solution** : Remplacement bouchon
- **Pieces** : Bouchon vase expansion
- **Urgence** : Basse

### 4. Joint de culasse
- **Probabilite** : 10%
- **Verification** : Mayonnaise sous bouchon huile, fumee blanche echappement
- **Solution** : Remplacement joint (intervention lourde)
- **Pieces** : Joint de culasse, kit vis
- **Urgence** : Critique

### 5. Radiateur de chauffage
- **Probabilite** : 10%
- **Verification** : Odeur sucree habitacle, buee pare-brise
- **Solution** : Remplacement radiateur chauffage
- **Pieces** : Radiateur de chauffage
- **Urgence** : Moyenne

## Diagnostics complementaires

### Test de pression circuit
- Outil : Pompe de mise en pression
- Pression : 1.2 à 1.5 bar selon vehicule
- But : Detecter fuites non visibles

### Test CO2 dans liquide
- Outil : Testeur de fuite joint culasse
- Indicateur : Changement couleur (bleu → jaune)
- But : Confirmer fuite joint de culasse

## Recommandations

- **Liquide** : Respecter specifications constructeur (G12, G13, type D)
- **Melange** : Ne jamais melanger differents types
- **Vidange** : Tous les 4-5 ans ou 100 000 km
- **Purge** : Obligatoire apres intervention (bulles d'air = surchauffe)
- **Marques** : Valeo, Gates, SKF (pompes), Behr (radiateurs)
