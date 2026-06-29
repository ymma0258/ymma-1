# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.896748 | 0.000% | 0.226106 | 2.693672 | 0.247272 | 0.880410 | 90.324% |
| 2 | 2 | 203337.0 | 38.578% | 1.988681 | 74.816% | 0.038061 | 0.779442 | 0.275046 | 0.742342 | 67.437% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
