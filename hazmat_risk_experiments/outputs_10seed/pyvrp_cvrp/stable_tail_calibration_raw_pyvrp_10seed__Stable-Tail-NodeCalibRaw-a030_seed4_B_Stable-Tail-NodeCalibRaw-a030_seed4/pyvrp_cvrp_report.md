# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.4 | 0.000% | 8.522258 | 0.000% | 0.259869 | 2.615838 | 0.185387 | 0.872902 | 89.076% |
| 0.25 | 0 | 156246.3 | 6.196% | 7.281797 | 14.556% | 0.195456 | 2.259970 | 0.198993 | 0.869805 | 88.085% |
| 0.5 | 0 | 164724.3 | 11.958% | 5.478909 | 35.711% | 0.146922 | 2.027623 | 0.320816 | 0.850186 | 84.624% |
| 1 | 0 | 175121.2 | 19.024% | 3.972146 | 53.391% | 0.097106 | 1.582015 | 0.328244 | 0.822612 | 80.227% |
| 2 | 0 | 191370.6 | 30.069% | 3.283614 | 61.470% | 0.071785 | 1.184347 | 0.285980 | 0.804457 | 77.305% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
