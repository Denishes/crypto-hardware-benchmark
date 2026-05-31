# AES Core Mapping — V1

This page presents the first cleaned AES core mapping result set.

## ASIC 45 nm and FPGA ECP5 Results

| Key Size | Design | ASIC Area (mm²) | ASIC CLK (MHz) | ASIC Throughput (Gbps) | Latency (Cycles) | ASIC Efficiency (Gbps/mm²) | ECP5 Fmax (MHz) | ECP5 LUTs |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 128 | Pipeline | 0.109 | 881 | 113 | 10 | 1035 | 54.66 | 38033 |
| 128 | Pipeline GF | 0.052 | 671 | 86 | 10 | 1652 | 64.37 | 24426 |
| 128 | Iterative | 0.033 | 293 | 3.8 | 10 | 114 | 79.43 | 5925 |
| 128 | Iterative GF | 0.016 | 309 | 4.0 | 10 | 247 | 67.76 | 5306 |
| 128 | Partial Unrolled | 0.040 | 284 | 7.3 | 5 | 182 | 50.16 | 11469 |
| 128 | Partial Unrolled GF | 0.022 | 220 | 5.6 | 5 | 256 | 36.05 | 9872 |
| 192 | Pipeline | 0.130 | 886 | 113 | 12 | 872 | 57.72 | 45247 |
| 192 | Pipeline GF | 0.064 | 671 | 86 | 12 | 1342 | 62.80 | 30302 |
| 192 | Iterative | 0.029 | 523 | 5.6 | 12 | 192 | 83.82 | 5788 |
| 192 | Iterative GF | 0.017 | 512 | 5.5 | 12 | 321 | 67.91 | 5263 |
| 192 | Partial Unrolled | 0.045 | 284 | 6.1 | 6 | 135 | 50.23 | 13048 |
| 192 | Partial Unrolled GF | 0.025 | 221 | 4.7 | 6 | 189 | 35.67 | 9898 |
| 256 | Pipeline | 0.150 | 883 | 113 | 14 | 753 | 50.76 | 51040 |
| 256 | Pipeline GF | 0.073 | 666 | 85 | 14 | 1168 | 60.37 | 30505 |
| 256 | Iterative | 0.040 | 595 | 7.6 | 14 | 190 | 78.65 | 4892 |
| 256 | Iterative GF | 0.024 | 591 | 7.6 | 14 | 315 | 68.64 | 4401 |
| 256 | Partial Unrolled | 0.078 | 244 | 6.2 | 7 | 80 | 51.06 | 10446 |
| 256 | Partial Unrolled GF | 0.040 | 214 | 5.5 | 7 | 137 | 36.37 | 8909 |
| 512 | Pipeline | 0.218 | 880 | 113 | 22 | 517 | 52.36 | 78007 |
| 512 | Pipeline GF | 0.104 | 662 | 85 | 22 | 815 | 63.90 | 46438 |
| 512 | Iterative | 0.036 | 324 | 4.1 | 22 | 115 | 82.40 | 4630 |
| 512 | Iterative GF | 0.022 | 322 | 4.1 | 22 | 187 | 67.55 | 3965 |
| 512 | Partial Unrolled | 0.114 | 359 | 9.2 | 11 | 81 | 50.89 | 10483 |
| 512 | Partial Unrolled GF | 0.059 | 195 | 5.0 | 11 | 85 | 36.70 | 8350 |
| 1024 | Pipeline | 0.359 | 879 | 113 | 38 | 313 | — | 133619 |
| 1024 | Pipeline GF | 0.170 | 662 | 85 | 38 | 499 | 62.87 | 75733 |
| 1024 | Iterative | 0.038 | 427 | 5.5 | 38 | 144 | 81.83 | 4658 |
| 1024 | Iterative GF | 0.025 | 423 | 5.4 | 38 | 219 | 70.65 | 4053 |
| 1024 | Partial Unrolled | 0.185 | 271 | 6.9 | 19 | 38 | 50.45 | 11386 |
| 1024 | Partial Unrolled GF | 0.092 | 188 | 4.8 | 19 | 52 | 36.00 | 9482 |

## Notes

- ASIC results target Nangate45.
- FPGA results target ECP5.
- GF indicates composite-field S-Box implementation.
- AES-512 and AES-1024 are exploratory non-standard Rijndael-style extensions.
- Older duplicated spreadsheet values are excluded from this version.
