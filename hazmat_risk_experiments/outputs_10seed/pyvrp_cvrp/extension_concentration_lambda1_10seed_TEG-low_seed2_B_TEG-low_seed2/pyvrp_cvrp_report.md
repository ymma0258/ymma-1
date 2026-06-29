# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.764525 | 0.000% | 0.284438 | 3.273121 | 0.245837 | 0.843413 | 88.250% |
| 1 | 0 | 179410.9 | 22.272% | 4.942771 | 49.380% | 0.100676 | 1.772606 | 0.264403 | 0.782497 | 78.958% |
| 1 | 1 | 195182.2 | 33.021% | 3.693461 | 62.175% | 0.071084 | 1.547106 | 0.316379 | 0.725979 | 71.521% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
