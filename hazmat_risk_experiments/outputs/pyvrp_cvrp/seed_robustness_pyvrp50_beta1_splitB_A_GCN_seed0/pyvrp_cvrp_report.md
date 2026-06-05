# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 6.902470 | 0.000% | 0.199403 | 2.335172 | 0.225989 | 0.859822 | 88.451% |
| 1 | 0 | 157005.4 | 17.170% | 2.602514 | 62.296% | 0.057335 | 0.793944 | 0.184516 | 0.763423 | 74.837% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
