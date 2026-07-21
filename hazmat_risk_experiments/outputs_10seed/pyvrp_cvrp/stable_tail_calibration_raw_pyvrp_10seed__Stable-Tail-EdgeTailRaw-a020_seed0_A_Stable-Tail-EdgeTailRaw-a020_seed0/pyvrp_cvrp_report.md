# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.1 | 0.000% | 8.031231 | 0.000% | 0.251518 | 2.418023 | 0.198635 | 0.883640 | 90.408% |
| 0.25 | 0 | 142129.9 | 5.753% | 4.950222 | 38.363% | 0.148732 | 1.508817 | 0.198441 | 0.867921 | 87.297% |
| 0.5 | 0 | 147938.0 | 10.074% | 3.951441 | 50.799% | 0.117941 | 1.439773 | 0.266793 | 0.847145 | 84.401% |
| 1 | 0 | 155370.7 | 15.605% | 2.524337 | 68.568% | 0.063282 | 0.952102 | 0.246794 | 0.788426 | 75.916% |
| 2 | 0 | 167191.6 | 24.400% | 1.819151 | 77.349% | 0.034500 | 0.598367 | 0.232521 | 0.735237 | 67.555% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
