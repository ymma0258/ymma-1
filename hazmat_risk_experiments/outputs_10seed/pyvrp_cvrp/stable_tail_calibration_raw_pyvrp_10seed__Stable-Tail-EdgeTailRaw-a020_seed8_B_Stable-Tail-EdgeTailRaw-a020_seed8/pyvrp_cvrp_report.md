# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 7.614869 | 0.000% | 0.235995 | 2.351552 | 0.191412 | 0.860320 | 87.888% |
| 0.25 | 0 | 156912.3 | 6.552% | 6.389365 | 16.094% | 0.174692 | 1.993462 | 0.179068 | 0.856230 | 86.869% |
| 0.5 | 0 | 165521.4 | 12.398% | 4.812134 | 36.806% | 0.120563 | 1.569697 | 0.229252 | 0.833445 | 83.272% |
| 1 | 0 | 175638.9 | 19.268% | 3.060800 | 59.805% | 0.073611 | 1.057096 | 0.225119 | 0.782705 | 75.705% |
| 2 | 0 | 190609.7 | 29.434% | 2.498089 | 67.195% | 0.054288 | 0.744019 | 0.216451 | 0.754764 | 70.870% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
