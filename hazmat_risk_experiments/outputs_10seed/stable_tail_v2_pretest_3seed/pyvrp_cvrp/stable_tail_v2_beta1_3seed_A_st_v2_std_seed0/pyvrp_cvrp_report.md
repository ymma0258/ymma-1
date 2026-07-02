# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 3.233942 | 0.000% | 0.082477 | 0.890506 | 0.161332 | 0.762161 | 75.369% |
| 1 | 0 | 162533.7 | 21.296% | 1.588583 | 50.878% | 0.028588 | 0.525859 | 0.200060 | 0.608250 | 55.315% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
