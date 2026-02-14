---
category: freinage
created_at: '2026-02-12T18:20:52.133227+00:00'
doc_family: catalog
source_ref: structure_profile
source_type: json
source_uri: /tmp/rag_smoke_export.json
title: Structure profile rag_smoke_export.json
truth_level: L3
updated_at: '2026-02-12T18:20:52.133245+00:00'
verification_status: unverified
---

# Structure Profile: rag_smoke_export.json

## Decision

- index_knowledge: true
- index_snapshots: true
- index_raw_data: false (default=false recommended)

## Overview

- source_type: json
- records_total: 2
- records_profiled: 2
- field_count: 4

## Fields

### brand
- dominant_type: str
- sample_non_null_count: 2
- sample_distinct_count: 2
- sample_null_ratio: 0.0
- sample_top_values: [('BOSCH', 1), ('ATE', 1)]

### id
- dominant_type: str
- sample_non_null_count: 2
- sample_distinct_count: 2
- sample_null_ratio: 0.0
- sample_top_values: [('A1', 1), ('A2', 1)]

### name
- dominant_type: str
- sample_non_null_count: 2
- sample_distinct_count: 2
- sample_null_ratio: 0.0
- sample_top_values: [('Brake Pad', 1), ('Brake Disc', 1)]

### price
- dominant_type: float
- sample_non_null_count: 2
- sample_distinct_count: 2
- sample_null_ratio: 0.0
- sample_top_values: [('49.9', 1), ('89.0', 1)]