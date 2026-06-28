# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 9.004061 | 0.000% | 0.281616 | 2.991333 | 0.222064 | 0.880266 | 90.037% |
| 1 | 0 | 180695.6 | 22.980% | 4.006931 | 55.499% | 0.095376 | 1.651786 | 0.357637 | 0.838126 | 81.358% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
