---
category: distribution
slug: poulie-vilebrequin
title: Poulie vilebrequin
pg_id: 3213
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
  role: Transmet le mouvement du vilebrequin aux accessoires
  must_be_true:
  - entrainer
  - transmettre
  - amortir
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
  - ❌ "plus de puissance"
  cost_range:
    min: 50
    max: 200
    currency: EUR
    unit: poulie
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE
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
    label: Vibrations moteur importantes au ralenti
    severity: confort
  - id: S2
    label: Caoutchouc de la poulie fissure ou decolle
    severity: confort
  - id: S3
    label: Courroie d accessoire qui deraille
    severity: confort
  - id: S4
    label: Bruit sourd au niveau du bas moteur
    severity: confort
  - id: S5
    label: Reperes de calage impossibles a aligner
    severity: immobilisation
  - id: S6
    label: Voyant moteur codes vibrations vilebrequin
    severity: confort
  causes:
  - verification urgente piece et alimentation
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - verifier equilibrage et fixations
  quick_checks:
  - Vibrations moteur importantes au ralenti ?
  - 'Observer : caoutchouc de la poulie fissure ou decolle ?'
  - 'Observer : courroie d accessoire qui deraille ?'
  - Bruit sourd au niveau du bas moteur ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Vibrations moteur importantes au ralenti
  - Caoutchouc de la poulie fissure ou decolle
  - Courroie d accessoire qui deraille
  - Bruit sourd au niveau du bas moteur
  - Reperes de calage impossibles a aligner
  - Voyant moteur codes vibrations vilebrequin
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '3213'
  intro_title: A quoi sert Poulie vilebrequin ?
  risk_title: Pourquoi remplacer Poulie vilebrequin a temps ?
  risk_explanation: '**Pièce HS** - Le poulie vilebrequin peut être hors service et nécessiter un remplacement'
  risk_consequences:
  - '**Pièce HS** - Le poulie vilebrequin peut être hors service et nécessiter un remplacement'
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
  - question: Poulie vilebrequin OE ou adaptable ?
    answer: Privilégiez l'OE. C'est une pièce critique pour l'équilibrage moteur. Les copies peuvent vibrer.
  - question: Comment savoir si ma poulie vilebrequin est HS ?
    answer: Vibrations importantes moteur, caoutchouc de la poulie fissuré ou décollé, courroie qui saute.
  - question: Tous les combien changer la poulie vilebrequin ?
    answer: Pas de périodicité fixe. À remplacer si fissurée ou si le caoutchouc est détérioré. Souvent 150 000+ km.
  - question: Peut-on changer la poulie vilebrequin soi-même ?
    answer: Difficile. Nécessite de bloquer le volant moteur et un extracteur. Vis centrale très serrée.
  - question: Quelle erreur éviter avec la poulie vilebrequin ?
    answer: Ne pas frapper pour démonter. Utiliser un extracteur adapté. Vérifier le repère de calage. Serrer au couple.
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
doc_id: 32f52546-4115-532e-a9eb-b621edd1a6a9
content_hash: sha256:4f67a48a7475f924
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
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_19_a: '19 a'
    val_20_a: '20 A'
    val_40_kw: '40 kW'
    val_60_kw: '60 kW'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La poulie vilebrequin (poulie damper ou poulie d''amortissement) transmet le
    mouvement de rotation du vilebrequin aux accessoires moteur via la courroie
    d''accessoire : alternateur, pompe de direction, compresseur de clim, pompe
    à eau. Elle intègre un amortisseur de vibrations torsionnelles (en
    caoutchouc ou hydraulique) qui absorbe les à-coups de combustion de chaque
    cylindre. Niveau de difficulté : Avancé — la vis centrale de la poulie est
    très serrée (200-400 Nm) et nécessite de bloquer le volant moteur. Comptez 1
    à 3 heures. Outils : clé à chocs ou rallonge longue, contre-appui volant
    moteur, extracteur de poulie (si nécessaire). Pièces liées : courroie
    d''accessoire, galet tendeur, galet enrouleur, courroie de distribution (le
    calage passe souvent par la poulie).
  S2: >-
    Pas de périodicité fixe. Durée de vie : 150 000+ km. À vérifier lors du
    changement de la distribution ou de la courroie d''accessoire. Symptômes de
    défaillance : - Vibrations moteur importantes au ralenti — l''amortisseur en
    caoutchouc est décollé ou fissuré, il ne filtre plus les vibrations
    torsionnelles- Caoutchouc de la poulie fissuré ou décollé — visible à
    l''oeil nu en soulevant le capot- Courroie d''accessoire qui déraille — la
    poulie désaxée ou voilée déporte la courroie- Bruit sourd au niveau du bas
    moteur — la partie extérieure de la poulie tourne désynchronisée du moyeu
    central- Repères de calage impossibles à aligner — la bague extérieure a
    tourné par rapport au moyeu, le calage de distribution est faussé- Voyant
    moteur avec codes vibrations vilebrequin — le capteur PMH lit des signaux
    parasites
  S3: >-
    Pour choisir la bonne poulie vilebrequin : - Type : poulie simple
    (entraînement seul), poulie damper caoutchouc (amortissement vibrations, la
    plus courante), poulie damper viscoélastique (véhicules diesel récents, plus
    sophistiquée) — ne pas interchanger- Nombre de gorges : doit correspondre
    exactement au profil de la courroie d''accessoire (poly-V 4, 5, 6 ou 7
    nervures)- Diamètre : le diamètre détermine le rapport de transmission vers
    les accessoires — une poulie de mauvais diamètre fait tourner l''alternateur
    trop vite ou trop lentement- Marques : Gates, Continental/Contitech
    (premium), Dayco, SKF, INA (standard) — c''est une pièce critique pour
    l''équilibrage moteur, éviter les copies- Budget : 50 à 200 EUR — une poulie
    OES coûte 30-40% de moins que l''OE
  S4_DEPOSE: >-
    1. Déposer la courroie d''accessoire en détendant le galet tendeur. 2.
    Bloquer le volant moteur (outil de maintien dans la couronne de démarreur ou
    bloquer en vitesse sur les manuelles). 3. Dévisser la vis/boulon central de
    la poulie (sens horaire = desserrage standard, mais certains moteurs ont un
    filetage inversé — vérifier). 4. Si la poulie ne vient pas à la main,
    utiliser un extracteur à griffes adapté au diamètre — ne JAMAIS faire levier
    avec un tournevis contre le bloc (risque de casse du carter). 5. Vérifier
    l''état de la clavette ou du clavetage sur le vilebrequin — une clavette
    cisaillée fausse le calage. 6. Nettoyer la portée du vilebrequin avant
    montage de la poulie neuve.
  S5: >-
    Erreurs fréquentes avec la poulie vilebrequin : - Utiliser une poulie simple
    à la place d''une poulie damper — le moteur vibre excessivement et la
    courroie de distribution peut sauter par à-coups- Ne pas bloquer le volant
    moteur avant de desserrer la vis centrale — la vis est serrée à 200-400 Nm,
    le vilebrequin tourne si non bloqué- Faire levier avec un tournevis contre
    le bloc moteur pour extraire la poulie — risque de casser le carter d''huile
    ou le couvre-distribution- Ne pas vérifier la clavette de positionnement —
    une clavette cisaillée ou absente permet à la poulie de tourner sur le
    vilebrequin, faussant le calage de distribution et de l''allumage- Ignorer
    un caoutchouc fissuré en se disant que la poulie tourne encore — le
    découplage soudain entre la bague extérieure et le moyeu provoque la chute
    de la courroie d''accessoire en roulant- Serrer la vis centrale au couple
    insuffisant — la poulie se desserre en fonctionnement
  S6: >-
    Après le remplacement de la poulie vilebrequin : - Couple de serrage : vis
    centrale = 200-400 Nm + angle selon constructeur (souvent 90°
    supplémentaires). Utiliser impérativement une clé dynamométrique- Calage :
    vérifier que les repères de calage de la distribution sont alignés après
    remontage — la poulie porte souvent le repère PMH- Courroie : reposer la
    courroie d''accessoire et vérifier la tension via le galet tendeur- Test
    moteur : au ralenti, les vibrations doivent avoir significativement diminué
    par rapport à l''ancienne poulie. Si les vibrations persistent, vérifier les
    supports moteur- Bruit : aucun bruit de frottement ou de cognement au niveau
    du bas moteur — un bruit indique un mauvais alignement ou une clavette mal
    positionnée
