# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.357164 | 0.000% | 0.239110 | 2.944828 | 0.274723 | 0.883600 | 90.215% |
| 2 | 1 | 203439.1 | 38.648% | 2.492518 | 70.175% | 0.045742 | 0.896412 | 0.292694 | 0.785925 | 72.344% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
