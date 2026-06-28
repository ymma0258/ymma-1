# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 9.014765 | 0.000% | 0.289824 | 2.448348 | 0.147308 | 0.877403 | 90.194% |
| 1 | 0 | 158254.1 | 18.043% | 3.639975 | 59.622% | 0.102558 | 1.205768 | 0.276242 | 0.827234 | 80.416% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
