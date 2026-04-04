---
category: climatisation
slug: gicleur-detendeur
title: Gicleur détendeur
pg_id: 2408
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
  role: Detendre le fluide frigorigene avant l'evaporateur
  must_be_true:
  - detendre
  - abaisser la pression
  must_not_contain:
  - injection
  - freinage
  - allumage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - compresseur-de-climatisation
  - condenseur-de-climatisation
  - evaporateur-de-climatisation
  - filtre-d-habitacle
  - detendeur-de-climatisation
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de climatisation
    pour confirmer Gicleur détendeur.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Respecter le type de gaz refrigerant (R134a, R1234yf) pour la compatibilite
  - Choisir un equipementier reconnu (Denso, Valeo, Delphi, NRF)
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "refroidit instantanement"
  cost_range:
    min: 10
    max: 40
    currency: EUR
    unit: pièce
    source: catalogue automecanik
  quality_tiers:
  - tier: Qualité Origine (OE)
    description: Gicleurs détendeurs calibrés en usine par les équipementiers de climatisation automobile. Orifice de détente
      usiné avec précision pour un débit frigorigène optimal.
  - tier: Équivalent Qualité Origine
    description: Détendeurs fabriqués selon les mêmes spécifications de débit et de pression que l'OE. Compatibilité avec
      les fluides frigorigènes R134a et R1234yf.
  - tier: Adaptable Économique
    description: Gicleurs détendeurs aux dimensions compatibles. Conviennent pour la remise en état du circuit de climatisation.
      Vérifier le type de raccord et le calibre.
  brands:
    premium:
    - Denso
    - Valeo
    standard:
    - NRF
    - Delphi
    - Hella
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Clim qui refroidit mal
    severity: confort
  - id: S2
    label: Givre visible sur les conduites
    severity: confort
  - id: S3
    label: Clim qui fonctionne par a-coups
    severity: confort
  - id: S4
    label: Compresseur qui s emballe
    severity: confort
  - id: S5
    label: Bruits de glouglou dans le circuit
    severity: confort
  - id: S6
    label: Clim qui marche puis s arrete
    severity: confort
  - id: S7
    label: Pressions instables au diagnostic
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'Usure ou defaillance causant : clim qui refroidit mal'
  - 'Usure ou defaillance causant : givre visible sur les conduites'
  quick_checks:
  - 'Observer : clim qui refroidit mal ?'
  - 'Observer : givre visible sur les conduites ?'
  - 'Observer : clim qui fonctionne par a-coups ?'
  - 'Observer : compresseur qui s emballe ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Clim qui refroidit mal
  - Givre visible sur les conduites
  - Clim qui fonctionne par a-coups
  - Compresseur qui s emballe
  - Bruits de glouglou dans le circuit
  - Clim qui marche puis s arrete
  good_practices:
  - Faire tourner la climatisation 10 min par semaine meme en hiver
  - Remplacement du filtre d habitacle chaque annee
  - Recharge de gaz par un professionnel equipe (circuit sous pression)
  - Controle d etancheite si baisse de performance
rendering:
  pgId: '2408'
  intro_title: A quoi sert Gicleur détendeur ?
  risk_title: Pourquoi remplacer Gicleur détendeur a temps ?
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
  - question: Quelle différence entre gicleur et détendeur ?
    answer: Le gicleur est un simple orifice calibré (système moins coûteux). Le détendeur est une valve thermostatique plus
      précise. Les deux régulent le débit.
  - question: Comment savoir lequel j'ai ?
    answer: Les véhicules américains et certains asiatiques utilisent des gicleurs (orifice tubes). Les européens utilisent
      généralement des détendeurs.
  - question: Le gicleur s'use-t-il ?
    answer: L'orifice peut se boucher avec des particules ou de l'humidité. Le maillage du filtre intégré peut se colmater.
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Confondre gicleur et détendeur (incompatibles). Ne pas changer l'accumulateur avec le gicleur. Oublier le tirage
      au vide.
  - question: Comment faire un diagnostic rapide ?
    answer: Gicleur bouché → BP très basse, pas de froid. Gicleur usé → pressions instables. Filtre colmaté → débit faible.
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
doc_id: 377ff578-9d9a-5e87-94c7-ab01d625b7c2
content_hash: sha256:19584d02e3218430
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
  area: Face avant (condenseur), habitacle (evaporateur), moteur (compresseur)
  access: Variable selon composant (capot, tableau de bord, face avant)
  adjacent_parts:
  - compresseur
  - condenseur
  - detendeur
  - evaporateur
installation:
  difficulty: difficile (pro obligatoire)
  time: 1h a 4h
  tools:
  - station de recharge
  - detecteur de fuites
  - cle a douille
  prerequisite: Recuperation du gaz obligatoire par professionnel agree
