# AES Hardware Results

This page summarizes the AES hardware benchmark results.

## Result Versions

- [AES Core Mapping V1](aes_v1.md)

## Implemented Key Sizes

| Variant | Status |
|---|---|
| AES-128 | Implemented |
| AES-192 | Implemented |
| AES-256 | Implemented |
| AES-512 | Exploratory |
| AES-1024 | Exploratory |

## Architectures

| Architecture | Description |
|---|---|
| Iterative | Reuses one round datapath across multiple cycles |
| Pipeline | One round per pipeline stage |
| Iterative GF | Iterative architecture using composite-field S-Box |
| Pipeline GF | Fully pipelined architecture using composite-field S-Box |
| Partial Unrolled | Processes multiple rounds per cycle |
| Partial Unrolled GF | Partial unrolled architecture using composite-field S-Box |

## Result Sources

The structured result database is stored in:

```text
results/tables/hardware_results.csv
