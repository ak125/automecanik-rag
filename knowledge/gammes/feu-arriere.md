---
category: eclairage
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
  - signaler
  - indiquer
  - eclairer
  must_not_contain_concepts:
  - injection
  - freinage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Signale la présence et les actions du véhicule
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "sécurité maximale"
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
    question: Comment choisir Feu arrière compatible avec mon vehicule ?
  - answer: En cas de arriere allume plus cote stop ou de degradation mesurable, il
      faut controler rapidement avant panne secondaire.
    question: Quand remplacer Feu arrière ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Feu arrière sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Feu arrière.
  id: 290
  intro:
    role: Signale la présence et les actions du véhicule
    syncParts:
    - signaler
    - indiquer
    - eclairer
    title: A quoi sert Feu arrière ?
  pgId: '290'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/feu-arriere.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Feu arrière a temps ?
  symptoms:
  - arriere allume plus cote stop
  - buee visible interieur bloc optique
  - ampoule qui grille frequemment probleme de masse
  - controle technique refuse pour feux defaillants
  - plus de 10 ans sans verification des connecteurs
  - bruit crissement electrique niveau arriere
  - feux inefficaces car tres faibles a l allumage
  - odeur plastique surchauffe niveau feux
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 290
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: feu-arriere
source_type: gamme
symptoms:
- description: arriere allume plus cote stop
  evidence:
  - 'Observation: arriere allume plus cote stop'
  - Vérification visuelle ou auditive
  id: S1
  label: Arriere allume plus cote stop
  risk_level: confort
- description: buee visible interieur bloc optique
  evidence:
  - 'Observation: buee visible interieur bloc optique'
  - Vérification visuelle ou auditive
  id: S2
  label: Buee visible interieur bloc optique
  risk_level: confort
- description: ampoule qui grille frequemment probleme de masse
  evidence:
  - 'Observation: ampoule qui grille frequemment probleme de masse'
  - Vérification visuelle ou auditive
  id: S3
  label: Ampoule qui grille frequemment probleme de masse
  risk_level: confort
- description: controle technique refuse pour feux defaillants
  evidence:
  - 'Observation: controle technique refuse pour feux defaillants'
  - Vérification visuelle ou auditive
  id: S4
  label: Controle technique refuse pour feux defaillants
  risk_level: confort
- description: plus de 10 ans sans verification des connecteurs
  evidence:
  - 'Observation: plus de 10 ans sans verification des connecteurs'
  - Vérification visuelle ou auditive
  id: S5
  label: Plus de 10 ans sans verification des connecteurs
  risk_level: confort
- description: bruit crissement electrique niveau arriere
  evidence:
  - 'Observation: bruit crissement electrique niveau arriere'
  - Vérification visuelle ou auditive
  id: S6
  label: Bruit crissement electrique niveau arriere
  risk_level: confort
- description: feux inefficaces car tres faibles a l allumage
  evidence:
  - 'Observation: feux inefficaces car tres faibles a l allumage'
  - Vérification visuelle ou auditive
  id: S7
  label: Feux inefficaces car tres faibles a l allumage
  risk_level: confort
- description: odeur plastique surchauffe niveau feux
  evidence:
  - 'Observation: odeur plastique surchauffe niveau feux'
  - Vérification visuelle ou auditive
  id: S8
  label: Odeur plastique surchauffe niveau feux
  risk_level: confort
title: Feu arrière
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Feu arrière - Guide Diagnostic Complet

## Fonction et Rôle

Signale la présence et les actions du véhicule

**Actions principales:** signaler, indiquer, eclairer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- arriere allume plus cote stop
- buee visible interieur bloc optique
- ampoule qui grille frequemment probleme de masse
- controle technique refuse pour feux defaillants
- plus de 10 ans sans verification des connecteurs
- bruit crissement electrique niveau arriere

## Procédure de Diagnostic

Pour diagnostiquer un problème de feu arrière:

1. **Inspection visuelle** - Examiner l'état du feu arrière
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-arriere
- commande-d-eclairage
- contacteur-de-feu-de-recul
- feu-avant
- feu-clignotant
- interrupteur-des-feux-de-freins

## Critères de Compatibilité

Pour commander le bon feu arrière, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "sécurité maximale"