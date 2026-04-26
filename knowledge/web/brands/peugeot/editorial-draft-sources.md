---
type: draft-sources
brand_alias: peugeot
marque_id: 128
generated_at: 2026-04-21
---

# Peugeot — Editorial Draft Sources (R7)

Annotations par entrée du `editorial-draft.json`. À lire avant toute publication pour validation mot-pour-mot.

## FAQ

### FAQ 1 — Peugeot fait-il partie d'un groupe ?

- **Source** : `wikipedia-fr-main.md` ligne « Peugeot, constructeur automobile français est depuis 2021 une filiale du groupe Stellantis » + « L'entreprise Peugeot est à l'origine du Groupe PSA qui englobe également Citroën, achetée à Michelin en 1976, DS, fondée en 2014, ainsi que Vauxhall et sa sœur allemande Opel »
- **Source** : RAG frontmatter `group: Stellantis`
- **Status** : factuel, directement issu de Wikipedia FR — PAS de synthèse LLM

### FAQ 2 — Compatibilité Peugeot / Citroën / DS

- **Source** : Wikipedia FR Peugeot (même passage groupe PSA/Stellantis) + connaissance publique que les constructeurs du même groupe partagent des plateformes
- **Status** : phrase volontairement prudente — « à vérifier référence par référence » pour éviter d'affirmer une compatibilité totale qui serait fausse
- **Attention** : ne nomme PAS de plateforme ou moteur précis (EMP2/CMP/HDi serait R8)

### FAQ 3 — Depuis quand Peugeot automobile ?

- **Source** : `wikipedia-fr-main.md` lignes « En 1896, il crée la "Société anonyme des automobiles Peugeot" » + « Ainsi, en janvier 1891, Peugeot produit et commercialise l'une des premières voitures "sans chevaux" »
- **Source** : RAG frontmatter `founded_year: 1810`
- **Status** : 100 % factuel Wikipedia

### FAQ 4 — Peugeot motorisations disponibles

- **Source** : Wikipedia FR « Peugeot est le premier constructeur français à commercialiser un véhicule de série diesel avec les 402 à carrosserie longue et vendues comme taxis en 1939 » + « la 604 D Turbo, première voiture à moteur turbo-Diesel vendue en Europe » (1978)
- **Statement actuel** : « gamme actuelle couvre l'essence, le diesel, l'hybride et le 100 % électrique » — c'est vrai en 2026 mais pas dans Wikipedia FR explicitement (info datée par site constructeur). **À valider par l'admin**.
- **Status** : historique OK, statement actuel à vérifier

### FAQ 5 — Siège + site industriel

- **Source** : RAG frontmatter `headquarters.city: Poissy`
- **Source** : Wikipedia FR « En 1912, l'usine de Sochaux est inaugurée »
- **Source** : Wikipedia FR « fermement associée à la ville de Sochaux où se trouve son plus gros site industriel qui regroupe des activités de recherche et développement et de fabrication d'automobile en série »
- **Status** : 100 % factuel Wikipedia + RAG

## Common issues — volontairement vide

Corpus `rappel-conso-fr.json` contient 100 rappels Peugeot mais tous sont **modèle-spécifique** (Boxer NG, 308 V3, Rifter, Partner, Expert, etc.). R7 impose du marque-transversal. Aucune agrégation légitime ne donne un signal R7 sans inventer.

Ce qu'un admin avec expertise catalogue peut ajouter :
- « Couverture catalogue : X % pour modèles XXXX-présent, Y % pour XXXX-XXXX » (données AutoMecanik internes, pas inventables)
- « Historique constructeur : pattern de rappels carburant fréquent depuis 2020 » si ce pattern est confirmé par l'admin

## Maintenance tips — volontairement vide

Pas de source OEM publique fiable pour intervalles Peugeot. Sources potentielles :
- Manuel constructeur Peugeot (PDF payant)
- Haynes / Autodata (payant ~500€/an)
- Expertise interne AutoMecanik

Ce qu'un admin **avec source en main** peut ajouter (marque-level uniquement) :
- « Peugeot recommande DOT 4 LV sur l'ensemble de sa gamme récente » — si confirmé
- « L'intervalle vidange allongé Peugeot s'applique à l'ensemble des moteurs BlueHDi Euro 6 » — si confirmé
- Surtout pas : « Moteur DV6 — intervalle 180 000 km » (R8 modèle)

## Workflow suggéré pour l'admin

1. Ouvrir `/admin/brands-seo?brand=peugeot`
2. Copier le contenu `faq` du JSON dans le formulaire FAQ
3. Valider / corriger / publier
4. Noter score R7 obtenu (diversity_score devrait monter au-dessus de 85 avec 5 FAQ marque-level sourcées)
5. Si OK, passer à BMW / Renault / Citroën selon la même méthode
