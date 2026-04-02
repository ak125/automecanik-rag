---
category: freinage
slug: pompe-a-vide-de-freinage
title: Pompe à vide de freinage
pg_id: 387
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
  last_enriched_by: skill:phase5-hella-ngk
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Assister l'effort du conducteur sur la pedale de frein
  must_be_true:
  - assister le freinage
  - reduire l'effort
  - fournir une depression
  must_not_contain:
  - friction
  - hydraulique directe
  - ABS
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
  - ❌ "freinage direct"
  cost_range:
    min: 15
    max: 200
    currency: EUR
    unit: l'unite
    source: estimation categorie
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
    label: Pedale de frein tres dure
    severity: securite
  - id: S2
    label: Assistance au freinage defaillante
    severity: securite
  - id: S3
    label: Sifflement au niveau du moteur
    severity: confort
  - id: S4
    label: Voyant defaut frein allume
    severity: securite
  - id: S5
    label: Pedale dure surtout freinage depression
    severity: securite
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  quick_checks:
  - 'Observer : pedale de frein tres dure ?'
  - 'Observer : assistance au freinage defaillante ?'
  - 'Observer : sifflement au niveau du moteur ?'
  - Voyant defaut frein allume ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Pedale de frein tres dure
  - Assistance au freinage defaillante
  - Sifflement au niveau du moteur
  - Voyant defaut frein allume
  - Pedale dure surtout freinage depression
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '387'
  intro_title: A quoi sert Pompe à vide de freinage ?
  risk_title: Pourquoi remplacer Pompe à vide de freinage a temps ?
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
  - question: Tous les véhicules ont-ils une pompe à vide ?
    answer: Principalement les diesel et certains essence turbo. Les moteurs essence atmosphériques utilisent la dépression
      du collecteur d'admission.
  - question: Comment savoir si la pompe à vide est HS ?
    answer: Pédale de frein très dure, surtout après 2-3 freinages successifs. Un sifflement peut indiquer une fuite. Mesure
      au vacuomètre pour confirmer.
  - question: La pompe à vide est-elle critique pour la sécurité ?
    answer: Oui, sans elle le freinage nécessite beaucoup plus de force sur la pédale. Le freinage reste possible mais très
      pénible, surtout en urgence.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Accuser la pompe alors que c'est une durite de dépression fissurée ou un clapet anti-retour du servo-frein. Ignorer
      la fuite d'huile qui contamine la dépression.
  - question: Comment faire un diagnostic rapide ?
    answer: Pédale dure + sifflement → fuite dépression/durite/clapet. Mesure vacuomètre < -0,6 bar au ralenti → pompe faible.
      Fuite d'huile autour pompe → joint/pompe à traiter rapidement.
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
doc_id: 898a4c30-a6a5-5bb3-961b-2430c4d537f0
content_hash: sha256:66875b662797be93
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
  _source: HELLA TechWorld + NGK/NTK
  _validation_status: oem_verified
  _enriched_at: '2026-03-29'
  types_variants:
  - type: Pompe a vide electrique a palettes
    description: Rotor excentrique avec palettes, genere depression pour servo-frein
    era: diesel, hybrides, electriques, Stop/Start
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La fonction principale de la pompe à vide estl'assistance du freinage. Elle
    fonctionne en parallèle avec le servofrein de la voiture(amplificateur de
    freinage). Son rôle est de créer une dépression dans leservofrein de
    l'automobile pour démultiplier la force de pression exercé sur la pédale de
    freindans ce cas l'effort à fournir sera diminué. Autres fonctionde la pompe
    à vide : - L'alimentation d'électrovannes de commande du turbocompresseur et
    de la vanne EGR . - La commande pneumatique de volets d'air pour la
    climatisation. - La commande pneumatique de verrouillage des portes. Il
    existe deux types de pompe à vide desystème de freinage : - A membranes. - A
    palettes. L'entraînement de la pompe à vide change en fonction de la
    motorisation : - Par courroie. - Par pignon solidaire à l'arbre à cames. -
    Par moteur électrique associé à la pompe à vide. En savoir plus : pompe à
    vide de freinage — définition et rôle mécanique 🚨 Bruit Pompe à vide de
    freinage : causes et diagnostic
  S2: >-
    Ne pas attendre la panne complete pour intervenir. Symptômes d'usure : -
    Pedale de frein tres dure - Assistance au freinage defaillante - Sifflement
    au niveau du moteur - Voyant defaut frein allume - Pedale dure surtout
    freinage depression
  S3: >-
    Pour choisir les bons pompe a vide de freinage pour votre véhicule : -
    Marque de votre véhicule - Modele de votre véhicule - Annee de votre
    véhicule - Vérifier : pedale de frein tres dure - Vérifier : assistance au
    freinage defaillante - Vérifier : sifflement au niveau du moteur - Vérifier
    : voyant defaut frein allume - Vérifier : pedale dure surtout freinage
    depression
  S4_DEPOSE: >-
    - Si localiser source et verifier usure mecanique - Si lecture codes defaut
    obd et diagnostic electronique - Si bruit anormal detecte : localiser source
    et verifier usure mecanique - Si voyant tableau bord allume : lecture codes
    defaut obd et diagnostic electronique
  S4_REPOSE: >-
    Le remontage d'une pompe à vide de freinage doit être mené avec attention :
    un raccordement défectueux des durites de dépression ou un joint
    d'étanchéité mal positionné annule complètement l'assistance au freinage. La
    pédale sera alors extrêmement dure, surtout lors des premiers freinages
    après démarrage à froid. Vérifier systématiquement le servofrein associé
    avant de conclure l'intervention. - Contrôler la conformité de la pompe
    neuve — Comparer la pompe à vide de freinage neuve avec celle déposée : type
    d'entraînement (mécanique par arbre à cames, électrique ou par courroie
    selon modèle), position du raccord dépression, sens de rotation. Une pompe
    incorrecte est incompatible avec le circuit de dépression du véhicule. -
    Inspecter l'état du servofrein — Contrôler l'état d'usure du servofrein :
    vérifier l'absence de fuite d'huile sur la membrane, tester le clapet anti-
    retour de dépression (pression à la main sur le raccord — l'air doit passer
    dans un seul sens). Un servofrein défaillant doit être remplacé en même
    temps que la pompe à vide. - Monter le joint d'étanchéité neuf — Positionner
    le joint d'étanchéité neuf sur la flasque de montage de la pompe. Ce joint
    assure l'étanchéité mécanique entre la pompe et le carter moteur
    (entraînement par arbre à cames). Ne jamais réutiliser l'ancien joint, même
    apparent en bon état. - Mettre en place la pompe à vide — Engager la pompe à
    vide de freinage sur son logement en alignant le téton ou la rainure
    d'entraînement avec l'arbre à cames ou le pivot d'entraînement. Guider
    délicatement pour ne pas endommager le joint ou la surface de contact. -
    Brancher le connecteur électrique — Reconnecter le connecteur électrique de
    commande de la pompe (sur les pompes à vide électriques des moteurs diesel
    modernes sans dépression naturelle). Vérifier le clipsage complet du
    connecteur. - Serrer les fixations au couple prescrit — Visser les vis de
    fixation de la pompe à vide progressivement et en croix au couple
    constructeur. Un serrage insuffisant provoque une fuite de dépression à
    l'interface pompe-moteur ; un sur-serrage endommage le filetage dans
    l'aluminium du carter. - Reconnecter les durites de dépression — Rebrancher
    la ou les durites de dépression sur le raccord de la pompe. Vérifier le bon
    clipsage des colliers ou des raccords rapides. Inspecter l'état des durites
    sur toute leur longueur : une durite fissurée ou poreuse annule l'assistance
    au freinage même avec une pompe neuve. - Rebrancher la batterie et contrôler
    la dépression — Rebrancher la batterie. Démarrer le moteur et laisser
    tourner 2 minutes au ralenti pour permettre à la pompe à vide de créer la
    dépression dans le servofrein. Tester la pédale de frein : elle doit
    s'enfoncer facilement au premier appui avec l'assistance active. Mesurer la
    dépression au vacuomètre si disponible (valeur cible : supérieure à -0,6 bar
    au ralenti). - Essai routier et vérification finale — Effectuer un essai de
    freinage à faible allure pour confirmer l'assistance normale. Contrôler
    l'absence de sifflement de dépression au ralenti autour de la pompe et des
    durites, signe d'une fuite résiduelle à corriger avant tout usage normal du
    véhicule.
  S5: >-
    - ❌ "homologué CT" - ❌ "sécurité garantie" - ❌ "zéro panne" - ❌ "garanti à
    vie" - ❌ "freinage direct"
  S6: >-
    Contrôles statiques - Vérifier l'absence de fuite d'huile au joint d'embase
    de la pompe - Contrôler l'étanchéité du tuyau de dépression (pas de
    craquement, raccords bien serrés) - Démarrer le moteur et pomper la pédale
    de frein : elle doit s'enfoncer plus facilement qu'au contact (assistance
    active) - Couper le moteur et pomper 3 à 4 fois : la pédale doit rester
    assistée 2 à 3 appuis puis durcir (réserve de dépression) Essai routier -
    Freinage normal à 30, 50, 70 km/h : la pédale doit être progressive et
    souple - Couper le moteur et freiner : l'assistance doit persister 2 à 3
    coups de pédale (clapet anti-retour OK) - Après 50 km, vérifier l'absence de
    fuite d'huile à la pompe ⚠️ Consulter un atelier si : pédale dure dès le
    premier freinage moteur tournant, sifflement au niveau du servo-frein, fuite
    d'huile persistante, voyant de frein allumé. 🚨 Bruit Pompe à vide de
    freinage : causes et diagnostic
  S_GARAGE: >-
    Nous vous recommandons de confier cette intervention à un professionnel : -
    Plusieurs causes possibles de défaillance (4 identifiées) nécessitent un
    diagnostic professionnel Un garagiste qualifié dispose de l'outillage et de
    l'expérience nécessaires pour effectuer cette opération en toute sécurité.
  S7: >-
    Quel est le prix d'un pompe à vide de freinage ?Le prix varie selon le
    véhicule et la marque. Utilisez notre sélecteur pour trouver le pompe à vide
    de freinage compatible avec votre véhicule et comparer les tarifs des
    différents équipementiers.Comment savoir si mon pompe à vide de freinage est
    à changer ?Les signes d'usure les plus courants sont détaillés dans la
    section diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par
    un professionnel.Peut-on rouler avec un pompe à vide de freinage défaillant
    ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans
    la sécurité du véhicule. Consultez la section symptômes pour évaluer
    l'urgence du remplacement.- maitre cylindre de frein - servo frein
  S8: >-
    Tous les véhicules ont-ils une pompe à vide ?Principalement les diesel et
    certains essence turbo. Les moteurs essence atmosphériques utilisent la
    dépression du collecteur d'admission. Comment savoir si la pompe à vide est
    HS ?Pédale de frein très dure, surtout après 2-3 freinages successifs. Un
    sifflement peut indiquer une fuite. Mesure au vacuomètre pour confirmer. La
    pompe à vide est-elle critique pour la sécurité ?Oui, sans elle le freinage
    nécessite beaucoup plus de force sur la pédale. Le freinage reste possible
    mais très pénible, surtout en urgence. Quelles sont les erreurs fréquentes à
    éviter ?Accuser la pompe alors que c'est une durite de dépression fissurée
    ou un clapet anti-retour du servo-frein. Ignorer la fuite d'huile qui
    contamine la dépression. Comment faire un diagnostic rapide ?Pédale dure +
    sifflement → fuite dépression/durite/clapet. Mesure vacuomètre
  META: >-
    Guide complet pour remplacer votre pompe à vide de freinage : compatibilité,
    test de dépression, clapet anti-retour et FAQ assistance freinage.
