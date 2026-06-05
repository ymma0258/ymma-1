# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.4 | 0.000% | 7.236555 | 0.000% | 0.224757 | 2.418750 | 0.223692 | 0.848981 | 87.702% |
| 1 | 158131.8 | 18.011% | 2.798622 | 61.327% | 0.062095 | 0.935832 | 0.242759 | 0.729334 | 72.230% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
