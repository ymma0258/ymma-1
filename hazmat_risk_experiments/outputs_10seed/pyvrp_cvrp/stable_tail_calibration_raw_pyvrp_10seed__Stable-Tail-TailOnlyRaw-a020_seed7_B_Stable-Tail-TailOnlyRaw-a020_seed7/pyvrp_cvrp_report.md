# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.1 | 0.000% | 10.993550 | 0.000% | 0.339533 | 3.255400 | 0.176879 | 0.882357 | 91.356% |
| 0.25 | 0 | 158338.2 | 7.520% | 8.755001 | 20.362% | 0.254881 | 2.965976 | 0.249074 | 0.881438 | 90.201% |
| 0.5 | 0 | 167859.1 | 13.985% | 6.430940 | 41.503% | 0.185119 | 2.421225 | 0.288215 | 0.868067 | 87.280% |
| 1 | 0 | 179061.9 | 21.592% | 4.293798 | 60.943% | 0.112303 | 1.502319 | 0.269958 | 0.839694 | 81.839% |
| 2 | 0 | 196436.9 | 33.391% | 3.608183 | 67.179% | 0.087379 | 1.201609 | 0.252149 | 0.821224 | 78.704% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
