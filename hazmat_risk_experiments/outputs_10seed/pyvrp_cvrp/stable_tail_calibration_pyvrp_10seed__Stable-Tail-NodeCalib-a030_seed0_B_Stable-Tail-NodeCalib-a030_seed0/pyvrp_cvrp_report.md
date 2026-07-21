# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 7.560556 | 0.000% | 0.206637 | 2.571246 | 0.251575 | 0.878189 | 89.386% |
| 0.25 | 0 | 156550.7 | 6.596% | 6.405727 | 15.274% | 0.155672 | 2.274412 | 0.261972 | 0.872379 | 88.282% |
| 0.5 | 0 | 164725.3 | 12.162% | 4.281077 | 43.376% | 0.109530 | 1.433161 | 0.235910 | 0.843881 | 83.362% |
| 1 | 0 | 175520.5 | 19.512% | 3.174511 | 58.012% | 0.076885 | 1.150571 | 0.276891 | 0.813612 | 78.465% |
| 2 | 0 | 190311.8 | 29.584% | 2.366303 | 68.702% | 0.049606 | 0.862675 | 0.279640 | 0.770625 | 71.424% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
