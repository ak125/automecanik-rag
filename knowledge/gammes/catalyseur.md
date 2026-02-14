---
category: echappement
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
  - transformer
  - convertir
  - reduire
  must_not_contain_concepts:
  - fap
  - filtre a particules
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  role_summary: Transforme les gaz polluants (CO, HC, NOx) en gaz moins nocifs par
    réaction chimique
page_contract:
  antiMistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "passe le controle technique"
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
    question: Comment choisir Catalyseur compatible avec mon vehicule ?
  - answer: En cas de voyant moteur allume codes p0420 p0430 ou de degradation mesurable,
      il faut controler rapidement avant panne secondaire.
    question: Quand remplacer Catalyseur ?
  - answer: Le montage peut exiger controles de couple, alignement et references.
      En cas de doute, appliquez la procedure constructeur.
    question: Puis-je monter Catalyseur sans verification atelier ?
  howToChoose: Renseignez marque, modele, type puis comparez references et dimensions.
    Validez ensuite les contraintes de compatibilite pour confirmer Catalyseur.
  id: 429
  intro:
    role: Transforme les gaz polluants (CO, HC, NOx) en gaz moins nocifs par réaction
      chimique
    syncParts:
    - transformer
    - convertir
    - reduire
    title: A quoi sert Catalyseur ?
  pgId: '429'
  quality:
    flags:
    - FAQ_TOO_SMALL
    - TOO_SHORT
    score: 76
    source: reindex:gammes/catalyseur.md
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
    title: Pourquoi remplacer Catalyseur a temps ?
  symptoms:
  - voyant moteur allume codes p0420 p0430
  - perte de puissance progressive du moteur
  - bruit metallique de ferraille sous le vehicule
  - odeur d uf pourri soufre a l echappement
  - echec au controle technique pollution
  - surconsommation de carburant
  - '**Bruit metallique de ferraille sous le vehicule**'
  timing:
    km: Controle a chaque revision constructeur
    note: Ne pas attendre la panne complete pour intervenir.
    title: Quand intervenir ?
    years: Controle annuel recommande
pg_id: 429
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
slug: catalyseur
source_type: gamme
symptoms:
- description: voyant moteur allume codes p0420 p0430
  evidence:
  - 'Observation: voyant moteur allume codes p0420 p0430'
  - Vérification visuelle ou auditive
  id: S1
  label: Voyant moteur allume codes p0420 p0430
  risk_level: confort
- description: perte de puissance progressive du moteur
  evidence:
  - 'Observation: perte de puissance progressive du moteur'
  - Vérification visuelle ou auditive
  id: S2
  label: Perte de puissance progressive du moteur
  risk_level: confort
- description: bruit metallique de ferraille sous le vehicule
  evidence:
  - 'Observation: bruit metallique de ferraille sous le vehicule'
  - Vérification visuelle ou auditive
  id: S3
  label: Bruit metallique de ferraille sous le vehicule
  risk_level: degats_volant_moteur
- description: odeur d uf pourri soufre a l echappement
  evidence:
  - 'Observation: odeur d uf pourri soufre a l echappement'
  - Vérification visuelle ou auditive
  id: S4
  label: Odeur d uf pourri soufre a l echappement
  risk_level: confort
- description: echec au controle technique pollution
  evidence:
  - 'Observation: echec au controle technique pollution'
  - Vérification visuelle ou auditive
  id: S5
  label: Echec au controle technique pollution
  risk_level: confort
- description: surconsommation de carburant
  evidence:
  - 'Observation: surconsommation de carburant'
  - Vérification visuelle ou auditive
  id: S6
  label: Surconsommation de carburant
  risk_level: confort
title: Catalyseur
truth_level: L2
updated_at: '2026-01-14'
verification_status: draft
---

# Catalyseur - Guide Diagnostic Complet

## Fonction et Rôle

Transforme les gaz polluants (CO, HC, NOx) en gaz moins nocifs par réaction chimique

**Actions principales:** transformer, convertir, reduire, traiter

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit metallique de ferraille sous le vehicule**
  bruit metallique de ferraille sous le vehicule

### 🟢 Autres Symptômes

- voyant moteur allume codes p0420 p0430
- perte de puissance progressive du moteur
- odeur d uf pourri soufre a l echappement
- echec au controle technique pollution
- surconsommation de carburant

## Procédure de Diagnostic

Pour diagnostiquer un problème de catalyseur:

1. **Inspection visuelle** - Examiner l'état du catalyseur
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- capteur-temperature-d-air-admission
- fap
- sonde-lambda
- tube-d-echappement
- vanne-egr

## Critères de Compatibilité

Pour commander le bon catalyseur, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "passe le controle technique"