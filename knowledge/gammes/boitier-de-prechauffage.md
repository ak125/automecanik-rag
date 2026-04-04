---
category: allumage
slug: boitier-de-prechauffage
title: Boîtier de préchauffage
pg_id: 1750
source_type: gamme
doc_family: catalog
truth_level: L2
schema_version: '5.0'
updated_at: '2026-04-03'
verification_status: draft
intent_targets:
- diagnostic
- achat
- compatibilite
business_priority: medium
lifecycle:
  stage: v5_ssot
  last_enriched_by: script:materialize-db-to-md
  last_enriched_at: '2026-04-03'
  v5_migrated_at: '2026-03-29'
domain:
  role: Alimenter et controler les bougies de prechauffage diesel - Gere le temps et l'intensite de chauffe
  must_be_true:
  - alimenter
  - controler
  - commander
  must_not_contain:
  - essence
  - etincelle
  - haute tension
  - bobine
  - distributeur
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - alimenter
  - controler
  - commander
  confusion_with:
  - term: piece-voisine-meme-systeme
    difference: Verifier la reference exacte et la position de montage. Les pieces du meme systeme se ressemblent mais ne
      sont pas interchangeables.
selection:
  criteria:
  - Marque de votre véhicule
  - Modele de votre véhicule
  - Annee de votre véhicule
  anti_mistakes:
  - ❌ "homologué CT"
  - ❌ "sécurité garantie"
  - ❌ "zéro panne"
  - ❌ "garanti à vie"
  - ❌ "plus de puissance"
  cost_range:
    min: 15
    max: 200
    currency: EUR
    unit: l'unite
    source: estimation categorie
  quality_tiers:
  - tier: Piece d'origine (OE)
    description: Module reference constructeur, programme pour les strategies de prechauffage specifiques au moteur. Recommande
      en premier choix sur vehicules recents.
  - tier: Equipementier specialise systemes diesel
    description: Fabricants specialises en systemes de prechauffage diesel. Equivalences documentees par motorisation et annee.
      Verifier que la strategie de gestion est compatible avec le moteur.
  brands:
    premium:
    - Bosch
    - Valeo
    standard:
    - Febi
    - Meyle
    budget:
    - Ridex
    - Topran
diagnostic:
  symptoms:
  - id: S1
    label: Voyant prechauffage qui clignote ou reste allume
    severity: confort
  - id: S2
    label: Demarrage tres difficile par temps froid
    severity: confort
  - id: S3
    label: Fumee blanche excessive au demarrage a froid
    severity: confort
  - id: S4
    label: Bruit claquement diesel demarrage combustion
    severity: confort
  - id: S5
    label: Odeur de carburant non brule a l echappement
    severity: confort
  - id: S6
    label: Code defaut p0380 ou p0381 a la valise diagnostic
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - lecture codes defaut obd et diagnostic electronique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'voyant tableau bord allume : lecture codes defaut obd et diagnostic electronique'
  depose_steps: []
  quick_checks:
  - Voyant prechauffage qui clignote ou reste allume ?
  - 'Observer : demarrage tres difficile par temps froid ?'
  - 'Observer : fumee blanche excessive au demarrage a froid ?'
  - Bruit claquement diesel demarrage combustion ?
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Voyant prechauffage qui clignote ou reste allume
  - Demarrage tres difficile par temps froid
  - Fumee blanche excessive au demarrage a froid
  - Bruit claquement diesel demarrage combustion
  - Odeur de carburant non brule a l echappement
  - Code defaut p0380 ou p0381 a la valise diagnostic
  good_practices:
  - Controle visuel a chaque revision ou entretien periodique
  - Remplacement preventif si signes d usure detectes
  - Utiliser des pieces de qualite equivalente a l origine
  - Respecter les preconisations constructeur pour les intervalles
rendering:
  pgId: '1750'
  intro_title: A quoi sert Boîtier de préchauffage ?
  risk_title: Pourquoi remplacer Boîtier de préchauffage a temps ?
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
  - question: Boîtier de préchauffage OE ou adaptable ?
    answer: Privilégiez l'OE ou OES (Beru, Bosch, NGK). C'est une pièce électronique de précision qui doit résister aux cycles
      thermiques.
  - question: Comment savoir si mon boîtier de préchauffage est HS ?
    answer: Voyant préchauffage qui reste allumé ou clignote, démarrage difficile à froid, fumée blanche excessive au démarrage,
      code défaut P0380.
  - question: Tous les combien changer le boîtier de préchauffage ?
    answer: Pas de périodicité fixe. Durée de vie 150 000 à 250 000 km. À remplacer en cas de défaut avéré ou si les bougies
      neuves ne chauffent pas.
  - question: Peut-on changer le boîtier de préchauffage soi-même ?
    answer: Oui, opération accessible. Localiser le boîtier (près du moteur), débrancher la batterie, déconnecter les fils,
      dévisser. 30 min à 1h.
  - question: Quelle erreur éviter avec le boîtier de préchauffage ?
    answer: Ne pas confondre avec les bougies HS. Tester d'abord les bougies individuellement. Vérifier la masse et l'alimentation
      du boîtier avant remplacement.
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
doc_id: f46936be-9fcf-57a3-a9da-b78fb70d9973
content_hash: sha256:b95c9da14ff28a02
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
phase5_enrichment:
  _source: fr.wikipedia.org
  _validation_status: oem_verified
  _enriched_at: '2026-04-03'
  _web_files_count: 1
  _has_tech_data: true
  types_variants:
  - type: nao
    source_ref: corpus RAG web OEM
  - type: pneumatique
    source_ref: corpus RAG web OEM
  technical_notes:
    val_1954__v: 1954, v
    val_2_v: 2 V
    val_2_a: 2 a
    val_20__c: 20 °C
    val_26_a: 26 a
    val_30_kg: 30 kg
    val_5_kw: 5 kW
    val_54_a: 54 a
    val_55_a: 55 A
    val_55_v: 55 V
    val_6_v: 6 V
    val_6_5_kw: 6,5 kW
    val_72_a: 72 a
    val_84_a: 84 A
