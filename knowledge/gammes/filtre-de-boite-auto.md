---
category: filtration
diagnostic_tree:
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
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
  - filtrer
  - retenir
  - purifier
  must_not_contain_concepts:
  - injection
  - freinage
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Filtrer l'huile de la boite automatique
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "filtration parfaite"
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
    question: Comment choisir Filtre de boîte auto compatible avec mon vehicule ?
  - answer: En cas de passages de vitesses brutaux ou tardifs ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Filtre de boîte auto ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Filtre de boîte auto sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Filtre de boîte
    auto.
  id: 416
  intro:
    role: Filtre de boîte auto intervient directement sur compatibilite du vehicule.
      Un choix conforme protege la securite et limite les pannes secondaires.
    syncParts:
    - filtrer
    - retenir
    - purifier
    title: A quoi sert Filtre de boîte auto ?
  pgId: '416'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/filtre-de-boite-auto.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Défaillance électrique** - Problème de connexion, de câblage ou
      de composant électronique'
    title: Pourquoi remplacer Filtre de boîte auto a temps ?
  symptoms:
  - passages de vitesses brutaux ou tardifs
  - vibrations lors des changements de rapport
  - boite qui patine sous charge
  - huile atf brune ou odeur brule
  - voyant temperature boite
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 416
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: filtre-de-boite-auto
source_type: gamme
symptoms:
- description: passages de vitesses brutaux ou tardifs
  evidence:
  - 'Observation: passages de vitesses brutaux ou tardifs'
  - Vérification visuelle ou auditive
  id: S1
  label: Passages de vitesses brutaux ou tardifs
  risk_level: confort
- description: vibrations lors des changements de rapport
  evidence:
  - 'Observation: vibrations lors des changements de rapport'
  - Vérification visuelle ou auditive
  id: S2
  label: Vibrations lors des changements de rapport
  risk_level: confort
- description: boite qui patine sous charge
  evidence:
  - 'Observation: boite qui patine sous charge'
  - Vérification visuelle ou auditive
  id: S3
  label: Boite qui patine sous charge
  risk_level: confort
- description: huile atf brune ou odeur brule
  evidence:
  - 'Observation: huile atf brune ou odeur brule'
  - Vérification visuelle ou auditive
  id: S4
  label: Huile atf brune ou odeur brule
  risk_level: confort
- description: voyant temperature boite
  evidence:
  - 'Observation: voyant temperature boite'
  - Vérification visuelle ou auditive
  id: S5
  label: Voyant temperature boite
  risk_level: confort
title: Filtre de boîte auto
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Filtre de boîte auto - Guide Diagnostic Complet

## Fonction et Rôle

Filtrer l'huile de la boite automatique

**Actions principales:** filtrer, retenir, purifier

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- passages de vitesses brutaux ou tardifs
- vibrations lors des changements de rapport
- boite qui patine sous charge
- huile atf brune ou odeur brule
- voyant temperature boite

## Procédure de Diagnostic

Pour diagnostiquer un problème de filtre de boîte auto:

1. **Inspection visuelle** - Examiner l'état du filtre de boîte auto
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords

## Causes Probables

- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- boite-automatique
- huile-bva

## Critères de Compatibilité

Pour commander le bon filtre de boîte auto, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "filtration parfaite"