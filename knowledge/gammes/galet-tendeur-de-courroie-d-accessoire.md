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
  - tendre
  - maintenir
  - guider
  must_not_contain_concepts:
  - freinage
  - climatisation
  - turbo
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Maintient la tension de la courroie d'accessoire
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de durée de vie"
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
    question: Comment choisir Galet tendeur de courroie d'accessoire compatible avec
      mon vehicule ?
  - answer: En cas de sifflement de la courroie ou de degradation mesurable, il faut
      controler rapidement avant panne secondaire.
    question: Quand remplacer Galet tendeur de courroie d'accessoire ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Galet tendeur de courroie d'accessoire sans verification
      atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Galet tendeur
    de courroie d'accessoire.
  id: 310
  intro:
    role: Maintient la tension de la courroie d'accessoire
    syncParts:
    - tendre
    - maintenir
    - guider
    title: A quoi sert Galet tendeur de courroie d'accessoire ?
  pgId: '310'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/galet-tendeur-de-courroie-d-accessoire.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le galet tendeur de courroie d''accessoire peut être hors service
      et nécessiter un remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le galet tendeur de courroie d''accessoire peut être
      hors service et nécessiter un remplacement'
    title: Pourquoi remplacer Galet tendeur de courroie d'accessoire a temps ?
  symptoms:
  - sifflement de la courroie
  - bruit de roulement cote accessoires
  - courroie qui patine temoin batterie
  - galet qui ne bouge plus tendeur bloque
  - vibrations dans le moteur
  - bruit de claquement courroie detendue
  - courroie qui saute de son logement
  - '**Galet qui ne bouge plus tendeur bloque**'
  - '**Bruit de claquement courroie detendue**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 310
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: galet-tendeur-de-courroie-d-accessoire
source_type: gamme
symptoms:
- description: sifflement de la courroie
  evidence:
  - 'Observation: sifflement de la courroie'
  - Vérification visuelle ou auditive
  id: S1
  label: Sifflement de la courroie
  risk_level: confort
- description: bruit de roulement cote accessoires
  evidence:
  - 'Observation: bruit de roulement cote accessoires'
  - Vérification visuelle ou auditive
  id: S2
  label: Bruit de roulement cote accessoires
  risk_level: confort
- description: courroie qui patine temoin batterie
  evidence:
  - 'Observation: courroie qui patine temoin batterie'
  - Vérification visuelle ou auditive
  id: S3
  label: Courroie qui patine temoin batterie
  risk_level: confort
- description: galet qui ne bouge plus tendeur bloque
  evidence:
  - 'Observation: galet qui ne bouge plus tendeur bloque'
  - Vérification visuelle ou auditive
  id: S4
  label: Galet qui ne bouge plus tendeur bloque
  risk_level: immobilisation
- description: vibrations dans le moteur
  evidence:
  - 'Observation: vibrations dans le moteur'
  - Vérification visuelle ou auditive
  id: S5
  label: Vibrations dans le moteur
  risk_level: confort
- description: bruit de claquement courroie detendue
  evidence:
  - 'Observation: bruit de claquement courroie detendue'
  - Vérification visuelle ou auditive
  id: S6
  label: Bruit de claquement courroie detendue
  risk_level: degats_volant_moteur
- description: courroie qui saute de son logement
  evidence:
  - 'Observation: courroie qui saute de son logement'
  - Vérification visuelle ou auditive
  id: S7
  label: Courroie qui saute de son logement
  risk_level: confort
title: Galet tendeur de courroie d'accessoire
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Galet tendeur de courroie d'accessoire - Guide Diagnostic Complet

## Fonction et Rôle

Maintient la tension de la courroie d'accessoire

**Actions principales:** tendre, maintenir, guider

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Galet qui ne bouge plus tendeur bloque**
  galet qui ne bouge plus tendeur bloque

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement courroie detendue**
  bruit de claquement courroie detendue

### 🟢 Autres Symptômes

- sifflement de la courroie
- bruit de roulement cote accessoires
- courroie qui patine temoin batterie
- vibrations dans le moteur
- courroie qui saute de son logement

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet tendeur de courroie d'accessoire:

1. **Inspection visuelle** - Examiner l'état du galet tendeur de courroie d'accessoire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le galet tendeur de courroie d'accessoire peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- compresseur-de-climatisation
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- pompe-de-direction-assistee
- poulie-d-alternateur
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon galet tendeur de courroie d'accessoire, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de durée de vie"