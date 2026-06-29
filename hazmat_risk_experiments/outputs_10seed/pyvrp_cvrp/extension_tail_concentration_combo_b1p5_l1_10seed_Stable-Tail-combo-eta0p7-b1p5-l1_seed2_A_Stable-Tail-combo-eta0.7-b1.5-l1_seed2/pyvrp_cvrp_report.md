# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.698255 | 0.000% | 0.272341 | 2.457055 | 0.145302 | 0.877596 | 90.238% |
| 1.5 | 1 | 183561.7 | 36.989% | 2.731069 | 68.602% | 0.061128 | 1.582816 | 0.438528 | 0.792189 | 74.440% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
