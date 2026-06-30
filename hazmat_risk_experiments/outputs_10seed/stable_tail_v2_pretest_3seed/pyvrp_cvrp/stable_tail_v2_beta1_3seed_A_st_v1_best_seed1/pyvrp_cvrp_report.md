# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 8.306538 | 0.000% | 0.264863 | 2.389725 | 0.128088 | 0.867255 | 89.491% |
| 1 | 0 | 157817.7 | 17.777% | 3.298695 | 60.288% | 0.070164 | 0.912319 | 0.165161 | 0.802367 | 78.257% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
