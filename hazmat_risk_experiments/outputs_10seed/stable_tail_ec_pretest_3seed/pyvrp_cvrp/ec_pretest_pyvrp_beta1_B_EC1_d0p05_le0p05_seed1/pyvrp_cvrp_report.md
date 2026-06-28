# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.337550 | 0.000% | 0.311049 | 3.324913 | 0.207520 | 0.873236 | 91.298% |
| 1 | 0 | 178979.8 | 21.978% | 4.744376 | 54.105% | 0.124907 | 1.580794 | 0.263378 | 0.846663 | 83.714% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
