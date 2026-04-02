---
category: allumage
slug: bobine-d-allumage
title: Bobine d'allumage
pg_id: 689
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
  role: Transformer la basse tension batterie en haute tension (15-40kV) pour creer l'etincelle aux bougies
  must_be_true:
  - transformer la tension
  - amplifier
  - generer la haute tension
  must_not_contain:
  - diesel
  - prechauffage
  - incandescence
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - alternateur
  - batterie
  - demarreur
  - bougie-d-allumage
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
  - ❌ "plus de puissance"
  cost_range:
    min: 25
    max: 245
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
  quality_tiers:
  - tier: Piece d'origine (OE)
    description: Bobine reference constructeur, generalement produite par un equipementier de rang 1. Recommandee sur vehicules
      recents ou si une garantie constructeur est en jeu.
  - tier: Equipementier rang 1 - electricite/allumage
    description: Fabricants specialises en systemes d'allumage, fournissant les constructeurs en premiere monte. Equivalences
      documentees par reference vehicule et motorisation.
  - tier: Marque intermediaire
    description: Bobines de remplacement conformes aux specifications electriques. Verifier la tension nominale, la resistance
      primaire et secondaire avant achat.
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
    label: Rate moteur localise sur un cylindre precis
    severity: confort
  - id: S2
    label: Voyant moteur allume code p030x
    severity: confort
  - id: S3
    label: Perte de puissance brutale ou progressive
    severity: confort
  - id: S4
    label: Surconsommation de carburant
    severity: confort
  - id: S5
    label: Odeur d essence non brulee a l echappement
    severity: confort
  - id: S6
    label: Demarrage difficile par temps humide
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  - 'Usure ou defaillance causant : rate moteur localise sur un cylindre precis'
  depose_steps: []
  quick_checks:
  - 'Observer : rate moteur localise sur un cylindre precis ?'
  - Voyant moteur allume code p030x ?
  - 'Observer : perte de puissance brutale ou progressive ?'
  - 'Comparer la consommation : surconsommation de carburant ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Rate moteur localise sur un cylindre precis
  - Voyant moteur allume code p030x
  - Perte de puissance brutale ou progressive
  - Surconsommation de carburant
  - Odeur d essence non brulee a l echappement
  - Demarrage difficile par temps humide
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '689'
  intro_title: A quoi sert Bobine d'allumage ?
  risk_title: Pourquoi remplacer Bobine d'allumage a temps ?
  risk_explanation: '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  risk_consequences:
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
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
  - question: Bobine d'allumage OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (Bosch, Denso, NGK). Les bobines bas de gamme ont une durée de vie réduite et peuvent
      griller rapidement.
  - question: Comment savoir si ma bobine d'allumage est HS ?
    answer: Raté moteur localisé sur un cylindre, voyant moteur + code P030x, perte de puissance, test à l'ohmmètre hors tolérance.
  - question: Tous les combien changer les bobines d'allumage ?
    answer: Pas de périodicité fixe. Durée de vie 100 000 à 200 000 km. À remplacer uniquement en cas de défaut avéré (test
      diagnostic).
  - question: Peut-on changer une bobine d'allumage soi-même ?
    answer: Oui, opération simple sur bobines crayon. Débrancher le connecteur, dévisser la vis de fixation, extraire la bobine.
      10 à 20 minutes.
  - question: Quelle erreur éviter avec les bobines d'allumage ?
    answer: Ne pas changer toutes les bobines par précaution (inutile et coûteux). Vérifier l'état des bougies avant de remplacer
      la bobine.
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
doc_id: bdcb2e3a-53f9-59b8-b5f3-46e27c0c9941
content_hash: sha256:0479945fd18601e8
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
  _source: delphiautoparts.com
  _validation_status: oem_verified
  _enriched_at: '2026-04-02'
  _web_files_count: 9
  _has_tech_data: true
  types_variants:
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_000_v: '000 v'
    val_100_a: '100 a'
    val_12_v: '12 v'
    val_7_a: '7 a'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La bobine d'allumage transmet du courant haute tension auxbougies d'allumage
    à travers le faisceau d'allumage pour produire l'étincellenécessaire à la
    combustion du moteur essence. Lorsqu'on démarre le moteur le courant passe
    directementdans la bobine d'allumage. Le courant haute tension produit une
    étincelle quipasse de l'électrode centrale à l'électrode de masse de la
    bougie d'allumagepour enflammer le mélange air-carburant. La bobine
    d'allumage est un quadripôle mettant à profit lephénomène d'induction
    électromagnétique pour engendrer une impulsion sous unetrès haute tension.
    Types de bobines : - Bobine classique. - Bobine double indépendante. -
    Bobine rampe à distributeurhaute tension?.. En savoir plus : bobine
    d'allumage — définition et rôle mécanique 🚨 Bruit Bobine d'allumage : causes
    et diagnostic
  S2: >-
    Ne pas attendre la panne complete pour intervenir. Symptômes d'usure : -
    Rate moteur localise sur un cylindre precis - Voyant moteur allume code
    p030x - Perte de puissance brutale ou progressive - Surconsommation de
    carburant - Odeur d essence non brulee a l echappement - Demarrage difficile
    par temps humide - # Bobine d'allumage - Accueil Pièces Allumage Allumage
    Bobine d'allumage Bobine d'allumage Bien que les principes fondamentaux
    d'une bobine d'allumage n'aient pas changé, les exigences qui leur sont... -
    ## INSCRIVEZ-VOUS POUR EN SAVOIR PLUS Renseignez vos coordonnées pour
    écouter nos experts et recevoir les dernières actualités de . Diagnostic
    Découvrez notre vaste gamme d'équipements de diagnostic... - ### Dois-je
    utiliser un outil de diagnostic ? Après avoir installé la nouvelle bobine
    d'allumage, vous devez supprimer tous les codes d'erreurs et vérifier
    qu'elle fonctionne correctement à l'aide...
  S3: >-
    Pour choisir les bons bobine d allumage pour votre véhicule : - Marque de
    votre véhicule - Modele de votre véhicule - Annee de votre véhicule -
    Vérifier : rate moteur localise sur un cylindre precis - Vérifier : voyant
    moteur allume code p030x - Vérifier : perte de puissance brutale ou
    progressive - Vérifier : surconsommation de carburant - Vérifier : odeur d
    essence non brulee a l echappement - Vérifier : demarrage difficile par
    temps humidePour aller plus loin : consultez notre guide d'achat bobine
    d'allumage — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    1. Débranchez la batterie (borne négative). 2. Retirez le cache moteur et la
    cloison d'accès pour atteindre la bobine d'allumage. 3. Débranchez le
    connecteur électrique de la bobine (desserrez le clip de verrouillage). 4.
    Dévissez la bobine de son logement et retirez-la. 5. Vérifiez l'état de la
    bougie d'allumage en dessous (remplacer si usée). 6. Installez la bobine
    neuve en vérifiant qu'elle est bien centrée au-dessus de la bougie. 7.
    Appuyez fermement pour assurer l'étanchéité, rebranchez le connecteur
    électrique.
  S4_REPOSE: >-
    - Vérifier que la bobine d'allumage neuveest identique à celle démonté. -
    Remplacez les bougies d'allumage. - Contrôlez le faisceau d'allumage et
    leremplacé si nécessaire. - Reposez la bobine d'allumage. - Serrez les vis
    de fixation de la bobined'allumage. - Rebrancher le connecteur et le
    faisceauhaut tension de la bobine d'allumage. - Rebranchez les fils des
    bougies d'allumage. - Remettez le boîtierfiltre à air . - Rebranchez la
    batterie. - Contrôlez le fonctionnement du moteur. ✅ Après remontage,
    vérifiez les spécifications dans la fiche technique Bobine d'allumage.
  S5: >-
    Erreurs frequentes avec la bobine d'allumage : - Ne pas remplacer les
    bougies d'allumage en meme temps — des bougies usees sursollicitent la
    bobine neuve et reduisent sa duree de vie- Confondre un probleme de faisceau
    avec un defaut de bobine — tester d'abord la resistance du faisceau
    d'allumage et l'etat des capuchons- Remplacer une seule bobine sur un moteur
    a bobines crayon individuelles — si une bobine a lache, les autres du meme
    age sont proches de la fin de vie- Ignorer des rates moteur intermittents
    par temps humide — signe de micro-fissure dans l'isolant de la bobine qui
    cree des arcs parasites- Ne pas verifier le connecteur electrique de la
    bobine — l'oxydation ou un clip casse provoquent un faux contact
    intermittent- Oublier d'effacer les codes defaut apres remplacement — le
    calculateur peut maintenir le mode degrade tant que l'ancien defaut est
    memorise
  S6: >-
    - Démarrer le moteur et vérifier l'absence de raté d'allumage (ralenti
    stable) - Vérifier le voyant moteur : doit s'éteindre après quelques cycles
    de démarrage - Effacer les codes défaut OBD (P030x) et vérifier qu'ils ne
    reviennent pas - Contrôler l'absence d'arc électrique autour du connecteur
    de la bobine - Faire un essai routier (accélération franche) pour confirmer
    la disparition des à-coups
  S7: >-
    Quel est le prix d'un bobine d'allumage ?Le prix varie selon le véhicule et
    la marque. Utilisez notre sélecteur pour trouver le bobine d'allumage
    compatible avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon bobine d'allumage est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un bobine d'allumage défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la
    sécurité du véhicule. Consultez la section symptômes pour évaluer l'urgence
    du remplacement.- alternateur - bougie d allumage - faisceau d allumage
  S8: >-
    Bobine d'allumage OE ou adaptable ?Privilégiez l'OE ou OES (Bosch, Denso,
    NGK). Les bobines bas de gamme ont une durée de vie réduite et peuvent
    griller rapidement. Comment savoir si ma bobine d'allumage est HS ?Raté
    moteur localisé sur un cylindre, voyant moteur + code P030x, perte de
    puissance, test à l'ohmmètre hors tolérance. Tous les combien changer les
    bobines d'allumage ?Pas de périodicité fixe. Durée de vie 100 000 à 200 000
    km. À remplacer uniquement en cas de défaut avéré (test diagnostic). Peut-on
    changer une bobine d'allumage soi-même ?Oui, opération simple sur bobines
    crayon. Débrancher le connecteur, dévisser la vis de fixation, extraire la
    bobine. 10 à 20 minutes. Quelle erreur éviter avec les bobines d'allumage
    ?Ne pas changer toutes les bobines par précaution (inutile et coûteux).
    Vérifier l'état des bougies avant de remplacer la bobine.
  META: >-
    Remplacer une bobine d'allumage HS sur la Twingo II 1.2 16v.
