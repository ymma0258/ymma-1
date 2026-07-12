# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 9.851446 | 0.000% | 0.341239 | 2.719875 | 0.158001 | 0.880994 | 90.399% |
| 0.25 | 0 | 141641.1 | 5.651% | 7.085827 | 28.073% | 0.183382 | 2.344106 | 0.219719 | 0.878117 | 88.770% |
| 0.5 | 0 | 147241.8 | 9.829% | 5.046880 | 48.770% | 0.134813 | 1.712765 | 0.216847 | 0.855069 | 84.863% |
| 1 | 0 | 155818.4 | 16.226% | 3.476821 | 64.708% | 0.086928 | 1.154843 | 0.237351 | 0.815891 | 78.415% |
| 2 | 0 | 166676.0 | 24.325% | 2.216332 | 77.502% | 0.043496 | 0.767040 | 0.257389 | 0.741691 | 66.810% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
