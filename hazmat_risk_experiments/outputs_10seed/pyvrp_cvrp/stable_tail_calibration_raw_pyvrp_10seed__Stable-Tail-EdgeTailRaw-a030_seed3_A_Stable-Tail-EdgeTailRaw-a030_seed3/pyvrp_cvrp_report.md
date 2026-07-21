# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134531.2 | 0.000% | 7.217154 | 0.000% | 0.225515 | 2.289969 | 0.199425 | 0.872911 | 88.860% |
| 0.25 | 0 | 141793.2 | 5.398% | 4.770363 | 33.902% | 0.137484 | 1.546806 | 0.218244 | 0.856623 | 86.600% |
| 0.5 | 0 | 147360.2 | 9.536% | 3.938123 | 45.434% | 0.114183 | 1.387215 | 0.243113 | 0.843038 | 84.338% |
| 1 | 0 | 154922.7 | 15.157% | 2.358311 | 67.324% | 0.060891 | 0.746031 | 0.235141 | 0.772307 | 74.360% |
| 2 | 0 | 166715.0 | 23.923% | 2.214494 | 69.316% | 0.054358 | 0.733673 | 0.264157 | 0.758439 | 72.467% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
