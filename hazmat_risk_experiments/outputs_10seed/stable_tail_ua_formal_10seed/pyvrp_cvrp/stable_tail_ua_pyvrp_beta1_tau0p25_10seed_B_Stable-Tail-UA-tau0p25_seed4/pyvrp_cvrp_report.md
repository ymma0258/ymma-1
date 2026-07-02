# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 12.702124 | 0.000% | 0.320277 | 3.998947 | 0.198789 | 0.857420 | 89.026% |
| 1 | 0 | 182755.7 | 24.552% | 5.626658 | 55.703% | 0.112830 | 1.815681 | 0.215612 | 0.799175 | 79.912% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
