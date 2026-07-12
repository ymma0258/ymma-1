# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.4 | 0.000% | 7.567833 | 0.000% | 0.215359 | 2.510345 | 0.229064 | 0.863890 | 88.195% |
| 0.25 | 0 | 156761.3 | 6.497% | 6.669845 | 11.866% | 0.182018 | 2.160401 | 0.203025 | 0.860066 | 87.568% |
| 0.5 | 0 | 166159.4 | 12.882% | 5.387528 | 28.810% | 0.136056 | 1.565858 | 0.169496 | 0.848497 | 85.275% |
| 1 | 0 | 179299.8 | 21.809% | 3.677330 | 51.408% | 0.088952 | 1.111793 | 0.226384 | 0.814332 | 79.597% |
| 2 | 0 | 197636.6 | 34.266% | 2.996562 | 60.404% | 0.067787 | 0.982556 | 0.252949 | 0.792529 | 75.882% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
