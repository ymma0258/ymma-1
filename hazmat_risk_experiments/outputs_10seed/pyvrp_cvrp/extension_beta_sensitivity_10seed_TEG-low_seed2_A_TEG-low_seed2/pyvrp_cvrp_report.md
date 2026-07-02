# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.919855 | 0.000% | 0.272365 | 2.549163 | 0.146762 | 0.845714 | 87.964% |
| 0.5 | 0 | 150264.3 | 12.140% | 5.330345 | 40.242% | 0.148216 | 1.854058 | 0.246829 | 0.808250 | 82.142% |
| 1 | 0 | 160591.9 | 19.847% | 3.597740 | 59.666% | 0.076383 | 1.189036 | 0.279900 | 0.743618 | 73.646% |
| 1.5 | 0 | 169025.5 | 26.141% | 3.544143 | 60.267% | 0.075535 | 1.147465 | 0.272428 | 0.739052 | 73.037% |
| 2 | 0 | 176945.9 | 32.052% | 3.398969 | 61.894% | 0.072168 | 1.115321 | 0.270063 | 0.727329 | 71.702% |
| 3 | 0 | 191907.1 | 43.217% | 3.071308 | 65.568% | 0.061643 | 1.088252 | 0.267484 | 0.704202 | 68.594% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
