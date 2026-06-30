# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.474597 | 0.000% | 0.219416 | 2.237541 | 0.159268 | 0.884427 | 90.224% |
| 1.5 | 1 | 179346.7 | 33.843% | 2.137381 | 71.405% | 0.040173 | 0.981006 | 0.353455 | 0.769870 | 71.287% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
