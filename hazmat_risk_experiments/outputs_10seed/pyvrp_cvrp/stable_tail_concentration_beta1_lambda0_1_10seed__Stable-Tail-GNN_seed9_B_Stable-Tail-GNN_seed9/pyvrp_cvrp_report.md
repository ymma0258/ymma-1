# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.896748 | 0.000% | 0.226106 | 2.693672 | 0.247272 | 0.880410 | 90.324% |
| 1 | 0 | 172466.1 | 17.539% | 2.534512 | 67.904% | 0.053090 | 0.923329 | 0.287799 | 0.788145 | 74.429% |
| 1 | 1 | 180717.2 | 23.162% | 2.138823 | 72.915% | 0.043044 | 0.738420 | 0.230246 | 0.753600 | 69.602% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
