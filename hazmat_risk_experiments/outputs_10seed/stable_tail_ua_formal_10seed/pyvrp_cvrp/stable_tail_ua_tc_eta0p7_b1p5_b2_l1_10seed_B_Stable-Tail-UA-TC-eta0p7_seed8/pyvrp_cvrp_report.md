# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146797.4 | 0.000% | 14.292882 | 0.000% | 0.385647 | 4.255444 | 0.177747 | 0.844519 | 87.949% |
| 1.5 | 1 | 222499.1 | 51.569% | 5.490541 | 61.585% | 0.102409 | 2.141829 | 0.371295 | 0.756945 | 75.111% |
| 2 | 1 | 234668.2 | 59.859% | 5.495371 | 61.552% | 0.103426 | 2.175488 | 0.383372 | 0.757221 | 75.067% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
