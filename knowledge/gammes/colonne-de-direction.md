---
category: direction
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
  - relier
  - transmettre
  - connecter
  must_not_contain_concepts:
  - suspension
  - amortissement
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Relier le volant a la cremailliere - Transmet la rotation du conducteur
    au systeme de direction
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "securite garantie"
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
    question: Comment choisir Colonne de direction compatible avec mon vehicule ?
  - answer: En cas de jeu important du volant vertical ou lateral ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Colonne de direction ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Colonne de direction sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Colonne de direction.
  id: 1211
  intro:
    role: Relier le volant a la cremailliere - Transmet la rotation du conducteur
      au systeme de direction
    syncParts:
    - relier
    - transmettre
    - connecter
    title: A quoi sert Colonne de direction ?
  pgId: '1211'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/colonne-de-direction.md
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
    title: Pourquoi remplacer Colonne de direction a temps ?
  symptoms:
  - jeu important du volant vertical ou lateral
  - craquements ou bruits secs en tournant le volant
  - volant qui ne revient pas seul apres un virage
  - bruits de frottement dans la colonne
  - voyant direction assistee allume
  - sensation de points durs en tournant
  - '**Voyant direction assistee allume**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1211
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: colonne-de-direction
source_type: gamme
symptoms:
- description: jeu important du volant vertical ou lateral
  evidence:
  - 'Observation: jeu important du volant vertical ou lateral'
  - Vérification visuelle ou auditive
  id: S1
  label: Jeu important du volant vertical ou lateral
  risk_level: confort
- description: craquements ou bruits secs en tournant le volant
  evidence:
  - 'Observation: craquements ou bruits secs en tournant le volant'
  - Vérification visuelle ou auditive
  id: S2
  label: Craquements ou bruits secs en tournant le volant
  risk_level: confort
- description: volant qui ne revient pas seul apres un virage
  evidence:
  - 'Observation: volant qui ne revient pas seul apres un virage'
  - Vérification visuelle ou auditive
  id: S3
  label: Volant qui ne revient pas seul apres un virage
  risk_level: confort
- description: bruits de frottement dans la colonne
  evidence:
  - 'Observation: bruits de frottement dans la colonne'
  - Vérification visuelle ou auditive
  id: S4
  label: Bruits de frottement dans la colonne
  risk_level: confort
- description: voyant direction assistee allume
  evidence:
  - 'Observation: voyant direction assistee allume'
  - Vérification visuelle ou auditive
  id: S5
  label: Voyant direction assistee allume
  risk_level: securite
- description: sensation de points durs en tournant
  evidence:
  - 'Observation: sensation de points durs en tournant'
  - Vérification visuelle ou auditive
  id: S6
  label: Sensation de points durs en tournant
  risk_level: confort
title: Colonne de direction
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Colonne de direction - Guide Diagnostic Complet

## Fonction et Rôle

Relier le volant a la cremailliere - Transmet la rotation du conducteur au systeme de direction

**Actions principales:** relier, transmettre, connecter, vehiculer la rotation

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Voyant direction assistee allume**
  voyant direction assistee allume

### 🟢 Autres Symptômes

- jeu important du volant vertical ou lateral
- craquements ou bruits secs en tournant le volant
- volant qui ne revient pas seul apres un virage
- bruits de frottement dans la colonne
- sensation de points durs en tournant

## Procédure de Diagnostic

Pour diagnostiquer un problème de colonne de direction:

1. **Inspection visuelle** - Examiner l'état du colonne de direction
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- cremailliere-de-direction
- pompe-de-direction-assistee
- rotule-de-direction

## Critères de Compatibilité

Pour commander le bon colonne de direction, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "securite garantie"