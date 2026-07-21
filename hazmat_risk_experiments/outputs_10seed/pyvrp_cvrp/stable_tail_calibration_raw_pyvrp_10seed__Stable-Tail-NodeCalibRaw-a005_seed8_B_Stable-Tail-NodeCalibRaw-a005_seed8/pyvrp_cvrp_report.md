# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.4 | 0.000% | 7.424448 | 0.000% | 0.217301 | 2.241743 | 0.192615 | 0.860325 | 87.701% |
| 0.25 | 0 | 156589.8 | 6.285% | 6.123237 | 17.526% | 0.142373 | 2.018901 | 0.218958 | 0.852737 | 86.496% |
| 0.5 | 0 | 165309.2 | 12.203% | 4.992632 | 32.754% | 0.123007 | 1.641151 | 0.225869 | 0.840037 | 84.044% |
| 1 | 0 | 175988.2 | 19.451% | 2.994075 | 59.673% | 0.072262 | 1.011997 | 0.231594 | 0.781323 | 75.158% |
| 2 | 0 | 190851.2 | 29.540% | 2.477383 | 66.632% | 0.054429 | 0.693085 | 0.184960 | 0.752863 | 70.743% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
