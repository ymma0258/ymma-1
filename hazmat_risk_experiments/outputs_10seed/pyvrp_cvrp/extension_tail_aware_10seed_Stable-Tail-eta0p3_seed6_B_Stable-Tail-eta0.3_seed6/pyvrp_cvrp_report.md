# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 11.117272 | 0.000% | 0.298447 | 3.724609 | 0.232779 | 0.884269 | 90.416% |
| 1 | 0 | 179788.6 | 22.529% | 4.775499 | 57.044% | 0.101925 | 1.838441 | 0.350526 | 0.841357 | 80.979% |
| 2 | 0 | 199760.2 | 36.141% | 4.242334 | 61.840% | 0.095406 | 1.743539 | 0.364255 | 0.832465 | 79.356% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
