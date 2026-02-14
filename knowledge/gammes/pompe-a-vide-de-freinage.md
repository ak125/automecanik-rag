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
  - assister le freinage
  - reduire l'effort
  - fournir une depression
  must_not_contain_concepts:
  - friction
  - hydraulique directe
  - ABS
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Assister l'effort du conducteur sur la pedale de frein
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "freinage direct"
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
    question: Comment choisir Pompe à vide de freinage compatible avec mon vehicule
      ?
  - answer: En cas de pedale de frein tres dure ou de degradation mesurable, il faut
      controler rapidement avant panne secondaire.
    question: Quand remplacer Pompe à vide de freinage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Pompe à vide de freinage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Pompe à vide de freinage.
  id: 387
  intro:
    role: Assister l'effort du conducteur sur la pedale de frein
    syncParts:
    - assister le freinage
    - reduire l'effort
    - fournir une depression
    title: A quoi sert Pompe à vide de freinage ?
  pgId: '387'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/pompe-a-vide-de-freinage.md
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
    title: Pourquoi remplacer Pompe à vide de freinage a temps ?
  symptoms:
  - pedale de frein tres dure
  - assistance au freinage defaillante
  - sifflement au niveau du moteur
  - voyant defaut frein allume
  - pedale dure surtout freinage depression
  - '**Pedale de frein tres dure**'
  - '**Assistance au freinage defaillante**'
  - '**Voyant defaut frein allume**'
  - '**Pedale dure surtout freinage depression**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 387
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: pompe-a-vide-de-freinage
source_type: gamme
symptoms:
- description: pedale de frein tres dure
  evidence:
  - 'Observation: pedale de frein tres dure'
  - Vérification visuelle ou auditive
  id: S1
  label: Pedale de frein tres dure
  risk_level: securite
- description: assistance au freinage defaillante
  evidence:
  - 'Observation: assistance au freinage defaillante'
  - Vérification visuelle ou auditive
  id: S2
  label: Assistance au freinage defaillante
  risk_level: securite
- description: sifflement au niveau du moteur
  evidence:
  - 'Observation: sifflement au niveau du moteur'
  - Vérification visuelle ou auditive
  id: S3
  label: Sifflement au niveau du moteur
  risk_level: confort
- description: voyant defaut frein allume
  evidence:
  - 'Observation: voyant defaut frein allume'
  - Vérification visuelle ou auditive
  id: S4
  label: Voyant defaut frein allume
  risk_level: securite
- description: pedale dure surtout freinage depression
  evidence:
  - 'Observation: pedale dure surtout freinage depression'
  - Vérification visuelle ou auditive
  id: S5
  label: Pedale dure surtout freinage depression
  risk_level: securite
title: Pompe à vide de freinage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Pompe à vide de freinage - Guide Diagnostic Complet

## Fonction et Rôle

Assister l'effort du conducteur sur la pedale de frein

**Actions principales:** assister le freinage, reduire l'effort, fournir une depression, creer le vide, alimenter le servofrein

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Pedale de frein tres dure**
  pedale de frein tres dure
- **Assistance au freinage defaillante**
  assistance au freinage defaillante
- **Voyant defaut frein allume**
  voyant defaut frein allume
- **Pedale dure surtout freinage depression**
  pedale dure surtout freinage depression

### 🟢 Autres Symptômes

- sifflement au niveau du moteur

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à vide de freinage:

1. **Inspection visuelle** - Examiner l'état du pompe à vide de freinage
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- maitre-cylindre-de-frein
- servo-frein

## Critères de Compatibilité

Pour commander le bon pompe à vide de freinage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage direct"