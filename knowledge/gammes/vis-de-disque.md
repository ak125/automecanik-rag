---
category: freinage
slug: vis-de-disque
title: Vis de disque
pg_id: 54
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
  last_enriched_by: skill:phase5-vague6
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Fixer le disque de frein sur le moyeu de roue
  must_be_true:
  - fixer
  - maintenir
  - bloquer
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
  - ❌ "freinage garanti"
  cost_range:
    min: 3
    max: 15
    currency: EUR
    unit: l'unite
    source: estimation categorie
  brands:
    premium:
    - Brembo
    - ATE
    - TRW
    standard:
    - Febi Bilstein
    - Swag
    - Bosch
    - Textar
    budget:
    - NK
    - A.B.S.
    - Mapco
  quality_tiers:
  - tier: Origine (OE/OES)
    description: Vis de disque fabriquées par les équipementiers d'origine. Traitement anti-corrosion et couple de serrage
      calibrés pour le moyeu spécifique.
  - tier: Équivalent OE
    description: Fabricants aftermarket reconnus en visserie de freinage. Conformes aux spécifications constructeur, traitement
      de surface adapté.
  - tier: Adaptable
    description: Vis économiques. Vérifier le type d'empreinte (Torx, Allen, hexagonale), le diamètre et le pas de filetage
      avant commande.
