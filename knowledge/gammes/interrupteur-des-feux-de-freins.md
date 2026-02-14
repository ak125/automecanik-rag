---
category: capteurs
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
  - detecter
  - signaler
  - activer
  must_not_contain_concepts:
  - reparation
  - regeneration
  - nettoyage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Detecte l'appui sur la pedale de frein pour activer les feux stop
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "meilleur freinage"
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
    question: Comment choisir Interrupteur des feux de freins compatible avec mon
      vehicule ?
  - answer: En cas de feux stop qui restent allumes moteur eteint ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Interrupteur des feux de freins ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Interrupteur des feux de freins sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Interrupteur des
    feux de freins.
  id: 806
  intro:
    role: Detecte l'appui sur la pedale de frein pour activer les feux stop
    syncParts:
    - detecter
    - signaler
    - activer
    title: A quoi sert Interrupteur des feux de freins ?
  pgId: '806'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/interrupteur-des-feux-de-freins.md
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
    title: Pourquoi remplacer Interrupteur des feux de freins a temps ?
  symptoms:
  - feux stop qui restent allumes moteur eteint
  - feux stop qui ne s allument plus du tout
  - regulateur de vitesse qui ne fonctionne plus
  - message d erreur systeme esp au tableau de bord
  - batterie decharge feux stop restes
  - clic audible absent quand on appuie sur la pedale
  - odeur de plastique brule court-circuit
  - plus de 150 000 km sans verification
  - '**Message d erreur systeme esp au tableau de bord**'
  - '**Clic audible absent quand on appuie sur la pedale**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 806
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: interrupteur-des-feux-de-freins
source_type: gamme
symptoms:
- description: feux stop qui restent allumes moteur eteint
  evidence:
  - 'Observation: feux stop qui restent allumes moteur eteint'
  - Vérification visuelle ou auditive
  id: S1
  label: Feux stop qui restent allumes moteur eteint
  risk_level: confort
- description: feux stop qui ne s allument plus du tout
  evidence:
  - 'Observation: feux stop qui ne s allument plus du tout'
  - Vérification visuelle ou auditive
  id: S2
  label: Feux stop qui ne s allument plus du tout
  risk_level: confort
- description: regulateur de vitesse qui ne fonctionne plus
  evidence:
  - 'Observation: regulateur de vitesse qui ne fonctionne plus'
  - Vérification visuelle ou auditive
  id: S3
  label: Regulateur de vitesse qui ne fonctionne plus
  risk_level: confort
- description: message d erreur systeme esp au tableau de bord
  evidence:
  - 'Observation: message d erreur systeme esp au tableau de bord'
  - Vérification visuelle ou auditive
  id: S4
  label: Message d erreur systeme esp au tableau de bord
  risk_level: securite
- description: batterie decharge feux stop restes
  evidence:
  - 'Observation: batterie decharge feux stop restes'
  - Vérification visuelle ou auditive
  id: S5
  label: Batterie decharge feux stop restes
  risk_level: confort
- description: clic audible absent quand on appuie sur la pedale
  evidence:
  - 'Observation: clic audible absent quand on appuie sur la pedale'
  - Vérification visuelle ou auditive
  id: S6
  label: Clic audible absent quand on appuie sur la pedale
  risk_level: securite
- description: odeur de plastique brule court-circuit
  evidence:
  - 'Observation: odeur de plastique brule court-circuit'
  - Vérification visuelle ou auditive
  id: S7
  label: Odeur de plastique brule court-circuit
  risk_level: confort
- description: plus de 150 000 km sans verification
  evidence:
  - 'Observation: plus de 150 000 km sans verification'
  - Vérification visuelle ou auditive
  id: S8
  label: Plus de 150 000 km sans verification
  risk_level: confort
title: Interrupteur des feux de freins
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Interrupteur des feux de freins - Guide Diagnostic Complet

## Fonction et Rôle

Detecte l'appui sur la pedale de frein pour activer les feux stop

**Actions principales:** detecter, signaler, activer, commander

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Message d erreur systeme esp au tableau de bord**
  message d erreur systeme esp au tableau de bord
- **Clic audible absent quand on appuie sur la pedale**
  clic audible absent quand on appuie sur la pedale

### 🟢 Autres Symptômes

- feux stop qui restent allumes moteur eteint
- feux stop qui ne s allument plus du tout
- regulateur de vitesse qui ne fonctionne plus
- batterie decharge feux stop restes
- odeur de plastique brule court-circuit
- plus de 150 000 km sans verification

## Procédure de Diagnostic

Pour diagnostiquer un problème de interrupteur des feux de freins:

1. **Inspection visuelle** - Examiner l'état du interrupteur des feux de freins
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- feu-arriere
- kit-de-freins-arriere
- machoires-de-frein

## Critères de Compatibilité

Pour commander le bon interrupteur des feux de freins, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleur freinage"