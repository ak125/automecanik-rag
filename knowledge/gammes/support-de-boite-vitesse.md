---
category: support_moteur
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
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
  - supporter
  - fixer
  - amortir
  must_not_contain_concepts:
  - injection
  - freinage
  - climatisation
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Supporter et fixer la boite de vitesses au chassis
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "zero vibration"
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
    question: Comment choisir Support de boîte vitesse compatible avec mon vehicule
      ?
  - answer: En cas de vibrations ressenties sur le levier de vitesses ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Support de boîte vitesse ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Support de boîte vitesse sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de moteur pour confirmer Support de boîte vitesse.
  id: 249
  intro:
    role: Support de boîte vitesse intervient directement sur moteur du vehicule.
      Un choix conforme protege la combustion et limite les pannes secondaires.
    syncParts:
    - supporter
    - fixer
    - amortir
    title: A quoi sert Support de boîte vitesse ?
  pgId: '249'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/support-de-boite-vitesse.md
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
    title: Pourquoi remplacer Support de boîte vitesse a temps ?
  symptoms:
  - vibrations ressenties sur le levier de vitesses
  - caoutchouc du support visiblement deteriore
  - claquement ou bruit sourd au passage des rapports
  - boite de vitesses qui semble bouger anormalement
  - sensation d a-coups a l embrayage ou debrayage
  - plus de 100 000 km ou supports moteur a changer
  - '**Claquement ou bruit sourd au passage des rapports**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 249
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: support-de-boite-vitesse
source_type: gamme
symptoms:
- description: vibrations ressenties sur le levier de vitesses
  evidence:
  - 'Observation: vibrations ressenties sur le levier de vitesses'
  - Vérification visuelle ou auditive
  id: S1
  label: Vibrations ressenties sur le levier de vitesses
  risk_level: confort
- description: caoutchouc du support visiblement deteriore
  evidence:
  - 'Observation: caoutchouc du support visiblement deteriore'
  - Vérification visuelle ou auditive
  id: S2
  label: Caoutchouc du support visiblement deteriore
  risk_level: confort
- description: claquement ou bruit sourd au passage des rapports
  evidence:
  - 'Observation: claquement ou bruit sourd au passage des rapports'
  - Vérification visuelle ou auditive
  id: S3
  label: Claquement ou bruit sourd au passage des rapports
  risk_level: degats_volant_moteur
- description: boite de vitesses qui semble bouger anormalement
  evidence:
  - 'Observation: boite de vitesses qui semble bouger anormalement'
  - Vérification visuelle ou auditive
  id: S4
  label: Boite de vitesses qui semble bouger anormalement
  risk_level: confort
- description: sensation d a-coups a l embrayage ou debrayage
  evidence:
  - 'Observation: sensation d a-coups a l embrayage ou debrayage'
  - Vérification visuelle ou auditive
  id: S5
  label: Sensation d a-coups a l embrayage ou debrayage
  risk_level: confort
- description: plus de 100 000 km ou supports moteur a changer
  evidence:
  - 'Observation: plus de 100 000 km ou supports moteur a changer'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 100 000 km ou supports moteur a changer
  risk_level: confort
title: Support de boîte vitesse
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Support de boîte vitesse - Guide Diagnostic Complet

## Fonction et Rôle

Supporter et fixer la boite de vitesses au chassis

**Actions principales:** supporter, fixer, amortir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement ou bruit sourd au passage des rapports**
  claquement ou bruit sourd au passage des rapports

### 🟢 Autres Symptômes

- vibrations ressenties sur le levier de vitesses
- caoutchouc du support visiblement deteriore
- boite de vitesses qui semble bouger anormalement
- sensation d a-coups a l embrayage ou debrayage
- plus de 100 000 km ou supports moteur a changer

## Procédure de Diagnostic

Pour diagnostiquer un problème de support de boîte vitesse:

1. **Inspection visuelle** - Examiner l'état du support de boîte vitesse
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- support-moteur
- boite-de-vitesses

## Critères de Compatibilité

Pour commander le bon support de boîte vitesse, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "zero vibration"