diagnostic:
  symptoms:
  - id: S1
    label: Vis grippee impossible a devisser
    severity: confort
  - id: S2
    label: Tete de vis arrondie ou endommagee
    severity: confort
  - id: S3
    label: Vis rouillee visible a travers la jante
    severity: confort
  - id: S4
    label: Disque qui bouge legerement vis desserree
    severity: confort
  - id: S5
    label: Bruit claquement freinage cassee absente
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : vis grippee impossible a devisser'
  quick_checks:
  - 'Observer : vis grippee impossible a devisser ?'
  - 'Observer : tete de vis arrondie ou endommagee ?'
  - 'Observer : vis rouillee visible a travers la jante ?'
  - 'Observer : disque qui bouge legerement vis desserree ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Vis grippee impossible a devisser
  - Tete de vis arrondie ou endommagee
  - Vis rouillee visible a travers la jante
  - Disque qui bouge legerement vis desserree
  - Bruit claquement freinage cassee absente
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '54'
  intro_title: A quoi sert Vis de disque ?
  risk_title: Pourquoi remplacer Vis de disque a temps ?
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
  - question: Les vis de disque sont-elles indispensables ?
    answer: Elles maintiennent le disque en place pendant le montage. Une fois la roue serrée, les écrous de roue assurent
      le maintien principal.
  - question: Comment retirer une vis grippée ?
    answer: 'Dégrippant, chaleur localisée, embout à frapper. En dernier recours : perçage et extraction. Prévoyez des vis
      neuves.'
  - question: Faut-il graisser ou freiner les vis ?
    answer: 'Selon constructeur : certains préconisent du frein-filet (Loctite bleu), d''autres de la graisse cuivrée. Consultez
      la documentation technique.'
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Forcer une vis Torx/Allen grippée sans outil → tête foirée. Oublier de nettoyer l'empreinte → l'embout ripe.
  - question: Comment faire un diagnostic rapide ?
    answer: 'Vis déjà arrondie/rouillée → prévoir vis neuves + embout neuf + dégrippant. Si elle casse : extraction/perçage
      (prévoir temps atelier).'
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
doc_id: eb3cd898-8b88-5d10-9322-ba32273a3786
content_hash: sha256:81bcfb7df7043650
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
phase5_enrichment:
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    couple: '8-12 Nm (Torx ou 6 pans)'
    role: 'maintien du disque sur le moyeu pendant le montage de la roue — pas structural'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La vis de disque est une vis de centrage et de maintien qui fixe le disque
    de frein sur le moyeu de roue lors des phases de montage. Généralement au
    nombre d'une à deux par roue selon le véhicule, elle bloque le disque dans
    sa position angulaire exacte pendant que l'on monte et serre les écrous de
    roue — ce qui permet de travailler sans que le disque ne pivote librement
    sur le moyeu. Une fois les écrous de roue serrés au couple prescrit, ce sont
    ces derniers qui assurent le maintien principal du disque en service. La vis
    de disque joue alors un rôle secondaire de sécurité anti-rotation : sur la
    plupart des véhicules, sa présence n'est plus structurellement requise une
    fois la roue en place, mais son absence peut laisser le disque osciller
    légèrement lors des prochains montages ou lors d'une dépose de roue en
    atelier (contrôle technique, vidange, etc.). Son matériau est généralement
    de l'acier traité avec un filetage métrique M5 à M8 selon le constructeur,
    et la tête est de type Torx ou Allen (six pans creux) pour permettre un
    serrage précis. L'empreinte Torx est privilégiée pour sa résistance à
    l'arrimage et sa tolérance à la corrosion, mais c'est aussi la première
    partie à s'arrondir si l'on utilise un outil inadapté ou usé.
  S2: >-
    Ne pas attendre la panne complete pour intervenir. Symptômes d'usure : - Vis
    grippee impossible a devisser - Tete de vis arrondie ou endommagee - Vis
    rouillee visible a travers la jante - Disque qui bouge legerement vis
    desserree - Bruit claquement freinage cassee absente
  S2_DIAG: >-
    SymptômeCause probableActionVis grippee impossible a devisserlocaliser
    source et verifier usure mecaniqueObserver : vis grippee impossible a
    devisser ?Tete de vis arrondie ou endommageebruit anormal detecte :
    localiser source et verifier usure mecaniqueObserver : tete de vis arrondie
    ou endommagee ?Vis rouillee visible a travers la janteUsure ou defaillance
    causant : vis grippee impossible a devisserObserver : vis rouillee visible a
    travers la jante ?Disque qui bouge legerement vis desserreelocaliser source
    et verifier usure mecaniqueObserver : disque qui bouge legerement vis
    desserree ?Bruit claquement freinage cassee absentelocaliser source et
    verifier usure mecaniqueObserver : vis grippee impossible a devisser ?
  S3: >-
    Pour choisir les bons vis de disque pour votre véhicule : - Marque de votre
    véhicule - Modele de votre véhicule - Annee de votre véhicule
  S4_DEPOSE: >-
    Le remplacement de la vis de disque est une opération courte mais qui peut
    devenir complexe si la vis est grippée. La procédure ci-dessous couvre les
    deux cas : vis encore dévissable et vis grippée nécessitant une extraction.
    Toujours immobiliser le disque avant toute tentative de dévissage pour ne
    pas faire tourner l'ensemble frein. - Lever le véhicule et déposer la roue :
    soulever le véhicule sur chandelles, retirer les écrous de roue et sortir la
    roue. Le disque de frein et sa vis sont maintenant accessibles sur le moyeu.
    - Identifier l'empreinte et l'état de la vis : Torx ou Allen ? La tête est-
    elle intacte ou déjà arrondie ? Inspecter avec une lampe. Si la tête est
    encore saine, passer à l'étape 4. Si elle est foirée, aller directement à
    l'étape 5. - Appliquer du dégrippant si nécessaire : pulvériser du
    dégrippant à base de molybdène ou de zinc sur la vis et laisser pénétrer 10
    à 15 minutes. Pour une vis très grippée, renouveler l'application 2 fois et
    attendre 30 minutes au total. - Dévisser avec un embout neuf et adapté :
    insérer l'embout Torx ou Allen neuf (jamais usé) à fond dans l'empreinte,
    maintenir une pression axiale ferme et appliquer une force de rotation
    progressive. Ne jamais à-coups qui arrondissent l'empreinte. - Extraction si
    tête foirée : utiliser un embout extracteur pour vis endommagées (type
    Irwin), une pince multiprise à mâchoires droites ou pointer au centre de la
    vis et percer progressivement avec un foret de 2, puis 4 mm pour extraire le
    noyau fileté. Prévoir du temps et des forets neufs. - Nettoyer le taraudage
    du moyeu : passer un taraud de même pas de vis pour rétablir le filetage si
    la vis grippée l'a endommagé. Éliminer les copeaux avec de l'air comprimé. -
    Préparer et visser la vis neuve : appliquer frein-filet ou graisse cuivrée
    selon la préconisation constructeur, introduire à la main pour vérifier
    l'absence de faux pas de vis, puis serrer à la clé dynamométrique au couple
    prescrit (généralement 4 à 8 Nm). - Remonter la roue et reposer le véhicule
    : reposer la roue, serrer les écrous de roue au couple prescrit. Descendre
    le véhicule, effectuer un déplacement de 10 m en marche avant et arrière,
    puis re-contrôler le serrage des écrous.
  S4_REPOSE: >-
    Après l'extraction de l'ancienne vis de disque — qu'elle ait été dévissée
    normalement ou extraite après grippage — la repose consiste à installer la
    vis neuve avec le bon produit de blocage et au couple exact. Une vis sous-
    serrée crée un bruit de claquement au freinage ; une vis sur-serrée se
    grippe immédiatement et deviendra impossible à démonter lors du prochain
    remplacement de disque. - Nettoyer le taraudage du moyeu : passer un taraud
    de même diamètre et pas de vis dans le trou pour éliminer la rouille, les
    résidus de filetage et les particules de la vis extraite. Souffler les
    copeaux à l'air comprimé ou les retirer avec un chiffon propre. Un taraudage
    propre est la condition d'un serrage au couple fiable. - Aligner le disque
    neuf sur le moyeu : poser le disque de frein en centrant les trous de la vis
    (généralement 1 trou par disque) sur le taraudage du moyeu. Le disque doit
    reposer à plat, sans jeu axial. Si le disque bouge ou est incliné, vérifier
    que les surfaces de contact du moyeu sont propres. - Appliquer le produit de
    blocage selon la préconisation constructeur : deux options selon le
    constructeur : frein-filet Loctite bleu (220 / 243) pour la majorité des
    applications, ou graisse cuivrée sur filetage pour les constructeurs qui
    préconisent un démontage facilité à la prochaine révision. Ne jamais
    utiliser les deux simultanément ni choisir du Loctite rouge (démontage
    impossible à froid). - Introduire la vis à la main : visser la vis neuve à
    la main sur les 3 à 4 premiers filets pour s'assurer de l'absence de faux
    pas de vis. Si la vis résiste dès le départ, dévisser complètement et
    reprendre. Forcer à la clé sur un faux pas de vis détériore le taraudage du
    moyeu — réparation coûteuse. - Serrer à la clé dynamométrique au couple
    prescrit : serrer progressivement à la clé dynamométrique. Le couple
    prescrit pour les vis de disque est généralement de 4 à 8 Nm selon le
    constructeur — consulter la documentation technique du véhicule. Ne pas
    estimer le couple à la main : une vis Torx M6 semble serrée bien avant
    d'atteindre le couple. - Vérifier l'absence de dépassement du nez de vis :
    la tête de vis doit être au ras de la surface du disque ou légèrement en
    retrait. Une vis qui dépasse peut interférer avec l'étrier de frein ou le
    cache-poussière lors du montage de la roue. - Remonter la roue et serrer les
    écrous au couple : poser la roue, serrer les écrous de roue à la main en
    croix, descendre le véhicule des chandelles, puis serrer les écrous au
    couple final prescrit avec une clé dynamométrique (généralement 100 à 130 Nm
    selon le véhicule). - Effectuer un freinage d'rodage : réaliser 5 à 10
    freinages modérés depuis 50 km/h pour rodage si le disque de frein est neuf.
    Ce rodage n'est pas lié à la vis mais s'effectue naturellement lors de la
    validation de l'intervention.
  S5: >-
    - ❌ "homologué CT" - ❌ "sécurité garantie" - ❌ "zéro panne" - ❌ "garanti à
    vie" - ❌ "freinage garanti"
  S6: >-
    Après le montage de la vis de disque neuve, quelques contrôles rapides
    permettent de confirmer que le disque est correctement fixé et que le
    freinage sera efficace et sans vibration lors des premières sollicitations.
    - Contrôle du couple de serrage de la vis de disque : vérifier avec une clé
    dynamométrique que la vis est serrée au couple prescrit par le constructeur
    (généralement 4 à 8 Nm). Un serrage insuffisant laisse la vis se desserrer
    aux vibrations ; excessif, il détériore le filetage du moyeu. - Absence de
    jeu axial du disque sur le moyeu : tenter de faire bouger le disque
    latéralement à la main — il ne doit présenter aucun jeu axial perceptible
    une fois la vis serrée. Un jeu indique un filetage endommagé ou une vis
    insuffisamment serrée. - Contrôle du voile du disque après repose : avec un
    comparateur à cadran sur support magnétique, mesurer le voile du disque
    après montage — valeur maximale généralement de 0,05 à 0,10 mm selon le
    constructeur. Un voile excessif provoque une vibration de pédale au
    freinage. - Serrage des écrous de roue au couple et vérification croisée :
    serrer les écrous de roue en étoile au couple prescrit (généralement 100 à
    130 Nm). Descendre le véhicule, avancer de 10 mètres, puis re-contrôler le
    serrage à la clé dynamométrique. - Premier freinage progressif : effectuer 5
    à 10 freinages progressifs depuis 40 km/h jusqu'à l'arrêt complet pour
    constater l'absence de bruit anormal (claquement, craquement, sifflement)
    qui signalerait un problème de montage.
  S_GARAGE: >-
    Nous vous recommandons de confier cette intervention à un professionnel : -
    Plusieurs causes possibles de défaillance (3 identifiées) nécessitent un
    diagnostic professionnel Un garagiste qualifié dispose de l'outillage et de
    l'expérience nécessaires pour effectuer cette opération en toute sécurité.
  S8: >-
    Les vis de disque sont-elles indispensables ?Elles maintiennent le disque en
    place pendant le montage. Une fois la roue serrée, les écrous de roue
    assurent le maintien principal. Comment retirer une vis grippée ?Dégrippant,
    chaleur localisée, embout à frapper. En dernier recours : perçage et
    extraction. Prévoyez des vis neuves. Faut-il graisser ou freiner les vis
    ?Selon constructeur : certains préconisent du frein-filet (Loctite bleu),
    d'autres de la graisse cuivrée. Consultez la documentation technique.
    Quelles sont les erreurs fréquentes à éviter ?Forcer une vis Torx/Allen
    grippée sans outil → tête foirée. Oublier de nettoyer l'empreinte → l'embout
    ripe. Comment faire un diagnostic rapide ?Vis déjà arrondie/rouillée →
    prévoir vis neuves + embout neuf + dégrippant. Si elle casse :
    extraction/perçage (prévoir temps atelier).
