---
category: allumage
diagnostic_tree:
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
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
  - produire une etincelle
  - enflammer
  - allumer le melange
  must_not_contain_concepts:
  - diesel
  - prechauffage
  - incandescence
  - chambre de combustion diesel
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Produire l'etincelle qui enflamme le melange air-essence - Fonctionne
    en continu moteur tournant
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de puissance"
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
    question: Comment choisir Bougie d'allumage compatible avec mon vehicule ?
  - answer: En cas de demarrage difficile ou laborieux ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Bougie d'allumage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Bougie d'allumage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Bougie d'allumage.
  id: 686
  intro:
    role: Produire l'etincelle qui enflamme le melange air-essence - Fonctionne en
      continu moteur tournant
    syncParts:
    - produire une etincelle
    - enflammer
    - allumer le melange
    title: A quoi sert Bougie d'allumage ?
  pgId: '686'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/bougie-d-allumage.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure normale** - Après un certain kilométrage, le remplacement
      préventif est recommandé'
    title: Pourquoi remplacer Bougie d'allumage a temps ?
  symptoms:
  - demarrage difficile ou laborieux
  - rates moteur a froid ou a l acceleration
  - consommation de carburant excessive
  - voyant moteur allume code rate d allumage
  - odeur essence echappement combustion incomplete
  - plus de 40 000 km sans remplacement standard
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 686
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: bougie-d-allumage
source_type: gamme
symptoms:
- description: demarrage difficile ou laborieux
  evidence:
  - 'Observation: demarrage difficile ou laborieux'
  - Vérification visuelle ou auditive
  id: S1
  label: Demarrage difficile ou laborieux
  risk_level: confort
- description: rates moteur a froid ou a l acceleration
  evidence:
  - 'Observation: rates moteur a froid ou a l acceleration'
  - Vérification visuelle ou auditive
  id: S2
  label: Rates moteur a froid ou a l acceleration
  risk_level: confort
- description: consommation de carburant excessive
  evidence:
  - 'Observation: consommation de carburant excessive'
  - Vérification visuelle ou auditive
  id: S3
  label: Consommation de carburant excessive
  risk_level: confort
- description: voyant moteur allume code rate d allumage
  evidence:
  - 'Observation: voyant moteur allume code rate d allumage'
  - Vérification visuelle ou auditive
  id: S4
  label: Voyant moteur allume code rate d allumage
  risk_level: confort
- description: odeur essence echappement combustion incomplete
  evidence:
  - 'Observation: odeur essence echappement combustion incomplete'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur essence echappement combustion incomplete
  risk_level: confort
- description: plus de 40 000 km sans remplacement standard
  evidence:
  - 'Observation: plus de 40 000 km sans remplacement standard'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 40 000 km sans remplacement standard
  risk_level: confort
title: Bougie d'allumage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Bougie d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Produire l'etincelle qui enflamme le melange air-essence - Fonctionne en continu moteur tournant

**Actions principales:** produire une etincelle, enflammer, allumer le melange, declencher la combustion, generer l'arc electrique

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- demarrage difficile ou laborieux
- rates moteur a froid ou a l acceleration
- consommation de carburant excessive
- voyant moteur allume code rate d allumage
- odeur essence echappement combustion incomplete
- plus de 40 000 km sans remplacement standard

## Procédure de Diagnostic

Pour diagnostiquer un problème de bougie d'allumage:

1. **Inspection visuelle** - Examiner l'état du bougie d'allumage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- bobine-d-allumage
- faisceau-d-allumage
- filtre-a-air
- filtre-a-carburant
- filtre-a-huile
- sonde-lambda

## Critères de Compatibilité

Pour commander le bon bougie d'allumage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"