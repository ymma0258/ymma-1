# Customer-set composition

| Set | High-risk customers | High-exposure customers | Mean risk | Risk P90 | Mean exposure | Q1-Q5 distribution |
|---|---:|---:|---:|---:|---:|---|
| A | 44.0% | 40.0% | 0.158366 | 0.373716 | 0.013133 | Q1:6 (12.0%) / Q2:8 (16.0%) / Q3:7 (14.0%) / Q4:7 (14.0%) / Q5:22 (44.0%) |
| B | 30.0% | 36.0% | 0.135990 | 0.338710 | 0.009442 | Q1:8 (16.0%) / Q2:6 (12.0%) / Q3:10 (20.0%) / Q4:11 (22.0%) / Q5:15 (30.0%) |

Definitions:

- High-risk customer: customer node whose Stable-Tail `S_i_norm` is in the global top 20% of 2021 nodes.
- High-exposure customer: customer node whose normalized incident edge exposure is in the global top 20% of 2021 nodes.
- Q1-Q5 distribution: customer-node risk quintiles computed from the global 2021 Stable-Tail `S_i_norm` distribution.
- Risk source: Stable-Tail GNN, split B seed 0, `floor_0.01` edge-risk matrix.
