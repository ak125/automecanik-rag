---
category: capteurs
diagnostic_tree:
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - detecter
  - mesurer
  - transmettre
  must_not_contain_concepts:
  - allumage
  - bougie
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Detecter les vibrations anormales du moteur liees au cliquetis et
    informer le calculateur pour ajuster l'avance
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "corrige la panne"
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
    question: Comment choisir Capteur de cognement compatible avec mon vehicule ?
  - answer: En cas de voyant moteur allume avec code p0325 ou p0327 ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Capteur de cognement ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Capteur de cognement sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Capteur de cognement.
  id: 3921
  intro:
    role: Detecter les vibrations anormales du moteur liees au cliquetis et informer
      le calculateur pour ajuster l'avance
    syncParts:
    - detecter
    - mesurer
    - transmettre
    title: A quoi sert Capteur de cognement ?
  pgId: '3921'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/capteur-de-cognement.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Défaillance électrique** - Problème de connexion, de câblage ou
      de composant électronique'
    title: Pourquoi remplacer Capteur de cognement a temps ?
  symptoms:
  - voyant moteur allume avec code p0325 ou p0327
  - cliquetis metallique a l acceleration detonation
  - perte de puissance notable allumage retarde
  - surconsommation de carburant anormale
  - fumee noire a l echappement
  - moteur qui chauffe plus que d habitude
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 3921
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: capteur-de-cognement
source_type: gamme
symptoms:
- description: voyant moteur allume avec code p0325 ou p0327
  evidence:
  - 'Observation: voyant moteur allume avec code p0325 ou p0327'
  - Vérification visuelle ou auditive
  id: S1
  label: Voyant moteur allume avec code p0325 ou p0327
  risk_level: confort
- description: cliquetis metallique a l acceleration detonation
  evidence:
  - 'Observation: cliquetis metallique a l acceleration detonation'
  - Vérification visuelle ou auditive
  id: S2
  label: Cliquetis metallique a l acceleration detonation
  risk_level: confort
- description: perte de puissance notable allumage retarde
  evidence:
  - 'Observation: perte de puissance notable allumage retarde'
  - Vérification visuelle ou auditive
  id: S3
  label: Perte de puissance notable allumage retarde
  risk_level: confort
- description: surconsommation de carburant anormale
  evidence:
  - 'Observation: surconsommation de carburant anormale'
  - Vérification visuelle ou auditive
  id: S4
  label: Surconsommation de carburant anormale
  risk_level: confort
- description: fumee noire a l echappement
  evidence:
  - 'Observation: fumee noire a l echappement'
  - Vérification visuelle ou auditive
  id: S5
  label: Fumee noire a l echappement
  risk_level: confort
- description: moteur qui chauffe plus que d habitude
  evidence:
  - 'Observation: moteur qui chauffe plus que d habitude'
  - Vérification visuelle ou auditive
  id: S6
  label: Moteur qui chauffe plus que d habitude
  risk_level: confort
title: Capteur de cognement
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Capteur de cognement - Guide Diagnostic Complet

## Fonction et Rôle

Detecter les vibrations anormales du moteur liees au cliquetis et informer le calculateur pour ajuster l'avance

**Actions principales:** detecter, mesurer, transmettre, analyser

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant moteur allume avec code p0325 ou p0327
- cliquetis metallique a l acceleration detonation
- perte de puissance notable allumage retarde
- surconsommation de carburant anormale
- fumee noire a l echappement
- moteur qui chauffe plus que d habitude

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur de cognement:

1. **Inspection visuelle** - Examiner l'état du capteur de cognement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-impulsion
- corps-papillon
- debitmetre-d-air
- injecteur

## Critères de Compatibilité

Pour commander le bon capteur de cognement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la panne"