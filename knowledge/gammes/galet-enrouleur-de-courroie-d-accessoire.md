---
category: distribution
slug: galet-enrouleur-de-courroie-d-accessoire
title: Galet enrouleur de courroie d'accessoire
pg_id: 312
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
  last_enriched_by: skill:phase5-vague6-final
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Guide la courroie d'accessoire
  must_be_true:
  - guider
  - enrouler
  - maintenir
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
    max: 45
    currency: EUR
    unit: galet
    source: catalogue automecanik
  quality_tiers:
  - tier: Qualité Origine (OE)
    description: Galets enrouleurs fournis en première monte par les équipementiers des constructeurs. Roulement à billes
      haute précision, surface de contact lisse et traitée.
  - tier: Équivalent Qualité Origine
    description: Galets de qualité comparable à l'OE, fabriqués selon les mêmes normes dimensionnelles. Roulement de précision
      et revêtement de guidage conformes.
  - tier: Adaptable Économique
    description: Galets enrouleurs aux dimensions compatibles pour un usage standard. Vérifier le diamètre intérieur, extérieur
      et la largeur avant commande.
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
    label: Courroie d accessoire visiblement usee ou fissuree
    severity: confort
  - id: S2
    label: Sifflement ou grondement au niveau de la courroie
    severity: confort
  - id: S3
    label: Perceptible faisant tourner galet main
    severity: confort
  - id: S4
    label: Perte de tension de la courroie
    severity: confort
  - id: S5
    label: Odeur de caoutchouc chaud
    severity: confort
  - id: S6
    label: Plus de 80 000 km depuis le dernier changement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - remplacement preventif recommande
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'kilometrage eleve ou usure visible : remplacement preventif recommande'
  quick_checks:
  - 'Observer : courroie d accessoire visiblement usee ou fissuree ?'
  - 'Observer : sifflement ou grondement au niveau de la courroie ?'
  - 'Observer : perceptible faisant tourner galet main ?'
  - 'Observer : perte de tension de la courroie ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Courroie d accessoire visiblement usee ou fissuree
  - Sifflement ou grondement au niveau de la courroie
  - Perceptible faisant tourner galet main
  - Perte de tension de la courroie
  - Odeur de caoutchouc chaud
  - Plus de 80 000 km depuis le dernier changement
  good_practices:
  - Respecter strictement l intervalle constructeur (rupture = casse moteur)
  - Remplacer le kit complet (courroie + galets + pompe a eau si entrainee)
  - Controler la pompe a eau et le thermostat lors du remplacement
  - Ne jamais reutiliser les pieces de distribution demontees
