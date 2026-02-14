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
  - absorber
  - limiter
  - amortir
  must_not_contain_concepts:
  - injection
  - freinage
  - climatisation
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Limiter la course de l'amortisseur en fin de detente
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "confort parfait"
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
    question: Comment choisir Butée élastique d'amortisseur compatible avec mon vehicule
      ?
  - answer: En cas de bruit sourd de talonnement sur gros nids-de-poule ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Butée élastique d'amortisseur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Butée élastique d'amortisseur sans verification atelier
      ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de suspension pour confirmer Butée élastique d'amortisseur.
  id: 1182
  intro:
    role: Butée élastique d'amortisseur intervient directement sur suspension du vehicule.
      Un choix conforme protege la stabilite et limite les pannes secondaires.
    syncParts:
    - absorber
    - limiter
    - amortir
    title: A quoi sert Butée élastique d'amortisseur ?
  pgId: '1182'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - MISSING_REQUIRED_TERMS
    - TOO_SHORT
    score: 60
    source: reindex:gammes/butee-elastique-d-amortisseur.md
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
    title: Pourquoi remplacer Butée élastique d'amortisseur a temps ?
  symptoms:
  - bruit sourd de talonnement sur gros nids-de-poule
  - butee visible fissuree ou ecrasee
  - amortisseur qui tape en fin de course
  - sensation rebonds amortis grosses bosses
  - odeur de caoutchouc chaud si butee frotte
  - plus de 80 000 km ou changement amortisseurs prevu
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1182
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: butee-elastique-d-amortisseur
source_type: gamme
symptoms:
- description: bruit sourd de talonnement sur gros nids-de-poule
  evidence:
  - 'Observation: bruit sourd de talonnement sur gros nids-de-poule'
  - Vérification visuelle ou auditive
  id: S1
  label: Bruit sourd de talonnement sur gros nids-de-poule
  risk_level: confort
- description: butee visible fissuree ou ecrasee
  evidence:
  - 'Observation: butee visible fissuree ou ecrasee'
  - Vérification visuelle ou auditive
  id: S2
  label: Butee visible fissuree ou ecrasee
  risk_level: confort
- description: amortisseur qui tape en fin de course
  evidence:
  - 'Observation: amortisseur qui tape en fin de course'
  - Vérification visuelle ou auditive
  id: S3
  label: Amortisseur qui tape en fin de course
  risk_level: confort
- description: sensation rebonds amortis grosses bosses
  evidence:
  - 'Observation: sensation rebonds amortis grosses bosses'
  - Vérification visuelle ou auditive
  id: S4
  label: Sensation rebonds amortis grosses bosses
  risk_level: confort
- description: odeur de caoutchouc chaud si butee frotte
  evidence:
  - 'Observation: odeur de caoutchouc chaud si butee frotte'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de caoutchouc chaud si butee frotte
  risk_level: confort
- description: plus de 80 000 km ou changement amortisseurs prevu
  evidence:
  - 'Observation: plus de 80 000 km ou changement amortisseurs prevu'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 80 000 km ou changement amortisseurs prevu
  risk_level: confort
title: Butée élastique d'amortisseur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Butée élastique d'amortisseur - Guide Diagnostic Complet

## Fonction et Rôle

Limiter la course de l'amortisseur en fin de detente

**Actions principales:** absorber, limiter, amortir

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- bruit sourd de talonnement sur gros nids-de-poule
- butee visible fissuree ou ecrasee
- amortisseur qui tape en fin de course
- sensation rebonds amortis grosses bosses
- odeur de caoutchouc chaud si butee frotte
- plus de 80 000 km ou changement amortisseurs prevu

## Procédure de Diagnostic

Pour diagnostiquer un problème de butée élastique d'amortisseur:

1. **Inspection visuelle** - Examiner l'état du butée élastique d'amortisseur
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
- ressort-de-suspension

## Critères de Compatibilité

Pour commander le bon butée élastique d'amortisseur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "confort parfait"