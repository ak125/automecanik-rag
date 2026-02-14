---
category: distribution
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
  - faire circuler
  - pomper
  - alimenter
  must_not_contain_concepts:
  - huile
  - carburant
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Faire circuler le liquide de refroidissement dans le circuit moteur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "evite la casse moteur"
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
    question: Comment choisir Pompe à eau compatible avec mon vehicule ?
  - answer: En cas de fuite de liquide au niveau de la pompe ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Pompe à eau ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Pompe à eau sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Pompe à eau.
  id: 1260
  intro:
    role: Faire circuler le liquide de refroidissement dans le circuit moteur
    syncParts:
    - faire circuler
    - pomper
    - alimenter
    title: A quoi sert Pompe à eau ?
  pgId: '1260'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/pompe-a-eau.md
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
    title: Pourquoi remplacer Pompe à eau a temps ?
  symptoms:
  - fuite de liquide au niveau de la pompe
  - bruit de roulement cote distribution
  - jeu perceptible dans la poulie de pompe
  - surchauffe moteur malgre niveau correct
  - odeur de liquide de refroidissement chaud
  - echeance distribution approche preventif
  - '**Surchauffe moteur malgre niveau correct**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1260
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: pompe-a-eau
source_type: gamme
symptoms:
- description: fuite de liquide au niveau de la pompe
  evidence:
  - 'Observation: fuite de liquide au niveau de la pompe'
  - Vérification visuelle ou auditive
  id: S1
  label: Fuite de liquide au niveau de la pompe
  risk_level: confort
- description: bruit de roulement cote distribution
  evidence:
  - 'Observation: bruit de roulement cote distribution'
  - Vérification visuelle ou auditive
  id: S2
  label: Bruit de roulement cote distribution
  risk_level: confort
- description: jeu perceptible dans la poulie de pompe
  evidence:
  - 'Observation: jeu perceptible dans la poulie de pompe'
  - Vérification visuelle ou auditive
  id: S3
  label: Jeu perceptible dans la poulie de pompe
  risk_level: confort
- description: surchauffe moteur malgre niveau correct
  evidence:
  - 'Observation: surchauffe moteur malgre niveau correct'
  - Vérification visuelle ou auditive
  id: S4
  label: Surchauffe moteur malgre niveau correct
  risk_level: degats_volant_moteur
- description: odeur de liquide de refroidissement chaud
  evidence:
  - 'Observation: odeur de liquide de refroidissement chaud'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de liquide de refroidissement chaud
  risk_level: confort
- description: echeance distribution approche preventif
  evidence:
  - 'Observation: echeance distribution approche preventif'
  - Vérification visuelle ou auditive
  id: S6
  label: Echeance distribution approche preventif
  risk_level: confort
title: Pompe à eau
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Pompe à eau - Guide Diagnostic Complet

## Fonction et Rôle

Faire circuler le liquide de refroidissement dans le circuit moteur

**Actions principales:** faire circuler, pomper, alimenter, assurer la circulation

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Surchauffe moteur malgre niveau correct**
  surchauffe moteur malgre niveau correct

### 🟢 Autres Symptômes

- fuite de liquide au niveau de la pompe
- bruit de roulement cote distribution
- jeu perceptible dans la poulie de pompe
- odeur de liquide de refroidissement chaud
- echeance distribution approche preventif

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à eau:

1. **Inspection visuelle** - Examiner l'état du pompe à eau
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- chaine-de-distribution
- courroie-d-accessoire
- courroie-de-distribution
- durite-de-refroidissement
- kit-de-chaine-de-distribution
- kit-de-distribution
- radiateur-de-refroidissement
- sonde-de-refroidissement

## Critères de Compatibilité

Pour commander le bon pompe à eau, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "evite la casse moteur"