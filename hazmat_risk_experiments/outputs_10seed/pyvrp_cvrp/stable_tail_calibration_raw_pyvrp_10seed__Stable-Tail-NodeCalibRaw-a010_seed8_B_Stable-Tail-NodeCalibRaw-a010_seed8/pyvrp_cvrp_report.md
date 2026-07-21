# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.1 | 0.000% | 7.755486 | 0.000% | 0.239823 | 2.402264 | 0.206284 | 0.859317 | 87.728% |
| 0.25 | 0 | 156758.2 | 6.351% | 6.480110 | 16.445% | 0.155900 | 2.098984 | 0.206112 | 0.854132 | 86.995% |
| 0.5 | 0 | 165168.5 | 12.057% | 4.775459 | 38.425% | 0.117990 | 1.718659 | 0.257594 | 0.836019 | 83.444% |
| 1 | 0 | 176253.7 | 19.577% | 3.208855 | 58.625% | 0.075308 | 1.107250 | 0.235112 | 0.787086 | 76.241% |
| 2 | 0 | 191559.1 | 29.961% | 2.516275 | 67.555% | 0.048620 | 0.778803 | 0.221263 | 0.752681 | 70.831% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
