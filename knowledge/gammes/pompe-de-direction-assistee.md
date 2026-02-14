---
category: direction
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
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
  - assister
  - fournir la pression
  - alimenter
  must_not_contain_concepts:
  - suspension
  - amortisseur
  - electrique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Fournir la pression hydraulique pour assister l'effort de braquage
    - Reduit l'effort au volant
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
    question: Comment choisir Pompe de direction assistée compatible avec mon vehicule
      ?
  - answer: En cas de bruit grognement gemissement tournant volant ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Pompe de direction assistée ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Pompe de direction assistée sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Pompe de direction
    assistée.
  id: 12
  intro:
    role: Fournir la pression hydraulique pour assister l'effort de braquage - Reduit
      l'effort au volant
    syncParts:
    - assister
    - fournir la pression
    - alimenter
    title: A quoi sert Pompe de direction assistée ?
  pgId: '12'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/pompe-de-direction-assistee.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Pompe de direction assistée a temps ?
  symptoms:
  - bruit grognement gemissement tournant volant
  - direction dure en man uvre a basse vitesse
  - sifflement aigu au demarrage qui s attenue
  - mousse ou bulles dans le bocal de liquide
  - fuite de liquide au niveau de la pompe
  - niveau de liquide qui baisse regulierement
  - '**Direction dure en man uvre a basse vitesse**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 12
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: pompe-de-direction-assistee
source_type: gamme
symptoms:
- description: bruit grognement gemissement tournant volant
  evidence:
  - 'Observation: bruit grognement gemissement tournant volant'
  - Vérification visuelle ou auditive
  id: S1
  label: Bruit grognement gemissement tournant volant
  risk_level: confort
- description: direction dure en man uvre a basse vitesse
  evidence:
  - 'Observation: direction dure en man uvre a basse vitesse'
  - Vérification visuelle ou auditive
  id: S2
  label: Direction dure en man uvre a basse vitesse
  risk_level: securite
- description: sifflement aigu au demarrage qui s attenue
  evidence:
  - 'Observation: sifflement aigu au demarrage qui s attenue'
  - Vérification visuelle ou auditive
  id: S3
  label: Sifflement aigu au demarrage qui s attenue
  risk_level: confort
- description: mousse ou bulles dans le bocal de liquide
  evidence:
  - 'Observation: mousse ou bulles dans le bocal de liquide'
  - Vérification visuelle ou auditive
  id: S4
  label: Mousse ou bulles dans le bocal de liquide
  risk_level: confort
- description: fuite de liquide au niveau de la pompe
  evidence:
  - 'Observation: fuite de liquide au niveau de la pompe'
  - Vérification visuelle ou auditive
  id: S5
  label: Fuite de liquide au niveau de la pompe
  risk_level: confort
- description: niveau de liquide qui baisse regulierement
  evidence:
  - 'Observation: niveau de liquide qui baisse regulierement'
  - Vérification visuelle ou auditive
  id: S6
  label: Niveau de liquide qui baisse regulierement
  risk_level: confort
title: Pompe de direction assistée
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Pompe de direction assistée - Guide Diagnostic Complet

## Fonction et Rôle

Fournir la pression hydraulique pour assister l'effort de braquage - Reduit l'effort au volant

**Actions principales:** assister, fournir la pression, alimenter, reduire l'effort

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Direction dure en man uvre a basse vitesse**
  direction dure en man uvre a basse vitesse

### 🟢 Autres Symptômes

- bruit grognement gemissement tournant volant
- sifflement aigu au demarrage qui s attenue
- mousse ou bulles dans le bocal de liquide
- fuite de liquide au niveau de la pompe
- niveau de liquide qui baisse regulierement

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe de direction assistée:

1. **Inspection visuelle** - Examiner l'état du pompe de direction assistée
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- colonne-de-direction
- courroie-d-accessoire
- cremailliere-de-direction
- poulie-vilebrequin
- rotule-de-direction
- rotule-de-suspension

## Critères de Compatibilité

Pour commander le bon pompe de direction assistée, vous devez connaître:

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