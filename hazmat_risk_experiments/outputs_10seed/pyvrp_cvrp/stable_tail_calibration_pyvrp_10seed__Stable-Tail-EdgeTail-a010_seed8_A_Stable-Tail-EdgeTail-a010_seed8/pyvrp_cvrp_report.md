# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 8.130744 | 0.000% | 0.261073 | 2.513409 | 0.185020 | 0.867219 | 88.058% |
| 0.25 | 0 | 143441.0 | 6.729% | 5.249683 | 35.434% | 0.147930 | 1.575578 | 0.185476 | 0.853302 | 86.387% |
| 0.5 | 0 | 149712.9 | 11.395% | 4.174705 | 48.655% | 0.121970 | 1.414156 | 0.225656 | 0.835440 | 83.351% |
| 1 | 0 | 158725.9 | 18.101% | 2.773828 | 65.885% | 0.063808 | 0.813829 | 0.201733 | 0.779820 | 75.570% |
| 2 | 0 | 173851.5 | 29.356% | 2.272681 | 72.048% | 0.045859 | 0.702534 | 0.220665 | 0.745075 | 69.946% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
