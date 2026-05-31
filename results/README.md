# Results Database

This folder stores structured benchmark results for cryptographic hardware implementations.

The main file is:

- `tables/hardware_results.csv`

Each row represents one implementation result, including algorithm, architecture, target platform, area, frequency, throughput, latency, and toolchain information.

The CSV file is the source of truth. Website tables and plots should be generated from this data.
