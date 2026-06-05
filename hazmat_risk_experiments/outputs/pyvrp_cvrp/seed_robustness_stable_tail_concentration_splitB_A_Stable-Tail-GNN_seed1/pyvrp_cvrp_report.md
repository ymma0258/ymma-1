# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 7.310559 | 0.000% | 0.236596 | 2.276946 | 0.185665 | 0.876530 | 89.264% |
| 1 | 0 | 155071.6 | 15.727% | 2.608679 | 64.316% | 0.059846 | 0.856802 | 0.230933 | 0.793039 | 75.633% |
| 1 | 1 | 163019.0 | 21.658% | 2.077922 | 71.576% | 0.048172 | 0.607741 | 0.215007 | 0.760112 | 70.318% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
