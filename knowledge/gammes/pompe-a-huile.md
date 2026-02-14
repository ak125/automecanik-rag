---
category: moteur
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: voyant_tableau_bord_allume
  then: lecture_codes_defaut_obd_et_diagnostic_electronique
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
  - alimenter
  - pressuriser
  - distribuer
  must_not_contain_concepts:
  - freinage
  - climatisation
  - direction
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Alimenter le circuit de lubrification en huile sous pression
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare le moteur"
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
    question: Comment choisir Pompe à huile compatible avec mon vehicule ?
  - answer: En cas de voyant huile allume moteur chaud ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Pompe à huile ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Pompe à huile sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de moteur pour confirmer Pompe à huile.
  id: 596
  intro:
    role: Alimenter le circuit de lubrification en huile sous pression
    syncParts:
    - alimenter
    - pressuriser
    - distribuer
    title: A quoi sert Pompe à huile ?
  pgId: '596'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/pompe-a-huile.md
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
    title: Pourquoi remplacer Pompe à huile a temps ?
  symptoms:
  - voyant huile allume moteur chaud
  - pression d huile insuffisante
  - bruit de cliquetis moteur
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 596
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: pompe-a-huile
source_type: gamme
symptoms:
- description: voyant huile allume moteur chaud
  evidence:
  - 'Observation: voyant huile allume moteur chaud'
  - Vérification visuelle ou auditive
  id: S1
  label: Voyant huile allume moteur chaud
  risk_level: confort
- description: pression d huile insuffisante
  evidence:
  - 'Observation: pression d huile insuffisante'
  - Vérification visuelle ou auditive
  id: S2
  label: Pression d huile insuffisante
  risk_level: confort
- description: bruit de cliquetis moteur
  evidence:
  - 'Observation: bruit de cliquetis moteur'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruit de cliquetis moteur
  risk_level: confort
title: Pompe à huile
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Pompe à huile - Guide Diagnostic Complet

## Fonction et Rôle

Alimenter le circuit de lubrification en huile sous pression

**Actions principales:** alimenter, pressuriser, distribuer

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant huile allume moteur chaud
- pression d huile insuffisante
- bruit de cliquetis moteur

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à huile:

1. **Inspection visuelle** - Examiner l'état du pompe à huile
2. **Contrôle des fuites** - Rechercher traces d'huile ou liquide
3. **Test fonctionnel** - Vérifier le comportement moteur
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- bagues-d-etancheite-moteur
- capteur-niveau-d-huile-moteur
- capteur-pression-et-temperature-d-huile
- carter-d-huile
- pressostat-d-huile

## Critères de Compatibilité

Pour commander le bon pompe à huile, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare le moteur"