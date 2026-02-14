---
category: electrique
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
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
  confusion_with:
    batterie:
      key_difference: Alternateur recharge la batterie, si batterie HS l'alternateur
        ne peut compenser
    demarreur:
      key_difference: Alternateur = recharge batterie (moteur tournant), Démarreur
        = lance le moteur (au démarrage)
  must_be_true:
  - recharger
  - alimenter
  - fournir du courant
  must_not_contain_concepts:
  - demarrage
  - demarreur
  - lancer le moteur
  - rotation initiale
  - neiman
  - universel
  - tous modèles
  - adaptable tous
  role_summary: Recharger la batterie et alimenter les equipements electriques du
    vehicule moteur tournant
page_contract:
  antiMistakes:
  - ❌ "zéro panne électrique"
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
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
    question: Comment choisir Alternateur compatible avec mon vehicule ?
  - answer: En cas de voyant batterie allume moteur tournant ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Alternateur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Alternateur sans verification atelier ?
  howToChoose: Renseignez marque, modele, motorisation, type puis comparez references
    et dimensions. Validez ensuite les contraintes de electrique pour confirmer Alternateur.
  id: 4
  intro:
    role: Recharger la batterie et alimenter les equipements electriques du vehicule
      moteur tournant
    syncParts:
    - recharger
    - alimenter
    - fournir du courant
    title: A quoi sert Alternateur ?
  pgId: '4'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/alternateur.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant
      électronique'
    - ❌ "zéro panne électrique"
    - ❌ "homologué CT"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Alternateur a temps ?
  symptoms:
  - voyant batterie allume moteur tournant
  - batterie qui se decharge malgre les trajets
  - phares qui faiblissent ou clignotent
  - sifflement de la courroie d accessoire
  - odeur de courroie brulee ou d electrique
  - plus de 150 000 km ou tension de charge basse
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - adaptable tous
  requires_vehicle: true
slug: alternateur
source_type: gamme
subcategory: charge
symptoms:
- description: voyant batterie allume moteur tournant
  evidence:
  - 'Observation: voyant batterie allume moteur tournant'
  - Vérification visuelle ou auditive
  id: S1
  label: Voyant batterie allume moteur tournant
  risk_level: confort
- description: batterie qui se decharge malgre les trajets
  evidence:
  - 'Observation: batterie qui se decharge malgre les trajets'
  - Vérification visuelle ou auditive
  id: S2
  label: Batterie qui se decharge malgre les trajets
  risk_level: confort
- description: phares qui faiblissent ou clignotent
  evidence:
  - 'Observation: phares qui faiblissent ou clignotent'
  - Vérification visuelle ou auditive
  id: S3
  label: Phares qui faiblissent ou clignotent
  risk_level: confort
- description: sifflement de la courroie d accessoire
  evidence:
  - 'Observation: sifflement de la courroie d accessoire'
  - Vérification visuelle ou auditive
  id: S4
  label: Sifflement de la courroie d accessoire
  risk_level: confort
- description: odeur de courroie brulee ou d electrique
  evidence:
  - 'Observation: odeur de courroie brulee ou d electrique'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de courroie brulee ou d electrique
  risk_level: confort
- description: plus de 150 000 km ou tension de charge basse
  evidence:
  - 'Observation: plus de 150 000 km ou tension de charge basse'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 150 000 km ou tension de charge basse
  risk_level: confort
title: Alternateur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Alternateur - Guide Diagnostic Complet

## Fonction et Rôle

Recharger la batterie et alimenter les equipements electriques du vehicule moteur tournant

**Actions principales:** recharger, alimenter, fournir du courant, maintenir la charge, produire de lelectricite

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant batterie allume moteur tournant
- batterie qui se decharge malgre les trajets
- phares qui faiblissent ou clignotent
- sifflement de la courroie d accessoire
- odeur de courroie brulee ou d electrique
- plus de 150 000 km ou tension de charge basse

## Procédure de Diagnostic

Pour diagnostiquer un problème de alternateur:

1. **Inspection visuelle** - Examiner l'état du alternateur
2. **Test électrique** - Vérifier la tension et les connexions
3. **Lecture codes défaut** - Scanner OBD si voyant allumé
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- demarreur
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- poulie-d-alternateur
- poulie-vilebrequin

## ⚠️ Ne Pas Confondre Avec

### demarreur
**Distinction:** Alternateur = recharge batterie (moteur tournant), Démarreur = lance le moteur (au démarrage)

### batterie
**Distinction:** Alternateur recharge la batterie, si batterie HS l'alternateur ne peut compenser

## Critères de Compatibilité

Pour commander le bon alternateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "zéro panne électrique"
- ❌ "homologué CT"
- ❌ "sécurité garantie"