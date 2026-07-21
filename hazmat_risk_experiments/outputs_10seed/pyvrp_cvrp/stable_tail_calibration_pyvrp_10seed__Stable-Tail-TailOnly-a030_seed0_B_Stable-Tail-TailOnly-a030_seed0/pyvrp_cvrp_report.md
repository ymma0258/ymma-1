# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 7.878751 | 0.000% | 0.217054 | 2.701767 | 0.263403 | 0.882289 | 89.987% |
| 0.25 | 0 | 156040.0 | 6.152% | 6.233838 | 20.878% | 0.153489 | 1.982474 | 0.210587 | 0.874041 | 88.367% |
| 0.5 | 0 | 164109.1 | 11.641% | 4.322361 | 45.139% | 0.107300 | 1.413162 | 0.220183 | 0.844483 | 83.857% |
| 1 | 0 | 173985.2 | 18.359% | 3.011148 | 61.781% | 0.074926 | 1.117919 | 0.300310 | 0.805027 | 77.410% |
| 2 | 0 | 188536.7 | 28.259% | 2.473544 | 68.605% | 0.052042 | 0.974410 | 0.299874 | 0.782970 | 73.160% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
