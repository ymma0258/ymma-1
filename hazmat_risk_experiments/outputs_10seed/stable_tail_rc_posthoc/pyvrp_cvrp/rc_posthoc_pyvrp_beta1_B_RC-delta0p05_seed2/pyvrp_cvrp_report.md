# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.098592 | 0.000% | 0.309973 | 3.455743 | 0.248751 | 0.877776 | 90.973% |
| 1 | 0 | 178339.1 | 21.542% | 4.693395 | 53.524% | 0.121456 | 1.737863 | 0.324433 | 0.851738 | 83.902% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
