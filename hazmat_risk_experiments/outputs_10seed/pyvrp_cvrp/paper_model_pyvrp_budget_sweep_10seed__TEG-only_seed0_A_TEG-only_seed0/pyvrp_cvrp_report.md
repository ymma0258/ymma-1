# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.4 | 0.000% | 8.733017 | 0.000% | 0.273982 | 2.878034 | 0.208026 | 0.847891 | 87.464% |
| 0.25 | 0 | 143562.5 | 6.978% | 5.711501 | 34.599% | 0.153715 | 1.854569 | 0.217082 | 0.814509 | 83.227% |
| 0.5 | 0 | 150198.7 | 11.923% | 4.606157 | 47.256% | 0.126501 | 1.850233 | 0.308840 | 0.784287 | 79.567% |
| 1 | 0 | 159992.0 | 19.220% | 3.283811 | 62.398% | 0.066209 | 1.150741 | 0.248529 | 0.716388 | 71.247% |
| 2 | 0 | 174741.6 | 30.211% | 2.390976 | 72.621% | 0.038062 | 0.776135 | 0.229418 | 0.624220 | 59.979% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
