---
category: embrayage
slug: tringle-de-vitesses
title: Tringle de vitesses
pg_id: 1650
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
  role: Transmettre le mouvement du levier vers la boite
  must_be_true:
  - transmettre
  - guider
  - relier
  must_not_contain:
  - injection
  - freinage
  - climatisation
  - turbo
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - kit-d-embrayage
  - butee-d-embrayage
  - volant-moteur
  - emetteur-d-embrayage
  - recepteur-d-embrayage
  - cable-d-embrayage
  confusion_with:
  - term: piece-d-embrayage-voisine
    difference: Le systeme d embrayage comporte plusieurs pieces (disque, mecanisme, butee, emetteur, recepteur). Verifier
      laquelle est defectueuse.
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
  - ❌ "passage de vitesse parfait"
  cost_range:
    min: 800
    max: 2000
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Pièce identique au premier montage. Jeu articulaire et longueur calibrés selon les spécifications constructeur.
  - tier: Équivalent OE (OES)
    description: Fabricants comme Lemförder, Febi Bilstein ou Sachs produisent ces pièces en première monte pour les constructeurs.
      Même qualité que l'OE.
  - tier: Adaptable (aftermarket)
    description: Pièces aftermarket compatibles. Vérifier la longueur totale, le type de rotule et le mode de fixation (clips,
      goupilles) avant commande.
  brands:
    premium:
    - LuK
    - Sachs
    standard:
    - Valeo
    - Exedy
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Vitesses dures a passer
    severity: confort
  - id: S2
    label: Levier de vitesses flottant
    severity: confort
  - id: S3
    label: Craquements au passage des rapports
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : vitesses dures a passer'
  quick_checks:
  - 'Observer : vitesses dures a passer ?'
  - 'Observer : levier de vitesses flottant ?'
  - 'Observer : craquements au passage des rapports ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Vitesses dures a passer
  - Levier de vitesses flottant
  - Craquements au passage des rapports
  good_practices:
  - Eviter de laisser le pied sur la pedale d embrayage au point mort
  - Remplacement du kit complet (disque + mecanisme + butee)
  - Purge du circuit hydraulique si recepteur/emetteur concerne
  - Verifier le volant moteur lors du remplacement d embrayage
rendering:
  pgId: '1650'
  intro_title: A quoi sert Tringle de vitesses ?
  risk_title: Pourquoi remplacer Tringle de vitesses a temps ?
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
  - question: Comment choisir Tringle de vitesses compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Tringle de vitesses ?
    answer: En cas de vitesses dures a passer ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Tringle de vitesses sans verification atelier ?
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
doc_id: 2b1c5bd6-dbce-5957-9f6e-2db7251b20aa
content_hash: sha256:e8106c1860b759bd
lang: fr
variants:
- name: Kit embrayage complet
  aliases:
  - kit complet
  - 3 pieces
  functional_differences:
  - Disque + mecanisme + butee
  - Remplacement recommande en bloc
- name: Kit avec volant moteur
  aliases:
  - kit 4 pieces
  - kit + volant
  functional_differences:
  - Inclut le volant moteur bimasse
  - Pour vehicules diesel modernes
location_on_vehicle:
  area: Entre le moteur et la boite de vitesses
  access: Depose de la boite de vitesses necessaire (pont elevateur)
  adjacent_parts:
  - volant moteur
  - boite de vitesses
  - arbre primaire
installation:
  difficulty: difficile (pro recommande)
  time: 4h a 8h
  tools:
  - pont elevateur
  - cric de boite
  - centreur d embrayage
  - cle dynamometrique
  prerequisite: Depose complete de la boite de vitesses
---

# Tringle de vitesses - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le mouvement du levier vers la boite

**Actions principales:** transmettre, guider, relier

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- vitesses dures a passer
- levier de vitesses flottant
- craquements au passage des rapports

## Procédure de Diagnostic

Pour diagnostiquer un problème de tringle de vitesses:

1. **Inspection visuelle** - Examiner l'état du tringle de vitesses
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

- fourchette-d-embrayage
- guide-d-embrayage

## Critères de Compatibilité

Pour commander le bon tringle de vitesses, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passage de vitesse parfait"

## FAQ

**Comment choisir Tringle de vitesses compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Tringle de vitesses ?**
En cas de vitesses dures a passer ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Tringle de vitesses sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
