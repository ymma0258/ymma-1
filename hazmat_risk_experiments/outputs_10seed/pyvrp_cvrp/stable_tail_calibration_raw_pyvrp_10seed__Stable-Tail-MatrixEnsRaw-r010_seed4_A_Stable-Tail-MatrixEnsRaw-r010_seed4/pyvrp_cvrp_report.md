# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.021673 | 0.000% | 0.246869 | 2.249542 | 0.151954 | 0.879068 | 90.268% |
| 0.25 | 0 | 143153.3 | 6.832% | 6.083823 | 24.158% | 0.194562 | 1.891740 | 0.240028 | 0.874832 | 89.105% |
| 0.5 | 0 | 150127.7 | 12.037% | 4.441384 | 44.633% | 0.136132 | 1.608529 | 0.306657 | 0.851188 | 85.441% |
| 1 | 0 | 159451.4 | 18.995% | 3.196585 | 60.151% | 0.085767 | 1.091987 | 0.294105 | 0.817840 | 80.274% |
| 2 | 0 | 174713.3 | 30.385% | 2.584015 | 67.787% | 0.062425 | 0.969905 | 0.357355 | 0.790759 | 76.196% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
