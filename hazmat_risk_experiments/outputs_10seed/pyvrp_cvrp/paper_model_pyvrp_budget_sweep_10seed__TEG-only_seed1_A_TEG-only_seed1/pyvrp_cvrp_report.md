# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.7 | 0.000% | 8.101764 | 0.000% | 0.263512 | 2.430854 | 0.167417 | 0.835409 | 86.023% |
| 0.25 | 0 | 142716.0 | 6.295% | 5.115117 | 36.864% | 0.141684 | 1.601988 | 0.198905 | 0.798645 | 81.250% |
| 0.5 | 0 | 148658.7 | 10.721% | 4.276865 | 47.211% | 0.101063 | 1.571669 | 0.280471 | 0.766215 | 77.151% |
| 1 | 0 | 156988.1 | 16.924% | 2.928788 | 63.850% | 0.059471 | 0.985659 | 0.231672 | 0.682237 | 67.181% |
| 2 | 0 | 171127.9 | 27.456% | 2.669106 | 67.055% | 0.051702 | 0.902445 | 0.225072 | 0.656459 | 63.646% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
