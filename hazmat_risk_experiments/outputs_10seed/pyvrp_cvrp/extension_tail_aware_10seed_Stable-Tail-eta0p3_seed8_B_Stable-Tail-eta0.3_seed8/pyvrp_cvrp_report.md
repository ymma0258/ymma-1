# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.853891 | 0.000% | 0.195558 | 2.803549 | 0.192662 | 0.880130 | 89.052% |
| 1 | 0 | 175264.2 | 19.446% | 3.919087 | 55.736% | 0.078896 | 1.617756 | 0.354828 | 0.826556 | 79.535% |
| 2 | 0 | 191345.6 | 30.406% | 3.014997 | 65.947% | 0.059145 | 1.191696 | 0.305918 | 0.794309 | 74.262% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
