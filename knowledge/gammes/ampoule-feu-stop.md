---
category: eclairage
diagnostic_tree:
- if: symptome_general_detecte
  then: inspection_visuelle_et_test_fonctionnel
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - produire
  - emettre
  - signaler
  must_not_contain_concepts:
  - feu complet
  - optique
  - relais
  - commande
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Produit la lumière pour signaler le freinage du véhicule
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
    question: Comment choisir Ampoule feu stop compatible avec mon vehicule ?
  - answer: En cas de un seul feu stop ne s allume pas ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Ampoule feu stop ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Ampoule feu stop sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Ampoule feu stop.
  id: 111
  intro:
    role: Produit la lumière pour signaler le freinage du véhicule
    syncParts:
    - produire
    - emettre
    - signaler
    title: A quoi sert Ampoule feu stop ?
  pgId: '111'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/ampoule-feu-stop.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Défaillance progressive** - Usure normale due à l''utilisation'
    title: Pourquoi remplacer Ampoule feu stop a temps ?
  symptoms:
  - un seul feu stop ne s allume pas
  - feu stop qui clignote ou s allume faiblement
  - ampoule noircie visible a travers le feu
  - message defaut feux au tableau de bord
  - feux stop grillent souvent verifier
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 111
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: ampoule-feu-stop
source_type: gamme
symptoms:
- description: un seul feu stop ne s allume pas
  evidence:
  - 'Observation: un seul feu stop ne s allume pas'
  - Vérification visuelle ou auditive
  id: S1
  label: Un seul feu stop ne s allume pas
  risk_level: confort
- description: feu stop qui clignote ou s allume faiblement
  evidence:
  - 'Observation: feu stop qui clignote ou s allume faiblement'
  - Vérification visuelle ou auditive
  id: S2
  label: Feu stop qui clignote ou s allume faiblement
  risk_level: confort
- description: ampoule noircie visible a travers le feu
  evidence:
  - 'Observation: ampoule noircie visible a travers le feu'
  - Vérification visuelle ou auditive
  id: S3
  label: Ampoule noircie visible a travers le feu
  risk_level: confort
- description: message defaut feux au tableau de bord
  evidence:
  - 'Observation: message defaut feux au tableau de bord'
  - Vérification visuelle ou auditive
  id: S4
  label: Message defaut feux au tableau de bord
  risk_level: confort
- description: feux stop grillent souvent verifier
  evidence:
  - 'Observation: feux stop grillent souvent verifier'
  - Vérification visuelle ou auditive
  id: S5
  label: Feux stop grillent souvent verifier
  risk_level: confort
title: Ampoule feu stop
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Ampoule feu stop - Guide Diagnostic Complet

## Fonction et Rôle

Produit la lumière pour signaler le freinage du véhicule

**Actions principales:** produire, emettre, signaler

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- un seul feu stop ne s allume pas
- feu stop qui clignote ou s allume faiblement
- ampoule noircie visible a travers le feu
- message defaut feux au tableau de bord
- feux stop grillent souvent verifier

## Procédure de Diagnostic

Pour diagnostiquer un problème de ampoule feu stop:

1. **Inspection visuelle** - Examiner l'état du ampoule feu stop
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- feu-arriere
- contacteur-feu-stop

## Critères de Compatibilité

Pour commander le bon ampoule feu stop, vous devez connaître:

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