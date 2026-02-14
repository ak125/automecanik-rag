---
category: climatisation
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
  - filtrer
  - assecher
  - retenir l'humidite
  must_not_contain_concepts:
  - injection
  - freinage
  - allumage
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Filtre et assèche le fluide frigorigène
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "refroidit le moteur"
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
    question: Comment choisir Bouteille déshydratante compatible avec mon vehicule
      ?
  - answer: En cas de circuit de clim ouvert recemment intervention ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Bouteille déshydratante ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Bouteille déshydratante sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de climatisation pour confirmer Bouteille déshydratante.
  id: 851
  intro:
    role: Bouteille déshydratante intervient directement sur climatisation du vehicule.
      Un choix conforme protege la froid et limite les pannes secondaires.
    syncParts:
    - filtrer
    - assecher
    - retenir l'humidite
    title: A quoi sert Bouteille déshydratante ?
  pgId: '851'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/bouteille-deshydratante.md
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
    title: Pourquoi remplacer Bouteille déshydratante a temps ?
  symptoms:
  - circuit de clim ouvert recemment intervention
  - clim moins performante apres une reparation
  - compresseur qui fait un bruit anormal
  - humidite visible dans le voyant du deshydrateur
  - gaz recupere trouble ou avec impuretes
  - remplacement de compresseur prevu preventif
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 851
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: bouteille-deshydratante
source_type: gamme
symptoms:
- description: circuit de clim ouvert recemment intervention
  evidence:
  - 'Observation: circuit de clim ouvert recemment intervention'
  - Vérification visuelle ou auditive
  id: S1
  label: Circuit de clim ouvert recemment intervention
  risk_level: confort
- description: clim moins performante apres une reparation
  evidence:
  - 'Observation: clim moins performante apres une reparation'
  - Vérification visuelle ou auditive
  id: S2
  label: Clim moins performante apres une reparation
  risk_level: confort
- description: compresseur qui fait un bruit anormal
  evidence:
  - 'Observation: compresseur qui fait un bruit anormal'
  - Vérification visuelle ou auditive
  id: S3
  label: Compresseur qui fait un bruit anormal
  risk_level: confort
- description: humidite visible dans le voyant du deshydrateur
  evidence:
  - 'Observation: humidite visible dans le voyant du deshydrateur'
  - Vérification visuelle ou auditive
  id: S4
  label: Humidite visible dans le voyant du deshydrateur
  risk_level: confort
- description: gaz recupere trouble ou avec impuretes
  evidence:
  - 'Observation: gaz recupere trouble ou avec impuretes'
  - Vérification visuelle ou auditive
  id: S5
  label: Gaz recupere trouble ou avec impuretes
  risk_level: confort
- description: remplacement de compresseur prevu preventif
  evidence:
  - 'Observation: remplacement de compresseur prevu preventif'
  - Vérification visuelle ou auditive
  id: S6
  label: Remplacement de compresseur prevu preventif
  risk_level: confort
title: Bouteille déshydratante
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Bouteille déshydratante - Guide Diagnostic Complet

## Fonction et Rôle

Filtre et assèche le fluide frigorigène

**Actions principales:** filtrer, assecher, retenir l'humidite

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- circuit de clim ouvert recemment intervention
- clim moins performante apres une reparation
- compresseur qui fait un bruit anormal
- humidite visible dans le voyant du deshydrateur
- gaz recupere trouble ou avec impuretes
- remplacement de compresseur prevu preventif

## Procédure de Diagnostic

Pour diagnostiquer un problème de bouteille déshydratante:

1. **Inspection visuelle** - Examiner l'état du bouteille déshydratante
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- commande-de-ventilation
- compresseur-de-climatisation
- condenseur-de-climatisation
- detendeur-de-climatisation
- evaporateur-de-climatisation
- filtre-d-habitacle
- pulseur-d-air-d-habitacle

## Critères de Compatibilité

Pour commander le bon bouteille déshydratante, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "refroidit le moteur"