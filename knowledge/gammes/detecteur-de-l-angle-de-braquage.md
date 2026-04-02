---
category: direction
slug: detecteur-de-l-angle-de-braquage
title: Détecteur de l'angle de braquage
pg_id: 3252
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
  role: Mesurer l'angle de rotation du volant pour l'ESP
  must_be_true:
  - mesurer
  - detecter
  - transmettre
  must_not_contain:
  - injection
  - freinage
  - distribution
  - turbo
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - cremailliere-de-direction
  - rotule-de-direction
  - pompe-de-direction-assistee
  - barre-de-direction
  - soufflet-de-direction
  - colonne-de-direction
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Détecteur de l'angle de braquage.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Respecter le type de direction (assistee hydraulique, electrique, mecanique)
  - Choisir un equipementier certifie (TRW, Lemforder, Febi) pour la securite
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "direction parfaite"
  cost_range:
    min: 200
    max: 600
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipementier d'origine (OE)
    description: Pièce identique à celle montée en usine. Référence constructeur garantie, codage plug-and-play sans recalibration
      spécifique dans la plupart des cas.
  - tier: Équivalent OE (équipementiers premier rang)
    description: Produit des fabricants qui approvisionnent les constructeurs automobiles. Tolérance et plage de mesure identiques
      à la pièce d'origine.
  - tier: Pièce adaptable
    description: Prix inférieur, peut convenir sur certains modèles. Vérifier impérativement la plage angulaire, le protocole
      de communication (CAN/LIN) et la référence avant commande.
  brands:
    premium:
    - Lemforder
    - TRW
    standard:
    - Febi
    - Meyle
    - MOOG
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Voyant esp allume en permanence
    severity: securite
  - id: S2
    label: Direction assistee desactivee
    severity: securite
  - id: S3
    label: Comportement anormal du vehicule en virage
    severity: confort
  causes:
  - lecture codes defaut obd et diagnostic electronique
  - 'Usure ou defaillance causant : voyant esp allume en permanence'
  - 'Usure ou defaillance causant : direction assistee desactivee'
  quick_checks:
  - Voyant esp allume en permanence ?
  - 'Observer : direction assistee desactivee ?'
  - 'Observer : comportement anormal du vehicule en virage ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant esp allume en permanence
  - Direction assistee desactivee
  - Comportement anormal du vehicule en virage
  good_practices:
  - Controle du jeu de direction a chaque revision
  - Verifier les soufflets de protection (pas de fuite de graisse)
  - Faire verifier la geometrie apres remplacement
  - Inspecter les biellettes et rotules associees
rendering:
  pgId: '3252'
  intro_title: A quoi sert Détecteur de l'angle de braquage ?
  risk_title: Pourquoi remplacer Détecteur de l'angle de braquage a temps ?
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
  - question: Comment choisir Détecteur de l'angle de braquage compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Détecteur de l'angle de braquage ?
    answer: En cas de voyant esp allume en permanence ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Détecteur de l'angle de braquage sans verification atelier ?
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
doc_id: a4e31860-1b48-57a1-92c0-023de5db7a3e
content_hash: sha256:3553e143a764599a
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
  area: Sous le vehicule, relie le volant aux roues
  access: Par le dessous (pont elevateur recommande)
  adjacent_parts:
  - cremailliere
  - biellette
  - rotule
  - soufflet
installation:
  difficulty: difficile
  time: 1h a 3h
  tools:
  - cle a douille
  - arrache-rotule
  - cle dynamometrique
  prerequisite: Pont elevateur, geometrie a refaire apres
phase5_enrichment:
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    calibration: 'reinitialisation obligatoire apres toute intervention sur la direction/trains roulants'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Mesurer l'angle de rotation du volant pour l'ESP. Pièces liées : vérifier
    les composants adjacents lors du remplacement.
  S2: >-
    Intervalle : selon constructeur. Symptômes de défaillance : - Voyant esp
    allume en permanence- Direction assistee desactivee- Comportement anormal du
    vehicule en virage
  S3: >-
    Pour choisir le bon détecteur de l'angle de braquage pour votre véhicule : -
    Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Détecteur de
    l'angle de braquage.- Verifier la reference OE ou equivalence constructeur
    pour le vehicule exact- Respecter le type de direction (assistee
    hydraulique, electrique, mecanique)- Choisir un equipementier certifie (TRW,
    Lemforder, Febi) pour la securite- Marques : Lemforder, TRW (premium), Febi,
    Meyle, MOOG (standard), Ridex, Topran (budget)- Budget : 200 à 600 EUR
  S4_DEPOSE: >-
    1. Débrancher la batterie. 2. Localiser la pièce selon la documentation
    constructeur. 3. Déconnecter les connecteurs électriques et raccords. 4.
    Dévisser les fixations de la pièce. 5. Déposer la pièce en notant
    l'orientation et la position de montage. 6. Nettoyer le logement et vérifier
    l'état des pièces adjacentes.
  S5: >-
    Erreurs fréquentes avec le détecteur de l'angle de braquage : - Ne pas
    vérifier la référence exacte avant commande — une pièce de mauvaise
    référence ne fonctionne pas correctement même si elle se monte physiquement-
    Oublier de débrancher la batterie avant intervention — risque de court-
    circuit sur les composants électroniques- Ne pas respecter le couple de
    serrage constructeur au remontage- Ignorer les symptômes d'usure en espérant
    que ça passe — une défaillance progressive s'aggrave toujours- Ne pas
    effacer les codes défaut après remplacement — le calculateur peut rester en
    mode dégradé
  S6: >-
    Après le remplacement du détecteur de l'angle de braquage : - Controle du
    jeu de direction a chaque revision- Verifier les soufflets de protection
    (pas de fuite de graisse)- Faire verifier la geometrie apres remplacement-
    Inspecter les biellettes et rotules associees- Effacer les codes défaut
    éventuels avec l'outil OBD- Effectuer un essai route pour confirmer la
    disparition des symptômes
---

# Détecteur de l'angle de braquage - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer l'angle de rotation du volant pour l'ESP

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant esp allume en permanence**
  voyant esp allume en permanence
- **Direction assistee desactivee**
  direction assistee desactivee

### 🟢 Autres Symptômes

- comportement anormal du vehicule en virage

## Procédure de Diagnostic

Pour diagnostiquer un problème de détecteur de l'angle de braquage:

1. **Inspection visuelle** - Examiner l'état du détecteur de l'angle de braquage
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

- calculateur-esp
- capteur-abs

## Critères de Compatibilité

Pour commander le bon détecteur de l'angle de braquage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "direction parfaite"

## FAQ

**Comment choisir Détecteur de l'angle de braquage compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Détecteur de l'angle de braquage ?**
En cas de voyant esp allume en permanence ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Détecteur de l'angle de braquage sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
