# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 3.528162 | 0.000% | 0.094910 | 1.099075 | 0.176513 | 0.802173 | 79.477% |
| 1 | 0 | 171827.0 | 17.512% | 1.697514 | 51.887% | 0.035059 | 0.503614 | 0.204918 | 0.682366 | 62.435% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
