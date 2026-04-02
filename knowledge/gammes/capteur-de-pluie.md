---
category: accessoires
slug: capteur-de-pluie
title: Capteur de pluie
pg_id: 2275
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
  last_enriched_by: skill:phase5-vague6-final
  last_enriched_at: '2026-03-29'
  v5_migrated_at: '2026-03-29'
domain:
  role: Détecte la présence d'eau sur le pare-brise pour activer automatiquement les essuie-glaces
  must_be_true:
  - detecter
  - mesurer
  - analyser
  must_not_contain:
  - balai
  - moteur essuie-glace
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - alternateur
  - batterie
  - demarreur
  - bougie-d-allumage
  - bobine-d-allumage
  - poulie-d-alternateur
  confusion_with:
  - term: piece-electrique-voisine
    difference: Les pieces electriques ont des connecteurs specifiques. Verifier le nombre de broches et le voltage.
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
    min: 50
    max: 300
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  brands:
    premium:
    - Bosch
    - Valeo
    - Denso
    standard:
    - Hella
    - NGK
    - Delphi
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Essuie-glaces declenches sans pluie
    severity: confort
  - id: S2
    label: Essuie-glaces automatiques inactifs
    severity: confort
  - id: S3
    label: Vitesse d essuyage inadaptee a l intensite
    severity: confort
  causes:
  - inspection visuelle et test fonctionnel
  - 'symptome general detecte : inspection visuelle et test fonctionnel'
  - 'Usure ou defaillance causant : essuie-glaces declenches sans pluie'
  quick_checks:
  - 'Observer : essuie-glaces declenches sans pluie ?'
  - 'Observer : essuie-glaces automatiques inactifs ?'
  - 'Observer : vitesse d essuyage inadaptee a l intensite ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Essuie-glaces declenches sans pluie
  - Essuie-glaces automatiques inactifs
  - Vitesse d essuyage inadaptee a l intensite
  good_practices:
  - Controle de la tension et du courant avec un multimetre
  - Verifier les connexions electriques (oxydation, jeu)
  - Remplacement preventif si signes de faiblesse avant l hiver
  - Ne pas laisser le vehicule immobilise longtemps sans protection
rendering:
  pgId: '2275'
  intro_title: A quoi sert Capteur de pluie ?
  risk_title: Pourquoi remplacer Capteur de pluie a temps ?
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
  - question: Comment choisir Capteur de pluie compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Capteur de pluie ?
    answer: En cas de essuie-glaces declenches sans pluie ou de degradation mesurable, il faut controler rapidement avant
      panne secondaire.
  - question: Puis-je monter Capteur de pluie sans verification atelier ?
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
doc_id: c8b1a08a-b456-5599-ba25-fd58722f6a08
content_hash: sha256:47775e1069634a29
lang: fr
variants:
- name: Piece neuve OE/OES
  aliases:
  - neuf
  - OE
  - OES
  functional_differences:
  - Garantie constructeur ou equipementier
  - Calibration d usine
- name: Piece echange standard
  aliases:
  - echange standard
  - reconditionne
  functional_differences:
  - Moins cher
  - Piece d origine reconditionnee
location_on_vehicle:
  area: Compartiment moteur (alternateur, demarreur) ou peripherie
  access: Par le dessus (capot) ou par le dessous selon modele
  adjacent_parts:
  - faisceau electrique
  - batterie
  - fusibles
installation:
  difficulty: facile a moyen
  time: 15min a 1h
  tools:
  - cle a douille
  - multimetre
  - tournevis
  prerequisite: Debrancher la batterie avant intervention
phase5_enrichment:
  _source: contenu LLM — a revalider contre sources OEM
  _validation_status: pending_oem_validation
  _enriched_at: '2026-03-30'
  technical_notes:
    type: 'capteur optique infrarouge colle sur le pare-brise (face interieure)'
    calibration: 'recalibration necessaire apres remplacement du pare-brise'
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: >-
    Détecte la présence d'eau sur le pare-brise pour activer automatiquement les
    essuie-glaces. Pièces liées : vérifier les composants adjacents lors du
    remplacement.
  S2: >-
    Intervalle : selon constructeur. Symptômes de défaillance : - Essuie-glaces
    declenches sans pluie- Essuie-glaces automatiques inactifs- Vitesse d
    essuyage inadaptee a l intensite
  S3: >-
    Pour choisir le bon capteur de pluie pour votre véhicule : - Marque de votre
    véhicule- Modele de votre véhicule- Annee de votre véhicule- Marques :
    Bosch, Valeo, Denso (premium), Hella, NGK, Delphi (standard), Ridex, Topran
    (budget)- Budget : 50 à 300 EUR
  S4_DEPOSE: >-
    1. Débrancher la batterie. 2. Localiser la pièce selon la documentation
    constructeur. 3. Déconnecter les connecteurs électriques et raccords. 4.
    Dévisser les fixations de la pièce. 5. Déposer la pièce en notant
    l'orientation et la position de montage. 6. Nettoyer le logement et vérifier
    l'état des pièces adjacentes.
  S5: >-
    Erreurs fréquentes avec le capteur de pluie : - Ne pas vérifier la référence
    exacte avant commande — une pièce de mauvaise référence ne fonctionne pas
    correctement même si elle se monte physiquement- Oublier de débrancher la
    batterie avant intervention — risque de court-circuit sur les composants
    électroniques- Ne pas respecter le couple de serrage constructeur au
    remontage- Ignorer les symptômes d'usure en espérant que ça passe — une
    défaillance progressive s'aggrave toujours- Ne pas effacer les codes défaut
    après remplacement — le calculateur peut rester en mode dégradé
  S6: >-
    Après le remplacement du capteur de pluie : - Controle de la tension et du
    courant avec un multimetre- Verifier les connexions electriques (oxydation,
    jeu)- Remplacement preventif si signes de faiblesse avant l hiver- Ne pas
    laisser le vehicule immobilise longtemps sans protection- Effacer les codes
    défaut éventuels avec l'outil OBD- Effectuer un essai route pour confirmer
    la disparition des symptômes
---

# Capteur de pluie - Guide Diagnostic Complet

## Fonction et Rôle

Détecte la présence d'eau sur le pare-brise pour activer automatiquement les essuie-glaces

**Actions principales:** detecter, mesurer, analyser

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- essuie-glaces declenches sans pluie
- essuie-glaces automatiques inactifs
- vitesse d essuyage inadaptee a l intensite

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur de pluie:

1. **Inspection visuelle** - Examiner l'état du capteur de pluie
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

- moteur-d-essuie-glace
- commande-essuie-glace
- balai-d-essuie-glace

## Critères de Compatibilité

Pour commander le bon capteur de pluie, vous devez connaître:

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

**Comment choisir Capteur de pluie compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Capteur de pluie ?**
En cas de essuie-glaces declenches sans pluie ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Capteur de pluie sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
