# Customer-set diagnostics by model seed

| Set | Seed | Customers | High-risk ratio | High-exposure ratio | Mean risk | Risk P90 | Risk P95 | Mean exposure | Q1 | Q2 | Q3 | Q4 | Q5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 0 | 50 | 44.0% | 40.0% | 0.158366 | 0.373716 | 0.494697 | 0.013133 | 6 | 8 | 7 | 7 | 22 |
| B | 0 | 50 | 30.0% | 36.0% | 0.135990 | 0.338710 | 0.456830 | 0.009442 | 8 | 6 | 10 | 11 | 15 |
| A | 1 | 50 | 38.0% | 40.0% | 0.154139 | 0.508215 | 0.603673 | 0.013133 | 7 | 7 | 10 | 7 | 19 |
| B | 1 | 50 | 26.0% | 36.0% | 0.118486 | 0.257419 | 0.529581 | 0.009442 | 10 | 7 | 11 | 9 | 13 |
| A | 2 | 50 | 44.0% | 40.0% | 0.191186 | 0.458663 | 0.569730 | 0.013133 | 5 | 6 | 5 | 12 | 22 |
| B | 2 | 50 | 30.0% | 36.0% | 0.154564 | 0.333783 | 0.569730 | 0.009442 | 9 | 5 | 7 | 14 | 15 |
| A | 3 | 50 | 44.0% | 40.0% | 0.170289 | 0.339908 | 0.438374 | 0.013133 | 5 | 9 | 5 | 9 | 22 |
| B | 3 | 50 | 34.0% | 36.0% | 0.145300 | 0.339908 | 0.438374 | 0.009442 | 9 | 8 | 6 | 10 | 17 |
| A | 4 | 50 | 44.0% | 40.0% | 0.210615 | 0.525681 | 0.652245 | 0.013133 | 5 | 8 | 8 | 7 | 22 |
| B | 4 | 50 | 30.0% | 36.0% | 0.168701 | 0.363142 | 0.595073 | 0.009442 | 9 | 6 | 10 | 10 | 15 |

Definitions:

- Each row uses the fixed Set A/B customers and one Stable-Tail GNN Split-B model seed risk matrix.
- High-risk ratio uses the global top-20% threshold of `S_i_norm` for the corresponding seed.
- High-exposure ratio uses the global top-20% threshold of normalized incident exposure for the corresponding seed risk matrix.
- Q1-Q5 counts are risk quintiles computed from the global 2021 `S_i_norm` distribution for the corresponding seed.
