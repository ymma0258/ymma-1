# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 6.580157 | 0.000% | 0.200800 | 2.201141 | 0.242380 | 0.868789 | 88.878% |
| 0.25 | 0 | 155347.8 | 5.681% | 5.260995 | 20.048% | 0.133137 | 1.883683 | 0.267900 | 0.863082 | 87.556% |
| 0.5 | 0 | 162969.1 | 10.865% | 4.400870 | 33.119% | 0.109502 | 1.583759 | 0.240666 | 0.850370 | 85.412% |
| 1 | 0 | 175059.9 | 19.091% | 3.473579 | 47.211% | 0.088585 | 1.367681 | 0.287655 | 0.835298 | 82.509% |
| 2 | 0 | 192400.4 | 30.887% | 2.582940 | 60.747% | 0.063961 | 1.041509 | 0.289559 | 0.805066 | 77.041% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
