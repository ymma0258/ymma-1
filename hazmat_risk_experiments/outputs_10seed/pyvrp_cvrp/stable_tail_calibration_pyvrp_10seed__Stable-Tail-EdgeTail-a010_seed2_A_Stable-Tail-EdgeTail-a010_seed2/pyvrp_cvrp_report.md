# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 9.134142 | 0.000% | 0.305603 | 2.977259 | 0.207687 | 0.878992 | 89.840% |
| 0.25 | 0 | 142645.1 | 6.242% | 6.048749 | 33.779% | 0.171139 | 2.029724 | 0.229711 | 0.866137 | 87.817% |
| 0.5 | 0 | 148452.0 | 10.567% | 4.751548 | 47.980% | 0.142105 | 1.622200 | 0.253291 | 0.853996 | 85.339% |
| 1 | 0 | 157384.9 | 17.220% | 3.291583 | 63.964% | 0.088410 | 1.319590 | 0.365429 | 0.813562 | 79.306% |
| 2 | 0 | 171829.5 | 27.978% | 3.000470 | 67.151% | 0.073179 | 1.193811 | 0.317562 | 0.802505 | 77.363% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
