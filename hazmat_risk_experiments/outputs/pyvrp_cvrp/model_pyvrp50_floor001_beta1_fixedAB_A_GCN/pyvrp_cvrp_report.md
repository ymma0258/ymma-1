# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.2 | 0.000% | 7.251121 | 0.000% | 0.204571 | 2.540507 | 0.232374 | 0.864117 | 88.932% |
| 1 | 156975.8 | 17.149% | 2.507068 | 65.425% | 0.052613 | 0.790557 | 0.218823 | 0.759431 | 74.105% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
