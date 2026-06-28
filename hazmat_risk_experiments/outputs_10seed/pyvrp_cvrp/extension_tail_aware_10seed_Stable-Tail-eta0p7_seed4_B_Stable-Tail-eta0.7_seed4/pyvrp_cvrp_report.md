# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 12.572288 | 0.000% | 0.278488 | 3.948670 | 0.187305 | 0.876604 | 89.916% |
| 1 | 0 | 177219.3 | 20.778% | 4.906105 | 60.977% | 0.060560 | 1.898987 | 0.323324 | 0.809664 | 77.883% |
| 2 | 0 | 193538.7 | 31.900% | 4.123811 | 67.199% | 0.048985 | 1.844104 | 0.365067 | 0.786706 | 74.310% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
