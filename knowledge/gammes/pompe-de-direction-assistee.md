---
category: direction
slug: pompe-de-direction-assistee
title: Pompe de direction assistée
pg_id: 12
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
  role: Fournir la pression hydraulique pour assister l'effort de braquage - Reduit l'effort au volant
  must_be_true:
  - assister
  - fournir la pression
  - alimenter
  must_not_contain:
  - suspension
  - amortisseur
  - electrique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - cremailliere-de-direction
  - rotule-de-direction
  - barre-de-direction
  - soufflet-de-direction
  - colonne-de-direction
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
  - ❌ "securite garantie"
  cost_range:
    min: 211
    max: 467
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
    - Lemforder
    - TRW
    standard:
    - Febi
    - Meyle
    - MOOG
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Bruit grognement gemissement tournant volant
    severity: confort
  - id: S2
    label: Direction dure en man uvre a basse vitesse
    severity: securite
  - id: S3
    label: Sifflement aigu au demarrage qui s attenue
    severity: confort
  - id: S4
    label: Mousse ou bulles dans le bocal de liquide
    severity: confort
  - id: S5
    label: Fuite de liquide au niveau de la pompe
    severity: confort
  - id: S6
    label: Niveau de liquide qui baisse regulierement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  quick_checks:
  - Bruit grognement gemissement tournant volant ?
  - 'Observer : direction dure en man uvre a basse vitesse ?'
  - 'Observer : sifflement aigu au demarrage qui s attenue ?'
  - 'Observer : mousse ou bulles dans le bocal de liquide ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Bruit grognement gemissement tournant volant
  - Direction dure en man uvre a basse vitesse
  - Sifflement aigu au demarrage qui s attenue
  - Mousse ou bulles dans le bocal de liquide
  - Fuite de liquide au niveau de la pompe
  - Niveau de liquide qui baisse regulierement
  good_practices:
  - Controle du jeu de direction a chaque revision
  - Verifier les soufflets de protection (pas de fuite de graisse)
  - Faire verifier la geometrie apres remplacement
  - Inspecter les biellettes et rotules associees
rendering:
  pgId: '12'
  intro_title: A quoi sert Pompe de direction assistée ?
  risk_title: Pourquoi remplacer Pompe de direction assistée a temps ?
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
  - question: Pompe de direction assistée OE ou échange standard ?
    answer: L'échange standard est économique et fiable. Vérifiez la compatibilité exacte (nombre de gorges poulie, type de
      raccords).
  - question: Comment savoir si ma pompe de direction assistée est HS ?
    answer: Bruit de grognement ou sifflement au volant, direction dure surtout en manœuvre, mousse dans le bocal de liquide.
  - question: Tous les combien changer la pompe de direction assistée ?
    answer: Entre 150 000 et 250 000 km. Changer le liquide tous les 100 000 km prolonge sa durée de vie.
  - question: Peut-on changer la pompe de direction assistée soi-même ?
    answer: Oui, opération accessible. Détendre la courroie, débrancher les durites, déposer la pompe. Purge obligatoire après.
  - question: Quelle erreur éviter avec la pompe de direction assistée ?
    answer: Ne pas rouler sans liquide (détruit la pompe en quelques minutes). Bien purger le circuit après remplacement.
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
doc_id: ee4fdaeb-c2fd-5f53-96b3-e5572e989fb4
content_hash: sha256:09309929e50af506
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
  area: Sous le vehicule, relie le volant aux roues
  access: Par le dessous (pont elevateur recommande)
  adjacent_parts:
  - cremailliere
  - biellette
  - rotule
  - soufflet
installation:
  difficulty: difficile
  time: 1h a 3h
  tools:
  - cle a douille
  - arrache-rotule
  - cle dynamometrique
  prerequisite: Pont elevateur, geometrie a refaire apres
