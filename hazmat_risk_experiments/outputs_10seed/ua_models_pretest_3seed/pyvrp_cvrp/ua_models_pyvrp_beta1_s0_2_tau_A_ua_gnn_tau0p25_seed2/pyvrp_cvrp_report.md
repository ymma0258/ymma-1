# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 10.414095 | 0.000% | 0.328720 | 2.995789 | 0.132173 | 0.844060 | 88.167% |
| 1 | 0 | 161355.0 | 20.417% | 4.450394 | 57.266% | 0.110383 | 1.333361 | 0.201603 | 0.775014 | 77.878% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
