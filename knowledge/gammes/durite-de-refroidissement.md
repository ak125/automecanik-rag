---
category: refroidissement
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
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
  - acheminer
  - conduire
  - relier
  must_not_contain_concepts:
  - huile
  - carburant
  - frein
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Acheminer le liquide de refroidissement entre les elements du circuit
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "evite la casse moteur"
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
    question: Comment choisir Durite de refroidissement compatible avec mon vehicule
      ?
  - answer: En cas de traces de liquide colore sous le vehicule ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Durite de refroidissement ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Durite de refroidissement sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Durite de refroidissement.
  id: 475
  intro:
    role: Acheminer le liquide de refroidissement entre les elements du circuit
    syncParts:
    - acheminer
    - conduire
    - relier
    title: A quoi sert Durite de refroidissement ?
  pgId: '475'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/durite-de-refroidissement.md
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
    title: Pourquoi remplacer Durite de refroidissement a temps ?
  symptoms:
  - traces de liquide colore sous le vehicule
  - durite visiblement gonflee ou craquelee
  - sifflement ou gargouillement dans le circuit
  - niveau de liquide qui baisse regulierement
  - odeur sucree de liquide de refroidissement
  - plus de 100 000 km ou 8 ans sans remplacement
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 475
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: durite-de-refroidissement
source_type: gamme
symptoms:
- description: traces de liquide colore sous le vehicule
  evidence:
  - 'Observation: traces de liquide colore sous le vehicule'
  - Vérification visuelle ou auditive
  id: S1
  label: Traces de liquide colore sous le vehicule
  risk_level: confort
- description: durite visiblement gonflee ou craquelee
  evidence:
  - 'Observation: durite visiblement gonflee ou craquelee'
  - Vérification visuelle ou auditive
  id: S2
  label: Durite visiblement gonflee ou craquelee
  risk_level: confort
- description: sifflement ou gargouillement dans le circuit
  evidence:
  - 'Observation: sifflement ou gargouillement dans le circuit'
  - Vérification visuelle ou auditive
  id: S3
  label: Sifflement ou gargouillement dans le circuit
  risk_level: confort
- description: niveau de liquide qui baisse regulierement
  evidence:
  - 'Observation: niveau de liquide qui baisse regulierement'
  - Vérification visuelle ou auditive
  id: S4
  label: Niveau de liquide qui baisse regulierement
  risk_level: confort
- description: odeur sucree de liquide de refroidissement
  evidence:
  - 'Observation: odeur sucree de liquide de refroidissement'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur sucree de liquide de refroidissement
  risk_level: confort
- description: plus de 100 000 km ou 8 ans sans remplacement
  evidence:
  - 'Observation: plus de 100 000 km ou 8 ans sans remplacement'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 100 000 km ou 8 ans sans remplacement
  risk_level: confort
title: Durite de refroidissement
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Durite de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Acheminer le liquide de refroidissement entre les elements du circuit

**Actions principales:** acheminer, conduire, relier, transporter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- traces de liquide colore sous le vehicule
- durite visiblement gonflee ou craquelee
- sifflement ou gargouillement dans le circuit
- niveau de liquide qui baisse regulierement
- odeur sucree de liquide de refroidissement
- plus de 100 000 km ou 8 ans sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de durite de refroidissement:

1. **Inspection visuelle** - Examiner l'état du durite de refroidissement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- thermostat
- vase-d-expansion
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon durite de refroidissement, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "evite la casse moteur"