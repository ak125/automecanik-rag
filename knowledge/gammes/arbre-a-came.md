---
category: moteur
slug: arbre-a-came
title: Arbre à came
pg_id: 566
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
  role: Commander l'ouverture et la fermeture des soupapes
  must_be_true:
  - commander
  - synchroniser
  - actionner les soupapes
  must_not_contain:
  - vilebrequin
  - boite de vitesses
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - commander
  - synchroniser
  - actionner les soupapes
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
    min: 1000
    max: 5000
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
  - tier: Équivalent OE (motoriste reconnu)
  - tier: Pièce reconstruite / reconditionnée
  brands:
    premium:
    - Elring
    - Victor Reinz
    standard:
    - Febi
    - Ajusa
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Bruit moteur
    severity: confort
  - id: S2
    label: Claquement
    severity: confort
  - id: S3
    label: Perte puissance
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : bruit moteur'
  quick_checks:
  - Bruit moteur ?
  - 'Observer : claquement ?'
  - 'Observer : perte puissance ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Bruit moteur
  - Claquement
  - Perte puissance
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '566'
  intro_title: A quoi sert Arbre à came ?
  risk_title: Pourquoi remplacer Arbre à came a temps ?
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
  - question: Comment choisir Arbre à came compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Arbre à came ?
    answer: En cas de bruit moteur ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Arbre à came sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
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
doc_id: aa1443a1-93ae-5896-939e-b5d3b1128591
content_hash: sha256:c19cf85131ca62a8
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
  area: Sur le vehicule (position variable selon modele)
  access: Consulter la revue technique du vehicule
  adjacent_parts:
  - pieces adjacentes du meme systeme
