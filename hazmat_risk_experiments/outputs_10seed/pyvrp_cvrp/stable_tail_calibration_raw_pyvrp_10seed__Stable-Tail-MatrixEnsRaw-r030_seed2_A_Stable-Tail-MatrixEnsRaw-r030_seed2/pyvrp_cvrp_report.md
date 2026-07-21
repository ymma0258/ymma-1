# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 6.218938 | 0.000% | 0.209546 | 1.921068 | 0.192899 | 0.877493 | 89.860% |
| 0.25 | 0 | 142381.1 | 6.150% | 4.002205 | 35.645% | 0.118029 | 1.497017 | 0.297904 | 0.863825 | 87.456% |
| 0.5 | 0 | 148567.9 | 10.763% | 3.387256 | 45.533% | 0.100565 | 1.252230 | 0.266427 | 0.853981 | 85.550% |
| 1 | 0 | 157632.5 | 17.521% | 2.302040 | 62.983% | 0.062617 | 0.828342 | 0.294039 | 0.813038 | 79.322% |
| 2 | 0 | 171891.3 | 28.151% | 2.044061 | 67.132% | 0.050592 | 0.837737 | 0.341446 | 0.795810 | 76.418% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
