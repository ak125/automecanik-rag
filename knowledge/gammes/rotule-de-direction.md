---
category: direction
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
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
  - orienter
  - transmettre le mouvement
  - articuler
  must_not_contain_concepts:
  - suspension
  - bras
  - triangle
  - charge
  - poids
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Articuler la barre de direction et la fusee - Permet le braquage.
    NE SUPPORTE PAS LA CHARGE!
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
    question: Comment choisir Rotule de direction compatible avec mon vehicule ?
  - answer: En cas de jeu perceptible dans le volant ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Rotule de direction ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Rotule de direction sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Rotule de direction.
  id: 2066
  intro:
    role: Articuler la barre de direction et la fusee - Permet le braquage. NE SUPPORTE
      PAS LA CHARGE!
    syncParts:
    - orienter
    - transmettre le mouvement
    - articuler
    title: A quoi sert Rotule de direction ?
  pgId: '2066'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/rotule-de-direction.md
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
    title: Pourquoi remplacer Rotule de direction a temps ?
  symptoms:
  - jeu perceptible dans le volant
  - claquements en tournant a basse vitesse
  - direction imprecise ou floue
  - usure asymetrique des pneus avant
  - soufflet de rotule dechire ou graisse visible
  - controle technique refuse pour jeu aux trains
  - '**Claquements en tournant a basse vitesse**'
  - '**Direction imprecise ou floue**'
  - '**Usure asymetrique des pneus avant**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 2066
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: rotule-de-direction
source_type: gamme
symptoms:
- description: jeu perceptible dans le volant
  evidence:
  - 'Observation: jeu perceptible dans le volant'
  - Vérification visuelle ou auditive
  id: S1
  label: Jeu perceptible dans le volant
  risk_level: confort
- description: claquements en tournant a basse vitesse
  evidence:
  - 'Observation: claquements en tournant a basse vitesse'
  - Vérification visuelle ou auditive
  id: S2
  label: Claquements en tournant a basse vitesse
  risk_level: degats_volant_moteur
- description: direction imprecise ou floue
  evidence:
  - 'Observation: direction imprecise ou floue'
  - Vérification visuelle ou auditive
  id: S3
  label: Direction imprecise ou floue
  risk_level: securite
- description: usure asymetrique des pneus avant
  evidence:
  - 'Observation: usure asymetrique des pneus avant'
  - Vérification visuelle ou auditive
  id: S4
  label: Usure asymetrique des pneus avant
  risk_level: securite
- description: soufflet de rotule dechire ou graisse visible
  evidence:
  - 'Observation: soufflet de rotule dechire ou graisse visible'
  - Vérification visuelle ou auditive
  id: S5
  label: Soufflet de rotule dechire ou graisse visible
  risk_level: confort
- description: controle technique refuse pour jeu aux trains
  evidence:
  - 'Observation: controle technique refuse pour jeu aux trains'
  - Vérification visuelle ou auditive
  id: S6
  label: Controle technique refuse pour jeu aux trains
  risk_level: confort
title: Rotule de direction
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Rotule de direction - Guide Diagnostic Complet

## Fonction et Rôle

Articuler la barre de direction et la fusee - Permet le braquage. NE SUPPORTE PAS LA CHARGE!

**Actions principales:** orienter, transmettre le mouvement, articuler, permettre le braquage, guider

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquements en tournant a basse vitesse**
  claquements en tournant a basse vitesse

### 🟡 Symptômes de Sécurité

- **Direction imprecise ou floue**
  direction imprecise ou floue
- **Usure asymetrique des pneus avant**
  usure asymetrique des pneus avant

### 🟢 Autres Symptômes

- jeu perceptible dans le volant
- soufflet de rotule dechire ou graisse visible
- controle technique refuse pour jeu aux trains

## Procédure de Diagnostic

Pour diagnostiquer un problème de rotule de direction:

1. **Inspection visuelle** - Examiner l'état du rotule de direction
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- amortisseur
- barre-de-direction
- bras-de-suspension
- cremailliere-de-direction
- pompe-de-direction-assistee
- rotule-de-suspension
- soufflet-de-direction

## Critères de Compatibilité

Pour commander le bon rotule de direction, vous devez connaître:

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