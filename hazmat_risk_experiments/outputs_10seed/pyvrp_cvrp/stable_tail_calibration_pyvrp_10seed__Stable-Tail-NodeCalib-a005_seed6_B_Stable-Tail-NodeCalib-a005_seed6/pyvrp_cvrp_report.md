# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.4 | 0.000% | 8.977040 | 0.000% | 0.264436 | 3.105413 | 0.245011 | 0.869509 | 89.574% |
| 0.25 | 0 | 158431.9 | 7.486% | 7.743658 | 13.739% | 0.208691 | 2.643244 | 0.230735 | 0.866792 | 88.828% |
| 0.5 | 0 | 168909.3 | 14.594% | 6.090114 | 32.159% | 0.156564 | 2.312149 | 0.292586 | 0.857425 | 86.564% |
| 1 | 0 | 182021.8 | 23.491% | 4.160307 | 53.656% | 0.103806 | 1.508176 | 0.308982 | 0.825563 | 81.035% |
| 2 | 0 | 203518.0 | 38.074% | 3.714873 | 58.618% | 0.093315 | 1.404658 | 0.328480 | 0.816205 | 79.077% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
