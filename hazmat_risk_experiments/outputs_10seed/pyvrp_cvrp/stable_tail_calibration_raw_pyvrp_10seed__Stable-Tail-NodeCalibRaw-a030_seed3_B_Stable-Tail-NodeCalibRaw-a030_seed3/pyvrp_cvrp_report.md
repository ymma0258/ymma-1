# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.4 | 0.000% | 6.985064 | 0.000% | 0.190901 | 2.226677 | 0.222689 | 0.868168 | 88.846% |
| 0.25 | 0 | 155208.3 | 5.490% | 6.018604 | 13.836% | 0.146718 | 2.223136 | 0.286147 | 0.864474 | 88.169% |
| 0.5 | 0 | 163188.3 | 10.914% | 4.781246 | 31.550% | 0.123461 | 1.820324 | 0.258918 | 0.854905 | 85.870% |
| 1 | 0 | 174946.3 | 18.906% | 3.776729 | 45.931% | 0.101268 | 1.487344 | 0.292486 | 0.840742 | 82.940% |
| 2 | 0 | 192488.4 | 30.828% | 2.773180 | 60.298% | 0.068505 | 1.178227 | 0.309579 | 0.810501 | 77.459% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
