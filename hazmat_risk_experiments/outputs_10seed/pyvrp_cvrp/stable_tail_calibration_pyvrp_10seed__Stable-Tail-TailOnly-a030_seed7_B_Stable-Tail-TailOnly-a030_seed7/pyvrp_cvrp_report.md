# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 10.574025 | 0.000% | 0.320502 | 3.188724 | 0.179072 | 0.881403 | 91.017% |
| 0.25 | 0 | 157717.4 | 7.390% | 7.460149 | 29.448% | 0.199389 | 2.648762 | 0.277282 | 0.873727 | 88.544% |
| 0.5 | 0 | 167476.7 | 14.035% | 5.711347 | 45.987% | 0.157006 | 1.978551 | 0.256156 | 0.855460 | 85.421% |
| 1 | 0 | 178792.9 | 21.741% | 4.071124 | 61.499% | 0.106486 | 1.365514 | 0.233544 | 0.830660 | 80.742% |
| 2 | 0 | 195314.8 | 32.990% | 3.372327 | 68.107% | 0.076747 | 1.061608 | 0.216883 | 0.809782 | 77.357% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
