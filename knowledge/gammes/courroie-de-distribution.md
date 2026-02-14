---
category: distribution
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
doc_family: catalog
entity_type: gamme
intent_targets:
- diagnostic
- achat
- compatibilite
mechanical_rules:
  confusion_with:
    chaine-de-distribution:
      key_difference: Courroie = caoutchouc à remplacer, Chaîne = métal plus durable
    courroie-d-accessoire:
      key_difference: Courroie distribution = synchronise moteur (CRITIQUE), Courroie
        accessoire = alternateur/clim (moins critique)
  must_be_true:
  - synchroniser
  - entrainer
  - maintenir
  must_not_contain_concepts:
  - chaine
  - universel
  - tous moteurs
  - adaptable
  role_summary: Kit complet pour la synchronisation de la distribution avec tous les
    composants necessaires
page_contract:
  antiMistakes:
  - ❌ "évite la casse moteur"
  - ❌ "sécurité garantie"
  - ❌ "garanti CT"
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
    question: Comment choisir Courroie de distribution compatible avec mon vehicule
      ?
  - answer: En cas de aucun symptome visible courroie casse ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Courroie de distribution ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Courroie de distribution sans verification atelier ?
  howToChoose: Renseignez marque, modele, motorisation, type puis comparez references
    et dimensions. Validez ensuite les contraintes de compatibilite pour confirmer
    Courroie de distribution.
  id: 306
  intro:
    role: Kit complet pour la synchronisation de la distribution avec tous les composants
      necessaires
    syncParts:
    - synchroniser
    - entrainer
    - maintenir
    title: A quoi sert Courroie de distribution ?
  pgId: '306'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/courroie-de-distribution.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Défaillance progressive** - Usure normale due à l''utilisation'
    - '**Conditions d''utilisation** - Sollicitations excessives ou environnement
      défavorable'
    - ❌ "évite la casse moteur"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Courroie de distribution a temps ?
  symptoms:
  - aucun symptome visible courroie casse
  - echeance kilometrique ou temps depassee
  - traces de craquelures sur la courroie si visible
  - bruit de claquement cote distribution
  - fuite de liquide de refroidissement pompe a eau
  - jeu dans le galet tendeur
  - courroie effilochee sur les bords
  - '**Aucun symptome visible courroie casse**'
  - '**Bruit de claquement cote distribution**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 306
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous moteurs
  - adaptable
  requires_vehicle: true
slug: courroie-de-distribution
source_type: gamme
symptoms:
- description: aucun symptome visible courroie casse
  evidence:
  - 'Observation: aucun symptome visible courroie casse'
  - Vérification visuelle ou auditive
  id: S1
  label: Aucun symptome visible courroie casse
  risk_level: degats_volant_moteur
- description: echeance kilometrique ou temps depassee
  evidence:
  - 'Observation: echeance kilometrique ou temps depassee'
  - Vérification visuelle ou auditive
  id: S2
  label: Echeance kilometrique ou temps depassee
  risk_level: confort
- description: traces de craquelures sur la courroie si visible
  evidence:
  - 'Observation: traces de craquelures sur la courroie si visible'
  - Vérification visuelle ou auditive
  id: S3
  label: Traces de craquelures sur la courroie si visible
  risk_level: confort
- description: bruit de claquement cote distribution
  evidence:
  - 'Observation: bruit de claquement cote distribution'
  - Vérification visuelle ou auditive
  id: S4
  label: Bruit de claquement cote distribution
  risk_level: degats_volant_moteur
- description: fuite de liquide de refroidissement pompe a eau
  evidence:
  - 'Observation: fuite de liquide de refroidissement pompe a eau'
  - Vérification visuelle ou auditive
  id: S5
  label: Fuite de liquide de refroidissement pompe a eau
  risk_level: confort
- description: jeu dans le galet tendeur
  evidence:
  - 'Observation: jeu dans le galet tendeur'
  - Vérification visuelle ou auditive
  id: S6
  label: Jeu dans le galet tendeur
  risk_level: confort
- description: courroie effilochee sur les bords
  evidence:
  - 'Observation: courroie effilochee sur les bords'
  - Vérification visuelle ou auditive
  id: S7
  label: Courroie effilochee sur les bords
  risk_level: confort
title: Courroie de distribution
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Courroie de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Kit complet pour la synchronisation de la distribution avec tous les composants necessaires

**Actions principales:** synchroniser, entrainer, maintenir

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Aucun symptome visible courroie casse**
  aucun symptome visible courroie casse
- **Bruit de claquement cote distribution**
  bruit de claquement cote distribution

### 🟢 Autres Symptômes

- echeance kilometrique ou temps depassee
- traces de craquelures sur la courroie si visible
- fuite de liquide de refroidissement pompe a eau
- jeu dans le galet tendeur
- courroie effilochee sur les bords

## Procédure de Diagnostic

Pour diagnostiquer un problème de courroie de distribution:

1. **Inspection visuelle** - Examiner l'état du courroie de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- kit-de-distribution
- pompe-a-eau
- poulie-d-arbre-a-came
- poulie-vilebrequin

## ⚠️ Ne Pas Confondre Avec

### courroie-d-accessoire
**Distinction:** Courroie distribution = synchronise moteur (CRITIQUE), Courroie accessoire = alternateur/clim (moins critique)

### chaine-de-distribution
**Distinction:** Courroie = caoutchouc à remplacer, Chaîne = métal plus durable

## Critères de Compatibilité

Pour commander le bon courroie de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Motorisation** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "évite la casse moteur"
- ❌ "sécurité garantie"
- ❌ "garanti CT"