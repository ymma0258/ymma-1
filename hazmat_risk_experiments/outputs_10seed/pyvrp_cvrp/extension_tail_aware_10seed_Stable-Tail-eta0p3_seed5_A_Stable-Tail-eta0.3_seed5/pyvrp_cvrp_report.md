# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.554593 | 0.000% | 0.212789 | 2.275586 | 0.176186 | 0.876439 | 89.143% |
| 1 | 0 | 154230.8 | 15.100% | 2.628117 | 65.212% | 0.068762 | 1.012191 | 0.314668 | 0.772608 | 73.340% |
| 2 | 0 | 164746.4 | 22.947% | 1.970027 | 73.923% | 0.042717 | 0.612143 | 0.232035 | 0.716865 | 65.388% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
