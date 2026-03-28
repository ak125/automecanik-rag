---
category: freinage
slug: vis-de-disque
title: Vis de disque
pg_id: 54
source_type: gamme
doc_family: catalog
truth_level: L2
updated_at: '2026-03-25'
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
  role: Fixer le disque de frein sur le moyeu de roue
  must_be_true:
  - fixer
  - maintenir
  - bloquer
  must_not_contain:
  - injection
  - climatisation
  - embrayage
  - distribution
  - universel
  - tous modèles
  - compatible tout véhicule
  - adaptable
  related_parts:
  - disque-de-frein
  - plaquette-de-frein
  - etrier-de-frein
  - flexible-de-frein
  - maitre-cylindre-de-frein
  - liquide-de-frein
  confusion_with:
  - term: piece-de-freinage-voisine
    difference: 'Verifier la reference exacte : les pieces de freinage se ressemblent mais ne sont pas interchangeables entre
      essieux ou types de montage.'
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
  - ❌ "freinage garanti"
  cost_range:
    min: 3
    max: 15
    currency: EUR
    unit: l'unite
    source: estimation categorie
  brands:
    premium:
    - Brembo
    - ATE
    - TRW
    standard:
    - Febi Bilstein
    - Swag
    - Bosch
    - Textar
    budget:
    - NK
    - A.B.S.
    - Mapco
  quality_tiers:
  - tier: Origine (OE/OES)
    description: Vis de disque fabriquées par les équipementiers d'origine. Traitement anti-corrosion et couple de serrage
      calibrés pour le moyeu spécifique.
  - tier: Équivalent OE
    description: Fabricants aftermarket reconnus en visserie de freinage. Conformes aux spécifications constructeur, traitement
      de surface adapté.
  - tier: Adaptable
    description: Vis économiques. Vérifier le type d'empreinte (Torx, Allen, hexagonale), le diamètre et le pas de filetage
      avant commande.
diagnostic:
  symptoms:
  - id: S1
    label: Vis grippee impossible a devisser
    severity: confort
  - id: S2
    label: Tete de vis arrondie ou endommagee
    severity: confort
  - id: S3
    label: Vis rouillee visible a travers la jante
    severity: confort
  - id: S4
    label: Disque qui bouge legerement vis desserree
    severity: confort
  - id: S5
    label: Bruit claquement freinage cassee absente
    severity: confort
  causes:
  - localiser source et verifier usure mecanique
  - 'bruit anormal detecte : localiser source et verifier usure mecanique'
  - 'Usure ou defaillance causant : vis grippee impossible a devisser'
  quick_checks:
  - 'Observer : vis grippee impossible a devisser ?'
  - 'Observer : tete de vis arrondie ou endommagee ?'
  - 'Observer : vis rouillee visible a travers la jante ?'
  - 'Observer : disque qui bouge legerement vis desserree ?'
maintenance:
  interval:
    value: selon constructeur
    unit: condition
    note: Ne pas attendre la panne complete pour intervenir.
    source: null
  wear_signs:
  - Vis grippee impossible a devisser
  - Tete de vis arrondie ou endommagee
  - Vis rouillee visible a travers la jante
  - Disque qui bouge legerement vis desserree
  - Bruit claquement freinage cassee absente
  good_practices:
  - Controle visuel a chaque revision ou tous les 15 000 km
  - Remplacement par paire (essieu complet) pour equilibre de freinage
  - Rodage des pieces neuves sur 200 km (freinages progressifs)
  - Verifier le niveau de liquide de frein lors de chaque intervention
rendering:
  pgId: '54'
  intro_title: A quoi sert Vis de disque ?
  risk_title: Pourquoi remplacer Vis de disque a temps ?
  risk_explanation: '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  risk_consequences:
  - '**Usure mécanique** - Les bruits indiquent souvent une usure des composants internes'
  - '**Défaillance progressive** - Usure normale due à l''utilisation'
  - '**Conditions d''utilisation** - Sollicitations excessives ou environnement défavorable'
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
  - question: Les vis de disque sont-elles indispensables ?
    answer: Elles maintiennent le disque en place pendant le montage. Une fois la roue serrée, les écrous de roue assurent
      le maintien principal.
  - question: Comment retirer une vis grippée ?
    answer: 'Dégrippant, chaleur localisée, embout à frapper. En dernier recours : perçage et extraction. Prévoyez des vis
      neuves.'
  - question: Faut-il graisser ou freiner les vis ?
    answer: 'Selon constructeur : certains préconisent du frein-filet (Loctite bleu), d''autres de la graisse cuivrée. Consultez
      la documentation technique.'
  - question: Quelles sont les erreurs fréquentes à éviter ?
    answer: Forcer une vis Torx/Allen grippée sans outil → tête foirée. Oublier de nettoyer l'empreinte → l'embout ripe.
  - question: Comment faire un diagnostic rapide ?
    answer: 'Vis déjà arrondie/rouillée → prévoir vis neuves + embout neuf + dégrippant. Si elle casse : extraction/perçage
      (prévoir temps atelier).'
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
doc_id: eb3cd898-8b88-5d10-9322-ba32273a3786
content_hash: sha256:81bcfb7df7043650
lang: fr
variants:
- name: Piece standard
  aliases:
  - standard
  - OE equivalent
  functional_differences:
  - Qualite equivalente a la monte d origine
  - Compatible avec la majorite des vehicules
