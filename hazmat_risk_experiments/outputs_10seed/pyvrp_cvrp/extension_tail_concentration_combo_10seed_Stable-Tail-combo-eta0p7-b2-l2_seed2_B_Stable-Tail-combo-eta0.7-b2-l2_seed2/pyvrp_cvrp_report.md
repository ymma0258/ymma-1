# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.938070 | 0.000% | 0.305060 | 3.409897 | 0.250389 | 0.878131 | 90.980% |
| 2 | 2 | 232932.8 | 58.748% | 3.446400 | 65.321% | 0.070477 | 2.008042 | 0.473940 | 0.818609 | 77.806% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
