---
category: suspension
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
  - supporter
  - maintenir la hauteur
  - porter
  must_not_contain_concepts:
  - direction
  - freinage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Supporter la charge du vehicule et maintenir la hauteur de caisse.
    Stocke et restitue l'energie. N'AMORTIT PAS!
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
    question: Comment choisir Ressort de suspension compatible avec mon vehicule ?
  - answer: En cas de vehicule affaisse d un cote avant ou arriere ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Ressort de suspension ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Ressort de suspension sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de suspension pour confirmer Ressort de suspension.
  id: 188
  intro:
    role: Supporter la charge du vehicule et maintenir la hauteur de caisse. Stocke
      et restitue l'energie. N'AMORTIT PAS!
    syncParts:
    - supporter
    - maintenir la hauteur
    - porter
    title: A quoi sert Ressort de suspension ?
  pgId: '188'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/ressort-de-suspension.md
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
    title: Pourquoi remplacer Ressort de suspension a temps ?
  symptoms:
  - vehicule affaisse d un cote avant ou arriere
  - bruit de claquement metallique sur bosses
  - spire de ressort visiblement cassee ou fissuree
  - tenue de route degradee en virage et freinage
  - odeur metallique ressort frotte contre
  - plus de 150 000 km ou controle technique refuse
  - '**Bruit de claquement metallique sur bosses**'
  - '**Spire de ressort visiblement cassee ou fissuree**'
  - '**Tenue de route degradee en virage et freinage**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 188
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: ressort-de-suspension
source_type: gamme
symptoms:
- description: vehicule affaisse d un cote avant ou arriere
  evidence:
  - 'Observation: vehicule affaisse d un cote avant ou arriere'
  - Vérification visuelle ou auditive
  id: S1
  label: Vehicule affaisse d un cote avant ou arriere
  risk_level: confort
- description: bruit de claquement metallique sur bosses
  evidence:
  - 'Observation: bruit de claquement metallique sur bosses'
  - Vérification visuelle ou auditive
  id: S2
  label: Bruit de claquement metallique sur bosses
  risk_level: degats_volant_moteur
- description: spire de ressort visiblement cassee ou fissuree
  evidence:
  - 'Observation: spire de ressort visiblement cassee ou fissuree'
  - Vérification visuelle ou auditive
  id: S3
  label: Spire de ressort visiblement cassee ou fissuree
  risk_level: degats_volant_moteur
- description: tenue de route degradee en virage et freinage
  evidence:
  - 'Observation: tenue de route degradee en virage et freinage'
  - Vérification visuelle ou auditive
  id: S4
  label: Tenue de route degradee en virage et freinage
  risk_level: securite
- description: odeur metallique ressort frotte contre
  evidence:
  - 'Observation: odeur metallique ressort frotte contre'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur metallique ressort frotte contre
  risk_level: confort
- description: plus de 150 000 km ou controle technique refuse
  evidence:
  - 'Observation: plus de 150 000 km ou controle technique refuse'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 150 000 km ou controle technique refuse
  risk_level: confort
title: Ressort de suspension
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Ressort de suspension - Guide Diagnostic Complet

## Fonction et Rôle

Supporter la charge du vehicule et maintenir la hauteur de caisse. Stocke et restitue l'energie. N'AMORTIT PAS!

**Actions principales:** supporter, maintenir la hauteur, porter, stocker l'energie, restituer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit de claquement metallique sur bosses**
  bruit de claquement metallique sur bosses
- **Spire de ressort visiblement cassee ou fissuree**
  spire de ressort visiblement cassee ou fissuree

### 🟡 Symptômes de Sécurité

- **Tenue de route degradee en virage et freinage**
  tenue de route degradee en virage et freinage

### 🟢 Autres Symptômes

- vehicule affaisse d un cote avant ou arriere
- odeur metallique ressort frotte contre
- plus de 150 000 km ou controle technique refuse

## Procédure de Diagnostic

Pour diagnostiquer un problème de ressort de suspension:

1. **Inspection visuelle** - Examiner l'état du ressort de suspension
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- amortisseur
- kit-de-butee-de-suspension

## Critères de Compatibilité

Pour commander le bon ressort de suspension, vous devez connaître:

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