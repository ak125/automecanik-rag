---
category: eclairage
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with: {}
  must_be_true:
  - eclairer
  - illuminer
  must_not_contain_concepts:
  - injection
  - freinage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Éclaire la route devant le véhicule
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "meilleure visibilité garantie"
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
    question: Comment choisir Feu avant compatible avec mon vehicule ?
  - answer: En cas de eclairage insuffisant nuit malgre ampoules ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Feu avant ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Feu avant sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Feu avant.
  id: 259
  intro:
    role: Feu avant intervient directement sur compatibilite du vehicule. Un choix
      conforme protege la securite et limite les pannes secondaires.
    syncParts:
    - eclairer
    - illuminer
    title: A quoi sert Feu avant ?
  pgId: '259'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/feu-avant.md
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
    title: Pourquoi remplacer Feu avant a temps ?
  symptoms:
  - eclairage insuffisant nuit malgre ampoules
  - phare qui ne s allume plus ou par intermittence
  - condensation ou eau a l interieur du bloc optique
  - reglage impossible phares faisceau toujours
  - odeur de plastique brule au niveau du phare
  - phare opaque couleur jaunie reduisant
  - grincement ou bruit metallique du reglage de phare
  - perte luminosite progressive meme ampoules
  - '**Grincement ou bruit metallique du reglage de phare**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 259
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: feu-avant
source_type: gamme
symptoms:
- description: eclairage insuffisant nuit malgre ampoules
  evidence:
  - 'Observation: eclairage insuffisant nuit malgre ampoules'
  - Vérification visuelle ou auditive
  id: S1
  label: Eclairage insuffisant nuit malgre ampoules
  risk_level: confort
- description: phare qui ne s allume plus ou par intermittence
  evidence:
  - 'Observation: phare qui ne s allume plus ou par intermittence'
  - Vérification visuelle ou auditive
  id: S2
  label: Phare qui ne s allume plus ou par intermittence
  risk_level: confort
- description: condensation ou eau a l interieur du bloc optique
  evidence:
  - 'Observation: condensation ou eau a l interieur du bloc optique'
  - Vérification visuelle ou auditive
  id: S3
  label: Condensation ou eau a l interieur du bloc optique
  risk_level: confort
- description: reglage impossible phares faisceau toujours
  evidence:
  - 'Observation: reglage impossible phares faisceau toujours'
  - Vérification visuelle ou auditive
  id: S4
  label: Reglage impossible phares faisceau toujours
  risk_level: confort
- description: odeur de plastique brule au niveau du phare
  evidence:
  - 'Observation: odeur de plastique brule au niveau du phare'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de plastique brule au niveau du phare
  risk_level: confort
- description: phare opaque couleur jaunie reduisant
  evidence:
  - 'Observation: phare opaque couleur jaunie reduisant'
  - Vérification visuelle ou auditive
  id: S6
  label: Phare opaque couleur jaunie reduisant
  risk_level: confort
- description: grincement ou bruit metallique du reglage de phare
  evidence:
  - 'Observation: grincement ou bruit metallique du reglage de phare'
  - Vérification visuelle ou auditive
  id: S7
  label: Grincement ou bruit metallique du reglage de phare
  risk_level: degats_volant_moteur
- description: perte luminosite progressive meme ampoules
  evidence:
  - 'Observation: perte luminosite progressive meme ampoules'
  - Vérification visuelle ou auditive
  id: S8
  label: Perte luminosite progressive meme ampoules
  risk_level: confort
title: Feu avant
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Feu avant - Guide Diagnostic Complet

## Fonction et Rôle

Éclaire la route devant le véhicule

**Actions principales:** eclairer, illuminer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Grincement ou bruit metallique du reglage de phare**
  grincement ou bruit metallique du reglage de phare

### 🟢 Autres Symptômes

- eclairage insuffisant nuit malgre ampoules
- phare qui ne s allume plus ou par intermittence
- condensation ou eau a l interieur du bloc optique
- reglage impossible phares faisceau toujours
- odeur de plastique brule au niveau du phare
- phare opaque couleur jaunie reduisant

## Procédure de Diagnostic

Pour diagnostiquer un problème de feu avant:

1. **Inspection visuelle** - Examiner l'état du feu avant
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- ampoule-feu-avant
- commande-d-eclairage
- feu-arriere
- feu-clignotant

## Critères de Compatibilité

Pour commander le bon feu avant, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure visibilité garantie"