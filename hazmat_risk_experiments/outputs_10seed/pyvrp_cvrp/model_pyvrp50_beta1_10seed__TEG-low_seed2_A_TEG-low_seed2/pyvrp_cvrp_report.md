# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.919855 | 0.000% | 0.272365 | 2.549163 | 0.146762 | 0.845714 | 87.964% |
| 1 | 0 | 160591.9 | 19.847% | 3.597740 | 59.666% | 0.076383 | 1.189036 | 0.279900 | 0.743618 | 73.646% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
