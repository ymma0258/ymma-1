# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.0 | 0.000% | 9.726224 | 0.000% | 0.306385 | 3.426007 | 0.260385 | 0.873171 | 89.883% |
| 0.25 | 0 | 156359.1 | 6.224% | 7.916535 | 18.606% | 0.222431 | 2.432125 | 0.218243 | 0.869728 | 88.592% |
| 0.5 | 0 | 164828.6 | 11.978% | 6.814920 | 29.933% | 0.188447 | 2.281598 | 0.251462 | 0.861670 | 87.174% |
| 1 | 0 | 174540.6 | 18.576% | 3.979938 | 59.080% | 0.094337 | 1.442724 | 0.251875 | 0.813799 | 79.164% |
| 2 | 0 | 188539.8 | 28.087% | 3.290458 | 66.169% | 0.062728 | 1.146773 | 0.262518 | 0.793188 | 75.473% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
