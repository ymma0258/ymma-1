# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 7.203500 | 0.000% | 0.228387 | 2.252594 | 0.183893 | 0.870474 | 88.380% |
| 0.25 | 0 | 142528.0 | 6.154% | 5.013527 | 30.402% | 0.142678 | 1.655364 | 0.242090 | 0.856557 | 86.030% |
| 0.5 | 0 | 148037.2 | 10.258% | 3.682942 | 48.873% | 0.105385 | 1.257906 | 0.270676 | 0.831561 | 81.936% |
| 1 | 0 | 155811.6 | 16.048% | 2.431581 | 66.244% | 0.061186 | 0.930334 | 0.269455 | 0.765723 | 72.866% |
| 2 | 0 | 167527.1 | 24.774% | 1.998103 | 72.262% | 0.044644 | 0.645336 | 0.219305 | 0.726303 | 67.079% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
