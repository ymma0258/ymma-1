# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.926540 | 0.000% | 0.180369 | 2.848258 | 0.202465 | 0.874125 | 89.139% |
| 1 | 0 | 155376.7 | 15.955% | 3.048564 | 65.848% | 0.044125 | 1.194615 | 0.321862 | 0.765480 | 73.086% |
| 2 | 0 | 167741.5 | 25.183% | 2.416119 | 72.933% | 0.032861 | 0.825666 | 0.217472 | 0.714575 | 66.033% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