---

# Bobine d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Transformer la basse tension batterie en haute tension (15-40kV) pour creer l'etincelle aux bougies

**Actions principales:** transformer la tension, amplifier, generer la haute tension, alimenter les bougies, creer l'arc

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rate moteur localise sur un cylindre precis
- voyant moteur allume code p030x
- perte de puissance brutale ou progressive
- surconsommation de carburant
- odeur d essence non brulee a l echappement
- demarrage difficile par temps humide

## Procédure de Diagnostic

Pour diagnostiquer un problème de bobine d'allumage:

1. **Inspection visuelle** - Examiner l'état du bobine d'allumage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- bougie-d-allumage
- faisceau-d-allumage

## Critères de Compatibilité

Pour commander le bon bobine d'allumage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"

## FAQ

**Bobine d'allumage OE ou adaptable ?**
Privilégiez l'OE ou OES (Bosch, Denso, NGK). Les bobines bas de gamme ont une durée de vie réduite et peuvent griller rapidement.

**Comment savoir si ma bobine d'allumage est HS ?**
Raté moteur localisé sur un cylindre, voyant moteur + code P030x, perte de puissance, test à l'ohmmètre hors tolérance.

**Tous les combien changer les bobines d'allumage ?**
Pas de périodicité fixe. Durée de vie 100 000 à 200 000 km. À remplacer uniquement en cas de défaut avéré (test diagnostic).