---

# Vis de disque - Guide Diagnostic Complet

## Fonction et Rôle

Fixer le disque de frein sur le moyeu de roue

**Actions principales:** fixer, maintenir, bloquer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit claquement freinage cassee absente**
  bruit claquement freinage cassee absente

### 🟢 Autres Symptômes

- vis grippee impossible a devisser
- tete de vis arrondie ou endommagee
- vis rouillee visible a travers la jante
- disque qui bouge legerement vis desserree

## Procédure de Diagnostic

Pour diagnostiquer un problème de vis de disque:

1. **Inspection visuelle** - Examiner l'état du vis de disque
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
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

- disque-de-frein

## Critères de Compatibilité

Pour commander le bon vis de disque, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage garanti"

## FAQ

**Les vis de disque sont-elles indispensables ?**
Elles maintiennent le disque en place pendant le montage. Une fois la roue serrée, les écrous de roue assurent le maintien principal.

**Comment retirer une vis grippée ?**
Dégrippant, chaleur localisée, embout à frapper. En dernier recours : perçage et extraction. Prévoyez des vis neuves.

**Faut-il graisser ou freiner les vis ?**
Selon constructeur : certains préconisent du frein-filet (Loctite bleu), d'autres de la graisse cuivrée. Consultez la documentation technique.

**Quelles sont les erreurs fréquentes à éviter ?**
Forcer une vis Torx/Allen grippée sans outil → tête foirée. Oublier de nettoyer l'empreinte → l'embout ripe.

**Comment faire un diagnostic rapide ?**
Vis déjà arrondie/rouillée → prévoir vis neuves + embout neuf + dégrippant. Si elle casse : extraction/perçage (prévoir temps atelier).


## References supplementaires

<!-- materialized-from-db guides/freinage__quand-changer.md 2026-03-03 -->
### Quand changer les plaquettes et disques

## Signes d'usure

- bruit metallique au freinage
- vibration a la pedale
- distance de freinage en hausse
- epaisseur de garniture faible

## Frequence de controle

- controle visuel regulier
- verification a chaque entretien periodique
- remplacement selon usure reelle et recommandations constructeur
