# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.573809 | 0.000% | 0.222898 | 2.150523 | 0.145774 | 0.878323 | 89.535% |
| 1 | 0 | 158998.3 | 18.658% | 2.898866 | 61.725% | 0.077334 | 0.951183 | 0.275062 | 0.808054 | 77.941% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
