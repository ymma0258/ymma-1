# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.595173 | 0.000% | 0.233970 | 2.406448 | 0.196804 | 0.863354 | 88.677% |
| 1 | 0 | 158219.2 | 18.076% | 2.802832 | 63.097% | 0.063752 | 0.923090 | 0.224491 | 0.763825 | 74.946% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
