---
category: allumage
diagnostic_tree:
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
  - transmettre
  - conduire
  - acheminer
  must_not_contain_concepts:
  - diesel
  - prechauffage
  - incandescence
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transmettre la haute tension de la bobine aux bougies d'allumage sans
    perte
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
    question: Comment choisir Faisceau d'allumage compatible avec mon vehicule ?
  - answer: En cas de rates moteur a l acceleration ou au ralenti ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Faisceau d'allumage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Faisceau d'allumage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Faisceau d'allumage.
  id: 685
  intro:
    role: Transmettre la haute tension de la bobine aux bougies d'allumage sans perte
    syncParts:
    - transmettre
    - conduire
    - acheminer
    title: A quoi sert Faisceau d'allumage ?
  pgId: '685'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/faisceau-d-allumage.md
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
    title: Pourquoi remplacer Faisceau d'allumage a temps ?
  symptoms:
  - rates moteur a l acceleration ou au ralenti
  - demarrage difficile surtout par temps humide
  - consommation de carburant anormalement elevee
  - arc electrique visible sur les cables dans le noir
  - odeur d essence au pot d echappement
  - plus de 80 000 km sans remplacement
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 685
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: faisceau-d-allumage
source_type: gamme
symptoms:
- description: rates moteur a l acceleration ou au ralenti
  evidence:
  - 'Observation: rates moteur a l acceleration ou au ralenti'
  - Vérification visuelle ou auditive
  id: S1
  label: Rates moteur a l acceleration ou au ralenti
  risk_level: confort
- description: demarrage difficile surtout par temps humide
  evidence:
  - 'Observation: demarrage difficile surtout par temps humide'
  - Vérification visuelle ou auditive
  id: S2
  label: Demarrage difficile surtout par temps humide
  risk_level: confort
- description: consommation de carburant anormalement elevee
  evidence:
  - 'Observation: consommation de carburant anormalement elevee'
  - Vérification visuelle ou auditive
  id: S3
  label: Consommation de carburant anormalement elevee
  risk_level: confort
- description: arc electrique visible sur les cables dans le noir
  evidence:
  - 'Observation: arc electrique visible sur les cables dans le noir'
  - Vérification visuelle ou auditive
  id: S4
  label: Arc electrique visible sur les cables dans le noir
  risk_level: confort
- description: odeur d essence au pot d echappement
  evidence:
  - 'Observation: odeur d essence au pot d echappement'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur d essence au pot d echappement
  risk_level: confort
- description: plus de 80 000 km sans remplacement
  evidence:
  - 'Observation: plus de 80 000 km sans remplacement'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 80 000 km sans remplacement
  risk_level: confort
title: Faisceau d'allumage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Faisceau d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre la haute tension de la bobine aux bougies d'allumage sans perte

**Actions principales:** transmettre, conduire, acheminer, vehiculer la haute tension, relier bobine et bougies

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rates moteur a l acceleration ou au ralenti
- demarrage difficile surtout par temps humide
- consommation de carburant anormalement elevee
- arc electrique visible sur les cables dans le noir
- odeur d essence au pot d echappement
- plus de 80 000 km sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de faisceau d'allumage:

1. **Inspection visuelle** - Examiner l'état du faisceau d'allumage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- bobine-d-allumage
- bougie-d-allumage

## Critères de Compatibilité

Pour commander le bon faisceau d'allumage, vous devez connaître:

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