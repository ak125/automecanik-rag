---
category: embrayage
slug: emetteur-d-embrayage
title: Emetteur d'embrayage
pg_id: 234
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
  role: Transmettre la pression hydraulique de la pédale vers le récepteur
  must_be_true:
  - transmettre la pression
  - pousser le liquide
  - convertir l'effort
  must_not_contain:
  - disque
  - volant
  - couple
  - câble
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - kit-d-embrayage
  - butee-d-embrayage
  - volant-moteur
  - recepteur-d-embrayage
  - cable-d-embrayage
  confusion_with:
  - term: piece-d-embrayage-voisine
    difference: Le systeme d embrayage comporte plusieurs pieces (disque, mecanisme, butee, emetteur, recepteur). Verifier
      laquelle est defectueuse.
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
  - ❌ "pression parfaite"
  cost_range:
    min: 40
    max: 150
    currency: EUR
    unit: émetteur
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: Pièce conforme aux préconisations constructeur. Diamètre de piston et course identiques, joints inclus. Recommandé
      sur les véhicules récents ou lorsque la fidélité de la pédale est prioritaire.
  - tier: Équipementier reconnu (embrayage / freinage)
    description: Fabricants spécialisés en composants hydrauliques. Matières des joints compatibles avec les liquides de frein
      DOT 4/DOT 5.1, diamètres conformes aux spécifications.
  - tier: Pièce adaptable
    description: Option économique pour les véhicules anciens. Vérifier impérativement le diamètre de piston (en mm), la longueur
      hors tout et la compatibilité du filetage de raccordement.
  brands:
    premium:
    - LuK
    - Sachs
    standard:
    - Valeo
    - Exedy
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Pedale d embrayage molle ou spongieuse
    severity: confort
  - id: S2
    label: Pedale qui s enfonce jusqu au plancher
    severity: confort
  - id: S3
    label: Niveau liquide frein baisse fuite
    severity: securite
  - id: S4
    label: Fuite liquide sous tableau bord
    severity: confort
  - id: S5
    label: Embrayage qui patine par intermittence
    severity: confort
  - id: S6
    label: Difficulte a debrayer completement
    severity: confort
  causes:
  - identifier origine fuite et verifier joints
  - 'fuite detectee ou niveau bas : identifier origine fuite et verifier joints'
  - 'Usure ou defaillance causant : pedale d embrayage molle ou spongieuse'
  quick_checks:
  - 'Observer : pedale d embrayage molle ou spongieuse ?'
  - 'Observer : pedale qui s enfonce jusqu au plancher ?'
  - 'Observer : niveau liquide frein baisse fuite ?'
  - Fuite liquide sous tableau bord ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Pedale d embrayage molle ou spongieuse
  - Pedale qui s enfonce jusqu au plancher
  - Niveau liquide frein baisse fuite
  - Fuite liquide sous tableau bord
  - Embrayage qui patine par intermittence
  - Difficulte a debrayer completement
  good_practices:
  - Eviter de laisser le pied sur la pedale d embrayage au point mort
  - Remplacement du kit complet (disque + mecanisme + butee)
  - Purge du circuit hydraulique si recepteur/emetteur concerne
  - Verifier le volant moteur lors du remplacement d embrayage
rendering:
  pgId: '234'
  intro_title: A quoi sert Emetteur d'embrayage ?
  risk_title: Pourquoi remplacer Emetteur d'embrayage a temps ?
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
  - question: Émetteur d'embrayage OE ou OES ?
    answer: Les émetteurs OES (Sachs, LuK, Valeo) sont fiables. Certains véhicules ont un émetteur concentrique plus complexe.
      Vérifiez le type exact pour votre véhicule.
  - question: Comment savoir si mon émetteur d'embrayage fuit ?
    answer: Pédale d'embrayage molle ou qui s'enfonce, niveau de liquide de frein qui baisse, tache de liquide sous le tableau
      de bord, embrayage qui patine.
  - question: Faut-il purger après changement d'émetteur ?
    answer: Oui obligatoirement. Le circuit a été ouvert et de l'air est entré. Purge par gravité ou avec purgeur. Utiliser
      du liquide de frein DOT4 neuf.
  - question: Peut-on changer l'émetteur d'embrayage soi-même ?
    answer: Oui, opération accessible. L'émetteur est généralement sous le tableau de bord. La purge demande un assistant
      ou un purgeur automatique.
  - question: Quelle erreur éviter avec l'émetteur d'embrayage ?
    answer: Ne pas mélanger les liquides de frein. Bien purger pour éliminer l'air. Vérifier aussi le récepteur si l'émetteur
      était défaillant.
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
doc_id: 7ac8a510-b4a8-521b-a220-782770fcb54c
content_hash: sha256:29694840b0ab4ed1
lang: fr
variants:
- name: Kit embrayage complet
  aliases:
  - kit complet
  - 3 pieces
  functional_differences:
  - Disque + mecanisme + butee
  - Remplacement recommande en bloc
