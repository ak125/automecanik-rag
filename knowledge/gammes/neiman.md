---
category: electrique
slug: neiman
title: Neiman
pg_id: 1367
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
  role: Verrouiller la direction et alimenter les circuits electriques
  must_be_true:
  - verrouiller
  - alimenter
  - securiser
  must_not_contain:
  - injection
  - climatisation
  - freinage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - alternateur
  - batterie
  - demarreur
  - bougie-d-allumage
  - bobine-d-allumage
  - poulie-d-alternateur
  confusion_with:
  - term: piece-electrique-voisine
    difference: Les pieces electriques ont des connecteurs specifiques. Verifier le nombre de broches et le voltage.
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
  - ❌ "demarrage garanti"
  cost_range:
    min: 80
    max: 250
    currency: EUR
    unit: neuf
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    price_range: Prix élevé — évite les frais de reprogrammation antidémarrage
  - tier: Équivalent OE (OES)
    price_range: Prix intermédiaire — vérifier les exigences de reprogrammation
  - tier: Aftermarket standard
    price_range: Prix bas — risque de reprogrammation à prévoir sur certains véhicules
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
    label: Tableau de bord qui ne s allume pas au contact
    severity: confort
  - id: S2
    label: Cle qui tourne dans le vide sans effet
    severity: confort
  - id: S3
    label: Direction bloquee impossible a debloquer
    severity: immobilisation
  - id: S4
    label: Contact electrique intermittent coupures
    severity: confort
  - id: S5
    label: Odeur de plastique brule court-circuit interne
    severity: confort
  - id: S6
    label: Difficulte recurrente a tourner la cle
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - 'vehicule immobilise ou symptome critique : verification urgente piece et alimentation'
  - 'Usure ou defaillance causant : tableau de bord qui ne s allume pas au contact'
  quick_checks:
  - 'Observer : tableau de bord qui ne s allume pas au contact ?'
  - 'Observer : cle qui tourne dans le vide sans effet ?'
  - 'Observer : direction bloquee impossible a debloquer ?'
  - 'Observer : contact electrique intermittent coupures ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Tableau de bord qui ne s allume pas au contact
  - Cle qui tourne dans le vide sans effet
  - Direction bloquee impossible a debloquer
  - Contact electrique intermittent coupures
  - Odeur de plastique brule court-circuit interne
  - Difficulte recurrente a tourner la cle
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '1367'
  intro_title: A quoi sert Neiman ?
  risk_title: Pourquoi remplacer Neiman a temps ?
  risk_explanation: '**Pièce HS** - Le neiman peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le neiman peut être hors service et nécessiter un remplacement'
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
  - question: Neiman OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (Valeo, Hella) pour garantir la compatibilité avec l'immobiliseur. Les adaptables peuvent
      nécessiter une reprogrammation coûteuse.
  - question: Comment savoir si mon neiman est HS ?
    answer: Clé qui tourne dans le vide, direction bloquée en permanence, tableau de bord qui ne s'allume pas, contact intermittent,
      impossibilité de démarrer.
  - question: Quand faut-il changer le neiman ?
    answer: Pas de périodicité. À remplacer si usé mécaniquement (clé qui force), si les contacts sont oxydés, ou si la direction
      reste bloquée.
  - question: Peut-on changer le neiman soi-même ?
    answer: Difficile. Nécessite de démonter le carénage de colonne et souvent des vis de sécurité. Risque de bloquer l'antidémarrage.
      Prévoir reprogrammation.
  - question: Quelle erreur éviter avec le neiman ?
    answer: Ne pas forcer sur la clé (risque de casser). Vérifier la compatibilité immobiliseur avant achat. Prévoir le coût
      de reprogrammation si nécessaire.
  quality:
    score: 60
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: 24b47372-a822-5b06-9266-d6204849ac46
content_hash: sha256:5528ddc3f7b11b75
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
  _source: gpa26.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 2
  _has_tech_data: true
  technical_notes:
    val_4_a: '4 a'
    val_503_a: '503 a'
    val_59_a: '59 a'
    val_6_a: '6 a'
    val_70_a: '70 a'
    val_988_a: '988 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le Neiman est la pièce où on insère la clé de contactpour démarrer le moteur
    appelé aussi contact à clé. Il est sous la forme d'unantivol qui sert pour
    bloques la colonne de direction du véhicule jusqu'à ceque on introduit la
    clé de contact pour débloquer la colonne de direction.Le neiman joue le rôle
    d'un interrupteur parce qu'entournant la clé, on actionne tous les
    mécanismes dans le véhicule quipermettent la combustion, le démarrage du
    moteur et tous qu'est électrique dansle véhicule. Le Neiman est composé de
    deux éléments le cylindre de serrure danslequel en met la clé pour la
    tourner et le commutateur électronique situéderrière celui-ci. Le
    commutateur va donner l'impulsion électrique, encommandant l'arrivée du
    courant vers le démarreur à partir du moment où la cléest tournée, pour le
    démarrage du moteur. Après le démarrage du moteur démarre vousdevez relâcher
    la clé. En savoir plus : neiman — définition et rôle mécanique 🚨 Bruit
    Neiman : causes et diagnostic
  S2: >-
    Un neiman défaillantprésente plusieurs symptômes : - Il est abîmé ou forcé.
    - Il lâche lors du démarrage. - Vous remarquez la présence d'un petit délai
    entre le moment où voustournez la clé et le moment où le moteur se lance. -
    Vous appuyez très fort sur la clé pour démarrer. Un neiman usé doit être
    changédirectement si non vous risquez l'usure du démarreur et le
    déchargement de labatterie. Diagnostic complet : identifier une panne de
    neiman
  S3: >-
    Le neiman (ou antivol de direction) remplit deux fonctions distinctes :
    verrouiller mécaniquement la colonne de direction lorsque le contact est
    coupé, et alimenter les circuits électriques du véhicule à travers ses
    différentes positions de contact. Une défaillance partielle peut se
    manifester par une coupure électrique intermittente sans immobilisation — ce
    qui complique le diagnostic et justifie un choix rigoureux de la pièce de
    remplacement. - Référence constructeur stricte — OEM conseillé : le neiman
    est couplé mécaniquement à la colonne de direction via un ergot d'antivol
    dont la géométrie est propre à chaque constructeur et génération de
    véhicule. Une pièce aftermarket doit reproduire exactement le profil de
    l'ergot et la course angulaire du barillet. Toute approximation sur ce point
    bloque définitivement la colonne ou laisse la direction non verrouillée. -
    Version avec ou sans transpondeur : les véhicules produits après 1998
    (directive 95/56/CE) intègrent un transpondeur dans le barillet du neiman
    qui communique avec le calculateur anti-démarrage. Un neiman de remplacement
    doit être codé ou appairé avec le calculateur du véhicule. Un neiman non
    codé permet de tourner le contact mais empêche le démarrage du moteur
    (voyant antidémarrage allumé, moteur qui ne s'amorce pas). - Nombre de
    positions de contact : les neimanns modernes disposent de 4 positions
    (arrêt, accessoires, contact, démarrage). Certains modèles anciens en
    utilisent 3. La pièce de remplacement doit reproduire le même nombre de
    positions pour que les circuits accessoires (radio, vitre, direction
    assistée électrique) s'activent aux bons moments. - Fourniture avec ou sans
    jeu de clés : si le barillet est livré seul (sans clé), il est monté nu et
    doit être appairé avec la clé existante par un serrurier automobile ou un
    concessionnaire. Si le kit inclut un nouveau barillet avec clés, celles-ci
    doivent être découpées à la référence de la serrure du véhicule. Vérifier
    que le profil de clé correspond bien à la serrure de porte pour éviter
    d'avoir deux clés différentes sur un même véhicule. - Qualité du connecteur
    électrique du tambour : le tambour (partie électrique du neiman) distribue
    le courant vers les différents relais et calculateurs. Contrôler que le
    connecteur du remplacement dispose du même nombre de broches et d'une
    section de câble adaptée. Un connecteur avec sections réduites provoque des
    chutes de tension sur les circuits de puissance (démarreur, pompe à
    carburant). - Compatibilité avec la colonne de direction d'origine :
    certains neimanns sont fixés par une vis de cisaillement (vis à tête de
    sécurité) qui se casse volontairement à l'installation pour empêcher le
    démontage ultérieur. Prévoir l'outillage adapté (extracteur de vis
    cisaillées) et vérifier que la colonne de direction ne présente pas de
    déformation avant de fixer le neiman neuf. Pour aller plus loin : consultez
    notre guide d'achat neiman — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Neiman pour connaître les
    spécifications. - Débranchez la batterie. - Démontez les vis de fixation des
    caches en dessous du volant dedirection. - Démontez les vis de fixation du
    neiman sur la colonne de direction. - Débranchez le connecteur duneiman. -
    Démontez le neiman.
  S4_REPOSE: >-
    - Vérifiez que le neiman neufest identique à celui démonté. - Contrôlez
    l'état defonctionnement du démarreur . - Mettre en place le neiman. -
    Rebranchez le connecteur duneiman. - Serrez les vis de fixationdu neiman. -
    Mettre en place les cachesen dessous du volant de direction et serrez leurs
    fixations. - Rebranchez la batterie. - Contrôlez le bonfonctionnement du
    neiman. ✅ Après remontage, vérifiez les spécifications dans la fiche
    technique Neiman.
  S5: >-
    - ❌ "homologué CT - ❌ "sécurité garantie - ❌ "zéro panne - ❌ "garanti à vie
    - ❌ "demarrage garanti
  S6: >-
    Le neiman (contacteur antivol de colonne de direction) cumule deux fonctions
    critiques : le verrouillage mécanique de la colonne et l'alimentation des
    circuits électriques au contact. Son remplacement exige des vérifications
    électriques, mécaniques et électroniques avant de remettre le véhicule en
    circulation. - Déverrouillage de la colonne de direction : après
    installation, vérifier que la colonne de direction se déverrouille
    complètement en insérant la clé et en la tournant en position I (contact).
    La colonne ne doit présenter aucun point dur résiduel. Si le volant reste
    partiellement bloqué, le neiman n'est pas correctement aligné avec le
    mécanisme de verrouillage interne. - Alimentation des circuits au contact :
    en position I (contact), vérifier que le tableau de bord s'illumine
    normalement (voyants d'avertissement allumés, compteurs actifs). En position
    II (démarrage), la consommation doit chuter après allumage du moteur. Un
    tableau de bord qui ne s'allume pas en position I indique un problème de
    connexion électrique sur le neiman. - Test des positions de contact : tester
    chaque position de clé : 0 (verrouillé), I (accessoires), II (contact
    complet), III (démarrage). Les équipements doivent s'activer et se couper
    conformément à la logique constructeur. Sur certains véhicules, la position
    I alimente uniquement l'autoradio et les lève-vitres. - Compatibilité avec
    l'antidémarrage (immobiliseur) : si le véhicule est équipé d'un
    antidémarrage électronique, vérifier que le moteur démarre normalement sans
    affichage de code défaut antivol. Sur les neiman avec transpondeur intégré,
    une reprogrammation est obligatoire via un outil de diagnostic constructeur
    ou un serrurier agréé. Sans cette étape, le moteur refuse de démarrer même
    avec la clé correcte. - Absence d'odeur de brûlé : après 10 minutes de
    fonctionnement normal, ouvrir le carénage de colonne et vérifier l'absence
    d'odeur de plastique chaud. Un échauffement résiduel révèle un problème de
    contact électrique ou une résistance trop élevée dans le circuit
    d'alimentation. - Test des feux clignotants et du klaxon : activer les
    clignotants gauche et droit, puis le klaxon. Ces commandes transitent par le
    contacteur de colonne et permettent de valider l'ensemble des contacts
    électriques du neiman. Un clignotant qui ne fonctionne que d'un côté peut
    indiquer un mauvais engagement du connecteur. - Remontage du carénage de
    colonne : refermer le carénage supérieur et inférieur en vérifiant l'absence
    de jeu et de grincement. Un carénage mal clipsé vibre à la conduite et peut
    interférer avec le commodo de clignotants ou d'essuie-glaces.
  S7: >-
    Quel est le prix d'un neiman ?Le prix varie selon le véhicule et la marque.
    Utilisez notre sélecteur pour trouver le neiman compatible avec votre
    véhicule et comparer les tarifs des différents équipementiers.Comment savoir
    si mon neiman est à changer ?Les signes d'usure les plus courants sont
    détaillés dans la section diagnostic ci-dessus. En cas de doute, faites
    contrôler la pièce par un professionnel.Peut-on rouler avec un neiman
    défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la
    pièce dans la sécurité du véhicule. Consultez la section symptômes pour
    évaluer l'urgence du remplacement.- alternateur - colonne de direction -
    demarreur
  S8: >-
    Comment choisir Neiman compatible avec mon vehicule ?Renseignez marque,
    modele, type moteur et annee, puis verifiez la reference Quand remplacer
    Neiman ?En cas de tableau de bord qui ne s allume pas au contact ou de
    degradation Puis-je monter Neiman sans verification atelier ?Le montage peut
    exiger controles de couple, alignement et references.
---

# Neiman - Guide Diagnostic Complet

## Fonction et Rôle

Verrouiller la direction et alimenter les circuits electriques

**Actions principales:** verrouiller, alimenter, securiser

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Direction bloquee impossible a debloquer**
  direction bloquee impossible a debloquer

### 🟢 Autres Symptômes

- tableau de bord qui ne s allume pas au contact
- cle qui tourne dans le vide sans effet
- contact electrique intermittent coupures
- odeur de plastique brule court-circuit interne
- difficulte recurrente a tourner la cle

## Procédure de Diagnostic

Pour diagnostiquer un problème de neiman:

1. **Inspection visuelle** - Examiner l'état du neiman
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le neiman peut être hors service et nécessiter un remplacement
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- colonne-de-direction
- demarreur

## Critères de Compatibilité

Pour commander le bon neiman, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "demarrage garanti"

## FAQ

**Neiman OE ou adaptable ?**
Privilégiez l'OE ou OES (Valeo, Hella) pour garantir la compatibilité avec l'immobiliseur. Les adaptables peuvent nécessiter une reprogrammation coûteuse.

**Comment savoir si mon neiman est HS ?**
Clé qui tourne dans le vide, direction bloquée en permanence, tableau de bord qui ne s'allume pas, contact intermittent, impossibilité de démarrer.

**Quand faut-il changer le neiman ?**
Pas de périodicité. À remplacer si usé mécaniquement (clé qui force), si les contacts sont oxydés, ou si la direction reste bloquée.

**Peut-on changer le neiman soi-même ?**
Difficile. Nécessite de démonter le carénage de colonne et souvent des vis de sécurité. Risque de bloquer l'antidémarrage. Prévoir reprogrammation.

**Quelle erreur éviter avec le neiman ?**
Ne pas forcer sur la clé (risque de casser). Vérifier la compatibilité immobiliseur avant achat. Prévoir le coût de reprogrammation si nécessaire.
