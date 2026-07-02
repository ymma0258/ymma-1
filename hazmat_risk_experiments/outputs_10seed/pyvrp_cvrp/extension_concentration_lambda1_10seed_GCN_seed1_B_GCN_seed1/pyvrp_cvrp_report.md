# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.346082 | 0.000% | 0.261192 | 2.747818 | 0.218390 | 0.868624 | 89.353% |
| 1 | 0 | 176913.4 | 20.570% | 3.842682 | 53.958% | 0.093228 | 1.309446 | 0.303075 | 0.820139 | 80.695% |
| 1 | 1 | 191537.3 | 30.536% | 3.107756 | 62.764% | 0.074431 | 1.034390 | 0.279495 | 0.797225 | 76.994% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
