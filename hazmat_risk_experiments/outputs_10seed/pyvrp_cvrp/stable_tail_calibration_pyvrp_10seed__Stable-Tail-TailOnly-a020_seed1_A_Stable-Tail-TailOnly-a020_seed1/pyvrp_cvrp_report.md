# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 9.468924 | 0.000% | 0.303475 | 2.585672 | 0.147840 | 0.874318 | 90.072% |
| 0.25 | 0 | 141643.1 | 5.705% | 6.819939 | 27.976% | 0.207479 | 2.184639 | 0.248195 | 0.871735 | 88.735% |
| 0.5 | 0 | 147395.2 | 9.998% | 4.914263 | 48.101% | 0.139007 | 1.674392 | 0.242106 | 0.847695 | 84.867% |
| 1 | 0 | 155632.2 | 16.145% | 3.534478 | 62.673% | 0.080406 | 1.109774 | 0.222564 | 0.801965 | 78.361% |
| 2 | 0 | 167788.9 | 25.217% | 2.895726 | 69.419% | 0.062461 | 0.872022 | 0.212415 | 0.780863 | 74.718% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