---

# Poulie vilebrequin - Guide Diagnostic Complet

## Fonction et Rôle

Transmet le mouvement du vilebrequin aux accessoires

**Actions principales:** entrainer, transmettre, amortir

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Reperes de calage impossibles a aligner**
  reperes de calage impossibles a aligner

### 🟢 Autres Symptômes

- vibrations moteur importantes au ralenti
- caoutchouc de la poulie fissure ou decolle
- courroie d accessoire qui deraille
- bruit sourd au niveau du bas moteur
- voyant moteur codes vibrations vilebrequin

## Procédure de Diagnostic

Pour diagnostiquer un problème de poulie vilebrequin:

1. **Inspection visuelle** - Examiner l'état du poulie vilebrequin
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Pièce HS** - Le poulie vilebrequin peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- capteur-impulsion
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-de-direction-assistee
- poulie-d-alternateur

## Critères de Compatibilité

Pour commander le bon poulie vilebrequin, vous devez connaître:

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

**Poulie vilebrequin OE ou adaptable ?**
Privilégiez l'OE. C'est une pièce critique pour l'équilibrage moteur. Les copies peuvent vibrer.

**Comment savoir si ma poulie vilebrequin est HS ?**
Vibrations importantes moteur, caoutchouc de la poulie fissuré ou décollé, courroie qui saute.

**Tous les combien changer la poulie vilebrequin ?**
Pas de périodicité fixe. À remplacer si fissurée ou si le caoutchouc est détérioré. Souvent 150 000+ km.

**Peut-on changer la poulie vilebrequin soi-même ?**
Difficile. Nécessite de bloquer le volant moteur et un extracteur. Vis centrale très serrée.

**Quelle erreur éviter avec la poulie vilebrequin ?**
Ne pas frapper pour démonter. Utiliser un extracteur adapté. Vérifier le repère de calage. Serrer au couple.
