---
category: alimentation
slug: pompe-a-air
title: Pompe à air
pg_id: 903
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-01'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v4_converted
  last_enriched_by: script:rag-fill-remaining-gaps
  last_enriched_at: '2026-03-28'
domain:
  role: Injecter de l'air frais dans l'echappement pour accelerer le rechauffement du catalyseur
  must_be_true:
  - insuffler
  - injecter
  - alimenter
  must_not_contain:
  - freinage
  - climatisation
  - distribution
  - embrayage
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - insuffler
  - injecter
  - alimenter
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Renseignez marque, modele, type puis comparez references et dimensions. Validez ensuite les contraintes de compatibilite
    pour confirmer Pompe à air.
  - Verifier la reference OE ou equivalence constructeur pour le vehicule exact
  - Comparer les dimensions et le type de montage avec la piece d origine
  - Choisir un equipementier reconnu pour garantir qualite et compatibilite
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "repare l'injection"
  cost_range:
    min: 200
    max: 800
    currency: EUR
    unit: l'unite
    source: catalogue automecanik
  quality_tiers:
  - tier: Origine constructeur (OE)
  - tier: Equivalent OE homologue
  - tier: Adaptable generique
  brands:
    premium:
    - Bosch
    - Delphi
    - Denso
    standard:
    - Pierburg
    - VDO
    budget:
    - Ridex
diagnostic:
  symptoms:
  - id: S1
    label: Voyant moteur au demarrage a froid
    severity: confort
  - id: S2
    label: Bruit de soufflerie anormal au demarrage
    severity: confort
  - id: S3
    label: Code defaut systeme air secondaire
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - 'Usure ou defaillance causant : voyant moteur au demarrage a froid'
  quick_checks:
  - Voyant moteur au demarrage a froid ?
  - Bruit de soufflerie anormal au demarrage ?
  - 'Observer : code defaut systeme air secondaire ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant moteur au demarrage a froid
  - Bruit de soufflerie anormal au demarrage
  - Code defaut systeme air secondaire
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '903'
  intro_title: A quoi sert Pompe à air ?
  risk_title: Pourquoi remplacer Pompe à air a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique'
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  risk_conclusion: Un diagnostic precoce reduit le risque technique et financier.
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
  - question: Comment choisir Pompe à air compatible avec mon vehicule ?
    answer: Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.
  - question: Quand remplacer Pompe à air ?
    answer: En cas de voyant moteur au demarrage a froid ou de degradation mesurable, il faut controler rapidement avant panne
      secondaire.
  - question: Puis-je monter Pompe à air sans verification atelier ?
    answer: Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure
      constructeur.
  quality:
    score: 76
    source: script:rag-upgrade-v4
    version: GammeContentContract.v4
purchase_guardrails:
  forbidden_terms:
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  requires_vehicle: true
doc_id: 463dbe16-d048-5dee-9d93-50104fe6a17e
content_hash: sha256:30a8f1b19ce329bf
lang: fr
variants:
- name: Version OE (origine)
  aliases:
  - OE
  - constructeur
  functional_differences:
  - Reference constructeur exacte
  - Garantie et compatibilite maximales
- name: Version equivalente OES
  aliases:
  - OES
  - equipementier
  functional_differences:
  - Qualite equivalente, prix aftermarket
  - Equipementier de premier monte
location_on_vehicle:
  area: Sur le vehicule (position variable selon modele)
  access: Consulter la revue technique du vehicule
  adjacent_parts:
  - pieces adjacentes du meme systeme
installation:
  difficulty: variable
  time: consulter revue technique
  tools:
  - outillage standard
  prerequisite: Consulter la procedure constructeur
---

# Pompe à air - Guide Diagnostic Complet

## Fonction et Rôle

Injecter de l'air frais dans l'echappement pour accelerer le rechauffement du catalyseur

**Actions principales:** insuffler, injecter, alimenter

## Symptômes de Défaillance

### 🟢 Autres Symptômes

- voyant moteur au demarrage a froid
- bruit de soufflerie anormal au demarrage
- code defaut systeme air secondaire

## Procédure de Diagnostic

Pour diagnostiquer un problème de pompe à air:

1. **Inspection visuelle** - Examiner l'état du pompe à air
2. **Test fonctionnel** - Vérifier le bon fonctionnement
3. **Contrôle des fixations** - Examiner les supports et raccords
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance électrique** - Problème de connexion, de câblage ou de composant électronique

## Pièces Associées

Lors du remplacement, vérifier également:

- intercooler
- soupape-d-air-secondaire
- soupape-d-aspiration-d-air-secondaire

## Critères de Compatibilité

Pour commander le bon pompe à air, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "repare l'injection"

## FAQ

**Comment choisir Pompe à air compatible avec mon vehicule ?**
Renseignez marque, modele, type moteur et annee, puis verifiez la reference exacte avant montage.

**Quand remplacer Pompe à air ?**
En cas de voyant moteur au demarrage a froid ou de degradation mesurable, il faut controler rapidement avant panne secondaire.

**Puis-je monter Pompe à air sans verification atelier ?**
Le montage peut exiger controles de couple, alignement et references. En cas de doute, appliquez la procedure constructeur.
