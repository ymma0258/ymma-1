# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.2 | 0.000% | 6.794083 | 0.000% | 0.201976 | 2.031238 | 0.178067 | 0.870741 | 88.587% |
| 0.25 | 0 | 141626.7 | 5.693% | 4.737893 | 30.264% | 0.141559 | 1.432644 | 0.209618 | 0.854045 | 86.298% |
| 0.5 | 0 | 147161.8 | 9.824% | 3.615082 | 46.791% | 0.107309 | 1.363399 | 0.273981 | 0.831580 | 82.909% |
| 1 | 0 | 155039.7 | 15.703% | 2.350453 | 65.404% | 0.060338 | 0.740295 | 0.248477 | 0.767736 | 73.978% |
| 2 | 0 | 167151.0 | 24.741% | 2.121837 | 68.769% | 0.051308 | 0.728059 | 0.255251 | 0.750283 | 71.068% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
