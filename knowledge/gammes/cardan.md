---
category: transmission
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: vibrations_anormales
  then: verifier_equilibrage_et_fixations
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
  - entrainer
  must_not_contain_concepts:
  - injection
  - freinage
  - climatisation
  - allumage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transmet le couple moteur aux roues tout en permettant les mouvements
    de suspension
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
    question: Comment choisir Cardan compatible avec mon vehicule ?
  - answer: En cas de claquement braquant accelerant marche arriere ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Cardan ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Cardan sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de transmission pour confirmer Cardan.
  id: 13
  intro:
    role: Transmet le couple moteur aux roues tout en permettant les mouvements de
      suspension
    syncParts:
    - transmettre
    - entrainer
    title: A quoi sert Cardan ?
  pgId: '13'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/cardan.md
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
    title: Pourquoi remplacer Cardan a temps ?
  symptoms:
  - claquement braquant accelerant marche arriere
  - vibrations ressenties vitesse constante
  - graisse noire visible jante passage
  - soufflet de cardan dechire ou fendu visible
  - bruit roulement change selon angle
  - plus de 150 000 km sans verification des soufflets
  - '**Claquement braquant accelerant marche arriere**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 13
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: cardan
source_type: gamme
symptoms:
- description: claquement braquant accelerant marche arriere
  evidence:
  - 'Observation: claquement braquant accelerant marche arriere'
  - Vérification visuelle ou auditive
  id: S1
  label: Claquement braquant accelerant marche arriere
  risk_level: degats_volant_moteur
- description: vibrations ressenties vitesse constante
  evidence:
  - 'Observation: vibrations ressenties vitesse constante'
  - Vérification visuelle ou auditive
  id: S2
  label: Vibrations ressenties vitesse constante
  risk_level: confort
- description: graisse noire visible jante passage
  evidence:
  - 'Observation: graisse noire visible jante passage'
  - Vérification visuelle ou auditive
  id: S3
  label: Graisse noire visible jante passage
  risk_level: confort
- description: soufflet de cardan dechire ou fendu visible
  evidence:
  - 'Observation: soufflet de cardan dechire ou fendu visible'
  - Vérification visuelle ou auditive
  id: S4
  label: Soufflet de cardan dechire ou fendu visible
  risk_level: confort
- description: bruit roulement change selon angle
  evidence:
  - 'Observation: bruit roulement change selon angle'
  - Vérification visuelle ou auditive
  id: S5
  label: Bruit roulement change selon angle
  risk_level: confort
- description: plus de 150 000 km sans verification des soufflets
  evidence:
  - 'Observation: plus de 150 000 km sans verification des soufflets'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 150 000 km sans verification des soufflets
  risk_level: confort
title: Cardan
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Cardan - Guide Diagnostic Complet

## Fonction et Rôle

Transmet le couple moteur aux roues tout en permettant les mouvements de suspension

**Actions principales:** transmettre, entrainer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement braquant accelerant marche arriere**
  claquement braquant accelerant marche arriere

### 🟢 Autres Symptômes

- vibrations ressenties vitesse constante
- graisse noire visible jante passage
- soufflet de cardan dechire ou fendu visible
- bruit roulement change selon angle
- plus de 150 000 km sans verification des soufflets

## Procédure de Diagnostic

Pour diagnostiquer un problème de cardan:

1. **Inspection visuelle** - Examiner l'état du cardan
2. **Test dynamique** - Vérifier les bruits en roulant
3. **Contrôle du jeu** - Examiner l'usure des articulations
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- bague-d-etancheite-cardan
- soufflet-de-cardan

## Critères de Compatibilité

Pour commander le bon cardan, vous devez connaître:

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