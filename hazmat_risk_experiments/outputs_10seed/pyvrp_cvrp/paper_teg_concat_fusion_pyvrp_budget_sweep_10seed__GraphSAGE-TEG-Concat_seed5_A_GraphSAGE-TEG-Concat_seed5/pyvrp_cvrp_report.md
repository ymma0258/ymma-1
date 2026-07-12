# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134531.0 | 0.000% | 9.702278 | 0.000% | 0.313492 | 2.897469 | 0.180325 | 0.883636 | 90.265% |
| 0.25 | 0 | 144392.9 | 7.331% | 5.882208 | 39.373% | 0.173891 | 1.739614 | 0.197544 | 0.864429 | 86.709% |
| 0.5 | 0 | 150849.8 | 12.130% | 4.639722 | 52.179% | 0.130442 | 1.753157 | 0.291430 | 0.846765 | 83.930% |
| 1 | 0 | 160215.9 | 19.092% | 2.924218 | 69.860% | 0.062367 | 1.028747 | 0.271887 | 0.795153 | 75.336% |
| 2 | 0 | 173068.1 | 28.646% | 2.177700 | 77.555% | 0.043093 | 0.804731 | 0.261503 | 0.745526 | 67.620% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
