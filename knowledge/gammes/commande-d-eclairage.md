---
category: eclairage
diagnostic_tree:
- if: vehicule_immobilise_ou_symptome_critique
  then: verification_urgente_piece_et_alimentation
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
  - commander
  - activer
  - regler
  must_not_contain_concepts:
  - injection
  - freinage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Commande les différents feux du véhicule
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "meilleur éclairage"
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
    question: Comment choisir Commande d'éclairage compatible avec mon vehicule ?
  - answer: En cas de feux croisement route allument plus ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Commande d'éclairage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Commande d'éclairage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Commande d'éclairage.
  id: 809
  intro:
    role: Commande les différents feux du véhicule
    syncParts:
    - commander
    - activer
    - regler
    title: A quoi sert Commande d'éclairage ?
  pgId: '809'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/commande-d-eclairage.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le commande d''éclairage peut être hors service et nécessiter
      un remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le commande d''éclairage peut être hors service et
      nécessiter un remplacement'
    title: Pourquoi remplacer Commande d'éclairage a temps ?
  symptoms:
  - feux croisement route allument plus
  - commodo bloque ou difficile a tourner
  - fonctions aleatoires s allument puis s eteignent
  - clignotants fonctionnent plus depuis commodo
  - bruit de craquement en actionnant l interrupteur
  - fusibles ok mais feux inoperants
  - '**Commodo bloque ou difficile a tourner**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 809
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: commande-d-eclairage
source_type: gamme
symptoms:
- description: feux croisement route allument plus
  evidence:
  - 'Observation: feux croisement route allument plus'
  - Vérification visuelle ou auditive
  id: S1
  label: Feux croisement route allument plus
  risk_level: confort
- description: commodo bloque ou difficile a tourner
  evidence:
  - 'Observation: commodo bloque ou difficile a tourner'
  - Vérification visuelle ou auditive
  id: S2
  label: Commodo bloque ou difficile a tourner
  risk_level: immobilisation
- description: fonctions aleatoires s allument puis s eteignent
  evidence:
  - 'Observation: fonctions aleatoires s allument puis s eteignent'
  - Vérification visuelle ou auditive
  id: S3
  label: Fonctions aleatoires s allument puis s eteignent
  risk_level: confort
- description: clignotants fonctionnent plus depuis commodo
  evidence:
  - 'Observation: clignotants fonctionnent plus depuis commodo'
  - Vérification visuelle ou auditive
  id: S4
  label: Clignotants fonctionnent plus depuis commodo
  risk_level: confort
- description: bruit de craquement en actionnant l interrupteur
  evidence:
  - 'Observation: bruit de craquement en actionnant l interrupteur'
  - Vérification visuelle ou auditive
  id: S5
  label: Bruit de craquement en actionnant l interrupteur
  risk_level: confort
- description: fusibles ok mais feux inoperants
  evidence:
  - 'Observation: fusibles ok mais feux inoperants'
  - Vérification visuelle ou auditive
  id: S6
  label: Fusibles ok mais feux inoperants
  risk_level: confort
title: Commande d'éclairage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Commande d'éclairage - Guide Diagnostic Complet

## Fonction et Rôle

Commande les différents feux du véhicule

**Actions principales:** commander, activer, regler

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Commodo bloque ou difficile a tourner**
  commodo bloque ou difficile a tourner

### 🟢 Autres Symptômes

- feux croisement route allument plus
- fonctions aleatoires s allument puis s eteignent
- clignotants fonctionnent plus depuis commodo
- bruit de craquement en actionnant l interrupteur
- fusibles ok mais feux inoperants

## Procédure de Diagnostic

Pour diagnostiquer un problème de commande d'éclairage:

1. **Inspection visuelle** - Examiner l'état du commande d'éclairage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le commande d'éclairage peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-d-essuie-glace
- feu-arriere
- feu-avant
- feu-clignotant

## Critères de Compatibilité

Pour commander le bon commande d'éclairage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur éclairage"