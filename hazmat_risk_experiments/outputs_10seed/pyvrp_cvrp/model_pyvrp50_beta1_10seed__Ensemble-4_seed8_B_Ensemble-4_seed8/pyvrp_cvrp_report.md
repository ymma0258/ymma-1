# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.154391 | 0.000% | 0.236561 | 2.678503 | 0.215866 | 0.852073 | 87.897% |
| 1 | 0 | 179457.0 | 22.303% | 4.055053 | 50.272% | 0.090727 | 1.685594 | 0.309827 | 0.786723 | 78.680% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
