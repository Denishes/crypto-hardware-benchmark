# FPGA ECP5 Results

[Pre-layout](prelayout.md) · [Post-layout](postlayout.md) · **ECP5**

**Platform:** Lattice ECP5 · **Configurations:** 5 · **Implementations:** 30

AES and non-standard extended Rijndael (ER) hardware results.

## 128-bit configuration

| Design | Maximum frequency (MHz) | LUTs (total) |
| :--- | ---: | ---: |
| Pipeline | 54.66 | 38,033 |
| Pipeline GF | 64.37 | 24,426 |
| Iterative | 79.43 | 5,925 |
| Iterative GF | 67.76 | 5,306 |
| Partially unrolled | 50.16 | 11,469 |
| Partially unrolled GF | 36.05 | 9,872 |

## 192-bit configuration

| Design | Maximum frequency (MHz) | LUTs (total) |
| :--- | ---: | ---: |
| Pipeline | 57.72 | 45,247 |
| Pipeline GF | 62.80 | 30,302 |
| Iterative | 83.82 | 5,788 |
| Iterative GF | 67.91 | 5,263 |
| Partially unrolled | 50.23 | 13,048 |
| Partially unrolled GF | 35.67 | 9,898 |

## 256-bit configuration

| Design | Maximum frequency (MHz) | LUTs (total) |
| :--- | ---: | ---: |
| Pipeline | 50.76 | 51,040 |
| Pipeline GF | 60.37 | 30,505 |
| Iterative | 78.65 | 4,892 |
| Iterative GF | 68.64 | 4,401 |
| Partially unrolled | 51.06 | 10,446 |
| Partially unrolled GF | 36.37 | 8,909 |

## 512-bit configuration

| Design | Maximum frequency (MHz) | LUTs (total) |
| :--- | ---: | ---: |
| Pipeline | 52.36 | 78,007 |
| Pipeline GF | 63.90 | 46,438 |
| Iterative | 82.40 | 4,630 |
| Iterative GF | 67.55 | 3,965 |
| Partially unrolled | 50.89 | 10,483 |
| Partially unrolled GF | 36.70 | 8,350 |

## 1024-bit configuration

| Design | Maximum frequency (MHz) | LUTs (total) |
| :--- | ---: | ---: |
| Pipeline | Not reported | 133,619 |
| Pipeline GF | 62.87 | 75,733 |
| Iterative | 81.83 | 4,658 |
| Iterative GF | 70.65 | 4,053 |
| Partially unrolled | 50.45 | 11,386 |
| Partially unrolled GF | 36.00 | 9,482 |
