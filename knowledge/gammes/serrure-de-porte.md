---
category: accessoires
slug: serrure-de-porte
title: Serrure de porte
pg_id: 1361
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
  role: Verrouille et déverrouille la porte du véhicule
  must_be_true:
  - verrouiller
  - deverrouiller
  - bloquer
  must_not_contain:
  - alarme
  - antivol
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - verrouiller
  - deverrouiller
  - bloquer
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
  - ❌ "securite garantie"
  cost_range:
    min: 30
    max: 150
    currency: EUR
    unit: l'unite
    source: estimation categorie
  brands:
    premium:
    - Valeo
    - Kiekert
    - Brose
    standard:
    - Febi Bilstein
    - Topran
    - Trucktec
    budget:
    - Blic
    - Maxgear
    - Polcar
  quality_tiers:
  - tier: Origine (OE)
    description: Serrures fabriquees par l'equipementier d'origine du constructeur. Mecanisme, references cle et electronique
      (centralisation) identiques a la piece usine.
  - tier: Qualite equivalente OE (OES)
    description: Equipementiers reconnus dans la fermeture automobile. Compatibilite electronique verifiee, tarif inferieur
      a l'OE.
  - tier: Adaptable de qualite
    description: Marques fiables en entree de gamme. Bien verifier la compatibilite avec le systeme de centralisation et le
      nombre de broches du connecteur.
