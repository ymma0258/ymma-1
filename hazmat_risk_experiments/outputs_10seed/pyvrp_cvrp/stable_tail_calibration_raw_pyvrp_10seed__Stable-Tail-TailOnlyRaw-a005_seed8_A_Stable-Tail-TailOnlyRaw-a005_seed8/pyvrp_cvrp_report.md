# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 8.272368 | 0.000% | 0.266010 | 2.677741 | 0.194413 | 0.868842 | 88.422% |
| 0.25 | 0 | 143532.7 | 6.850% | 5.328419 | 35.588% | 0.150562 | 1.458603 | 0.132788 | 0.853263 | 86.654% |
| 0.5 | 0 | 149827.1 | 11.535% | 3.816096 | 53.869% | 0.110314 | 1.404845 | 0.258818 | 0.819135 | 81.325% |
| 1 | 0 | 158931.0 | 18.313% | 2.804517 | 66.098% | 0.068505 | 0.832870 | 0.201285 | 0.781886 | 75.721% |
| 2 | 0 | 174173.9 | 29.660% | 2.317782 | 71.982% | 0.046095 | 0.728970 | 0.221562 | 0.751026 | 70.711% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
