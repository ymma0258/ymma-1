# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.044218 | 0.000% | 0.209034 | 2.417286 | 0.224008 | 0.872567 | 88.893% |
| 1 | 0 | 174101.5 | 18.654% | 2.941825 | 58.238% | 0.073640 | 1.198657 | 0.296619 | 0.799482 | 77.337% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
