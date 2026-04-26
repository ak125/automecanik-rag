---
category: accessoires
slug: leve-vitre
title: Lève-vitre
pg_id: 1561
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
  role: Monte et descend la vitre de la portière
  must_be_true:
  - lever
  - descendre
  - actionner
  must_not_contain:
  - injection
  - freinage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - lever
  - descendre
  - actionner
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
  - ❌ "fonctionnement garanti"
  cost_range:
    min: 80
    max: 250
    currency: EUR
    unit: mécanisme complet
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE (OES)
  - tier: Adaptable qualite
  - tier: Reconditionne
  - tier: Echange standard
  brands:
    premium:
    - Stabilus
    - Valeo
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Vitre qui ne monte ou ne descend plus
    severity: confort
  - id: S2
    label: Vitre tres lente arrete cours
    severity: confort
  - id: S3
    label: Bruit de moteur mais vitre immobile cable casse
    severity: confort
  - id: S4
    label: Vitre qui descend toute seule mecanisme use
    severity: confort
  - id: S5
    label: Grincement ou bruit anormal a la montee descente
    severity: confort
  - id: S6
    label: Vitre de travers ou mal guidee dans le rail
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : vitre qui ne monte ou ne descend plus'
  quick_checks:
  - 'Observer : vitre qui ne monte ou ne descend plus ?'
  - 'Observer : vitre tres lente arrete cours ?'
  - Bruit de moteur mais vitre immobile cable casse ?
  - 'Observer : vitre qui descend toute seule mecanisme use ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Vitre qui ne monte ou ne descend plus
  - Vitre tres lente arrete cours
  - Bruit de moteur mais vitre immobile cable casse
  - Vitre qui descend toute seule mecanisme use
  - Grincement ou bruit anormal a la montee descente
  - Vitre de travers ou mal guidee dans le rail
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1561'
  intro_title: A quoi sert Lève-vitre ?
  risk_title: Pourquoi remplacer Lève-vitre a temps ?
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
  - question: Lève-vitre OE ou adaptable ?
    answer: Les lève-vitres OES (Valeo, Brose) sont de qualité équivalente. Les adaptables conviennent mais vérifiez la compatibilité
      exacte (avec ou sans moteur, gauche/droite).
  - question: Comment savoir si mon lève-vitre est HS ?
    answer: Vitre qui ne monte plus ou très lentement, bruit de moteur sans mouvement (câble cassé), vitre qui descend toute
      seule, bruit de grincement.
  - question: Tous les combien changer le lève-vitre ?
    answer: Pas de périodicité. Durée de vie variable selon usage. Les portières conducteur s'usent plus vite. Peut durer
      150 000+ km ou tomber en panne avant.
  - question: Peut-on changer un lève-vitre soi-même ?
    answer: Oui mais opération délicate. Déposer le panneau de porte, débrancher les connecteurs, dévisser le mécanisme, tenir
      la vitre. Prévoir 1 à 2h par portière.
  - question: Quelle erreur éviter ?
    answer: Maintenir la vitre pendant l'opération (risque de chute). Vérifier l'interrupteur et le fusible avant de changer
      le mécanisme. Ne pas forcer une vitre bloquée.
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
doc_id: b558ca86-cf40-5fe2-be35-ab7e56300a50
content_hash: sha256:0a91f62c0d05d9df
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
  - type: 'pneumatique'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_14_a: '14 a'
    val_15_a: '15 a'
    val_18_a: '18 a'
    val_28_a: '28 a'
    val_3_v: '3 v'
    val_4_v: '4 v'
    val_63_a: '63 A'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Le lève-vitre est le mécanisme qui monte et descend la vitre de la portière. Il se compose d''''un moteur électrique
    (sur les véhicules modernes), d''''un système de transmission (câble + poulie ou bras articulé) et de rails de guidage.
    La vitre est fixée au chariot du mécanisme par deux boulons ou clips. Niveau de difficulté : Intermédiaire — nécessite
    la dépose du panneau de porte intérieur. Comptez 1 à 2h par portière. Outils : outil de démontage clips plastique, tournevis,
    douilles 10 mm, scotch de maintien de vitre. Pièces liées : moteur de lève-vitre (souvent vendu séparément), interrupteur
    de lève-vitre (bouton de commande), fusible lève-vitre.'
  S2: 'Pas de périodicité de remplacement. Durée de vie variable — la portière conducteur s''''use plus vite (usage quotidien).
    Peut durer 150 000+ km ou tomber en panne avant 80 000 km selon l''''usage. Symptômes de défaillance : - Vitre qui ne
    monte ou ne descend plus — moteur HS ou câble cassé- Vitre très lente ou qui s''''arrête en cours de mouvement — moteur
    fatigué ou mécanisme grippé- Bruit de moteur mais vitre immobile — câble cassé ou poulie déboîtée- Vitre qui descend toute
    seule — mécanisme usé, le câble ne maintient plus la vitre en position- Grincement ou bruit anormal à la montée/descente
    — rails de guidage sales ou secs- Vitre de travers ou mal guidée dans le rail — chariot ou clips de fixation cassés'
  S3: 'Pour choisir le bon lève-vitre : - Côté : gauche (conducteur) ou droite (passager) — les mécanismes ne sont pas symétriques-
    Avant ou arrière : les dimensions et le type de mécanisme diffèrent entre portes avant et arrière- Avec ou sans moteur
    : certaines références incluent le moteur électrique, d''''autres non — vérifier si le moteur est intégré ou séparé sur
    votre véhicule- Type de mécanisme : à câble (le plus courant, moins cher) ou à bras articulé (véhicules haut de gamme,
    plus robuste)- Marques : Valeo, Brose (OES), Febi, Meyle (standard) — les adaptables conviennent mais vérifier la compatibilité
    exacte du connecteur moteur- Budget : 80 à 250 EUR selon avec ou sans moteur'
  S4_DEPOSE: 1. Débrancher la batterie. 2. Déposer le panneau de porte intérieur (clips plastique + vis cachées derrière les
    caches et la poignée). 3. Décoller le film plastique d''étanchéité de la porte (le conserver intact pour le remontage).
    4. Monter la vitre en position haute et la maintenir avec du scotch large collé sur le montant de porte. 5. Débrancher
    le connecteur du moteur de lève-vitre. 6. Dévisser les 2 boulons de fixation de la vitre sur le chariot du mécanisme.
    7. Dévisser les vis de fixation du mécanisme sur la tôle de porte (3 à 5 vis selon véhicule). 8. Extraire le mécanisme
    par l''ouverture de la tôle de porte en le faisant pivoter.
  S5: 'Erreurs fréquentes avec le lève-vitre : - Ne pas maintenir la vitre avec du scotch avant de débrancher le mécanisme
    — la vitre tombe dans la porte et peut se casser ou rayer la peinture- Remplacer le mécanisme complet alors que seul le
    moteur ou l''''interrupteur est en cause — tester le fusible, l''''interrupteur et le moteur séparément avant de tout
    changer- Forcer une vitre bloquée avec les mains — le mécanisme casse ou le câble se déboîte de la poulie- Oublier de
    remettre le film plastique d''''étanchéité lors du remontage — l''''eau de pluie entre dans la porte et corrode le moteur
    et les connecteurs- Ne pas vérifier le coulissement des rails de guidage — des rails sales ou rouillés font forcer le
    moteur et réduisent sa durée de vie- Confondre lève-vitre gauche et droite — les mécanismes ne sont pas symétriques'
  S6: 'Après le remplacement du lève-vitre : - Test fonctionnel : monter et descendre la vitre 3 à 4 fois complètement — le
    mouvement doit être fluide et silencieux- Initialisation : sur les véhicules avec anti-pincement, réinitialiser le module
    de confort en maintenant l''''interrupteur en position haute pendant 5 secondes après la course complète- Étanchéité :
    vérifier que le film plastique est bien recollé sur la tôle de porte — un film décollé laisse entrer l''''eau- Alignement
    vitre : en position haute, la vitre doit être alignée avec le joint de baie — un décalage provoque du bruit de vent et
    des infiltrations d''''eau'
---

# Lève-vitre - Guide Diagnostic Complet

## Fonction et Rôle

Monte et descend la vitre de la portière

**Actions principales:** lever, descendre, actionner

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de moteur mais vitre immobile cable casse**
  bruit de moteur mais vitre immobile cable casse
- **Grincement ou bruit anormal a la montee descente**
  grincement ou bruit anormal a la montee descente

### 🟢 Autres Symptômes

- vitre qui ne monte ou ne descend plus
- vitre tres lente arrete cours
- vitre qui descend toute seule mecanisme use
- vitre de travers ou mal guidee dans le rail

## Procédure de Diagnostic

Pour diagnostiquer un problème de lève-vitre:

1. **Inspection visuelle** - Examiner l'état du lève-vitre
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
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

- moteur-leve-vitre
- interrupteur-leve-vitre

## Critères de Compatibilité

Pour commander le bon lève-vitre, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "fonctionnement garanti"

## FAQ

**Lève-vitre OE ou adaptable ?**
Les lève-vitres OES (Valeo, Brose) sont de qualité équivalente. Les adaptables conviennent mais vérifiez la compatibilité exacte (avec ou sans moteur, gauche/droite).

**Comment savoir si mon lève-vitre est HS ?**
Vitre qui ne monte plus ou très lentement, bruit de moteur sans mouvement (câble cassé), vitre qui descend toute seule, bruit de grincement.

**Tous les combien changer le lève-vitre ?**
Pas de périodicité. Durée de vie variable selon usage. Les portières conducteur s'usent plus vite. Peut durer 150 000+ km ou tomber en panne avant.

**Peut-on changer un lève-vitre soi-même ?**
Oui mais opération délicate. Déposer le panneau de porte, débrancher les connecteurs, dévisser le mécanisme, tenir la vitre. Prévoir 1 à 2h par portière.

**Quelle erreur éviter ?**
Maintenir la vitre pendant l'opération (risque de chute). Vérifier l'interrupteur et le fusible avant de changer le mécanisme. Ne pas forcer une vitre bloquée.
