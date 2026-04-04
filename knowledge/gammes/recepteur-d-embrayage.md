---
category: embrayage
slug: recepteur-d-embrayage
title: Récepteur d'embrayage
pg_id: 620
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
  role: Recevoir la pression hydraulique et actionner la butée ou la fourchette
  must_be_true:
  - recevoir la pression
  - actionner la butée
  - pousser la fourchette
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
  - emetteur-d-embrayage
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
  - ❌ "action parfaite"
  cost_range:
    min: 26
    max: 165
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
    label: Fuite de liquide visible sous la boite de vitesses
    severity: confort
  - id: S3
    label: Bruit de grincement au niveau de la fourchette
    severity: confort
  - id: S4
    label: Odeur de liquide de frein brule sous la voiture
    severity: securite
  - id: S5
    label: Embrayage qui ne debraye plus piston bloque
    severity: immobilisation
  - id: S6
    label: Plus de 150 000 km sans verification du circuit
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - identifier origine fuite et verifier joints
  - remplacement preventif recommande
  depose_steps: []
  quick_checks:
  - 'Observer : pedale d embrayage molle ou spongieuse ?'
  - Fuite de liquide visible sous la boite de vitesses ?
  - Bruit de grincement au niveau de la fourchette ?
  - Odeur de liquide de frein brule sous la voiture ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Pedale d embrayage molle ou spongieuse
  - Fuite de liquide visible sous la boite de vitesses
  - Bruit de grincement au niveau de la fourchette
  - Odeur de liquide de frein brule sous la voiture
  - Embrayage qui ne debraye plus piston bloque
  - Plus de 150 000 km sans verification du circuit
  good_practices:
  - Eviter de laisser le pied sur la pedale d embrayage au point mort
  - Remplacement du kit complet (disque + mecanisme + butee)
  - Purge du circuit hydraulique si recepteur/emetteur concerne
  - Verifier le volant moteur lors du remplacement d embrayage
