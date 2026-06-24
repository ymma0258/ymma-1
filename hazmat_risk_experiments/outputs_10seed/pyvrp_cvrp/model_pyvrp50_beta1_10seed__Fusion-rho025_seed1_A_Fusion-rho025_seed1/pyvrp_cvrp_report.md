# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.371315 | 0.000% | 0.211801 | 2.228653 | 0.174343 | 0.859668 | 88.134% |
| 1 | 0 | 157076.7 | 17.224% | 2.917482 | 60.421% | 0.073615 | 1.026628 | 0.253151 | 0.762497 | 74.861% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
