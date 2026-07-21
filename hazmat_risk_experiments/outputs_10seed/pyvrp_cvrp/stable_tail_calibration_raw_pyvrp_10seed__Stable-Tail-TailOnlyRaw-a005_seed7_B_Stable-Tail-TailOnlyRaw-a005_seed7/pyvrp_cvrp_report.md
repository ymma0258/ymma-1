# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.6 | 0.000% | 9.980292 | 0.000% | 0.300931 | 3.084756 | 0.195333 | 0.879576 | 90.567% |
| 0.25 | 0 | 158097.6 | 7.308% | 7.868634 | 21.158% | 0.224037 | 2.605631 | 0.241978 | 0.874036 | 89.157% |
| 0.5 | 0 | 167320.9 | 13.568% | 6.373060 | 36.144% | 0.174948 | 2.425357 | 0.295440 | 0.861834 | 86.609% |
| 1 | 0 | 178781.5 | 21.347% | 3.882192 | 61.101% | 0.097956 | 1.294916 | 0.258690 | 0.828403 | 80.016% |
| 2 | 0 | 196068.9 | 33.081% | 3.461198 | 65.320% | 0.080287 | 1.105570 | 0.228477 | 0.813056 | 77.667% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
