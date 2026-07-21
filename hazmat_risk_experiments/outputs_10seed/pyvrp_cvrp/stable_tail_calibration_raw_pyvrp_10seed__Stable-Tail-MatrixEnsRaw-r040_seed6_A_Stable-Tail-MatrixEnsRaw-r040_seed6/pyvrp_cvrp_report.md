# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.2 | 0.000% | 4.883920 | 0.000% | 0.143658 | 1.366267 | 0.155259 | 0.870347 | 89.195% |
| 0.25 | 0 | 143224.5 | 6.779% | 3.122046 | 36.075% | 0.089496 | 1.066332 | 0.285025 | 0.849753 | 85.676% |
| 0.5 | 0 | 149027.9 | 11.106% | 2.506508 | 48.678% | 0.074276 | 1.010472 | 0.338760 | 0.824420 | 82.538% |
| 1 | 0 | 158558.8 | 18.212% | 1.789013 | 63.369% | 0.048615 | 0.560319 | 0.252798 | 0.783153 | 76.460% |
| 2 | 0 | 172630.0 | 28.702% | 1.410641 | 71.117% | 0.033070 | 0.502705 | 0.280982 | 0.734221 | 69.796% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
