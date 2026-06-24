# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.991640 | 0.000% | 0.258755 | 2.568101 | 0.139689 | 0.851847 | 88.660% |
| 1 | 0 | 160639.8 | 19.883% | 3.729168 | 58.526% | 0.103210 | 1.322455 | 0.277291 | 0.770730 | 76.987% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