- name: Kit avec volant moteur
  aliases:
  - kit 4 pieces
  - kit + volant
  functional_differences:
  - Inclut le volant moteur bimasse
  - Pour vehicules diesel modernes
location_on_vehicle:
  area: Entre le moteur et la boite de vitesses
  access: Depose de la boite de vitesses necessaire (pont elevateur)
  adjacent_parts:
  - volant moteur
  - boite de vitesses
  - arbre primaire
installation:
  difficulty: difficile (pro recommande)
  time: 4h a 8h
  tools:
  - pont elevateur
  - cric de boite
  - centreur d embrayage
  - cle dynamometrique
  prerequisite: Depose complete de la boite de vitesses
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: hydraulique
    source_ref: corpus RAG web OEM
  - type: plein
    source_ref: corpus RAG web OEM
  - type: électrique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_11_a: 11 a
    val_12_a: 12 a
    val_13_a: 13 a
    val_15__: 15 %
    val_2__: 2 %
    val_2_a: 2 a
    val_54__: 54 %
    val_6_a: 6 a
    val_8__: 8 %
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: '- Niveau de difficulté : intermédiaire (accès sous véhicule + côté habitacle). - Temps estimé : 1 h 30 à 3 h selon
    l''accessibilité. - Outils : cric + chandelles, clés plates 10-14 mm, clés à tuyauter, seringue de purge, bac de récupération.
    - Consommables : liquide de frein DOT 4 neuf (500 mL à 1 L). - Sécurité : le liquide de frein est corrosif — protégez
    la peinture et rincez tout contact. Véhicule sur chandelles, vitesse au point mort. 🚨 Bruit Emetteur d''embrayage : causes
    et diagnostic Bon à savoir avant de commander : - Il existe deux types d''émetteur : l''émetteur externe (fixé sur la
    cloison pare-feu, actionné par la pédale via une tige) et l''émetteur concentrique (intégré autour de l''arbre primaire
    de boîte, plus courant sur les véhicules récents). Ils ne sont pas interchangeables. - Sur un émetteur concentrique, l''intervention
    nécessite la dépose de la boîte de vitesses — confiez-la à un professionnel. - Vérifiez le niveau de liquide de frein
    avant de démonter : un niveau bas sans fuite visible aux freins pointe vers l''émetteur ou le récepteur d''embrayage.'
  S2: 'L''émetteur d''embrayage n''a pas une période de remplacementprécise. Généralement un émetteur se remplace lorsqu''il
    fuit. Le circuithydraulique se désamorce et la pédale ne transmet plus suffisamment de force àla butée d''embrayage hydraulique.
    Diagnostic complet : identifier une panne de emetteur d''embrayage Symptômes détaillés et vérifications L''émetteur d''embrayage
    défaillant (maître-cylindre d''embrayage) est souvent la cause d''une pédale molle ou sans réaction. Voici comment le
    reconnaître avant que le circuit hydraulique se désamorce complètement : - Pédale d''embrayage molle ou spongieuse : signe
    classique d''un joint interne qui ne retient plus correctement la pression hydraulique — peut indiquer une usure du piston
    émetteur. - Pédale qui s''enfonce jusqu''au plancher : le circuit n''est plus pressurisé, l''embrayage ne débraye plus
    — le véhicule devient difficilement manœuvrable. - Niveau de liquide de frein qui baisse : l''émetteur partage le bocal
    avec le circuit de frein; une baisse inexpliquée du niveau peut révéler une fuite interne ou externe de l''émetteur. -
    Fuite de liquide sous le tableau de bord : une tache humide côté pédale d''embrayage est un signe direct d''une défaillance
    du joint de l''émetteur. - Patinage de l''embrayage par intermittence : une pression hydraulique insuffisante ne dégage
    pas complètement les disques, provoquant un patinage résiduel. - Difficulté à débrayer complètement : les passages de
    vitesses deviennent durs et grincent, même pédale enfoncée à fond. Hypothèses à explorer Ces symptômes peuvent indiquer
    : une usure des joints internes du piston émetteur, une fuite au niveau du raccord ou de la durite, ou une contamination
    du liquide hydraulique. Le remplacement de l''émetteur seul peut suffire si le reste du circuit est sain. Vérifications
    non-invasives (à faire soi-même) - Vérifier le niveau du liquide dans le bocal (repères MIN/MAX) : une baisse sans fuite
    visible côté frein oriente vers l''émetteur d''embrayage. - Inspecter sous le tableau de bord, au-dessus de la pédale
    d''embrayage : une humidité ou un dépôt jaunâtre confirme une fuite de l''émetteur. - Pomper plusieurs fois la pédale
    moteur arrêté : si la fermeté revient temporairement puis disparaît, le joint interne est suspect. - Observer si la pédale
    remonte normalement : une pédale qui ne revient pas en position haute peut indiquer un piston coincé. Pour un diagnostic
    personnalisé adapté à votre véhicule, utilisez notre outil de diagnostic gratuit.'
  S3: '- Émetteur vs récepteur : identifiez lequel est en cause avant de commander. L''émetteur est côté pédale, le récepteur
    côté boîte. - Type de commande : hydraulique (avec conduite) ou à câble (pas de circuit hydraulique). Ce guide concerne
    uniquement la commande hydraulique. - Diamètre du piston : varie selon la motorisation. Vérifiez la référence OEM sur
    la pièce d''origine. - Récepteur concentrique ou externe : le concentrique se monte autour de l''arbre primaire (dépose
    boîte nécessaire), l''externe se fixe sur la cloche. - Longueur de conduite : les conduites pré-remplies simplifient la
    purge. Vérifiez la compatibilité longueur + raccords. Pour aller plus loin : consultez notre guide d''achat emetteur d''embrayage
    — comparatif marques, critères de choix et prix. Causes principales d''usure de l''émetteur d''embrayage - Usure naturelle
    des joints internes — le piston et les joints toriques se dégradent avec le temps et les cycles d''appui pédale. Au-delà
    de 120 000 à 180 000 km, le joint commence à fuir. - Liquide de frein dégradé — le DOT 4 absorbe l''humidité (hygroscopique).
    Un liquide non changé depuis plus de 2 ans corrode les parois internes du cylindre et accélère l''usure des joints. -
    Conduite en appui pédale — garder le pied sur la pédale d''embrayage (en feu rouge par exemple) maintient le piston sous
    pression et use prématurément le joint. - Contamination par particules — un circuit mal purgé ou un bocal sans bouchon
    peut introduire des impuretés qui rayent le cylindre. - Surchauffe du compartiment moteur — l''émetteur étant proche du
    tablier, la chaleur moteur dégrade les joints en caoutchouc sur le long terme. Signe précoce : une micro-fuite apparaît
    souvent sous le tableau de bord (côté conducteur) avant que la pédale ne devienne molle. Inspectez régulièrement cette
    zone.'
  S4_DEPOSE: '📖 Avant de démonter, consultez la fiche technique Émetteur d''embrayage pour connaître les spécifications. Étapes
    de dépose : 1. Vidangez le circuit — aspirez le liquide de frein du réservoir avec une seringue. Placez un bac sous l''émetteur.
    2. Débranchez la batterie — précaution obligatoire avant toute intervention sous le tableau de bord. 3. Déconnectez la
    tige de poussée — retirez la goupille et la rotule reliant l''émetteur à la pédale d''embrayage. 4. Déconnectez la canalisation
    hydraulique — utilisez une clé à tuyauter (évitez les clés plates qui arrondiront le raccord). Bouchez immédiatement les
    orifices pour éviter l''entrée d''air et la perte de liquide. 5. Déposez l''émetteur — selon le montage : 2 vis de fixation,
    ou quart de tour dans le sens horaire avec douille spéciale (montage baïonnette). 6. Nettoyez le logement — retirez les
    résidus de joint et vérifiez l''état de la cloison pare-feu. ⚠️ Attention : le liquide de frein est corrosif pour la peinture.
    Protégez les surfaces et rincez immédiatement tout contact.'
  S4_REPOSE: 'Le remontage de l''émetteur d''embrayage est conditionné par une purge complète du circuit hydraulique : sans
    purge efficace, la pédale reste molle ou s''enfonce jusqu''au plancher malgré un émetteur neuf. Ayez à disposition du
    liquide de frein DOT4 neuf et soit un assistant, soit un purgeur automatique. - Vérifiez que l''émetteur d''embrayage
    neuf est identique à celui déposé : mêmes cotes de l''alésage, même type de raccord hydraulique (union à olive ou à bague
    d''étanchéité). - Contrôlez l''état de la butée d''embrayage hydraulique et du kit d''embrayage : si l''un est usé, remplacez-
    les pendant que la boîte est accessible — un retour en atelier coûte plus cher que le remplacement préventif. - Positionnez
    l''émetteur d''embrayage sur son support sous le tableau de bord. Alignez les trous de fixation avant de serrer les vis.
    - Reconnectez la rotule de pédale d''embrayage sur l''axe de l''émetteur. Vérifiez que la goupille ou la fixation de la
    rotule est bien verrouillée. - Remontez la canalisation hydraulique sur l''émetteur. Serrez le raccord à la main puis
    avec une clé de 11 mm ou un outil à œil adapté, sans serrage excessif (risque de fileter le raccord). - Remplissez le
    réservoir de liquide de frein DOT4 jusqu''au niveau MAX. Ne mélangez pas avec du DOT3 ni avec du liquide usagé. - Purgez
    le circuit hydraulique d''embrayage par la vis de purge du récepteur (cylindre récepteur ou butée concentrique) : appuyez
    sur la pédale, ouvrez la vis, fermez avant de relâcher. Répétez jusqu''à obtenir un jet de liquide sans bulle d''air.
    - Rebranchez la batterie (borne positive en premier). - Contrôlez la fermeté de la pédale d''embrayage : elle doit offrir
    de la résistance dès le début de la course et débloquer la boîte franchement avant mi-course. - Effectuez un essai routier
    en démarrant sur à-plat puis en côte pour confirmer l''absence de patinage et la réponse précise du débrayage. ✅ Après
    remontage, vérifiez les spécifications dans la fiche technique Emetteur d''embrayage.'
  S5: '- Purge incomplète — des bulles d''air résiduelles rendent la pédale spongieuse. Purgez jusqu''à obtenir un flux limpide
    et continu. - Réutiliser l''ancien liquide — le DOT 4 usagé contient de l''humidité qui provoque corrosion interne et
    perte d''efficacité. - Serrage excessif des raccords hydrauliques — les écrous de conduite se déforment facilement. Serrez
    fermement à la clé à tuyauter sans forcer. - Oublier le contacteur de pédale — sur certains véhicules, le démarrage est
    conditionné par ce capteur. Rebranchez-le avant l''essai. - Ignorer l''état de la fourchette — une fourchette usée ou
    tordue empêche le récepteur de transmettre la course correctement. - Laisser le réservoir se vider pendant la purge —
    si le réservoir est commun frein/embrayage, un niveau trop bas désamorce le circuit de freinage. 📖 Fiche technique Emetteur
    d''embrayage — spécifications à vérifier avant montage.'
  S6: '- Course de pédale : ferme, point de débrayage dans le premier tiers, retour complet sans assistance. - Étanchéité
    : aucune trace de liquide aux raccords, à l''émetteur et au récepteur après 10 min moteur tournant. - Passage des vitesses
    : testez toutes les vitesses à l''arrêt moteur tournant. La marche arrière doit s''engager sans craquement. - Essai routier
    : vérifiez le point de patinage, la progressivité du débrayage et l''absence de vibration en démarrage en côte. - Niveau
    de liquide : complétez après l''essai si nécessaire. Le niveau se stabilise après quelques actionnements. 🚨 Bruit Emetteur
    d''embrayage : causes et diagnostic'
  S7: 'Quelle est la différence entre émetteur et récepteur d''embrayage ? L''émetteur (ou maître-cylindre d''embrayage) est
    fixé sur la pédale, côté habitacle. Il convertit l''appui sur la pédale en pression hydraulique. Le récepteur (ou cylindre
    récepteur) est fixé sur la boîte de vitesses — il reçoit cette pression et actionne la fourchette d''embrayage. Une fuite
    sur l''un des deux provoque une pédale molle. Quel est le prix d''un émetteur d''embrayage ? La pièce coûte entre 25 €
    et 120 € selon le véhicule et la marque (LuK, Sachs, Valeo). La main-d''œuvre est de 1 à 2 heures (30 à 100 €). Prévoyez
    aussi 500 mL de liquide de frein DOT 4 pour la purge du circuit, obligatoire après le remplacement. Faut-il purger le
    circuit après le remplacement de l''émetteur ? Oui, obligatoirement. Toute ouverture du circuit hydraulique d''embrayage
    introduit de l''air. Sans purge, la pédale reste molle ou spongieuse. La purge se fait comme un circuit de frein : bocal
    plein → pédale pompée → vis de purge ouverte sur le récepteur → fermer quand le liquide coule sans bulle. Peut-on rouler
    avec un émetteur d''embrayage qui fuit ? C''est fortement déconseillé. Une fuite progressive vide le réservoir de liquide
    de frein (partagé avec le freinage sur certains véhicules). Vous risquez de ne plus pouvoir débrayer en roulant, rendant
    l''arrêt du véhicule dangereux. Remplacez dès les premiers signes de fuite. Pièces associées à l''émetteur d''embrayage
    : - Kit d''embrayage (disque + mécanisme + butée) — à contrôler si le kilométrage dépasse 120 000 km. - Conduite hydraulique
    — remplacez si rigide, fissurée ou gonflée sous pression. - Liquide de frein DOT 4 — 500 mL à 1 L pour la purge complète
    du circuit. - Fourchette d''embrayage — vérifiez l''usure du point de contact avec le récepteur. - Joint de passe-cloison
    — peut être endommagé lors de la dépose de l''émetteur. 📖 Fiche technique Emetteur d''embrayage — intervalles et spécifications
    d’entretien.'
  S8: '- Faut-il changer émetteur et récepteur ensemble ? Pas obligatoirement, mais si l''un fuit, l''autre a souvent le même
    âge et les mêmes joints fatigués. Le remplacement simultané évite une seconde intervention. - Peut-on rouler avec un émetteur
    qui fuit ? Temporairement en complétant le niveau, mais le risque de perte totale d''embrayage est réel. Intervention
    à prévoir rapidement. - DOT 3 ou DOT 4 ? Le DOT 4 est le standard actuel. Vérifiez la préconisation constructeur sur le
    bouchon du réservoir. - La purge est-elle indispensable ? Oui, systématiquement. Toute ouverture du circuit introduit
    de l''air qui rend la commande inefficace. - Récepteur concentrique : faut-il déposer la boîte ? Oui. Le récepteur concentrique
    se monte autour de l''arbre primaire, ce qui impose la dépose de la boîte de vitesses. Prévoyez 4 à 6 h de main-d''œuvre.
    📖 Pour plus de détails techniques : fiche Emetteur d''embrayage'
  META: '{"og_title": "Émetteur d''embrayage : guide remplacement et purge", "meta_title": "Émetteur d''embrayage : pédale
    molle, diagnostic et prix | AutoMecanik", "gate_report": "PASS", "schema_type": "Article", "og_description": "Pédale molle
    ou qui s''enfonce ? L''émetteur d''embrayage fuit peut-être. Symptômes, purge et remplacement.", "primary_intent": "diagnostic",
    "char_count_desc": 136, "char_count_title": 57, "meta_description": "Pédale d''embrayage molle ou qui s''enfonce ? L''émetteur
    fuit peut-être. Guide : symptômes, purge du circuit hydraulique et remplacement."}'
