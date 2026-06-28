# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 12.217774 | 0.000% | 0.305965 | 3.390583 | 0.134738 | 0.839282 | 87.738% |
| 1 | 0 | 161509.0 | 20.532% | 5.369230 | 56.054% | 0.104313 | 1.505481 | 0.163642 | 0.771493 | 77.981% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
