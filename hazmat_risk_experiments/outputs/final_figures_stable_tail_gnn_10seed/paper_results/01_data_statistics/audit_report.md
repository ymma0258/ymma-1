# Hazardous Materials Trajectory Graph Data Audit

## Summary

| Year | Nodes | Edges | Labeled | Unlabeled | High risk 6-8 | Edge attr mean | Edge attr P95 | Largest WCC | Largest SCC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| data_2020 | 4696 | 7048 | 419 | 4277 | 40 | 0.123487 | 0.222222 | 3706 | 2324 |
| data_2021 | 5261 | 8115 | 443 | 4818 | 51 | 0.074455 | 0.133333 | 4357 | 2823 |

## Label Distribution

### data_2020

| Label | Count |
|---:|---:|
| 0 | 4277 |
| 1 | 255 |
| 2 | 61 |
| 3 | 40 |
| 4 | 11 |
| 5 | 12 |
| 6 | 9 |
| 7 | 23 |
| 8 | 8 |

### data_2021

| Label | Count |
|---:|---:|
| 0 | 4818 |
| 1 | 262 |
| 2 | 62 |
| 3 | 44 |
| 4 | 12 |
| 5 | 12 |
| 6 | 11 |
| 7 | 29 |
| 8 | 11 |

## Notes

- Label 0 is treated as unlabeled, not low risk.
- High risk is defined as labels 6, 7, and 8.
- The main path-validation graph should be undirected using max edge-attribute merge.
- Strongly connected components are reported only to diagnose directed reachability.
