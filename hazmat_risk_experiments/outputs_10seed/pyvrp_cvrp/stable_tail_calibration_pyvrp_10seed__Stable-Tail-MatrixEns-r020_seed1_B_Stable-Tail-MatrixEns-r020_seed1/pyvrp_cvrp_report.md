# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 7.821478 | 0.000% | 0.247224 | 2.715359 | 0.254425 | 0.873405 | 89.909% |
| 0.25 | 0 | 155690.5 | 5.914% | 6.295631 | 19.508% | 0.170605 | 2.022633 | 0.247596 | 0.868294 | 88.466% |
| 0.5 | 0 | 163706.0 | 11.367% | 5.680545 | 27.372% | 0.150110 | 1.679248 | 0.213946 | 0.864271 | 87.483% |
| 1 | 0 | 173186.1 | 17.816% | 3.082274 | 60.592% | 0.073239 | 1.065105 | 0.231082 | 0.812748 | 78.854% |
| 2 | 0 | 187583.9 | 27.610% | 2.703437 | 65.436% | 0.053909 | 0.919685 | 0.250237 | 0.799692 | 76.318% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
