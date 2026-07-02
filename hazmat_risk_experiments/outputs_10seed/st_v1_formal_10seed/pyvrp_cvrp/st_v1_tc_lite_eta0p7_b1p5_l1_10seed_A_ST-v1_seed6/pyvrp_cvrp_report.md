# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.573809 | 0.000% | 0.222898 | 2.150523 | 0.145774 | 0.878323 | 89.535% |
| 1.5 | 1 | 178644.7 | 33.319% | 2.118207 | 72.032% | 0.038356 | 1.023501 | 0.350647 | 0.750495 | 69.207% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