conseil_v5:
  _sync_source: __seo_gamme_conseil
  _sync_date: '2026-03-29'
  S1: 'Alimenter et controler les bougies de prechauffage diesel - Gere le temps et l''intensite de chauffe. Pièces liées
    : vérifier les composants adjacents lors du remplacement.'
  S2: 'Intervalle : selon constructeur. Symptômes de défaillance : - Voyant prechauffage qui clignote ou reste allume- Demarrage
    tres difficile par temps froid- Fumee blanche excessive au demarrage a froid- Bruit claquement diesel demarrage combustion-
    Odeur de carburant non brule a l echappement- Code defaut p0380 ou p0381 a la valise diagnostic'
  S3: 'Pour choisir le bon boîtier de préchauffage pour votre véhicule : - Marque de votre véhicule- Modele de votre véhicule-
    Annee de votre véhicule- Marques : Bosch, Valeo (premium), Febi, Meyle (standard), Ridex, Topran (budget)- Budget : 15
    à 200 EUR'
  S4_DEPOSE: 1. Débrancher la batterie. 2. Localiser la pièce selon la documentation constructeur. 3. Déconnecter les connecteurs
    électriques et raccords. 4. Dévisser les fixations de la pièce. 5. Déposer la pièce en notant l'orientation et la position
    de montage. 6. Nettoyer le logement et vérifier l'état des pièces adjacentes.
  S5: 'Erreurs fréquentes avec le boîtier de préchauffage : - Ne pas vérifier la référence exacte avant commande — une pièce
    de mauvaise référence ne fonctionne pas correctement même si elle se monte physiquement- Oublier de débrancher la batterie
    avant intervention — risque de court-circuit sur les composants électroniques- Ne pas confondre avec les bougies HS. Tester
    d''abord les bougies individuellement. Vérifier la masse et l''alimentation du boîtier avant remplacement.- Ne pas respecter
    le couple de serrage constructeur au remontage- Ignorer les symptômes d''usure en espérant que ça passe — une défaillance
    progressive s''aggrave toujours- Ne pas effacer les codes défaut après remplacement — le calculateur peut rester en mode
    dégradé'
  S6: 'Après le remplacement du boîtier de préchauffage : - Controle visuel a chaque revision ou entretien periodique- Remplacement
    preventif si signes d usure detectes- Utiliser des pieces de qualite equivalente a l origine- Respecter les preconisations
    constructeur pour les intervalles- Effacer les codes défaut éventuels avec l''outil OBD- Effectuer un essai route pour
    confirmer la disparition des symptômes'
---

# Boîtier de préchauffage - Guide Diagnostic Complet

## Fonction et Rôle

Alimenter et controler les bougies de prechauffage diesel - Gere le temps et l'intensite de chauffe

**Actions principales:** alimenter, controler, commander, reguler, gerer le prechauffage

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit claquement diesel demarrage combustion**
  bruit claquement diesel demarrage combustion

### 🟢 Autres Symptômes

- voyant prechauffage qui clignote ou reste allume
- demarrage tres difficile par temps froid
- fumee blanche excessive au demarrage a froid
- odeur de carburant non brule a l echappement
- code defaut p0380 ou p0381 a la valise diagnostic

## Procédure de Diagnostic

Pour diagnostiquer un problème de boîtier de préchauffage:

1. **Inspection visuelle** - Examiner l'état du boîtier de préchauffage
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

- alternateur
- bougie-de-prechauffage
- demarreur

## Critères de Compatibilité

Pour commander le bon boîtier de préchauffage, vous devez connaître:

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

## FAQ

**Boîtier de préchauffage OE ou adaptable ?**
Privilégiez l'OE ou OES (Beru, Bosch, NGK). C'est une pièce électronique de précision qui doit résister aux cycles thermiques.

**Comment savoir si mon boîtier de préchauffage est HS ?**
Voyant préchauffage qui reste allumé ou clignote, démarrage difficile à froid, fumée blanche excessive au démarrage, code défaut P0380.

**Tous les combien changer le boîtier de préchauffage ?**
Pas de périodicité fixe. Durée de vie 150 000 à 250 000 km. À remplacer en cas de défaut avéré ou si les bougies neuves ne chauffent pas.

**Peut-on changer le boîtier de préchauffage soi-même ?**
Oui, opération accessible. Localiser le boîtier (près du moteur), débrancher la batterie, déconnecter les fils, dévisser. 30 min à 1h.

**Quelle erreur éviter avec le boîtier de préchauffage ?**
Ne pas confondre avec les bougies HS. Tester d'abord les bougies individuellement. Vérifier la masse et l'alimentation du boîtier avant remplacement.


## References supplementaires

<!-- materialized-from-db manual/8cd44348d118 2026-04-03 -->
### Données techniques OEM — Boîtier de préchauffage

# Données techniques OEM — Boîtier de préchauffage
Source : fr.wikipedia.org (1 fichiers OEM analysés)
Validation : oem_verified

## Variantes et types
- nao
- pneumatique

## Valeurs techniques de référence
- 20 °C
- 30 kg
