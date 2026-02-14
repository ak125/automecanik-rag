---
category: distribution
diagnostic_tree:
- if: vehicule_immobilise_ou_symptome_critique
  then: verification_urgente_piece_et_alimentation
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - entrainer
  - synchroniser
  - transmettre
  must_not_contain_concepts:
  - vilebrequin
  - accessoire
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Entrainer l'arbre a cames en synchronisation avec le vilebrequin
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare le moteur"
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
    question: Comment choisir Poulie d'arbre à came compatible avec mon vehicule ?
  - answer: En cas de bruit de claquement au niveau de la culasse ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Poulie d'arbre à came ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Poulie d'arbre à came sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Poulie d'arbre
    à came.
  id: 1067
  intro:
    role: Entrainer l'arbre a cames en synchronisation avec le vilebrequin
    syncParts:
    - entrainer
    - synchroniser
    - transmettre
    title: A quoi sert Poulie d'arbre à came ?
  pgId: '1067'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/poulie-d-arbre-a-came.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le poulie d''arbre à came peut être hors service et nécessiter
      un remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le poulie d''arbre à came peut être hors service
      et nécessiter un remplacement'
    title: Pourquoi remplacer Poulie d'arbre à came a temps ?
  symptoms:
  - bruit de claquement au niveau de la culasse
  - perte de puissance progressive
  - moteur qui cale au ralenti
  - fumee anormale a l echappement
  - voyant moteur allume codes calage
  - distribution a remplacer selon carnet d entretien
  - '**Moteur qui cale au ralenti**'
  - '**Voyant moteur allume codes calage**'
  - '**Bruit de claquement au niveau de la culasse**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1067
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: poulie-d-arbre-a-came
source_type: gamme
symptoms:
- description: bruit de claquement au niveau de la culasse
  evidence:
  - 'Observation: bruit de claquement au niveau de la culasse'
  - Vérification visuelle ou auditive
  id: S1
  label: Bruit de claquement au niveau de la culasse
  risk_level: degats_volant_moteur
- description: perte de puissance progressive
  evidence:
  - 'Observation: perte de puissance progressive'
  - Vérification visuelle ou auditive
  id: S2
  label: Perte de puissance progressive
  risk_level: confort
- description: moteur qui cale au ralenti
  evidence:
  - 'Observation: moteur qui cale au ralenti'
  - Vérification visuelle ou auditive
  id: S3
  label: Moteur qui cale au ralenti
  risk_level: immobilisation
- description: fumee anormale a l echappement
  evidence:
  - 'Observation: fumee anormale a l echappement'
  - Vérification visuelle ou auditive
  id: S4
  label: Fumee anormale a l echappement
  risk_level: confort
- description: voyant moteur allume codes calage
  evidence:
  - 'Observation: voyant moteur allume codes calage'
  - Vérification visuelle ou auditive
  id: S5
  label: Voyant moteur allume codes calage
  risk_level: immobilisation
- description: distribution a remplacer selon carnet d entretien
  evidence:
  - 'Observation: distribution a remplacer selon carnet d entretien'
  - Vérification visuelle ou auditive
  id: S6
  label: Distribution a remplacer selon carnet d entretien
  risk_level: confort
title: Poulie d'arbre à came
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Poulie d'arbre à came - Guide Diagnostic Complet

## Fonction et Rôle

Entrainer l'arbre a cames en synchronisation avec le vilebrequin

**Actions principales:** entrainer, synchroniser, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Moteur qui cale au ralenti**
  moteur qui cale au ralenti
- **Voyant moteur allume codes calage**
  voyant moteur allume codes calage

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement au niveau de la culasse**
  bruit de claquement au niveau de la culasse

### 🟢 Autres Symptômes

- perte de puissance progressive
- fumee anormale a l echappement
- distribution a remplacer selon carnet d entretien

## Procédure de Diagnostic

Pour diagnostiquer un problème de poulie d'arbre à came:

1. **Inspection visuelle** - Examiner l'état du poulie d'arbre à came
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le poulie d'arbre à came peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- arbre-a-came
- capteur-impulsion
- chaine-de-distribution
- courroie-de-distribution
- kit-de-chaine-de-distribution
- kit-de-distribution

## Critères de Compatibilité

Pour commander le bon poulie d'arbre à came, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"