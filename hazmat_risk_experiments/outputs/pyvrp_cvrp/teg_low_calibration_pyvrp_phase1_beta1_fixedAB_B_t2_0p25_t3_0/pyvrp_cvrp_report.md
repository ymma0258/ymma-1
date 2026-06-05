# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.560660 | 0.000% | 0.231142 | 2.867425 | 0.229006 | 0.844356 | 87.380% |
| 1 | 0 | 177082.6 | 20.850% | 3.879093 | 54.687% | 0.084991 | 1.250627 | 0.219605 | 0.732562 | 73.111% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
