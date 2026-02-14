---
category: distribution
diagnostic_tree:
- if: vehicule_immobilise_ou_symptome_critique
  then: verification_urgente_piece_et_alimentation
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - synchroniser
  - entrainer
  - transmettre
  must_not_contain_concepts:
  - courroie
  - caoutchouc
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Synchroniser la rotation de l'arbre a cames avec le vilebrequin de
    maniere durable
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
    question: Comment choisir Chaîne de distribution compatible avec mon vehicule
      ?
  - answer: En cas de bruit de cliquetis metallique au demarrage a froid ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Chaîne de distribution ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Chaîne de distribution sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Chaîne de distribution.
  id: 1123
  intro:
    role: Synchroniser la rotation de l'arbre a cames avec le vilebrequin de maniere
      durable
    syncParts:
    - synchroniser
    - entrainer
    - transmettre
    title: A quoi sert Chaîne de distribution ?
  pgId: '1123'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/chaine-de-distribution.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Pièce HS** - Le chaîne de distribution peut être hors service et nécessiter
      un remplacement'
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Pièce HS** - Le chaîne de distribution peut être hors service
      et nécessiter un remplacement'
    title: Pourquoi remplacer Chaîne de distribution a temps ?
  symptoms:
  - bruit de cliquetis metallique au demarrage a froid
  - claquement qui disparait apres quelques secondes
  - voyant moteur allume codes calage
  - moteur qui manque de puissance
  - bruit de ferraille permanent cote distribution
  - difficultes de demarrage
  - consommation huile anormale tendeur hydraulique
  - '**Voyant moteur allume codes calage**'
  - '**Claquement qui disparait apres quelques secondes**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1123
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: chaine-de-distribution
source_type: gamme
symptoms:
- description: bruit de cliquetis metallique au demarrage a froid
  evidence:
  - 'Observation: bruit de cliquetis metallique au demarrage a froid'
  - Vérification visuelle ou auditive
  id: S1
  label: Bruit de cliquetis metallique au demarrage a froid
  risk_level: confort
- description: claquement qui disparait apres quelques secondes
  evidence:
  - 'Observation: claquement qui disparait apres quelques secondes'
  - Vérification visuelle ou auditive
  id: S2
  label: Claquement qui disparait apres quelques secondes
  risk_level: degats_volant_moteur
- description: voyant moteur allume codes calage
  evidence:
  - 'Observation: voyant moteur allume codes calage'
  - Vérification visuelle ou auditive
  id: S3
  label: Voyant moteur allume codes calage
  risk_level: immobilisation
- description: moteur qui manque de puissance
  evidence:
  - 'Observation: moteur qui manque de puissance'
  - Vérification visuelle ou auditive
  id: S4
  label: Moteur qui manque de puissance
  risk_level: confort
- description: bruit de ferraille permanent cote distribution
  evidence:
  - 'Observation: bruit de ferraille permanent cote distribution'
  - Vérification visuelle ou auditive
  id: S5
  label: Bruit de ferraille permanent cote distribution
  risk_level: confort
- description: difficultes de demarrage
  evidence:
  - 'Observation: difficultes de demarrage'
  - Vérification visuelle ou auditive
  id: S6
  label: Difficultes de demarrage
  risk_level: confort
- description: consommation huile anormale tendeur hydraulique
  evidence:
  - 'Observation: consommation huile anormale tendeur hydraulique'
  - Vérification visuelle ou auditive
  id: S7
  label: Consommation huile anormale tendeur hydraulique
  risk_level: confort
title: Chaîne de distribution
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Chaîne de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Synchroniser la rotation de l'arbre a cames avec le vilebrequin de maniere durable

**Actions principales:** synchroniser, entrainer, transmettre

## Symptômes de Défaillance

### 🔴 Symptômes Critiques (Immobilisation)

- **Voyant moteur allume codes calage**
  voyant moteur allume codes calage

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement qui disparait apres quelques secondes**
  claquement qui disparait apres quelques secondes

### 🟢 Autres Symptômes

- bruit de cliquetis metallique au demarrage a froid
- moteur qui manque de puissance
- bruit de ferraille permanent cote distribution
- difficultes de demarrage
- consommation huile anormale tendeur hydraulique

## Procédure de Diagnostic

Pour diagnostiquer un problème de chaîne de distribution:

1. **Inspection visuelle** - Examiner l'état du chaîne de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Pièce HS** - Le chaîne de distribution peut être hors service et nécessiter un remplacement
- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- kit-de-chaine-de-distribution
- pompe-a-eau
- pompe-a-injection
- poulie-d-arbre-a-came

## Critères de Compatibilité

Pour commander le bon chaîne de distribution, vous devez connaître:

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