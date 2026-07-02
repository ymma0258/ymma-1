# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.755210 | 0.000% | 0.244320 | 2.307465 | 0.171847 | 0.878262 | 89.500% |
| 1 | 0 | 155167.4 | 15.799% | 2.687883 | 65.341% | 0.063050 | 0.889415 | 0.221855 | 0.787063 | 74.982% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
