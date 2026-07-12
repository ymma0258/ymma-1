# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.0 | 0.000% | 8.377687 | 0.000% | 0.252208 | 2.490394 | 0.188024 | 0.879675 | 87.912% |
| 0.25 | 0 | 155143.5 | 5.256% | 6.707437 | 19.937% | 0.195994 | 2.248763 | 0.247882 | 0.867520 | 85.374% |
| 0.5 | 0 | 161725.7 | 9.721% | 5.341651 | 36.240% | 0.147559 | 1.775705 | 0.268357 | 0.848535 | 81.827% |
| 1 | 0 | 169580.7 | 15.050% | 3.232168 | 61.419% | 0.068914 | 1.448929 | 0.320128 | 0.782835 | 71.261% |
| 2 | 0 | 182198.9 | 23.611% | 2.885164 | 65.561% | 0.056844 | 1.358341 | 0.335015 | 0.768508 | 69.031% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
