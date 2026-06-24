# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.642029 | 0.000% | 0.255625 | 3.196525 | 0.317628 | 0.867912 | 89.720% |
| 1 | 0 | 179293.4 | 22.192% | 4.756927 | 44.956% | 0.127015 | 1.790992 | 0.267414 | 0.841518 | 83.766% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
