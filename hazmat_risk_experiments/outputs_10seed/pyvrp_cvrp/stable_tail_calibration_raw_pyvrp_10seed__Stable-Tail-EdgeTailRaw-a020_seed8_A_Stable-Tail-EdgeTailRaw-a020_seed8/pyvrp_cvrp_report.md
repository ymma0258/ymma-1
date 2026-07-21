# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.8 | 0.000% | 8.138945 | 0.000% | 0.262240 | 2.551470 | 0.189632 | 0.870429 | 88.597% |
| 0.25 | 0 | 142995.4 | 6.397% | 5.499201 | 32.433% | 0.154291 | 1.725819 | 0.214015 | 0.856580 | 86.844% |
| 0.5 | 0 | 149265.3 | 11.062% | 4.176100 | 48.690% | 0.118793 | 1.596986 | 0.267956 | 0.836378 | 83.497% |
| 1 | 0 | 157881.2 | 17.473% | 2.976597 | 63.428% | 0.077118 | 0.846489 | 0.173624 | 0.790710 | 77.163% |
| 2 | 0 | 172552.2 | 28.389% | 2.362938 | 70.968% | 0.048856 | 0.750730 | 0.241163 | 0.757058 | 71.617% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
