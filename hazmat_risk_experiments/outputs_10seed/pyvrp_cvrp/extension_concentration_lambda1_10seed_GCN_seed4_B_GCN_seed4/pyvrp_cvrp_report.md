# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.772931 | 0.000% | 0.256644 | 3.007084 | 0.249171 | 0.861805 | 89.101% |
| 1 | 0 | 180570.7 | 23.062% | 4.474298 | 48.999% | 0.096559 | 1.581150 | 0.282718 | 0.824634 | 82.110% |
| 1 | 1 | 196988.8 | 34.252% | 3.303364 | 62.346% | 0.068411 | 1.482569 | 0.368553 | 0.784143 | 75.789% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