rendering:
  pgId: '620'
  intro_title: A quoi sert Récepteur d'embrayage ?
  risk_title: Pourquoi remplacer Récepteur d'embrayage a temps ?
  risk_explanation: '**Pièce HS** - Le récepteur d''embrayage peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le récepteur d''embrayage peut être hors service et nécessiter un remplacement'
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
  - question: Récepteur d'embrayage OE ou OES ?
    answer: Les récepteurs OES (Sachs, LuK, Valeo) sont fiables. Pour un récepteur concentrique (CSC), privilégiez l'OE ou
      un kit embrayage complet incluant le CSC.
  - question: Comment savoir si mon récepteur d'embrayage fuit ?
    answer: Pédale molle ou qui s'enfonce, fuite de liquide sous la boîte de vitesses, niveau de liquide de frein qui baisse,
      embrayage qui ne débraye plus.
  - question: Faut-il purger après changement de récepteur ?
    answer: Oui obligatoirement. Purge par le purgeur situé sur le récepteur. Utiliser du liquide DOT4 neuf. Vérifier l'absence
      de bulles d'air.
  - question: Peut-on changer le récepteur d'embrayage soi-même ?
    answer: 'Le récepteur externe oui (sous la voiture). Le récepteur concentrique nécessite de déposer la boîte : autant
      changer l''embrayage en même temps.'
  - question: Quelle erreur éviter avec le récepteur d'embrayage ?
    answer: Ne pas forcer sur le piston. Bien purger pour éliminer tout l'air. Vérifier l'émetteur si le récepteur fuyait.
      Remplacer le CSC avec l'embrayage.
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
doc_id: 564a76d1-b7a3-5481-813d-fb1c8d4391df
content_hash: sha256:e6faf6048dd44e73
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
  - type: composite
    source_ref: corpus RAG web OEM
  - type: céramique
    source_ref: corpus RAG web OEM
  - type: hydraulique
    source_ref: corpus RAG web OEM
  - type: pneumatique
    source_ref: corpus RAG web OEM
  - type: rainuré
    source_ref: corpus RAG web OEM
  - type: électrique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_20_a: 20 a
    val_5_a: 5 a
  materials:
  - materiau: céramique
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Lorsque le conducteur appui sur la pédale d''embrayage, l''émetteur transmetla pression du liquide hydraulique au récepteur
    d''embrayage complémentaire del''émetteur d''embrayage qui permet la transmission de la force exercée par le conducteursur
    la pédale d''embrayage. Le récepteur d''embrayage est composé d''un cylindre à l''intérieur duquelcoulisse un piston relié
    à une tige qui pousse la fourchette d''embrayage , pour actionnerla butée d''embrayage hydraulique qui déclenche le débrayage.
    Lorsque vous relâchez lapédale l''effet inverse se produit. En savoir plus : récepteur d''embrayage — définition et rôle
    mécanique 🚨 Bruit Récepteur d''embrayage : causes et diagnostic'
  S2: 'Ne pas attendre la panne complete pour intervenir. Symptômes d''usure : - pedale d embrayage molle ou spongieuse -
    fuite de liquide visible sous la boite de vitesses - bruit de grincement au niveau de la fourchette - odeur de liquide
    de frein brule sous la voiture - embrayage qui ne debraye plus piston bloque - plus de 150 000 km sans verification du
    circuit - **Embrayage qui ne debraye plus piston bloque** - **Bruit de grincement au niveau de la fourchette** - **Odeur
    de liquide de frein brule sous la voiture** Symptômes détaillés et vérifications Un récepteur d''embrayage défaillant
    se signale généralement par des signes hydrauliques ou mécaniques. Voici les symptômes à surveiller : - Pédale d''embrayage
    molle ou spongieuse : lorsque le piston du récepteur ne maintient plus la pression, la pédale perd sa fermeté — signe
    d''une fuite interne ou d''un joint dégradé. - Fuite de liquide visible sous la boîte de vitesses : une tache de liquide
    ambré ou jaunâtre sous le véhicule côté boîte est un indicateur direct d''une fuite récepteur. - Bruit de grincement au
    niveau de la fourchette : un récepteur en fin de course ou mal alimenté peut ne plus actionner correctement la fourchette,
    générant des bruits métalliques. - Odeur de liquide de frein chaud : une fuite sur le récepteur peut projeter du liquide
    sur des pièces chaudes, produisant une odeur caractéristique sous le véhicule. - Embrayage qui ne débraye plus (piston
    bloqué) : un récepteur dont le piston est grippé ou bloqué empêche toute manœuvre d''embrayage — situation qui impose
    l''arrêt du véhicule. - Kilométrage élevé sans vérification : au-delà de 150 000 km, une inspection préventive du circuit
    hydraulique est justifiée. Hypothèses à explorer Ces symptômes peuvent indiquer : une usure du joint de piston interne,
    une corrosion du cylindre récepteur, une durite de raccordement percée, ou un piston grippé par dépôt de boue hydraulique.
    Le récepteur et l''émetteur sont souvent remplacés ensemble pour fiabiliser le circuit. Vérifications non-invasives (à
    faire soi-même) - Vérifier le niveau de liquide de frein dans le bocal : une baisse non justifiée par le circuit de frein
    oriente vers une fuite du circuit embrayage. - Inspecter visuellement le récepteur accessible depuis le dessous du véhicule
    : chercher des traces de liquide ou de corrosion sur le corps du cylindre. - Tester la fermeté de la pédale : une pédale
    qui s''améliore après purge du circuit mais redevient molle rapidement indique une fuite active. - Contrôler l''état de
    la durite de raccordement entre émetteur et récepteur : des craquelures ou un gonflement de la durite sont des signes
    précurseurs de rupture. Pour un diagnostic personnalisé adapté à votre véhicule, utilisez notre outil de diagnostic gratuit.'
  S3: 'Le récepteur d''embrayage convertit la pression hydraulique transmise par l''émetteur en déplacement mécanique de la
    butée ou de la fourchette d''embrayage. Sa course de piston et son alésage sont calculés au millimètre pour le mécanisme
    d''embrayage du véhicule : un récepteur avec un rapport de surface de piston différent modifie la force de débrayage et
    la hauteur de pédale, rendant l''embrayage difficile à doser ou à fond de course avant séparation complète. - Type : récepteur
    externe ou butée hydraulique concentrique (CSC) — Le récepteur externe est fixé sur le carter de boîte et agit par fourchette
    ; la butée concentrique (Concentric Slave Cylinder) est montée à l''intérieur du carter d''embrayage directement sur l''arbre
    d''entrée de boîte. Ces deux solutions ne sont pas interchangeables et nécessitent une dépose partielle ou totale de la
    boîte selon le cas. - Alésage du cylindre et course de piston — L''alésage (diamètre interne) détermine la force exercée
    par la même pression hydraulique. Les alésages courants vont de 19 mm à 31,75 mm (3/4 po à 1 po 1/4). Une variation de
    3 mm sur l''alésage modifie la force de débrayage de plus de 25 %, rendant la pédale trop lourde ou insuffisamment puissante.
    - Longueur de la tige de poussée et course totale — La longueur de la tige doit permettre un jeu résiduel de la fourchette
    conforme aux préconisations constructeur (généralement 2 à 4 mm de jeu à froid). Une tige trop courte laisse la butée
    en contact permanent avec le mécanisme, accélérant son usure. - Raccord hydraulique : filetage et diamètre du tuyau —
    Le raccord banjo ou droit à visser doit correspondre au pas de vis (M10x1 le plus courant) et à l''angle de sortie du
    tuyau hydraulique existant. Un raccord mal orienté contraint le tuyau en flexion et favorise les fissures sous pression.
    - Matériau du corps et du piston — Les récepteurs en aluminium anodisé ont une durée de vie supérieure aux corps plastique
    sur les circuits soumis à des températures élevées (boîtes proches de la ligne d''échappement). Le piston en aluminium
    ou en acier inoxydable résiste mieux aux dépôts de liquide de frein dégradé. - Purge du circuit et compatibilité du liquide
    de frein — Le circuit hydraulique d''embrayage partage généralement le liquide DOT 4 avec le circuit de freinage. Vérifier
    la préconisation constructeur (DOT 4 ou DOT 5.1) et purger intégralement le circuit après remplacement pour éliminer les
    bulles d''air responsables d''une pédale spongieuse. - Remplacement simultané recommandé — Lors d''une intervention sur
    le récepteur, contrôler l''état de l''émetteur d''embrayage (cylindre maître) et du tuyau hydraulique. Remplacer le kit
    complet émetteur/récepteur si le kilométrage dépasse 150 000 km, car le démontage fragilise les joints vieillis de l''émetteur.
    Pour aller plus loin : consultez notre guide d''achat récepteur d''embrayage — comparatif marques, critères de choix et
    prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Récepteur d'embrayage pour connaître les spécifications. -
    Vidangez le circuit hydraulique de l'embrayage. - Débranchez la batterie. - Démontez la boîte de vitesses (selon laversion
    de la boîte de vitesses). - Démontez les vis de fixations du récepteurd'embrayage sur la butée (selon la version de la
    boîte de vitesses). - Démontez la canalisation hydraulique durécepteur d'embrayage (selon la version de la boîte de vitesses).
    - Démontez le récepteur d'embrayage.
  S4_REPOSE: 'Avant de remonter le récepteur d''embrayage, vérifiez systématiquement l''état de toutes les pièces accessibles
    lors de la dépose. Une purge complète du circuit hydraulique est indispensable après tout remplacement : la moindre bulle
    d''air rend la pédale spongieuse et compromet le débrayage. - Vérifiez que le récepteur d''embrayage neuf est identique
    à celui démonté : diamètre du piston, filetage des canalisations, type concentrique (CSC) ou externe. - Contrôlez l''état
    de la butée d''embrayage hydraulique — si le récepteur fuyait, la butée a pu subir une contamination par le liquide ;
    remplacez-la si nécessaire. - Contrôlez l''état du kit d''embrayage (disque, mécanisme) : profitez de la boîte de vitesses
    déposée pour vérifier l''usure. Un kit à moins de 20 % de friction restante doit être changé simultanément. - Contrôlez
    l''état de l''émetteur d''embrayage et de ses canalisations : un émetteur qui fuyait en parallèle du récepteur doit être
    remplacé au même moment. - Remontez le récepteur d''embrayage en position correcte, serrez les vis de fixation au couple
    préconisé par le constructeur (typiquement 8 à 12 N·m selon véhicule). - Raccordez la canalisation hydraulique soigneusement
    — serrez le raccord sans forcer pour ne pas endommager le filetage aluminium. Vérifiez l''absence de micro-fuite avant
    de continuer. - Remontez la boîte de vitesses et reconnectez le câblage électrique si le véhicule dispose d''un détecteur
    de rapport engagé. - Remplissez le circuit avec du liquide DOT 4 neuf par le réservoir de l''émetteur et procédez à la
    purge complète via le purgeur du récepteur jusqu''à l''absence totale de bulles. - Remontez la roue si applicable, reposez
    le véhicule au sol, puis testez la pédale à froid : la course doit être franche, sans enfoncement progressif. - Vérifiez
    le niveau du liquide de frein dans le réservoir après purge et complétez si nécessaire avant de circuler.'
  S5: '- ❌ "homologué CT - ❌ "sécurité garantie - ❌ "zéro panne - ❌ "garanti à vie - ❌ "action parfaite'
  S6: 'Le récepteur d''embrayage est l''élément hydraulique terminal du circuit d''actionnement — il convertit la pression
    du liquide de frein en déplacement mécanique pour désaccoupler le moteur de la boîte de vitesses. Après son remplacement,
    la vérification porte sur l''étanchéité du circuit hydraulique, la purge de l''air et la qualité de la commande d''embrayage
    au pied. - Purge complète du circuit hydraulique d''embrayage : purger le circuit par la vis de purge du récepteur jusqu''à
    obtenir un flux de liquide de frein DOT 4 sans bulles d''air. La présence d''air dans le circuit se manifeste par une
    pédale molle ou spongieuse. Reprendre la purge jusqu''à ce que la résistance de la pédale soit ferme et régulière sur
    toute la course. - Contrôle de la course et de la fermeté de la pédale d''embrayage : la pédale doit offrir une résistance
    progressive et constante sur toute sa course. Le point de patinage de l''embrayage doit se situer entre le tiers et la
    moitié de la course de pédale, à environ 50-80 mm de la position haute selon les constructeurs. Une pédale qui touche
    le plancher signale une purge incomplète ou une fuite. - Absence de fuite de liquide de frein sous la boîte de vitesses
    : après le premier cycle d''utilisation, inspecter visuellement la zone du récepteur d''embrayage. Aucune trace de liquide
    de frein (aspect huileux transparent à légèrement jaunâtre) ne doit apparaître sur le carter de la boîte de vitesses ou
    sur le flanc du récepteur. - Test de démarrage en côte avec changement de vitesses : effectuer 5 à 10 manœuvres en boîte
    de vitesses (1ère, 2ème, marche arrière) pour valider le désaccouplement complet. L''embrayage doit débrayer proprement
    sans à-coups ni bruit de grincement de la fourchette. Un grincement au niveau de la fourchette indique un défaut d''alignement
    du récepteur ou une usure de la fourchette elle-même. - Vérification du niveau de liquide de frein : le réservoir de liquide
    de frein (commun avec le circuit d''embrayage sur les systèmes hydrauliques) doit être rempli entre MIN et MAX avec du
    DOT 4 neuf. Un niveau qui baisse dans les 48h sans fuite visible externe signale une fuite interne du récepteur ou de
    l''émetteur. - Contrôle à 150 000 km : pour les véhicules à kilométrage élevé, vérifier simultanément l''émetteur d''embrayage
    et la butée d''embrayage si accessibles, car une défaillance séquentielle de ces composants est fréquente après 150 000
    km.'
  S7: Quel est le prix d'un récepteur d'embrayage ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur
    pour trouver le récepteur d'embrayage compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon récepteur d'embrayage est à changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un récepteur
    d'embrayage défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l'urgence du remplacement.- butee d embrayage - emetteur d embrayage - kit
    d embrayage - volant moteur
  S8: Comment choisir Récepteur d'embrayage compatible avec mon vehicule ?Renseignez marque, modele, type moteur et annee,
    puis verifiez la reference Quand remplacer Récepteur d'embrayage ?En cas de pedale d embrayage molle ou spongieuse ou
    de degradation mesurable, Puis-je monter Récepteur d'embrayage sans verification atelier ?Le montage peut exiger controles
    de couple, alignement et references.
  META: '{"meta_title":"Récepteur d''embrayage : fuite et remplacement | AutoMecanik","meta_description":"Pédale molle, fuite
    sous la boîte, embrayage bloqué : diagnostiquer un récepteur d''embrayage HS et savoir quand changer cette pièce hydraulique
    critique.","og_title":"Récepteur d''embrayage : pédale molle ou fuite, que faire ?","og_description":"Pédale spongieuse
    ou fuite de liquide sous la boîte de vitesses ? Identifiez un récepteur défaillant et découvrez la procédure de remplacement
    et de purge.","sources":[{"type":"rag","ref":"gammes/recepteur-d- embrayage.md","field":"diagnostic.symptoms,domain.role,rendering.faq"}]}'
