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
  - essuyer
  - nettoyer
  - balayer
  must_not_contain_concepts:
  - capteur abs
  - freinage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Nettoie le pare-brise de l'eau et des impuretés
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "visibilité parfaite garantie"
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
    question: Comment choisir Balais d'essuie-glace compatible avec mon vehicule ?
  - answer: En cas de traces ou stries sur le pare-brise apres essuyage ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Balais d'essuie-glace ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Balais d'essuie-glace sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Balais d'essuie-glace.
  id: 298
  intro:
    role: Nettoie le pare-brise de l'eau et des impuretés
    syncParts:
    - essuyer
    - nettoyer
    - balayer
    title: A quoi sert Balais d'essuie-glace ?
  pgId: '298'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/balais-d-essuie-glace.md
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
    title: Pourquoi remplacer Balais d'essuie-glace a temps ?
  symptoms:
  - traces ou stries sur le pare-brise apres essuyage
  - zones non essuyees voile d eau persistant
  - bruit de frottement ou de crissement
  - balai qui sautille sur le pare-brise
  - caoutchouc fissure durci ou decolle
  - plus d un an depuis le dernier remplacement
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 298
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: balais-d-essuie-glace
source_type: gamme
symptoms:
- description: traces ou stries sur le pare-brise apres essuyage
  evidence:
  - 'Observation: traces ou stries sur le pare-brise apres essuyage'
  - Vérification visuelle ou auditive
  id: S1
  label: Traces ou stries sur le pare-brise apres essuyage
  risk_level: confort
- description: zones non essuyees voile d eau persistant
  evidence:
  - 'Observation: zones non essuyees voile d eau persistant'
  - Vérification visuelle ou auditive
  id: S2
  label: Zones non essuyees voile d eau persistant
  risk_level: confort
- description: bruit de frottement ou de crissement
  evidence:
  - 'Observation: bruit de frottement ou de crissement'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruit de frottement ou de crissement
  risk_level: confort
- description: balai qui sautille sur le pare-brise
  evidence:
  - 'Observation: balai qui sautille sur le pare-brise'
  - Vérification visuelle ou auditive
  id: S4
  label: Balai qui sautille sur le pare-brise
  risk_level: confort
- description: caoutchouc fissure durci ou decolle
  evidence:
  - 'Observation: caoutchouc fissure durci ou decolle'
  - Vérification visuelle ou auditive
  id: S5
  label: Caoutchouc fissure durci ou decolle
  risk_level: confort
- description: plus d un an depuis le dernier remplacement
  evidence:
  - 'Observation: plus d un an depuis le dernier remplacement'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus d un an depuis le dernier remplacement
  risk_level: confort
title: Balais d'essuie-glace
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Balais d'essuie-glace - Guide Diagnostic Complet

## Fonction et Rôle

Nettoie le pare-brise de l'eau et des impuretés

**Actions principales:** essuyer, nettoyer, balayer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- traces ou stries sur le pare-brise apres essuyage
- zones non essuyees voile d eau persistant
- bruit de frottement ou de crissement
- balai qui sautille sur le pare-brise
- caoutchouc fissure durci ou decolle
- plus d un an depuis le dernier remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de balais d'essuie-glace:

1. **Inspection visuelle** - Examiner l'état du balais d'essuie-glace
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-d-essuie-glace

## Critères de Compatibilité

Pour commander le bon balais d'essuie-glace, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "visibilité parfaite garantie"