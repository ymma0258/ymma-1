# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.7 | 0.000% | 9.758927 | 0.000% | 0.287956 | 3.096461 | 0.202847 | 0.876744 | 90.241% |
| 0.25 | 0 | 157866.0 | 7.151% | 8.335999 | 14.581% | 0.244629 | 2.881653 | 0.249934 | 0.877087 | 89.750% |
| 0.5 | 0 | 167430.8 | 13.643% | 5.930626 | 39.229% | 0.168528 | 2.285160 | 0.298331 | 0.857978 | 85.859% |
| 1 | 0 | 178925.1 | 21.445% | 4.071196 | 58.282% | 0.103372 | 1.399231 | 0.219023 | 0.826982 | 80.299% |
| 2 | 0 | 196086.5 | 33.093% | 3.365577 | 65.513% | 0.071986 | 1.088478 | 0.232469 | 0.811617 | 77.238% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
