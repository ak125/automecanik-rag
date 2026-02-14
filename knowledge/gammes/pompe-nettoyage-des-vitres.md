---
category: accessoires
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - projeter
  - pulveriser
  - alimenter
  must_not_contain_concepts:
  - balai
  - moteur essuie-glace
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Projette le liquide lave-glace sur le pare-brise
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "visibilite parfaite"
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
    question: Comment choisir Pompe nettoyage des vitres compatible avec mon vehicule
      ?
  - answer: En cas de jet de lave-glace absent ou de degradation mesurable, il faut
      controler rapidement avant panne secondaire.
    question: Quand remplacer Pompe nettoyage des vitres ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Pompe nettoyage des vitres sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Pompe nettoyage
    des vitres.
  id: 794
  intro:
    role: Projette le liquide lave-glace sur le pare-brise
    syncParts:
    - projeter
    - pulveriser
    - alimenter
    title: A quoi sert Pompe nettoyage des vitres ?
  pgId: '794'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/pompe-nettoyage-des-vitres.md
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
    title: Pourquoi remplacer Pompe nettoyage des vitres a temps ?
  symptoms:
  - jet de lave-glace absent
  - pompe qui fait du bruit sans projeter
  - jet faible malgre reservoir plein
  - '**Jet de lave-glace absent**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 794
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: pompe-nettoyage-des-vitres
source_type: gamme
symptoms:
- description: jet de lave-glace absent
  evidence:
  - 'Observation: jet de lave-glace absent'
  - Vérification visuelle ou auditive
  id: S1
  label: Jet de lave-glace absent
  risk_level: securite
- description: pompe qui fait du bruit sans projeter
  evidence:
  - 'Observation: pompe qui fait du bruit sans projeter'
  - Vérification visuelle ou auditive
  id: S2
  label: Pompe qui fait du bruit sans projeter
  risk_level: confort
- description: jet faible malgre reservoir plein
  evidence:
  - 'Observation: jet faible malgre reservoir plein'
  - Vérification visuelle ou auditive
  id: S3
  label: Jet faible malgre reservoir plein
  risk_level: confort
title: Pompe nettoyage des vitres
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Pompe nettoyage des vitres - Guide Diagnostic Complet

## Fonction et Rôle

Projette le liquide lave-glace sur le pare-brise

**Actions principales:** projeter, pulveriser, alimenter

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Jet de lave-glace absent**
  jet de lave-glace absent

### 🟢 Autres Symptômes

- pompe qui fait du bruit sans projeter
- jet faible malgre reservoir plein

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe nettoyage des vitres:

1. **Inspection visuelle** - Examiner l'état du pompe nettoyage des vitres
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bras-d-essuie-glace
- commande-d-essuie-glace
- moteur-d-essuie-glace

## Critères de Compatibilité

Pour commander le bon pompe nettoyage des vitres, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilite parfaite"