---
category: embrayage
diagnostic_tree:
- if: vibrations_anormales
  then: verifier_equilibrage_et_fixations
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
  - transmettre le couple
  - accoupler
  - désaccoupler
  must_not_contain_concepts:
  - sélecteur
  - pommeau
  - levier de vitesses
  - differentiel
  - cardan
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transmettre le couple moteur à la boîte de vitesses et permettre la
    séparation temporaire
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "passage parfait"
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
    question: Comment choisir Kit d'embrayage compatible avec mon vehicule ?
  - answer: En cas de embrayage patine regime monte acceleration ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Kit d'embrayage ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Kit d'embrayage sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Kit d'embrayage.
  id: 479
  intro:
    role: Transmettre le couple moteur à la boîte de vitesses et permettre la séparation
      temporaire
    syncParts:
    - transmettre le couple
    - accoupler
    - désaccoupler
    title: A quoi sert Kit d'embrayage ?
  pgId: '479'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/kit-d-embrayage.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure normale** - Après un certain kilométrage, le remplacement
      préventif est recommandé'
    title: Pourquoi remplacer Kit d'embrayage a temps ?
  symptoms:
  - embrayage patine regime monte acceleration
  - odeur brule apres cote demarrage
  - pedale d embrayage anormalement haute ou basse
  - vibrations ou a-coups au demarrage
  - difficulte a passer les vitesses craquements
  - plus de 150 000 km ou conduite urbaine intensive
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 479
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: kit-d-embrayage
source_type: gamme
symptoms:
- description: embrayage patine regime monte acceleration
  evidence:
  - 'Observation: embrayage patine regime monte acceleration'
  - Vérification visuelle ou auditive
  id: S1
  label: Embrayage patine regime monte acceleration
  risk_level: confort
- description: odeur brule apres cote demarrage
  evidence:
  - 'Observation: odeur brule apres cote demarrage'
  - Vérification visuelle ou auditive
  id: S2
  label: Odeur brule apres cote demarrage
  risk_level: confort
- description: pedale d embrayage anormalement haute ou basse
  evidence:
  - 'Observation: pedale d embrayage anormalement haute ou basse'
  - Vérification visuelle ou auditive
  id: S3
  label: Pedale d embrayage anormalement haute ou basse
  risk_level: confort
- description: vibrations ou a-coups au demarrage
  evidence:
  - 'Observation: vibrations ou a-coups au demarrage'
  - Vérification visuelle ou auditive
  id: S4
  label: Vibrations ou a-coups au demarrage
  risk_level: confort
- description: difficulte a passer les vitesses craquements
  evidence:
  - 'Observation: difficulte a passer les vitesses craquements'
  - Vérification visuelle ou auditive
  id: S5
  label: Difficulte a passer les vitesses craquements
  risk_level: confort
- description: plus de 150 000 km ou conduite urbaine intensive
  evidence:
  - 'Observation: plus de 150 000 km ou conduite urbaine intensive'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 150 000 km ou conduite urbaine intensive
  risk_level: confort
title: Kit d'embrayage
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Kit d'embrayage - Guide Diagnostic Complet

## Fonction et Rôle

Transmettre le couple moteur à la boîte de vitesses et permettre la séparation temporaire

**Actions principales:** transmettre le couple, accoupler, désaccoupler, permettre le passage des rapports, relier

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- embrayage patine regime monte acceleration
- odeur brule apres cote demarrage
- pedale d embrayage anormalement haute ou basse
- vibrations ou a-coups au demarrage
- difficulte a passer les vitesses craquements
- plus de 150 000 km ou conduite urbaine intensive

## Procédure de Diagnostic

Pour diagnostiquer un problème de kit d'embrayage:

1. **Inspection visuelle** - Examiner l'état du kit d'embrayage
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- butee-d-embrayage
- cable-d-embrayage
- emetteur-d-embrayage
- recepteur-d-embrayage
- volant-moteur

## Critères de Compatibilité

Pour commander le bon kit d'embrayage, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passage parfait"