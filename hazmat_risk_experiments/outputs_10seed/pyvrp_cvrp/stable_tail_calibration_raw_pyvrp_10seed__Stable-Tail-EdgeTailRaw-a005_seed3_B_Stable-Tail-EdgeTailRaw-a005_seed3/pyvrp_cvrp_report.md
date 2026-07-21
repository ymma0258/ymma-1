# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.0 | 0.000% | 7.048301 | 0.000% | 0.214342 | 2.401343 | 0.254271 | 0.869741 | 89.071% |
| 0.25 | 0 | 155559.2 | 5.538% | 5.683001 | 19.371% | 0.140586 | 2.023090 | 0.256717 | 0.863597 | 87.691% |
| 0.5 | 0 | 163740.2 | 11.088% | 4.561865 | 35.277% | 0.114976 | 1.725638 | 0.291115 | 0.850751 | 85.218% |
| 1 | 0 | 175347.5 | 18.963% | 3.369643 | 52.192% | 0.084175 | 1.415315 | 0.310427 | 0.830880 | 81.290% |
| 2 | 0 | 192536.1 | 30.624% | 2.787368 | 60.453% | 0.069433 | 1.142918 | 0.303756 | 0.811592 | 77.949% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
