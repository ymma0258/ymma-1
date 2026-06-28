# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.275491 | 0.000% | 0.291917 | 3.021439 | 0.209019 | 0.877111 | 89.848% |
| 0.5 | 0 | 166195.3 | 13.265% | 5.482366 | 40.894% | 0.143276 | 1.944148 | 0.267637 | 0.849541 | 84.674% |
| 1 | 0 | 176937.1 | 20.586% | 3.939516 | 57.528% | 0.092070 | 1.611153 | 0.356868 | 0.821067 | 79.929% |
| 1.5 | 0 | 185059.8 | 26.122% | 3.113461 | 66.433% | 0.063248 | 1.345861 | 0.323149 | 0.796557 | 75.707% |
| 2 | 0 | 192699.4 | 31.328% | 3.098694 | 66.593% | 0.062068 | 1.406944 | 0.353767 | 0.793335 | 75.444% |
| 3 | 0 | 207413.0 | 41.356% | 2.921618 | 68.502% | 0.055065 | 1.393592 | 0.376838 | 0.781552 | 73.525% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
