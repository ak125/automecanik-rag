---
category: csv
created_at: '2026-02-12T18:20:52.030651+00:00'
doc_family: catalog
source_ref: profile
source_type: csv
source_uri: /tmp/rag_smoke_products.csv
title: Dataset profile rag_smoke_products.csv
truth_level: L3
updated_at: '2026-02-12T18:20:52.030671+00:00'
verification_status: unverified
---

# Dataset Profile: rag_smoke_products.csv

## Decision

- index_knowledge: true
- index_snapshots: true
- index_raw_data: false (default=false recommended)

## Overview

- source_type: csv
- rows_total: 3
- rows_profiled: 3

## Fields

### brand
- dominant_type: str
- sample_non_null_count: 3
- sample_distinct_count: 3
- sample_null_ratio: 0.0
- sample_top_values: [('BOSCH', 1), ('ATE', 1), ('BREMBO', 1)]

### price
- dominant_type: float
- sample_non_null_count: 3
- sample_distinct_count: 3
- sample_null_ratio: 0.0
- sample_top_values: [('49.90', 1), ('59.50', 1), ('79.00', 1)]

### product_id
- dominant_type: int
- sample_non_null_count: 3
- sample_distinct_count: 3
- sample_null_ratio: 0.0
- sample_top_values: [('1', 1), ('2', 1), ('3', 1)]

### sku
- dominant_type: str
- sample_non_null_count: 3
- sample_distinct_count: 3
- sample_null_ratio: 0.0
- sample_top_values: [('SKU-001', 1), ('SKU-002', 1), ('SKU-003', 1)]

### stock
- dominant_type: int
- sample_non_null_count: 3
- sample_distinct_count: 3
- sample_null_ratio: 0.0
- sample_top_values: [('12', 1), ('4', 1), ('0', 1)]