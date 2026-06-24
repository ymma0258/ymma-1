# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.896748 | 0.000% | 0.226106 | 2.693672 | 0.247272 | 0.880410 | 90.324% |
| 0.25 | 0 | 155970.3 | 6.297% | 6.737579 | 14.679% | 0.203309 | 2.604396 | 0.278832 | 0.877500 | 89.470% |
| 0.5 | 0 | 163946.8 | 11.733% | 4.683940 | 40.685% | 0.126322 | 1.542460 | 0.245538 | 0.856298 | 84.949% |
| 1 | 0 | 172466.1 | 17.539% | 2.534512 | 67.904% | 0.053090 | 0.923329 | 0.287799 | 0.788145 | 74.429% |
| 2 | 0 | 183744.2 | 25.225% | 2.145795 | 72.827% | 0.042291 | 0.761580 | 0.244510 | 0.753096 | 69.564% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
