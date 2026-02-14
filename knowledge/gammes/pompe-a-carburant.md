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
  - alimenter
  - acheminer
  - pomper
  must_not_contain_concepts:
  - haute pression
  - injection
  - injecteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Acheminer le carburant du reservoir vers le systeme d'injection a
    basse pression
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
    question: Comment choisir Pompe à carburant compatible avec mon vehicule ?
  - answer: En cas de moteur qui refuse de demarrer pas d amorcage ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Pompe à carburant ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Pompe à carburant sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Pompe à carburant.
  id: 458
  intro:
    role: Acheminer le carburant du reservoir vers le systeme d'injection a basse
      pression
    syncParts:
    - alimenter
    - acheminer
    - pomper
    title: A quoi sert Pompe à carburant ?
  pgId: '458'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/pompe-a-carburant.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le pompe à carburant peut être hors service et nécessiter un
      remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le pompe à carburant peut être hors service et nécessiter
      un remplacement'
    title: Pourquoi remplacer Pompe à carburant a temps ?
  symptoms:
  - moteur qui refuse de demarrer pas d amorcage
  - calages repetes a chaud ou en cote
  - a-coups a l acceleration
  - bruit de gemissement dans le reservoir
  - perte de puissance en montee
  - plus de 200 000 km ou reservoir souvent vide
  - '**Calages repetes a chaud ou en cote**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 458
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: pompe-a-carburant
source_type: gamme
symptoms:
- description: moteur qui refuse de demarrer pas d amorcage
  evidence:
  - 'Observation: moteur qui refuse de demarrer pas d amorcage'
  - Vérification visuelle ou auditive
  id: S1
  label: Moteur qui refuse de demarrer pas d amorcage
  risk_level: confort
- description: calages repetes a chaud ou en cote
  evidence:
  - 'Observation: calages repetes a chaud ou en cote'
  - Vérification visuelle ou auditive
  id: S2
  label: Calages repetes a chaud ou en cote
  risk_level: immobilisation
- description: a-coups a l acceleration
  evidence:
  - 'Observation: a-coups a l acceleration'
  - Vérification visuelle ou auditive
  id: S3
  label: A-coups a l acceleration
  risk_level: confort
- description: bruit de gemissement dans le reservoir
  evidence:
  - 'Observation: bruit de gemissement dans le reservoir'
  - Vérification visuelle ou auditive
  id: S4
  label: Bruit de gemissement dans le reservoir
  risk_level: confort
- description: perte de puissance en montee
  evidence:
  - 'Observation: perte de puissance en montee'
  - Vérification visuelle ou auditive
  id: S5
  label: Perte de puissance en montee
  risk_level: confort
- description: plus de 200 000 km ou reservoir souvent vide
  evidence:
  - 'Observation: plus de 200 000 km ou reservoir souvent vide'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 200 000 km ou reservoir souvent vide
  risk_level: confort
title: Pompe à carburant
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Pompe à carburant - Guide Diagnostic Complet

## Fonction et Rôle

Acheminer le carburant du reservoir vers le systeme d'injection a basse pression

**Actions principales:** alimenter, acheminer, pomper

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Calages repetes a chaud ou en cote**
  calages repetes a chaud ou en cote

### 🟢 Autres Symptômes

- moteur qui refuse de demarrer pas d amorcage
- a-coups a l acceleration
- bruit de gemissement dans le reservoir
- perte de puissance en montee
- plus de 200 000 km ou reservoir souvent vide

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à carburant:

1. **Inspection visuelle** - Examiner l'état du pompe à carburant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le pompe à carburant peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-pression-de-carburant
- filtre-a-carburant
- injecteur

## Critères de Compatibilité

Pour commander le bon pompe à carburant, vous devez connaître:

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