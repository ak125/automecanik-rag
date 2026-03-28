---
category: suspension
slug: sphere-de-suspension
title: Sphère de suspension
pg_id: 1718
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
  role: Assurer la suspension via pression hydraulique et gaz (systeme Citroen). Remplace amortisseur ET ressort. NE FONCTIONNE
    PAS COMME UN RESSORT CLASSIQUE!
  must_be_true:
  - stabiliser hydrauliquement
  - reguler la pression
  - amortir hydrauliquement
  must_not_contain:
  - ressort helicoidale
  - amortisseur classique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - amortisseur
  - ressort-de-suspension
  - bras-de-suspension
  - rotule-de-suspension
  - barre-stabilisatrice
  - biellette-de-barre-stabilisatrice
  confusion_with:
  - term: piece-de-suspension-voisine
    difference: Les pieces de suspension travaillent ensemble mais ont des references distinctes. Verifier la position (avant/arriere,
      gauche/droite).
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
  - ❌ "tenue de route parfaite"
  cost_range:
    min: 300
    max: 800
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  brands:
    premium:
    - Citroen Genuine Parts
    - DS Automobiles
    standard:
    - Monroe (Tenneco)
    - Lizarte
    - Dunlop
    budget:
    - Febi Bilstein
    - Optimal
    - NK
  quality_tiers:
  - tier: Origine constructeur
    description: Spheres de suspension d origine Citroen/DS, chargees en azote a la pression nominale specifiee pour chaque
      position (avant, arriere, accumulateur).
  - tier: Equipementier qualite OE
    description: Spheres fabriquees selon les specifications Citroen avec membrane et charge d azote conformes. Pression de
      precharge verifiee.
  - tier: Adaptable qualite reconnue
    description: Spheres compatibles avec verification de la pression de precharge et de la qualite de la membrane avant montage.
diagnostic:
  symptoms:
  - id: S1
    label: Suspension tres dure
    severity: securite
  - id: S2
    label: Vehicule qui ne monte plus en hauteur
    severity: confort
  - id: S3
    label: Confort de roulement degrade
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : suspension tres dure'
  quick_checks:
  - 'Observer : suspension tres dure ?'
  - 'Observer : vehicule qui ne monte plus en hauteur ?'
  - 'Observer : confort de roulement degrade ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Suspension tres dure
  - Vehicule qui ne monte plus en hauteur
  - Confort de roulement degrade
  good_practices:
  - Controle visuel des fuites et deformations a chaque revision
  - Remplacement par paire (meme essieu) pour equilibre du vehicule
  - Faire verifier la geometrie apres remplacement
  - Inspection des silent-blocs et des rotules associees
rendering:
  pgId: '1718'
  intro_title: A quoi sert Sphère de suspension ?
  risk_title: Pourquoi remplacer Sphère de suspension a temps ?
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
  - question: Comment choisir Sphère de suspension compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Sphère de suspension ?
    answer: En cas de suspension tres dure ou de degradation mesurable, il faut controler rapidement avant panne secondaire.
  - question: Puis-je monter Sphère de suspension sans verification atelier ?
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
doc_id: eb4d0f2f-dd14-5143-b17f-1350fadea53a
content_hash: sha256:91f7f5a6a7e80820
lang: fr
variants:
- name: Version gaz
  aliases:
  - gaz
  - gas-a-just
  functional_differences:
  - Meilleure tenue de route
  - Plus ferme que l huile
- name: Version huile
  aliases:
  - huile
  - hydraulique
  functional_differences:
  - Confort de conduite superieur
  - Moins cher que le gaz
location_on_vehicle:
  area: Entre la roue et la carrosserie (avant et/ou arriere)
  access: Par le dessous (pont elevateur) ou demontage roue
  adjacent_parts:
  - amortisseur
  - ressort
  - bras
  - rotule
installation:
  difficulty: moyen a difficile
  time: 1h a 2h par cote
  tools:
  - compresseur de ressort
  - cle a douille
  - cle dynamometrique
  - arrache-rotule
  prerequisite: Pont elevateur recommande, vehicule decharge
---

# Sphère de suspension - Guide Diagnostic Complet

## Fonction et Rôle

Assurer la suspension via pression hydraulique et gaz (systeme Citroen). Remplace amortisseur ET ressort. NE FONCTIONNE PAS COMME UN RESSORT CLASSIQUE!

**Actions principales:** stabiliser hydrauliquement, reguler la pression, amortir hydrauliquement, maintenir la hauteur

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Suspension tres dure**
  suspension tres dure

### 🟢 Autres Symptômes

- vehicule qui ne monte plus en hauteur
- confort de roulement degrade

## Procédure de Diagnostic

Pour diagnostiquer un problème de sphère de suspension:

1. **Inspection visuelle** - Examiner l'état du sphère de suspension
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

- amortisseur
- suspension

## Critères de Compatibilité

Pour commander le bon sphère de suspension, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "tenue de route parfaite"

## FAQ

**Comment choisir Sphère de suspension compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Sphère de suspension ?**
En cas de suspension tres dure ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Sphère de suspension sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