**Peut-on changer une bobine d'allumage soi-même ?**
Oui, opération simple sur bobines crayon. Débrancher le connecteur, dévisser la vis de fixation, extraire la bobine. 10 à 20 minutes.

**Quelle erreur éviter avec les bobines d'allumage ?**
Ne pas changer toutes les bobines par précaution (inutile et coûteux). Vérifier l'état des bougies avant de remplacer la bobine.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/demarrage-batterie.md 2026-02-15 -->
### Diagnostic - Démarrage et circuit électrique

# Démarrage et circuit électrique - Diagnostic complet

## Le véhicule ne démarre pas

### Rien ne se passe (pas de bruit)
- **Batterie complètement déchargée** : Vérifier la tension aux bornes (< 11.5V = batterie HS ou déchargée). Tester avec un chargeur ou des câbles de démarrage.
- **Bornes de batterie oxydées** : Dépôt blanc-verdâtre sur les cosses. Nettoyer avec une brosse métallique et de la graisse diélectrique.
- **Fusible principal grillé** : Vérifier le fusible de démarreur dans la boîte à fusibles moteur.

### Le démarreur claque sans tourner
- **Solénoïde de démarreur usé** : Le contacteur magnétique fonctionne mais ne peut plus engager le pignon. Remplacement du démarreur nécessaire.
- **Batterie faible** : Assez de courant pour le solénoïde mais pas pour le moteur électrique. Tension entre 11.5V et 12.2V.
- **Mauvaise masse moteur** : Câble de masse entre batterie et bloc moteur corrodé ou desserré.

### Le démarreur tourne mais le moteur ne part pas
- **Problème d'alimentation carburant** : Pompe à carburant HS, filtre à carburant bouché, ou relais de pompe défaillant.
- **Problème d'allumage (essence)** : Bougies encrassées, bobine d'allumage défaillante, capteur vilebrequin HS.
- **Problème d'injection (diesel)** : Injecteurs grippés, préchauffage défaillant (surtout par temps froid), capteur PMH.

## Voyant batterie allumé

- **Alternateur défaillant** : L'alternateur ne charge plus. La batterie se vide progressivement. Vérifier la tension moteur tournant (doit être entre 13.5V et 14.5V).
- **Courroie d'alternateur lâche ou cassée** : Sifflement au démarrage, voyant batterie intermittent.
- **Régulateur de tension HS** : Surcharge ou sous-charge de la batterie.

## Chute de tension intermittente

- **Consommateur parasite** : Un équipement reste sous tension moteur coupé (autoradio, éclairage coffre, etc.). Mesurer le courant de repos (< 50mA normal).
- **Batterie en fin de vie** : Plus de 4-5 ans, la batterie perd sa capacité. Tester avec un testeur de charge.

## Quand consulter un professionnel

- Démarreur qui tourne au ralenti (bruit anormal)
- Fumée ou odeur de brûlé au niveau du démarreur
- Batterie neuve qui se décharge en moins de 48h
- Voyant batterie qui s'allume en roulant
