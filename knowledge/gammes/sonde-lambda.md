---
category: capteurs
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
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
  - mesurer
  - detecter
  - analyser
  must_not_contain_concepts:
  - injecteur
  - pompe
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Mesurer le taux d'oxygene dans les gaz d'echappement pour optimiser
    la combustion et le fonctionnement du catalyseur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "corrige la pollution"
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
    question: Comment choisir Sonde lambda compatible avec mon vehicule ?
  - answer: En cas de voyant moteur allume avec codes p0130 a p0167 ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Sonde lambda ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Sonde lambda sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Sonde lambda.
  id: 3922
  intro:
    role: Mesurer le taux d'oxygene dans les gaz d'echappement pour optimiser la combustion
      et le fonctionnement du catalyseur
    syncParts:
    - mesurer
    - detecter
    - analyser
    title: A quoi sert Sonde lambda ?
  pgId: '3922'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/sonde-lambda.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Sonde lambda a temps ?
  symptoms:
  - voyant moteur allume avec codes p0130 a p0167
  - surconsommation de carburant inexpliquee
  - perte de puissance et ralenti instable
  - fumee noire excessive a l echappement
  - controle technique refuse pour pollution
  - sifflement bruit anormal niveau echappement
  - odeur d essence non brulee a l echappement
  - sonde service depuis plus remplacement
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 3922
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: sonde-lambda
source_type: gamme
symptoms:
- description: voyant moteur allume avec codes p0130 a p0167
  evidence:
  - 'Observation: voyant moteur allume avec codes p0130 a p0167'
  - Vérification visuelle ou auditive
  id: S1
  label: Voyant moteur allume avec codes p0130 a p0167
  risk_level: confort
- description: surconsommation de carburant inexpliquee
  evidence:
  - 'Observation: surconsommation de carburant inexpliquee'
  - Vérification visuelle ou auditive
  id: S2
  label: Surconsommation de carburant inexpliquee
  risk_level: confort
- description: perte de puissance et ralenti instable
  evidence:
  - 'Observation: perte de puissance et ralenti instable'
  - Vérification visuelle ou auditive
  id: S3
  label: Perte de puissance et ralenti instable
  risk_level: confort
- description: fumee noire excessive a l echappement
  evidence:
  - 'Observation: fumee noire excessive a l echappement'
  - Vérification visuelle ou auditive
  id: S4
  label: Fumee noire excessive a l echappement
  risk_level: confort
- description: controle technique refuse pour pollution
  evidence:
  - 'Observation: controle technique refuse pour pollution'
  - Vérification visuelle ou auditive
  id: S5
  label: Controle technique refuse pour pollution
  risk_level: confort
- description: sifflement bruit anormal niveau echappement
  evidence:
  - 'Observation: sifflement bruit anormal niveau echappement'
  - Vérification visuelle ou auditive
  id: S6
  label: Sifflement bruit anormal niveau echappement
  risk_level: confort
- description: odeur d essence non brulee a l echappement
  evidence:
  - 'Observation: odeur d essence non brulee a l echappement'
  - Vérification visuelle ou auditive
  id: S7
  label: Odeur d essence non brulee a l echappement
  risk_level: confort
- description: sonde service depuis plus remplacement
  evidence:
  - 'Observation: sonde service depuis plus remplacement'
  - Vérification visuelle ou auditive
  id: S8
  label: Sonde service depuis plus remplacement
  risk_level: confort
title: Sonde lambda
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Sonde lambda - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer le taux d'oxygene dans les gaz d'echappement pour optimiser la combustion et le fonctionnement du catalyseur

**Actions principales:** mesurer, detecter, analyser, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant moteur allume avec codes p0130 a p0167
- surconsommation de carburant inexpliquee
- perte de puissance et ralenti instable
- fumee noire excessive a l echappement
- controle technique refuse pour pollution
- sifflement bruit anormal niveau echappement

## Procédure de Diagnostic

Pour diagnostiquer un problème de sonde lambda:

1. **Inspection visuelle** - Examiner l'état du sonde lambda
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- bougie-d-allumage
- bougie-de-prechauffage
- catalyseur
- fap

## Critères de Compatibilité

Pour commander le bon sonde lambda, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "corrige la pollution"