---
title: "Systeme xenon — ballast, ampoules D1S-D4S, specs tension (HELLA)"
source_type: guide
category: knowledge
truth_level: L3
source_url: "https://www.hella.com/techworld/fr/technique/eclairage/projecteurs-au-xenon/"
ingested_at: "2026-03-29T23:00:07Z"
ingested_by: batch-web-ingest-phase5
mapped_gammes:
- feu-avant
- ballast-a-lampe-xenon
---

# Systeme Xenon — Guide technique

## Composants
- Ballast (EVG) : genere impulsion haute tension pour ioniser le gaz
- Ampoules : D1, D2, D3, D4 (S=reflecteur, R=projection)

## Specifications
- Tension d'amorcage : jusqu'a 30 kV (4eme generation)
- Puissance nominale : 35W regule
- Frequence : 300 Hz courant alternatif
- Tension min alimentation : 9V DC au ballast
- Arret securite : < 0,2s si ampoule absente/endommagee ou fuite > 30 mA
- Protection : 7 tentatives d'amorcage max avant arret definitif

## Diagnostic
Ecouter les tentatives d'amorcage pres du projecteur. Si absent = verifier 9V min aux bornes ballast + fusible.