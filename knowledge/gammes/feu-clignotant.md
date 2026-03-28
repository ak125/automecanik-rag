---
category: eclairage
slug: feu-clignotant
title: Feu clignotant
pg_id: 62
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-25'
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
  role: Signale les changements de direction
  must_be_true:
  - signaler
  - indiquer
  - clignoter
  must_not_contain:
  - injection
  - freinage
  - embrayage
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
  - ❌ "meilleure visibilité"
  cost_range:
    min: 10
    max: 50
    currency: EUR
    unit: répétiteur
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Répétiteur identique à l'origine. Recommandé pour les véhicules récents avec répétiteurs intégrés dans les
      rétroviseurs.
  - tier: Équivalent OE (OES)
    description: Valeo et Hella proposent des répétiteurs OES sur les principaux modèles. Qualité équivalente à l'OE.
  - tier: Adaptable (aftermarket)
    description: Le marché aftermarket est bien développé pour les répétiteurs. Disponibles en version transparente, fumée
      ou LED. L'homologation E est obligatoire.
  brands:
    premium:
    - Osram
    - Philips
    standard:
    - Bosch
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Clignotant lateral qui ne s allume plus
    severity: confort
  - id: S2
    label: Clignotement rapide tableau bord ampoule
    severity: confort
  - id: S3
    label: Repetiteur casse ou fissure choc
    severity: confort
  - id: S4
    label: Eau ou buee visible dans le repetiteur
    severity: confort
  - id: S5
    label: Controle technique refuse signalisation defaillante
    severity: confort
  - id: S6
    label: Ampoule qui grille frequemment infiltration
    severity: confort
  - id: S7
    label: Clignotement plus rapide normale hyper
    severity: confort
  - id: S8
    label: Clignotant fonctionne intermittence maniere aleatoire
    severity: confort
  - id: S9
    label: Odeur plastique fondu court circuit
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : clignotant lateral qui ne s allume plus'
  quick_checks:
  - 'Observer : clignotant lateral qui ne s allume plus ?'
  - 'Observer : clignotement rapide tableau bord ampoule ?'
  - 'Observer : repetiteur casse ou fissure choc ?'
  - 'Observer : eau ou buee visible dans le repetiteur ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Clignotant lateral qui ne s allume plus
  - Clignotement rapide tableau bord ampoule
  - Repetiteur casse ou fissure choc
  - Eau ou buee visible dans le repetiteur
  - Controle technique refuse signalisation defaillante
  - Ampoule qui grille frequemment infiltration
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '62'
  intro_title: A quoi sert Feu clignotant ?
  risk_title: Pourquoi remplacer Feu clignotant a temps ?
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
  - question: Répétiteur clignotant OE ou adaptable ?
    answer: Les répétiteurs adaptables conviennent généralement. Vérifiez l'homologation E obligatoire. Les versions LED transparentes
      ou fumées sont populaires pour personnaliser.
  - question: Comment savoir si mon répétiteur est HS ?
    answer: Clignotant latéral qui ne s'allume plus, clignotement rapide (ampoule grillée), plastique cassé ou fissuré, eau
      à l'intérieur.
  - question: Tous les combien changer le répétiteur ?
    answer: Pas de périodicité. Remplacement si cassé ou si l'ampoule grille souvent (infiltration d'eau). Pièce qui peut
      durer toute la vie du véhicule.
  - question: Peut-on changer un répétiteur soi-même ?
    answer: Oui, très simple. Pousser le répétiteur vers l'avant ou l'arrière pour le déclipser, débrancher l'ampoule ou le
      connecteur, clipser le neuf. 5-10 min.
  - question: Quelle erreur éviter avec le répétiteur ?
    answer: Ne pas forcer pour déclipser (casser les pattes). Vérifier que le joint est en place. Tester le clignotement avant
      de tout remonter.
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
doc_id: 5b464c69-277d-5c5f-9872-23d7e41bc0dd
content_hash: sha256:9992177eb3eee225
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

# Feu clignotant - Guide Diagnostic Complet

## Fonction et Rôle

Signale les changements de direction

**Actions principales:** signaler, indiquer, clignoter

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Repetiteur casse ou fissure choc**
  repetiteur casse ou fissure choc

