# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 10.642407 | 0.000% | 0.284726 | 3.085976 | 0.149252 | 0.850111 | 88.392% |
| 1 | 0 | 161768.7 | 20.725% | 3.975081 | 62.649% | 0.081457 | 1.518321 | 0.316464 | 0.756854 | 74.751% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
