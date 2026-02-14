---
category: distribution
diagnostic_tree:
- if: vehicule_immobilise_ou_symptome_critique
  then: verification_urgente_piece_et_alimentation
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
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
  - entrainer
  - transmettre
  - amortir
  must_not_contain_concepts:
  - freinage
  - climatisation
  - turbo
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transmet le mouvement du vilebrequin aux accessoires
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
    question: Comment choisir Poulie vilebrequin compatible avec mon vehicule ?
  - answer: En cas de vibrations moteur importantes au ralenti ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Poulie vilebrequin ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Poulie vilebrequin sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Poulie vilebrequin.
  id: 3213
  intro:
    role: Transmet le mouvement du vilebrequin aux accessoires
    syncParts:
    - entrainer
    - transmettre
    - amortir
    title: A quoi sert Poulie vilebrequin ?
  pgId: '3213'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/poulie-vilebrequin.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le poulie vilebrequin peut être hors service et nécessiter un
      remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le poulie vilebrequin peut être hors service et nécessiter
      un remplacement'
    title: Pourquoi remplacer Poulie vilebrequin a temps ?
  symptoms:
  - vibrations moteur importantes au ralenti
  - caoutchouc de la poulie fissure ou decolle
  - courroie d accessoire qui deraille
  - bruit sourd au niveau du bas moteur
  - reperes de calage impossibles a aligner
  - voyant moteur codes vibrations vilebrequin
  - '**Reperes de calage impossibles a aligner**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 3213
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: poulie-vilebrequin
source_type: gamme
symptoms:
- description: vibrations moteur importantes au ralenti
  evidence:
  - 'Observation: vibrations moteur importantes au ralenti'
  - Vérification visuelle ou auditive
  id: S1
  label: Vibrations moteur importantes au ralenti
  risk_level: confort
- description: caoutchouc de la poulie fissure ou decolle
  evidence:
  - 'Observation: caoutchouc de la poulie fissure ou decolle'
  - Vérification visuelle ou auditive
  id: S2
  label: Caoutchouc de la poulie fissure ou decolle
  risk_level: confort
- description: courroie d accessoire qui deraille
  evidence:
  - 'Observation: courroie d accessoire qui deraille'
  - Vérification visuelle ou auditive
  id: S3
  label: Courroie d accessoire qui deraille
  risk_level: confort
- description: bruit sourd au niveau du bas moteur
  evidence:
  - 'Observation: bruit sourd au niveau du bas moteur'
  - Vérification visuelle ou auditive
  id: S4
  label: Bruit sourd au niveau du bas moteur
  risk_level: confort
- description: reperes de calage impossibles a aligner
  evidence:
  - 'Observation: reperes de calage impossibles a aligner'
  - Vérification visuelle ou auditive
  id: S5
  label: Reperes de calage impossibles a aligner
  risk_level: immobilisation
- description: voyant moteur codes vibrations vilebrequin
  evidence:
  - 'Observation: voyant moteur codes vibrations vilebrequin'
  - Vérification visuelle ou auditive
  id: S6
  label: Voyant moteur codes vibrations vilebrequin
  risk_level: confort
title: Poulie vilebrequin
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Poulie vilebrequin - Guide Diagnostic Complet

## Fonction et Rôle

Transmet le mouvement du vilebrequin aux accessoires

**Actions principales:** entrainer, transmettre, amortir

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Reperes de calage impossibles a aligner**
  reperes de calage impossibles a aligner

### 🟢 Autres Symptômes

- vibrations moteur importantes au ralenti
- caoutchouc de la poulie fissure ou decolle
- courroie d accessoire qui deraille
- bruit sourd au niveau du bas moteur
- voyant moteur codes vibrations vilebrequin

## Procédure de Diagnostic

Pour diagnostiquer un problème de poulie vilebrequin:

1. **Inspection visuelle** - Examiner l'état du poulie vilebrequin
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le poulie vilebrequin peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- capteur-impulsion
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-de-direction-assistee
- poulie-d-alternateur

## Critères de Compatibilité

Pour commander le bon poulie vilebrequin, vous devez connaître:

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