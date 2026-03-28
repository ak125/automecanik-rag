---
category: direction
slug: roulement-de-roue
title: Roulement de roue
pg_id: 655
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-01'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v4_converted
  last_enriched_by: script:rag-enrich-metier-templates
  last_enriched_at: '2026-03-26'
domain:
  role: Permettre la rotation libre de la roue sur son axe - Supporte les charges radiales et axiales
  must_be_true:
  - permettre la rotation
  - supporter
  - guider
  must_not_contain:
  - direction
  - cremailliere
  - volant
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
    min: 40
    max: 150
    currency: EUR
    unit: pièce
    source: catalogue automecanik
  brands:
    premium:
    - SKF
    - FAG (Schaeffler)
    - NTN-SNR
    standard:
    - SNR
    - INA (Schaeffler)
    - Timken
    budget:
    - Febi Bilstein
    - Optimal
    - GSP
  quality_tiers:
  - tier: Origine (OE)
    description: Roulements fabriques par l'equipementier d'origine. Tolerances micrometriques, etancheite et precharge identiques
      a la piece usine.
  - tier: Qualite equivalente OE (OES)
    description: Grands roulementiers mondiaux qui equipent aussi les constructeurs. Qualite tres proche de l'OE.
  - tier: Adaptable de qualite
    description: Marques fiables en entree de gamme. Verifier si le kit inclut l'ecrou de moyeu (souvent a usage unique).
diagnostic:
  symptoms:
  - id: S1
    label: Ronronnement grondement augmente vitesse
    severity: confort
  - id: S2
    label: Bruit qui change d intensite dans les virages
    severity: confort
  - id: S3
    label: Jeu perceptible en secouant la roue montee
    severity: confort
  - id: S4
    label: Vibrations dans le volant a certaines vitesses
    severity: confort
  - id: S5
    label: Roue anormalement chaude apres roulage
    severity: confort
  - id: S6
    label: Bruit de frottement ou de craquement
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'vibrations anormales : verifier equilibrage et fixations'
  quick_checks:
  - 'Observer : ronronnement grondement augmente vitesse ?'
  - Bruit qui change d intensite dans les virages ?
  - 'Observer : jeu perceptible en secouant la roue montee ?'
  - Vibrations dans le volant a certaines vitesses ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Ronronnement grondement augmente vitesse
  - Bruit qui change d intensite dans les virages
  - Jeu perceptible en secouant la roue montee
  - Vibrations dans le volant a certaines vitesses
  - Roue anormalement chaude apres roulage
  - Bruit de frottement ou de craquement
  good_practices:
  - Controle du jeu de direction a chaque revision
  - Verifier les soufflets de protection (pas de fuite de graisse)
  - Faire verifier la geometrie apres remplacement
  - Inspecter les biellettes et rotules associees
rendering:
  pgId: '655'
  intro_title: A quoi sert Roulement de roue ?
  risk_title: Pourquoi remplacer Roulement de roue a temps ?
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
  - question: Roulement de roue OE ou adaptable ?
    answer: 'OES (SKF, FAG, SNR) sont excellents. Vérifiez le type : roulement seul, avec moyeu intégré ou kit complet.'
  - question: Comment savoir si mon roulement de roue est usé ?
    answer: Ronronnement qui varie avec la vitesse, bruit qui change en virage, jeu en secouant la roue, vibrations au volant.
  - question: Tous les combien changer le roulement de roue ?
    answer: Entre 120 000 et 200 000 km. Durée de vie variable. Un roulement peut lâcher avant l'autre.
  - question: Peut-on changer le roulement de roue soi-même ?
    answer: 'Dépend du type. Roulement-moyeu intégré : facile. Roulement à presser : nécessite presse hydraulique.'
  - question: Quelle erreur éviter avec le roulement de roue ?
    answer: Ne pas serrer l'écrou de moyeu au couple exact (trop serré = destruction). Ne pas réutiliser l'écrou si à usage
      unique.
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
doc_id: 32acb057-3062-513a-984e-98ec764ffa5d
content_hash: sha256:f1c9f4271fdb1786
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
---

# Roulement de roue - Guide Diagnostic Complet

## Fonction et Rôle

Permettre la rotation libre de la roue sur son axe - Supporte les charges radiales et axiales

**Actions principales:** permettre la rotation, supporter, guider, rouler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- ronronnement grondement augmente vitesse
- bruit qui change d intensite dans les virages
- jeu perceptible en secouant la roue montee
- vibrations dans le volant a certaines vitesses
- roue anormalement chaude apres roulage
- bruit de frottement ou de craquement

## Procédure de Diagnostic

Pour diagnostiquer un problème de roulement de roue:

1. **Inspection visuelle** - Examiner l'état du roulement de roue
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

- capteur-abs
- disque-de-frein
- plaquette-de-frein

## Critères de Compatibilité

Pour commander le bon roulement de roue, vous devez connaître:

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

**Roulement de roue OE ou adaptable ?**
OES (SKF, FAG, SNR) sont excellents. Vérifiez le type : roulement seul, avec moyeu intégré ou kit complet.

**Comment savoir si mon roulement de roue est usé ?**
Ronronnement qui varie avec la vitesse, bruit qui change en virage, jeu en secouant la roue, vibrations au volant.

**Tous les combien changer le roulement de roue ?**
Entre 120 000 et 200 000 km. Durée de vie variable. Un roulement peut lâcher avant l'autre.

**Peut-on changer le roulement de roue soi-même ?**
Dépend du type. Roulement-moyeu intégré : facile. Roulement à presser : nécessite presse hydraulique.

**Quelle erreur éviter avec le roulement de roue ?**
Ne pas serrer l'écrou de moyeu au couple exact (trop serré = destruction). Ne pas réutiliser l'écrou si à usage unique.
