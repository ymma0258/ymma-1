# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.315298 | 0.000% | 0.208039 | 2.324658 | 0.196457 | 0.853593 | 88.032% |
| 1 | 0 | 157451.4 | 17.503% | 2.776051 | 62.051% | 0.061627 | 0.935800 | 0.224519 | 0.745261 | 73.826% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
