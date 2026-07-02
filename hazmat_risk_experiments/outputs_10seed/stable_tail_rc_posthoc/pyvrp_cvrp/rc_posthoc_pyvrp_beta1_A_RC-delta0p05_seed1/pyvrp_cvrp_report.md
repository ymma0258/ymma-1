# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.694454 | 0.000% | 0.242443 | 2.291778 | 0.172181 | 0.878427 | 89.514% |
| 1 | 0 | 155103.4 | 15.751% | 2.553716 | 66.811% | 0.054506 | 0.921599 | 0.257301 | 0.782206 | 74.145% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
