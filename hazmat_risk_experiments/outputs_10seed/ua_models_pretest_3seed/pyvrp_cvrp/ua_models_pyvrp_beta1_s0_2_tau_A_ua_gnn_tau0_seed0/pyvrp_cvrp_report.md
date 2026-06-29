# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 7.306866 | 0.000% | 0.235965 | 2.309937 | 0.183845 | 0.856700 | 88.441% |
| 1 | 0 | 158015.0 | 17.924% | 2.682270 | 63.291% | 0.066728 | 0.894355 | 0.231305 | 0.768473 | 75.700% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
