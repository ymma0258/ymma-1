# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 6.883367 | 0.000% | 0.204340 | 2.370042 | 0.226137 | 0.873010 | 88.919% |
| 1.5 | 1 | 193472.0 | 31.855% | 2.064270 | 70.011% | 0.038299 | 0.868296 | 0.310283 | 0.748018 | 69.040% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
