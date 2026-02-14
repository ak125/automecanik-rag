---
category: distribution
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
  confusion_with: {}
  must_be_true:
  - entrainer
  - transmettre
  must_not_contain_concepts:
  - freinage
  - climatisation
  - turbo
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Entraîne les accessoires moteur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de puissance"
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
    question: Comment choisir Courroie d'accessoire compatible avec mon vehicule ?
  - answer: En cas de sifflement au demarrage ou a l acceleration ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Courroie d'accessoire ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Courroie d'accessoire sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Courroie d'accessoire.
  id: 10
  intro:
    role: Courroie d'accessoire intervient directement sur compatibilite du vehicule.
      Un choix conforme protege la securite et limite les pannes secondaires.
    syncParts:
    - entrainer
    - transmettre
    title: A quoi sert Courroie d'accessoire ?
  pgId: '10'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/courroie-d-accessoire.md
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
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Courroie d'accessoire a temps ?
  symptoms:
  - sifflement au demarrage ou a l acceleration
  - courroie fissuree ou effilochee visible
  - voyant batterie allume alternateur non entraine
  - perte de direction assistee si sur meme courroie
  - odeur de caoutchouc brule
  - plus de 60 000 km ou 5 ans depuis le remplacement
  - '**Perte de direction assistee si sur meme courroie**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 10
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: courroie-d-accessoire
source_type: gamme
symptoms:
- description: sifflement au demarrage ou a l acceleration
  evidence:
  - 'Observation: sifflement au demarrage ou a l acceleration'
  - Vérification visuelle ou auditive
  id: S1
  label: Sifflement au demarrage ou a l acceleration
  risk_level: confort
- description: courroie fissuree ou effilochee visible
  evidence:
  - 'Observation: courroie fissuree ou effilochee visible'
  - Vérification visuelle ou auditive
  id: S2
  label: Courroie fissuree ou effilochee visible
  risk_level: confort
- description: voyant batterie allume alternateur non entraine
  evidence:
  - 'Observation: voyant batterie allume alternateur non entraine'
  - Vérification visuelle ou auditive
  id: S3
  label: Voyant batterie allume alternateur non entraine
  risk_level: confort
- description: perte de direction assistee si sur meme courroie
  evidence:
  - 'Observation: perte de direction assistee si sur meme courroie'
  - Vérification visuelle ou auditive
  id: S4
  label: Perte de direction assistee si sur meme courroie
  risk_level: securite
- description: odeur de caoutchouc brule
  evidence:
  - 'Observation: odeur de caoutchouc brule'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de caoutchouc brule
  risk_level: confort
- description: plus de 60 000 km ou 5 ans depuis le remplacement
  evidence:
  - 'Observation: plus de 60 000 km ou 5 ans depuis le remplacement'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 60 000 km ou 5 ans depuis le remplacement
  risk_level: confort
title: Courroie d'accessoire
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Courroie d'accessoire - Guide Diagnostic Complet

## Fonction et Rôle

Entraîne les accessoires moteur

**Actions principales:** entrainer, transmettre

## Symptômes de Défaillance

### 🟡 Symptômes de Sécurité

- **Perte de direction assistee si sur meme courroie**
  perte de direction assistee si sur meme courroie

### 🟢 Autres Symptômes

- sifflement au demarrage ou a l acceleration
- courroie fissuree ou effilochee visible
- voyant batterie allume alternateur non entraine
- odeur de caoutchouc brule
- plus de 60 000 km ou 5 ans depuis le remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de courroie d'accessoire:

1. **Inspection visuelle** - Examiner l'état du courroie d'accessoire
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- compresseur-de-climatisation
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- pompe-a-eau
- pompe-de-direction-assistee
- poulie-d-alternateur
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon courroie d'accessoire, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "plus de puissance"