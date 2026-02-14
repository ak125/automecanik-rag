---
category: freinage
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
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
  - pousser les machoires
  - transmettre la pression
  - actionner le freinage tambour
  must_not_contain_concepts:
  - disque
  - etrier
  - plaquette
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transmettre la pression hydraulique aux machoires
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
    question: Comment choisir Cylindre de roue compatible avec mon vehicule ?
  - answer: En cas de traces de liquide sur le dos des machoires ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Cylindre de roue ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Cylindre de roue sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de frein pour confirmer Cylindre de roue.
  id: 277
  intro:
    role: Transmettre la pression hydraulique aux machoires
    syncParts:
    - pousser les machoires
    - transmettre la pression
    - actionner le freinage tambour
    title: A quoi sert Cylindre de roue ?
  pgId: '277'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/cylindre-de-roue.md
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
    title: Pourquoi remplacer Cylindre de roue a temps ?
  symptoms:
  - traces de liquide sur le dos des machoires
  - interieur du tambour mouille ou gras
  - niveau de liquide de frein qui baisse
  - freinage arriere desequilibre
  - machoires usees de facon asymetrique
  - fuite visible au niveau du cylindre
  - bruit de frottement a l arriere
  - odeur de liquide de frein pres des roues arriere
  - plus de 100 000 km sans controle des cylindres
  - '**Niveau de liquide de frein qui baisse**'
  - '**Freinage arriere desequilibre**'
  - '**Odeur de liquide de frein pres des roues arriere**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 277
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: cylindre-de-roue
source_type: gamme
symptoms:
- description: traces de liquide sur le dos des machoires
  evidence:
  - 'Observation: traces de liquide sur le dos des machoires'
  - Vérification visuelle ou auditive
  id: S1
  label: Traces de liquide sur le dos des machoires
  risk_level: confort
- description: interieur du tambour mouille ou gras
  evidence:
  - 'Observation: interieur du tambour mouille ou gras'
  - Vérification visuelle ou auditive
  id: S2
  label: Interieur du tambour mouille ou gras
  risk_level: confort
- description: niveau de liquide de frein qui baisse
  evidence:
  - 'Observation: niveau de liquide de frein qui baisse'
  - Vérification visuelle ou auditive
  id: S3
  label: Niveau de liquide de frein qui baisse
  risk_level: securite
- description: freinage arriere desequilibre
  evidence:
  - 'Observation: freinage arriere desequilibre'
  - Vérification visuelle ou auditive
  id: S4
  label: Freinage arriere desequilibre
  risk_level: securite
- description: machoires usees de facon asymetrique
  evidence:
  - 'Observation: machoires usees de facon asymetrique'
  - Vérification visuelle ou auditive
  id: S5
  label: Machoires usees de facon asymetrique
  risk_level: confort
- description: fuite visible au niveau du cylindre
  evidence:
  - 'Observation: fuite visible au niveau du cylindre'
  - Vérification visuelle ou auditive
  id: S6
  label: Fuite visible au niveau du cylindre
  risk_level: confort
- description: bruit de frottement a l arriere
  evidence:
  - 'Observation: bruit de frottement a l arriere'
  - Vérification visuelle ou auditive
  id: S7
  label: Bruit de frottement a l arriere
  risk_level: confort
- description: odeur de liquide de frein pres des roues arriere
  evidence:
  - 'Observation: odeur de liquide de frein pres des roues arriere'
  - Vérification visuelle ou auditive
  id: S8
  label: Odeur de liquide de frein pres des roues arriere
  risk_level: securite
- description: plus de 100 000 km sans controle des cylindres
  evidence:
  - 'Observation: plus de 100 000 km sans controle des cylindres'
  - Vérification visuelle ou auditive
  id: S9
  label: Plus de 100 000 km sans controle des cylindres
  risk_level: confort
title: Cylindre de roue
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Cylindre de roue - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre la pression hydraulique aux machoires

**Actions principales:** pousser les machoires, transmettre la pression, actionner le freinage tambour, ecarter, commander

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Niveau de liquide de frein qui baisse**
  niveau de liquide de frein qui baisse
- **Freinage arriere desequilibre**
  freinage arriere desequilibre
- **Odeur de liquide de frein pres des roues arriere**
  odeur de liquide de frein pres des roues arriere

### 🟢 Autres Symptômes

- traces de liquide sur le dos des machoires
- interieur du tambour mouille ou gras
- machoires usees de facon asymetrique
- fuite visible au niveau du cylindre
- bruit de frottement a l arriere
- plus de 100 000 km sans controle des cylindres

## Procédure de Diagnostic

Pour diagnostiquer un problème de cylindre de roue:

1. **Inspection visuelle** - Examiner l'état du cylindre de roue
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- cable-de-frein-a-main
- disque-de-frein
- etrier-de-frein
- flexible-de-frein
- kit-de-freins-arriere
- machoires-de-frein
- plaquette-de-frein
- tambour-de-frein

## Critères de Compatibilité

Pour commander le bon cylindre de roue, vous devez connaître:

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