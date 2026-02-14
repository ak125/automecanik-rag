---
category: alimentation
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - insuffler
  - injecter
  - alimenter
  must_not_contain_concepts:
  - freinage
  - climatisation
  - distribution
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Injecter de l'air frais dans l'echappement pour accelerer le rechauffement
    du catalyseur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare l'injection"
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
    question: Comment choisir Pompe à air compatible avec mon vehicule ?
  - answer: En cas de voyant moteur au demarrage a froid ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Pompe à air ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Pompe à air sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Pompe à air.
  id: 903
  intro:
    role: Injecter de l'air frais dans l'echappement pour accelerer le rechauffement
      du catalyseur
    syncParts:
    - insuffler
    - injecter
    - alimenter
    title: A quoi sert Pompe à air ?
  pgId: '903'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/pompe-a-air.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Pompe à air a temps ?
  symptoms:
  - voyant moteur au demarrage a froid
  - bruit de soufflerie anormal au demarrage
  - code defaut systeme air secondaire
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 903
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: pompe-a-air
source_type: gamme
symptoms:
- description: voyant moteur au demarrage a froid
  evidence:
  - 'Observation: voyant moteur au demarrage a froid'
  - Vérification visuelle ou auditive
  id: S1
  label: Voyant moteur au demarrage a froid
  risk_level: confort
- description: bruit de soufflerie anormal au demarrage
  evidence:
  - 'Observation: bruit de soufflerie anormal au demarrage'
  - Vérification visuelle ou auditive
  id: S2
  label: Bruit de soufflerie anormal au demarrage
  risk_level: confort
- description: code defaut systeme air secondaire
  evidence:
  - 'Observation: code defaut systeme air secondaire'
  - Vérification visuelle ou auditive
  id: S3
  label: Code defaut systeme air secondaire
  risk_level: confort
title: Pompe à air
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Pompe à air - Guide Diagnostic Complet

## Fonction et Rôle

Injecter de l'air frais dans l'echappement pour accelerer le rechauffement du catalyseur

**Actions principales:** insuffler, injecter, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant moteur au demarrage a froid
- bruit de soufflerie anormal au demarrage
- code defaut systeme air secondaire

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à air:

1. **Inspection visuelle** - Examiner l'état du pompe à air
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- intercooler
- soupape-d-air-secondaire
- soupape-d-aspiration-d-air-secondaire

## Critères de Compatibilité

Pour commander le bon pompe à air, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"