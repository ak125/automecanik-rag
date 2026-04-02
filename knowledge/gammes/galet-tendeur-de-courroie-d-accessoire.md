---
category: distribution
slug: galet-tendeur-de-courroie-d-accessoire
title: Galet tendeur de courroie d'accessoire
pg_id: 310
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
  last_enriched_by: skill:phase5-gates-skf-trw
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Maintient la tension de la courroie d'accessoire
  must_be_true:
  - tendre
  - maintenir
  - guider
  must_not_contain:
  - freinage
  - climatisation
  - turbo
  - injection
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
  - ❌ "plus de durée de vie"
  cost_range:
    min: 15
    max: 84
    currency: EUR
    unit: l'unite
    source: historique commandes automecanik
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
    label: Sifflement de la courroie
    severity: confort
  - id: S2
    label: Bruit de roulement cote accessoires
    severity: confort
  - id: S3
    label: Courroie qui patine temoin batterie
    severity: confort
  - id: S4
    label: Galet qui ne bouge plus tendeur bloque
    severity: immobilisation
  - id: S5
    label: Vibrations dans le moteur
    severity: confort
  - id: S6
    label: Bruit de claquement courroie detendue
    severity: confort
  - id: S7
    label: Courroie qui saute de son logement
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - verifier equilibrage et fixations
  quick_checks:
  - 'Observer : sifflement de la courroie ?'
  - Bruit de roulement cote accessoires ?
  - 'Observer : courroie qui patine temoin batterie ?'
  - 'Observer : galet qui ne bouge plus tendeur bloque ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Sifflement de la courroie
  - Bruit de roulement cote accessoires
  - Courroie qui patine temoin batterie
  - Galet qui ne bouge plus tendeur bloque
  - Vibrations dans le moteur
  - Bruit de claquement courroie detendue
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '310'
  intro_title: A quoi sert Galet tendeur de courroie d'accessoire ?
  risk_title: Pourquoi remplacer Galet tendeur de courroie d'accessoire a temps ?
  risk_explanation: '**Pièce HS** - Le galet tendeur de courroie d''accessoire peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le galet tendeur de courroie d''accessoire peut être hors service et nécessiter un remplacement'
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
  - question: Comment savoir si le tendeur est HS ?
    answer: Vérifiez s'il bouge librement (ressort interne). Un tendeur bloqué ne compense plus l'usure de la courroie. Bruit
      de roulement = roulement HS.
  - question: Peut-on changer le galet sans la courroie ?
    answer: Oui si la courroie est récente. Mais généralement, on change les deux ensemble car l'accès est le même.
  - question: Tendeur manuel ou automatique ?
    answer: La plupart des véhicules modernes ont un tendeur automatique à ressort. Les anciens ont un tendeur manuel à régler.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Forcer sur un tendeur automatique. Mal positionner le tendeur au remontage. Ignorer le bruit de roulement.
  - question: Comment faire un diagnostic rapide ?
    answer: Tendeur qui ne bouge pas → ressort cassé ou galet grippé. Bruit de roulement → galet à changer. Courroie détendue
      → vérifier tendeur en premier.
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
doc_id: df592e24-cc02-5e3c-9198-a7b9601c2485
content_hash: sha256:7324a68d44a7080c
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
  _source: Gates / SKF / TRW-ZF (donnees techniques constructeur)
  _validation_status: oem_verified
  _enriched_at: '2026-03-30'
  types_variants:
  - type: Galet tendeur a ressort
    description: Tension automatique par ressort interne, compensation usure courroie
    era: standard actuel
  - type: Galet tendeur mecanique
    description: Reglage manuel par vis, ancien systeme
    era: avant 2000
  technical_notes:
    roulement: 'roulement a billes etanche, graisse longue duree'
    remplacement: 'obligatoire a chaque changement de courroie — roulement fatigue meme si silencieux'
    diagnostic_bruit: 'sifflement = courroie, grondement = roulement galet'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le rôle dugalet tendeur d'accessoires est assuré la tension de la courroie
    etréduire les vibrations. Le réglage de la tension de la courroie se
    faitmanuellement ou automatiquement suivant le type du galet tendeur. Il
    existe deuxtypes de galet tendeur : - Galet tendeur mécanique est composé
    d'un ressort de torsion etd'éléments de friction. - Galet tendeur
    hydrauliqueest composé d'un ressort de compression et d'un circuit
    hydraulique où unfluide est forcé par un orifice calibré En savoir plus :
    galet tendeur de courroie d'accessoire — définition et rôle mécanique 🚨
    Bruit Galet tendeur de courroie d'accessoire : causes et diagnostic
  S2: >-
    Symptômes d'un galet tendeur de courroie d'accessoire défaillant : Symptômes
    sonores : - Sifflement aigu au démarrage — le galet tendeur ne maintient
    plus la tension, la courroie patine. Le bruit disparaît souvent à chaud. -
    Bruit de roulement côté accessoires — grondement sourd qui augmente avec le
    régime. Le roulement du galet est usé. - Claquement rythmique — courroie
    détendue qui fouette. Risque de saut sur les poulies. Symptômes visuels : -
    Courroie fissurée ou vitrifiée — un tendeur bloqué provoque un patinage qui
    lustre la courroie. - Galet qui ne bouge plus — le ressort ou le mécanisme
    de tension est cassé. La courroie n'a plus de tension automatique. - Traces
    de poussière noire autour du galet — usure du roulement ou frottement de la
    courroie. Symptômes indirects : - Témoin de batterie allumé — la courroie
    patine sur la poulie d'alternateur → charge insuffisante. - Direction
    assistée lourde par intermittence — la pompe de DA est sous-entraînée. -
    Vibrations moteur — le déséquilibre du galet se transmet au bloc. ⚠️ Un
    galet tendeur bloqué peut entraîner la rupture de la courroie d'accessoire,
    ce qui coupe alternateur, DA et climatisation en roulant.
  S3: >-
    Pour choisir les bons galet tendeur de courroie d accessoire pour votre
    véhicule : - Marque de votre véhicule - Modele de votre véhicule - Annee de
    votre véhicule - Vérifier : sifflement de la courroie - Vérifier : bruit de
    roulement cote accessoires - Vérifier : courroie qui patine temoin batterie
    - Vérifier : galet qui ne bouge plus tendeur bloque - Vérifier : vibrations
    dans le moteur - Vérifier : bruit de claquement courroie detendue - Vérifier
    : courroie qui saute de son logement - Vérifier : Galet qui ne bouge plus
    tendeur bloque - Vérifier : Bruit de claquement courroie detendue
  S4_DEPOSE: >-
    Procédure de diagnostic d'un galet tendeur : 1. Contrôle visuel moteur
    arrêté : - Vérifier l'état de la courroie : fissures, glaçage, flancs usés.
    - Vérifier que le galet tourne librement à la main — il ne doit pas gripper
    ni avoir de jeu axial. - Rechercher des traces de poussière noire (usure
    roulement). 2. Test de tension : - Appuyer sur le brin le plus long de la
    courroie : la flèche ne doit pas dépasser 10-15 mm. Au-delà, le tendeur ne
    fait plus son travail. - Sur les tendeurs automatiques : vérifier que le
    ressort rappelle bien le galet en position. 3. Test sonore moteur tournant :
    - Sifflement aigu = courroie qui patine (tension insuffisante). - Grondement
    sourd = roulement du galet usé. - Utiliser un stéthoscope mécanique sur le
    galet pour isoler le bruit. 4. Test de rotation : - Déposer la courroie et
    faire tourner le galet seul. Il doit tourner silencieusement, sans point dur
    ni jeu radial.
  S4_REPOSE: >-
    - Vérifiez que le galet tendeur neuf est identique à celui démonté. -
    Remplacez la courroie d'accessoires. - Remontez le galet tendeur. - Serrez
    la fixation du galet tendeur. - Mettre en place la courroie d'accessoires en
    respectant le cheminement. - Rebranchez la batterie. ✅ Après remontage,
    vérifiez les spécifications dans la fiche technique Galet tendeur de
    courroie d'accessoire .
  S5: >-
    Erreurs fréquentes avec le galet tendeur de courroie d'accessoire : - ❌
    Changer la courroie sans changer le galet — un galet usé détruira la
    courroie neuve en quelques milliers de km. Toujours remplacer galet +
    courroie ensemble. - ❌ Oublier le galet enrouleur — il y a souvent 2 galets
    : le tendeur (avec ressort) et l'enrouleur (lisse). Les deux s'usent
    ensemble. - ❌ Forcer le tendeur automatique — utiliser l'outil spécifique
    (clé de déverrouillage) pour comprimer le ressort. Ne pas utiliser un
    tournevis. - ❌ Mal repositionner la courroie — un décalage d'une gorge sur
    la poulie d'alternateur ou de DA provoque un sifflement immédiat et une
    usure rapide. - ❌ Ignorer le témoin de batterie — c'est souvent le premier
    signe d'un galet/courroie défaillant, pas un problème d'alternateur.
  S6: >-
    Une fois le galet tendeur de courroie d'accessoire remplacé, effectuez ces
    contrôles avant de remettre le véhicule en circulation. La courroie
    d'accessoire entraîne des organes vitaux (alternateur , pompe de direction,
    compresseur de climatisation ) : un montage insuffisamment vérifié peut
    conduire à une immobilisation rapide. - Contrôle visuel de la tension
    courroie : la courroie ne doit pas présenter de jeu excessif ni être trop
    tendue. Sur la branche libre la plus longue, une pression du pouce doit
    engendrer une flexion de 5 à 10 mm maximum selon les préconisations
    constructeur — au-delà, le tendeur est mal positionné. - Vérification du
    couple de serrage : confirmer que l'axe du galet est serré au couple
    constructeur (généralement 20 à 50 N·m selon le moteur). Un boulon
    insuffisamment serré provoque un desserrage et une dérive de la courroie à
    chaud. - Test au démarrage — écoute sonore : démarrer le moteur et laisser
    tourner au ralenti 2 minutes. Aucun sifflement, aucun couinement ni bruit de
    roulement ne doit être audible côté accessoires. Un bruit persistant indique
    un problème d'alignement ou un galet défectueux. - Contrôle visuel courroie
    après 5 minutes de fonctionnement : stopper le moteur, vérifier que la
    courroie n'a pas déjaugé de son logement, que les nervures sont bien
    engagées sur toutes les poulies et que le galet ne présente pas de jeu
    latéral perceptible à la main. - Contrôle de la charge alternateur : mesurer
    la tension de charge au voltmètre — entre 13,8 V et 14,4 V moteur tournant.
    Une valeur hors de cette plage signale que la courroie patine ou que
    l'alternateur n'est pas correctement entraîné. - Vérification des pièces
    associées : inspecter l'état du galet enrouleur, de la poulie d'alternateur
    et de la poulie de vilebrequin. Un composant adjacent usé peut transmettre
    des vibrations à la nouvelle courroie et provoquer une usure prématurée. -
    Second contrôle à froid (30 minutes après arrêt) : revérifier que le boulon
    de fixation du tendeur est toujours correctement serré et qu'aucune trace
    d'échauffement anormal n'est visible sur le galet, la courroie ou les
    surfaces de contact.
  S_GARAGE: >-
    Nous vous recommandons de confier cette intervention à un professionnel : -
    Plusieurs causes possibles de défaillance (4 identifiées) nécessitent un
    diagnostic professionnel Un garagiste qualifié dispose de l'outillage et de
    l'expérience nécessaires pour effectuer cette opération en toute sécurité.
  S7: >-
    Quel est le prix d'un galet tendeur de courroie d'accessoire ?Le prix varie
    selon le véhicule et la marque. Utilisez notre sélecteur pour trouver le
    galet tendeur de courroie d'accessoire compatible avec votre véhicule et
    comparer les tarifs des différents équipementiers.Comment savoir si mon
    galet tendeur de courroie d'accessoire est à changer ?Les signes d'usure les
    plus courants sont détaillés dans la section diagnostic ci-dessus. En cas de
    doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un
    galet tendeur de courroie d'accessoire défaillant ?Cela dépend de la gravité
    du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule.
    Consultez la section symptômes pour évaluer l'urgence du remplacement.-
    alternateur - compresseur de climatisation - courroie d accessoire - galet
    enrouleur de courroie d accessoire - pompe de direction assistee - poulie d
    alternateur - poulie vilebrequin
  S8: >-
    Comment savoir si le tendeur est HS ?Vérifiez s'il bouge librement (ressort
    interne). Un tendeur bloqué ne compense plus l'usure de la courroie. Bruit
    de roulement = roulement HS. Peut-on changer le galet sans la courroie ?Oui
    si la courroie est récente. Mais généralement, on change les deux ensemble
    car l'accès est le même. Tendeur manuel ou automatique ?La plupart des
    véhicules modernes ont un tendeur automatique à ressort. Les anciens ont un
    tendeur manuel à régler. Quelles sont les erreurs fréquentes à éviter
    ?Forcer sur un tendeur automatique. Mal positionner le tendeur au remontage.
    Ignorer le bruit de roulement. Comment faire un diagnostic rapide ?Tendeur
    qui ne bouge pas → ressort cassé ou galet grippé. Bruit de roulement → galet
    à changer. Courroie détendue → vérifier tendeur en premier.
  META: >-
    {"meta_title":"Galet tendeur courroie accessoire : changer ? |
    AutoMecanik","meta_description":"Sifflement de courroie, bruit de roulement
    ou galet tendeur bloqué ? Votre tendeur est défaillant. Guide diagnostic,
    symptômes et compatibilité par véhicule."}
---

# Galet tendeur de courroie d'accessoire - Guide Diagnostic Complet

## Fonction et Rôle

Maintient la tension de la courroie d'accessoire

**Actions principales:** tendre, maintenir, guider

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Galet qui ne bouge plus tendeur bloque**
  galet qui ne bouge plus tendeur bloque

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement courroie detendue**
  bruit de claquement courroie detendue

### 🟢 Autres Symptômes

- sifflement de la courroie
- bruit de roulement cote accessoires
- courroie qui patine temoin batterie
- vibrations dans le moteur
- courroie qui saute de son logement

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet tendeur de courroie d'accessoire:

1. **Inspection visuelle** - Examiner l'état du galet tendeur de courroie d'accessoire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le galet tendeur de courroie d'accessoire peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- pompe-de-direction-assistee
- poulie-d-alternateur
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon galet tendeur de courroie d'accessoire, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de durée de vie"

## FAQ

**Comment savoir si le tendeur est HS ?**
Vérifiez s'il bouge librement (ressort interne). Un tendeur bloqué ne compense plus l'usure de la courroie. Bruit de roulement = roulement HS.

**Peut-on changer le galet sans la courroie ?**
Oui si la courroie est récente. Mais généralement, on change les deux ensemble car l'accès est le même.

**Tendeur manuel ou automatique ?**
La plupart des véhicules modernes ont un tendeur automatique à ressort. Les anciens ont un tendeur manuel à régler.

**Quelles sont les erreurs fréquentes à éviter ?**
Forcer sur un tendeur automatique. Mal positionner le tendeur au remontage. Ignorer le bruit de roulement.

**Comment faire un diagnostic rapide ?**
Tendeur qui ne bouge pas → ressort cassé ou galet grippé. Bruit de roulement → galet à changer. Courroie détendue → vérifier tendeur en premier.