- name: Piece performance/sport
  aliases:
  - sport
  - haute performance
  functional_differences:
  - Materiaux haute temperature
  - Pour usage intensif ou sportif
location_on_vehicle:
  area: Au niveau des roues (avant et/ou arriere)
  access: Demontage de la roue necessaire (cric + chandelle)
  adjacent_parts:
  - disque
  - plaquette
  - etrier
  - flexible
installation:
  difficulty: moyen
  time: 30min a 1h par essieu
  tools:
  - cle a douille
  - cle Allen
  - pied a coulisse
  - cle dynamometrique
  prerequisite: Vehicule sur chandelles, roue demontee
---

# Vis de disque - Guide Diagnostic Complet

## Fonction et Rôle

Fixer le disque de frein sur le moyeu de roue

**Actions principales:** fixer, maintenir, bloquer

## Symptômes de Défaillance

### 🟠 Symptômes de Dégâts Potentiels

- **Bruit claquement freinage cassee absente**
  bruit claquement freinage cassee absente

### 🟢 Autres Symptômes

- vis grippee impossible a devisser
- tete de vis arrondie ou endommagee
- vis rouillee visible a travers la jante
- disque qui bouge legerement vis desserree

## Procédure de Diagnostic

Pour diagnostiquer un problème de vis de disque:

1. **Inspection visuelle** - Examiner l'état du vis de disque
2. **Mesure d'usure** - Contrôler l'épaisseur et l'état de surface
3. **Test au roulage** - Vérifier l'efficacité et les bruits
4. **Diagnostic sonore** - Localiser la source des bruits anormaux


## Entretien et Intervalles

- **Intervalle** : selon constructeur
- Ne pas attendre la panne complete pour intervenir.

## Causes Probables

- **Usure mécanique** - Les bruits indiquent souvent une usure des composants internes
- **Défaillance progressive** - Usure normale due à l'utilisation
- **Conditions d'utilisation** - Sollicitations excessives ou environnement défavorable

## Pièces Associées

Lors du remplacement, vérifier également:

- disque-de-frein

## Critères de Compatibilité

Pour commander le bon vis de disque, vous devez connaître:

- **Marque** de votre véhicule
- **Modele** de votre véhicule
- **Annee** de votre véhicule

## ❌ Attention aux Fausses Promesses

Méfiez-vous des vendeurs qui utilisent ces termes interdits:

- ❌ "homologué CT"
- ❌ "sécurité garantie"
- ❌ "zéro panne"
- ❌ "garanti à vie"
- ❌ "freinage garanti"

## FAQ

**Les vis de disque sont-elles indispensables ?**
Elles maintiennent le disque en place pendant le montage. Une fois la roue serrée, les écrous de roue assurent le maintien principal.

**Comment retirer une vis grippée ?**
Dégrippant, chaleur localisée, embout à frapper. En dernier recours : perçage et extraction. Prévoyez des vis neuves.

**Faut-il graisser ou freiner les vis ?**
Selon constructeur : certains préconisent du frein-filet (Loctite bleu), d'autres de la graisse cuivrée. Consultez la documentation technique.

**Quelles sont les erreurs fréquentes à éviter ?**
Forcer une vis Torx/Allen grippée sans outil → tête foirée. Oublier de nettoyer l'empreinte → l'embout ripe.

**Comment faire un diagnostic rapide ?**
Vis déjà arrondie/rouillée → prévoir vis neuves + embout neuf + dégrippant. Si elle casse : extraction/perçage (prévoir temps atelier).


## References supplementaires

<!-- materialized-from-db guides/freinage__quand-changer.md 2026-03-03 -->
### Quand changer les plaquettes et disques

## Signes d'usure

- bruit metallique au freinage
- vibration a la pedale
- distance de freinage en hausse
- epaisseur de garniture faible

## Frequence de controle

- controle visuel regulier
- verification a chaque entretien periodique
- remplacement selon usure reelle et recommandations constructeur
