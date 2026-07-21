# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 7.451105 | 0.000% | 0.225148 | 2.222240 | 0.177393 | 0.875389 | 89.447% |
| 0.25 | 0 | 141678.0 | 5.469% | 4.913170 | 34.061% | 0.140473 | 1.515520 | 0.208926 | 0.858962 | 86.939% |
| 0.5 | 0 | 147176.1 | 9.562% | 3.685592 | 50.536% | 0.105030 | 1.366658 | 0.265557 | 0.833721 | 83.233% |
| 1 | 0 | 155273.3 | 15.590% | 2.423461 | 67.475% | 0.063613 | 0.722739 | 0.225575 | 0.771086 | 74.548% |
| 2 | 0 | 166979.9 | 24.305% | 2.187921 | 70.636% | 0.052834 | 0.689524 | 0.234386 | 0.754596 | 71.863% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