---

# Emetteur d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre la pression hydraulique de la pédale vers le récepteur

**Actions principales:** transmettre la pression, pousser le liquide, convertir l'effort, envoyer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Niveau liquide frein baisse fuite**
  niveau liquide frein baisse fuite

### 🟢 Autres Symptômes

- pedale d embrayage molle ou spongieuse
- pedale qui s enfonce jusqu au plancher
- fuite liquide sous tableau bord
- embrayage qui patine par intermittence
- difficulte a debrayer completement

## Procédure de Diagnostic

Pour diagnostiquer un problème de emetteur d'embrayage:

1. **Inspection visuelle** - Examiner l'état du emetteur d'embrayage
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

- butee-d-embrayage
- kit-d-embrayage
- recepteur-d-embrayage

## Critères de Compatibilité

Pour commander le bon emetteur d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "pression parfaite"

## FAQ

**Émetteur d'embrayage OE ou OES ?**
Les émetteurs OES (Sachs, LuK, Valeo) sont fiables. Certains véhicules ont un émetteur concentrique plus complexe. Vérifiez le type exact pour votre véhicule.

**Comment savoir si mon émetteur d'embrayage fuit ?**
Pédale d'embrayage molle ou qui s'enfonce, niveau de liquide de frein qui baisse, tache de liquide sous le tableau de bord, embrayage qui patine.

