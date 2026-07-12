# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134065.1 | 0.000% | 8.057549 | 0.000% | 0.252784 | 2.445517 | 0.210746 | 0.876231 | 89.408% |
| 0.25 | 0 | 143363.6 | 6.936% | 6.554747 | 18.651% | 0.189341 | 2.101056 | 0.255769 | 0.869509 | 87.911% |
| 0.5 | 0 | 150751.0 | 12.446% | 4.486646 | 44.317% | 0.125959 | 1.763082 | 0.293016 | 0.837440 | 82.828% |
| 1 | 0 | 160513.5 | 19.728% | 3.659450 | 54.584% | 0.088440 | 1.241189 | 0.279318 | 0.812731 | 79.072% |
| 2 | 0 | 176173.0 | 31.409% | 2.322936 | 71.171% | 0.047284 | 1.088972 | 0.352900 | 0.739549 | 67.962% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
