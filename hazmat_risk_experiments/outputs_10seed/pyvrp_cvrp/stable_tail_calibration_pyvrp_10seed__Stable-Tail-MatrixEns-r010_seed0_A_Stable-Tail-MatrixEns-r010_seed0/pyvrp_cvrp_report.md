# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 6.995574 | 0.000% | 0.207546 | 2.172325 | 0.210008 | 0.883694 | 90.372% |
| 0.25 | 0 | 142422.0 | 6.287% | 4.041928 | 42.222% | 0.122594 | 1.415365 | 0.250609 | 0.859200 | 86.092% |
| 0.5 | 0 | 148189.6 | 10.591% | 3.482105 | 50.224% | 0.101833 | 1.524679 | 0.323883 | 0.846178 | 84.373% |
| 1 | 0 | 155929.4 | 16.367% | 2.152535 | 69.230% | 0.048364 | 0.809881 | 0.243646 | 0.785057 | 75.121% |
| 2 | 0 | 167950.6 | 25.338% | 1.623833 | 76.788% | 0.029412 | 0.521412 | 0.231162 | 0.733470 | 67.192% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
