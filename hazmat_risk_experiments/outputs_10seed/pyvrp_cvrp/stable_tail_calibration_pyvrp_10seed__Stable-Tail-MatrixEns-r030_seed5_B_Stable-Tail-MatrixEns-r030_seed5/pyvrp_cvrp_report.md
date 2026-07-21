# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 5.406952 | 0.000% | 0.168321 | 1.763766 | 0.218589 | 0.874431 | 88.981% |
| 0.25 | 0 | 156106.3 | 6.245% | 4.773164 | 11.722% | 0.121941 | 1.452590 | 0.193198 | 0.873164 | 88.859% |
| 0.5 | 0 | 164676.7 | 12.078% | 3.610488 | 33.225% | 0.085226 | 1.144719 | 0.212723 | 0.848135 | 84.907% |
| 1 | 0 | 175032.8 | 19.126% | 2.432956 | 55.003% | 0.059348 | 0.798718 | 0.249702 | 0.815291 | 79.360% |
| 2 | 0 | 190816.1 | 29.868% | 1.946519 | 64.000% | 0.046625 | 0.592836 | 0.243304 | 0.792133 | 75.138% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
