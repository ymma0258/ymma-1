# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 11.743320 | 0.000% | 0.238706 | 3.358512 | 0.151142 | 0.869561 | 89.583% |
| 1 | 0 | 158733.4 | 18.460% | 4.758067 | 59.483% | 0.074080 | 1.584998 | 0.287059 | 0.821029 | 79.431% |
| 2 | 0 | 173315.8 | 29.343% | 4.055004 | 65.470% | 0.057322 | 1.518806 | 0.341355 | 0.794211 | 75.437% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
