# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.335510 | 0.000% | 0.211857 | 2.218565 | 0.178233 | 0.866917 | 88.652% |
| 1 | 0 | 157163.6 | 17.288% | 2.870133 | 60.873% | 0.072765 | 0.900571 | 0.223890 | 0.782043 | 76.271% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
