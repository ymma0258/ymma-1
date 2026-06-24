# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.440807 | 0.000% | 0.291032 | 3.254343 | 0.264998 | 0.855746 | 89.015% |
| 1 | 0 | 179676.0 | 22.453% | 4.943603 | 47.636% | 0.127754 | 1.826413 | 0.292763 | 0.814986 | 82.145% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
