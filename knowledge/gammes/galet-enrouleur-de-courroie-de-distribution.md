---
category: distribution
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
  - guider
  - enrouler
  - positionner
  must_not_contain_concepts:
  - freinage
  - climatisation
  - turbo
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Guider la courroie de distribution dans son parcours
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "synchronisation parfaite"
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
    question: Comment choisir Galet enrouleur de courroie de distribution compatible
      avec mon vehicule ?
  - answer: En cas de bruit de roulement au ralenti ou de degradation mesurable, il
      faut controler rapidement avant panne secondaire.
    question: Quand remplacer Galet enrouleur de courroie de distribution ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Galet enrouleur de courroie de distribution sans verification
      atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Galet enrouleur
    de courroie de distribution.
  id: 313
  intro:
    role: Guider la courroie de distribution dans son parcours
    syncParts:
    - guider
    - enrouler
    - positionner
    title: A quoi sert Galet enrouleur de courroie de distribution ?
  pgId: '313'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/galet-enrouleur-de-courroie-de-distribution.md
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
    title: Pourquoi remplacer Galet enrouleur de courroie de distribution a temps
      ?
  symptoms:
  - bruit de roulement au ralenti
  - sifflement cote distribution
  - traces d usure anormale sur la courroie
  - galet qui tourne difficilement a la main
  - jeu radial ou axial dans le galet
  - bruit metallique leger
  - courroie qui se deporte sur le cote
  - '**Bruit metallique leger**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 313
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: galet-enrouleur-de-courroie-de-distribution
source_type: gamme
symptoms:
- description: bruit de roulement au ralenti
  evidence:
  - 'Observation: bruit de roulement au ralenti'
  - Vérification visuelle ou auditive
  id: S1
  label: Bruit de roulement au ralenti
  risk_level: confort
- description: sifflement cote distribution
  evidence:
  - 'Observation: sifflement cote distribution'
  - Vérification visuelle ou auditive
  id: S2
  label: Sifflement cote distribution
  risk_level: confort
- description: traces d usure anormale sur la courroie
  evidence:
  - 'Observation: traces d usure anormale sur la courroie'
  - Vérification visuelle ou auditive
  id: S3
  label: Traces d usure anormale sur la courroie
  risk_level: confort
- description: galet qui tourne difficilement a la main
  evidence:
  - 'Observation: galet qui tourne difficilement a la main'
  - Vérification visuelle ou auditive
  id: S4
  label: Galet qui tourne difficilement a la main
  risk_level: confort
- description: jeu radial ou axial dans le galet
  evidence:
  - 'Observation: jeu radial ou axial dans le galet'
  - Vérification visuelle ou auditive
  id: S5
  label: Jeu radial ou axial dans le galet
  risk_level: confort
- description: bruit metallique leger
  evidence:
  - 'Observation: bruit metallique leger'
  - Vérification visuelle ou auditive
  id: S6
  label: Bruit metallique leger
  risk_level: degats_volant_moteur
- description: courroie qui se deporte sur le cote
  evidence:
  - 'Observation: courroie qui se deporte sur le cote'
  - Vérification visuelle ou auditive
  id: S7
  label: Courroie qui se deporte sur le cote
  risk_level: confort
title: Galet enrouleur de courroie de distribution
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Galet enrouleur de courroie de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Guider la courroie de distribution dans son parcours

**Actions principales:** guider, enrouler, positionner

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit metallique leger**
  bruit metallique leger

### 🟢 Autres Symptômes

- bruit de roulement au ralenti
- sifflement cote distribution
- traces d usure anormale sur la courroie
- galet qui tourne difficilement a la main
- jeu radial ou axial dans le galet
- courroie qui se deporte sur le cote

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet enrouleur de courroie de distribution:

1. **Inspection visuelle** - Examiner l'état du galet enrouleur de courroie de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-de-distribution

## Critères de Compatibilité

Pour commander le bon galet enrouleur de courroie de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "synchronisation parfaite"