---
category: distribution
diagnostic_tree:
- if: bruit_anormal_detecte
  then: localiser_source_et_verifier_usure_mecanique
- if: vibrations_anormales
  then: verifier_equilibrage_et_fixations
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
  role_summary: Transmet le mouvement à l'alternateur
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "meilleure charge"
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
    question: Comment choisir Poulie d'alternateur compatible avec mon vehicule ?
  - answer: En cas de sifflement aigu au demarrage a froid ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Poulie d'alternateur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Poulie d'alternateur sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Poulie d'alternateur.
  id: 1108
  intro:
    role: Poulie d'alternateur intervient directement sur compatibilite du vehicule.
      Un choix conforme protege la securite et limite les pannes secondaires.
    syncParts:
    - entrainer
    - transmettre
    title: A quoi sert Poulie d'alternateur ?
  pgId: '1108'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/poulie-d-alternateur.md
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
    title: Pourquoi remplacer Poulie d'alternateur a temps ?
  symptoms:
  - sifflement aigu au demarrage a froid
  - courroie d accessoire qui saute ou patine
  - vibrations moteur au ralenti
  - bruit de roulement au niveau de l alternateur
  - alternateur qui charge mal par intermittence
  - plus de 120 000 km sans remplacement
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 1108
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: poulie-d-alternateur
source_type: gamme
symptoms:
- description: sifflement aigu au demarrage a froid
  evidence:
  - 'Observation: sifflement aigu au demarrage a froid'
  - Vérification visuelle ou auditive
  id: S1
  label: Sifflement aigu au demarrage a froid
  risk_level: confort
- description: courroie d accessoire qui saute ou patine
  evidence:
  - 'Observation: courroie d accessoire qui saute ou patine'
  - Vérification visuelle ou auditive
  id: S2
  label: Courroie d accessoire qui saute ou patine
  risk_level: confort
- description: vibrations moteur au ralenti
  evidence:
  - 'Observation: vibrations moteur au ralenti'
  - Vérification visuelle ou auditive
  id: S3
  label: Vibrations moteur au ralenti
  risk_level: confort
- description: bruit de roulement au niveau de l alternateur
  evidence:
  - 'Observation: bruit de roulement au niveau de l alternateur'
  - Vérification visuelle ou auditive
  id: S4
  label: Bruit de roulement au niveau de l alternateur
  risk_level: confort
- description: alternateur qui charge mal par intermittence
  evidence:
  - 'Observation: alternateur qui charge mal par intermittence'
  - Vérification visuelle ou auditive
  id: S5
  label: Alternateur qui charge mal par intermittence
  risk_level: confort
- description: plus de 120 000 km sans remplacement
  evidence:
  - 'Observation: plus de 120 000 km sans remplacement'
  - Vérification visuelle ou auditive
  id: S6
  label: Plus de 120 000 km sans remplacement
  risk_level: confort
title: Poulie d'alternateur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Poulie d'alternateur - Guide Diagnostic Complet

## Fonction et Rôle

Transmet le mouvement à l'alternateur

**Actions principales:** entrainer, transmettre

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- sifflement aigu au demarrage a froid
- courroie d accessoire qui saute ou patine
- vibrations moteur au ralenti
- bruit de roulement au niveau de l alternateur
- alternateur qui charge mal par intermittence
- plus de 120 000 km sans remplacement

## Procédure de Diagnostic

Pour diagnostiquer un problème de poulie d'alternateur:

1. **Inspection visuelle** - Examiner l'état du poulie d'alternateur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Usure normale** - Après un certain kilométrage, le remplacement préventif est recommandé

## Pièces Associées

Lors du remplacement, vérifier également:

- alternateur
- courroie-d-accessoire
- galet-enrouleur-de-courroie-d-accessoire
- galet-tendeur-de-courroie-d-accessoire
- poulie-vilebrequin

## Critères de Compatibilité

Pour commander le bon poulie d'alternateur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "meilleure charge"