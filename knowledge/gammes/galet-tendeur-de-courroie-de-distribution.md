---
category: distribution
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
  - tendre
  - maintenir
  - ajuster
  must_not_contain_concepts:
  - freinage
  - climatisation
  - turbo
  - injection
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Maintenir la tension de la courroie de distribution
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "synchronisation parfaite"
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
    question: Comment choisir Galet tendeur de courroie de distribution compatible
      avec mon vehicule ?
  - answer: En cas de sifflement ou couinement cote distribution ou de degradation
      mesurable, il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Galet tendeur de courroie de distribution ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Galet tendeur de courroie de distribution sans verification
      atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Galet tendeur
    de courroie de distribution.
  id: 308
  intro:
    role: Maintenir la tension de la courroie de distribution
    syncParts:
    - tendre
    - maintenir
    - ajuster
    title: A quoi sert Galet tendeur de courroie de distribution ?
  pgId: '308'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/galet-tendeur-de-courroie-de-distribution.md
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
    title: Pourquoi remplacer Galet tendeur de courroie de distribution a temps ?
  symptoms:
  - sifflement ou couinement cote distribution
  - bruit de roulement au ralenti
  - jeu excessif dans le galet controle main
  - traces de rouille sur le galet
  - bruit qui varie avec le regime moteur
  - grincement au demarrage a froid
  - courroie qui saute cas extreme
  - '**Grincement au demarrage a froid**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 308
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: galet-tendeur-de-courroie-de-distribution
source_type: gamme
symptoms:
- description: sifflement ou couinement cote distribution
  evidence:
  - 'Observation: sifflement ou couinement cote distribution'
  - Vérification visuelle ou auditive
  id: S1
  label: Sifflement ou couinement cote distribution
  risk_level: confort
- description: bruit de roulement au ralenti
  evidence:
  - 'Observation: bruit de roulement au ralenti'
  - Vérification visuelle ou auditive
  id: S2
  label: Bruit de roulement au ralenti
  risk_level: confort
- description: jeu excessif dans le galet controle main
  evidence:
  - 'Observation: jeu excessif dans le galet controle main'
  - Vérification visuelle ou auditive
  id: S3
  label: Jeu excessif dans le galet controle main
  risk_level: confort
- description: traces de rouille sur le galet
  evidence:
  - 'Observation: traces de rouille sur le galet'
  - Vérification visuelle ou auditive
  id: S4
  label: Traces de rouille sur le galet
  risk_level: confort
- description: bruit qui varie avec le regime moteur
  evidence:
  - 'Observation: bruit qui varie avec le regime moteur'
  - Vérification visuelle ou auditive
  id: S5
  label: Bruit qui varie avec le regime moteur
  risk_level: confort
- description: grincement au demarrage a froid
  evidence:
  - 'Observation: grincement au demarrage a froid'
  - Vérification visuelle ou auditive
  id: S6
  label: Grincement au demarrage a froid
  risk_level: degats_volant_moteur
- description: courroie qui saute cas extreme
  evidence:
  - 'Observation: courroie qui saute cas extreme'
  - Vérification visuelle ou auditive
  id: S7
  label: Courroie qui saute cas extreme
  risk_level: confort
title: Galet tendeur de courroie de distribution
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Galet tendeur de courroie de distribution - Guide Diagnostic Complet

## Fonction et Rôle

Maintenir la tension de la courroie de distribution

**Actions principales:** tendre, maintenir, ajuster

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Grincement au demarrage a froid**
  grincement au demarrage a froid

### 🟢 Autres Symptômes

- sifflement ou couinement cote distribution
- bruit de roulement au ralenti
- jeu excessif dans le galet controle main
- traces de rouille sur le galet
- bruit qui varie avec le regime moteur
- courroie qui saute cas extreme

## Procédure de Diagnostic

Pour diagnostiquer un problème de galet tendeur de courroie de distribution:

1. **Inspection visuelle** - Examiner l'état du galet tendeur de courroie de distribution
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- courroie-de-distribution

## Critères de Compatibilité

Pour commander le bon galet tendeur de courroie de distribution, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "synchronisation parfaite"