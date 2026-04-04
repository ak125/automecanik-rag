---
category: distribution
slug: poulie-d-arbre-a-came
title: Poulie d'arbre à came
pg_id: 1067
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
  role: Entrainer l'arbre a cames en synchronisation avec le vilebrequin
  must_be_true:
  - entrainer
  - synchroniser
  - transmettre
  must_not_contain:
  - vilebrequin
  - accessoire
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - courroie-de-distribution
  - kit-de-distribution
  - galet-tendeur-de-courroie-de-distribution
  - galet-enrouleur-de-courroie-de-distribution
  - pompe-a-eau
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
  - ❌ "repare le moteur"
  cost_range:
    min: 40
    max: 150
    currency: EUR
    unit: poulie
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE — equipementiers distribution
  - tier: Adaptable
  brands:
    premium:
    - Gates
    - Continental/Contitech
    standard:
    - Dayco
    - SKF
    - INA
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Bruit de claquement au niveau de la culasse
    severity: confort
  - id: S2
    label: Perte de puissance progressive
    severity: confort
  - id: S3
    label: Moteur qui cale au ralenti
    severity: immobilisation
  - id: S4
    label: Fumee anormale a l echappement
    severity: confort
  - id: S5
    label: Voyant moteur allume codes calage
    severity: immobilisation
  - id: S6
    label: Distribution a remplacer selon carnet d entretien
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  quick_checks:
  - Bruit de claquement au niveau de la culasse ?
  - 'Observer : perte de puissance progressive ?'
  - 'Observer : moteur qui cale au ralenti ?'
  - 'Observer : fumee anormale a l echappement ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Bruit de claquement au niveau de la culasse
  - Perte de puissance progressive
  - Moteur qui cale au ralenti
  - Fumee anormale a l echappement
  - Voyant moteur allume codes calage
  - Distribution a remplacer selon carnet d entretien
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '1067'
  intro_title: A quoi sert Poulie d'arbre à came ?
  risk_title: Pourquoi remplacer Poulie d'arbre à came a temps ?
  risk_explanation: '**Pièce HS** - Le poulie d''arbre à came peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le poulie d''arbre à came peut être hors service et nécessiter un remplacement'
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
  - question: Poulie d'arbre à came OE ou adaptable ?
    answer: Privilégiez l'OE ou le kit distribution complet. C'est une pièce critique pour le calage moteur.
  - question: Comment savoir si ma poulie d'arbre à came est HS ?
    answer: Bruit de claquement moteur, calage distribution décalé, perte de puissance, moteur qui cale.
  - question: Tous les combien changer la poulie d'arbre à came ?
    answer: À chaque remplacement du kit de distribution (80 000 à 120 000 km selon véhicule). Jamais seule.
  - question: Peut-on changer la poulie d'arbre à came soi-même ?
    answer: Déconseillé sans expérience. Nécessite de caler la distribution. Erreur = destruction moteur.
  - question: Quelle erreur éviter avec la poulie d'arbre à came ?
    answer: Ne jamais réutiliser une poulie usée. Respecter les repères de calage. Serrer au couple exact.
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
doc_id: 3d6efecb-2f0a-58ca-9791-bbdbd6561d53
content_hash: sha256:9d6cc5f8a6607b99
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
  area: Face laterale du moteur, derriere le carter de distribution
  access: Depose courroie accessoire + carter distribution
  adjacent_parts:
  - courroie
  - galets
  - pompe a eau
  - poulie
