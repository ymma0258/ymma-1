# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 6.881138 | 0.000% | 0.212138 | 2.026575 | 0.167162 | 0.867595 | 88.427% |
| 0.25 | 0 | 142997.2 | 6.716% | 4.818095 | 29.981% | 0.137468 | 1.550845 | 0.236740 | 0.858390 | 86.894% |
| 0.5 | 0 | 149169.4 | 11.322% | 3.616623 | 47.442% | 0.102666 | 1.479561 | 0.277842 | 0.827484 | 82.558% |
| 1 | 0 | 158343.2 | 18.168% | 2.521526 | 63.356% | 0.064348 | 0.728952 | 0.188602 | 0.781290 | 75.759% |
| 2 | 0 | 173118.3 | 29.195% | 2.024947 | 70.572% | 0.042957 | 0.595419 | 0.190063 | 0.747672 | 70.204% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