---

# Pompe à vide de freinage - Guide Diagnostic Complet

## Fonction et Rôle

Assister l'effort du conducteur sur la pedale de frein

**Actions principales:** assister le freinage, reduire l'effort, fournir une depression, creer le vide, alimenter le servofrein

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Pedale de frein tres dure**
  pedale de frein tres dure
- **Assistance au freinage defaillante**
  assistance au freinage defaillante
- **Voyant defaut frein allume**
  voyant defaut frein allume
- **Pedale dure surtout freinage depression**
  pedale dure surtout freinage depression

### 🟢 Autres Symptômes

- sifflement au niveau du moteur

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à vide de freinage:

1. **Inspection visuelle** - Examiner l'état du pompe à vide de freinage
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

- maitre-cylindre-de-frein
- servo-frein

## Critères de Compatibilité

Pour commander le bon pompe à vide de freinage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage direct"

## FAQ

**Tous les véhicules ont-ils une pompe à vide ?**
Principalement les diesel et certains essence turbo. Les moteurs essence atmosphériques utilisent la dépression du collecteur d'admission.

**Comment savoir si la pompe à vide est HS ?**
Pédale de frein très dure, surtout après 2-3 freinages successifs. Un sifflement peut indiquer une fuite. Mesure au vacuomètre pour confirmer.

**La pompe à vide est-elle critique pour la sécurité ?**
Oui, sans elle le freinage nécessite beaucoup plus de force sur la pédale. Le freinage reste possible mais très pénible, surtout en urgence.

**Quelles sont les erreurs fréquentes à éviter ?**
Accuser la pompe alors que c'est une durite de dépression fissurée ou un clapet anti-retour du servo-frein. Ignorer la fuite d'huile qui contamine la dépression.

**Comment faire un diagnostic rapide ?**
Pédale dure + sifflement → fuite dépression/durite/clapet. Mesure vacuomètre < -0,6 bar au ralenti → pompe faible. Fuite d'huile autour pompe → joint/pompe à traiter rapidement.
