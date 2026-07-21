# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 8.926790 | 0.000% | 0.274936 | 2.438836 | 0.146991 | 0.879459 | 90.327% |
| 0.25 | 0 | 143064.7 | 6.713% | 7.019111 | 21.370% | 0.224531 | 2.140742 | 0.232526 | 0.875321 | 89.335% |
| 0.5 | 0 | 149928.4 | 11.833% | 5.125952 | 42.578% | 0.135616 | 1.723056 | 0.244661 | 0.857116 | 86.181% |
| 1 | 0 | 159610.4 | 19.055% | 3.609548 | 59.565% | 0.080901 | 1.345712 | 0.328418 | 0.818291 | 80.453% |
| 2 | 0 | 174494.0 | 30.157% | 2.900065 | 67.513% | 0.063373 | 1.060738 | 0.331634 | 0.793325 | 76.363% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
