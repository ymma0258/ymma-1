# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.896748 | 0.000% | 0.226106 | 2.693672 | 0.247272 | 0.880410 | 90.324% |
| 3 | 1 | 207725.7 | 41.569% | 2.015824 | 74.473% | 0.038327 | 0.769186 | 0.268876 | 0.745393 | 67.825% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
