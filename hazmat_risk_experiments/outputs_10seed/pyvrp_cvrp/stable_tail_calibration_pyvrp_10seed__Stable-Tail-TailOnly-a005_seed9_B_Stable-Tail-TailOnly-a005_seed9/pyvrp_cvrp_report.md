# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.1 | 0.000% | 8.959765 | 0.000% | 0.275313 | 2.925994 | 0.226088 | 0.871469 | 90.159% |
| 0.25 | 0 | 158973.6 | 7.951% | 7.638716 | 14.744% | 0.215719 | 2.425155 | 0.225805 | 0.868182 | 89.205% |
| 0.5 | 0 | 168480.0 | 14.407% | 5.141873 | 42.612% | 0.135996 | 1.626297 | 0.236345 | 0.844167 | 85.012% |
| 1 | 0 | 179983.1 | 22.218% | 3.598301 | 59.839% | 0.080776 | 1.346293 | 0.307734 | 0.814664 | 79.767% |
| 2 | 0 | 197383.9 | 34.034% | 3.082579 | 65.595% | 0.063305 | 0.980944 | 0.256793 | 0.795462 | 76.597% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
