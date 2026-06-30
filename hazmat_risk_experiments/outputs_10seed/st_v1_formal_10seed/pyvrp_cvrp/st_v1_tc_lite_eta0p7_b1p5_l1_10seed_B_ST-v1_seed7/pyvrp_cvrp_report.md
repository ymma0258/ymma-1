# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.851676 | 0.000% | 0.287040 | 3.185509 | 0.204509 | 0.879458 | 90.687% |
| 1.5 | 1 | 203792.1 | 38.888% | 2.996105 | 69.588% | 0.065234 | 1.114699 | 0.343839 | 0.795494 | 74.041% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
