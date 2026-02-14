---
category: allumage
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
  - transformer la tension
  - amplifier
  - generer la haute tension
  must_not_contain_concepts:
  - diesel
  - prechauffage
  - incandescence
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transformer la basse tension batterie en haute tension (15-40kV) pour
    creer l'etincelle aux bougies
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
    question: Comment choisir Bobine d'allumage compatible avec mon vehicule ?
  - answer: En cas de rate moteur localise sur un cylindre precis ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Bobine d'allumage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Bobine d'allumage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Bobine d'allumage.
  id: 689
  intro:
    role: Transformer la basse tension batterie en haute tension (15-40kV) pour creer
      l'etincelle aux bougies
    syncParts:
    - transformer la tension
    - amplifier
    - generer la haute tension
    title: A quoi sert Bobine d'allumage ?
  pgId: '689'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/bobine-d-allumage.md
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
    title: Pourquoi remplacer Bobine d'allumage a temps ?
  symptoms:
  - rate moteur localise sur un cylindre precis
  - voyant moteur allume code p030x
  - perte de puissance brutale ou progressive
  - surconsommation de carburant
  - odeur d essence non brulee a l echappement
  - demarrage difficile par temps humide
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 689
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: bobine-d-allumage
source_type: gamme
symptoms:
- description: rate moteur localise sur un cylindre precis
  evidence:
  - 'Observation: rate moteur localise sur un cylindre precis'
  - Vérification visuelle ou auditive
  id: S1
  label: Rate moteur localise sur un cylindre precis
  risk_level: confort
- description: voyant moteur allume code p030x
  evidence:
  - 'Observation: voyant moteur allume code p030x'
  - Vérification visuelle ou auditive
  id: S2
  label: Voyant moteur allume code p030x
  risk_level: confort
- description: perte de puissance brutale ou progressive
  evidence:
  - 'Observation: perte de puissance brutale ou progressive'
  - Vérification visuelle ou auditive
  id: S3
  label: Perte de puissance brutale ou progressive
  risk_level: confort
- description: surconsommation de carburant
  evidence:
  - 'Observation: surconsommation de carburant'
  - Vérification visuelle ou auditive
  id: S4
  label: Surconsommation de carburant
  risk_level: confort
- description: odeur d essence non brulee a l echappement
  evidence:
  - 'Observation: odeur d essence non brulee a l echappement'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur d essence non brulee a l echappement
  risk_level: confort
- description: demarrage difficile par temps humide
  evidence:
  - 'Observation: demarrage difficile par temps humide'
  - Vérification visuelle ou auditive
  id: S6
  label: Demarrage difficile par temps humide
  risk_level: confort
title: Bobine d'allumage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Bobine d'allumage - Guide Diagnostic Complet

## Fonction et Rôle

Transformer la basse tension batterie en haute tension (15-40kV) pour creer l'etincelle aux bougies

**Actions principales:** transformer la tension, amplifier, generer la haute tension, alimenter les bougies, creer l'arc

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- rate moteur localise sur un cylindre precis
- voyant moteur allume code p030x
- perte de puissance brutale ou progressive
- surconsommation de carburant
- odeur d essence non brulee a l echappement
- demarrage difficile par temps humide

## Procédure de Diagnostic

Pour diagnostiquer un problème de bobine d'allumage:

1. **Inspection visuelle** - Examiner l'état du bobine d'allumage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- bougie-d-allumage
- faisceau-d-allumage

## Critères de Compatibilité

Pour commander le bon bobine d'allumage, vous devez connaître:

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