installation:
  difficulty: variable
  time: consulter revue technique
  tools:
  - outillage standard
  prerequisite: Consulter la procedure constructeur
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: 'hydraulique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_2_a: '2 A'
    val_2_a: '2 a'
    val_7_6_litres: '7,6 litres'
    val_800_v: '800 V'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: '- Niveau de difficulté : avancé (professionnel) — calage de distribution requis. - Temps estimé : 4 à 8 h selon le
    moteur. - Outils : piges de calage spécifiques, clé dynamométrique 10-50 Nm, comparateur, clés Torx. - Consommables :
    joint de couvre-culasse neuf, huile moteur + filtre neufs, pâte d''étanchéité. - Sécurité : ne jamais tourner le vilebrequin
    sans calage sur un moteur interférent — risque de collision soupapes-pistons.'
  S2: 'Symptômes d''un arbre à cames usé ou défectueux : Symptômes sonores : - Claquement métallique au ralenti — jeu excessif
    entre les cames et les poussoirs. Le bruit s''atténue à chaud (dilatation). - Bruit de distribution anormal — cliquetis
    régulier synchronisé avec le régime moteur. Distinct du claquement d''injecteurs. Symptômes de performance : - Perte de
    puissance progressive — les cames usées ne lèvent plus assez les soupapes, le remplissage est insuffisant. - Ratés d''allumage
    — la synchronisation des soupapes est décalée, le mélange n''est plus optimal. - Consommation en hausse — le moteur compense
    la perte de rendement. Symptômes visuels : - Voyant moteur allumé — codes P0340-P0349 (capteur arbre à cames) ou P0011-P0014
    (calage variable). - Usure visible des cames — profil arrondi au lieu d''ovoïde net. Nécessite dépose du cache culbuteurs.
    ⚠️ Un arbre à cames grippé peut entraîner la rupture de la courroie/chaîne de distribution et un contact soupapes/pistons
    sur les moteurs interférents.'
  S3: '- Nombre de cames : admission seule (simple ACT) ou admission + échappement (double ACT). Ne pas confondre. - Profil
    des cames : spécifique à chaque motorisation. Vérifiez la référence OEM exacte. - Entraînement : par courroie ou chaîne.
    Le pignon/poulie de l''arbre doit correspondre au type d''entraînement. - Capteur de position : certains arbres intègrent
    une cible pour le capteur d''arbre à cames. Vérifiez la compatibilité. - Système de distribution variable (VVT) : si équipé,
    l''arbre intègre un phaser ou un actuateur. La référence est spécifique. Pour aller plus loin : consultez notre guide
    d''achat arbre à came — comparatif marques, critères de choix et prix.'
  S4_DEPOSE: 📖 Avant de démonter, consultez la fiche technique Arbre à came pour connaître les spécifications. - Calez le
    véhicule. - Débranchez la batterie. - Démontez le cache moteur. - Vidangez le liquide de refroidissement. - Démontez la
    courroie d'accessoires. - Démontez la courroie de distribution ou lachaîne de distribution (suivant le type de distribution).
    - Démontez la vanne EGR. - Démontez le cache de protection supérieure du collecteur d'échappement. - Démontez la vis de
    fixation de la poulie d'arbre à cames. - Démontez la poulie d'arbre à cames. - Démontez le carter arrière de protectionde
    la courroie de distribution (suivant équipement). - Démontez le capteur d'arbre à cames. - Démontez la pompe à vide de
    freinage. - Démontez le filtre àcarburant pour moteur diesel. - Démontez le support dufiltre à carburant pour moteur diesel.
    - Démontez les injecteurs. - Démontez le carter des chapeauxde palier d'arbres à cames. - Sur certain motorisationles
    arbres à cames sont entraînées par une petite chaîne dans ce cas il faudradémontez cette dernière. - Démontez la fixation
    du tendeur de chaîned'arbres à cames. - Démontez les vis de palier d'arbre à cames. - Démontez les arbres à cames et la
    bague d'étanchéité.
  S4_REPOSE: 'Le remontage d''un arbre à cames est une opération de haute précision sur la distribution du moteur. Le calage
    des arbres à cames par rapport au vilebrequin conditionne directement le fonctionnement des soupapes. Une erreur de positionnement
    entraîne une perte de puissance, des claquements de soupapes ou, dans les cas graves, un contact entre pistons et soupapes.
    Consultez impérativement la revue technique de votre véhicule pour les ordres de serrage et les valeurs de calage. - Vérifiez
    que l''arbre à cames neuf est identique à celui déposé : nombre et profil des cames, diamètre des paliers, position du
    crabot de synchronisation. - Lubrifiez généreusement les paliers de l''arbre à cames, le corps des poussoirs de soupape
    et les linguets de commande avec de l''huile moteur propre ou une huile d''assemblage dédiée. - Positionnez l''arbre à
    cames dans les chapeaux de palier en respectant le marquage de position (repère de came ou encoche d''alignement visible
    sur l''arbre). - Remontez les bagues d''étanchéité à l''aide d''un chasse-bague adapté — ne jamais les frapper directement.
    Appliquez un léger film d''huile sur la lèvre avant montage. - Serrez les vis de palier d''arbre à cames en plusieurs
    passes dans l''ordre prescrit par le constructeur (typiquement de l''intérieur vers l''extérieur), en respectant le couple
    de serrage (généralement 10 à 20 Nm selon motorisation). - Positionnez la chaîne ou courroie de distribution sur la poulie
    d''arbre à cames en alignant les repères de calage. Si présence d''une chaîne secondaire d''arbres à cames, respecter
    le nombre de tours indiqué dans la revue technique (souvent 40 tours) pour le calage final. - Remontez le tendeur de chaîne
    et vérifiez la tension. Remontez le carter de palier en appliquant un léger cordon de pâte d''étanchéité sur les zones
    prévues ; respectez l''ordre de serrage. - Remontez dans l''ordre inverse les éléments déposés : capteur d''arbre à cames,
    pompe à vide, poulie d''arbre à cames (couple de la vis de poulie selon constructeur, souvent 80 à 120 Nm), vanne EGR,
    courroie d''accessoires. - Remplissez le niveau de liquide de refroidissement et vérifiez le niveau d''huile moteur. Rebranchez
    la batterie. - Démarrez le moteur et laissez tourner au ralenti 2 à 3 minutes. Vérifiez l''absence de claquement, de voyant
    allumé et de fuite d''huile au niveau du carter. Effectuez une lecture de défauts avec l''outil de diagnostic pour confirmer
    l''absence de codes liés à la distribution.'
  S5: '- Mauvais calage de distribution — un décalage d''une dent dégrade les performances. Plusieurs dents = destruction
    du moteur interférent. - Desserrage brutal des chapeaux — l''arbre se déforme. Procédez par quarts de tour, en étoile,
    du centre vers l''extérieur. - Démarrage sans lubrification — un palier neuf démarré à sec est rayé irréversiblement.
    - Joint de couvre- culasse réutilisé — fuite d''huile garantie. Joint neuf obligatoire. - Jeu aux soupapes non vérifié
    — un arbre neuf modifie le jeu. Réglez selon les spécifications constructeur. - Rotation du vilebrequin sans calage —
    collision soupapes-pistons sur moteur interférent.'
  S6: '- Calage de distribution : repères alignés PMH cylindre 1, piges en place. - Rotation manuelle : 2 tours complets à
    la main sans résistance anormale. - Pression d''huile : voyant d''huile éteint en moins de 5 secondes après démarrage.
    - Ralenti stable : pas de claquement ni de raté, régime régulier. - Absence de fuite : vérifiez le joint de couvre-culasse
    après 10 min moteur tournant.'
  S7: Quel est le prix d'un arbre à came ?Le prix varie selon le véhicule et la marque. Utilisez notre sélecteur pour trouver
    l'arbre à came compatible avec votre véhicule et comparer les tarifs des différents équipementiers.Comment savoir si l'arbre
    à came est à changer ?Les signes d'usure les plus courants sont détaillés dans la section diagnostic ci-dessus. En cas
    de doute, faites contrôler la pièce par un professionnel.Peut-on rouler avec un arbre à came défaillant ?Cela dépend de
    la gravité du dysfonctionnement et du rôle de la pièce dans la sécurité du véhicule. Consultez la section symptômes pour
    évaluer l'urgence du remplacement. - Kit de distribution (courroie/chaîne + tendeur + galets) — à remplacer systématiquement.
    - Poussoirs hydrauliques ou linguets — vérifiez le jeu, usure couplée à l'arbre. - Joint de couvre- culasse neuf — obligatoire
    à chaque ouverture. - Huile moteur + filtre neufs — vidange obligatoire (résidus métalliques). - Joint/pompe à eau — à
    remplacer si entraînée par la distribution.
  S8: '- L''arbre à cames s''use-t-il ? Rarement avec un entretien correct. L''usure survient par manque de lubrification
    (vidanges négligées, niveau bas). - Peut-on changer un seul arbre sur un double ACT ? Oui, mais vérifiez l''usure de l''autre.
    Un écart crée un déséquilibre admission/échappement. - Faut-il remplacer les paliers ? Si les paliers de culasse présentent
    des rayures ou un jeu excessif, la culasse doit être rectifiée. - Combien de temps dure l''intervention ? 4 à 8 h. Le
    coût main-d''œuvre est la majorité de la facture. - Un arbre à cames se reconditionne-t-il ? Le reprofilage existe mais
    est rare. Le remplacement neuf est la norme.'
  META: '{"meta_title":"Arbre à came : claquement moteur, causes | AutoMecanik","meta_description":"Claquement au ralenti,
    bruit métallique ou perte de puissance ? L''arbre à came commande les soupapes. Symptômes, diagnostic et compatibilité
    par véhicule.","og_title":"Arbre à came : diagnostic claquement et remplacement","og_description":"Bruit moteur, claquement
    ou perte de puissance au ralenti : peut-être l''arbre à came. Guide complet : causes, vérification synchronisation, pièces
    associées.","ca nonical_intent":"diagnostic","schema_type":"HowTo","sources":[{"type":"rag", "ref":"gammes/arbre-a-came.md","field":"domain.role
    + diagnostic.symptoms + domain.related_parts"}]}'
---

# Arbre à came - Guide Diagnostic Complet

## Fonction et Rôle

Commander l'ouverture et la fermeture des soupapes

**Actions principales:** commander, synchroniser, actionner les soupapes

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement**
  claquement

### 🟢 Autres Symptômes

- bruit moteur
- perte puissance

## Procédure de Diagnostic

Pour diagnostiquer un problème de arbre à came:

1. **Inspection visuelle** - Examiner l'état du arbre à came
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur
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

- courroie-de-distribution
- culbuteur
- kit-de-poussoir-culbuteur
- poulie-d-arbre-a-came
- poussoir-de-soupape

## Critères de Compatibilité

Pour commander le bon arbre à came, vous devez connaître:

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

**Comment choisir Arbre à came compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Arbre à came ?**
En cas de bruit moteur ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Arbre à came sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
