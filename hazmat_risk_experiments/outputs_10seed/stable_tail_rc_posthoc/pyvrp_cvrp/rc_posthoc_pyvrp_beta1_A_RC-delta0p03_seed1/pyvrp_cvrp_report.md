# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 8.362908 | 0.000% | 0.250448 | 2.442484 | 0.171164 | 0.882027 | 90.148% |
| 1 | 0 | 155145.0 | 15.724% | 2.624473 | 68.618% | 0.059956 | 0.907594 | 0.236266 | 0.783537 | 74.543% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
