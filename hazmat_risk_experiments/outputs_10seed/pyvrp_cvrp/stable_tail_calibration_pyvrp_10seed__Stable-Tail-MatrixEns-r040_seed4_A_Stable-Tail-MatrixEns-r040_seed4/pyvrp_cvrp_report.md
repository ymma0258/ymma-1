# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 5.434640 | 0.000% | 0.167503 | 1.529646 | 0.154368 | 0.880483 | 90.422% |
| 0.25 | 0 | 143007.2 | 6.723% | 4.233124 | 22.108% | 0.134446 | 1.306842 | 0.226056 | 0.874284 | 89.213% |
| 0.5 | 0 | 149730.9 | 11.741% | 3.166785 | 41.730% | 0.098058 | 1.021961 | 0.242347 | 0.858795 | 86.402% |
| 1 | 0 | 159030.0 | 18.681% | 2.152155 | 60.399% | 0.056066 | 0.814793 | 0.330900 | 0.819587 | 80.559% |
| 2 | 0 | 173711.2 | 29.637% | 1.746851 | 67.857% | 0.042261 | 0.639540 | 0.347963 | 0.795634 | 76.756% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
