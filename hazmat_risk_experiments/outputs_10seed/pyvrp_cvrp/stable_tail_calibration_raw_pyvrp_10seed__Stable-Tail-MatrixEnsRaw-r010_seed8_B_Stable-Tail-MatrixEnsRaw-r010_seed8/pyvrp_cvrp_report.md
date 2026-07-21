# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.2 | 0.000% | 6.899630 | 0.000% | 0.213325 | 2.101667 | 0.199425 | 0.860306 | 87.823% |
| 0.25 | 0 | 156453.9 | 6.289% | 5.539754 | 19.709% | 0.128729 | 1.771874 | 0.202740 | 0.854642 | 86.659% |
| 0.5 | 0 | 164898.6 | 12.026% | 4.485330 | 34.992% | 0.110146 | 1.373461 | 0.183700 | 0.841659 | 84.199% |
| 1 | 0 | 175937.7 | 19.525% | 2.849424 | 58.702% | 0.069578 | 0.970546 | 0.217079 | 0.786871 | 76.146% |
| 2 | 0 | 190104.5 | 29.150% | 2.212380 | 67.935% | 0.047547 | 0.640260 | 0.209805 | 0.751348 | 70.572% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
