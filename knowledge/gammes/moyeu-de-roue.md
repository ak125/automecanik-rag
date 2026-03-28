---
category: direction
slug: moyeu-de-roue
title: Moyeu de roue
pg_id: 653
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
  role: Supporter la roue et transmettre la rotation - Fixe la roue au roulement
  must_be_true:
  - supporter
  - fixer
  - transmettre
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
    min: 200
    max: 600
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    price_range: Prix élevé — justifié par les certifications de sécurité
  - tier: Équivalent OE (OES)
    price_range: Prix intermédiaire — recommandé pour les applications courantes
  - tier: Aftermarket standard
    price_range: Prix bas — vigilance accrue sur les certifications sécurité
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
    label: Jeu anormal de la roue
    severity: confort
  - id: S2
    label: Vibrations a vitesse constante
    severity: confort
  - id: S3
    label: Bruits sourds en roulant
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - verifier equilibrage et fixations
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'vibrations anormales : verifier equilibrage et fixations'
  quick_checks:
  - 'Observer : jeu anormal de la roue ?'
  - Vibrations a vitesse constante ?
  - Bruits sourds en roulant ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Jeu anormal de la roue
  - Vibrations a vitesse constante
  - Bruits sourds en roulant
  good_practices:
  - Controle du jeu de direction a chaque revision
  - Verifier les soufflets de protection (pas de fuite de graisse)
  - Faire verifier la geometrie apres remplacement
  - Inspecter les biellettes et rotules associees
rendering:
  pgId: '653'
  intro_title: A quoi sert Moyeu de roue ?
  risk_title: Pourquoi remplacer Moyeu de roue a temps ?
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
  - question: Comment choisir Moyeu de roue compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Moyeu de roue ?
    answer: En cas de jeu anormal de la roue ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Moyeu de roue sans verification atelier ?
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
doc_id: 410e21f6-db4d-5ed2-9f60-136bbcc39025
content_hash: sha256:e51d4e7adca4cae1
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

# Moyeu de roue - Guide Diagnostic Complet

## Fonction et Rôle

Supporter la roue et transmettre la rotation - Fixe la roue au roulement

**Actions principales:** supporter, fixer, transmettre, recevoir la roue

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- jeu anormal de la roue
- vibrations a vitesse constante
- bruits sourds en roulant

## Procédure de Diagnostic

Pour diagnostiquer un problème de moyeu de roue:

1. **Inspection visuelle** - Examiner l'état du moyeu de roue
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

- roulement-de-roue
- disque-de-frein

## Critères de Compatibilité

Pour commander le bon moyeu de roue, vous devez connaître:

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

**Comment choisir Moyeu de roue compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Moyeu de roue ?**
En cas de jeu anormal de la roue ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Moyeu de roue sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
