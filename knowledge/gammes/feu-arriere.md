---
category: eclairage
slug: feu-arriere
title: Feu arrière
pg_id: 290
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
  role: Signale la présence et les actions du véhicule
  must_be_true:
  - signaler
  - indiquer
  - eclairer
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
  - ❌ "sécurité maximale"
  cost_range:
    min: 50
    max: 250
    currency: EUR
    unit: bloc complet
    source: catalogue automecanik
  quality_tiers:
  - tier: Équipement d'origine (OE)
    description: Pièce identique à celle montée en usine. Fit parfait, homologation E garantie.
  - tier: Équivalent OE (OES)
    description: Fabricants comme Valeo, Hella ou Magneti Marelli fournissent souvent les constructeurs en premier montage.
      Qualité identique à l'OE.
  - tier: Adaptable (aftermarket)
    description: Fabricants spécialisés dans l'éclairage aftermarket. Rapport qualité/prix acceptable pour usage standard.
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
    label: Arriere allume plus cote stop
    severity: confort
  - id: S2
    label: Buee visible interieur bloc optique
    severity: confort
  - id: S3
    label: Ampoule qui grille frequemment probleme de masse
    severity: confort
  - id: S4
    label: Controle technique refuse pour feux defaillants
    severity: confort
  - id: S5
    label: Plus de 10 ans sans verification des connecteurs
    severity: confort
  - id: S6
    label: Bruit crissement electrique niveau arriere
    severity: confort
  - id: S7
    label: Feux inefficaces car tres faibles a l allumage
    severity: confort
  - id: S8
    label: Odeur plastique surchauffe niveau feux
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : arriere allume plus cote stop'
  quick_checks:
  - 'Observer : arriere allume plus cote stop ?'
  - 'Observer : buee visible interieur bloc optique ?'
  - 'Observer : ampoule qui grille frequemment probleme de masse ?'
  - 'Observer : controle technique refuse pour feux defaillants ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Arriere allume plus cote stop
  - Buee visible interieur bloc optique
  - Ampoule qui grille frequemment probleme de masse
  - Controle technique refuse pour feux defaillants
  - Plus de 10 ans sans verification des connecteurs
  - Bruit crissement electrique niveau arriere
  good_practices:
  - Controle regulier du fonctionnement de tous les feux
  - Remplacement par paire pour eclairage homogene
  - 'Ne pas toucher l ampoule a mains nues (halogen: trace = point chaud)'
  - Reglage des phares apres remplacement d ampoule ou d optique
rendering:
  pgId: '290'
  intro_title: A quoi sert Feu arrière ?
  risk_title: Pourquoi remplacer Feu arrière a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
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
  - question: Feu arrière OE, OES ou adaptable ?
    answer: Les feux OES (Valeo, Hella, Magneti Marelli) sont de qualité équivalente à l'OE. Les adaptables (TYC) offrent
      un bon rapport qualité/prix. Vérifiez l'homologation E.
  - question: Comment savoir si mon feu arrière est HS ?
    answer: Fissure ou casse visible, buée à l'intérieur, ampoules qui grillent souvent, plastique jauni ou opaque, contrôle
      technique refusé.
  - question: Tous les combien changer le feu arrière ?
    answer: Pas de périodicité. Le feu arrière se change uniquement si cassé, fissuré ou défaillant. Durée de vie normale
      = vie du véhicule.
  - question: Peut-on changer un feu arrière soi-même ?
    answer: Oui, opération simple. Ouvrir le coffre, accéder par l'intérieur, dévisser les fixations, débrancher le connecteur,
      retirer le bloc. 15-30 min par côté.
  - question: Quelle erreur éviter avec le feu arrière ?
    answer: Vérifier que le joint d'étanchéité est bien en place. Ne pas serrer excessivement (risque de casse). Tester toutes
      les fonctions après montage.
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
doc_id: b734bd5d-6191-5c78-ada6-25d7f722ff16
content_hash: sha256:f172d301e4a4c2d4
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

# Feu arrière - Guide Diagnostic Complet

## Fonction et Rôle

Signale la présence et les actions du véhicule

**Actions principales:** signaler, indiquer, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- arriere allume plus cote stop
- buee visible interieur bloc optique
- ampoule qui grille frequemment probleme de masse
- controle technique refuse pour feux defaillants
- plus de 10 ans sans verification des connecteurs
- bruit crissement electrique niveau arriere

## Procédure de Diagnostic

Pour diagnostiquer un problème de feu arrière:

1. **Inspection visuelle** - Examiner l'état du feu arrière
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-arriere
- commande-d-eclairage
- contacteur-de-feu-de-recul
- feu-avant
- feu-clignotant
- interrupteur-des-feux-de-freins

## Critères de Compatibilité

Pour commander le bon feu arrière, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "sécurité maximale"

## FAQ

**Feu arrière OE, OES ou adaptable ?**
Les feux OES (Valeo, Hella, Magneti Marelli) sont de qualité équivalente à l'OE. Les adaptables (TYC) offrent un bon rapport qualité/prix. Vérifiez l'homologation E.

**Comment savoir si mon feu arrière est HS ?**
Fissure ou casse visible, buée à l'intérieur, ampoules qui grillent souvent, plastique jauni ou opaque, contrôle technique refusé.

**Tous les combien changer le feu arrière ?**
Pas de périodicité. Le feu arrière se change uniquement si cassé, fissuré ou défaillant. Durée de vie normale = vie du véhicule.

**Peut-on changer un feu arrière soi-même ?**
Oui, opération simple. Ouvrir le coffre, accéder par l'intérieur, dévisser les fixations, débrancher le connecteur, retirer le bloc. 15-30 min par côté.

**Quelle erreur éviter avec le feu arrière ?**
Vérifier que le joint d'étanchéité est bien en place. Ne pas serrer excessivement (risque de casse). Tester toutes les fonctions après montage.


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
