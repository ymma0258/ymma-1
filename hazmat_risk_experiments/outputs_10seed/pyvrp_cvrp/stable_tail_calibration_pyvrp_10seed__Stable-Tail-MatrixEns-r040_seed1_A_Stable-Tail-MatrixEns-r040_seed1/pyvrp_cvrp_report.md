# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 5.638036 | 0.000% | 0.180341 | 1.563591 | 0.149134 | 0.874878 | 90.001% |
| 0.25 | 0 | 142005.7 | 5.976% | 4.164443 | 26.137% | 0.126794 | 1.318729 | 0.222176 | 0.870781 | 88.869% |
| 0.5 | 0 | 147580.3 | 10.136% | 2.852588 | 49.405% | 0.078495 | 1.002515 | 0.217789 | 0.842129 | 84.165% |
| 1 | 0 | 156005.6 | 16.424% | 1.933079 | 65.714% | 0.046022 | 0.625870 | 0.223076 | 0.794501 | 77.019% |
| 2 | 0 | 168328.8 | 25.620% | 1.658451 | 70.585% | 0.034265 | 0.501908 | 0.220433 | 0.775951 | 73.865% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
