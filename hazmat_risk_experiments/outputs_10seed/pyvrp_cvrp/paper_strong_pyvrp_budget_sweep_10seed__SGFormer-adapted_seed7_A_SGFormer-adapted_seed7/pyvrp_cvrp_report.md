# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 8.546579 | 0.000% | 0.278769 | 2.752906 | 0.217096 | 0.872312 | 87.909% |
| 0.25 | 0 | 143781.6 | 6.982% | 4.922620 | 42.402% | 0.121876 | 1.891909 | 0.297817 | 0.844396 | 82.163% |
| 0.5 | 0 | 149567.9 | 11.287% | 3.990065 | 53.314% | 0.091297 | 1.638082 | 0.296240 | 0.815176 | 77.828% |
| 1 | 0 | 157363.2 | 17.087% | 2.523193 | 70.477% | 0.048403 | 0.866873 | 0.241926 | 0.742075 | 66.857% |
| 2 | 0 | 168575.1 | 25.430% | 1.988323 | 76.735% | 0.033376 | 0.583948 | 0.200856 | 0.691266 | 59.016% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
