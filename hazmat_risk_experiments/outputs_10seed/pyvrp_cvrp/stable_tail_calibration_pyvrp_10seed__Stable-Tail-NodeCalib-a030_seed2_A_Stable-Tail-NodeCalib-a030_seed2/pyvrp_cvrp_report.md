# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.840235 | 0.000% | 0.285421 | 2.575991 | 0.170476 | 0.877360 | 89.773% |
| 0.25 | 0 | 142291.9 | 6.190% | 5.846985 | 33.859% | 0.169843 | 2.076070 | 0.289501 | 0.866025 | 87.775% |
| 0.5 | 0 | 148301.8 | 10.675% | 4.684978 | 47.004% | 0.126220 | 1.568862 | 0.231341 | 0.853301 | 85.238% |
| 1 | 0 | 157370.8 | 17.443% | 3.383044 | 61.731% | 0.086701 | 1.198668 | 0.296093 | 0.817280 | 79.810% |
| 2 | 0 | 171306.1 | 27.842% | 2.894033 | 67.263% | 0.063724 | 1.258352 | 0.352410 | 0.796397 | 76.449% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