phase5_enrichment:
  _source: denso-am.eu + fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 2
  _has_tech_data: true
  types_variants:
  - type: 'plein'
    source_ref: corpus RAG web OEM
  - type: 'électrique'
    source_ref: corpus RAG web OEM
  technical_notes:
    val_000_km: '000 km'
    val_100__c: '100 °C'
    val_1000_a: '1000 a'
    val_15_a: '15 a'
    val_21_a: '21 a'
    val_23_a: '23 a'
    val_240_a: '240 a'
    val_25__: '25 %'
    val_25_mm: '25 mm'
    val_30_a: '30 a'
    val_33__: '33 %'
    val_400_bars: '400 bars'
    val_50_kw: '50 kW'
    val_6_mm: '6 mm'
    val_625__c: '625 °C'
  materials:
  - materiau: 'aluminium'
    source_ref: corpus RAG web OEM
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Detendre le fluide frigorigene avant l''evaporateur. Pièces liées : vérifier les composants adjacents lors du remplacement.'
  S2: 'Intervalle : selon constructeur. Symptômes de défaillance : - Clim qui refroidit mal- Givre visible sur les conduites-
    Clim qui fonctionne par a-coups- Compresseur qui s emballe- Bruits de glouglou dans le circuit- Clim qui marche puis s
    arrete'
  S3: 'Pour choisir le bon gicleur détendeur pour votre véhicule : - Renseignez marque, modele, type puis comparez references
    et dimensions. Validez ensuite les contraintes de climatisation pour confirmer Gicleur détendeur.- Verifier la reference
    OE ou equivalence constructeur pour le vehicule exact- Respecter le type de gaz refrigerant (R134a, R1234yf) pour la compatibilite-
    Choisir un equipementier reconnu (Denso, Valeo, Delphi, NRF)- Marques : Denso, Valeo (premium), NRF, Delphi, Hella (standard),
    Ridex (budget)- Budget : 10 à 40 EUR'
  S4_DEPOSE: 1. Débrancher la batterie. 2. Localiser la pièce selon la documentation constructeur. 3. Déconnecter les connecteurs
    électriques et raccords. 4. Dévisser les fixations de la pièce. 5. Déposer la pièce en notant l'orientation et la position
    de montage. 6. Nettoyer le logement et vérifier l'état des pièces adjacentes.
  S5: 'Erreurs fréquentes avec le gicleur détendeur : - Ne pas vérifier la référence exacte avant commande — une pièce de
    mauvaise référence ne fonctionne pas correctement même si elle se monte physiquement- Oublier de débrancher la batterie
    avant intervention — risque de court-circuit sur les composants électroniques- Confondre gicleur et détendeur (incompatibles).
    Ne pas changer l''accumulateur avec le gicleur. Oublier le tirage au vide.- Ne pas respecter le couple de serrage constructeur
    au remontage- Ignorer les symptômes d''usure en espérant que ça passe — une défaillance progressive s''aggrave toujours-
    Ne pas effacer les codes défaut après remplacement — le calculateur peut rester en mode dégradé'
  S6: 'Après le remplacement du gicleur détendeur : - Faire tourner la climatisation 10 min par semaine meme en hiver- Remplacement
    du filtre d habitacle chaque annee- Recharge de gaz par un professionnel equipe (circuit sous pression)- Controle d etancheite
    si baisse de performance- Effacer les codes défaut éventuels avec l''outil OBD- Effectuer un essai route pour confirmer
    la disparition des symptômes'
---

# Gicleur détendeur - Guide Diagnostic Complet

## Fonction et Rôle

Detendre le fluide frigorigene avant l'evaporateur

**Actions principales:** detendre, abaisser la pression

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- clim qui refroidit mal
- givre visible sur les conduites
- clim qui fonctionne par a-coups
- compresseur qui s emballe
- bruits de glouglou dans le circuit
- clim qui marche puis s arrete

## Procédure de Diagnostic

Pour diagnostiquer un problème de gicleur détendeur:

1. **Inspection visuelle** - Examiner l'état du gicleur détendeur
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

- evaporateur-de-climatisation
- conduite-de-climatisation

## Critères de Compatibilité

Pour commander le bon gicleur détendeur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit instantanement"

## FAQ

**Quelle différence entre gicleur et détendeur ?**
Le gicleur est un simple orifice calibré (système moins coûteux). Le détendeur est une valve thermostatique plus précise. Les deux régulent le débit.

**Comment savoir lequel j'ai ?**
Les véhicules américains et certains asiatiques utilisent des gicleurs (orifice tubes). Les européens utilisent généralement des détendeurs.

**Le gicleur s'use-t-il ?**
L'orifice peut se boucher avec des particules ou de l'humidité. Le maillage du filtre intégré peut se colmater.

**Quelles sont les erreurs fréquentes à éviter ?**
Confondre gicleur et détendeur (incompatibles). Ne pas changer l'accumulateur avec le gicleur. Oublier le tirage au vide.

**Comment faire un diagnostic rapide ?**
Gicleur bouché → BP très basse, pas de froid. Gicleur usé → pressions instables. Filtre colmaté → débit faible.


## References supplementaires

<!-- materialized-from-db manual/8198ade9ad34 2026-04-03 -->
### Données techniques OEM — Gicleur détendeur

# Données techniques OEM — Gicleur détendeur
Source : denso-am.eu + fr.wikipedia.org (2 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- plein
- électrique

## Matériaux
- aluminium

## Valeurs techniques de référence
- 100 °C
- 25 %
- 25 mm
- 33 %
- 400 bars
- 6 mm
- 625 °C
