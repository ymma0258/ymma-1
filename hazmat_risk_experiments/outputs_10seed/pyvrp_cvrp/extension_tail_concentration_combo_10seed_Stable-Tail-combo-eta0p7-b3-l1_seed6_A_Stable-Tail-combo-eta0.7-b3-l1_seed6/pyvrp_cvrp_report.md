# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.573809 | 0.000% | 0.222898 | 2.150523 | 0.145774 | 0.878323 | 89.535% |
| 3 | 1 | 197144.8 | 47.126% | 2.069839 | 72.671% | 0.036630 | 1.023084 | 0.377614 | 0.744715 | 68.307% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
