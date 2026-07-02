# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.971653 | 0.000% | 0.293216 | 3.210650 | 0.207724 | 0.875816 | 91.674% |
| 1 | 0 | 179233.2 | 22.151% | 4.647972 | 53.388% | 0.127703 | 1.688654 | 0.283018 | 0.853732 | 84.368% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
