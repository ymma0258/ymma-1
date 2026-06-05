# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.395791 | 0.000% | 0.245304 | 2.753865 | 0.219965 | 0.835537 | 86.771% |
| 1 | 0 | 175991.4 | 20.105% | 4.015772 | 52.169% | 0.080991 | 1.153723 | 0.203737 | 0.737057 | 73.869% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
