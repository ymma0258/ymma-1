# Customer-set composition

| Set | Seeds | High-risk customers | High-exposure customers | Mean risk | Risk P90 | Mean exposure | Q1-Q5 distribution |
|---|---:|---:|---:|---:|---:|---:|---|
| A | 10 | 41.2% +/- 4.8% | 40.0% +/- 0.0% | 0.198366 +/- 0.020433 | 0.454516 +/- 0.054195 | 0.013133 +/- 0.000000 | Q1:5.8 +/- 1.4 / Q2:7.2 +/- 1.4 / Q3:7.6 +/- 2.1 / Q4:8.8 +/- 1.9 / Q5:20.6 +/- 2.4 |
| B | 10 | 30.0% +/- 5.0% | 36.0% +/- 0.0% | 0.163869 +/- 0.015736 | 0.376382 +/- 0.049217 | 0.009442 +/- 0.000000 | Q1:8.9 +/- 1.2 / Q2:7.1 +/- 1.6 / Q3:9.3 +/- 2.3 / Q4:9.7 +/- 2.5 / Q5:15.0 +/- 2.5 |

Definitions:

- Values are mean +/- std over the listed Stable-Tail GNN Split-B model seeds.
- Customers are fixed Set A/B CVRP customers; only the risk matrix seed changes.
- High-risk customer: customer node whose Stable-Tail `S_i_norm` is in the global top 20% of 2021 nodes for the corresponding seed.
- High-exposure customer: customer node whose normalized incident edge exposure is in the global top 20% of 2021 nodes.
- Q1-Q5 distribution: mean +/- std of customer counts in global 2021 risk quintiles across seeds.
