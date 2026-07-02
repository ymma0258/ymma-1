# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.573809 | 0.000% | 0.222898 | 2.150523 | 0.145774 | 0.878323 | 89.535% |
| 1.5 | 1 | 178638.1 | 33.314% | 2.142307 | 71.714% | 0.039073 | 1.047715 | 0.355824 | 0.752328 | 69.474% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
