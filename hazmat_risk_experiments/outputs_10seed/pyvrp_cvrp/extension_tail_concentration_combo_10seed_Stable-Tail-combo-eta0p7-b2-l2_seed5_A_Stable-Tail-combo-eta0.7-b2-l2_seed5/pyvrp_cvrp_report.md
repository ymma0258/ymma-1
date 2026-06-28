# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 6.282950 | 0.000% | 0.177174 | 1.869566 | 0.168377 | 0.875220 | 89.237% |
| 2 | 2 | 180983.4 | 35.065% | 1.495434 | 76.199% | 0.030520 | 0.412131 | 0.188211 | 0.695220 | 61.194% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
