# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 7.653455 | 0.000% | 0.224502 | 2.257226 | 0.167495 | 0.867423 | 88.371% |
| 0.25 | 0 | 143038.8 | 6.747% | 5.003224 | 34.628% | 0.145287 | 1.687806 | 0.248365 | 0.850501 | 85.588% |
| 0.5 | 0 | 149487.9 | 11.560% | 4.186469 | 45.300% | 0.119876 | 1.580483 | 0.261618 | 0.833682 | 83.268% |
| 1 | 0 | 158407.0 | 18.216% | 2.869763 | 62.504% | 0.063593 | 0.836294 | 0.167912 | 0.785294 | 76.240% |
| 2 | 0 | 173438.7 | 29.434% | 2.357095 | 69.202% | 0.049311 | 0.738907 | 0.213389 | 0.755670 | 71.392% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