**Faut-il purger après changement d'émetteur ?**
Oui obligatoirement. Le circuit a été ouvert et de l'air est entré. Purge par gravité ou avec purgeur. Utiliser du liquide de frein DOT4 neuf.

**Peut-on changer l'émetteur d'embrayage soi-même ?**
Oui, opération accessible. L'émetteur est généralement sous le tableau de bord. La purge demande un assistant ou un purgeur automatique.

**Quelle erreur éviter avec l'émetteur d'embrayage ?**
Ne pas mélanger les liquides de frein. Bien purger pour éliminer l'air. Vérifier aussi le récepteur si l'émetteur était défaillant.
## Symptomes courants

### Pedale d'embrayage dure
- **Quand** : A chaque actionnement
- **Caracteristique** : Resistance excessive, fatigue musculaire

### Pedale molle ou spongieuse
- **Quand** : Constant
- **Caracteristique** : Course excessive, point de patinage haut

### Patinage embrayage
- **Quand** : En acceleration forte, en cote
- **Caracteristique** : Regime moteur monte sans acceleration proportionnelle

### Bruit au debrayage
- **Quand** : Appui sur la pedale
- **Caracteristique** : Grincement, sifflement, claquement

### Difficulte passage vitesses
- **Quand** : A froid ou constant
- **Caracteristique** : Craquements, resistance

