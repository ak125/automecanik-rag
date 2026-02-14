---
category: echappement
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: vibrations_anormales
  then: verifier_equilibrage_et_fixations
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - attenuer
  - evacuer
  - reduire le bruit
  must_not_contain_concepts:
  - injection
  - freinage
  - climatisation
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Atténue le bruit des gaz d'échappement avant évacuation
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "passe le controle technique"
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
    question: Comment choisir Silencieux compatible avec mon vehicule ?
  - answer: En cas de bruit excessif ou de degradation mesurable, il faut controler
      rapidement avant panne secondaire.
    question: Quand remplacer Silencieux ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Silencieux sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Silencieux.
  id: 26
  intro:
    role: Atténue le bruit des gaz d'échappement avant évacuation
    syncParts:
    - attenuer
    - evacuer
    - reduire le bruit
    title: A quoi sert Silencieux ?
  pgId: '26'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/silencieux.md
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
    title: Pourquoi remplacer Silencieux a temps ?
  symptoms:
  - bruit excessif
  - vibrations
  - corrosion
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 26
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: silencieux
source_type: gamme
symptoms:
- description: bruit excessif
  evidence:
  - 'Observation: bruit excessif'
  - Vérification visuelle ou auditive
  id: S1
  label: Bruit excessif
  risk_level: confort
- description: vibrations
  evidence:
  - 'Observation: vibrations'
  - Vérification visuelle ou auditive
  id: S2
  label: Vibrations
  risk_level: confort
- description: corrosion
  evidence:
  - 'Observation: corrosion'
  - Vérification visuelle ou auditive
  id: S3
  label: Corrosion
  risk_level: confort
title: Silencieux
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Silencieux - Guide Diagnostic Complet

## Fonction et Rôle

Atténue le bruit des gaz d'échappement avant évacuation

**Actions principales:** attenuer, evacuer, reduire le bruit

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- bruit excessif
- vibrations
- corrosion

## Procédure de Diagnostic

Pour diagnostiquer un problème de silencieux:

1. **Inspection visuelle** - Examiner l'état du silencieux
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- tube-d-echappement
- support-d-echappement

## Critères de Compatibilité

Pour commander le bon silencieux, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passe le controle technique"