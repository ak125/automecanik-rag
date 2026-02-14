---
category: refroidissement
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - dissiper
  - echanger
  - refroidir
  must_not_contain_concepts:
  - chauffage
  - habitacle
  - huile
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Dissiper la chaleur du liquide de refroidissement vers l'air exterieur
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
    question: Comment choisir Radiateur de refroidissement compatible avec mon vehicule
      ?
  - answer: En cas de flaque de liquide colore sous l avant ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Radiateur de refroidissement ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Radiateur de refroidissement sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Radiateur de refroidissement.
  id: 470
  intro:
    role: Dissiper la chaleur du liquide de refroidissement vers l'air exterieur
    syncParts:
    - dissiper
    - echanger
    - refroidir
    title: A quoi sert Radiateur de refroidissement ?
  pgId: '470'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/radiateur-de-refroidissement.md
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
    title: Pourquoi remplacer Radiateur de refroidissement a temps ?
  symptoms:
  - flaque de liquide colore sous l avant
  - traces de corrosion sur les tubes du radiateur
  - sifflement d air ou de vapeur a l avant
  - surchauffe au ralenti ou en embouteillage
  - odeur de liquide de refroidissement chaud
  - radiateur visiblement deforme ou perce
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 470
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: radiateur-de-refroidissement
source_type: gamme
symptoms:
- description: flaque de liquide colore sous l avant
  evidence:
  - 'Observation: flaque de liquide colore sous l avant'
  - Vérification visuelle ou auditive
  id: S1
  label: Flaque de liquide colore sous l avant
  risk_level: confort
- description: traces de corrosion sur les tubes du radiateur
  evidence:
  - 'Observation: traces de corrosion sur les tubes du radiateur'
  - Vérification visuelle ou auditive
  id: S2
  label: Traces de corrosion sur les tubes du radiateur
  risk_level: confort
- description: sifflement d air ou de vapeur a l avant
  evidence:
  - 'Observation: sifflement d air ou de vapeur a l avant'
  - Vérification visuelle ou auditive
  id: S3
  label: Sifflement d air ou de vapeur a l avant
  risk_level: confort
- description: surchauffe au ralenti ou en embouteillage
  evidence:
  - 'Observation: surchauffe au ralenti ou en embouteillage'
  - Vérification visuelle ou auditive
  id: S4
  label: Surchauffe au ralenti ou en embouteillage
  risk_level: confort
- description: odeur de liquide de refroidissement chaud
  evidence:
  - 'Observation: odeur de liquide de refroidissement chaud'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de liquide de refroidissement chaud
  risk_level: confort
- description: radiateur visiblement deforme ou perce
  evidence:
  - 'Observation: radiateur visiblement deforme ou perce'
  - Vérification visuelle ou auditive
  id: S6
  label: Radiateur visiblement deforme ou perce
  risk_level: confort
title: Radiateur de refroidissement
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Radiateur de refroidissement - Guide Diagnostic Complet

## Fonction et Rôle

Dissiper la chaleur du liquide de refroidissement vers l'air exterieur

**Actions principales:** dissiper, echanger, refroidir, evacuer la chaleur

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- flaque de liquide colore sous l avant
- traces de corrosion sur les tubes du radiateur
- sifflement d air ou de vapeur a l avant
- surchauffe au ralenti ou en embouteillage
- odeur de liquide de refroidissement chaud
- radiateur visiblement deforme ou perce

## Procédure de Diagnostic

Pour diagnostiquer un problème de radiateur de refroidissement:

1. **Inspection visuelle** - Examiner l'état du radiateur de refroidissement
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bouchon-de-radiateur
- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-chauffage
- sonde-de-refroidissement
- thermostat
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon radiateur de refroidissement, vous devez connaître:

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