# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.229509 | 0.000% | 0.238237 | 2.077261 | 0.168624 | 0.873502 | 89.536% |
| 0.25 | 0 | 142990.7 | 6.711% | 4.974157 | 31.196% | 0.148132 | 1.748674 | 0.261499 | 0.863860 | 87.410% |
| 0.5 | 0 | 149125.2 | 11.289% | 3.552331 | 50.863% | 0.100786 | 1.234598 | 0.259548 | 0.834880 | 82.893% |
| 1 | 0 | 158355.4 | 18.177% | 2.627670 | 63.654% | 0.068710 | 0.971339 | 0.296707 | 0.800509 | 77.421% |
| 2 | 0 | 171375.2 | 27.894% | 2.076454 | 71.278% | 0.049925 | 0.669458 | 0.254581 | 0.764614 | 71.854% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