installation:
  difficulty: difficile (pro recommande)
  time: 3h a 6h
  tools:
  - kit calage distribution
  - cle dynamometrique
  - extracteur poulie
  prerequisite: Moteur cale au PMH, ne pas tourner le moteur sans courroie
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'composite'
    source_ref: corpus RAG web OEM
  - type: 'plein'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_20__: '20 %'
    val_35__: '35 %'
    val_65__: '65 %'
    val_70__: '70 %'
    val_80__: '80 %'
    val_85__: '85 %'
    val_99__: '99 %'
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le rôle de la poulie d''arbre à cames est de transformer le mouvement du vilebrequin à travers la courroie de distribution
    ou la chaîne de distribution à l''arbre à cames pour commander l''ouverture et la fermeture des soupapes d''admission
    et des soupapes d''échappement. Une poulie d''arbre à cames est sous forme d''une roue dentée composée de plusieurs dents
    ou se fixe la courroie ou la chaîne de distribution pour mettre en mouvement les arbres à cames après le démarrage du
    moteur. Le nombre des poulies d''arbre à cames ça change d''un moteur à autre selon le nombre d''arbre à cames. Un moteur
    peut comporter soit un ou deux ou quatre arbre à cames puisque sa dépend de nombres de soupapes au niveau du moteur par
    exemple un moteur V6 comporte 4 arbre à cames. En savoir plus : poulie d''arbre à came — définition et rôle mécanique
    🚨 Bruit Poulie d''arbre à came : causes et diagnostic'
  S2: 'Une poulie d''arbre à cames défectueuse présente plusieurssymptômes : - Bruit auniveau du moteur. - Mauvais fonctionnementdes
    soupapes (dosage air/carburant pas bien au niveau de chemise). - Faible puissance du moteur. - Le moteur ne fonctionne
    pas. Une poulied''arbre à cames usée et qu''elle n''est pas remplacée à temps peut causer plusieursproblèmes : - Casse
    des arbres à cames. - Usure des injecteurs. - Usure des soupapes. Diagnostic complet : identifier une panne de poulie
    d''arbre à came'
  S3: 'La poulie d''arbre à cames est la pièce de synchronisation qui relie la courroie ou la chaîne de distribution à l''arbre
    à cames, garantissant que l''ouverture et la fermeture des soupapes se produisent exactement au bon moment par rapport
    au déplacement des pistons. Un calage approximatif de 2° suffit à dégrader sensiblement les performances et la consommation
    ; un décalage de 10° ou plus peut provoquer l''impact pistons-soupapes et la destruction moteur sur les moteurs à interférence.
    Sur les systèmes à calage variable (VVT/VTC), la poulie intègre un mécanisme hydraulique qui exige une précision de référence
    absolue. - Poulie fixe vs poulie à déphaseur VVT/VTC — Les moteurs modernes à gestion variable de la distribution (VTEC
    Honda, VANOS BMW, VarioCam Porsche, VVT-i Toyota) utilisent des déphaseurs hydrauliques pilotés par l''ECU via la pression
    d''huile. Ces composants ne sont pas interchangeables avec une poulie fixe et exigent une référence OEM stricte. - Angle
    de calage et repères — Chaque poulie d''arbre à cames comporte un repère de calage (encoche, trait, trou) qui doit s''aligner
    exactement avec le repère de la culasse au point mort haut (PMH). Vérifier que la poulie de remplacement dispose du même
    repère à la même position angulaire que l''originale. - Nombre de dents et pas — Le nombre de dents de la poulie (par
    exemple 19, 21, 23 dents selon le moteur) et le pas de la courroie de distribution (pas de 9,525 mm / 3/8'' pour une courroie
    crantée standard) doivent correspondre parfaitement à la courroie ou à la chaîne en place. Une dent de différence décale
    le calage de façon inacceptable. - Matériau et traitement de surface — Les poulies en aluminium anodisé sont légères et
    résistantes à la corrosion. Certaines poulies sont en acier traité pour une meilleure résistance à l''usure des dents.
    Ne pas remplacer une poulie acier par une poulie aluminium générique sans vérifier les tolérances de jeu flanc à flanc
    avec la courroie. - Vis de fixation de la poulie sur l''arbre — La vis centrale de fixation de la poulie d''arbre à cames
    est une vis TTY (Torque-To-Yield) sur la majorité des moteurs récents : elle ne doit pas être réutilisée après desserrage.
    Prévoir une vis neuve de remplacement avec le couple de serrage et l''angle de serrage constructeur (ex. : 50 N·m + 60°).
    - Remplacement dans le cadre d''une révision distribution complète — La poulie d''arbre à cames est accessible uniquement
    après dépose du carter de distribution. Profiter de cette intervention pour remplacer simultanément la courroie de distribution,
    les galets tendeurs, la pompe à eau (si entraînée par la distribution) et le joint de couvre- culasse. Ces pièces partagent
    la même fenêtre de main-d''œuvre. - Marque, modèle, année, code moteur et puissance — Le code moteur (P.5 carte grise)
    est la donnée déterminante. Sur les moteurs à déphaseur VVT, la puissance en kW permet de distinguer les variantes de
    déphaseurs (angle de rotation différent selon la cartographie moteur). Ne jamais commander sans ce code. Pour aller plus
    loin : consultez notre guide d''achat poulie d''arbre à came — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Poulie d'arbre à came pour connaître les spécifications. -
    Calez le véhicule. - Débranchez labatterie. - Démontez le cache moteur. - Vidangez leliquide de refroidissement. - Démontez
    lacourroie d'accessoires. - Démontez lacourroie de distribution. - Bloquez l'arbre àcames avec un outil de blocage. -
    Démontez la fixationde la poulie d'arbre à cames. - Démontez la poulied'arbre à cames.
  S4_REPOSE: '- Vérifiez que lapoulie d''arbre à cames neuf est identique à celle démontée. - Remontez lepignon d''arbre à
    cames et serrez les fixations. - Démontez l''outilde blocage de l''arbre à cames. - Remontez lescourroies de distribution
    et d''accessoires. - Contrôlez le boncalage de la courroie de distribution . - Remplir leliquide de refroidissement. -
    Rebranchez labatterie. - Contrôlez lefonctionnement du moteur. ✅ Après remontage, vérifiez les spécifications dans la
    fiche technique Poulie d''arbre à came .'
  S5: 'Erreurs frequentes avec la poulie d''arbre a cames : - Ne pas bloquer le vilebrequin et l''arbre a cames avant depose
    — le moteur perd son calage de distribution et risque la casse des soupapes au remontage- Reutiliser le boulon central
    de la poulie — ce boulon est souvent a usage unique (etirement controle) et doit etre remplace- Confondre poulie d''arbre
    a cames admission et echappement sur les moteurs a double arbre — les deux poulies ne sont pas interchangeables- Ne pas
    verifier le jeu de la clavette ou de la goupille de positionnement — une clavette usee provoque un decalage de calage
    meme avec une poulie neuve- Ignorer un bruit de claquement au ralenti cote distribution — signe de poulie fissuree ou
    de moyeu use'
  S6: 'La poulie d''arbre à came (pignon de calage) synchronise la rotation de l''arbre à cames avec le vilebrequin via la
    courroie ou la chaîne de distribution. Un calage incorrect de un seul degré peut provoquer des à-coups, une perte de puissance
    ou, sur moteur interférence, un contact pistons/soupapes. Les contrôles post-remplacement sont donc particulièrement rigoureux.
    - Calage de la distribution vérifié aux repères constructeur : après pose, faire tourner le moteur à la main sur 720 °
    (deux tours de vilebrequin) et reconfirmer l''alignement de la marque sur la poulie d''arbre à came avec le repère fixe
    du cache de distribution ou de la culasse. Toute déviation impose un recalage immédiat avant démarrage. - Couple de serrage
    du boulon central respecté : le boulon de poulie d''arbre à came est un élément critique — souvent à usage unique sur
    les moteurs récents (vis à serrage angulaire). Le couple est généralement élevé : 60 à 120 N·m suivi d''un angle de 45
    à 90 ° selon le constructeur. Utiliser un dynamomètre calibré et une vis neuve si prescrit. - Absence de codes défaut
    de calage : après démarrage, brancher l''outil de diagnostic et vérifier l''absence de codes P0016 (corrélation de position
    arbre à cames/vilebrequin, bancA), P0017 (banc B), P0340 ou P0345 (capteur de phase arbre à cames). Ces codes confirment
    un problème de calage ou un capteur de position à repositionner. - Absence de claquement au niveau de la culasse : au
    démarrage à froid, écouter la culasse pendant les premières secondes. Un claquement rythmique (au rythme du moteur divisé
    par 2) indique un problème de calage ou un patin de chaîne en contact anormal avec la poulie. Couper le moteur immédiatement
    si le bruit est franc. - Régime moteur stable et absence de calage au ralenti : laisser le moteur monter en température
    et observer la stabilité du régime de ralenti (750 à 850 tr/min selon moteur). Un ralenti instable ou des calages répétés
    après remplacement de la poulie signalent un calage incorrect ou un problème du capteur de phase à couplage serré avec
    la poulie (systèmes VVT/VANOS). - Contrôle du déphaseur (système VVT si équipé) : sur les moteurs à calage variable (VVT,
    VANOS, VTEC), vérifier via l''outil de diagnostic que le déphaseur répond aux commandes du calculateur moteur en temps
    réel. La valeur de décalage doit évoluer de façon continue entre 0 et la valeur maximale (souvent 40 à 60 °) lors d''une
    montée progressive en régime de 1 000 à 4 000 tr/min.'
  S7: Quel est le prix d'un poulie d'arbre à came ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur
    pour trouver le poulie d'arbre à came compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment
    savoir si mon poulie d'arbre à came est à changer ?Les signes d'usure les plus courants sont détaillés dans la section
    diagnostic ci-dessus. En cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un poulie d'arbre
    à came défaillant ?Cela dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l'urgence du remplacement.- entrainer - synchroniser - transmettre
  S8: Comment choisir Poulie d'arbre à came compatible avec mon vehicule ?Renseignez marque, modele, type moteur et annee,
    puis verifiez la reference Quand remplacer Poulie d'arbre à came ?En cas de bruit de claquement au niveau de la culasse
    ou de degradation Puis-je monter Poulie d'arbre à came sans verification atelier ?Le montage peut exiger controles de
    couple, alignement et references.
  META: '{"meta_title":"Poulie d''arbre à came : guide remplacement distribution","meta_description":"Bruit de claquement
    moteur, voyant calage allumé ou distribution à réviser ? Découvrez quand changer la poulie d''arbre à came et les risques
    d''un remplacement manqué."}'
