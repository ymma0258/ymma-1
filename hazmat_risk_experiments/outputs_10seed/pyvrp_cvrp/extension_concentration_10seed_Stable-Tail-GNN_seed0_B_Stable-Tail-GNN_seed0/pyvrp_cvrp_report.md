# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.003160 | 0.000% | 0.253942 | 2.625387 | 0.223399 | 0.881536 | 90.545% |
| 1 | 0 | 176581.3 | 20.344% | 2.863800 | 64.217% | 0.060660 | 1.029346 | 0.281005 | 0.813975 | 78.114% |
| 1 | 0.5 | 182717.7 | 24.526% | 2.607370 | 67.421% | 0.054726 | 0.985907 | 0.290052 | 0.800696 | 75.829% |
| 1 | 1 | 188258.5 | 28.302% | 2.401557 | 69.992% | 0.050629 | 0.989414 | 0.303626 | 0.787521 | 73.584% |
| 1 | 2 | 198168.9 | 35.056% | 2.227138 | 72.172% | 0.046528 | 0.985442 | 0.326460 | 0.774112 | 71.451% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
