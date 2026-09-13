# ASIC Post-Layout Results

[Pre-layout](prelayout.md) · **Post-layout** · [ECP5](ecp5.md)

**Technology:** 45 nm · **Configurations:** 5 · **Implementations:** 30

AES and non-standard extended Rijndael (ER) hardware results.

## 128-bit configuration

| Design | Area (mm²) | Target clock (MHz) | Latency (cycles) | Throughput (Gbit/s) | Power (mW) | Core utilization (%) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pipeline | 0.149835 | 881 | 10 | 113.0 | 11.30 | 42 |
| Pipeline GF | 0.079142 | 671 | 10 | 86.0 | 7.90 | 42 |
| Iterative | 0.046999 | 293 | 10 | 3.8 | 1.97 | 38 |
| Iterative GF | 0.031441 | 309 | 10 | 4.0 | 3.99 | 39 |
| Partially unrolled | 0.057625 | 284 | 5 | 7.3 | 2.97 | 38 |
| Partially unrolled GF | 0.035835 | 220 | 5 | 5.6 | 4.45 | 40 |

## 192-bit configuration

| Design | Area (mm²) | Target clock (MHz) | Latency (cycles) | Throughput (Gbit/s) | Power (mW) | Core utilization (%) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pipeline | 0.179088 | 886 | 12 | 113.0 | 15.50 | 42 |
| Pipeline GF | 0.097804 | 671 | 12 | 86.0 | 10.20 | 42 |
| Iterative | 0.040812 | 523 | 12 | 5.6 | 1.56 | 38 |
| Iterative GF | 0.025935 | 512 | 12 | 5.5 | 3.03 | 42 |
| Partially unrolled | 0.065266 | 284 | 6 | 6.1 | 4.11 | 38 |
| Partially unrolled GF | 0.042075 | 221 | 6 | 4.7 | 6.08 | 39 |

## 256-bit configuration

| Design | Area (mm²) | Target clock (MHz) | Latency (cycles) | Throughput (Gbit/s) | Power (mW) | Core utilization (%) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pipeline | 0.204889 | 880 | 14 | 113.0 | 16.90 | 42 |
| Pipeline GF | 0.106417 | 600 | 14 | 77.0 | 10.50 | 41 |
| Iterative | 0.058698 | 595 | 14 | 7.6 | 3.39 | 37 |
| Iterative GF | 0.039233 | 591 | 14 | 7.6 | 5.33 | 39 |
| Partially unrolled | 0.114498 | 244 | 7 | 6.2 | 9.42 | 37 |
| Partially unrolled GF | 0.076191 | 214 | 7 | 5.5 | 13.10 | 39 |

## 512-bit configuration

| Design | Area (mm²) | Target clock (MHz) | Latency (cycles) | Throughput (Gbit/s) | Power (mW) | Core utilization (%) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pipeline | 0.286520 | 850 | 22 | 109.0 | 22.90 | 41 |
| Pipeline GF | 0.148803 | 590 | 22 | 76.0 | 12.60 | 41 |
| Iterative | 0.050321 | 324 | 22 | 4.1 | 2.10 | 38 |
| Iterative GF | 0.036739 | 322 | 22 | 4.1 | 3.93 | 40 |
| Partially unrolled | 0.165830 | 359 | 11 | 9.2 | 15.80 | 36 |
| Partially unrolled GF | 0.112140 | 195 | 11 | 5.0 | 20.00 | 39 |

## 1024-bit configuration

| Design | Area (mm²) | Target clock (MHz) | Latency (cycles) | Throughput (Gbit/s) | Power (mW) | Core utilization (%) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pipeline | 0.455480 | 840 | 38 | 108.0 | 36.70 | 40 |
| Pipeline GF | 0.238707 | 580 | 38 | 74.0 | 19.00 | 41 |
| Iterative | 0.052853 | 427 | 38 | 5.5 | 2.00 | 39 |
| Iterative GF | 0.039944 | 423 | 38 | 5.4 | 3.79 | 40 |
| Partially unrolled | 0.283276 | 271 | 19 | 6.9 | 29.80 | 34 |
| Partially unrolled GF | 0.186642 | 188 | 19 | 4.8 | 35.30 | 39 |
