# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147196.9 | 0.000% | 6.066489 | 0.000% | 0.186254 | 1.905004 | 0.196875 | 0.874780 | 89.337% |
| 0.25 | 0 | 156462.0 | 6.294% | 5.276702 | 13.019% | 0.148228 | 1.652572 | 0.190789 | 0.872350 | 88.540% |
| 0.5 | 0 | 164810.7 | 11.966% | 4.082623 | 32.702% | 0.109765 | 1.381999 | 0.280927 | 0.855903 | 85.586% |
| 1 | 0 | 175563.9 | 19.271% | 2.707396 | 55.371% | 0.067534 | 1.086295 | 0.325477 | 0.819434 | 79.949% |
| 2 | 0 | 191871.1 | 30.350% | 2.280701 | 62.405% | 0.045499 | 0.962569 | 0.353982 | 0.803579 | 77.317% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