rendering:
  pgId: '312'
  intro_title: A quoi sert Galet enrouleur de courroie d'accessoire ?
  risk_title: Pourquoi remplacer Galet enrouleur de courroie d'accessoire a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé'
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
  - question: Galet enrouleur OE ou adaptable ?
    answer: Les galets OES (SKF, INA, Gates) sont fiables. Vérifiez le diamètre et le type de roulement.
  - question: Comment savoir si mon galet enrouleur est HS ?
    answer: Sifflement ou grondement au niveau de la courroie, jeu perceptible à la main, roulement rugueux.
  - question: Tous les combien changer le galet enrouleur ?
    answer: À chaque changement de courroie d'accessoire (60 000 à 100 000 km). Ne jamais réutiliser un ancien galet.
  - question: Peut-on changer le galet enrouleur soi-même ?
    answer: Oui, opération accessible. Détendre la courroie, dévisser le galet, monter le neuf. 30 min à 1h.
  - question: Quelle erreur éviter avec le galet enrouleur ?
    answer: Ne pas oublier de vérifier le tendeur aussi. Respecter le cheminement de la courroie. Vérifier l'alignement.
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
doc_id: 316d28e0-3d97-57fa-b485-f8861c4f40fb
content_hash: sha256:6f4ca5630fe6c6ef
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
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    role: "guide le cheminement de la courroie d'accessoire (pas de tension — c'est le tendeur qui tend)"
    remplacement: 'systematique avec la courroie — roulement fatigue = bruit + risque de blocage'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Le galet enrouleur de courroie d'accessoires est sous forme d'une poulie
    avec ou sans étrier qui permettent le guidage correct de la courroie
    d'accessoires dans sa trajectoire. Dans le cheminement la courroie
    d'accessoire on utilise un galet enrouleur qui a pour but d'assurer
    l'alignement de la courroie d'accessoires. On peut trouver plus qu'un galet
    enrouleur au niveau du montage de la courroie d'accessoires puisque sa
    dépend de la longueur de la courroie. Tournant sur son axe grâce à un
    mécanisme à roulement, il fait appui, selon les cas, à l'intérieur ou à
    l'extérieur de la courroie. En savoir plus : galet enrouleur de courroie
    d'accessoire — définition et rôle mécanique 🚨 Bruit Galet enrouleur de
    courroie d'accessoire : causes et diagnostic
  S2: >-
    Un galet enrouleur défectueuxprésente plusieurs symptômes : - Courroie
    d'accessoires qui siffle. - Courroie d'accessoires détendu. - Un jeu au
    niveau du galet enrouleur. Un galet enrouleur usé etqu'il n'est pas remplacé
    à temps peut provoquer plusieurs problèmes : - Rupture de la courroie
    d'accessoires. - Rupture du vilebrequin. - Usure de la poulie de
    vilebrequin, de la poulie d'alternateur , de le poulie de compresseur de
    climatisation , de la poulie de la pompe de direction assistée ....
    Diagnostic complet : identifier une panne de galet enrouleur de courroie
    d'accessoire
  S3: >-
    Le galet enrouleur de courroie d'accessoire guide et maintient la tension de
    la courroie qui entraîne l'alternateur, la pompe de direction assistée, le
    compresseur de climatisation et parfois la pompe à eau. Un galet défaillant
    (roulement grippé, jeu axial excessif) provoque des sifflement
    caractéristiques, use prématurément la courroie et peut conduire à sa
    rupture, entraînant la panne simultanée de l'alternateur et du
    refroidissement. Voici les critères de sélection à respecter. - Référence
    constructeur et code moteur — La géométrie du galet (diamètre extérieur,
    largeur de gorge, profil de gorge : poly-V 6PK ou 7PK, plat) est définie par
    le constructeur pour chaque motorisation. Le code moteur (ex. : N47, EA189,
    9HZ) est indispensable pour identifier la référence exacte, car deux
    véhicules de même modèle avec des motorisations différentes peuvent utiliser
    des galets de diamètres différents. - Type de roulement intégré et classe de
    précision — Le galet intègre un roulement à billes scellé (joints Z ou 2RS).
    Privilégiez les roulements de classe de précision P5 ou P6 (norme ISO 492)
    pour garantir un jeu radial minimal et une rotation silencieuse sur la
    durée. Les roulements de classe C3 sont adaptés aux applications à forte
    dilatation thermique (moteurs soumis à des variations de température
    importantes). - Matériau de la poulie : acier embouti, aluminium, polymère
    chargé — Les galets polymère sont courants sur les moteurs modernes pour
    leur légèreté et leur amortissement des vibrations. Sur les applications à
    forte puissance (V8, gros diesels), les galets acier ou aluminium sont à
    privilégier pour leur résistance à la chaleur et aux charges radiales
    élevées. Vérifiez le matériau d'origine avant de substituer. - Axe de
    fixation et couple de serrage — Le galet est fixé par un axe fileté centré
    (M8, M10 ou M12 selon les moteurs) avec un couple de serrage précis
    (généralement 20 à 45 N.m). Un couple insuffisant provoque un desserrage en
    fonctionnement ; un couple excessif brise l'axe ou déforme la poupée.
    Renseignez-vous sur la valeur constructeur avant montage. - Compatibilité
    avec le lot complet de remplacement — Sur un véhicule ayant dépassé 80 000
    km, il est techniquement justifié de remplacer simultanément le galet
    enrouleur, le galet tendeur et la courroie d'accessoire. Ces pièces ont des
    durées de vie similaires ; remplacer le galet seul sur une courroie usée ou
    un tendeur fatigué réduit la durée de vie du nouveau galet. - Jeu radial
    admissible à froid — Avant toute commande, effectuez le test manuel : faites
    tourner le galet à la main sur le véhicule (capot ouvert, moteur froid et
    coupé). Tout jeu axial ou radial perceptible au toucher, tout point dur ou
    craquement, confirme la défaillance. Ce test valide aussi que le nouveau
    galet doit présenter une rotation parfaitement fluide et silencieuse au
    déballage. - Éviter les pièces sans référence OEM vérifiable — Les galets
    commercialisés sans référence constructeur associée ni code EAN traçable ne
    permettent aucune vérification de conformité dimensionnelle. Sur ce type de
    pièce mécanique tournante à grande vitesse (entre 3 000 et 8 000 tr/min), un
    défaut de fabrication du roulement peut provoquer un éclatement et
    endommager la courroie, l'alternateur et le carter moteur. Pour aller plus
    loin : consultez notre guide d'achat galet enrouleur de courroie
    d'accessoire — comparatif marques, critères de choix et prix.
  S4_DEPOSE: >-
    📖 Avant de démonter, consultez la fiche technique Galet enrouleur de
    courroie d'accessoire pour connaître les spécifications. - Débranchez la
    batterie. - Repérez le cheminement de la courroie d'accessoires. - Démontez
    la courroie d'accessoires. - Démontez la fixation du galet enrouleur. -
    Retirez le galet enrouleur de courroie d'accessoires.
  S4_REPOSE: >-
    - Vérifiez que le galet enrouleur neuf est identique à celui démonté. -
    Changez la courroie d'accessoires. - Remontez le galet enrouleur. - Serrez
    la fixation du galet enrouleur. - Mettre en place la courroie d'accessoires
    en respectant le cheminement. - Rebranchez la batterie. ✅ Après remontage,
    vérifiez les spécifications dans la fiche technique Galet enrouleur de
    courroie d'accessoire .
  S5: >-
    Erreurs frequentes avec le galet enrouleur de courroie d'accessoire : - Ne
    pas remplacer le galet en meme temps que la courroie — un galet use fait
    deporter ou vibrer la courroie neuve et reduit sa duree de vie- Confondre
    galet tendeur et galet enrouleur — le tendeur ajuste la tension, l'enrouleur
    guide le cheminement. Les deux ne sont pas interchangeables- Ignorer un
    sifflement ou un grondement au ralenti cote accessoires — signe de roulement
    de galet use, la casse est imminente- Ne pas verifier l'alignement des
    poulies apres montage — un galet desaxe use la courroie sur un bord et
    provoque un bruit de frottement- Reutiliser la vis de fixation du galet sans
    verifier son etat — une vis fatiguee se desserre en fonctionnement
  S6: >-
    Après la pose du nouveau galet enrouleur de courroie d'accessoire, les
    vérifications portent sur la tension de courroie, l'alignement du galet et
    l'absence de bruits de roulement au démarrage. Une courroie d'accessoire mal
    tendue peut lâcher et entraîner simultanément la panne de l'alternateur, de
    la direction assistée et de la pompe à eau.- Tension de courroie dans la
    plage constructeur — La flèche de la courroie d'accessoire ne doit pas
    dépasser 5 à 7 mm sous une pression de 10 N appliquée au milieu du brin le
    plus long (valeur indicative, vérifiez la préconisation constructeur). Une
    courroie trop lâche glisse et siffle ; trop tendue, elle sollicite
    excessivement les roulements.- Alignement du galet dans le plan de la
    courroie — Vérifiez visuellement que le galet est parfaitement dans l'axe
    des autres poulies (alternateur, compresseur de climatisation, pompe à eau).
    Toute désaxation de plus de 1 mm provoque une usure anormale sur le bord de
    la courroie et génère un sifflement caractéristique.- Absence de bruit de
    roulement au démarrage — Démarrez le moteur et écoutez attentivement au
    niveau de la courroie d'accessoire. Aucun grondement, sifflement ni
    crissement ne doit être audible. Un bruit persistant indique soit un galet
    défectueux (roulement interne), soit une mauvaise tension de courroie.-
    Rotation libre du galet à froid avant démarrage — Faites tourner le galet à
    la main avant de remettre la courroie : il doit tourner librement sans point
    dur ni jeu radial perceptible. Un jeu radial supérieur à 0,5 mm ou une
    résistance franche indique un roulement déjà défectueux sur la pièce neuve.-
    Disparition de l'odeur de caoutchouc chaud — Après 10 minutes de
    fonctionnement moteur, aucune odeur de caoutchouc surchauffé ne doit être
    perceptible. Cette odeur était le signe du galet défaillant qui faisait
    frotter la courroie : elle doit disparaître avec la pièce neuve.-
    Vérification de l'ensemble de la courroie d'accessoire — Profitez de
    l'intervention pour inspecter l'état de la courroie elle-même : craquelures,
    effilochage des nervures, perte de côtes. Une courroie présentant ces signes
    à moins de 80 000 km doit être remplacée simultanément pour éviter une
    nouvelle intervention à court terme.- Contrôle des poulies associées —
    Vérifiez la rotation des poulies de l'alternateur, du compresseur de
    climatisation et de la pompe à eau. Toute poulie grippée ou avec jeu axial
    doit être remplacée avant de remettre la courroie neuve en service.
  S7: >-
    Quel est le prix d'un galet enrouleur de courroie d'accessoire ?Le prix
    varie selon le véhicule et la marque. Utilisez notre sélecteur pour trouver
    le galet enrouleur de courroie d'accessoire compatible avec votre véhicule
    et comparer les tarifs des différents équipementiers.Comment savoir si mon
    galet enrouleur de courroie d'accessoire est à changer ?Les signes d'usure
    les plus courants sont détaillés dans la section diagnostic ci-dessus. En
    cas de doute, faites contrôler la pièce par un professionnel.Peut-on rouler
    avec un galet enrouleur de courroie d'accessoire défaillant ?Cela dépend de
    la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du
    véhicule. Consultez la section symptômes pour évaluer l'urgence du
    remplacement.- Courroie d'accessoire . - Poulie tendeur de courroie
    d'accessoire. 📖 Fiche technique Galet enrouleur de courroie d'accessoire —
    intervalles et spécifications d’entretien.
  S8: >-
    Comment choisir Galet enrouleur de courroie d'accessoire
    compatibleRenseignez marque, modele, type moteur et annee, puis verifiez la
    reference Quand remplacer Galet enrouleur de courroie d'accessoire ?En cas
    de courroie d accessoire visiblement usee ou fissuree ou de degradation
    Puis-je monter Galet enrouleur de courroie d'accessoire sans verificationLe
    montage peut exiger controles de couple, alignement et references.
  META: >-
    {"meta_title":"Galet enrouleur courroie accessoire : diagnostic |
    AutoMecanik","meta_description":"Sifflement ou grondement au niveau de la
    courroie, jeu perceptible à la main ? Découvrez comment diagnostiquer un
    galet enrouleur usé et à quel intervalle le
    remplacer.","source":"rag://gammes/galet-enrouleur-de-courroie-d-
    accessoire.md"}
---

# Galet enrouleur de courroie d'accessoire - Guide Diagnostic Complet

## Fonction et Rôle

Guide la courroie d'accessoire

**Actions principales:** guider, enrouler, maintenir

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- courroie d accessoire visiblement usee ou fissuree
- sifflement ou grondement au niveau de la courroie
- perceptible faisant tourner galet main
- perte de tension de la courroie
- odeur de caoutchouc chaud
- plus de 80 000 km depuis le dernier changement

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet enrouleur de courroie d'accessoire:

1. **Inspection visuelle** - Examiner l'état du galet enrouleur de courroie d'accessoire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-a-eau
- pompe-de-direction-assistee

## Critères de Compatibilité

Pour commander le bon galet enrouleur de courroie d'accessoire, vous devez connaître:

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

**Galet enrouleur OE ou adaptable ?**
Les galets OES (SKF, INA, Gates) sont fiables. Vérifiez le diamètre et le type de roulement.

**Comment savoir si mon galet enrouleur est HS ?**
Sifflement ou grondement au niveau de la courroie, jeu perceptible à la main, roulement rugueux.

**Tous les combien changer le galet enrouleur ?**
À chaque changement de courroie d'accessoire (60 000 à 100 000 km). Ne jamais réutiliser un ancien galet.

**Peut-on changer le galet enrouleur soi-même ?**
Oui, opération accessible. Détendre la courroie, dévisser le galet, monter le neuf. 30 min à 1h.

**Quelle erreur éviter avec le galet enrouleur ?**
Ne pas oublier de vérifier le tendeur aussi. Respecter le cheminement de la courroie. Vérifier l'alignement.
