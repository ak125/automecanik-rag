---
category: moteur
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
  - ouvrir
  - fermer
  - admettre
  must_not_contain_concepts:
  - echappement
  - carburant
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Ouvrir et fermer le passage des gaz d'admission
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de puissance"
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
    question: Comment choisir Soupape d'admission compatible avec mon vehicule ?
  - answer: En cas de perte de compression sur un ou plusieurs cylindres ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Soupape d'admission ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Soupape d'admission sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de moteur pour confirmer Soupape d'admission.
  id: 1269
  intro:
    role: Soupape d'admission intervient directement sur moteur du vehicule. Un choix
      conforme protege la combustion et limite les pannes secondaires.
    syncParts:
    - ouvrir
    - fermer
    - admettre
    title: A quoi sert Soupape d'admission ?
  pgId: '1269'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/soupape-d-admission.md
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
    title: Pourquoi remplacer Soupape d'admission a temps ?
  symptoms:
  - perte de compression sur un ou plusieurs cylindres
  - rates d allumage persistants
  - claquement au niveau de la culasse
  - consommation d huile anormale guides uses
  - fumee bleue a l echappement
  - casse de courroie de distribution controle
  - '**Claquement au niveau de la culasse**'
  - '**Casse de courroie de distribution controle**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1269
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: soupape-d-admission
source_type: gamme
symptoms:
- description: perte de compression sur un ou plusieurs cylindres
  evidence:
  - 'Observation: perte de compression sur un ou plusieurs cylindres'
  - Vérification visuelle ou auditive
  id: S1
  label: Perte de compression sur un ou plusieurs cylindres
  risk_level: confort
- description: rates d allumage persistants
  evidence:
  - 'Observation: rates d allumage persistants'
  - Vérification visuelle ou auditive
  id: S2
  label: Rates d allumage persistants
  risk_level: confort
- description: claquement au niveau de la culasse
  evidence:
  - 'Observation: claquement au niveau de la culasse'
  - Vérification visuelle ou auditive
  id: S3
  label: Claquement au niveau de la culasse
  risk_level: degats_volant_moteur
- description: consommation d huile anormale guides uses
  evidence:
  - 'Observation: consommation d huile anormale guides uses'
  - Vérification visuelle ou auditive
  id: S4
  label: Consommation d huile anormale guides uses
  risk_level: confort
- description: fumee bleue a l echappement
  evidence:
  - 'Observation: fumee bleue a l echappement'
  - Vérification visuelle ou auditive
  id: S5
  label: Fumee bleue a l echappement
  risk_level: confort
- description: casse de courroie de distribution controle
  evidence:
  - 'Observation: casse de courroie de distribution controle'
  - Vérification visuelle ou auditive
  id: S6
  label: Casse de courroie de distribution controle
  risk_level: degats_volant_moteur
title: Soupape d'admission
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Soupape d'admission - Guide Diagnostic Complet

## Fonction et Rôle

Ouvrir et fermer le passage des gaz d'admission

**Actions principales:** ouvrir, fermer, admettre

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Claquement au niveau de la culasse**
  claquement au niveau de la culasse
- **Casse de courroie de distribution controle**
  casse de courroie de distribution controle

### 🟢 Autres Symptômes

- perte de compression sur un ou plusieurs cylindres
- rates d allumage persistants
- consommation d huile anormale guides uses
- fumee bleue a l echappement

## Procédure de Diagnostic

Pour diagnostiquer un problème de soupape d'admission:

1. **Inspection visuelle** - Examiner l'état du soupape d'admission
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- bagues-d-etancheite-moteur
- joint-de-cache-culbuteurs
- joint-de-collecteur
- joint-de-culasse
- poulie-d-arbre-a-came
- poussoir-de-soupape
- soupape-d-echappement

## Critères de Compatibilité

Pour commander le bon soupape d'admission, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"