# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.591805 | 0.000% | 0.217609 | 2.311790 | 0.176601 | 0.859143 | 88.661% |
| 1 | 0 | 157374.9 | 17.446% | 2.747660 | 63.808% | 0.071838 | 0.925646 | 0.254450 | 0.742299 | 73.559% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
