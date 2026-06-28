# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 18.650412 | 0.000% | 0.147255 | 5.614997 | 0.188941 | 0.826705 | 88.442% |
| 1 | 0 | 190592.3 | 30.346% | 10.586476 | 43.237% | 0.085220 | 3.459256 | 0.261457 | 0.781494 | 80.493% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
