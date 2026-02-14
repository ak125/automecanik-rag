---
category: echappement
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
  - filtrer
  - retenir
  - regenerer
  must_not_contain_concepts:
  - catalyseur
  - pot catalytique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Filtre et retient les particules fines des gaz d'échappement diesel
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
    question: Comment choisir FAP compatible avec mon vehicule ?
  - answer: En cas de voyant filtre particules allume tableau ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer FAP ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter FAP sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer FAP.
  id: 1256
  intro:
    role: Filtre et retient les particules fines des gaz d'échappement diesel
    syncParts:
    - filtrer
    - retenir
    - regenerer
    title: A quoi sert FAP ?
  pgId: '1256'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/fap.md
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
    title: Pourquoi remplacer FAP a temps ?
  symptoms:
  - voyant filtre particules allume tableau
  - perte de puissance importante mode degrade
  - regenerations frequentes odeur de brule
  - fumee noire excessive a l acceleration
  - surconsommation de carburant anormale
  - plus de 150 000 km en conduite urbaine
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1256
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: fap
source_type: gamme
symptoms:
- description: voyant filtre particules allume tableau
  evidence:
  - 'Observation: voyant filtre particules allume tableau'
  - Vérification visuelle ou auditive
  id: S1
  label: Voyant filtre particules allume tableau
  risk_level: confort
- description: perte de puissance importante mode degrade
  evidence:
  - 'Observation: perte de puissance importante mode degrade'
  - Vérification visuelle ou auditive
  id: S2
  label: Perte de puissance importante mode degrade
  risk_level: confort
- description: regenerations frequentes odeur de brule
  evidence:
  - 'Observation: regenerations frequentes odeur de brule'
  - Vérification visuelle ou auditive
  id: S3
  label: Regenerations frequentes odeur de brule
  risk_level: confort
- description: fumee noire excessive a l acceleration
  evidence:
  - 'Observation: fumee noire excessive a l acceleration'
  - Vérification visuelle ou auditive
  id: S4
  label: Fumee noire excessive a l acceleration
  risk_level: confort
- description: surconsommation de carburant anormale
  evidence:
  - 'Observation: surconsommation de carburant anormale'
  - Vérification visuelle ou auditive
  id: S5
  label: Surconsommation de carburant anormale
  risk_level: confort
- description: plus de 150 000 km en conduite urbaine
  evidence:
  - 'Observation: plus de 150 000 km en conduite urbaine'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 150 000 km en conduite urbaine
  risk_level: confort
title: FAP
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# FAP - Guide Diagnostic Complet

## Fonction et Rôle

Filtre et retient les particules fines des gaz d'échappement diesel

**Actions principales:** filtrer, retenir, regenerer, stocker

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant filtre particules allume tableau
- perte de puissance importante mode degrade
- regenerations frequentes odeur de brule
- fumee noire excessive a l acceleration
- surconsommation de carburant anormale
- plus de 150 000 km en conduite urbaine

## Procédure de Diagnostic

Pour diagnostiquer un problème de fap:

1. **Inspection visuelle** - Examiner l'état du fap
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-temperature-d-air-admission
- catalyseur
- sonde-lambda
- tube-d-echappement
- vanne-egr

## Critères de Compatibilité

Pour commander le bon fap, vous devez connaître:

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