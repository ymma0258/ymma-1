# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 10.641821 | 0.000% | 0.261624 | 3.113351 | 0.168884 | 0.854840 | 88.738% |
| 1 | 0 | 161827.7 | 20.769% | 4.107491 | 61.402% | 0.083552 | 1.603799 | 0.292307 | 0.758744 | 75.329% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
