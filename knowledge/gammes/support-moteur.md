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
  - isoler
  - fixer
  must_not_contain_concepts:
  - injection
  - freinage
  - climatisation
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Fixe et isole le moteur du châssis
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "moins de vibrations garanties"
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
    question: Comment choisir Support moteur compatible avec mon vehicule ?
  - answer: En cas de vibrations excessives ressenties volant habitacle ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Support moteur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Support moteur sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de moteur pour confirmer Support moteur.
  id: 247
  intro:
    role: Support moteur intervient directement sur moteur du vehicule. Un choix conforme
      protege la combustion et limite les pannes secondaires.
    syncParts:
    - supporter
    - isoler
    - fixer
    title: A quoi sert Support moteur ?
  pgId: '247'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/support-moteur.md
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
    title: Pourquoi remplacer Support moteur a temps ?
  symptoms:
  - vibrations excessives ressenties volant habitacle
  - caoutchouc support visiblement fissure affaisse
  - bruit sourd ou claquement lors des accelerations
  - moteur bouge anormalement ouverture capot
  - a-coups au passage des vitesses
  - plus de 120 000 km ou vibrations au ralenti
  - '**Bruit sourd ou claquement lors des accelerations**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 247
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: support-moteur
source_type: gamme
symptoms:
- description: vibrations excessives ressenties volant habitacle
  evidence:
  - 'Observation: vibrations excessives ressenties volant habitacle'
  - Vérification visuelle ou auditive
  id: S1
  label: Vibrations excessives ressenties volant habitacle
  risk_level: confort
- description: caoutchouc support visiblement fissure affaisse
  evidence:
  - 'Observation: caoutchouc support visiblement fissure affaisse'
  - Vérification visuelle ou auditive
  id: S2
  label: Caoutchouc support visiblement fissure affaisse
  risk_level: confort
- description: bruit sourd ou claquement lors des accelerations
  evidence:
  - 'Observation: bruit sourd ou claquement lors des accelerations'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruit sourd ou claquement lors des accelerations
  risk_level: degats_volant_moteur
- description: moteur bouge anormalement ouverture capot
  evidence:
  - 'Observation: moteur bouge anormalement ouverture capot'
  - Vérification visuelle ou auditive
  id: S4
  label: Moteur bouge anormalement ouverture capot
  risk_level: confort
- description: a-coups au passage des vitesses
  evidence:
  - 'Observation: a-coups au passage des vitesses'
  - Vérification visuelle ou auditive
  id: S5
  label: A-coups au passage des vitesses
  risk_level: confort
- description: plus de 120 000 km ou vibrations au ralenti
  evidence:
  - 'Observation: plus de 120 000 km ou vibrations au ralenti'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 120 000 km ou vibrations au ralenti
  risk_level: confort
title: Support moteur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Support moteur - Guide Diagnostic Complet

## Fonction et Rôle

Fixe et isole le moteur du châssis

**Actions principales:** supporter, isoler, fixer, absorber

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit sourd ou claquement lors des accelerations**
  bruit sourd ou claquement lors des accelerations

### 🟢 Autres Symptômes

- vibrations excessives ressenties volant habitacle
- caoutchouc support visiblement fissure affaisse
- moteur bouge anormalement ouverture capot
- a-coups au passage des vitesses
- plus de 120 000 km ou vibrations au ralenti

## Procédure de Diagnostic

Pour diagnostiquer un problème de support moteur:

1. **Inspection visuelle** - Examiner l'état du support moteur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- courroie-de-distribution
- kit-de-chaine-de-distribution
- kit-de-distribution

## Critères de Compatibilité

Pour commander le bon support moteur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "moins de vibrations garanties"