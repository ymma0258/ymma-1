# Customer-set composition

| Set | Seeds | High-risk customers | High-exposure customers | Mean risk | Risk P90 | Mean exposure | Q1-Q5 distribution |
|---|---:|---:|---:|---:|---:|---:|---|
| A | 10 | 41.8% +/- 3.3% | 40.0% +/- 0.0% | 0.176814 +/- 0.019032 | 0.426017 +/- 0.064192 | 0.013133 +/- 0.000000 | Q1:6.1 +/- 1.1 / Q2:6.8 +/- 1.5 / Q3:7.0 +/- 1.9 / Q4:9.2 +/- 1.8 / Q5:20.9 +/- 1.7 |
| B | 10 | 30.2% +/- 3.5% | 36.0% +/- 0.0% | 0.145366 +/- 0.014148 | 0.340410 +/- 0.041266 | 0.009442 +/- 0.000000 | Q1:9.5 +/- 1.3 / Q2:5.9 +/- 1.3 / Q3:8.3 +/- 2.5 / Q4:11.2 +/- 1.8 / Q5:15.1 +/- 1.7 |

Definitions:

- Values are mean +/- std over the listed Stable-Tail GNN Split-B model seeds.
- Customers are fixed Set A/B CVRP customers; only the risk matrix seed changes.
- High-risk customer: customer node whose Stable-Tail `S_i_norm` is in the global top 20% of 2021 nodes for the corresponding seed.
- High-exposure customer: customer node whose normalized incident edge exposure is in the global top 20% of 2021 nodes.
- Q1-Q5 distribution: mean +/- std of customer counts in global 2021 risk quintiles across seeds.
