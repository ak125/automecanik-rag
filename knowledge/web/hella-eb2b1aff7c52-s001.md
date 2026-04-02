---
title: "Capteur temperature air admission NTC — valeurs resistance (HELLA)"
source_type: guide
category: knowledge
truth_level: L3
source_url: "https://www.hella.com/techworld/fr/technique/capteurs-et-actionneurs/capteur-de-temperature-de-l-air-d-admission/"
ingested_at: "2026-03-29T23:00:07Z"
ingested_by: batch-web-ingest-phase5
mapped_gammes:
- capteur-temperature-d-air-admission
---

# Capteur temperature air admission — Guide technique

## Type : NTC
Mesure la temperature dans le collecteur d'admission. Resistance diminue quand temperature augmente.

## Valeurs
- 25 degC (froid) : 2,0-6 kohms
- 80 degC (chaud) : ~300 ohms
- Tension alimentation : ~5V du calculateur

## Symptomes
Codes defaut + voyant moteur, difficultes de demarrage, puissance reduite, surconsommation.

## Diagnostic multimetre
1. Resistance a temperature connue vs specs constructeur
2. Continuite cablage capteur-calculateur : ~0 ohm
3. Tension 5V au connecteur debranche contact mis

## Causes : courts-circuits internes, coupures cables, dommage mecanique, encrassement pointe capteur.