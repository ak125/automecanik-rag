---
category: freinage
diagnostic_tree:
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
  - moduler
  - réguler
  - distribuer
  must_not_contain_concepts:
  - injection
  - climatisation
  - embrayage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Module hydraulique de freinage avec ABS/ESP
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
    question: Comment choisir Agregat de freinage compatible avec mon vehicule ?
  - answer: En cas de voyant abs allume en permanence au tableau de bord ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Agregat de freinage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Agregat de freinage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Agregat de freinage.
  id: 415
  intro:
    role: Module hydraulique de freinage avec ABS/ESP
    syncParts:
    - moduler
    - réguler
    - distribuer
    title: A quoi sert Agregat de freinage ?
  pgId: '415'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/agregat-de-freinage.md
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
    title: Pourquoi remplacer Agregat de freinage a temps ?
  symptoms:
  - voyant abs allume en permanence au tableau de bord
  - abs qui ne se declenche plus au freinage d urgence
  - bruit de pompe abs anormal ou continu
  - codes defaut abs stockes p ou c
  - pedale de frein qui pulse sans raison
  - esp ou controle de stabilite desactive
  - '**Voyant abs allume en permanence au tableau de bord**'
  - '**Abs qui ne se declenche plus au freinage d urgence**'
  - '**Bruit de pompe abs anormal ou continu**'
  - '**Codes defaut abs stockes p ou c**'
  - '**Pedale de frein qui pulse sans raison**'
  - '**Esp ou controle de stabilite desactive**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 415
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: agregat-de-freinage
source_type: gamme
symptoms:
- description: voyant abs allume en permanence au tableau de bord
  evidence:
  - 'Observation: voyant abs allume en permanence au tableau de bord'
  - Vérification visuelle ou auditive
  id: S1
  label: Voyant abs allume en permanence au tableau de bord
  risk_level: securite
- description: abs qui ne se declenche plus au freinage d urgence
  evidence:
  - 'Observation: abs qui ne se declenche plus au freinage d urgence'
  - Vérification visuelle ou auditive
  id: S2
  label: Abs qui ne se declenche plus au freinage d urgence
  risk_level: securite
- description: bruit de pompe abs anormal ou continu
  evidence:
  - 'Observation: bruit de pompe abs anormal ou continu'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruit de pompe abs anormal ou continu
  risk_level: securite
- description: codes defaut abs stockes p ou c
  evidence:
  - 'Observation: codes defaut abs stockes p ou c'
  - Vérification visuelle ou auditive
  id: S4
  label: Codes defaut abs stockes p ou c
  risk_level: securite
- description: pedale de frein qui pulse sans raison
  evidence:
  - 'Observation: pedale de frein qui pulse sans raison'
  - Vérification visuelle ou auditive
  id: S5
  label: Pedale de frein qui pulse sans raison
  risk_level: securite
- description: esp ou controle de stabilite desactive
  evidence:
  - 'Observation: esp ou controle de stabilite desactive'
  - Vérification visuelle ou auditive
  id: S6
  label: Esp ou controle de stabilite desactive
  risk_level: securite
title: Agregat de freinage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Agregat de freinage - Guide Diagnostic Complet

## Fonction et Rôle

Module hydraulique de freinage avec ABS/ESP

**Actions principales:** moduler, réguler, distribuer

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant abs allume en permanence au tableau de bord**
  voyant abs allume en permanence au tableau de bord
- **Abs qui ne se declenche plus au freinage d urgence**
  abs qui ne se declenche plus au freinage d urgence
- **Bruit de pompe abs anormal ou continu**
  bruit de pompe abs anormal ou continu
- **Codes defaut abs stockes p ou c**
  codes defaut abs stockes p ou c
- **Pedale de frein qui pulse sans raison**
  pedale de frein qui pulse sans raison
- **Esp ou controle de stabilite desactive**
  esp ou controle de stabilite desactive

## Procédure de Diagnostic

Pour diagnostiquer un problème de agregat de freinage:

1. **Inspection visuelle** - Examiner l'état du agregat de freinage
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- agregat-de-freinage
- capteur-abs
- cylindre-de-roue
- disque-de-frein
- etrier-de-frein
- flexible-de-frein
- interrupteur-des-feux-de-freins
- kit-de-freins-arriere

## Critères de Compatibilité

Pour commander le bon agregat de freinage, vous devez connaître:

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