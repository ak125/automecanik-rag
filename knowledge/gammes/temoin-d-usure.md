---
category: freinage
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
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
  - signaler
  - alerter
  - indiquer
  must_not_contain_concepts:
  - injection
  - climatisation
  - embrayage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Signale l'usure des plaquettes de frein
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "améliore le freinage"
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
    question: Comment choisir Témoin d'usure compatible avec mon vehicule ?
  - answer: En cas de voyant usure frein allume au tableau de bord ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Témoin d'usure ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Témoin d'usure sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Témoin d'usure.
  id: 407
  intro:
    role: Témoin d'usure intervient directement sur frein du vehicule. Un choix conforme
      protege la freinage et limite les pannes secondaires.
    syncParts:
    - signaler
    - alerter
    - indiquer
    title: A quoi sert Témoin d'usure ?
  pgId: '407'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/temoin-d-usure.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Témoin d'usure a temps ?
  symptoms:
  - voyant usure frein allume au tableau de bord
  - sifflement metallique freinage temoin acoustique
  - voyant allume en permanence meme plaquettes neuves
  - connecteur du temoin debranche ou coupe
  - fil du temoin fondu par frottement sur disque
  - freinage degrade malgre absence de voyant
  - odeur de brule si frottement du fil
  - plus de 30 000 km avec temoin non verifie
  - '**Voyant usure frein allume au tableau de bord**'
  - '**Sifflement metallique freinage temoin acoustique**'
  - '**Freinage degrade malgre absence de voyant**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 407
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: temoin-d-usure
source_type: gamme
symptoms:
- description: voyant usure frein allume au tableau de bord
  evidence:
  - 'Observation: voyant usure frein allume au tableau de bord'
  - Vérification visuelle ou auditive
  id: S1
  label: Voyant usure frein allume au tableau de bord
  risk_level: securite
- description: sifflement metallique freinage temoin acoustique
  evidence:
  - 'Observation: sifflement metallique freinage temoin acoustique'
  - Vérification visuelle ou auditive
  id: S2
  label: Sifflement metallique freinage temoin acoustique
  risk_level: securite
- description: voyant allume en permanence meme plaquettes neuves
  evidence:
  - 'Observation: voyant allume en permanence meme plaquettes neuves'
  - Vérification visuelle ou auditive
  id: S3
  label: Voyant allume en permanence meme plaquettes neuves
  risk_level: confort
- description: connecteur du temoin debranche ou coupe
  evidence:
  - 'Observation: connecteur du temoin debranche ou coupe'
  - Vérification visuelle ou auditive
  id: S4
  label: Connecteur du temoin debranche ou coupe
  risk_level: confort
- description: fil du temoin fondu par frottement sur disque
  evidence:
  - 'Observation: fil du temoin fondu par frottement sur disque'
  - Vérification visuelle ou auditive
  id: S5
  label: Fil du temoin fondu par frottement sur disque
  risk_level: confort
- description: freinage degrade malgre absence de voyant
  evidence:
  - 'Observation: freinage degrade malgre absence de voyant'
  - Vérification visuelle ou auditive
  id: S6
  label: Freinage degrade malgre absence de voyant
  risk_level: securite
- description: odeur de brule si frottement du fil
  evidence:
  - 'Observation: odeur de brule si frottement du fil'
  - Vérification visuelle ou auditive
  id: S7
  label: Odeur de brule si frottement du fil
  risk_level: confort
- description: plus de 30 000 km avec temoin non verifie
  evidence:
  - 'Observation: plus de 30 000 km avec temoin non verifie'
  - Vérification visuelle ou auditive
  id: S8
  label: Plus de 30 000 km avec temoin non verifie
  risk_level: confort
title: Témoin d'usure
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Témoin d'usure - Guide Diagnostic Complet

## Fonction et Rôle

Signale l'usure des plaquettes de frein

**Actions principales:** signaler, alerter, indiquer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant usure frein allume au tableau de bord**
  voyant usure frein allume au tableau de bord
- **Sifflement metallique freinage temoin acoustique**
  sifflement metallique freinage temoin acoustique
- **Freinage degrade malgre absence de voyant**
  freinage degrade malgre absence de voyant

### 🟢 Autres Symptômes

- voyant allume en permanence meme plaquettes neuves
- connecteur du temoin debranche ou coupe
- fil du temoin fondu par frottement sur disque
- odeur de brule si frottement du fil
- plus de 30 000 km avec temoin non verifie

## Procédure de Diagnostic

Pour diagnostiquer un problème de témoin d'usure:

1. **Inspection visuelle** - Examiner l'état du témoin d'usure
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- capteur-abs
- disque-de-frein
- etrier-de-frein
- interrupteur-des-feux-de-freins
- plaquette-de-frein
- servo-frein

## Critères de Compatibilité

Pour commander le bon témoin d'usure, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "améliore le freinage"