---

# Récepteur d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Recevoir la pression hydraulique et actionner la butée ou la fourchette

**Actions principales:** recevoir la pression, actionner la butée, pousser la fourchette, convertir

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Embrayage qui ne debraye plus piston bloque**
  embrayage qui ne debraye plus piston bloque

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de grincement au niveau de la fourchette**
  bruit de grincement au niveau de la fourchette

### 🟡 Symptômes de Sécurité

- **Odeur de liquide de frein brule sous la voiture**
  odeur de liquide de frein brule sous la voiture

### 🟢 Autres Symptômes

- pedale d embrayage molle ou spongieuse
- fuite de liquide visible sous la boite de vitesses
- plus de 150 000 km sans verification du circuit

## Procédure de Diagnostic

Pour diagnostiquer un problème de récepteur d'embrayage:

1. **Inspection visuelle** - Examiner l'état du récepteur d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le récepteur d'embrayage peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- butee-d-embrayage
- emetteur-d-embrayage
- kit-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon récepteur d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "action parfaite"

## FAQ

**Récepteur d'embrayage OE ou OES ?**
Les récepteurs OES (Sachs, LuK, Valeo) sont fiables. Pour un récepteur concentrique (CSC), privilégiez l'OE ou un kit embrayage complet incluant le CSC.