## Causes possibles et solutions

### 1. Disque d'embrayage use
- **Probabilite** : 50%
- **Verification** : Patinage, kilometrage eleve
- **Solution** : Remplacement kit embrayage complet
- **Pieces** : Kit embrayage (disque, mecanisme, butee)
- **Urgence** : Moyenne a haute

### 2. Butee hydraulique/mecanique HS
- **Probabilite** : 25%
- **Verification** : Bruit a l'appui pedale, fuite liquide
- **Solution** : Remplacement butee
- **Pieces** : Butee d'embrayage
- **Urgence** : Moyenne

### 3. Volant moteur bimasse HS
- **Probabilite** : 15%
- **Verification** : Vibrations excessives, claquements au ralenti
- **Solution** : Remplacement volant moteur
- **Pieces** : Volant moteur bimasse ou conversion simple masse
- **Urgence** : Moyenne

### 4. Emetteur/recepteur d'embrayage defaillant
- **Probabilite** : 10%
- **Verification** : Pedale molle, fuite liquide
- **Solution** : Remplacement cylindre emetteur ou recepteur
- **Pieces** : Emetteur, recepteur, liquide de frein
- **Urgence** : Moyenne

## Duree de vie embrayage

| Utilisation | Duree de vie |
|-------------|--------------|
| Autoroute | 150 000 - 200 000 km |
| Mixte | 100 000 - 150 000 km |
| Urbaine | 80 000 - 120 000 km |
| Agressive | 50 000 - 80 000 km |

## Recommandations

- **Kit complet** : Toujours remplacer disque + mecanisme + butee ensemble
- **Volant moteur** : Controler systematiquement le volant lors du changement
- **Marques** : Privilegier Valeo, LuK, Sachs
- **Conduite** : Eviter de garder le pied sur la pedale d'embrayage
