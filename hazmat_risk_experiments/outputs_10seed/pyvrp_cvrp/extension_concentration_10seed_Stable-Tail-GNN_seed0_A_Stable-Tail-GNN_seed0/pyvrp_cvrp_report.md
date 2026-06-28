# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.576641 | 0.000% | 0.242584 | 2.483964 | 0.221180 | 0.882370 | 90.311% |
| 1 | 0 | 156818.2 | 17.031% | 2.407933 | 68.219% | 0.052249 | 0.874088 | 0.254022 | 0.789544 | 75.383% |
| 1 | 0.5 | 161708.6 | 20.680% | 2.196597 | 71.008% | 0.044546 | 0.842594 | 0.297701 | 0.769723 | 72.322% |
| 1 | 1 | 164412.0 | 22.698% | 1.619176 | 78.629% | 0.027456 | 0.431433 | 0.172761 | 0.697143 | 61.953% |
| 1 | 2 | 168998.7 | 26.121% | 1.422822 | 81.221% | 0.022539 | 0.405685 | 0.165574 | 0.659327 | 56.701% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
