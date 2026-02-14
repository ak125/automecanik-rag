---
category: accessoires
diagnostic_tree:
- if: vehicule_immobilise_ou_symptome_critique
  then: verification_urgente_piece_et_alimentation
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: vibrations_anormales
  then: verifier_equilibrage_et_fixations
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - reflechir
  - montrer
  - permettre la vision
  must_not_contain_concepts:
  - injection
  - freinage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Permet la vision arrière et latérale
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "meilleure visibilité garantie"
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
    question: Comment choisir Rétroviseur extérieur compatible avec mon vehicule ?
  - answer: En cas de miroir casse fissure ou decolle ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Rétroviseur extérieur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Rétroviseur extérieur sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Rétroviseur extérieur.
  id: 50
  intro:
    role: Rétroviseur extérieur intervient directement sur compatibilite du vehicule.
      Un choix conforme protege la securite et limite les pannes secondaires.
    syncParts:
    - reflechir
    - montrer
    - permettre la vision
    title: A quoi sert Rétroviseur extérieur ?
  pgId: '50'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/retroviseur-exterieur.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le rétroviseur extérieur peut être hors service et nécessiter
      un remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le rétroviseur extérieur peut être hors service et
      nécessiter un remplacement'
    title: Pourquoi remplacer Rétroviseur extérieur a temps ?
  symptoms:
  - miroir casse fissure ou decolle
  - coque de retroviseur cassee choc accrochage
  - reglage electrique inoperant ou lent
  - degivrage du miroir qui ne fonctionne plus
  - retroviseur rabattable bloque ou qui vibre
  - repetiteur de clignotant integre grille
  - miroir fissure ebreche deformant image
  - bruit claquement vibration retroviseur vent
  - odeur plastique brule moteur electrique
  - '**Retroviseur rabattable bloque ou qui vibre**'
  - '**Miroir casse fissure ou decolle**'
  - '**Coque de retroviseur cassee choc accrochage**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 50
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: retroviseur-exterieur
source_type: gamme
symptoms:
- description: miroir casse fissure ou decolle
  evidence:
  - 'Observation: miroir casse fissure ou decolle'
  - Vérification visuelle ou auditive
  id: S1
  label: Miroir casse fissure ou decolle
  risk_level: degats_volant_moteur
- description: coque de retroviseur cassee choc accrochage
  evidence:
  - 'Observation: coque de retroviseur cassee choc accrochage'
  - Vérification visuelle ou auditive
  id: S2
  label: Coque de retroviseur cassee choc accrochage
  risk_level: degats_volant_moteur
- description: reglage electrique inoperant ou lent
  evidence:
  - 'Observation: reglage electrique inoperant ou lent'
  - Vérification visuelle ou auditive
  id: S3
  label: Reglage electrique inoperant ou lent
  risk_level: confort
- description: degivrage du miroir qui ne fonctionne plus
  evidence:
  - 'Observation: degivrage du miroir qui ne fonctionne plus'
  - Vérification visuelle ou auditive
  id: S4
  label: Degivrage du miroir qui ne fonctionne plus
  risk_level: confort
- description: retroviseur rabattable bloque ou qui vibre
  evidence:
  - 'Observation: retroviseur rabattable bloque ou qui vibre'
  - Vérification visuelle ou auditive
  id: S5
  label: Retroviseur rabattable bloque ou qui vibre
  risk_level: immobilisation
- description: repetiteur de clignotant integre grille
  evidence:
  - 'Observation: repetiteur de clignotant integre grille'
  - Vérification visuelle ou auditive
  id: S6
  label: Repetiteur de clignotant integre grille
  risk_level: confort
- description: miroir fissure ebreche deformant image
  evidence:
  - 'Observation: miroir fissure ebreche deformant image'
  - Vérification visuelle ou auditive
  id: S7
  label: Miroir fissure ebreche deformant image
  risk_level: confort
- description: bruit claquement vibration retroviseur vent
  evidence:
  - 'Observation: bruit claquement vibration retroviseur vent'
  - Vérification visuelle ou auditive
  id: S8
  label: Bruit claquement vibration retroviseur vent
  risk_level: degats_volant_moteur
- description: odeur plastique brule moteur electrique
  evidence:
  - 'Observation: odeur plastique brule moteur electrique'
  - Vérification visuelle ou auditive
  id: S9
  label: Odeur plastique brule moteur electrique
  risk_level: confort
title: Rétroviseur extérieur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Rétroviseur extérieur - Guide Diagnostic Complet

## Fonction et Rôle

Permet la vision arrière et latérale

**Actions principales:** reflechir, montrer, permettre la vision

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Retroviseur rabattable bloque ou qui vibre**
  retroviseur rabattable bloque ou qui vibre

### 🟠 Symptômes de Dégâts Potentiels

- **Miroir casse fissure ou decolle**
  miroir casse fissure ou decolle
- **Coque de retroviseur cassee choc accrochage**
  coque de retroviseur cassee choc accrochage
- **Bruit claquement vibration retroviseur vent**
  bruit claquement vibration retroviseur vent

### 🟢 Autres Symptômes

- reglage electrique inoperant ou lent
- degivrage du miroir qui ne fonctionne plus
- repetiteur de clignotant integre grille
- miroir fissure ebreche deformant image
- odeur plastique brule moteur electrique

## Procédure de Diagnostic

Pour diagnostiquer un problème de rétroviseur extérieur:

1. **Inspection visuelle** - Examiner l'état du rétroviseur extérieur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le rétroviseur extérieur peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- bouton-de-retroviseur

## Critères de Compatibilité

Pour commander le bon rétroviseur extérieur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure visibilité garantie"