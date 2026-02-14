---
category: distribution
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: fuite_detectee_ou_niveau_bas
  then: identifier_origine_fuite_et_verifier_joints
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
  - synchroniser
  - entrainer
  - guider
  must_not_contain_concepts:
  - courroie
  - caoutchouc
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Kit complet pour la distribution a chaine avec tous les composants
    (tendeur, patins, glissieres)
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
    question: Comment choisir Kit de distribution compatible avec mon vehicule ?
  - answer: En cas de echeance kilometrique ou temps atteinte ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Kit de distribution ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Kit de distribution sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Kit de distribution.
  id: 307
  intro:
    role: Kit complet pour la distribution a chaine avec tous les composants (tendeur,
      patins, glissieres)
    syncParts:
    - synchroniser
    - entrainer
    - guider
    title: A quoi sert Kit de distribution ?
  pgId: '307'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/kit-de-distribution.md
    version: GammeContentContract.v1
  risk:
    conclusion: Un diagnostic precoce reduit le risque technique et financier.
    consequences:
    - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants
      internes'
    - '**Usure normale** - Après un certain kilométrage, le remplacement préventif
      est recommandé'
    - ❌ "homologué CT"
    - ❌ "sécurité garantie"
    costRange: 120 a 1200 EUR selon vehicule et niveau de panne.
    explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des
      composants internes'
    title: Pourquoi remplacer Kit de distribution a temps ?
  symptoms:
  - echeance kilometrique ou temps atteinte
  - bruit de roulement cote distribution galet
  - fuite de liquide de refroidissement pompe a eau
  - sifflement au ralenti cote courroie
  - jeu dans les galets controle visuel
  - traces d usure sur la courroie
  - grincement au demarrage a froid
  - '**Grincement au demarrage a froid**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 307
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: kit-de-distribution
source_type: gamme
symptoms:
- description: echeance kilometrique ou temps atteinte
  evidence:
  - 'Observation: echeance kilometrique ou temps atteinte'
  - Vérification visuelle ou auditive
  id: S1
  label: Echeance kilometrique ou temps atteinte
  risk_level: confort
- description: bruit de roulement cote distribution galet
  evidence:
  - 'Observation: bruit de roulement cote distribution galet'
  - Vérification visuelle ou auditive
  id: S2
  label: Bruit de roulement cote distribution galet
  risk_level: confort
- description: fuite de liquide de refroidissement pompe a eau
  evidence:
  - 'Observation: fuite de liquide de refroidissement pompe a eau'
  - Vérification visuelle ou auditive
  id: S3
  label: Fuite de liquide de refroidissement pompe a eau
  risk_level: confort
- description: sifflement au ralenti cote courroie
  evidence:
  - 'Observation: sifflement au ralenti cote courroie'
  - Vérification visuelle ou auditive
  id: S4
  label: Sifflement au ralenti cote courroie
  risk_level: confort
- description: jeu dans les galets controle visuel
  evidence:
  - 'Observation: jeu dans les galets controle visuel'
  - Vérification visuelle ou auditive
  id: S5
  label: Jeu dans les galets controle visuel
  risk_level: confort
- description: traces d usure sur la courroie
  evidence:
  - 'Observation: traces d usure sur la courroie'
  - Vérification visuelle ou auditive
  id: S6
  label: Traces d usure sur la courroie
  risk_level: confort
- description: grincement au demarrage a froid
  evidence:
  - 'Observation: grincement au demarrage a froid'
  - Vérification visuelle ou auditive
  id: S7
  label: Grincement au demarrage a froid
  risk_level: degats_volant_moteur
title: Kit de distribution
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Kit de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Kit complet pour la distribution a chaine avec tous les composants (tendeur, patins, glissieres)

**Actions principales:** synchroniser, entrainer, guider

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Grincement au demarrage a froid**
  grincement au demarrage a froid

### 🟢 Autres Symptômes

- echeance kilometrique ou temps atteinte
- bruit de roulement cote distribution galet
- fuite de liquide de refroidissement pompe a eau
- sifflement au ralenti cote courroie
- jeu dans les galets controle visuel
- traces d usure sur la courroie

## Procédure de Diagnostic

Pour diagnostiquer un problème de kit de distribution:

1. **Inspection visuelle** - Examiner l'état du kit de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-d-accessoire
- pompe-a-eau
- poulie-d-arbre-a-came
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon kit de distribution, vous devez connaître:

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