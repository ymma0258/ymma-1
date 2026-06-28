# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 11.749640 | 0.000% | 0.209686 | 3.956833 | 0.224036 | 0.862752 | 89.944% |
| 1 | 0 | 179037.0 | 22.443% | 5.785074 | 50.764% | 0.110111 | 1.978076 | 0.287633 | 0.811129 | 81.702% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
