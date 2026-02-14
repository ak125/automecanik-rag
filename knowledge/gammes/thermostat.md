---
category: refroidissement
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
  - reguler
  - ouvrir
  - fermer
  must_not_contain_concepts:
  - sonde
  - capteur
  - electronique
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Reguler le flux de liquide de refroidissement selon la temperature
    moteur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "evite la casse moteur"
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
    question: Comment choisir Thermostat compatible avec mon vehicule ?
  - answer: En cas de aiguille de temperature dans le rouge rapidement ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Thermostat ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Thermostat sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Thermostat.
  id: 316
  intro:
    role: Reguler le flux de liquide de refroidissement selon la temperature moteur
    syncParts:
    - reguler
    - ouvrir
    - fermer
    title: A quoi sert Thermostat ?
  pgId: '316'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/thermostat.md
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
    title: Pourquoi remplacer Thermostat a temps ?
  symptoms:
  - aiguille de temperature dans le rouge rapidement
  - moteur qui ne chauffe jamais aiguille basse
  - sifflement ou vapeur s echappant du capot
  - chauffage qui reste froid tres longtemps
  - odeur de liquide de refroidissement en surchauffe
  - plus de 100 000 km sans remplacement
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 316
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: thermostat
source_type: gamme
symptoms:
- description: aiguille de temperature dans le rouge rapidement
  evidence:
  - 'Observation: aiguille de temperature dans le rouge rapidement'
  - Vérification visuelle ou auditive
  id: S1
  label: Aiguille de temperature dans le rouge rapidement
  risk_level: confort
- description: moteur qui ne chauffe jamais aiguille basse
  evidence:
  - 'Observation: moteur qui ne chauffe jamais aiguille basse'
  - Vérification visuelle ou auditive
  id: S2
  label: Moteur qui ne chauffe jamais aiguille basse
  risk_level: confort
- description: sifflement ou vapeur s echappant du capot
  evidence:
  - 'Observation: sifflement ou vapeur s echappant du capot'
  - Vérification visuelle ou auditive
  id: S3
  label: Sifflement ou vapeur s echappant du capot
  risk_level: confort
- description: chauffage qui reste froid tres longtemps
  evidence:
  - 'Observation: chauffage qui reste froid tres longtemps'
  - Vérification visuelle ou auditive
  id: S4
  label: Chauffage qui reste froid tres longtemps
  risk_level: confort
- description: odeur de liquide de refroidissement en surchauffe
  evidence:
  - 'Observation: odeur de liquide de refroidissement en surchauffe'
  - Vérification visuelle ou auditive
  id: S5
  label: Odeur de liquide de refroidissement en surchauffe
  risk_level: confort
- description: plus de 100 000 km sans remplacement
  evidence:
  - 'Observation: plus de 100 000 km sans remplacement'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 100 000 km sans remplacement
  risk_level: confort
title: Thermostat
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Thermostat - Guide Diagnostic Complet

## Fonction et Rôle

Reguler le flux de liquide de refroidissement selon la temperature moteur

**Actions principales:** reguler, ouvrir, fermer, controler le flux

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- aiguille de temperature dans le rouge rapidement
- moteur qui ne chauffe jamais aiguille basse
- sifflement ou vapeur s echappant du capot
- chauffage qui reste froid tres longtemps
- odeur de liquide de refroidissement en surchauffe
- plus de 100 000 km sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de thermostat:

1. **Inspection visuelle** - Examiner l'état du thermostat
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- durite-de-refroidissement
- pompe-a-eau
- radiateur-de-refroidissement
- sonde-de-refroidissement
- vase-d-expansion
- ventilateur-de-refroidissement

## Critères de Compatibilité

Pour commander le bon thermostat, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "evite la casse moteur"