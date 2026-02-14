---
category: suspension
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
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
  - amortir
  - controler
  - dissiper
  must_not_contain_concepts:
  - direction
  - freinage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Controler les oscillations du ressort et stabiliser la roue. Dissipe
    l'energie des chocs. NE SUPPORTE PAS LE POIDS DU VEHICULE!
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "tenue de route parfaite"
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
    question: Comment choisir Amortisseur compatible avec mon vehicule ?
  - answer: En cas de vehicule qui rebondit excessivement sur les bosses ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Amortisseur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Amortisseur sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de suspension pour confirmer Amortisseur.
  id: 854
  intro:
    role: Controler les oscillations du ressort et stabiliser la roue. Dissipe l'energie
      des chocs. NE SUPPORTE PAS LE POIDS DU VEHICULE!
    syncParts:
    - amortir
    - controler
    - dissiper
    title: A quoi sert Amortisseur ?
  pgId: '854'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/amortisseur.md
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
    title: Pourquoi remplacer Amortisseur a temps ?
  symptoms:
  - vehicule qui rebondit excessivement sur les bosses
  - fuite huile visible corps amortisseur
  - usure asymetrique ou irreguliere des pneus
  - bruit de cognement sur routes degradees
  - sensation d instabilite en virage ou au freinage
  - plus de 80 000 km sans remplacement
  - '**Usure asymetrique ou irreguliere des pneus**'
  - '**Sensation d instabilite en virage ou au freinage**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 854
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: amortisseur
source_type: gamme
symptoms:
- description: vehicule qui rebondit excessivement sur les bosses
  evidence:
  - 'Observation: vehicule qui rebondit excessivement sur les bosses'
  - Vérification visuelle ou auditive
  id: S1
  label: Vehicule qui rebondit excessivement sur les bosses
  risk_level: confort
- description: fuite huile visible corps amortisseur
  evidence:
  - 'Observation: fuite huile visible corps amortisseur'
  - Vérification visuelle ou auditive
  id: S2
  label: Fuite huile visible corps amortisseur
  risk_level: confort
- description: usure asymetrique ou irreguliere des pneus
  evidence:
  - 'Observation: usure asymetrique ou irreguliere des pneus'
  - Vérification visuelle ou auditive
  id: S3
  label: Usure asymetrique ou irreguliere des pneus
  risk_level: securite
- description: bruit de cognement sur routes degradees
  evidence:
  - 'Observation: bruit de cognement sur routes degradees'
  - Vérification visuelle ou auditive
  id: S4
  label: Bruit de cognement sur routes degradees
  risk_level: confort
- description: sensation d instabilite en virage ou au freinage
  evidence:
  - 'Observation: sensation d instabilite en virage ou au freinage'
  - Vérification visuelle ou auditive
  id: S5
  label: Sensation d instabilite en virage ou au freinage
  risk_level: securite
- description: plus de 80 000 km sans remplacement
  evidence:
  - 'Observation: plus de 80 000 km sans remplacement'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 80 000 km sans remplacement
  risk_level: confort
title: Amortisseur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Amortisseur - Guide Diagnostic Complet

## Fonction et Rôle

Controler les oscillations du ressort et stabiliser la roue. Dissipe l'energie des chocs. NE SUPPORTE PAS LE POIDS DU VEHICULE!

**Actions principales:** amortir, controler, dissiper, stabiliser, absorber les oscillations

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Usure asymetrique ou irreguliere des pneus**
  usure asymetrique ou irreguliere des pneus
- **Sensation d instabilite en virage ou au freinage**
  sensation d instabilite en virage ou au freinage

### 🟢 Autres Symptômes

- vehicule qui rebondit excessivement sur les bosses
- fuite huile visible corps amortisseur
- bruit de cognement sur routes degradees
- plus de 80 000 km sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de amortisseur:

1. **Inspection visuelle** - Examiner l'état du amortisseur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- bras-de-suspension
- kit-de-butee-de-suspension
- ressort-de-suspension
- rotule-de-suspension

## Critères de Compatibilité

Pour commander le bon amortisseur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "tenue de route parfaite"