# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 13.152528 | 0.000% | 0.319082 | 3.607889 | 0.126461 | 0.833551 | 87.491% |
| 1 | 0 | 163198.0 | 21.792% | 5.646488 | 57.069% | 0.099168 | 2.011754 | 0.270713 | 0.754764 | 76.158% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
