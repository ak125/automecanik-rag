---
category: eclairage
slug: relais-de-clignotant
title: Relais de clignotant
pg_id: 61
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
  role: Commande le clignotement intermittent des feux de direction
  must_be_true:
  - commander
  - activer
  - cadencer
  must_not_contain:
  - ampoule
  - feu
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - ampoule-feu-avant
  - ampoule-feu-arriere
  - feu-avant
  - feu-arriere
  - phares-antibrouillard
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
  - ❌ "visibilite parfaite"
  cost_range:
    min: 30
    max: 200
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  brands:
    premium:
    - Hella
    - Bosch
    - Continental/VDO
    standard:
    - Febi Bilstein
    - SWAG
    - Valeo
    budget:
    - Meat & Doria
    - ERA
    - Herth+Buss
  quality_tiers:
  - tier: Origine constructeur (OE/OES)
    description: Relais identique a celui monte en usine. Cadence de clignotement conforme, compatible avec le systeme de
      signalisation d'origine.
  - tier: Equivalent OE (qualite premiere monte)
    description: Relais de qualite equivalente. Cadence et brochage conformes aux specifications constructeur.
  - tier: Adaptable (qualite atelier courant)
    description: Relais compatible. Verifier le nombre de broches et la cadence de clignotement avant montage.
diagnostic:
  symptoms:
  - id: S1
    label: Clignotants ne fonctionnent pas
    severity: confort
  - id: S2
    label: Clignotement trop rapide
    severity: confort
  - id: S3
    label: Clignotement irregulier
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : clignotants ne fonctionnent pas'
  quick_checks:
  - 'Observer : clignotants ne fonctionnent pas ?'
  - 'Observer : clignotement trop rapide ?'
  - 'Observer : clignotement irregulier ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Clignotants ne fonctionnent pas
  - Clignotement trop rapide
  - Clignotement irregulier
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '61'
  intro_title: A quoi sert Relais de clignotant ?
  risk_title: Pourquoi remplacer Relais de clignotant a temps ?
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
  - question: Comment choisir Relais de clignotant compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Relais de clignotant ?
    answer: En cas de clignotants ne fonctionnent pas ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Relais de clignotant sans verification atelier ?
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
doc_id: 67fe4426-2646-529b-a086-d904c8ae938e
content_hash: sha256:9358072a14c379c4
lang: fr
variants:
- name: Ampoule halogene
  aliases:
  - halogene
  - H1
  - H4
  - H7
  functional_differences:
  - Standard, economique
  - Remplacement simple
- name: Ampoule LED
  aliases:
  - LED
  functional_differences:
  - Duree de vie superieure
  - Consommation reduite
  - Verifier homologation
location_on_vehicle:
  area: Face avant, arriere et laterale du vehicule
  access: Par le compartiment moteur (avant) ou coffre (arriere)
  adjacent_parts:
  - optique
  - ampoule
  - connecteur
  - reflecteur
installation:
  difficulty: facile
  time: 5 a 15 min
  tools:
  - tournevis
  - gants (ne pas toucher ampoule halogene)
  prerequisite: Moteur eteint, acces par compartiment moteur ou coffre
---

# Relais de clignotant - Guide Diagnostic Complet

## Fonction et Rôle

Commande le clignotement intermittent des feux de direction

**Actions principales:** commander, activer, cadencer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- clignotants ne fonctionnent pas
- clignotement trop rapide
- clignotement irregulier

## Procédure de Diagnostic

Pour diagnostiquer un problème de relais de clignotant:

1. **Inspection visuelle** - Examiner l'état du relais de clignotant
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

- feu-clignotant
- ampoule-feu-clignotant

## Critères de Compatibilité

Pour commander le bon relais de clignotant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"

## FAQ

**Comment choisir Relais de clignotant compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Relais de clignotant ?**
En cas de clignotants ne fonctionnent pas ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Relais de clignotant sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