phase5_enrichment:
  _source: automotive.hutchinson.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  technical_notes:
    norme_iso_9981: 'ISO 9981'
    val_000_km: '000 km'
    val_135__c: '135 °C'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La pompe de direction assistee fournit la pression hydraulique necessaire au
    boitier de direction pour reduire l'effort de braquage du volant. Elle est
    entrainee par la courroie d'accessoire a partir de la poulie de vilebrequin.
    Types de pompes : - Pompe hydraulique a palettes : la plus repandue,
    entrainee mecaniquement par la courroie- Pompe electro-hydraulique : moteur
    electrique integre, independante du regime moteur- Direction assistee
    electrique (EPAS) : pas de pompe hydraulique, un moteur electrique assiste
    directement la cremaillere Pieces liees : cremaillere de direction, courroie
    d'accessoire, durite haute pression de direction, reservoir de liquide de
    direction.
  S2: >-
    Ne pas attendre la panne complete pour intervenir. Symptômes d'usure : -
    Bruit grognement gemissement tournant volant - Direction dure en man uvre a
    basse vitesse - Sifflement aigu au demarrage qui s attenue - Mousse ou
    bulles dans le bocal de liquide - Fuite de liquide au niveau de la pompe -
    Niveau de liquide qui baisse regulierement
  S3: >-
    Pour choisir les bons pompe de direction assistee pour votre véhicule : -
    Marque de votre véhicule - Modele de votre véhicule - Annee de votre
    véhicule - Vérifier : bruit grognement gemissement tournant volant -
    Vérifier : direction dure en man uvre a basse vitesse - Vérifier :
    sifflement aigu au demarrage qui s attenue - Vérifier : mousse ou bulles
    dans le bocal de liquide - Vérifier : fuite de liquide au niveau de la pompe
    - Vérifier : niveau de liquide qui baisse regulierement - Vérifier :
    Direction dure en man uvre a basse vitessePour aller plus loin : consultez
    notre guide d'achat pompe de direction assistée — comparatif marques,
    critères de choix et prix.
  S4_DEPOSE: >-
    1. Debrancher la batterie. 2. Placer un bac de recuperation sous la pompe —
    le liquide hydraulique coule a la deconnexion des durites. 3. Detendre la
    courroie d'accessoire via le galet tendeur et la retirer de la poulie de la
    pompe. 4. Deconnecter les durites haute pression et retour (cle a fourche,
    ne pas utiliser de pince) — obturer immediatement les raccords pour eviter
    l'entree d'air. 5. Devisser les vis de fixation de la pompe sur le support
    moteur (2 a 3 vis selon vehicule). 6. Deposer la pompe en degageant la
    poulie du passage de courroie. 7. Si la poulie est reutilisee : la demonter
    avec un extracteur adapte (ne jamais frapper au marteau).
  S4_REPOSE: >-
    Le remontage de la pompe de direction assistée implique obligatoirement une
    purge complète du circuit hydraulique après repose. Sans purge, les bulles
    d'air dans le circuit provoquent un grincement caractéristique au braquage
    et accélèrent l'usure de la pompe neuve. Ne jamais démarrer le moteur sans
    s'assurer que le bocal de liquide de direction est au niveau maximum. -
    Contrôler la conformité de la pompe neuve — Comparer la pompe de direction
    assistée neuve avec celle déposée : nombre de gorges de la poulie, type et
    diamètre des raccords hydrauliques (haute pression et retour basse
    pression), sens de rotation. Une pompe d'échange standard doit correspondre
    exactement en termes de raccords et de poulie. - Inspecter les rotules de
    direction et la crémaillère — Contrôler l'absence de jeu dans les rotules de
    direction et vérifier l'état de la crémaillère de direction : fuites de
    soufflet, jeu dans le boîtier. Profiter de l'accès au circuit de direction
    pour signaler ou traiter ces défaillances. - Contrôler l'état de la courroie
    d'accessoires — Inspecter la courroie d'accessoires sur toute sa longueur :
    craquelures, usure des flancs, effilochage. Si la courroie approche de son
    kilométrage de remplacement (généralement 120 000 à 150 000 km), la
    remplacer maintenant pendant que l'accès est dégagé. - Monter la pompe et
    graisser les fixations — Positionner la pompe de direction assistée sur son
    support. Appliquer un filet de frein-filet ou graisser les fixations pour
    éviter le grippage. Serrer les boulons de fixation progressivement sans
    serrage définitif pour permettre le positionnement de la courroie. -
    Reconnecter les canalisations hydrauliques — Brancher la canalisation haute
    pression et la canalisation de retour basse pression sur leurs raccords
    respectifs de la pompe. Serrer les raccords banjo ou unions à la clé
    dynamométrique. Un raccord insuffisamment serré fuit sous la pression du
    circuit direction (jusqu'à 100 bars en plein braquage). - Remonter et tendre
    la courroie d'accessoires — Engager la courroie d'accessoires sur toutes les
    poulies dans l'ordre correct. Régler la tension : la courroie doit présenter
    un léger fléchissement (environ 10 mm sous pression du pouce) sur le brin le
    plus long. Serrer définitivement les fixations de la pompe une fois la
    tension correcte obtenue. - Remonter le cache de protection — Remettre en
    place le cache de protection de la pompe si le véhicule en est équipé.
    Vérifier que les fixations sont bien serrées. - Remplir le bocal de liquide
    de direction — Verser du liquide de direction assistée neuf (spécification
    constructeur — ne pas utiliser du liquide ATF universel sans vérification)
    jusqu'au repère MAX du bocal. Le bocal doit être plein avant tout démarrage.
    - Purger le circuit et rebrancher la batterie — Rebrancher la batterie.
    Démarrer le moteur. Sans rouler, braquer les roues à fond de gauche à droite
    plusieurs fois lentement pour chasser les bulles d'air du circuit. Contrôler
    le niveau dans le bocal entre chaque rotation et compléter si nécessaire.
    Recommencer jusqu'à ce que le niveau soit stable et que le braquage soit
    silencieux. - Essai routier et contrôle final — Effectuer un essai routier
    incluant des manœuvres lentes pour confirmer l'absence de grincement ou de
    dureté anormale au braquage. Vérifier après l'essai l'absence de fuite
    autour des raccords et le niveau de liquide dans le bocal.
  S5: >-
    Erreurs frequentes avec la pompe de direction assistee : - Rouler avec un
    niveau d'huile de direction bas — la pompe aspire de l'air, cavite et s'use
    prematurement. Verifier le niveau regulierement- Utiliser une huile
    hydraulique non conforme — chaque constructeur preconise un type d'huile
    specifique (ATF, CHF, LHM), les melanger degrade les joints internes-
    Ignorer un sifflement ou un gemissement en braquant — signe de pompe en fin
    de vie ou de niveau d'huile bas- Ne pas verifier l'etat de la courroie
    d'accessoire — une courroie detendue fait patiner la poulie de la pompe et
    reduit la pression hydraulique- Oublier de purger le circuit hydraulique
    apres remplacement — l'air dans le circuit provoque un fonctionnement
    saccade et bruyant de la direction- Ne pas inspecter les durites haute
    pression et le boitier de direction — une fuite en aval de la pompe provoque
    les memes symptomes qu'une pompe defaillante
  S6: >-
    Contrôles statiques (moteur tournant)- Vérifier le niveau de liquide dans le
    réservoir après purge (entre MIN et MAX, moteur chaud)- Inspecter tous les
    raccords : aucune fuite de liquide haute pression ou retour- Écouter le
    bruit de la pompe : un ronronnement sourd est normal, un gémissement aigu
    indique de l'air dans le circuit- Vérifier la tension de la courroie
    accessoire (pas de patinage au braquage)Test routier progressif- Manœuvrer à
    l'arrêt : la direction doit être légère et homogène de butée à butée- Rouler
    à 50 km/h : pas de durcissement de la direction ni de vibration dans le
    volant- Effectuer des créneaux : assistance constante, sans à-coup ni bruit
    anormal- Après 100 km, recontrôler le niveau de liquide et l'absence de
    fuites⚠️ Important : Un gémissement persistant après purge complète peut
    indiquer une prise d'air sur un raccord ou une durite d'aspiration poreuse.
    Ne pas ignorer ce bruit — la pompe s'usera prématurément.
  S_GARAGE: >-
    Nous vous recommandons de confier cette intervention à un professionnel : -
    Plusieurs causes possibles de défaillance (4 identifiées) nécessitent un
    diagnostic professionnel Un garagiste qualifié dispose de l'outillage et de
    l'expérience nécessaires pour effectuer cette opération en toute sécurité.
  S7: >-
    Quel est le prix d'un pompe de direction assistée ?Le prix varie selon le
    véhicule et la marque. Utilisez notre sélecteur pour trouver le pompe de
    direction assistée compatible avec votre véhicule et comparer les tarifs des
    différents équipementiers.Comment savoir si mon pompe de direction assistée
    est à changer ?Les signes d'usure les plus courants sont détaillés dans la
    section diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par
    un professionnel.Peut-on rouler avec un pompe de direction assistée
    défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la
    pièce dans la sécurité du véhicule. Consultez la section symptômes pour
    évaluer l'urgence du remplacement.- colonne de direction - courroie d
    accessoire - cremailliere de direction - poulie vilebrequin - rotule de
    direction - rotule de suspension
  S8: >-
    Pompe de direction assistée OE ou échange standard ?L'échange standard est
    économique et fiable. Vérifiez la compatibilité exacte (nombre de gorges
    poulie, type de raccords). Comment savoir si ma pompe de direction assistée
    est HS ?Bruit de grognement ou sifflement au volant, direction dure surtout
    en manœuvre, mousse dans le bocal de liquide. Tous les combien changer la
    pompe de direction assistée ?Entre 150 000 et 250 000 km. Changer le liquide
    tous les 100 000 km prolonge sa durée de vie. Peut-on changer la pompe de
    direction assistée soi-même ?Oui, opération accessible. Détendre la
    courroie, débrancher les durites, déposer la pompe. Purge obligatoire après.
    Quelle erreur éviter avec la pompe de direction assistée ?Ne pas rouler sans
    liquide (détruit la pompe en quelques minutes). Bien purger le circuit après
    remplacement.
  META: >-
    Remplacement pompe de direction assistée : compatibilité, purge du circuit,
    erreurs à éviter et FAQ. Guide technique complet avec vérifications.
---

# Pompe de direction assistée - Guide Diagnostic Complet

## Fonction et Rôle

Fournir la pression hydraulique pour assister l'effort de braquage - Reduit l'effort au volant

**Actions principales:** assister, fournir la pression, alimenter, reduire l'effort

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Direction dure en man uvre a basse vitesse**
  direction dure en man uvre a basse vitesse

### 🟢 Autres Symptômes

- bruit grognement gemissement tournant volant
- sifflement aigu au demarrage qui s attenue
- mousse ou bulles dans le bocal de liquide
- fuite de liquide au niveau de la pompe
- niveau de liquide qui baisse regulierement

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe de direction assistée:

1. **Inspection visuelle** - Examiner l'état du pompe de direction assistée
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
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

- colonne-de-direction
- courroie-d-accessoire
- cremailliere-de-direction
- poulie-vilebrequin
- rotule-de-direction
- rotule-de-suspension

## Critères de Compatibilité

Pour commander le bon pompe de direction assistée, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"

## FAQ

**Pompe de direction assistée OE ou échange standard ?**
L'échange standard est économique et fiable. Vérifiez la compatibilité exacte (nombre de gorges poulie, type de raccords).

**Comment savoir si ma pompe de direction assistée est HS ?**
Bruit de grognement ou sifflement au volant, direction dure surtout en manœuvre, mousse dans le bocal de liquide.

**Tous les combien changer la pompe de direction assistée ?**
Entre 150 000 et 250 000 km. Changer le liquide tous les 100 000 km prolonge sa durée de vie.

**Peut-on changer la pompe de direction assistée soi-même ?**
Oui, opération accessible. Détendre la courroie, débrancher les durites, déposer la pompe. Purge obligatoire après.

**Quelle erreur éviter avec la pompe de direction assistée ?**
Ne pas rouler sans liquide (détruit la pompe en quelques minutes). Bien purger le circuit après remplacement.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/direction-cremaillere.md 2026-02-15 -->
### Diagnostic - Direction et crémaillère

# Direction et crémaillère - Diagnostic complet

## Symptômes au volant

### Volant dur
- **Direction assistée défaillante** : Pompe DA qui siffle ou ne fournit plus assez de pression. Vérifier le niveau de liquide DA et l'état de la courroie.
- **Crémaillère grippée** : Corrosion interne ou manque de lubrification. Le volant est dur dans les deux sens, surtout à froid.
- **Colonne de direction usée** : Cardan de direction grippé, surtout après un long stationnement.

### Jeu dans le volant
- **Rotules de direction usées** : Jeu perceptible en tournant le volant sans que les roues bougent. Contrôler visuellement le jeu en secouant la roue.
- **Biellettes de direction desserrées** : Claquement en manœuvrant, jeu latéral au volant.
- **Crémaillère avec jeu interne** : Usure des pignons ou des bagues de guidage.

### Bruits en braquant
- **Craquement dans les virages** : Soufflet de cardan déchiré, graisse partie, croisillon usé.
- **Grincement à basse vitesse** : Roulements de butée d'amortisseur ou coupelles supérieures usées.
- **Sifflement continu** : Pompe de direction assistée en fin de vie ou niveau de liquide bas.

## Fuites de direction

### Fuite de liquide DA
- **Au niveau du bocal** : Joint de bouchon ou bocal fissuré.
- **Sur les raccords** : Durites de pression ou retour qui fuient aux colliers.
- **Sur la crémaillère** : Joints spy de crémaillère usés, fuite visible aux soufflets.

## Vérifications simples

- Contrôler le niveau de liquide de direction assistée (bocal sous le capot)
- Inspecter les soufflets de crémaillère (pas de déchirure, pas de fuite)
- Secouer la roue à 9h-15h pour détecter le jeu dans les rotules
- Tourner le volant moteur allumé : le mouvement doit être fluide et silencieux

## Quand consulter un professionnel

- Volant qui vibre ou tire d'un côté en ligne droite
- Bruit métallique constant dans la direction
- Fuite importante de liquide DA (risque de blocage)
- Jeu excessif au volant détecté au contrôle technique
