---
category: climatisation
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - absorber la chaleur
  must_not_contain_concepts:
  - moteur
  - refroidissement
  - radiateur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Absorbe la chaleur de l'air habitacle pour produire du froid - Circuit
    habitacle uniquement
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "refroidit le moteur"
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
  - answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference
      exacte avant montage.
    question: Comment choisir Evaporateur de climatisation compatible avec mon vehicule
      ?
  - answer: En cas de climatisation inefficace malgre recharge recente ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Evaporateur de climatisation ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Evaporateur de climatisation sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de climatisation pour confirmer Evaporateur de
    climatisation.
  id: 471
  intro:
    role: Absorbe la chaleur de l'air habitacle pour produire du froid - Circuit habitacle
      uniquement
    syncParts:
    - absorber la chaleur
    title: A quoi sert Evaporateur de climatisation ?
  pgId: '471'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/evaporateur-de-climatisation.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Evaporateur de climatisation a temps ?
  symptoms:
  - climatisation inefficace malgre recharge recente
  - odeur de moisi ou d humidite a la ventilation
  - buee persistante sur le pare-brise en mode clim
  - flaque d eau anormale sous le tableau de bord
  - bruit gargouillement boitier ventilation
  - mauvaises odeurs des l enclenchement de la clim
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 471
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: evaporateur-de-climatisation
source_type: gamme
symptoms:
- description: climatisation inefficace malgre recharge recente
  evidence:
  - 'Observation: climatisation inefficace malgre recharge recente'
  - Vérification visuelle ou auditive
  id: S1
  label: Climatisation inefficace malgre recharge recente
  risk_level: confort
- description: odeur de moisi ou d humidite a la ventilation
  evidence:
  - 'Observation: odeur de moisi ou d humidite a la ventilation'
  - Vérification visuelle ou auditive
  id: S2
  label: Odeur de moisi ou d humidite a la ventilation
  risk_level: confort
- description: buee persistante sur le pare-brise en mode clim
  evidence:
  - 'Observation: buee persistante sur le pare-brise en mode clim'
  - Vérification visuelle ou auditive
  id: S3
  label: Buee persistante sur le pare-brise en mode clim
  risk_level: confort
- description: flaque d eau anormale sous le tableau de bord
  evidence:
  - 'Observation: flaque d eau anormale sous le tableau de bord'
  - Vérification visuelle ou auditive
  id: S4
  label: Flaque d eau anormale sous le tableau de bord
  risk_level: confort
- description: bruit gargouillement boitier ventilation
  evidence:
  - 'Observation: bruit gargouillement boitier ventilation'
  - Vérification visuelle ou auditive
  id: S5
  label: Bruit gargouillement boitier ventilation
  risk_level: confort
- description: mauvaises odeurs des l enclenchement de la clim
  evidence:
  - 'Observation: mauvaises odeurs des l enclenchement de la clim'
  - Vérification visuelle ou auditive
  id: S6
  label: Mauvaises odeurs des l enclenchement de la clim
  risk_level: confort
title: Evaporateur de climatisation
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Evaporateur de climatisation - Guide Diagnostic Complet

## Fonction et Rôle

Absorbe la chaleur de l'air habitacle pour produire du froid - Circuit habitacle uniquement

**Actions principales:** absorber la chaleur

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- climatisation inefficace malgre recharge recente
- odeur de moisi ou d humidite a la ventilation
- buee persistante sur le pare-brise en mode clim
- flaque d eau anormale sous le tableau de bord
- bruit gargouillement boitier ventilation
- mauvaises odeurs des l enclenchement de la clim

## Procédure de Diagnostic

Pour diagnostiquer un problème de evaporateur de climatisation:

1. **Inspection visuelle** - Examiner l'état du evaporateur de climatisation
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- compresseur-de-climatisation
- condenseur-de-climatisation
- detendeur-de-climatisation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle

## Critères de Compatibilité

Pour commander le bon evaporateur de climatisation, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit le moteur"