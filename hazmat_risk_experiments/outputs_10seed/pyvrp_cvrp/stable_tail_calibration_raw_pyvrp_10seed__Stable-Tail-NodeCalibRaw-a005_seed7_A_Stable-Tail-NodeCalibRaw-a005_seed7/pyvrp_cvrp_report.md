# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.2 | 0.000% | 9.219983 | 0.000% | 0.299815 | 2.660490 | 0.168613 | 0.872811 | 89.361% |
| 0.25 | 0 | 143565.3 | 6.821% | 6.071417 | 34.149% | 0.172544 | 1.909442 | 0.216424 | 0.856547 | 86.643% |
| 0.5 | 0 | 149450.1 | 11.199% | 4.675493 | 49.290% | 0.135021 | 1.688951 | 0.244549 | 0.835406 | 83.328% |
| 1 | 0 | 158618.0 | 18.021% | 3.290042 | 64.316% | 0.089901 | 1.215238 | 0.285456 | 0.798591 | 77.215% |
| 2 | 0 | 171918.2 | 27.917% | 2.473016 | 73.178% | 0.055825 | 0.870432 | 0.294331 | 0.752404 | 70.164% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