**Comment savoir si mon récepteur d'embrayage fuit ?**
Pédale molle ou qui s'enfonce, fuite de liquide sous la boîte de vitesses, niveau de liquide de frein qui baisse, embrayage qui ne débraye plus.

**Faut-il purger après changement de récepteur ?**
Oui obligatoirement. Purge par le purgeur situé sur le récepteur. Utiliser du liquide DOT4 neuf. Vérifier l'absence de bulles d'air.

**Peut-on changer le récepteur d'embrayage soi-même ?**
Le récepteur externe oui (sous la voiture). Le récepteur concentrique nécessite de déposer la boîte : autant changer l'embrayage en même temps.

**Quelle erreur éviter avec le récepteur d'embrayage ?**
Ne pas forcer sur le piston. Bien purger pour éliminer tout l'air. Vérifier l'émetteur si le récepteur fuyait. Remplacer le CSC avec l'embrayage.
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


## References supplementaires

<!-- materialized-from-db manual/20d524862d16 2026-04-03 -->
### Données techniques OEM — Récepteur d'embrayage

# Données techniques OEM — Récepteur d'embrayage
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- composite
- céramique
- hydraulique
- pneumatique
- rainuré
- électrique

## Matériaux
- céramique

## Symptomes supplementaires

<!-- materialized-from-db diagnostic/embrayage.md 2026-01-08 -->
### Diagnostic - Embrayage

# Embrayage - Diagnostic complet

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
