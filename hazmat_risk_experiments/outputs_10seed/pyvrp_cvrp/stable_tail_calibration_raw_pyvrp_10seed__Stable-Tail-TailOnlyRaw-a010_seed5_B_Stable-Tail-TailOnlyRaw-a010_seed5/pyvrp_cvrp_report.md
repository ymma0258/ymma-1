# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.1 | 0.000% | 8.091686 | 0.000% | 0.247425 | 2.617931 | 0.215200 | 0.877472 | 89.523% |
| 0.25 | 0 | 156601.2 | 6.389% | 7.059229 | 12.759% | 0.191346 | 2.320351 | 0.223590 | 0.874986 | 89.014% |
| 0.5 | 0 | 165596.1 | 12.500% | 5.192174 | 35.833% | 0.129243 | 1.981602 | 0.308675 | 0.851915 | 85.310% |
| 1 | 0 | 176110.5 | 19.643% | 3.600510 | 55.504% | 0.090752 | 1.293979 | 0.294100 | 0.820666 | 80.003% |
| 2 | 0 | 191547.7 | 30.130% | 2.906874 | 64.076% | 0.071281 | 0.958809 | 0.279496 | 0.800448 | 76.311% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
