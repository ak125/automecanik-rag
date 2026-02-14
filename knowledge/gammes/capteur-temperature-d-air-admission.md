---
category: capteurs
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: kilometrage_eleve_ou_usure_visible
  then: remplacement_preventif_recommande
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
  - transmettre
  must_not_contain_concepts:
  - echappement
  - refroidissement
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Mesurer la temperature de l'air entrant dans le moteur pour optimiser
    le melange air-carburant
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
    question: Comment choisir Capteur température d'air admission compatible avec
      mon vehicule ?
  - answer: En cas de surconsommation de carburant anormale ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Capteur température d'air admission ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Capteur température d'air admission sans verification
      atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Capteur température
    d'air admission.
  id: 3939
  intro:
    role: Mesurer la temperature de l'air entrant dans le moteur pour optimiser le
      melange air-carburant
    syncParts:
    - mesurer
    - detecter
    - transmettre
    title: A quoi sert Capteur température d'air admission ?
  pgId: '3939'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/capteur-temperature-d-air-admission.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Capteur température d'air admission a temps ?
  symptoms:
  - surconsommation de carburant anormale
  - ralenti instable surtout a froid
  - sifflement anormal a l admission
  - fumee noire a l echappement
  - odeur de carburant non brule
  - plus de 150 000 km sans verification
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 3939
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: capteur-temperature-d-air-admission
source_type: gamme
symptoms:
- description: surconsommation de carburant anormale
  evidence:
  - 'Observation: surconsommation de carburant anormale'
  - Vérification visuelle ou auditive
  id: S1
  label: Surconsommation de carburant anormale
  risk_level: confort
- description: ralenti instable surtout a froid
  evidence:
  - 'Observation: ralenti instable surtout a froid'
  - Vérification visuelle ou auditive
  id: S2
  label: Ralenti instable surtout a froid
  risk_level: confort
- description: sifflement anormal a l admission
  evidence:
  - 'Observation: sifflement anormal a l admission'
  - Vérification visuelle ou auditive
  id: S3
  label: Sifflement anormal a l admission
  risk_level: confort
- description: fumee noire a l echappement
  evidence:
  - 'Observation: fumee noire a l echappement'
  - Vérification visuelle ou auditive
  id: S4
  label: Fumee noire a l echappement
  risk_level: confort
- description: odeur de carburant non brule
  evidence:
  - 'Observation: odeur de carburant non brule'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de carburant non brule
  risk_level: confort
- description: plus de 150 000 km sans verification
  evidence:
  - 'Observation: plus de 150 000 km sans verification'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 150 000 km sans verification
  risk_level: confort
title: Capteur température d'air admission
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Capteur température d'air admission - Guide Diagnostic Complet

## Fonction et Rôle

Mesurer la temperature de l'air entrant dans le moteur pour optimiser le melange air-carburant

**Actions principales:** mesurer, detecter, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- surconsommation de carburant anormale
- ralenti instable surtout a froid
- sifflement anormal a l admission
- fumee noire a l echappement
- odeur de carburant non brule
- plus de 150 000 km sans verification

## Procédure de Diagnostic

Pour diagnostiquer un problème de capteur température d'air admission:

1. **Inspection visuelle** - Examiner l'état du capteur température d'air admission
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- catalyseur
- corps-papillon
- debitmetre-d-air
- fap
- filtre-a-air

## Critères de Compatibilité

Pour commander le bon capteur température d'air admission, vous devez connaître:

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