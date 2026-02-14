---
category: alimentation
diagnostic_tree:
- if: vehicule_immobilise_ou_symptome_critique
  then: verification_urgente_piece_et_alimentation
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
  - doser
  - reguler
  - controler
  must_not_contain_concepts:
  - carburant
  - injection
  - injecteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Doser la quantite d'air admise dans le moteur en fonction de la position
    de l'accelerateur
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
    question: Comment choisir Boîtier papillon compatible avec mon vehicule ?
  - answer: En cas de ralenti instable ou irregulier ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Boîtier papillon ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Boîtier papillon sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Boîtier papillon.
  id: 158
  intro:
    role: Doser la quantite d'air admise dans le moteur en fonction de la position
      de l'accelerateur
    syncParts:
    - doser
    - reguler
    - controler
    title: A quoi sert Boîtier papillon ?
  pgId: '158'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/corps-papillon.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le boîtier papillon peut être hors service et nécessiter un
      remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le boîtier papillon peut être hors service et nécessiter
      un remplacement'
    title: Pourquoi remplacer Boîtier papillon a temps ?
  symptoms:
  - ralenti instable ou irregulier
  - accelerations saccadees ou a-coups
  - moteur qui cale au demarrage ou au ralenti
  - sifflement d air au niveau de l admission
  - odeur d essence melange trop riche
  - plus de 100 000 km sans nettoyage
  - '**Moteur qui cale au demarrage ou au ralenti**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 158
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: corps-papillon
source_type: gamme
symptoms:
- description: ralenti instable ou irregulier
  evidence:
  - 'Observation: ralenti instable ou irregulier'
  - Vérification visuelle ou auditive
  id: S1
  label: Ralenti instable ou irregulier
  risk_level: confort
- description: accelerations saccadees ou a-coups
  evidence:
  - 'Observation: accelerations saccadees ou a-coups'
  - Vérification visuelle ou auditive
  id: S2
  label: Accelerations saccadees ou a-coups
  risk_level: confort
- description: moteur qui cale au demarrage ou au ralenti
  evidence:
  - 'Observation: moteur qui cale au demarrage ou au ralenti'
  - Vérification visuelle ou auditive
  id: S3
  label: Moteur qui cale au demarrage ou au ralenti
  risk_level: immobilisation
- description: sifflement d air au niveau de l admission
  evidence:
  - 'Observation: sifflement d air au niveau de l admission'
  - Vérification visuelle ou auditive
  id: S4
  label: Sifflement d air au niveau de l admission
  risk_level: confort
- description: odeur d essence melange trop riche
  evidence:
  - 'Observation: odeur d essence melange trop riche'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur d essence melange trop riche
  risk_level: confort
- description: plus de 100 000 km sans nettoyage
  evidence:
  - 'Observation: plus de 100 000 km sans nettoyage'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 100 000 km sans nettoyage
  risk_level: confort
title: Boîtier papillon
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Boîtier papillon - Guide Diagnostic Complet

## Fonction et Rôle

Doser la quantite d'air admise dans le moteur en fonction de la position de l'accelerateur

**Actions principales:** doser, reguler, controler

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au demarrage ou au ralenti**
  moteur qui cale au demarrage ou au ralenti

### 🟢 Autres Symptômes

- ralenti instable ou irregulier
- accelerations saccadees ou a-coups
- sifflement d air au niveau de l admission
- odeur d essence melange trop riche
- plus de 100 000 km sans nettoyage

## Procédure de Diagnostic

Pour diagnostiquer un problème de boîtier papillon:

1. **Inspection visuelle** - Examiner l'état du boîtier papillon
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le boîtier papillon peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-position-papillon
- capteur-de-cognement
- capteur-temperature-d-air-admission
- corps-papillon
- injecteur
- valve-de-reglage-du-ralenti

## Critères de Compatibilité

Pour commander le bon boîtier papillon, vous devez connaître:

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