# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.334988 | 0.000% | 0.256130 | 2.811929 | 0.232643 | 0.843619 | 87.121% |
| 1 | 0 | 176514.6 | 20.462% | 3.656163 | 56.135% | 0.084665 | 1.267009 | 0.227464 | 0.720005 | 71.618% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
