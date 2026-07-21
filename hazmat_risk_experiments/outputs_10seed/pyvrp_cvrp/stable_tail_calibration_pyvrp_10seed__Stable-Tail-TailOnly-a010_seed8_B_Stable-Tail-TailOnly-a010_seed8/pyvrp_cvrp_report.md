# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 7.666725 | 0.000% | 0.236589 | 2.333631 | 0.193030 | 0.861681 | 87.937% |
| 0.25 | 0 | 156461.0 | 6.438% | 6.181032 | 19.378% | 0.149806 | 2.008138 | 0.211399 | 0.854413 | 86.701% |
| 0.5 | 0 | 165018.8 | 12.260% | 4.919059 | 35.839% | 0.119634 | 1.595473 | 0.226044 | 0.837955 | 83.846% |
| 1 | 0 | 175573.0 | 19.440% | 3.053363 | 60.174% | 0.074081 | 1.037623 | 0.233345 | 0.782115 | 75.450% |
| 2 | 0 | 190820.6 | 29.812% | 2.502053 | 67.365% | 0.053738 | 0.737209 | 0.204362 | 0.756202 | 71.232% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
