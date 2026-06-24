# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.320922 | 0.000% | 0.258919 | 3.070142 | 0.302674 | 0.867339 | 89.567% |
| 1 | 0 | 175786.5 | 19.802% | 4.160275 | 50.002% | 0.103492 | 1.466762 | 0.303273 | 0.831179 | 82.364% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
