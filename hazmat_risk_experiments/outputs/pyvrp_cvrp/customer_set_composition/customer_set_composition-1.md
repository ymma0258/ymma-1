# Customer-set composition

| Set | Seeds | High-risk customers | High-exposure customers | Mean risk | Risk P90 | Mean exposure | Q1-Q5 distribution |
|---|---:|---:|---:|---:|---:|---:|---|
| A | 10 | 42.0% +/- 4.1% | 40.0% +/- 0.0% | 0.190129 +/- 0.023641 | 0.458529 +/- 0.064714 | 0.013133 +/- 0.000000 | Q1:5.9 +/- 1.0 / Q2:6.9 +/- 1.2 / Q3:6.7 +/- 1.8 / Q4:9.5 +/- 2.2 / Q5:21.0 +/- 2.1 |
| B | 10 | 29.4% +/- 3.7% | 36.0% +/- 0.0% | 0.154401 +/- 0.017663 | 0.357648 +/- 0.061802 | 0.009442 +/- 0.000000 | Q1:9.0 +/- 1.2 / Q2:6.5 +/- 0.8 / Q3:8.6 +/- 2.2 / Q4:11.2 +/- 2.4 / Q5:14.7 +/- 1.8 |

Definitions:

- Values are mean +/- std over the listed Stable-Tail GNN Split-B model seeds.
- Customers are fixed Set A/B CVRP customers; only the risk matrix seed changes.
- High-risk customer: customer node whose Stable-Tail `S_i_norm` is in the global top 20% of 2021 nodes for the corresponding seed.
- High-exposure customer: customer node whose normalized incident edge exposure is in the global top 20% of 2021 nodes.
- Q1-Q5 distribution: mean +/- std of customer counts in global 2021 risk quintiles across seeds.