### 🟢 Autres Symptômes

- clignotant lateral qui ne s allume plus
- clignotement rapide tableau bord ampoule
- eau ou buee visible dans le repetiteur
- controle technique refuse signalisation defaillante
- ampoule qui grille frequemment infiltration
- clignotement plus rapide normale hyper

## Procédure de Diagnostic

Pour diagnostiquer un problème de feu clignotant:

1. **Inspection visuelle** - Examiner l'état du feu clignotant
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

- ampoule-feu-clignotant
- commande-d-eclairage
- feu-arriere
- feu-avant

## Critères de Compatibilité

Pour commander le bon feu clignotant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure visibilité"

## FAQ

**Répétiteur clignotant OE ou adaptable ?**
Les répétiteurs adaptables conviennent généralement. Vérifiez l'homologation E obligatoire. Les versions LED transparentes ou fumées sont populaires pour personnaliser.

**Comment savoir si mon répétiteur est HS ?**
Clignotant latéral qui ne s'allume plus, clignotement rapide (ampoule grillée), plastique cassé ou fissuré, eau à l'intérieur.

**Tous les combien changer le répétiteur ?**
Pas de périodicité. Remplacement si cassé ou si l'ampoule grille souvent (infiltration d'eau). Pièce qui peut durer toute la vie du véhicule.

**Peut-on changer un répétiteur soi-même ?**
Oui, très simple. Pousser le répétiteur vers l'avant ou l'arrière pour le déclipser, débrancher l'ampoule ou le connecteur, clipser le neuf. 5-10 min.

**Quelle erreur éviter avec le répétiteur ?**
Ne pas forcer pour déclipser (casser les pattes). Vérifier que le joint est en place. Tester le clignotement avant de tout remonter.


## Symptomes supplementaires

<!-- materialized-from-db diagnostic/eclairage-voyants.md 2026-02-15 -->
### Diagnostic - Éclairage et signalisation

# Éclairage et signalisation - Diagnostic complet

## Phares et feux

### Phares faibles
- **Ampoules vieillissantes** : Les ampoules halogènes perdent 20-30% de luminosité après 2-3 ans. Remplacement par paire recommandé.
- **Optiques ternies** : Le polycarbonate des phares jaunit et devient opaque avec le temps. Kit de rénovation ou polissage.
- **Réglage incorrect** : Phares trop bas après un chargement ou un remplacement. Réglage avec les vis dédiées.

### Ampoules grillées fréquemment
- **Surtension** : Régulateur d'alternateur défaillant (tension > 14.8V). Mesurer la tension de charge.
- **Vibrations excessives** : Ampoule mal fixée dans son support, vibrations transmises au filament.
- **Mauvaise qualité** : Préférer des ampoules de marque (Philips, Osram, Bosch).

### Feux qui ne fonctionnent pas
- **Fusible grillé** : Vérifier le fusible correspondant dans la boîte à fusibles.
- **Connecteur oxydé** : Humidité dans le porte-ampoule, nettoyage et graisse contact.
- **Problème de masse** : Fil de masse corrodé au niveau du feu. Fréquent sur les feux arrière.

## Contrôle technique - Points éclairage

- Tous les feux doivent fonctionner : croisement, route, position, stop, recul, clignotants, antibrouillard arrière
- Hauteur de faisceau correcte (réglage)
- Pas de fissure laissant entrer l'eau dans les optiques
- Couleur conforme : blanc devant, rouge derrière, orange pour les clignotants

## LED vs Halogène vs Xénon

- **Halogène (H7, H4, H1)** : Standard, remplacement facile, coût faible
- **Xénon (D1S, D2S, D3S)** : Puissant, durée de vie longue, remplacement coûteux, nécessite un ballast
- **LED** : Très longue durée de vie, faible consommation, remplacement du bloc optique entier en cas de panne

## Quand consulter un professionnel

- Phare xénon qui clignote ou change de couleur (ballast ou ampoule)
- Feux LED intégrés défaillants (remplacement du bloc complet)
- Court-circuit récurrent (fusible qui saute à chaque remplacement)
- Défaut de réglage persistant malgré les ajustements
