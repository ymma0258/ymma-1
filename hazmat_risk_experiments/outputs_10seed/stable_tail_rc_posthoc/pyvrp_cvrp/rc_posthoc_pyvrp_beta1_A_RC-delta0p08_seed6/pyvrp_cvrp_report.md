# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.763069 | 0.000% | 0.228352 | 2.202106 | 0.145691 | 0.877850 | 89.496% |
| 1 | 0 | 159086.5 | 18.723% | 2.922586 | 62.353% | 0.072783 | 1.010877 | 0.308247 | 0.803507 | 77.360% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
