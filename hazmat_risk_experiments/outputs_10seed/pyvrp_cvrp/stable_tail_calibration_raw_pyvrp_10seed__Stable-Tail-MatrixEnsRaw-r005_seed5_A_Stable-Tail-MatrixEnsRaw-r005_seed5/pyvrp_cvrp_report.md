# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.0 | 0.000% | 7.104339 | 0.000% | 0.223126 | 1.969506 | 0.158217 | 0.872438 | 88.819% |
| 0.25 | 0 | 142585.4 | 6.250% | 5.091233 | 28.336% | 0.144516 | 1.734058 | 0.241895 | 0.863572 | 87.055% |
| 0.5 | 0 | 148225.7 | 10.453% | 3.426359 | 51.771% | 0.100034 | 1.290102 | 0.306915 | 0.823725 | 81.183% |
| 1 | 0 | 156332.5 | 16.494% | 2.388454 | 66.380% | 0.061290 | 0.943453 | 0.293386 | 0.770095 | 73.636% |
| 2 | 0 | 168113.9 | 25.273% | 1.725604 | 75.711% | 0.036812 | 0.576394 | 0.247839 | 0.708433 | 64.278% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
