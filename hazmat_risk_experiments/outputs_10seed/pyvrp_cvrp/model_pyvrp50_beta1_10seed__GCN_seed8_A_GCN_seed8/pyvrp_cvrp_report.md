# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.925623 | 0.000% | 0.246790 | 2.316011 | 0.150048 | 0.872615 | 89.748% |
| 1 | 0 | 160243.5 | 19.587% | 3.300414 | 58.358% | 0.075381 | 1.172542 | 0.302583 | 0.809202 | 79.525% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