---

# Poulie d'arbre à came - Guide Diagnostic Complet

## Fonction et Rôle

Entrainer l'arbre a cames en synchronisation avec le vilebrequin

**Actions principales:** entrainer, synchroniser, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au ralenti**
  moteur qui cale au ralenti
- **Voyant moteur allume codes calage**
  voyant moteur allume codes calage

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement au niveau de la culasse**
  bruit de claquement au niveau de la culasse

### 🟢 Autres Symptômes

- perte de puissance progressive
- fumee anormale a l echappement
- distribution a remplacer selon carnet d entretien

## Procédure de Diagnostic

Pour diagnostiquer un problème de poulie d'arbre à came:

1. **Inspection visuelle** - Examiner l'état du poulie d'arbre à came
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le poulie d'arbre à came peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- arbre-a-came
- capteur-impulsion
- chaine-de-distribution
- courroie-de-distribution
- kit-de-chaine-de-distribution
- kit-de-distribution

## Critères de Compatibilité

Pour commander le bon poulie d'arbre à came, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"

## FAQ

**Poulie d'arbre à came OE ou adaptable ?**
Privilégiez l'OE ou le kit distribution complet. C'est une pièce critique pour le calage moteur.

**Comment savoir si ma poulie d'arbre à came est HS ?**
Bruit de claquement moteur, calage distribution décalé, perte de puissance, moteur qui cale.

**Tous les combien changer la poulie d'arbre à came ?**
À chaque remplacement du kit de distribution (80 000 à 120 000 km selon véhicule). Jamais seule.

**Peut-on changer la poulie d'arbre à came soi-même ?**
Déconseillé sans expérience. Nécessite de caler la distribution. Erreur = destruction moteur.

**Quelle erreur éviter avec la poulie d'arbre à came ?**
Ne jamais réutiliser une poulie usée. Respecter les repères de calage. Serrer au couple exact.


## References supplementaires

<!-- materialized-from-db manual/25dec5f35b7f 2026-04-03 -->
### Données techniques OEM — Poulie d'arbre à came

# Données techniques OEM — Poulie d'arbre à came
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- composite
- plein

## Matériaux
- aluminium

## Valeurs techniques de référence
- 20 %
- 35 %
- 65 %
- 70 %
- 80 %
- 85 %
- 99 %
