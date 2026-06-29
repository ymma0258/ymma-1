# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.589170 | 0.000% | 0.222722 | 2.266396 | 0.158158 | 0.884091 | 90.201% |
| 1 | 0 | 158032.3 | 17.937% | 2.974379 | 60.808% | 0.073795 | 0.981430 | 0.275136 | 0.818524 | 79.208% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
