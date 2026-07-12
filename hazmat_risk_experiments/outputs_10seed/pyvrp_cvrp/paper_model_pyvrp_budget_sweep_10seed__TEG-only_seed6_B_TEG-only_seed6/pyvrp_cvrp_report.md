# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.6 | 0.000% | 8.099905 | 0.000% | 0.225208 | 2.470858 | 0.184317 | 0.830453 | 85.285% |
| 0.25 | 0 | 158026.1 | 7.308% | 7.163548 | 11.560% | 0.174211 | 2.309929 | 0.208182 | 0.825374 | 84.719% |
| 0.5 | 0 | 167582.3 | 13.798% | 5.668942 | 30.012% | 0.136466 | 1.780032 | 0.204336 | 0.799913 | 81.127% |
| 1 | 0 | 180814.9 | 22.783% | 4.053283 | 49.959% | 0.095997 | 1.264101 | 0.223894 | 0.745153 | 73.758% |
| 2 | 0 | 200589.0 | 36.211% | 3.314078 | 59.085% | 0.070578 | 1.050689 | 0.232227 | 0.706629 | 68.565% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
