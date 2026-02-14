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
  - detendre
  - abaisser la pression
  must_not_contain_concepts:
  - injection
  - freinage
  - allumage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Detendre le fluide frigorigene avant l'evaporateur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "refroidit instantanement"
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
    question: Comment choisir Gicleur détendeur compatible avec mon vehicule ?
  - answer: En cas de clim qui refroidit mal ou de degradation mesurable, il faut
      controler rapidement avant panne secondaire.
    question: Quand remplacer Gicleur détendeur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Gicleur détendeur sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de climatisation pour confirmer Gicleur détendeur.
  id: 2408
  intro:
    role: Detendre le fluide frigorigene avant l'evaporateur
    syncParts:
    - detendre
    - abaisser la pression
    title: A quoi sert Gicleur détendeur ?
  pgId: '2408'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/gicleur-detendeur.md
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
    title: Pourquoi remplacer Gicleur détendeur a temps ?
  symptoms:
  - clim qui refroidit mal
  - givre visible sur les conduites
  - clim qui fonctionne par a-coups
  - compresseur qui s emballe
  - bruits de glouglou dans le circuit
  - clim qui marche puis s arrete
  - pressions instables au diagnostic
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 2408
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: gicleur-detendeur
source_type: gamme
symptoms:
- description: clim qui refroidit mal
  evidence:
  - 'Observation: clim qui refroidit mal'
  - Vérification visuelle ou auditive
  id: S1
  label: Clim qui refroidit mal
  risk_level: confort
- description: givre visible sur les conduites
  evidence:
  - 'Observation: givre visible sur les conduites'
  - Vérification visuelle ou auditive
  id: S2
  label: Givre visible sur les conduites
  risk_level: confort
- description: clim qui fonctionne par a-coups
  evidence:
  - 'Observation: clim qui fonctionne par a-coups'
  - Vérification visuelle ou auditive
  id: S3
  label: Clim qui fonctionne par a-coups
  risk_level: confort
- description: compresseur qui s emballe
  evidence:
  - 'Observation: compresseur qui s emballe'
  - Vérification visuelle ou auditive
  id: S4
  label: Compresseur qui s emballe
  risk_level: confort
- description: bruits de glouglou dans le circuit
  evidence:
  - 'Observation: bruits de glouglou dans le circuit'
  - Vérification visuelle ou auditive
  id: S5
  label: Bruits de glouglou dans le circuit
  risk_level: confort
- description: clim qui marche puis s arrete
  evidence:
  - 'Observation: clim qui marche puis s arrete'
  - Vérification visuelle ou auditive
  id: S6
  label: Clim qui marche puis s arrete
  risk_level: confort
- description: pressions instables au diagnostic
  evidence:
  - 'Observation: pressions instables au diagnostic'
  - Vérification visuelle ou auditive
  id: S7
  label: Pressions instables au diagnostic
  risk_level: confort
title: Gicleur détendeur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
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