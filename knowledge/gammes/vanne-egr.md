---
category: alimentation
diagnostic_tree:
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
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
  - recycler
  - ouvrir
  - fermer
  must_not_contain_concepts:
  - carburant
  - injection
  - injecteur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Recycler une partie des gaz d'echappement vers l'admission pour reduire
    les emissions de NOx
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "nettoie le moteur"
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
    question: Comment choisir Vanne EGR compatible avec mon vehicule ?
  - answer: En cas de perte de puissance a bas et moyen regime ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Vanne EGR ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Vanne EGR sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Vanne EGR.
  id: 1145
  intro:
    role: Recycler une partie des gaz d'echappement vers l'admission pour reduire
      les emissions de NOx
    syncParts:
    - recycler
    - ouvrir
    - fermer
    title: A quoi sert Vanne EGR ?
  pgId: '1145'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/vanne-egr.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure normale** - Après un certain kilométrage, le remplacement
      préventif est recommandé'
    title: Pourquoi remplacer Vanne EGR a temps ?
  symptoms:
  - perte de puissance a bas et moyen regime
  - fumee noire a l acceleration
  - ralenti irregulier ou moteur qui broute
  - voyant moteur allume codes p0400-p0409
  - a-coups a bas regime
  - plus de 80 000 km sans nettoyage diesel
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1145
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: vanne-egr
source_type: gamme
symptoms:
- description: perte de puissance a bas et moyen regime
  evidence:
  - 'Observation: perte de puissance a bas et moyen regime'
  - Vérification visuelle ou auditive
  id: S1
  label: Perte de puissance a bas et moyen regime
  risk_level: confort
- description: fumee noire a l acceleration
  evidence:
  - 'Observation: fumee noire a l acceleration'
  - Vérification visuelle ou auditive
  id: S2
  label: Fumee noire a l acceleration
  risk_level: confort
- description: ralenti irregulier ou moteur qui broute
  evidence:
  - 'Observation: ralenti irregulier ou moteur qui broute'
  - Vérification visuelle ou auditive
  id: S3
  label: Ralenti irregulier ou moteur qui broute
  risk_level: confort
- description: voyant moteur allume codes p0400-p0409
  evidence:
  - 'Observation: voyant moteur allume codes p0400-p0409'
  - Vérification visuelle ou auditive
  id: S4
  label: Voyant moteur allume codes p0400-p0409
  risk_level: confort
- description: a-coups a bas regime
  evidence:
  - 'Observation: a-coups a bas regime'
  - Vérification visuelle ou auditive
  id: S5
  label: A-coups a bas regime
  risk_level: confort
- description: plus de 80 000 km sans nettoyage diesel
  evidence:
  - 'Observation: plus de 80 000 km sans nettoyage diesel'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 80 000 km sans nettoyage diesel
  risk_level: confort
title: Vanne EGR
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Vanne EGR - Guide Diagnostic Complet

## Fonction et Rôle

Recycler une partie des gaz d'echappement vers l'admission pour reduire les emissions de NOx

**Actions principales:** recycler, ouvrir, fermer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- perte de puissance a bas et moyen regime
- fumee noire a l acceleration
- ralenti irregulier ou moteur qui broute
- voyant moteur allume codes p0400-p0409
- a-coups a bas regime
- plus de 80 000 km sans nettoyage diesel

## Procédure de Diagnostic

Pour diagnostiquer un problème de vanne egr:

1. **Inspection visuelle** - Examiner l'état du vanne egr
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- catalyseur
- fap
- injecteur
- turbo

## Critères de Compatibilité

Pour commander le bon vanne egr, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "nettoie le moteur"