diagnostic:
  symptoms:
  - id: S1
    label: Porte qui ne se verrouille plus
    severity: confort
  - id: S2
    label: Centralisation inoperante sur une porte
    severity: confort
  - id: S3
    label: Cle qui tourne dans le vide
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : porte qui ne se verrouille plus'
  quick_checks:
  - 'Observer : porte qui ne se verrouille plus ?'
  - 'Observer : centralisation inoperante sur une porte ?'
  - 'Observer : cle qui tourne dans le vide ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Porte qui ne se verrouille plus
  - Centralisation inoperante sur une porte
  - Cle qui tourne dans le vide
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1361'
  intro_title: A quoi sert Serrure de porte ?
  risk_title: Pourquoi remplacer Serrure de porte a temps ?
  risk_explanation: '**Défaillance progressive** - Usure normale due à l''utilisation'
  risk_consequences:
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
  - question: Comment choisir Serrure de porte compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Serrure de porte ?
    answer: En cas de porte qui ne se verrouille plus ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Serrure de porte sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
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
doc_id: 7a1bb075-b5dd-5638-a8e6-f5d36fb1df72
content_hash: sha256:1a305444914624de
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
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    centralisation: 'actionneur electrique integre — tester avant de remplacer toute la serrure'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    La serrure de porte est le mécanisme mécanique et électronique qui assure le
    verrouillage et le déverrouillage de chaque porte du véhicule. Elle
    constitue la pièce centrale du système de sécurité passive des portières,
    garantissant que la porte reste fermée en circulation et s'ouvre uniquement
    à la demande du conducteur ou des passagers. Structurellement, une serrure
    de porte se compose d'un mécanisme à pêne rotatif (la came) qui s'engage sur
    la gâche fixée au montant de caisse, d'un levier interne et d'un levier
    externe reliés aux poignées, et sur les véhicules modernes, d'un actionneur
    électrique (moteur ou solénoïde) qui active la centralisation à distance.
    Lors du verrouillage, la serrure bloque la rotation de la came, rendant
    impossible l'ouverture de la porte depuis l'extérieur. Sur les véhicules
    équipés de centralisation, cet actionneur reçoit une commande électrique
    depuis le boîtier de confort (BCM) lorsque le conducteur actionne la
    télécommande ou le bouton de verrouillage. Les systèmes d'entrée sans clé
    (keyless entry) intègrent en plus une antenne de proximité. La serrure de
    porte subit des sollicitations mécaniques répétées à chaque ouverture et
    fermeture — plusieurs milliers de cycles par an — ainsi que des contraintes
    climatiques (humidité, gel, poussière) qui accélèrent l'usure de ses
    composants internes. Un remplacement préventif dès les premiers signes de
    défaillance évite un blocage complet de la portière dans une situation
    inopportune.
  S2: >-
    Ne pas attendre la panne complete pour intervenir. Symptômes d'usure : -
    Porte qui ne se verrouille plus - Centralisation inoperante sur une porte -
    Cle qui tourne dans le vide
  S3: >-
    Pour choisir les bons serrure de porte pour votre véhicule : - Marque de
    votre véhicule - Modele de votre véhicule - Annee de votre véhicule -
    Vérifier : porte qui ne se verrouille plus - Vérifier : centralisation
    inoperante sur une porte - Vérifier : cle qui tourne dans le videPour aller
    plus loin : consultez notre guide d'achat serrure de porte — comparatif
    marques, critères de choix et prix.
  S4_DEPOSE: >-
    Le remplacement d'une serrure de porte nécessite le démontage du panneau
    intérieur de portière. L'opération est accessible pour un mécanicien
    expérimenté mais demande méthode et patience pour ne pas casser les clips de
    fixation du panneau. Voici la procédure générale : - Déconnecter la batterie
    (borne négative) pour neutraliser le circuit électrique de la centralisation
    avant toute intervention sur les connecteurs de la portière. - Retirer le
    panneau intérieur de porte : dévisser les vis cachées derrière les cache-vis
    ou sous l'accoudoir, puis désengager les clips de fixation périphériques en
    les levier délicatement avec un outil plastique de démonte-garniture. -
    Déconnecter les nappes électriques du panneau (lève-vitre, rétroviseur,
    haut-parleur) en appuyant sur les languettes de déverrouillage des
    connecteurs — ne jamais tirer sur les fils directement. - Écarter le film de
    protection pare-vapeur (feuille plastique noire collée sur la structure
    métallique de la porte) avec précaution pour le réutiliser lors de la
    repose. - Déconnecter les tringleries et câbles Bowden reliant la serrure
    aux poignées intérieure et extérieure — photographier l'arrangement avant
    dépose pour faciliter la repose exacte. - Débrancher le connecteur
    électrique de l'actionneur de centralisation intégré dans la serrure en
    appuyant sur le clip de déverrouillage. - Retirer les vis de fixation de la
    serrure sur la structure métallique de la porte (généralement 3 vis Torx ou
    cruciformes accessibles depuis l'intérieur de la portière). - Extraire
    l'ancienne serrure et installer le nouveau mécanisme en inversant les étapes
    — reconnecter toutes les tringleries et le connecteur électrique avant de
    recoller le film pare-vapeur et de reposer le panneau.
  S4_REPOSE: >-
    Après avoir installé la nouvelle serrure de porte dans son logement, le
    remontage du panneau de portière doit suivre une séquence précise pour
    garantir l'étanchéité acoustique et la solidité des clips. Ne pas forcer les
    éléments au risque de fracturer les agrafes de fixation. - Repositionner la
    serrure neuve dans son logement et visser les fixations au couple
    constructeur. Vérifier que les biellettes de commande intérieure et
    extérieure sont bien encliquetées dans leurs œillets. - Reconnecter les
    connecteurs électriques du moteur de centralisation : aligner les ergots de
    verrouillage jusqu'au clic caractéristique. Ne jamais forcer un connecteur à
    l'envers. - Rebrancher la tige de barillet côté extérieur si elle a été
    déposée, en vérifiant l'absence de jeu longitudinal excessif dans la
    liaison. - Reposer le cache des passe-fils et vérifier que le joint
    d'étanchéité de la portière est intact sur tout son pourtour avant de
    refermer le panneau. - Réencliquer le panneau de portière en commençant par
    les clips du bas, puis remonter progressivement le long des bords. Appuyer
    fermement à la paume sur chaque clip pour le verrouiller sans outil. -
    Visser les vis apparentes (poignée intérieure, accoudoir, cache triangle)
    dans leur ordre de démontage inverse. Respecter le couple de serrage pour ne
    pas déformer les plastiques. - Rebrancher le faisceau électrique du panneau
    (lève-vitre, rétroviseur, éclairage de courtoisie) et clipser le connecteur
    principal avant de pousser le panneau contre la portière. - Tester
    immédiatement la centralisation : verrouiller et déverrouiller plusieurs
    fois depuis la télécommande, la clé et la commande intérieure. Vérifier que
    la porte se ferme et s'ouvre sans résistance anormale.
  S5: >-
    - ❌ "homologué CT" - ❌ "sécurité garantie" - ❌ "zéro panne" - ❌ "garanti à
    vie" - ❌ "securite garantie"
  S6: >-
    Une fois la nouvelle serrure installée et le panneau de porte repositionné,
    une série de tests fonctionnels doit être réalisée avant de valider
    l'intervention et de rendre le véhicule à son usage normal : - Tester
    l'ouverture et la fermeture manuelle depuis l'intérieur et depuis
    l'extérieur : la porte doit s'ouvrir et se fermer sans effort anormal, avec
    un claquement net et franc signalant l'engagement correct du pêne dans la
    gâche. - Vérifier le verrouillage mécanique par la clé : tourner la clé dans
    le barillet et confirmer que la serrure se verrouille et se déverrouille
    correctement, avec une résistance mécanique normale. - Tester la
    centralisation électrique : actionner la télécommande ou le bouton de
    verrouillage central et vérifier que la portière concernée répond de façon
    synchronisée avec les autres portes du véhicule. - Contrôler l'absence de
    jeu ou de bruit de cliquetis à la fermeture : un cliquetis résiduel indique
    une tringlerie mal raccordée, un clip de panneau non engagé ou un mauvais
    alignement de la serrure sur la gâche. - Vérifier l'étanchéité du film pare-
    vapeur après remontage — un test à l'arrosage modéré peut être effectué si
    nécessaire pour détecter toute infiltration d'eau vers les mécanismes
    internes de la portière.
  S7: >-
    Quel est le prix d'un serrure de porte ?Le prix varie selon le véhicule et
    la marque. Utilisez notre sélecteur pour trouver le serrure de porte
    compatible avec votre véhicule et comparer les tarifs des différents
    équipementiers.Comment savoir si mon serrure de porte est à changer ?Les
    signes d'usure les plus courants sont détaillés dans la section diagnostic
    ci-dessus. En cas de doute, faites contrôler la pièce par un
    professionnel.Peut-on rouler avec un serrure de porte défaillant ?Cela
    dépend de la gravité du dysfonctionnement et du rôle de la pièce dans la
    sécurité du véhicule. Consultez la section symptômes pour évaluer l'urgence
    du remplacement.- poignee - barillet
  S8: >-
    Comment choisir Serrure de porte compatible avec mon vehicule ?Renseignez
    marque, modele, type moteur et annee, puis verifiez la reference exacte
    avant montage. Quand remplacer Serrure de porte ?En cas de porte qui ne se
    verrouille plus ou de degradation mesurable, il faut controler rapidement
    avant panne secondaire. Puis-je monter Serrure de porte sans verification
    atelier ?Le montage peut exiger controles de couple, alignement et
    references. En cas de doute, appliquez la procedure constructeur.
  META: >-
    {"meta_title":"Serrure de porte : symptômes et remplacement |
    AutoMecanik","meta_description":"Porte qui ne se verrouille plus, clé qui
    tourne dans le vide ou centralisation inopérante ? Guide diagnostic et
    remplacement de la serrure de porte.","og_title":"Serrure de porte
    défaillante : causes et remplacement | AutoMecanik","og_description":"Porte
    bloquée, centralisation inopérante, clé qui tourne dans le vide : identifiez
    la panne et remplacez la serrure selon votre
    modèle.","schema_type":"HowTo","canonical_hint":"/pieces/serrure-de-porte"}
---

# Serrure de porte - Guide Diagnostic Complet

## Fonction et Rôle

Verrouille et déverrouille la porte du véhicule

**Actions principales:** verrouiller, deverrouiller, bloquer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- porte qui ne se verrouille plus
- centralisation inoperante sur une porte
- cle qui tourne dans le vide

## Procédure de Diagnostic

Pour diagnostiquer un problème de serrure de porte:

1. **Inspection visuelle** - Examiner l'état du serrure de porte
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- poignee
- cle
- barillet

## Critères de Compatibilité

Pour commander le bon serrure de porte, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"

## FAQ

**Comment choisir Serrure de porte compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Serrure de porte ?**
En cas de porte qui ne se verrouille plus ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Serrure de porte sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
